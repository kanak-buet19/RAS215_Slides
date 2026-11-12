"""Slide 12 - How to draw the V and M diagrams by cutting the beam (Example 15.1 beam; before Ex 15.1).

Method of sections, one cut per region between loads. For each cut the LEFT piece is drawn as a
free body with V and M on its cut face, drawn positive (book's convention: on the left piece's right
face, V acts down and M counterclockwise), and the two equilibrium equations give V(x) and M(x):
  cut 1, 0 < x < 6:   10 - V = 0 -> V = 10;              M - 10x = 0 -> M = 10x            (60 at x = 6)
  cut 2, 6 < x < 12:  10 - 40 - V = 0 -> V = -30;        M = 10x - 40(x - 6)               (-120 at x = 12)
  cut 3, 12 < x < 18: 10 - 40 + 50 - V = 0 -> V = 20;    M = 10x - 40(x - 6) + 50(x - 12)  (0 at x = 18)
Clicks: 1 beam with its supports, 2 supports removed and replaced by R_A, R_B (free body), 3 reactions solved (values appear beside the arrows), 4-6 one cut each (FBD + equations on the right, that piece of the V and M
diagrams and the cut line on the left), 7 shortcut box (jumps and areas).
Beam and numbers: Ex. 15.1, p. 694, Fig. 15-7. The method is from the book's earlier chapter on V and M
diagrams (not in the Ch. 15 pages).

Writes ../slides/separate/13a_slide12_vm.html.
Run:  python3 16_make_slide12_vm.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, ST, SUP, TAU = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT, lib.TAU
sym = lib.sym
MC = "#c27c0e"

X0, PF = 80, 20
BY, VB, VS, MB, MS = 70, 266, 2.0, 440, 0.8
X = lambda ft: X0 + PF * ft
CUTS = [(0, 6, 4), (6, 12, 9), (12, 18, 15)]      # region start, end, where the cut is drawn (ft)


def M_at(x):
    return 10 * x - 40 * max(0, x - 6) + 50 * max(0, x - 12)


def V_at(x):
    return 10 - 40 * (x > 6) + 50 * (x > 12)


def left_svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY, TAU, MC)}</defs>'
    s += '<g data-step="1">'
    s += lib.wbeam_elev(X(0), BY, PF * 18, 26)
    s += lib.wbeam_end_view(X(18), X(18) + 46, BY, 26, 'end view', '')
    # supports: shown on click 1, removed on click 2 (replaced by the reactions) - see the script below
    s += ('<g id="sup" style="transition: opacity 0.5s">'
          f'<polygon points="{X(0)},{BY + 26} {X(0) - 10},{BY + 42} {X(0) + 10},{BY + 42}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
          f'<polygon points="{X(12)},{BY + 26} {X(12) - 10},{BY + 39} {X(12) + 10},{BY + 39}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
          f'<circle cx="{X(12) - 5}" cy="{BY + 42}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'
          f'<circle cx="{X(12) + 5}" cy="{BY + 42}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/></g>')
    for ft, P in ((6, 40), (18, 20)):
        s += f'<line x1="{X(ft)}" y1="{BY - 44}" x2="{X(ft)}" y2="{BY - 3}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>'
        s += f'<text x="{X(ft)}" y="{BY - 50}" font-size="17" fill="{RED}" text-anchor="middle" font-weight="bold">{P} kip</text>'
    s += f'<text x="{X(0) - 8}" y="{BY - 6}" font-size="17" text-anchor="end" font-style="italic">A</text>'
    s += f'<text x="{X(12) + 14}" y="{BY - 6}" font-size="17" font-style="italic">B</text>'
    for a in (0, 6, 12):
        s += f'<line x1="{X(a) + 2}" y1="{BY + 100}" x2="{X(a + 6) - 2}" y2="{BY + 100}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X(a + 3)}" y="{BY + 116}" font-size="14" fill="{GREY}" text-anchor="middle">6 ft</text>'
    s += '</g><g data-step="2">' + lib.hreact(X(0), BY + 26, "A", 3)
    for ft, R in ((0, 10), (12, 50)):
        s += f'<line x1="{X(ft)}" y1="{BY + 86}" x2="{X(ft)}" y2="{BY + 28}" stroke="{NAVY}" stroke-width="3" marker-end="url(#a_002060)"/>'
        nm = "A" if ft == 0 else "B"
        s += (f'<text x="{X(ft) + 8}" y="{BY + 78}" font-size="18" fill="{NAVY}" font-weight="bold">{sym("R", nm + "y")}</text>'
              f'<text data-step="3" x="{X(ft) + 40}" y="{BY + 78}" font-size="17" fill="{NAVY}" font-weight="bold">= {R} kip</text>')
    for y, lab, unit in ((VB, "V", "kip"), (MB, "M", "kip·ft")):
        s += f'<line x1="{X(0)}" y1="{y}" x2="{X(18) + 22}" y2="{y}" stroke="#000" stroke-width="1.2" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X(0) - 10}" y="{y + 5}" font-size="16" text-anchor="end">{sym(lab)} ({unit})</text>'
    s += '</g>'
    # one group per cut: cut line, its piece of V and M, end values
    for n, (a, b, xc) in enumerate(CUTS):
        v = V_at((a + b) / 2)
        g = f'<g data-step="{n + 4}">'
        g += (f'<line x1="{X(xc)}" y1="{BY - 18}" x2="{X(xc)}" y2="{MB + 100}" stroke="{RED}" stroke-width="1.4" stroke-dasharray="6 4"/>'
              f'<circle cx="{X(xc)}" cy="{BY - 26}" r="10" fill="{RED}"/>'
              f'<text x="{X(xc)}" y="{BY - 21}" font-size="14" fill="#fff" text-anchor="middle" font-weight="bold">{n + 1}</text>')
        v_prev = V_at(a - 0.01) if a > 0 else 0
        g += (f'<polygon points="{X(a)},{VB} {X(a)},{VB - VS * v} {X(b)},{VB - VS * v} {X(b)},{VB}" fill="{TAU}" fill-opacity="0.15" stroke="none"/>'
              f'<line x1="{X(a)}" y1="{VB - VS * v_prev}" x2="{X(a)}" y2="{VB - VS * v}" stroke="{TAU}" stroke-width="2.4"/>'
              f'<line x1="{X(a)}" y1="{VB - VS * v}" x2="{X(b)}" y2="{VB - VS * v}" stroke="{TAU}" stroke-width="2.4"/>')
        if b == 18:
            g += f'<line x1="{X(b)}" y1="{VB - VS * v}" x2="{X(b)}" y2="{VB}" stroke="{TAU}" stroke-width="2.4"/>'
        g += f'<text x="{X((a + b) / 2)}" y="{VB - VS * v + (-8 if v > 0 else 20)}" font-size="16" fill="{TAU}" font-weight="bold" text-anchor="middle">{("+" if v > 0 else "−") + str(abs(v))}</text>'
        g += (f'<polygon points="{X(a)},{MB} {X(a)},{MB - MS * M_at(a)} {X(b)},{MB - MS * M_at(b)} {X(b)},{MB}" fill="{MC}" fill-opacity="0.15" stroke="none"/>'
              f'<line x1="{X(a)}" y1="{MB - MS * M_at(a)}" x2="{X(b)}" y2="{MB - MS * M_at(b)}" stroke="{MC}" stroke-width="2.4"/>')
        mb = M_at(b)
        lab = (str(mb) if mb >= 0 else "−" + str(-mb)) if b < 18 else "0 ✓"
        g += f'<text x="{X(b) + (0 if b < 18 else -4)}" y="{MB - MS * mb + (-10 if mb >= 0 else 22)}" font-size="16" fill="{MC}" font-weight="bold" text-anchor="{"middle" if b < 18 else "end"}">{lab}</text>'
        s += g + '</g>'
    return f'<svg class="fig" style="left:20px; top:122px" width="520" height="560" viewBox="0 0 520 560">{s}</svg>'


def fbd(n):
    """Free-body diagram of the left piece for cut n (0, 1, 2); V down and M counterclockwise (positive)."""
    k, x0, y = 13.5, 22, 46
    xc = CUTS[n][2]
    xe = x0 + k * xc
    s = f'<rect x="{x0}" y="{y}" width="{k * xc}" height="12" fill="{ST["front"]}" stroke="{ST["edge"]}" stroke-width="1.3"/>'
    s += f'<line x1="{xe}" y1="{y - 6}" x2="{xe}" y2="{y + 18}" stroke="{RED}" stroke-width="1.3" stroke-dasharray="4 3"/>'
    s += f'<line x1="{x0}" y1="{y + 44}" x2="{x0}" y2="{y + 15}" stroke="{NAVY}" stroke-width="2.4" marker-end="url(#a_002060)"/>'
    s += f'<text x="{x0 + 4}" y="{y + 44}" font-size="13" fill="{NAVY}" font-weight="bold">{sym("R", "Ay")} = 10</text>'
    if xc > 6:
        s += f'<line x1="{x0 + 6 * k}" y1="{y - 32}" x2="{x0 + 6 * k}" y2="{y - 3}" stroke="{RED}" stroke-width="2.4" marker-end="url(#a_C00000)"/>'
        s += f'<text x="{x0 + 6 * k + 4}" y="{y - 22}" font-size="13" fill="{RED}" font-weight="bold">40</text>'
    if xc > 12:
        s += f'<line x1="{x0 + 12 * k}" y1="{y + 44}" x2="{x0 + 12 * k}" y2="{y + 15}" stroke="{NAVY}" stroke-width="2.4" marker-end="url(#a_002060)"/>'
        s += f'<text x="{x0 + 12 * k + 4}" y="{y + 44}" font-size="13" fill="{NAVY}" font-weight="bold">{sym("R", "By")} = 50</text>'
    # V down on the cut face, M counterclockwise around it
    s += f'<line x1="{xe + 3}" y1="{y - 22}" x2="{xe + 3}" y2="{y + 12}" stroke="{TAU}" stroke-width="2.4" marker-end="url(#a_1f7a5a)"/>'
    s += f'<text x="{xe - 4}" y="{y - 22}" font-size="15" fill="{TAU}" font-weight="bold" text-anchor="end">{sym("V")}</text>'
    s += f'<path d="M{xe + 10},{y + 28} A20,20 0 0,0 {xe + 10},{y - 12}" fill="none" stroke="{MC}" stroke-width="2.2" marker-end="url(#a_c27c0e)"/>'
    s += f'<text x="{xe + 34}" y="{y + 12}" font-size="15" fill="{MC}" font-weight="bold">{sym("M")}</text>'
    s += (f'<line x1="{x0}" y1="{y + 56}" x2="{xe}" y2="{y + 56}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
          f'<text x="{(x0 + xe) / 2}" y="{y + 70}" font-size="15" fill="{GREY}" text-anchor="middle">{sym("x")}</text>')
    return f'<svg width="252" height="103" viewBox="0 -2 290 118">{s}</svg>'


def m(x):
    return f"<math>{x}</math>"


def build():
    u = lambda t: f"<mspace width='0.2em'/><mtext>{t}</mtext>"
    imp = "<mspace width='0.4em'/><mo>⇒</mo><mspace width='0.2em'/>"
    VV, MM = "<mi mathcolor='%s'>V</mi>" % TAU, "<mi mathcolor='%s'>M</mi>" % MC
    eqs = [
        (f"<mn>10</mn><mo>−</mo>{VV}<mo>=</mo><mn>0</mn>{imp}{VV}<mo>=</mo><mn>10</mn>{u('kip')}",
         f"{MM}<mo>−</mo><mn>10</mn><mi>x</mi><mo>=</mo><mn>0</mn>{imp}{MM}<mo>=</mo><mn>10</mn><mi>x</mi>",
         "<mi>x</mi><mo>=</mo><mn>6</mn><mo>:</mo><mspace width='0.4em'/>" + MM + "<mo>=</mo><mn>60</mn>"),
        (f"<mn>10</mn><mo>−</mo><mn>40</mn><mo>−</mo>{VV}<mo>=</mo><mn>0</mn>{imp}{VV}<mo>=</mo><mn>−30</mn>{u('kip')}",
         f"{MM}<mo>=</mo><mn>10</mn><mi>x</mi><mo>−</mo><mn>40</mn><mo>(</mo><mi>x</mi><mo>−</mo><mn>6</mn><mo>)</mo>",
         "<mi>x</mi><mo>=</mo><mn>12</mn><mo>:</mo><mspace width='0.4em'/>" + MM + "<mo>=</mo><mn>−120</mn>"),
        (f"<mn>10</mn><mo>−</mo><mn>40</mn><mo>+</mo><mn>50</mn><mo>−</mo>{VV}<mo>=</mo><mn>0</mn>{imp}{VV}<mo>=</mo><mn>20</mn>{u('kip')}",
         f"{MM}<mo>=</mo><mn>10</mn><mi>x</mi><mo>−</mo><mn>40</mn><mo>(</mo><mi>x</mi><mo>−</mo><mn>6</mn><mo>)</mo><mo>+</mo><mn>50</mn><mo>(</mo><mi>x</mi><mo>−</mo><mn>12</mn><mo>)</mo>",
         "<mi>x</mi><mo>=</mo><mn>18</mn><mo>:</mo><mspace width='0.4em'/>" + MM + "<mo>=</mo><mn>0</mn><mspace width='0.3em'/><mtext>✓</mtext>"),
    ]
    ranges = [m(f"<mn>{a}</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>{b}</mn>" + u("ft")) for a, b in ((0, 6), (6, 12), (12, 18))]
    panels = ""
    for n in range(3):
        fv, mv, end = eqs[n]
        panels += f'''  <div class="cutp" data-step="{n + 4}" style="top:{300 + n * 106}px">
    <div class="fb">{fbd(n)}</div>
    <div class="ce"><div class="ct"><span class="cn">{n + 1}</span>Cut {n + 1}: {ranges[n]}</div>
      <div><span class="lab"><math><mo>∑</mo><msub><mi>F</mi><mi>y</mi></msub><mo>=</mo><mn>0</mn></math></span> {m(fv)}</div>
      <div><span class="lab"><math><mo>∑</mo><msub><mi>M</mi><mtext>cut</mtext></msub><mo>=</mo><mn>0</mn></math></span> {m(mv)}</div>
      <div class="end">{m(end)}</div></div>
  </div>
'''
    SM = "<mo>∑</mo>"
    SALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
    TALL = "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
    right = f"""
  <div class="given" data-step="1"><span class="gh">Problem</span>&nbsp; A steel beam carries the loads shown (Fig. 15-7).
    {m(SALL + '<mo>=</mo><mn>24</mn>' + u('ksi'))}, {m(TALL + '<mo>=</mo><mn>14.5</mn>' + u('ksi'))}.
    <span class="gf"><b>Find:</b> the lightest W-shape.</span> First step: the <i>V</i> and <i>M</i> diagrams.</div>
  <div class="step" data-step="3" style="top:196px"><b>Reactions</b> (whole beam)
    <div class="eqs">{m(SM + '<msub><mi>M</mi><mi>A</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.4em"/><msub><mi>R</mi><mrow><mi>B</mi><mi>y</mi></mrow></msub><mo>(</mo><mn>12</mn><mo>)</mo><mo>−</mo><mn>40</mn><mo>(</mo><mn>6</mn><mo>)</mo><mo>−</mo><mn>20</mn><mo>(</mo><mn>18</mn><mo>)</mo><mo>=</mo><mn>0</mn>' + imp + '<msub><mi>R</mi><mrow><mi>B</mi><mi>y</mi></mrow></msub><mo>=</mo><mn>50</mn>' + u('kip'))}<br>
    {m('<mo>∑</mo><msub><mi>F</mi><mi>x</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.3em"/><msub><mi>R</mi><mrow><mi>A</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>,</mo><mspace width="0.8em"/>' + SM + '<msub><mi>F</mi><mi>y</mi></msub><mo>=</mo><mn>0</mn><mo>:</mo><mspace width="0.4em"/><msub><mi>R</mi><mrow><mi>A</mi><mi>y</mi></mrow></msub><mo>+</mo><msub><mi>R</mi><mrow><mi>B</mi><mi>y</mi></mrow></msub><mo>−</mo><mn>40</mn><mo>−</mo><mn>20</mn><mo>=</mo><mn>0</mn>' + imp + '<msub><mi>R</mi><mrow><mi>A</mi><mi>y</mi></mrow></msub><mo>=</mo><mn>10</mn>' + u('kip'))}</div>
    <div class="conv">Then cut in each region and keep the <b>left</b> piece. Draw <i>V</i> and <i>M</i> positive: <span style="color:{TAU}"><i>V</i> down</span>, <span style="color:{MC}"><i>M</i> counterclockwise</span>.</div></div>
{panels}  <div class="rules" data-step="7"><b>Shortcut</b> (same result): a point force makes <i>V</i> jump by its size; the change in <i>M</i> = area under <i>V</i>; both end at 0.</div>"""

    css = lib.TEXT_CSS + f"""
  .step {{ position: absolute; left: 560px; width: 680px; font-size: 18px; }}
  .given {{ position: absolute; left: 556px; top: 104px; width: 656px; padding: 6px 14px 8px; font-size: 16px; line-height: 1.45;
            border: 2px solid {NAVY}; border-left-width: 7px; border-radius: 6px; }}
  .given math {{ font-size: 19px; font-weight: bold; }}
  .gh {{ font-size: 13px; font-weight: bold; color: {NAVY}; text-transform: uppercase; letter-spacing: 1px; }}
  .gf {{ color: {RED}; }}
  .eqs {{ margin: 4px 0 0 0; line-height: 1.6; }}
  .eqs math {{ font-size: 18px; }}
  .conv {{ font-size: 15px; color: #333; margin-top: 4px; }}
  .cutp {{ position: absolute; left: 548px; width: 720px; height: 104px; display: flex; align-items: flex-start; }}
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
  .rules {{ position: absolute; left: 560px; top: 622px; width: 660px; padding: 6px 12px; font-size: 15px;
           border: 2px solid {RED}; border-radius: 6px; }}
"""

    js = """<script>
  // supports are replaced by the reactions on click 2 (the deck sends buildstep with the click count k)
  addEventListener('buildstep', e => { document.getElementById('sup').style.opacity = e.detail.k >= 2 ? 0 : 1; });
</script>"""
    title = 'Example 15.1 (1/2): draw the <span class="key"><i>V</i> and <i>M</i></span> diagrams'
    body = left_svg() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.1, p. 694, Fig. 15-7. V and M by the method of sections.</div>')
    lib.write_page("13a_slide12_vm.html", "Slide 12 - V and M diagrams", title, body, 12, css)
    print("M:", [M_at(x) for x in (6, 8, 12, 18)], "V:", [V_at(x) for x in (3, 9, 15)])


if __name__ == "__main__":
    build()
