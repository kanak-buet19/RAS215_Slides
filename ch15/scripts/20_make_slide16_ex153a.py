"""Slide 16 - Example 15.3 (1/2): T-beam, check bending and shear (Hibbeler 6th ed., p. 696-697, Fig. 15-9).

  reactions: sum M_B: R_D(4) - 0.5(2)(1) - 1.5(2) = 0 -> R_D = 1 kN;  R_B = 0.5(2) + 1.5 - 1 = 1.5 kN
  V_max = 1.5 kN; M_max = M_C = 1.5(2) - 0.5(2)(1) = 2 kN.m
  y_bar = [0.1(0.03)(0.2) + 0.215(0.03)(0.2)] / [2(0.03)(0.2)] = 0.1575 m;  each board's centroid is 0.0575 m from the N.A.
  I = [1/12(0.03)(0.2)^3 + 0.006(0.0575)^2] + [1/12(0.2)(0.03)^3 + 0.006(0.0575)^2] = 60.125(10^-6) m^4
  sigma = 2(10^3)(0.1575)/60.125(10^-6) = 5.24 MPa <= 12 MPa OK   (c = 0.1575 m, not 0.0725 m)
  Q = (0.1575/2)(0.1575)(0.03) = 0.372(10^-3) m^3 (web below the N.A.);  tau = 1.5(10^3)(0.372(10^-3))/(60.125(10^-6)(0.03)) = 309 kPa OK
The reactions/V/M working is mine (the book only states the results).
Clicks: 1 problem, beam, section with dimensions; 2 supports -> reactions; 3 V and M; 4 N.A. and I;
5 bending (c marked, sigma bar); 6 shear (area for Q shaded, tau bar).

Writes ../slides/separate/16_slide16_ex153a.html.
Run:  python3 20_make_slide16_ex153a.py
"""
import importlib

c = importlib.import_module("19_ex153_common")
lib, NAVY, RED, GREY, TAU, MC, sym, X, BY = c.lib, c.NAVY, c.RED, c.GREY, c.TAU, c.MC, c.sym, c.X, c.BY
m, ds, U, P, E, IMP = c.m, c.ds, c.U, c.P, c.E, c.IMP

VB, VS = 212, 34                 # V baseline, px per kN
MB, MS = 334, 30                 # M baseline, px per kN.m
K = 600                          # section, px per m
CX, YB = 170, 168                # section centre, bottom of the web


def beam_svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY)}</defs><g data-step="1">' + c.beam() + '</g>'
    s += '<g data-step="2">' + c.reactions(2) + '</g>'
    s += '<g data-step="3">' + c.v_diagram(VB, VS) + c.m_diagram(MB, MS)
    s += (f'<text x="{X(2)}" y="{MB - MS * 2 - 8}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="middle">2 = {sym("M", "max")}</text>'
          f'<text x="{X(0) + 34}" y="{VB - VS * 1.5 - 6}" font-size="15" fill="{RED}" font-weight="bold">= {sym("V", "max")}</text></g>')
    return f'<svg class="fig" style="left:40px; top:164px" width="620" height="350" viewBox="0 0 620 350">{s}</svg>'


def section_svg():
    sec, y = c.tsec(CX, YB, K)
    fl, fr, wl, wr = CX - 0.1 * K, CX + 0.1 * K, CX - 0.015 * K, CX + 0.015 * K
    dim = lambda x1, y1, x2, y2: (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#000" stroke-width="1.1" '
                                  'marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>')
    s = f'<defs>{lib.markers(GREY, RED)}</defs><g data-step="1">' + sec
    s += dim(fl, y["top"] - 9, fr, y["top"] - 9) + f'<text x="{CX}" y="{y["top"] - 14:.1f}" font-size="14" text-anchor="middle">200 mm</text>'
    s += dim(fl - 10, y["top"], fl - 10, y["fb"]) + f'<text x="{fl - 16:.1f}" y="{y["fb"] - 3:.1f}" font-size="14" text-anchor="end">30 mm</text>'
    s += dim(wr + 26, y["fb"], wr + 26, YB) + f'<text x="{wr + 32:.1f}" y="{(y["fb"] + YB) / 2 + 5:.1f}" font-size="14">200 mm</text>'
    s += f'<text x="{CX}" y="{YB + 16}" font-size="14" text-anchor="middle">30 mm</text>'
    s += '</g>'
    # click 4: neutral axis
    s += (f'<g data-step="4"><line x1="{fl - 34:.1f}" y1="{y["na"]:.1f}" x2="{fr + 30:.1f}" y2="{y["na"]:.1f}" stroke="{NAVY}" stroke-width="1.4" stroke-dasharray="8 4"/>'
          f'<text x="{fr + 34:.1f}" y="{y["na"] + 5:.1f}" font-size="14" fill="{NAVY}" font-weight="bold">N.A.</text>'
          + dim(wl - 22, y["na"], wl - 22, YB)
          + f'<text x="{wl - 28:.1f}" y="{(y["na"] + YB) / 2:.1f}" font-size="15" text-anchor="end">{sym("ȳ")} = 157.5 mm</text></g>')
    # click 5: c = y_bar (bottom fibre farthest); click 6: area used for Q
    s += f'<text data-step="5" x="{wl - 28:.1f}" y="{(y["na"] + YB) / 2 + 19:.1f}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="end">= {sym("c")}</text>'
    s += (f'<g data-step="6"><rect x="{wl:.1f}" y="{y["na"]:.1f}" width="{wr - wl:.1f}" height="{YB - y["na"]:.1f}" fill="{TAU}" fill-opacity="0.55"/>'
          f'<text x="{wr + 4:.1f}" y="{YB - 6:.1f}" font-size="14" fill="{TAU}" font-weight="bold">{sym("A")}′</text></g>')
    # bars: stress / allowable, both allowables on one line
    bb, H = YB, 120
    for n, (bx, val, allow, lab, unit, step) in enumerate(((400, 5.24, 12, "σ", "MPa", 5), (510, 309, 800, "τ", "kPa", 6))):
        s += (f'<g data-step="{step}"><line x1="{bx - 20}" y1="{bb}" x2="{bx + 64}" y2="{bb}" stroke="#000" stroke-width="1.2"/>'
              f'<rect id="bar{n}" x="{bx}" width="44" fill="{TAU}"/>'
              f'<line x1="{bx - 12}" y1="{bb - H}" x2="{bx + 56}" y2="{bb - H}" stroke="{RED}" stroke-width="2.2" stroke-dasharray="7 4"/>'
              f'<text x="{bx + 22}" y="{bb - H - 8}" font-size="14" fill="{RED}" text-anchor="middle">allow {allow} {unit}</text>'
              f'<text id="bv{n}" x="{bx + 22}" font-size="15" fill="{TAU}" font-weight="bold" text-anchor="middle">{val:g} {unit}</text>'
              f'<text x="{bx + 22}" y="{bb + 18}" font-size="15" text-anchor="middle">{sym(lab, "max")}</text></g>')
    return f'<svg class="fig" style="left:40px; top:506px" width="620" height="190" viewBox="0 0 620 190">{s}</svg>'


def build():
    SALL, TALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>", "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
    SMAX, TMAX = "<msub><mi>σ</mi><mtext>max</mtext></msub>", "<msub><mi>τ</mi><mtext>max</mtext></msub>"
    VMAX, MMAX = "<msub><mi>V</mi><mtext>max</mtext></msub>", "<msub><mi>M</mi><mtext>max</mtext></msub>"
    RB, RD = "<msub><mi>R</mi><mrow><mi>B</mi><mi>y</mi></mrow></msub>", "<msub><mi>R</mi><mrow><mi>D</mi><mi>y</mi></mrow></msub>"
    YB_ = "<mover><mi>y</mi><mo>‾</mo></mover>"
    YT = "<mover><mi>y</mi><mo>~</mo></mover>"
    SM = "<mo>∑</mo>"
    right = f"""
  <div class="given" data-step="1"><span class="gh">Problem</span>&nbsp; A wooden T-beam is made from two 200 mm × 30 mm boards (Fig. 15-9).
    {m(SALL + '<mo>=</mo><mn>12</mn>' + U('MPa'))}, {m(TALL + '<mo>=</mo><mn>800</mn>' + U('kPa'))}.
    <span class="gf"><b>Find:</b> can it carry the loads?</span></div>
  <div class="steps">
  <div class="step" data-step="2"><span class="no">1</span><b>Reactions, <i>V</i> and <i>M</i></b>
    <div class="row"><span class="tag calc">Solve</span>{m(SM + '<msub><mi>M</mi><mi>B</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.3em"/>' + RD + P('<mn>4</mn>') + '<mo>−</mo><mn>0.5</mn>' + P('<mn>2</mn>') + P('<mn>1</mn>') + '<mo>−</mo><mn>1.5</mn>' + P('<mn>2</mn>') + '<mo>=</mo><mn>0</mn>' + IMP + RD + '<mo>=</mo><mn>1</mn>' + U('kN'))}</div>
    <div class="row"><span class="tag calc"></span>{m('<mo>∑</mo><msub><mi>F</mi><mi>x</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.3em"/><msub><mi>R</mi><mrow><mi>B</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mspace width="0.6em"/>' + SM + '<msub><mi>F</mi><mi>y</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.3em"/>' + RB + '<mo>=</mo><mn>1</mn><mo>+</mo><mn>1.5</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>1.5</mn>' + U('kN'))}</div>
    <div class="row" data-step="3"><span class="tag calc">Read</span>{m(VMAX + '<mo>=</mo><mn>1.5</mn>' + U('kN') + '<mo>,</mo><mspace width="0.6em"/>' + MMAX + '<mo>=</mo><msub><mi>M</mi><mi>C</mi></msub><mo>=</mo><mn>1.5</mn>' + P('<mn>2</mn>') + '<mo>−</mo><mn>1</mn>' + P('<mn>1</mn>') + '<mo>=</mo><mn>2</mn>' + U('kN·m'))}</div></div>
  <div class="step" data-step="4"><span class="no">2</span><b>Section</b> <span class="si">(m; {m(YB_)} from the bottom)</span>
    <div class="row"><span class="tag calc">Compute</span>{ds(YB_ + '<mo>=</mo><mfrac><mrow>' + SM + YT + '<mi>A</mi></mrow><mrow>' + SM + '<mi>A</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>0.1</mn>' + P('<mn>0.006</mn>') + '<mo>+</mo><mn>0.215</mn>' + P('<mn>0.006</mn>') + '</mrow><mrow><mn>0.006</mn><mo>+</mo><mn>0.006</mn></mrow></mfrac><mo>=</mo><mn>0.1575</mn>' + U('m'))}</div>
    <div class="row"><span class="tag calc">Compute</span>{ds('<mi>I</mi><mo>=</mo>' + SM + P('<mfrac><mn>1</mn><mn>12</mn></mfrac><mi>b</mi><msup><mi>h</mi><mn>3</mn></msup><mo>+</mo><mi>A</mi><msup><mi>d</mi><mn>2</mn></msup>') + '<mo>=</mo><mn>60.125</mn>' + E('−6') + U('m⁴'))}</div>
    <div class="cap">each board: {m('<mi>A</mi><mo>=</mo><mn>0.006</mn>' + U('m²'))}, centroid {m('<mi>d</mi><mo>=</mo><mn>0.0575</mn>' + U('m'))} from the N.A.</div></div>
  <div class="step" data-step="5"><span class="no">3</span><b>Bending</b>
    <div class="row"><span class="tag calc">Compute</span>{ds(SMAX + '<mo>=</mo><mfrac><mrow>' + MMAX + '<mi>c</mi></mrow><mi>I</mi></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn>' + E(3) + P('<mn>0.1575</mn>') + '</mrow><mrow><mn>60.125</mn>' + E('−6') + '</mrow></mfrac><mo>=</mo><mn>5.24</mn>' + U('MPa'))}</div>
    <div class="row"><span class="tag req">Check</span>{m(SMAX + '<mo>≤</mo>' + SALL + '<mo>:</mo><mspace width="0.4em"/><mn>5.24</mn><mo>≤</mo><mn>12</mn>' + U('MPa'))}<span class="ok">OK</span></div>
    <div class="cap">{m('<mi>c</mi><mo>=</mo><mn>0.1575</mn>' + U('m'))}, not 0.0725 m: the bottom fibre is farthest from the N.A.</div></div>
  <div class="step" data-step="6"><span class="no">4</span><b>Shear</b> (largest at the N.A., where {m('<mi>t</mi><mo>=</mo><mn>0.03</mn>' + U('m'))})
    <div class="row"><span class="tag calc">Compute</span>{ds('<mi>Q</mi><mo>=</mo><msup><mover><mi>y</mi><mo>‾</mo></mover><mo>′</mo></msup><msup><mi>A</mi><mo>′</mo></msup><mo>=</mo>' + P('<mfrac><mn>0.1575</mn><mn>2</mn></mfrac>') + P('<mn>0.1575</mn>') + P('<mn>0.03</mn>') + '<mo>=</mo><mn>0.372</mn>' + E('−3') + U('m³'))}</div>
    <div class="cap"><i>Q</i>: first moment of <i>A</i>′ (area beyond the line) about the N.A.</div>
    <div class="row"><span class="tag calc">Compute</span>{ds(TMAX + '<mo>=</mo><mfrac><mrow>' + VMAX + '<mi>Q</mi></mrow><mrow><mi>I</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1.5</mn>' + E(3) + P('<mn>0.372</mn>' + E('−3')) + '</mrow><mrow><mn>60.125</mn>' + E('−6') + P('<mn>0.03</mn>') + '</mrow></mfrac><mo>=</mo><mn>309</mn>' + U('kPa'))}</div>
    <div class="row"><span class="tag req">Check</span>{m(TMAX + '<mo>≤</mo>' + TALL + '<mo>:</mo><mspace width="0.4em"/><mn>309</mn><mo>≤</mo><mn>800</mn>' + U('kPa'))}<span class="ok">OK</span></div></div>
  </div>"""

    js = "<script>\n" + lib.ELASTIC_JS + """
(() => {
  const $ = id => document.getElementById(id);
  const bars = [[revealClock(5), 5.24 / 12], [revealClock(6), 309 / 800]];
  function draw() {
    bars.forEach(([clk, f], n) => {
      const g = smooth(Math.min(1, Math.max(0, (clk() - 0.3) / 1.2))), h = 120 * f * g;
      $('bar' + n).setAttribute('y', (%BB% - h).toFixed(1)); $('bar' + n).setAttribute('height', h.toFixed(1));
      $('bv' + n).setAttribute('y', (%BB% - h - 6).toFixed(1)); $('bv' + n).setAttribute('opacity', g.toFixed(2));
    });
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
  // supports are replaced by the reactions on click 2
  addEventListener('buildstep', e => { $('sup').style.opacity = e.detail.k >= 2 ? 0 : 1; });
})();
</script>""".replace("%BB%", str(YB))
    title = 'Example 15.3 (1/2): is the T-beam <span class="key">strong</span> enough?'
    body = beam_svg() + "\n" + section_svg() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.3, pp. 696–697, Fig. 15-9. Intermediate steps for the reactions added; results as in the text.</div>')
    lib.write_page("16_slide16_ex153a.html", "Slide 16 - Example 15.3 checks", title, body, 16, c.STEP_CSS)
    yb = (0.1 * 0.006 + 0.215 * 0.006) / 0.012
    I = 0.03 * 0.2 ** 3 / 12 + 0.006 * (yb - 0.1) ** 2 + 0.2 * 0.03 ** 3 / 12 + 0.006 * (0.215 - yb) ** 2
    Q = yb / 2 * yb * 0.03
    print(f"check: M_C = {c.M_at(2):.3f}, ybar = {yb:.4f}, I = {I * 1e6:.3f}e-6, sigma = {2e3 * yb / I / 1e6:.2f} MPa,"
          f" Q = {Q * 1e3:.4f}e-3, tau = {1.5e3 * Q / (I * 0.03) / 1e3:.0f} kPa")


if __name__ == "__main__":
    build()
