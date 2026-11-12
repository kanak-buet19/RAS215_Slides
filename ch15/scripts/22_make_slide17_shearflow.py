"""Slide 17 - Why the nails carry the shear flow q = VQ/I (before the nail-spacing slide, Ex. 15.3).

Free body of one slice of the flange, length s, in region B-C of the Ex. 15.3 beam (M grows from B to C):
  force of the bending stress on one end of the flange:  F = integral(sigma dA) = (M/I) integral(y dA) = M Q / I
  left end F1 = M Q/I, right end F2 = (M + dM) Q/I, with dM = V s (slope of M is V)
  imbalance dF = F2 - F1 = V s Q / I -> must come from the joint (the nail)
  per unit length: q = dF/s = V Q / I (shear flow); one nail per spacing: F_nail = q s -> s = F/q
  Ex 15.3, B-C: q = 8.61 kN/m, s = 0.15 m -> each nail carries 1.29 kN <= 1.50 kN
The derivation is from the book's earlier chapter on shear flow (not in the Ch. 15 pages); numbers from p. 697.
Arrow lengths follow sigma = My/I over the flange (0.0425 m to 0.0725 m above the N.A.); dM is exaggerated.
Clicks: 1 slice on the beam, zoomed free body, length s; 2 bending pushes on both ends (arrows grow);
3 no nail: the slice slides toward the smaller push; 4 the nail holds it, nail force = dF;
5 shear flow along the joint, s = F/q, number check.

Writes ../slides/separate/16b_slide17_shearflow.html.
Run:  python3 22_make_slide17_shearflow.py
"""
import importlib

c = importlib.import_module("19_ex153_common")
lib, NAVY, RED, GREY, TAU, WOOD, sym, X, BY, BH = c.lib, c.NAVY, c.RED, c.GREY, c.TAU, c.WOOD, c.sym, c.X, c.BY, c.BH
m, ds, U, P, E, IMP = c.m, c.ds, c.U, c.P, c.E, c.IMP

XA, XB = 0.6, 1.3                     # slice drawn on the beam (m; wider than one nail spacing so it shows)
FX0, FX1, FY0, FY1 = 120, 360, 100, 146  # zoomed flange slice: front face
DX, DY = 96, -48                        # oblique direction of the flange width (into the page)
WH = 84                                 # web height shown
L2 = 80; L1 = round(L2 * c.M_at(0.6) / c.M_at(1.3))  # push arrows scale with M at each cut
SLIDE = 44                            # px the unnailed slice slides


MB, MS = 170, 34                      # small M diagram under the beam: baseline, px per kN.m
M1, M2 = c.M_at(XA), c.M_at(XB)       # real Ex 15.3 moments at the two cuts (0.81 and 1.53 kN.m)


def beam_svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY, TAU)}</defs><g data-step="1">' + c.beam(dims=False) + c.m_diagram(MB, MS)
    s += (f'<rect x="{X(XA)}" y="{BY}" width="{X(XB) - X(XA)}" height="{c.FT}" fill="{RED}" fill-opacity="0.55"/>'
          f'<line x1="{X(XA)}" y1="{BY - 4}" x2="{X(XA)}" y2="{MB}" stroke="{RED}" stroke-width="1.2" stroke-dasharray="4 3"/>'
          f'<line x1="{X(XB)}" y1="{BY - 4}" x2="{X(XB)}" y2="{MB}" stroke="{RED}" stroke-width="1.2" stroke-dasharray="4 3"/>'
          f'<text x="{X(XA) - 5}" y="{BY + BH + 34}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="end">flange slice</text></g>')
    # click 2: the moment at each cut, as a bar that grows on the M diagram
    s += (f'<g data-step="2"><line id="mb1" x1="{X(XA)}" x2="{X(XA)}" y1="{MB}" y2="{MB}" stroke="{RED}" stroke-width="5"/>'
          f'<line id="mb2" x1="{X(XB)}" x2="{X(XB)}" y1="{MB}" y2="{MB}" stroke="{RED}" stroke-width="5"/>'
          f'<g id="mlab" opacity="0"><text x="{X(XA) - 6}" y="{MB - MS * M1 / 2 + 5:.1f}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="end">{sym("M")}</text>'
          f'<text x="{X(XB) + 6}" y="{MB - MS * M2 / 2 + 5:.1f}" font-size="15" fill="{RED}" font-weight="bold">{sym("M")} + Δ{sym("M")} (bigger)</text></g></g>')
    # click 4: nails in the beam, one per slice: centre nail in the slice, neighbours one slice length away,
    # so the slice length s is the spacing between two nails (spacing drawn as large as the slice, exaggerated)
    sp = XB - XA
    g = '<g data-step="4"><g id="nailbeam" opacity="0">'
    for xm in ((XA + XB) / 2 - sp, (XA + XB) / 2, (XA + XB) / 2 + sp):
        g += (f'<line x1="{X(xm):.1f}" y1="{BY - 2}" x2="{X(xm):.1f}" y2="{BY + c.FT + 9}" stroke="#333" stroke-width="2.2"/>'
              f'<line x1="{X(xm) - 4:.1f}" y1="{BY - 2}" x2="{X(xm) + 4:.1f}" y2="{BY - 2}" stroke="#333" stroke-width="2.6"/>')
    x1, x2, yd = X((XA + XB) / 2), X((XA + XB) / 2 + sp), BY + BH + 30
    g += (f'<line x1="{x1:.1f}" y1="{BY + c.FT + 11}" x2="{x1:.1f}" y2="{yd + 4}" stroke="{NAVY}" stroke-width="1" stroke-dasharray="3 2"/>'
          f'<line x1="{x2:.1f}" y1="{BY + c.FT + 11}" x2="{x2:.1f}" y2="{yd + 4}" stroke="{NAVY}" stroke-width="1" stroke-dasharray="3 2"/>'
          f'<line x1="{x1 + 2:.1f}" y1="{yd}" x2="{x2 - 2:.1f}" y2="{yd}" stroke="{NAVY}" stroke-width="1.6" marker-start="url(#a_002060)" marker-end="url(#a_002060)"/>'
          f'<text x="{x2 + 8:.1f}" y="{yd + 5}" font-size="15" fill="{NAVY}" font-weight="bold">{sym("s")} = nail spacing</text></g></g>')
    s += g
    return f'<svg class="fig" style="left:40px; top:158px" width="620" height="180" viewBox="0 0 620 180">{s}</svg>'


OP = 0.55                               # wood fill opacity, so the nail inside shows


def poly(pts, fill, extra=' fill-opacity="0.55"'):
    return (f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" '
            f'stroke="{WOOD["edge"]}" stroke-width="1.4" stroke-linejoin="round"{extra}/>')


def zoom_svg():
    """3-D (oblique) piece of the T-beam, length s: the flange slice sits on the web. Beam length runs across the
    screen, the flange width runs into the page along (DX, DY). Push arrows land on the two end faces (JS)."""
    s = (f'<defs>{lib.markers(RED, NAVY, GREY, TAU)}'
         '<linearGradient id="nailG" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#5a5f66"/>'
         '<stop offset="0.45" stop-color="#e4e7ea"/><stop offset="1" stop-color="#4a4f55"/></linearGradient>'
         '<radialGradient id="nailH" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#f0f2f4"/>'
         '<stop offset="1" stop-color="#5a5f66"/></radialGradient></defs><g data-step="1">')
    s += f'<text x="8" y="284" font-size="14" fill="{GREY}">zoom: one slice, length {sym("s")}, holding one nail (3-D)</text>'
    # web: narrow in depth (t = 0.425 ... 0.575 of the flange width), hangs below the flange
    a, b = 0.425, 0.575
    wx0, wx1 = FX0 + a * DX, FX1 + a * DX
    wy = FY1 + a * DY
    s += poly([(wx1, wy), (FX1 + b * DX, FY1 + b * DY), (FX1 + b * DX, FY1 + b * DY + WH), (wx1, wy + WH)], "#b08a55")
    s += poly([(wx0, wy), (wx1, wy), (FX1 + b * DX, FY1 + b * DY), (FX0 + b * DX, FY1 + b * DY)], "#c7a06a")
    s += '</g>'
    # click 4: the interface (web top = contact with the flange) and the nail through it, both inside the wood
    nx, ny = (FX0 + FX1) / 2 + DX / 2, FY0 + DY / 2          # nail head: centre of the flange top face
    yj = ny + (FY1 - FY0)                                     # where the nail crosses the interface
    s += (f'<g data-step="4"><g id="nailin">'
          + poly([(wx0, wy), (wx1, wy), (FX1 + b * DX, FY1 + b * DY), (FX0 + b * DX, FY1 + b * DY)], RED, ' fill-opacity="0.45"')
          + f'<rect x="{nx - 3.2:.1f}" y="{ny:.1f}" width="6.4" height="{FY1 - FY0 + 52}" fill="url(#nailG)"/>'
          f'<polygon points="{nx - 3.2:.1f},{ny + FY1 - FY0 + 52:.1f} {nx + 3.2:.1f},{ny + FY1 - FY0 + 52:.1f} {nx:.1f},{ny + FY1 - FY0 + 62:.1f}" fill="#555"/>'
          f'<ellipse cx="{nx:.1f}" cy="{yj:.1f}" rx="9" ry="4" fill="none" stroke="{RED}" stroke-width="2"/></g></g>')
    s += '<g data-step="1">'
    s += f'<rect x="{wx0:.1f}" y="{wy:.1f}" width="{FX1 - FX0}" height="{WH}" fill="#d6b27a" fill-opacity="{OP}" stroke="{WOOD["edge"]}" stroke-width="1.4"/>'
    s += f'<text x="{wx0 + 14:.1f}" y="{wy + WH - 10:.1f}" font-size="14" fill="{WOOD["edge"]}">web</text>'
    s += (f'<line x1="{wx0:.1f}" y1="{wy + WH + 14:.1f}" x2="{wx1:.1f}" y2="{wy + WH + 14:.1f}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
          f'<text x="{(wx0 + wx1) / 2:.1f}" y="{wy + WH + 32:.1f}" font-size="16" text-anchor="middle">{sym("s")} = nail spacing</text>')
    s += '</g>'
    # the flange slice: left pushes (behind), faces, right pushes (in front); slides as one group
    g = '<g id="slice"><g data-step="2">'
    for i in range(4):
        for j in range(2):
            g += f'<line id="pl{i}{j}" stroke="{NAVY}" stroke-width="2.2" marker-end="url(#a_002060)"/>'
    g += '</g>'
    g += poly([(FX0, FY0), (FX1, FY0), (FX1 + DX, FY0 + DY), (FX0 + DX, FY0 + DY)], "#efd8ad")
    g += poly([(FX1, FY0), (FX1 + DX, FY0 + DY), (FX1 + DX, FY1 + DY), (FX1, FY1)], "#c9a46a")
    g += f'<rect x="{FX0}" y="{FY0}" width="{FX1 - FX0}" height="{FY1 - FY0}" fill="{WOOD["face"]}" fill-opacity="{OP}" stroke="{WOOD["edge"]}" stroke-width="1.4"/>'
    g += f'<text x="{FX0 + 12}" y="{FY0 + 20}" font-size="14" fill="{WOOD["edge"]}">flange</text>'
    g += '<g data-step="2">'
    for i in range(4):
        for j in range(2):
            g += f'<line id="pr{i}{j}" stroke="{NAVY}" stroke-width="2.2" marker-end="url(#a_002060)"/>'
    g += '</g>'
    g += (f'<g data-step="4"><line x1="{FX0 + 70}" y1="{FY1 - 10}" x2="{FX0 + 150}" y2="{FY1 - 10}" stroke="{TAU}" stroke-width="3.2" marker-end="url(#a_1f7a5a)"/>'
          f'<text x="{FX0 + 70}" y="{FY1 - 18}" font-size="15" fill="{TAU}" font-weight="bold">nail: Δ{sym("F")}</text></g>')
    s += g + '</g>'
    # nail head sits on the top face (outside the wood); interface label
    s += (f'<g data-step="4"><g id="nailhd"><rect x="{nx - 8:.1f}" y="{ny - 3:.1f}" width="16" height="3" fill="#5a5f66"/>'
          f'<ellipse cx="{nx:.1f}" cy="{ny - 3:.1f}" rx="8" ry="3.6" fill="url(#nailH)" stroke="#444" stroke-width="0.8"/></g>'
          f'<line x1="{nx - 10:.1f}" y1="{yj:.1f}" x2="{wx0 - 4:.1f}" y2="{yj + 40:.1f}" stroke="{RED}" stroke-width="1.2"/>'
          f'<text x="{wx0 - 8:.1f}" y="{yj + 40:.1f}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="end">nail crosses</text>'
          f'<text x="{wx0 - 8:.1f}" y="{yj + 56:.1f}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="end">the interface</text></g>')
    s += (f'<g data-step="2"><text x="{FX0 - 62}" y="{FY0 + 14}" font-size="16" fill="{NAVY}" font-weight="bold" text-anchor="middle">{sym("F", "1")}</text>'
          f'<text x="{FX0 - 62}" y="{FY0 + 30}" font-size="12" fill="{NAVY}" text-anchor="middle">from {sym("M")}</text>'
          f'<text x="{FX1 + DX + 30}" y="{FY0 + DY - 20}" font-size="16" fill="{NAVY}" font-weight="bold" text-anchor="middle">{sym("F", "2")} (bigger)</text>'
          f'<text x="{FX1 + DX + 30}" y="{FY0 + DY - 4}" font-size="12" fill="{NAVY}" text-anchor="middle">from {sym("M")} + Δ{sym("M")}</text></g>')
    xc = (FX0 + FX1) / 2 + DX / 2
    s += (f'<g data-step="3"><line x1="{xc + 40}" y1="{FY0 + DY - 22}" x2="{xc - 40}" y2="{FY0 + DY - 22}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>'
          f'<text x="{xc}" y="{FY0 + DY - 32}" font-size="15" fill="{RED}" font-weight="bold" text-anchor="middle">net: Δ{sym("F")} = {sym("F", "2")} − {sym("F", "1")}</text>'
          f'<text id="slidetxt" x="{wx0 - 8:.1f}" y="{FY1 + 70}" font-size="14" fill="{RED}" font-weight="bold" text-anchor="end">no nail: slides</text></g>')
    # click 5: shear flow along the joint (just under the flange on the web)
    g5 = '<g data-step="5">'
    for i in range(6):
        x = wx0 + 22 + i * (FX1 - FX0 - 44) / 5
        g5 += f'<line x1="{x - 11:.1f}" y1="{FY1 + 8}" x2="{x + 11:.1f}" y2="{FY1 + 8}" stroke="{TAU}" stroke-width="2" marker-end="url(#a_1f7a5a)"/>'
    g5 += (f'<text x="{FX1 + DX * 0.6 + 8:.1f}" y="{FY1 + 4}" font-size="15" fill="{TAU}" font-weight="bold">{sym("q")} = Δ{sym("F")}/{sym("s")}</text>'
           f'<text x="{FX1 + DX * 0.6 + 8:.1f}" y="{FY1 + 22}" font-size="13" fill="{GREY}">along the joint</text>')
    # inset: a tiny element at the joint; tau on its horizontal faces (along the joint) = tau on its vertical faces
    ex, ey, h, L = 524, 222, 22, 30
    arr = lambda x1, y1, x2, y2: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{TAU}" stroke-width="2.2" marker-end="url(#a_1f7a5a)"/>'
    g5 += (f'<rect x="{ex - h}" y="{ey - h}" width="{2 * h}" height="{2 * h}" fill="#fff" stroke="#333" stroke-width="1.4"/>'
           + arr(ex - L / 2, ey - h - 6, ex + L / 2, ey - h - 6) + arr(ex + L / 2, ey + h + 6, ex - L / 2, ey + h + 6)
           + arr(ex + h + 6, ey + L / 2, ex + h + 6, ey - L / 2) + arr(ex - h - 6, ey - L / 2, ex - h - 6, ey + L / 2)
           + f'<text x="{ex}" y="{ey - h - 12}" font-size="14" fill="{TAU}" font-weight="bold" text-anchor="middle">{sym("τ")}</text>'
           f'<text x="{ex + h + 12}" y="{ey + 5}" font-size="14" fill="{TAU}" font-weight="bold">{sym("τ")}</text>'
           f'<text x="{ex}" y="{ey + h + 30}" font-size="12" fill="{GREY}" text-anchor="middle">element at the joint:</text>'
           f'<text x="{ex}" y="{ey + h + 44}" font-size="12" fill="{GREY}" text-anchor="middle">same {sym("τ")} on both planes</text></g>')
    s += g5
    return f'<svg class="fig" style="left:40px; top:342px" width="620" height="290" viewBox="0 0 620 290">{s}</svg>'


def build():
    MM, DM = "<mi>M</mi>", "<mrow><mi>Δ</mi><mi>M</mi></mrow>"
    F1, F2 = "<msub><mi>F</mi><mn>1</mn></msub>", "<msub><mi>F</mi><mn>2</mn></msub>"
    DF = "<mrow><mi>Δ</mi><mi>F</mi></mrow>"
    right = f"""
  <div class="given" data-step="1" style="left:680px; width:532px"><span class="gh">Question</span>&nbsp; The flange is nailed to the web (Ex. 15.3). What force does each nail have to carry?</div>
  <div class="steps" style="top:216px">
  <div class="step" data-step="1"><span class="no">1</span><b>Cut out one slice of the flange</b>, length <i>s</i>
    <div class="row"><span class="tag calc">Know</span>{m(DM + '<mo>=</mo><mi>V</mi><mi>s</mi>')}<span class="si" style="margin-left:10px">(slope of <i>M</i> is <i>V</i>)</span></div></div>
  <div class="step" data-step="2"><span class="no">2</span><b>Bending stress pushes on both ends</b>
    <div class="row"><span class="tag calc">Compute</span>{ds('<mi>F</mi><mo>=</mo><mo>∫</mo><mi>σ</mi><mspace width="0.1em"/><mi>d</mi><mi>A</mi><mo>=</mo><mfrac>' + MM + '<mi>I</mi></mfrac><mo>∫</mo><mi>y</mi><mspace width="0.1em"/><mi>d</mi><mi>A</mi><mo>=</mo><mfrac><mrow>' + MM + '<mi>Q</mi></mrow><mi>I</mi></mfrac>')}</div>
    <div class="row"><span class="tag calc"></span>{ds(F1 + '<mo>=</mo><mfrac><mrow>' + MM + '<mi>Q</mi></mrow><mi>I</mi></mfrac><mo>,</mo><mspace width="0.8em"/>' + F2 + '<mo>=</mo><mfrac><mrow>' + P(MM + '<mo>+</mo>' + DM) + '<mi>Q</mi></mrow><mi>I</mi></mfrac>')}</div>
    <div class="cap"><i>F</i> grows with <i>M</i>; <i>M</i> is bigger at the right cut, so <i>F</i><sub>2</sub> &gt; <i>F</i><sub>1</sub></div></div>
  <div class="step" data-step="3"><span class="no">3</span><b>The two ends do not balance</b>
    <div class="row"><span class="tag calc">Compute</span>{ds(DF + '<mo>=</mo>' + F2 + '<mo>−</mo>' + F1 + '<mo>=</mo><mfrac><mrow>' + DM + '<mi>Q</mi></mrow><mi>I</mi></mfrac><mo>=</mo><mfrac><mrow><mi>V</mi><mi>s</mi><mi>Q</mi></mrow><mi>I</mi></mfrac>')}<span class="si" style="margin-left:10px">no nail → it slides</span></div></div>
  <div class="step" data-step="4"><span class="no">4</span><b>The nail must supply Δ<i>F</i></b>; per metre of joint:
    <div class="row"><span class="tag calc">Compute</span>{ds('<mi>q</mi><mo>=</mo><mfrac>' + DF + '<mi>s</mi></mfrac><mo>=</mo><mfrac><mrow><mi>V</mi><mi>Q</mi></mrow><mi>I</mi></mfrac>')}<span class="si" style="margin-left:10px">shear flow (N/m)</span></div>
    <div class="cap"><i>q</i> = <i>τt</i>: the <i>τ</i> of <i>VQ</i>/(<i>It</i>), acting along the joint (horizontal <i>τ</i> = vertical <i>τ</i>)</div>
    <div class="row"><span class="tag req">Spacing</span>{ds('<mtext>nail force</mtext><mo>=</mo><mi>q</mi><mi>s</mi><mo>≤</mo><mi>F</mi>' + IMP + '<mi>s</mi><mo>≤</mo><mfrac><mi>F</mi><mi>q</mi></mfrac>')}</div></div>
  <div class="step" data-step="5"><span class="no">5</span><b>Ex 15.3, region B–C</b> ({m('<mi>q</mi><mo>=</mo><mn>8.61</mn>' + U('kN/m'))}, nails at 0.15 m)
    <div class="row"><span class="tag req">Check</span>{m('<mi>q</mi><mi>s</mi><mo>=</mo><mn>8.61</mn>' + P('<mn>0.15</mn>') + '<mo>=</mo><mn>1.29</mn>' + U('kN') + '<mo>≤</mo><mn>1.50</mn>' + U('kN'))}<span class="ok">OK</span></div></div>
  </div>"""

    js = "<script>\n" + lib.ELASTIC_JS + """
(() => {
  const $ = id => document.getElementById(id);
  const set = (id, a) => { const e = $(id); for (const k in a) e.setAttribute(k, a[k]); };
  const ramp = (clk, d) => smooth(Math.min(1, Math.max(0, (clk() - 0.3) / d)));
  const c2 = revealClock(2), c3 = revealClock(3), c4 = revealClock(4);
  const FX0 = %FX0%, FX1 = %FX1%, FY0 = %FY0%, FY1 = %FY1%, L1 = %L1%, L2 = %L2%, SL = %SL%, DX = %DX%, DY = %DY%;
  function draw() {
    const gm = ramp(c2, 0.8), g3 = ramp(c3, 1.2), g4 = ramp(c4, 0.8);
    const g2 = smooth(Math.min(1, Math.max(0, (c2() - 1.3) / 1.0)));   // pushes grow after the M bars
    $('mb1').setAttribute('y2', (%MB% - %MS% * %M1% * gm).toFixed(1));
    $('mb2').setAttribute('y2', (%MB% - %MS% * %M2% * gm).toFixed(1));
    $('mlab').setAttribute('opacity', gm.toFixed(2));
    // sigma = M y / I over the flange: y from 0.0725 (top) to 0.0425 m (bottom) above the N.A.
    for (let i = 0; i < 4; i++) for (let j = 0; j < 2; j++) {
      const t = j ? 0.62 : 0.0, y = FY0 + (FY1 - FY0) * (i + 0.5) / 4 + t * DY, f = (0.0725 - 0.03 * (i + 0.5) / 4) / 0.0725;
      const xl = FX0 + t * DX, xr = FX1 + t * DX;
      const tl = 0, yl = FY0 + (FY1 - FY0) * (i + 0.5) / 4;   // left end face is hidden: push on its front edge
      if (j) { set(`pl${i}${j}`, {opacity: 0}); } else set(`pl${i}${j}`, {x1: (FX0 - 4 - L1 * f * g2).toFixed(1), x2: (FX0 - 3).toFixed(1), y1: yl.toFixed(1), y2: yl.toFixed(1)});
      set(`pr${i}${j}`, {x1: (xr + 4 + L2 * f * g2).toFixed(1), x2: (xr + 3).toFixed(1), y1: y.toFixed(1), y2: y.toFixed(1)});
    }
    const dx = -SL * g3 * (1 - g4);           // slides on click 3, nailed back in place on click 4
    $('slice').setAttribute('transform', `translate(${dx.toFixed(1)},0)`);
    $('slidetxt').setAttribute('opacity', (g3 * (1 - g4)).toFixed(2));
    const gn = smooth(Math.min(1, Math.max(0, (c4() - 1.1) / 0.5)));   // nail goes in after the slice is back
    for (const k of ['nailin', 'nailhd', 'nailbeam']) $(k).setAttribute('opacity', gn.toFixed(2));
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>"""
    for k, v in dict(FX0=FX0, FX1=FX1, FY0=FY0, FY1=FY1, L1=L1, L2=L2, SL=SLIDE, DX=DX, DY=DY, MB=MB, MS=MS, M1=round(M1, 3), M2=round(M2, 3)).items():
        js = js.replace(f"%{k}%", str(v))
    title = 'Why the nails carry the <span class="key">shear flow</span> <i>q</i> = <i>VQ</i>/<i>I</i>'
    body = beam_svg() + "\n" + zoom_svg() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.3, p. 697; shear-flow derivation from the text’s chapter on shear flow. Slice length and nail spacing exaggerated for clarity.</div>')
    lib.write_page("16b_slide17_shearflow.html", "Slide 17 - Shear flow", title, body, 17, c.STEP_CSS)
    print(f"check: q_BC = {1.5e3 * 0.345e-3 / 60.125e-6 / 1e3:.2f} kN/m, nail force at 0.15 m = {1.5e3 * 0.345e-3 / 60.125e-6 * 0.15 / 1e3:.3f} kN")


if __name__ == "__main__":
    build()
