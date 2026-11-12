"""Slide 11 - Design procedure: bending, then shear, then fasteners (Sec. 15.2, p. 690-693).

One slide replaces the planned "S_req'd to a section", "steel W-shapes", "wood/built-up" and
"procedure" slides (75-min budget). Four step cards, one per click, each with a short one-shot
animation (about 1.5 s after its click, no loop):
  1  V and M diagrams: drawn left to right, then V_max and M_max marked
  2  bending: S_req'd = M_max / sigma_allow; simple shape -> solve S = I/c; steel table -> all
     sections with S > S_req'd, pick the lightest (three made-up I-shapes, all with S > S_req'd,
     weight bars from their computed areas; the lightest gets the red box)
  3  shear: tau_allow >= V_max Q/It; rectangle 1.5 V_max/A (parabola), W-shape V_max/A_web (web)
  4  fasteners: q = VQ/I, spacing s = F/q (F: one nail's capacity, Ex. 15.3) (nails drop into a two-board beam)
  Each card labels its equations CALCULATE (navy: you compute it) or REQUIREMENT (red: must hold).
  5  notes: short, heavily loaded (wood) beams -> design for shear first; wood: actual size
Equations and rules from the Procedure for Analysis, p. 693; wood sizes p. 691.

Writes ../slides/separate/12_slide11_procedure.html.
Run:  python3 14_make_slide11_procedure.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, ST, WOOD, TAU, SUP = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.WOOD, lib.TAU, lib.SUPPORT
sym = lib.sym
MC = "#c27c0e"
CW, CH, X0, GAP, TOP = 278, 432, 48, 24, 112      # card width/height, first x, gap, top

# three made-up I-shapes (units): d, bf, tf, tw; all have S > S_req'd = 2.0
CANDS = [(3.2, 2.8, 0.42, 0.28), (3.8, 2.2, 0.34, 0.20), (4.4, 1.7, 0.28, 0.16)]


def props(d, bf, tf, tw):
    A = 2 * bf * tf + tw * (d - 2 * tf)
    I = bf * d ** 3 / 12 - (bf - tw) * (d - 2 * tf) ** 3 / 12
    return A, I / (d / 2)


def ipath(cx, cy, d, bf, tf, tw, u):
    H, w, b, t = d / 2 * u, (d / 2 - tf) * u, bf / 2 * u, tw / 2 * u
    pts = [(-b, -H), (b, -H), (b, -w), (t, -w), (t, w), (b, w), (b, H), (-b, H), (-b, w), (-t, w), (-t, -w), (-b, -w)]
    return "M" + " L".join(f"{cx + x:.1f},{cy + y:.1f}" for x, y in pts) + " Z"


def m(x):
    return f"<math>{x}</math>"


SREQ = "<msub><mi>S</mi><mtext>req’d</mtext></msub>"
MMAX = "<msub><mi>M</mi><mtext>max</mtext></msub>"
VMAX = "<msub><mi>V</mi><mtext>max</mtext></msub>"
SALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
TALL = "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
TAV = "<msub><mi>τ</mi><mtext>avg</mtext></msub>"
QALL = "<msub><mi>q</mi><mtext>allow</mtext></msub>"


def fig1():
    """Beam with uniform load, V diagram (linear) and M diagram (parabola), revealed left to right."""
    x0, x1 = 30, 250
    s = f'<line x1="{x0}" y1="22" x2="{x1}" y2="22" stroke="{ST["edge"]}" stroke-width="7"/>'
    s += "".join(f'<line x1="{x0 + i * 22}" y1="2" x2="{x0 + i * 22}" y2="15" stroke="{RED}" stroke-width="1.5" marker-end="url(#a_C00000)"/>' for i in range(11))
    s += f'<polygon points="{x0},26 {x0 - 7},37 {x0 + 7},37" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'
    s += f'<polygon points="{x1},26 {x1 - 7},34 {x1 + 7},34" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'   # roller
    s += "".join(f'<circle cx="{x1 + dx}" cy="36.5" r="2.5" fill="#fff" stroke="{SUP}" stroke-width="1.2"/>' for dx in (-4, 4))
    vb, mb = 85, 178
    s += f'<g clip-path="url(#clip1)">'
    s += f'<polygon points="{x0},{vb} {x0},{vb - 26} {x1},{vb + 26} {x1},{vb}" fill="{TAU}" fill-opacity="0.15" stroke="{TAU}" stroke-width="2"/>'
    mp = " ".join(f"{x0 + (x1 - x0) * i / 40:.1f},{mb - 48 * 4 * (i / 40) * (1 - i / 40):.1f}" for i in range(41))
    s += f'<polygon points="{x0},{mb} {mp} {x1},{mb}" fill="{MC}" fill-opacity="0.15" stroke="{MC}" stroke-width="2"/></g>'
    for y, lab in ((vb, "V"), (mb, "M")):
        s += f'<line x1="{x0}" y1="{y}" x2="{x1 + 12}" y2="{y}" stroke="#000" stroke-width="1"/>'
        s += f'<text x="{x0 - 22}" y="{y + 5}" font-size="16">{sym(lab)}</text>'
    s += (f'<g id="max1" opacity="0"><circle cx="{x0}" cy="{vb - 26}" r="4.5" fill="{TAU}"/>'
          f'<text x="{x0 + 8}" y="{vb - 30}" font-size="15" fill="{TAU}" font-weight="bold">{sym("V", "max")}</text>'
          f'<circle cx="{(x0 + x1) / 2}" cy="{mb - 48}" r="4.5" fill="{MC}"/>'
          f'<text x="{(x0 + x1) / 2 + 8}" y="{mb - 52}" font-size="15" fill="{MC}" font-weight="bold">{sym("M", "max")}</text></g>')
    return s


def fig2():
    """Three I-shapes with S > S_req'd; weight bars from area; red box on the lightest."""
    u, cy, s = 26, 84, ""
    areas = [props(*c)[0] for c in CANDS]
    for i, c in enumerate(CANDS):
        cx = 50 + i * 90
        s += f'<path d="{ipath(cx, cy, *c, u)}" fill="{ST["inner"]}" stroke="{ST["edge"]}" stroke-width="1.5"/>'
        bw = 60 * areas[i] / max(areas)
        s += f'<rect x="{cx - 30}" y="152" width="{bw:.1f}" height="11" fill="#8a8f96"/>'
    s += f'<text x="20" y="180" font-size="13" fill="{GREY}">weight</text>'
    s += f'<text x="140" y="12" font-size="14" fill="{NAVY}" text-anchor="middle">all have {sym("S")} &gt; {sym("S", "req’d")}</text>'
    lx = 50 + 2 * 90
    s += (f'<g id="pick2" opacity="0"><rect x="{lx - 34}" y="{cy - 64}" width="68" height="128" fill="none" stroke="{RED}" stroke-width="2.5" rx="4"/>'
          f'<text x="276" y="196" font-size="15" fill="{RED}" font-weight="bold" text-anchor="end">lightest: use it</text></g>')
    return s


W3 = (4.4, 2.2, 0.34, 0.3)          # card 3 W-shape (units): d, bf, tf, tw


def w_tau(c, n=60):
    """tau = VQ/(I t) over a W-shape, normalised by its value at the N.A.; also tau_avg = V/(d tw) on the same scale.
    Returns ([(y/(d/2), tau)], tau_avg); y from top (+1) to bottom (-1), with the jump at the flange-web junction."""
    d, bf, tf, tw = c
    H, hw = d / 2, d / 2 - tf
    I = bf * d ** 3 / 12 - (bf - tw) * (2 * hw) ** 3 / 12
    def Qt(y, in_web):
        y = abs(y)
        if in_web:
            return (bf * tf * (H - tf / 2) + tw * (hw - y) * (hw + y) / 2) / tw
        return (bf * (H - y) * (H + y) / 2) / bf
    q0 = Qt(0, True)
    pts = []
    for k in range(n + 1):                                     # top flange
        y = H - tf * k / n
        pts.append((y / H, Qt(y, False) / q0))
    for k in range(n + 1):                                     # web
        y = hw - 2 * hw * k / n
        pts.append((y / H, Qt(y, True) / q0))
    for k in range(n + 1):                                     # bottom flange
        y = -hw - tf * k / n
        pts.append((y / H, Qt(y, False) / q0))
    # q0 = Q(0)/tw, so tau(0) = V q0 / I and tau_avg = V/(d tw): ratio = I / (d tw q0)
    return pts, I / (d * tw * q0)


def fig3():
    """Rectangle with its parabola; W-shape with tau = VQ/It drawn beside it (grows), and the average V/A_web."""
    s = ""
    rx, ry, rw, rh = 14, 30, 44, 110
    s += f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="{ST["inner"]}" stroke="{ST["edge"]}" stroke-width="1.5"/>'
    s += f'<line x1="{rx + rw + 8}" y1="{ry}" x2="{rx + rw + 8}" y2="{ry + rh}" stroke="#000" stroke-width="1"/>'
    s += f'<path id="par3" fill="{TAU}" fill-opacity="0.2" stroke="{TAU}" stroke-width="2"/>'
    s += f'<text x="{rx + rw / 2 + 14}" y="{ry + rh + 18}" font-size="14" text-anchor="middle">rectangle</text>'
    s += f'<text x="{rx + rw / 2 + 14}" y="{ry + rh + 50}" font-size="15" text-anchor="middle">{sym("τ", "max")} = 1.5{sym("V")}/{sym("A")}</text>'
    c = W3
    u, cx, cy = 25, 158, ry + rh / 2
    s += f'<path d="{ipath(cx, cy, *c, u)}" fill="{ST["inner"]}" stroke="{ST["edge"]}" stroke-width="1.5"/>'
    wy = (c[0] / 2 - c[2]) * u
    s += f'<rect id="web3" x="{cx - c[3] / 2 * u:.1f}" y="{cy - wy:.1f}" width="{c[3] * u:.1f}" height="{2 * wy:.1f}" fill="{TAU}" opacity="0"/>'
    ax = cx + c[1] / 2 * u + 10
    # d: full depth; t_w: web thickness (A_web = d t_w, as in Ex. 15.1)
    dx = cx - c[1] / 2 * u - 8
    s += (f'<line x1="{dx}" y1="{cy - c[0] / 2 * u + 2}" x2="{dx}" y2="{cy + c[0] / 2 * u - 2}" stroke="#000" stroke-width="1.2" '
          f'marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
          f'<text x="{dx - 4}" y="{cy + 5}" font-size="16" text-anchor="end">{sym("d")}</text>'
          f'<line x1="{cx + 4}" y1="{cy + 26}" x2="{cx + 16}" y2="{cy + 34}" stroke="#000" stroke-width="1"/>'
          f'<text x="{cx + 17}" y="{cy + 40}" font-size="15">{sym("t", "w")}</text>')
    s += f'<line x1="{ax}" y1="{cy - c[0] / 2 * u}" x2="{ax}" y2="{cy + c[0] / 2 * u}" stroke="#000" stroke-width="1"/>'
    s += f'<path id="wt3" fill="{TAU}" fill-opacity="0.2" stroke="{TAU}" stroke-width="2"/>'
    s += f'<line id="wavg3" x1="{ax}" x2="{ax}" y1="{cy - wy:.1f}" y2="{cy + wy:.1f}" stroke="{RED}" stroke-width="1.8" stroke-dasharray="5 3" opacity="0"/>'
    s += f'<text id="wavgl3" x="{ax + 4}" y="{cy + wy + 14:.1f}" font-size="12" fill="{RED}" opacity="0">average</text>'
    s += f'<text id="wmax3" x="{ax + 49}" y="{cy + 4}" font-size="12" fill="{TAU}" font-weight="bold" opacity="0">max</text>'
    s += f'<text x="{cx + 14}" y="{ry + rh + 18}" font-size="14" text-anchor="middle">W-shape</text>'
    s += f'<text x="{cx + 14}" y="{ry + rh + 32}" font-size="12" fill="{GREY}" text-anchor="middle">(wide-flange I-beam)</text>'
    s += f'<text x="{cx + 14}" y="{ry + rh + 50}" font-size="15" text-anchor="middle">{sym("τ", "avg")} = {sym("V")}/({sym("d")}{sym("t", "w")})</text>'
    return s


def fig4():
    """Side view of a two-board beam; nails drop in at spacing s."""
    x0, x1, s = 20, 260, ""
    s += f'<rect x="{x0}" y="70" width="{x1 - x0}" height="18" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.5"/>'
    s += f'<rect x="{x0}" y="88" width="{x1 - x0}" height="56" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.5"/>'
    s += f'<text x="{x0 + 6}" y="84" font-size="13" fill="{WOOD["edge"]}">flange</text>'
    s += f'<text x="{x0 + 6}" y="120" font-size="13" fill="{WOOD["edge"]}">web</text>'
    s += '<g id="nails4">' + "".join(
        f'<g class="nail"><line x1="{x0 + 70 + i * 45}" y1="0" x2="{x0 + 70 + i * 45}" y2="44" stroke="#333" stroke-width="2.5"/>'
        f'<line x1="{x0 + 63 + i * 45}" y1="0" x2="{x0 + 77 + i * 45}" y2="0" stroke="#333" stroke-width="3"/></g>' for i in range(4)) + '</g>'
    s += (f'<g id="sdim4" opacity="0"><line x1="{x0 + 70}" y1="56" x2="{x0 + 115}" y2="56" stroke="{RED}" stroke-width="1.5" '
          f'marker-start="url(#a_C00000)" marker-end="url(#a_C00000)"/>'
          f'<text x="{x0 + 92}" y="50" font-size="16" fill="{RED}" text-anchor="middle" font-weight="bold">{sym("s")}</text></g>')
    return s


CLIP = '<clipPath id="clip1"><rect id="cr1" x="0" y="40" width="0" height="160"/></clipPath>'


def card(i, head, fig, comp, check, cap):
    """Two rows at the same height in every card: Compute (you work it out) and Check (must hold)."""
    x = X0 + i * (CW + GAP)
    row = lambda tag, cls, h: (f'<div class="row"><span class="tag {cls}">{tag}</span>'
                               f'<span class="rh">{h}</span></div>')
    return f'''  <div class="card" data-step="{i + 1}" style="left:{x}px">
    <div class="ch"><span class="no">{i + 1}</span>{head}</div>
    <svg width="{CW - 2}" height="200" viewBox="0 0 280 200" style="margin-top:4px">
      <defs>{lib.markers(RED, GREY) if i == 3 else ""}{CLIP if i == 0 else ""}</defs>{fig}</svg>
    {row("Compute", "calc", comp)}
    {row("Check", "req", check) if check else '<div class="row"></div>'}
    <div class="cap2">{cap}</div>
  </div>'''


def ds(x):
    """Display-style inline maths (full-size fractions)."""
    return f'<math><mstyle displaystyle="true">{x}</mstyle></math>'


def build():
    TMAX = "<msub><mi>τ</mi><mtext>max</mtext></msub>"
    cards = [
        card(0, "<i>V</i> and <i>M</i> diagrams", fig1(),
             ds(f"{VMAX}<mo>,</mo><mspace width='0.5em'/>{MMAX}"), "",
             "read them off the diagrams"),
        card(1, "Bending: select the section", fig2(),
             ds(f"{SREQ}<mo>=</mo><mfrac>{MMAX}{SALL}</mfrac>"),
             ds(f"<mi>S</mi><mo>≥</mo>{SREQ}"),
             "take the lightest section that passes"),
        card(2, "Shear: check it", fig3(),
             ds(f"{TMAX}<mo>=</mo><mfrac><mrow>{VMAX}<mi>Q</mi></mrow><mrow><mi>I</mi><mi>t</mi></mrow></mfrac>"),
             ds(f"{TMAX}<mo>≤</mo>{TALL}"),
             "if not, choose a bigger section"),
        card(3, "Fasteners (built-up)", fig4(),
             ds("<mi>q</mi><mo>=</mo><mfrac><mrow><mi>V</mi><mi>Q</mi></mrow><mi>I</mi></mfrac>"),
             ds("<mi>s</mi><mo>≤</mo><mfrac><mi>F</mi><mi>q</mi></mfrac>"),
             "<i>F</i>: force one nail can carry"),
    ]
    notes = f'''  <div class="notes" data-step="5">
    <div><b class="em">Short beam, large loads</b> (often wood): shear may govern. Design for shear, then check bending.</div>
    <div><b>Wood:</b> use the <i>actual</i> size. A 2 × 4 is really 1.5 in. × 3.5 in.</div>
    <div><b>Allowable stresses</b> {m(SALL)} and {m(TALL)} are given (design code, or the problem statement).</div>
    <div><b>W-shapes:</b> the book takes τ as uniform over the web and checks {m(TAV + '<mo>=</mo><mi>V</mi><mo>/</mo><mo>(</mo><mi>d</mi><msub><mi>t</mi><mi>w</mi></msub><mo>)</mo><mo>≤</mo>' + TALL)}; the true peak is only slightly higher.</div>
  </div>'''

    wpts, wavg = w_tau(W3)
    wx = 158 + W3[1] / 2 * 25 + 10
    js = "<script>\n" + lib.ELASTIC_JS + "\nconst WPTS = " + str([[round(a, 4), round(b, 4)] for a, b in wpts]) + ", WAVG = " + f"{wavg:.4f}" + ";\n" + """
(() => {
  const $ = id => document.getElementById(id);
  const clamp = v => Math.min(1, Math.max(0, v));
  const k = [1, 2, 3, 4].map(n => revealClock(n));
  const nails = [...document.querySelectorAll('#nails4 .nail')];
  function draw() {
    const g1 = smooth(clamp((k[0]() - 0.3) / 1.4));
    $('cr1').setAttribute('width', (280 * g1).toFixed(1));
    $('max1').setAttribute('opacity', clamp((k[0]() - 1.8) / 0.4));
    $('pick2').setAttribute('opacity', clamp((k[1]() - 1.0) / 0.4));
    // rectangle: tau = 1.5 V/A (1 - 4y^2/h^2), grows in
    const g3 = smooth(clamp((k[2]() - 0.3) / 1.2)), x = 14 + 44 + 8, y0 = 30, h = 110;
    let d = `M${x},${y0}`;
    for (let i = 0; i <= 30; i++) { const yy = i / 30, tau = 1 - (2 * yy - 1) ** 2; d += ` L${(x + 30 * g3 * tau).toFixed(1)},${(y0 + h * yy).toFixed(1)}`; }
    $('par3').setAttribute('d', d + ' Z');
    // W-shape: tau = VQ/It (normalised, from Python), same growth
    const WX = %WX%, WCY = %WCY%, WH = %WH%, WS = 46;
    let dw = `M${WX},${(WCY - WH).toFixed(1)}`;
    for (const [yy, tau] of WPTS) dw += ` L${(WX + WS * g3 * tau).toFixed(1)},${(WCY - WH * yy).toFixed(1)}`;
    $('wt3').setAttribute('d', dw + ` L${WX},${(WCY + WH).toFixed(1)} Z`);
    const w = clamp((k[2]() - 1.6) / 0.5), xa = WX + WS * WAVG;
    $('web3').setAttribute('opacity', (0.6 * w).toFixed(2));
    for (const id of ['wavg3', 'wavgl3', 'wmax3']) $(id).setAttribute('opacity', w.toFixed(2));
    $('wavg3').setAttribute('x1', xa.toFixed(1)); $('wavg3').setAttribute('x2', xa.toFixed(1));
    $('wavgl3').setAttribute('x', (xa + 3).toFixed(1));
    // nails drop one after another into the boards
    nails.forEach((n, i) => {
      const g = smooth(clamp((k[3]() - 0.3 - 0.25 * i) / 0.5));
      n.setAttribute('transform', `translate(0, ${(-10 + 80 * g).toFixed(1)})`);
      n.setAttribute('opacity', g > 0 ? 1 : 0);
    });
    $('sdim4').setAttribute('opacity', clamp((k[3]() - 1.9) / 0.4));
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>"""
    js = js.replace("%WX%", f"{wx:.1f}").replace("%WCY%", "85").replace("%WH%", f"{W3[0] / 2 * 25:.1f}")

    css = lib.TEXT_CSS + f"""
  .card {{ position: absolute; top: {TOP}px; width: {CW}px; height: {CH}px; box-sizing: border-box;
          padding: 10px 0 0; }}
  .card + .card {{ border-left: 1px solid #d5d9df; }}
  .ch {{ font-size: 19px; font-weight: bold; color: {NAVY}; padding: 0 12px; height: 28px; white-space: nowrap; }}
  .no {{ display: inline-block; min-width: 22px; margin-right: 4px; color: {NAVY}; font-weight: bold; }}
  .no::after {{ content: "."; }}
  .row {{ display: flex; align-items: center; height: 62px; padding: 0 14px; }}
  .tag {{ width: 74px; flex: none; font-size: 13px; font-weight: bold; letter-spacing: 0.5px; text-transform: uppercase; }}
  .tag.calc {{ color: {NAVY}; }}
  .tag.req {{ color: {RED}; }}
  .rh {{ flex: 1; text-align: center; padding-right: 20px; }}
  .rh math {{ font-size: 23px; }}
  .cap2 {{ font-size: 15px; color: {GREY}; text-align: center; padding: 6px 14px 0; }}
  .notes {{ position: absolute; left: {X0}px; top: 562px; width: 1184px; font-size: 17px; line-height: 1.45; }}
"""
    title = 'Design for <span class="key">bending</span>, then check shear and fasteners'
    body = "\n".join(cards) + "\n" + notes + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.2, Procedure for Analysis, p. 693; wood, p. 691; '
        '<i>s</i> = <i>F</i>/<i>q</i>, Ex. 15.3, p. 697. I-shapes in step 2 are hypothetical.</div>')
    lib.write_page("12_slide11_procedure.html", "Slide 11 - Design procedure", title, body, 11, css)
    for c in CANDS:
        print("candidate", c, "A = %.2f, S = %.2f" % props(*c))


if __name__ == "__main__":
    build()
