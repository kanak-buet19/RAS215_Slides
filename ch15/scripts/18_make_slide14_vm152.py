"""Slide 14 - Example 15.2 (1/2): draw the V and M diagrams by cutting the beam (before slide 15).

Beam (Ex. 15.2, p. 695, Fig. 15-8): 12 kN/m over the whole 4 m; free left end, pin A at 1 m, roller B at 4 m.
x is measured from the free left end. Left piece of each cut, V down and M counterclockwise (positive):
  reactions: resultant 12(4) = 48 kN at x = 2 m;  sum M_B: -R_A(3) + 48(2) = 0 -> R_A = 32 kN;  R_B = 48 - 32 = 16 kN
  cut 1, 0 < x < 1:  -12x - V = 0 -> V = -12x;          M + 12x(x/2) = 0 -> M = -6x^2          (x = 1: V = -12, M = -6)
  cut 2, 1 < x < 4:  32 - 12x - V = 0 -> V = 32 - 12x;  M + 12x(x/2) - 32(x - 1) = 0
                     -> M = 32(x - 1) - 6x^2                                                   (x = 4: V = -16, M = 0)
  max M where V = 0: 32 - 12x = 0 -> x = 2.67 m; M = 32(1.67) - 6(2.67)^2 = 10.67 kN.m
These match the book's diagrams (V: -12, 20, -16; M: -6, 10.67). The cuts and the V = 0 step are the method of
the book's earlier chapter on V and M diagrams (not in the Ch. 15 pages).
Clicks: 1 problem + beam with supports, 2 supports removed -> R_A, R_B, 3 reactions solved, 4 cut 1, 5 cut 2,
6 maximum M where V = 0.

Writes ../slides/separate/14a_slide14_vm152.html.
Run:  python3 18_make_slide14_vm152.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, SUP, TAU, WOOD = lib.NAVY, lib.RED, lib.GREY, lib.SUPPORT, lib.TAU, lib.WOOD
sym = lib.sym
MC = "#c27c0e"

X0, PM = 80, 100                  # x of the free left end, px per m
X = lambda xm: X0 + PM * xm
BY, BH = 96, 24                   # beam top, depth
VB, VS = 290, 2.4                 # V baseline, px per kN
MB, MS = 450, 6.0                 # M baseline, px per kN.m
CUTS = [(0, 1, 0.6), (1, 4, 3.0)]  # region start, end, where the cut is drawn (m)
XM = 8 / 3                        # V = 0


def V_at(x):
    return -12 * x + 32 * (x > 1)


def M_at(x):
    return -6 * x * x + 32 * max(0, x - 1)


def fmt(v):
    v = round(v, 2)
    s = f"{abs(v):g}"
    return ("−" if v < 0 else "") + s


def left_svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY, TAU, MC)}</defs><g data-step="1">'
    s += f'<rect x="{X(0)}" y="{BY}" width="{PM * 4}" height="{BH}" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.6"/>'
    for i in range(1, 6):
        y = BY + BH * i / 6
        s += f'<line x1="{X(0)}" y1="{y:.1f}" x2="{X(4)}" y2="{y:.1f}" stroke="{WOOD["edge"]}" stroke-width="0.6" opacity="0.6"/>'
    s += '<g id="wload" style="transition: opacity 0.5s">'      # distributed load: greyed out while its resultant is shown (click 3)
    for i in range(17):
        x = X(4 * i / 16)
        s += f'<line x1="{x:.1f}" y1="{BY - 30}" x2="{x:.1f}" y2="{BY - 3}" stroke="{RED}" stroke-width="1.6" marker-end="url(#a_C00000)"/>'
    s += f'<line x1="{X(0)}" y1="{BY - 30}" x2="{X(4)}" y2="{BY - 30}" stroke="{RED}" stroke-width="1.6"/>'
    s += f'<text x="{X(4)}" y="{BY - 38}" font-size="17" fill="{RED}" font-weight="bold" text-anchor="end">12 kN/m</text></g>'
    s += ('<g id="sup" style="transition: opacity 0.5s">'
          f'<polygon points="{X(1)},{BY + BH} {X(1) - 10},{BY + BH + 16} {X(1) + 10},{BY + BH + 16}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
          f'<polygon points="{X(4)},{BY + BH} {X(4) - 10},{BY + BH + 13} {X(4) + 10},{BY + BH + 13}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
          f'<circle cx="{X(4) - 5}" cy="{BY + BH + 16}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'
          f'<circle cx="{X(4) + 5}" cy="{BY + BH + 16}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/></g>')
    s += f'<text x="{X(1) - 8}" y="{BY - 6}" font-size="17" text-anchor="end" font-style="italic">A</text>'
    s += f'<text x="{X(4) + 10}" y="{BY - 6}" font-size="17" font-style="italic">B</text>'
    for a, b, t in ((0, 1, "1 m"), (1, 4, "3 m")):
        s += f'<line x1="{X(a) + 2}" y1="{BY + 100}" x2="{X(b) - 2}" y2="{BY + 100}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X((a + b) / 2)}" y="{BY + 116}" font-size="14" fill="{GREY}" text-anchor="middle">{t}</text>'
    s += '</g><g data-step="2">' + lib.hreact(X(1), BY + BH, "A", 3)
    for xm, R, nm in ((1, 32, "A"), (4, 16, "B")):
        s += f'<line x1="{X(xm)}" y1="{BY + 86}" x2="{X(xm)}" y2="{BY + BH + 3}" stroke="{NAVY}" stroke-width="3" marker-end="url(#a_002060)"/>'
        if nm == "A":
            s += (f'<text x="{X(xm) + 8}" y="{BY + 78}" font-size="18" fill="{NAVY}" font-weight="bold">{sym("R", nm + "y")}</text>'
                  f'<text data-step="3" x="{X(xm) + 40}" y="{BY + 78}" font-size="17" fill="{NAVY}" font-weight="bold">= {R} kN</text>')
        else:
            s += (f'<text x="{X(xm) - 8}" y="{BY + 78}" font-size="18" fill="{NAVY}" font-weight="bold" text-anchor="end">{sym("R", nm + "y")}</text>'
                  f'<text data-step="3" x="{X(xm) - 46}" y="{BY + 78}" font-size="17" fill="{NAVY}" font-weight="bold" text-anchor="end">{R} kN =</text>')
    for y, lab, unit in ((VB, "V", "kN"), (MB, "M", "kN·m")):
        s += f'<line x1="{X(0)}" y1="{y}" x2="{X(4) + 22}" y2="{y}" stroke="#000" stroke-width="1.2" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X(0) - 8}" y="{y + 5}" font-size="16" text-anchor="end">{sym(lab)} ({unit})</text>'
    s += '</g>'
    # click 3: the load resultant used for the reactions
    s += (f'<g data-step="3"><line x1="{X(2)}" y1="{BY - 80}" x2="{X(2)}" y2="{BY - 3}" stroke="{RED}" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#a_C00000)"/>'
          f'<text x="{X(2) - 8}" y="{BY - 62}" font-size="15" fill="{RED}" text-anchor="end">resultant 12(4) = 48 kN</text></g>')
    # clicks 4-5: one cut each, its piece of V and M
    for n, (a, b, xc) in enumerate(CUTS):
        g = f'<g data-step="{n + 4}">'
        g += (f'<line x1="{X(xc)}" y1="{BY - 34}" x2="{X(xc)}" y2="{MB + 50}" stroke="{RED}" stroke-width="1.4" stroke-dasharray="6 4"/>'
              f'<circle cx="{X(xc)}" cy="{MB + 62}" r="10" fill="{RED}"/>'
              f'<text x="{X(xc)}" y="{MB + 67}" font-size="14" fill="#fff" text-anchor="middle" font-weight="bold">{n + 1}</text>')
        vp = [(a, 0)] + [(a + (b - a) * i / 40, V_at(a + (b - a) * i / 40 + (1e-9 if i == 0 else 0))) for i in range(41)] + [(b, 0)]
        g += '<polygon points="' + " ".join(f"{X(x):.1f},{VB - VS * v:.1f}" for x, v in vp) + f'" fill="{TAU}" fill-opacity="0.15" stroke="none"/>'
        line = [(a, V_at(a - 1e-9) if a > 0 else 0)] + vp[1:-1] + ([(b, 0)] if b == 4 else [])
        g += '<polyline points="' + " ".join(f"{X(x):.1f},{VB - VS * v:.1f}" for x, v in line) + f'" fill="none" stroke="{TAU}" stroke-width="2.4"/>'
        mp = [(a + (b - a) * i / 60, M_at(a + (b - a) * i / 60)) for i in range(61)]
        g += '<polygon points="' + " ".join(f"{X(x):.1f},{MB - MS * mm:.1f}" for x, mm in [(a, 0)] + mp + [(b, 0)]) + f'" fill="{MC}" fill-opacity="0.15" stroke="none"/>'
        g += '<polyline points="' + " ".join(f"{X(x):.1f},{MB - MS * mm:.1f}" for x, mm in mp) + f'" fill="none" stroke="{MC}" stroke-width="2.4"/>'
        if n == 0:
            g += (f'<text x="{X(1) - 6}" y="{VB + VS * 12 + 16}" font-size="15" fill="{TAU}" font-weight="bold" text-anchor="end">−12</text>'
                  f'<text x="{X(1)}" y="{MB + MS * 6 + 18}" font-size="15" fill="{MC}" font-weight="bold" text-anchor="middle">−6</text>')
        else:
            g += (f'<text x="{X(1) + 6}" y="{VB - VS * 20 - 6}" font-size="15" fill="{TAU}" font-weight="bold">+20</text>'
                  f'<text x="{X(4) - 6}" y="{VB + VS * 16 + 16}" font-size="15" fill="{TAU}" font-weight="bold" text-anchor="end">−16</text>'
                  f'<text x="{X(4) - 4}" y="{MB + 18}" font-size="15" fill="{MC}" font-weight="bold" text-anchor="end">0 ✓</text>')
        s += g + '</g>'
    # click 6: maximum M where V = 0
    s += (f'<g data-step="6"><line x1="{X(XM)}" y1="{VB - 20}" x2="{X(XM)}" y2="{MB}" stroke="{RED}" stroke-width="1.4" stroke-dasharray="3 3"/>'
          f'<circle cx="{X(XM)}" cy="{VB}" r="5" fill="{RED}"/><circle cx="{X(XM)}" cy="{MB - MS * 32 / 3:.1f}" r="5" fill="{RED}"/>'
          f'<text x="{X(XM) + 8}" y="{VB - 8}" font-size="15" fill="{RED}" font-weight="bold">{sym("V")} = 0</text>'
          f'<text x="{X(XM)}" y="{MB - MS * 32 / 3 - 10:.1f}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="middle">10.67 = {sym("M", "max")}</text>'
          f'<text x="{X(1) + 40}" y="{VB - VS * 20 - 6}" font-size="15" fill="{RED}" font-weight="bold">= {sym("V", "max")}</text></g>')
    return f'<svg class="fig" style="left:20px; top:122px" width="520" height="540" viewBox="0 0 520 540">{s}</svg>'


def fbd(n):
    """Left piece for cut n: load, R_A (cut 2 only), V down and M counterclockwise on the cut face, length x."""
    k, x0, y = 68, 22, 50
    xc = CUTS[n][2]
    xe = x0 + k * xc
    s = f'<rect x="{x0}" y="{y}" width="{k * xc}" height="12" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.3"/>'
    for i in range(int(xc * 4) + 1):
        xa = x0 + k * xc * i / int(xc * 4) if xc * 4 >= 1 else x0
        s += f'<line x1="{xa:.1f}" y1="{y - 16}" x2="{xa:.1f}" y2="{y - 2}" stroke="{RED}" stroke-width="1.4" marker-end="url(#a_C00000)"/>'
    s += f'<line x1="{x0}" y1="{y - 16}" x2="{xe}" y2="{y - 16}" stroke="{RED}" stroke-width="1.4"/>'
    s += f'<text x="{x0 + k * xc / 2:.1f}" y="{y - 22}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="middle">12<tspan font-style="italic">x</tspan></text>'
    if xc > 1:
        s += f'<line x1="{x0 + k}" y1="{y + 44}" x2="{x0 + k}" y2="{y + 15}" stroke="{NAVY}" stroke-width="2.4" marker-end="url(#a_002060)"/>'
        s += f'<text x="{x0 + k + 4}" y="{y + 44}" font-size="13" fill="{NAVY}" font-weight="bold">{sym("R", "Ay")} = 32</text>'
    s += f'<line x1="{xe + 3}" y1="{y - 22}" x2="{xe + 3}" y2="{y + 12}" stroke="{TAU}" stroke-width="2.4" marker-end="url(#a_1f7a5a)"/>'
    s += f'<text x="{xe + 9}" y="{y - 22}" font-size="15" fill="{TAU}" font-weight="bold">{sym("V")}</text>'
    s += f'<path d="M{xe + 10},{y + 28} A20,20 0 0,0 {xe + 10},{y - 12}" fill="none" stroke="{MC}" stroke-width="2.2" marker-end="url(#a_c27c0e)"/>'
    s += f'<text x="{xe + 34}" y="{y + 12}" font-size="15" fill="{MC}" font-weight="bold">{sym("M")}</text>'
    s += (f'<line x1="{x0}" y1="{y + 50}" x2="{xe}" y2="{y + 50}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
          f'<text x="{(x0 + xe) / 2}" y="{y + 64}" font-size="15" fill="{GREY}" text-anchor="middle">{sym("x")}</text>')
    return f'<svg width="252" height="103" viewBox="0 -2 290 118">{s}</svg>'


def m(x):
    return f"<math>{x}</math>"


def build():
    u = lambda t: f"<mspace width='0.2em'/><mtext>{t}</mtext>"
    imp = "<mspace width='0.4em'/><mo>⇒</mo><mspace width='0.2em'/>"
    VV, MM = "<mi mathcolor='%s'>V</mi>" % TAU, "<mi mathcolor='%s'>M</mi>" % MC
    P = lambda t: f"<mo stretchy='false'>(</mo>{t}<mo stretchy='false'>)</mo>"
    half = "<mn>12</mn><mi>x</mi>" + P("<mi>x</mi><mo>/</mo><mn>2</mn>")
    eqs = [
        (f"<mo>−</mo><mn>12</mn><mi>x</mi><mo>−</mo>{VV}<mo>=</mo><mn>0</mn>{imp}{VV}<mo>=</mo><mo>−</mo><mn>12</mn><mi>x</mi>",
         f"{MM}<mo>+</mo>{half}<mo>=</mo><mn>0</mn>{imp}{MM}<mo>=</mo><mo>−</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup>",
         f"<mi>x</mi><mo>=</mo><mn>1</mn><mo>:</mo><mspace width='0.4em'/>{VV}<mo>=</mo><mn>−12</mn>{u('kN')},<mspace width='0.4em'/>{MM}<mo>=</mo><mn>−6</mn>{u('kN·m')}"),
        (f"<mn>32</mn><mo>−</mo><mn>12</mn><mi>x</mi><mo>−</mo>{VV}<mo>=</mo><mn>0</mn>{imp}{VV}<mo>=</mo><mn>32</mn><mo>−</mo><mn>12</mn><mi>x</mi>",
         f"{MM}<mo>+</mo>{half}<mo>−</mo><mn>32</mn>{P('<mi>x</mi><mo>−</mo><mn>1</mn>')}<mo>=</mo><mn>0</mn>|{imp}{MM}<mo>=</mo><mn>32</mn>{P('<mi>x</mi><mo>−</mo><mn>1</mn>')}<mo>−</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup>",
         f"<mi>x</mi><mo>=</mo><mn>4</mn><mo>:</mo><mspace width='0.4em'/>{VV}<mo>=</mo><mn>−16</mn>{u('kN')},<mspace width='0.4em'/>{MM}<mo>=</mo><mn>0</mn><mspace width='0.3em'/><mtext>✓</mtext>"),
    ]
    ranges = [m(f"<mn>{a}</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>{b}</mn>" + u("m")) for a, b, _ in CUTS]
    panels = ""
    for n in range(2):
        fv, mv, end = eqs[n]
        panels += f'''  <div class="cutp" data-step="{n + 4}">
    <div class="fb">{fbd(n)}</div>
    <div class="ce"><div class="ct"><span class="cn">{n + 1}</span>Cut {n + 1}: {ranges[n]}</div>
      <div><span class="lab"><math><mo>∑</mo><msub><mi>F</mi><mi>y</mi></msub><mo>=</mo><mn>0</mn></math></span> {m(fv)}</div>
      <div><span class="lab"><math><mo>∑</mo><msub><mi>M</mi><mtext>cut</mtext></msub><mo>=</mo><mn>0</mn></math></span> {'</div><div class="end">'.join(m(t) for t in mv.split('|'))}</div>
      <div class="end">{m(end)}</div></div>
  </div>
'''
    SM = "<mo>∑</mo>"
    SALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
    TALL = "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
    RA, RB = "<msub><mi>R</mi><mrow><mi>A</mi><mi>y</mi></mrow></msub>", "<msub><mi>R</mi><mrow><mi>B</mi><mi>y</mi></mrow></msub>"
    right = f"""
  <div class="given" data-step="1"><span class="gh">Problem</span>&nbsp; A laminated wood beam carries 12 kN/m (Fig. 15-8). Height = 1.5 × width <i>a</i>.
    {m(SALL + '<mo>=</mo><mn>9</mn>' + u('MPa'))}, {m(TALL + '<mo>=</mo><mn>0.6</mn>' + u('MPa'))}.
    <span class="gf"><b>Find:</b> the smallest width <i>a</i>.</span></div>
  <div class="steps">
  <div class="step" data-step="3"><b>Reactions</b> (whole beam; load resultant 48 kN at 2 m from <i>B</i>)
    <div class="eqs">{m(SM + '<msub><mi>M</mi><mi>B</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.4em"/><mo>−</mo>' + RA + P('<mn>3</mn>') + '<mo>+</mo><mn>48</mn>' + P('<mn>2</mn>') + '<mo>=</mo><mn>0</mn>' + imp + RA + '<mo>=</mo><mn>32</mn>' + u('kN'))}<br>
    {m('<mo>∑</mo><msub><mi>F</mi><mi>x</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.3em"/><msub><mi>R</mi><mrow><mi>A</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mspace width="0.8em"/>' + SM + '<msub><mi>F</mi><mi>y</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.4em"/>' + RA + '<mo>+</mo>' + RB + '<mo>−</mo><mn>48</mn><mo>=</mo><mn>0</mn>' + imp + RB + '<mo>=</mo><mn>16</mn>' + u('kN'))}</div>
    <div class="conv"><i>x</i> from the free left end. Keep the <b>left</b> piece; <span style="color:{TAU}"><i>V</i> down</span>, <span style="color:{MC}"><i>M</i> counterclockwise</span> (positive).</div></div>
{panels}  <div class="step" data-step="6"><b>Largest values</b>
    <div class="eqs">{m(VV + '<mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.4em"/><mn>32</mn><mo>−</mo><mn>12</mn><mi>x</mi><mo>=</mo><mn>0</mn>' + imp + '<mi>x</mi><mo>=</mo><mn>2.67</mn>' + u('m'))}<br>
    {m('<msub><mi>M</mi><mtext>max</mtext></msub><mo>=</mo><mn>32</mn>' + P('<mn>1.67</mn>') + '<mo>−</mo><mn>6</mn><msup><mrow>' + P('<mn>2.67</mn>') + '</mrow><mn>2</mn></msup><mo>=</mo><mn>10.67</mn>' + u('kN·m'))},&nbsp;
    {m('<msub><mi>V</mi><mtext>max</mtext></msub><mo>=</mo><mn>20</mn>' + u('kN'))}</div>
    <div class="conv">Max <i>M</i> sits where <i>V</i> = 0 (slope of <i>M</i> = <i>V</i>).</div></div>
  </div>"""

    css = lib.TEXT_CSS + f"""
  .given {{ position: absolute; left: 556px; top: 104px; width: 656px; padding: 6px 14px 8px; font-size: 16px; line-height: 1.45;
            border: 2px solid {NAVY}; border-left-width: 7px; border-radius: 6px; }}
  .given math {{ font-size: 19px; font-weight: bold; }}
  .gh {{ font-size: 13px; font-weight: bold; color: {NAVY}; text-transform: uppercase; letter-spacing: 1px; }}
  .gf {{ color: {RED}; }}
  .steps {{ position: absolute; left: 556px; top: 192px; width: 690px; display: flex; flex-direction: column; gap: 14px; }}  /* uniform step spacing */
  .step {{ font-size: 18px; padding-left: 4px; }}
  .eqs {{ margin: 2px 0 0 0; line-height: 1.6; }}
  .eqs math {{ font-size: 18px; }}
  .conv {{ font-size: 15px; color: #333; margin-top: 2px; }}
  .cutp {{ min-height: 104px; display: flex; align-items: flex-start; }}
  .fb {{ width: 262px; flex: none; }}
  .ce {{ font-size: 15px; line-height: 1.55; padding-top: 4px; }}
  .ce math {{ font-size: 17px; }}
  .ct {{ font-weight: bold; color: {NAVY}; font-size: 16px; }}
  .ct math {{ font-size: 17px; color: {NAVY}; }}
  .cn {{ display: none; }}  /* 'Cut n:' already numbers the row */
  .lab {{ display: inline-block; width: 104px; color: {GREY}; }}
  .lab math {{ font-size: 15px; }}
  .end {{ padding-left: 104px; }}
  .end math {{ font-size: 16px; color: #333; }}
"""
    js = """<script>
  // supports are replaced by the reactions on click 2 (the deck sends buildstep with the click count k)
  addEventListener('buildstep', e => {
    document.getElementById('sup').style.opacity = e.detail.k >= 2 ? 0 : 1;
    // click 3 only: the distributed load fades back while its 48 kN resultant stands in for it
    document.getElementById('wload').style.opacity = e.detail.k === 3 ? 0.2 : 1;
  });
</script>"""
    title = 'Example 15.2 (1/2): draw the <span class="key"><i>V</i> and <i>M</i></span> diagrams'
    body = left_svg() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.2, p. 695, Fig. 15-8. V and M by the method of sections.</div>')
    lib.write_page("14a_slide14_vm152.html", "Slide 14 - Ex 15.2 V and M", title, body, 14, css)
    print("V:", [round(V_at(x), 2) for x in (1 - 1e-9, 1.0001, 4)], "M:", [round(M_at(x), 2) for x in (1, XM, 4)])


if __name__ == "__main__":
    build()
