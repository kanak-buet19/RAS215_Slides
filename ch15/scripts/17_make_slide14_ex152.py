"""Slide 14 - Example 15.2: wood beam; the size from bending fails shear (Hibbeler 6th ed., Ex. 15.2, p. 695, Fig. 15-8).

Book data (checked against the photo of p. 695):
  laminated wood beam, uniform load 12 kN/m over its whole 4 m length; overhang 1 m left of support A,
  support B 3 m right of A (end of the beam). Height = 1.5 x width a. sigma_allow = 9 MPa, tau_allow = 0.6 MPa.
  reactions A = 32 kN, B = 16 kN; V: -12 at A-, +20 at A+, -16 at B, zero 1.33 m left of B
  M: -6 at A, max 10.67 kN.m 1.33 m left of B; V_max = 20 kN, M_max = 10.67 kN.m
  S_req'd = 10.67(10^3)/9(10^6) = 0.00119 m^3 = (1/12)a(1.5a)^3/(0.75a) -> a^3 = 0.003160 m^3, a = 0.147 m
  tau_max = 1.5 V_max/A = 1.5(20e3)/((0.147)(1.5)(0.147)) = 0.929 MPa > 0.6 MPa   (fails)
  redesign: 600e3 = 1.5(20e3)/(a(1.5a)) -> a = 0.183 m = 183 mm
Clicks: 1 problem + beam, 2 V and M, 3 bending -> a = 147 mm (section drawn to scale), 4 shear check fails
(tau bar over the allowable line), 5 redesign: section grows to 183 mm, bar drops to the line; answer.

Writes ../slides/separate/14_slide14_ex152.html.
Run:  python3 17_make_slide14_ex152.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, SUP, TAU, WOOD = lib.NAVY, lib.RED, lib.GREY, lib.SUPPORT, lib.TAU, lib.WOOD
sym = lib.sym
MC = "#c27c0e"

X0, PM = 70, 112                 # x of the left end, px per m
X = lambda xm: X0 + PM * xm
BY, BH = 44, 24                  # beam top, depth
VB, VS = 190, 2.4                # V baseline, px per kN
MB, MS = 306, 5.0                # M baseline, px per kN.m
SEC_K = 400                      # section drawing, px per m


def V_at(x):
    return -12 * x + 32 * (x > 1) + 16 * (x >= 4)


def M_at(x):
    return -6 * x * x + 32 * max(0, x - 1)


def beam_svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY)}</defs><g data-step="1">'
    # glued-laminated wood beam: wood face with lamination lines
    s += f'<rect x="{X(0)}" y="{BY}" width="{PM * 4}" height="{BH}" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.6"/>'
    for i in range(1, 6):
        y = BY + BH * i / 6
        s += f'<line x1="{X(0)}" y1="{y:.1f}" x2="{X(4)}" y2="{y:.1f}" stroke="{WOOD["edge"]}" stroke-width="0.6" opacity="0.6"/>'
    for i in range(17):
        x = X(4 * i / 16)
        s += f'<line x1="{x:.1f}" y1="{BY - 30}" x2="{x:.1f}" y2="{BY - 3}" stroke="{RED}" stroke-width="1.6" marker-end="url(#a_C00000)"/>'
    s += f'<line x1="{X(0)}" y1="{BY - 30}" x2="{X(4)}" y2="{BY - 30}" stroke="{RED}" stroke-width="1.6"/>'
    s += f'<text x="{X(4)}" y="{BY - 38}" font-size="17" fill="{RED}" font-weight="bold" text-anchor="end">12 kN/m</text>'
    s += f'<polygon points="{X(1)},{BY + BH} {X(1) - 10},{BY + BH + 16} {X(1) + 10},{BY + BH + 16}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
    s += f'<polygon points="{X(4)},{BY + BH} {X(4) - 10},{BY + BH + 13} {X(4) + 10},{BY + BH + 13}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
    s += (f'<circle cx="{X(4) - 5}" cy="{BY + BH + 16}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'
          f'<circle cx="{X(4) + 5}" cy="{BY + BH + 16}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>')
    s += f'<text x="{X(1) - 12}" y="{BY + BH + 16}" font-size="17" text-anchor="end" font-style="italic">A</text>'
    s += f'<text x="{X(4) + 14}" y="{BY + BH + 16}" font-size="17" font-style="italic">B</text>'
    for a, b, t in ((0, 1, "1 m"), (1, 4, "3 m")):
        s += f'<line x1="{X(a) + 2}" y1="{BY + BH + 34}" x2="{X(b) - 2}" y2="{BY + BH + 34}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X((a + b) / 2)}" y="{BY + BH + 50}" font-size="14" fill="{GREY}" text-anchor="middle">{t}</text>'
    s += '</g>'
    # click 2: V and M (book values)
    s += '<g data-step="2">'
    vp = [(0, 0), (1, -12), (1, 20), (4, -16), (4, 0)]
    s += '<polygon points="' + " ".join(f"{X(x):.1f},{VB - VS * v:.1f}" for x, v in vp) + f'" fill="{TAU}" fill-opacity="0.15" stroke="{TAU}" stroke-width="2.2"/>'
    mp = [(X(0), MB)] + [(X(4 * i / 80), MB - MS * M_at(4 * i / 80)) for i in range(81)] + [(X(4), MB)]
    s += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in mp) + f'" fill="{MC}" fill-opacity="0.15" stroke="{MC}" stroke-width="2.2"/>'
    for y, lab, unit in ((VB, "V", "kN"), (MB, "M", "kN·m")):
        s += f'<line x1="{X(0)}" y1="{y}" x2="{X(4) + 22}" y2="{y}" stroke="#000" stroke-width="1.2" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X(0) - 8}" y="{y + 5}" font-size="15" text-anchor="end">{sym(lab)} ({unit})</text>'
    s += (f'<text x="{X(1) + 6}" y="{VB - VS * 20 - 4}" font-size="15" fill="{RED}" font-weight="bold">20 = {sym("V", "max")}</text>'
          f'<text x="{X(1) - 6}" y="{VB + VS * 12 + 16}" font-size="14" fill="{TAU}" text-anchor="end">−12</text>'
          f'<text x="{X(4) - 6}" y="{VB + VS * 16 + 16}" font-size="14" fill="{TAU}" text-anchor="end">−16</text>'
          f'<text x="{X(8 / 3)}" y="{MB - MS * 10.67 - 6}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="middle">10.67 = {sym("M", "max")}</text>'
          f'<text x="{X(1)}" y="{MB + MS * 6 + 16}" font-size="14" fill="{MC}" text-anchor="middle">−6</text>'
          f'<line x1="{X(8 / 3)}" y1="{VB + 6}" x2="{X(8 / 3)}" y2="{MB}" stroke="{GREY}" stroke-width="1" stroke-dasharray="3 3"/>'
          f'<text x="{X(8 / 3) - 5}" y="{VB + 16}" font-size="12" fill="{GREY}" text-anchor="end">{sym("V")} = 0</text>')
    s += '</g>'
    return f'<svg class="fig" style="left:40px; top:160px" width="620" height="350" viewBox="0 0 620 350">{s}</svg>'


def section_svg():
    """Section a x 1.5a to scale (147 mm, grows to 183 mm on click 5) and the tau bar vs tau_allow."""
    s = f'<defs>{lib.markers(GREY)}</defs>'
    s += '<g data-step="1">'
    s += f'<rect id="sec" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.6"/>'
    s += f'<g id="lams"></g>'
    s += f'<line id="dimA" stroke="#000" stroke-width="1.2" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
    s += f'<line id="dimH" stroke="#000" stroke-width="1.2" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
    s += f'<text id="secA" font-size="16" text-anchor="middle"></text>'
    s += f'<text x="150" y="184" font-size="13" fill="{GREY}" text-anchor="middle">beam cross section (drawn to scale)</text>'
    s += f'<text id="secH" font-size="16"></text>'
    s += '</g><g data-step="4">'
    bx, bb = 400, 168
    s += f'<line x1="{bx - 30}" y1="{bb}" x2="{bx + 110}" y2="{bb}" stroke="#000" stroke-width="1.2"/>'
    s += f'<rect id="tbar" x="{bx}" width="44"/>'
    s += f'<line x1="{bx - 16}" y1="{bb - 0.6 * 140}" x2="{bx + 60}" y2="{bb - 0.6 * 140}" stroke="{RED}" stroke-width="2.4" stroke-dasharray="7 4"/>'
    s += f'<text x="{bx + 64}" y="{bb - 0.6 * 140 + 5}" font-size="15" fill="{RED}">{sym("τ", "allow")} = 0.6 MPa</text>'
    s += f'<text id="tval" x="{bx + 22}" font-size="15" font-weight="bold" text-anchor="middle"></text>'
    s += f'<text x="{bx + 22}" y="{bb + 18}" font-size="15" text-anchor="middle">{sym("τ", "max")}</text>'
    s += '</g>'
    return f'<svg class="fig" style="left:40px; top:508px" width="620" height="190" viewBox="0 0 620 190">{s}</svg>'


def m(x):
    return f"<math>{x}</math>"


def ds(x):
    return f'<math><mstyle displaystyle="true">{x}</mstyle></math>'


def build():
    u = lambda t: f"<mspace width='0.2em'/><mtext>{t}</mtext>"
    SREQ = "<msub><mi>S</mi><mtext>req’d</mtext></msub>"
    MMAX = "<msub><mi>M</mi><mtext>max</mtext></msub>"
    VMAX = "<msub><mi>V</mi><mtext>max</mtext></msub>"
    SALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
    TALL = "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
    TMAX = "<msub><mi>τ</mi><mtext>max</mtext></msub>"
    p10 = lambda e: f"<mo stretchy='false'>(</mo><msup><mn>10</mn><mn>{e}</mn></msup><mo stretchy='false'>)</mo>"
    right = f"""
  <div class="given" data-step="1"><span class="gh">Problem</span>&nbsp; A laminated wood beam carries 12 kN/m (Fig. 15-8). Height = 1.5 × width <i>a</i>.
    {m(SALL + '<mo>=</mo><mn>9</mn>' + u('MPa'))}, {m(TALL + '<mo>=</mo><mn>0.6</mn>' + u('MPa'))}.
    <span class="gf"><b>Find:</b> the smallest width <i>a</i>.</span></div>
  <div class="steps">
  <div class="step" data-step="2"><span class="no">1</span><b>Diagrams</b> (slide 14; {m('<msub><mi>R</mi><mrow><mi>A</mi><mi>y</mi></mrow></msub><mo>=</mo><mn>32</mn>' + u('kN'))}, {m('<msub><mi>R</mi><mrow><mi>B</mi><mi>y</mi></mrow></msub><mo>=</mo><mn>16</mn>' + u('kN'))}):<br><span style="margin-left:32px"></span>{m(VMAX + '<mo>=</mo><mn>20</mn>' + u('kN'))},&nbsp; {m(MMAX + '<mo>=</mo><mn>10.67</mn>' + u('kN·m'))}</div>
  <div class="step" data-step="3"><span class="no">2</span><b>Bending</b> <span class="si">(N, m)</span>
    <div class="row"><span class="tag calc">Compute</span>{ds(SREQ + '<mo>=</mo><mfrac>' + MMAX + SALL + '</mfrac><mo>=</mo><mfrac><mrow><mn>10.67</mn>' + p10(3) + '</mrow><mrow><mn>9</mn>' + p10(6) + '</mrow></mfrac><mo>=</mo><mn>0.00119</mn>' + u('m³'))}</div>
    <div class="row"><span class="tag calc">Solve</span>{ds('<mi>S</mi><mo>=</mo><mfrac><mi>I</mi><mi>c</mi></mfrac><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>12</mn></mfrac><mi>a</mi><msup><mrow><mo stretchy="false">(</mo><mn>1.5</mn><mi>a</mi><mo stretchy="false">)</mo></mrow><mn>3</mn></msup></mrow><mrow><mn>0.75</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mn>0.00119</mn><mspace width="0.4em"/><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>0.147</mn>' + u('m'))}</div></div>
  <div class="step" data-step="4"><span class="no">3</span><b>Shear</b> (rectangle)
    <div class="row"><span class="tag calc">Compute</span>{ds(TMAX + '<mo>=</mo><mn>1.5</mn><mfrac>' + VMAX + '<mi>A</mi></mfrac><mo>=</mo><mn>1.5</mn><mfrac><mrow><mn>20</mn>' + p10(3) + '</mrow><mrow><mo stretchy="false">(</mo><mn>0.147</mn><mo stretchy="false">)</mo><mo stretchy="false">(</mo><mn>1.5</mn><mo>×</mo><mn>0.147</mn><mo stretchy="false">)</mo></mrow></mfrac><mo>=</mo><mn>0.929</mn>' + u('MPa'))}</div>
    <div class="row"><span class="tag req">Check</span>{ds(TMAX + '<mo>≤</mo>' + TALL + '<mo>?</mo><mspace width="0.6em"/><mn>0.929</mn><mo>&gt;</mo><mn>0.6</mn>' + u('MPa'))}<span class="bad">FAILS</span></div></div>
  <div class="step" data-step="5"><span class="no">4</span><b>Redesign for shear</b> (make {m(TMAX + '<mo>=</mo>' + TALL)})
    <div class="row"><span class="tag calc">Solve</span>{ds(TALL + '<mo>=</mo><mn>1.5</mn><mfrac>' + VMAX + '<mi>A</mi></mfrac><mo>:</mo><mspace width="0.5em"/><mn>0.6</mn>' + p10(6) + '<mo>=</mo><mn>1.5</mn><mfrac><mrow><mn>20</mn>' + p10(3) + '</mrow><mrow><mi>a</mi><mo stretchy="false">(</mo><mn>1.5</mn><mi>a</mi><mo stretchy="false">)</mo></mrow></mfrac>')}</div>
    <div class="row"><span class="tag calc"></span>{ds('<mo>⇒</mo><mi>a</mi><mo>=</mo><mn>0.183</mn>' + u('m'))}<span class="cap3">(a bigger section also passes bending)</span></div></div></div>
  <div class="ans" data-step="5">Use <b><i>a</i> = 183 mm</b></div>"""

    js = "<script>\n" + lib.ELASTIC_JS + """
(() => {
  const K = %K%, WE = "%WE%", RED = "%RED%", TAU = "%TAU%";
  const $ = id => document.getElementById(id);
  const set = (id, a) => { const e = $(id); for (const k in a) e.setAttribute(k, a[k]); };
  const clamp = v => Math.min(1, Math.max(0, v));
  const c5 = revealClock(5);
  let K_STEP = 99;                               // deck click count (standalone page: everything shown)
  addEventListener('buildstep', e => { K_STEP = e.detail.k; });
  const bx = 400, bb = 168, BS = 140;          // tau bar: px per MPa
  function draw() {
    const g = smooth(clamp((c5() - 0.4) / 1.6));
    const a = 0.147 + (0.183 - 0.147) * g, w = K * a, h = K * 1.5 * a, x = 150 - w / 2, y = 168 - h;
    set('sec', {x: x.toFixed(1), y: y.toFixed(1), width: w.toFixed(1), height: h.toFixed(1)});
    let L = '';
    for (let i = 1; i < 6; i++) L += `<line x1="${x.toFixed(1)}" x2="${(x + w).toFixed(1)}" y1="${(y + h * i / 6).toFixed(1)}" y2="${(y + h * i / 6).toFixed(1)}" stroke="${WE}" stroke-width="0.6" opacity="0.6"/>`;
    $('lams').innerHTML = L;
    // dimensions: width a above, depth 1.5a on the right; symbols only until a is known (click 3)
    set('dimA', {x1: (x + 1).toFixed(1), x2: (x + w - 1).toFixed(1), y1: (y - 10).toFixed(1), y2: (y - 10).toFixed(1)});
    set('dimH', {x1: (x + w + 12).toFixed(1), x2: (x + w + 12).toFixed(1), y1: (y + 1).toFixed(1), y2: (y + h - 1).toFixed(1)});
    const known = K_STEP >= 3;
    set('secA', {x: (x + w / 2).toFixed(1), y: (y - 16).toFixed(1)});
    $('secA').innerHTML = '<tspan class="sym">a</tspan>' + (known ? ` = ${(a * 1000).toFixed(0)} mm` : '');
    set('secH', {x: (x + w + 20).toFixed(1), y: (y + h / 2 + 5).toFixed(1)});
    $('secH').innerHTML = '1.5<tspan class="sym">a</tspan>' + (known ? ` = ${(1.5 * a * 1000).toFixed(0)} mm` : '');
    // tau_max = 1.5 V / A with V = 20 kN; the book rounds the first value to 0.929 MPa
    const tau = g >= 1 ? 0.6 : (g <= 0 ? 0.929 : 1.5 * 20e3 / (a * 1.5 * a) / 1e6);
    set('tbar', {y: (bb - BS * tau).toFixed(1), height: (BS * tau).toFixed(1), fill: tau > 0.601 ? RED : TAU});
    set('tval', {y: (bb - BS * tau - 6).toFixed(1), fill: tau > 0.601 ? RED : TAU}); $('tval').textContent = tau.toFixed(3) + ' MPa';
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>""".replace("%K%", str(SEC_K)).replace("%WE%", WOOD["edge"]).replace("%RED%", RED).replace("%TAU%", TAU)

    css = lib.TEXT_CSS + f"""
  .given {{ position: absolute; left: 48px; top: 104px; width: 1164px; box-sizing: border-box; padding: 7px 14px 8px; font-size: 16px; line-height: 1.45;
            border: 2px solid {NAVY}; border-left-width: 7px; border-radius: 6px; }}
  .given math {{ font-size: 19px; font-weight: bold; }}
  .gh {{ font-size: 13px; font-weight: bold; color: {NAVY}; text-transform: uppercase; letter-spacing: 1px; }}
  .gf {{ color: {RED}; }}
  .steps {{ position: absolute; left: 680px; top: 166px; width: 532px; display: flex; flex-direction: column; gap: 24px; }}  /* uniform step spacing */
  .step {{ font-size: 17px; }}
  .step math {{ font-size: 18px; }}
  .no {{ display: inline-block; min-width: 22px; margin-right: 4px; color: {NAVY}; font-weight: bold; }}
  .no::after {{ content: "."; }}
  .row {{ display: flex; align-items: center; margin-top: 4px; }}
  .tag {{ width: 78px; flex: none; font-size: 12px; font-weight: bold; text-transform: uppercase; }}
  .tag.calc {{ color: {NAVY}; }}
  .tag.req {{ color: {RED}; }}
  .si {{ font-size: 13px; color: {GREY}; }}
  .cap3 {{ font-size: 14px; color: {GREY}; margin-left: 12px; }}
  .bad {{ color: {RED}; font-weight: bold; margin-left: 14px; font-size: 18px; letter-spacing: 1px; padding: 1px 10px; border: 2px solid {RED}; border-radius: 4px; background: #fbecec; }}
  .cap2 {{ font-size: 14px; color: {GREY}; margin: 2px 0 0 78px; }}
  .ans {{ position: absolute; left: 758px; top: 652px; padding: 3px 16px; font-size: 19px; color: {RED};
         border: 2px solid {RED}; border-radius: 6px; }}
"""
    title = 'Example 15.2 (2/2): the bending design <span class="key">fails</span> in shear'
    body = beam_svg() + "\n" + section_svg() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.2, p. 695, Fig. 15-8.</div>')
    lib.write_page("14_slide14_ex152.html", "Slide 15 - Example 15.2", title, body, 15, css)
    a = (0.00119 / 0.375) ** (1 / 3)
    print(f"check: M(8/3) = {M_at(8/3):.2f}, M(1) = {M_at(1)}, a_bend = {a:.4f} m, a_shear = {(20e3 / 600e3) ** 0.5:.4f} m,"
          f" tau(0.147) = {1.5 * 20e3 / (0.147 * 1.5 * 0.147) / 1e6:.3f} MPa")


if __name__ == "__main__":
    build()
