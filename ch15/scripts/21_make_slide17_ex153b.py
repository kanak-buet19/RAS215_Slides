"""Slide 17 - Example 15.3 (2/2): nail spacing (Hibbeler 6th ed., p. 697, Fig. 15-9d).

  Q (flange) = y'A' = (0.0725 - 0.015)(0.2)(0.03) = 0.345(10^-3) m^3
  V = 1.5 kN in B-C, 1 kN in C-D (the largest V in each region, conservative)
  q_BC = 1.5(10^3)(0.345(10^-3))/60.125(10^-6) = 8.61 kN/m;  q_CD = 1(10^3)(...)/... = 5.74 kN/m
  s = F/q with F = 1.50 kN: s_BC = 0.174 m, s_CD = 0.261 m -> use 150 mm and 250 mm
Clicks: 1 problem + why nails (boards slide apart without them, one-shot animation); 2 Q of the flange
(flange shaded on the section); 3 q per region (V used in each region marked); 4 spacing, nails drawn to
scale on the beam, answer.
The slip sketch is my illustration (not from the book).

Writes ../slides/separate/17_slide17_ex153b.html.
Run:  python3 21_make_slide17_ex153b.py
"""
import importlib

c = importlib.import_module("19_ex153_common")
lib, NAVY, RED, GREY, TAU, WOOD, sym, X, BY, FT = c.lib, c.NAVY, c.RED, c.GREY, c.TAU, c.WOOD, c.sym, c.X, c.BY, c.FT
m, ds, U, P, E, IMP = c.m, c.ds, c.U, c.P, c.E, c.IMP

VB, VS = 214, 34
K = 520
CX, YB = 470, 160


BF, TF, TW, HW = 54, 10, 14, 40     # 3-D sketch: flange width/thickness, web width/height (px, not to scale)
LX, LY = 74, -34                    # oblique direction of the beam length
F_TOP, F_SIDE, W_FRONT, W_TOP, W_SIDE = "#efd8ad", "#c9a46a", "#d6b27a", "#c7a06a", "#b08a55"


def poly(pts, fill):
    return (f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" '
            f'stroke="{WOOD["edge"]}" stroke-width="1.2" stroke-linejoin="round"/>')


def tbeam3d(ox, oy, gid=None, nails=False):
    """Short piece of the T-beam in oblique view: the T is the front end face, the length runs up-right.
    ox, oy = top-left corner of the flange's front face. gid: id of the flange group (moved by the JS)."""
    wl, wr, wy = ox + BF / 2 - TW / 2, ox + BF / 2 + TW / 2, oy + TF
    s = (poly([(wr, wy), (wr + LX, wy + LY), (wr + LX, wy + HW + LY), (wr, wy + HW)], W_SIDE)
         + poly([(wl, wy), (wr, wy), (wr + LX, wy + LY), (wl + LX, wy + LY)], W_TOP)
         + f'<rect x="{wl}" y="{wy}" width="{TW}" height="{HW}" fill="{W_FRONT}" stroke="{WOOD["edge"]}" stroke-width="1.2"/>')
    f = (poly([(ox, oy), (ox + BF, oy), (ox + BF + LX, oy + LY), (ox + LX, oy + LY)], F_TOP)
         + poly([(ox + BF, oy), (ox + BF + LX, oy + LY), (ox + BF + LX, oy + TF + LY), (ox + BF, oy + TF)], F_SIDE)
         + f'<rect x="{ox}" y="{oy}" width="{BF}" height="{TF}" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.2"/>')
    if nails:                                   # nail heads along the flange centre line, driven into the web
        for t in (0.15, 0.38, 0.62, 0.85):
            x, y = ox + BF / 2 + t * LX, oy + t * LY
            f += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="3.2" ry="1.8" fill="#333"/>'
    s += f'<g id="{gid}">{f}</g>' if gid else f
    return s


def top_svg():
    """Left: a short piece of the same T-beam in 3-D. Without nails the flange slides along the web
    (JS moves it, one shot); nailed, the nails go through the flange into the web. Right: section with A'."""
    s = f'<defs>{lib.markers(GREY, RED, NAVY)}</defs><g data-step="1">'
    s += tbeam3d(84, 72, gid="flslip")
    s += (f'<text x="56" y="81" font-size="13" fill="{NAVY}" font-weight="bold" text-anchor="end">flange</text>'
          f'<text x="{84 + BF / 2 - TW / 2 - 6}" y="112" font-size="13" fill="{NAVY}" font-weight="bold" text-anchor="end">web</text>')
    s += (f'<g id="sliparr" opacity="0"><line x1="{84 + BF + LX + 8}" y1="{72 + LY - 2}" x2="{84 + BF + LX * 0.55 + 8}" y2="{72 + LY * 0.55 - 2}" '
          f'stroke="{RED}" stroke-width="2.2" marker-end="url(#a_C00000)"/>'
          f'<text x="{84 + BF + LX + 12}" y="{72 + LY + 2}" font-size="13" fill="{RED}" font-weight="bold">slides</text></g>')
    s += tbeam3d(252, 72, nails=True)
    s += (f'<text x="116" y="150" font-size="14" fill="{GREY}" text-anchor="middle">no nails: flange slides</text>'
          f'<text x="116" y="166" font-size="14" fill="{GREY}" text-anchor="middle">along the web</text>'
          f'<text x="296" y="150" font-size="14" fill="{GREY}" text-anchor="middle">nailed: they act as</text>'
          f'<text x="296" y="166" font-size="14" fill="{GREY}" text-anchor="middle">one T-beam</text>')
    s += '</g>'
    sec, y = c.tsec(CX, YB, K)
    fl, fr, wr = CX - 0.1 * K, CX + 0.1 * K, CX + 0.015 * K
    s += f'<g data-step="2">{sec}'
    s += f'<rect x="{fl:.1f}" y="{y["top"]:.1f}" width="{fr - fl:.1f}" height="{y["fb"] - y["top"]:.1f}" fill="{TAU}" fill-opacity="0.55" stroke="{c.WOOD["edge"]}" stroke-width="1.6"/>'
    yc = (y["top"] + y["fb"]) / 2
    # centroid of A' (flange mid-height): thin dashed line out to the y-bar' dimension (no dot: it read as a hole)
    s += f'<line x1="{fl + 3:.1f}" y1="{yc:.1f}" x2="{fr + 16:.1f}" y2="{yc:.1f}" stroke="#000" stroke-width="0.9" stroke-dasharray="4 3"/>'
    s += (f'<line x1="{fl - 30:.1f}" y1="{y["na"]:.1f}" x2="{fr + 24:.1f}" y2="{y["na"]:.1f}" stroke="{NAVY}" stroke-width="1.4" stroke-dasharray="8 4"/>'
          f'<text x="{fr + 28:.1f}" y="{y["na"] + 17:.1f}" font-size="14" fill="{NAVY}" font-weight="bold">N.A.</text>')
    s += (f'<line x1="{fr + 12:.1f}" y1="{yc:.1f}" x2="{fr + 12:.1f}" y2="{y["na"]:.1f}" stroke="#000" stroke-width="1.1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
          f'<text x="{fr + 18:.1f}" y="{(yc + y["na"]) / 2 + 2:.1f}" font-size="14">{sym("ȳ")}′ = 57.5 mm</text>'
          f'<text x="{CX}" y="{y["top"] - 8:.1f}" font-size="15" fill="{TAU}" font-weight="bold" text-anchor="middle">{sym("A")}′ = flange</text>'
          f'<text x="{CX}" y="{YB + 18}" font-size="13" fill="{GREY}" text-anchor="middle">nails cross this joint</text>'
          f'<line x1="{fl - 4:.1f}" y1="{y["fb"]:.1f}" x2="{fr + 4:.1f}" y2="{y["fb"]:.1f}" stroke="{RED}" stroke-width="2.4"/></g>')
    return f'<svg class="fig" style="left:40px; top:160px" width="620" height="180" viewBox="0 0 620 180">{s}</svg>'


def beam_svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY)}</defs><g data-step="1">' + c.beam() + c.v_diagram(VB, VS) + '</g>'
    # click 3: the V used in each region
    s += (f'<g data-step="3"><line x1="{X(0)}" y1="{VB - VS * 1.5}" x2="{X(2)}" y2="{VB - VS * 1.5}" stroke="{RED}" stroke-width="2" stroke-dasharray="6 4"/>'
          f'<text x="{X(0.85)}" y="{VB - VS * 0.45}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="middle">B–C: use {sym("V")} = 1.5 kN</text>'
          f'<text x="{X(3)}" y="{VB + VS * 0.6}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="middle">C–D: use {sym("V")} = 1 kN</text></g>')
    # click 4: nails to scale, 150 mm in B-C and 250 mm in C-D
    g = '<g data-step="4">'
    for a, b, sp in ((0, 2, 0.15), (2, 4, 0.25)):
        n = int(round((b - a) / sp))
        for i in range(n):
            xn = X(a + sp * (i + 0.5))
            g += (f'<line x1="{xn:.1f}" y1="{BY - 1}" x2="{xn:.1f}" y2="{BY + FT + 6}" stroke="#222" stroke-width="1.6"/>'
                  f'<line x1="{xn - 2.5:.1f}" y1="{BY - 1}" x2="{xn + 2.5:.1f}" y2="{BY - 1}" stroke="#222" stroke-width="2"/>')
    g += (f'<text x="{X(1)}" y="{BY + 62}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="middle">nails @ 150 mm</text>'
          f'<text x="{X(3)}" y="{BY + 62}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="middle">nails @ 250 mm</text>')
    s += g + '</g>'
    return f'<svg class="fig" style="left:40px; top:352px" width="620" height="280" viewBox="0 0 620 280">{s}</svg>'


def build():
    QQ = "<mi>Q</mi>"
    I_ = "<mn>60.125</mn>" + E("−6")
    q = lambda r: f"<msub><mi>q</mi><mtext>{r}</mtext></msub>"
    sp = lambda r: f"<msub><mi>s</mi><mtext>{r}</mtext></msub>"
    right = f"""
  <div class="given" data-step="1"><span class="gh">Problem</span>&nbsp; Same T-beam ({m('<mi>I</mi><mo>=</mo>' + I_ + U('m⁴'))}). The flange is nailed to the web;
    each nail can resist {m('<mi>F</mi><mo>=</mo><mn>1.50</mn>' + U('kN'))} in shear. <span class="gf"><b>Find:</b> the largest nail spacing.</span></div>
  <div class="steps">
  <div class="step" data-step="1"><span class="no">1</span><b>Idea</b>: the joint must carry the shear flow
    <div class="row"><span class="tag calc">Compute</span>{ds('<mi>q</mi><mo>=</mo><mfrac><mrow><mi>V</mi><mi>Q</mi></mrow><mi>I</mi></mfrac>')}<span class="si" style="margin-left:10px">force per metre along the joint</span></div>
    <div class="row"><span class="tag req">Spacing</span>{ds('<mi>s</mi><mo>=</mo><mfrac><mi>F</mi><mi>q</mi></mfrac>')}<span class="si" style="margin-left:10px">one nail carries <i>F</i> over a length <i>s</i></span></div></div>
  <div class="step" data-step="2"><span class="no">2</span><b><i>Q</i> of the flange</b> (the part the nails hold on)
    <div class="row"><span class="tag calc">Compute</span>{ds(QQ + '<mo>=</mo><msup><mover><mi>y</mi><mo>‾</mo></mover><mo>′</mo></msup><msup><mi>A</mi><mo>′</mo></msup><mo>=</mo>' + P('<mn>0.0725</mn><mo>−</mo><mn>0.015</mn>') + P('<mn>0.2</mn>') + P('<mn>0.03</mn>') + '<mo>=</mo><mn>0.345</mn>' + E('−3') + U('m³'))}</div>
    <div class="cap"><i>Q</i>: first moment of <i>A</i>′ (area beyond the line) about the N.A.</div></div>
  <div class="step" data-step="3"><span class="no">3</span><b>Shear flow</b> (largest <i>V</i> in each region)
    <div class="row"><span class="tag calc">Compute</span>{ds(q('BC') + '<mo>=</mo><mfrac><mrow><msub><mi>V</mi><mtext>BC</mtext></msub><mi>Q</mi></mrow><mi>I</mi></mfrac><mo>=</mo><mfrac><mrow><mn>1.5</mn>' + E(3) + P('<mn>0.345</mn>' + E('−3')) + '</mrow><mrow>' + I_ + '</mrow></mfrac><mo>=</mo><mn>8.61</mn>' + U('kN/m'))}</div>
    <div class="row"><span class="tag calc">Compute</span>{ds(q('CD') + '<mo>=</mo><mfrac><mrow><msub><mi>V</mi><mtext>CD</mtext></msub><mi>Q</mi></mrow><mi>I</mi></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn>' + E(3) + P('<mn>0.345</mn>' + E('−3')) + '</mrow><mrow>' + I_ + '</mrow></mfrac><mo>=</mo><mn>5.74</mn>' + U('kN/m'))}</div></div>
  <div class="step" data-step="4"><span class="no">4</span><b>Spacing</b>
    <div class="row"><span class="tag calc">Compute</span>{ds(sp('BC') + '<mo>=</mo><mfrac><mi>F</mi>' + q('BC') + '</mfrac><mo>=</mo><mfrac><mn>1.50</mn><mn>8.61</mn></mfrac><mo>=</mo><mn>0.174</mn>' + U('m'))}</div>
    <div class="row"><span class="tag calc">Compute</span>{ds(sp('CD') + '<mo>=</mo><mfrac><mi>F</mi>' + q('CD') + '</mfrac><mo>=</mo><mfrac><mn>1.50</mn><mn>5.74</mn></mfrac><mo>=</mo><mn>0.261</mn>' + U('m'))}</div>
    <div class="row"><span class="tag req">Check</span><span>pick a round spacing ≤ <i>s</i> (easy to measure)</span></div></div>
  <div class="ans" data-step="4" style="position:static; align-self:flex-start; margin:-4px 0 0 78px">Use {m(sp('BC') + '<mo>=</mo><mn>150</mn>' + U('mm'))}, {m(sp('CD') + '<mo>=</mo><mn>250</mn>' + U('mm'))}</div>
  </div>"""

    js = "<script>\n" + lib.ELASTIC_JS + """
(() => {
  const clk = revealClock(1);
  function draw() {
    const g = smooth(Math.min(1, Math.max(0, (clk() - 0.4) / 1.4)));
    // the flange moves along the beam length (toward the viewer) relative to the web
    document.getElementById('flslip').setAttribute('transform', `translate(${(-0.3 * %LX% * g).toFixed(1)},${(-0.3 * %LY% * g).toFixed(1)})`);
    document.getElementById('sliparr').setAttribute('opacity', g.toFixed(2));
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>""".replace("%LX%", str(LX)).replace("%LY%", str(LY))
    css = c.STEP_CSS + "\n  .ans math { font-size: 19px; color: " + RED + "; }\n"
    title = 'Example 15.3 (2/2): how far apart can the <span class="key">nails</span> be?'
    body = top_svg() + "\n" + beam_svg() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.3, p. 697, Fig. 15-9d. 3-D slip sketch schematic.</div>')
    lib.write_page("17_slide17_ex153b.html", "Slide 18 - Example 15.3 nails", title, body, 18, css)
    Q = (0.0725 - 0.015) * 0.2 * 0.03
    qbc, qcd = 1.5e3 * Q / 60.125e-6, 1e3 * Q / 60.125e-6
    print(f"check: Q = {Q * 1e3:.4f}e-3, q_BC = {qbc / 1e3:.2f}, q_CD = {qcd / 1e3:.2f} kN/m, s = {1.5e3 / qbc:.3f}, {1.5e3 / qcd:.3f} m")


if __name__ == "__main__":
    build()
