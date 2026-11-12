"""Slide 3 - Shear stress tau = VQ/It: why it exists, what each term means, sign convention.

Added after the bending slide (user request). Clicks:
  1  Why shear stress exists (top right, looping): a stack of three loose boards and a
     glued (solid) stack bend the same amount. Each loose board bends about its own
     middle line, so their ends slide past each other; the glued stack bends as one
     piece (plane sections), so the layers cannot slide: the glue (material) carries a
     shear stress tau along the layers. Kinematics as on slide 2, curvature exaggerated.
  2  The equation tau = VQ/It, large (MathML).
  3-6 One label per term (V, Q, I, t), colour-coded with the term in the equation and
     with the matching part of the section drawing:
       V  internal shear force on the cut face
       Q  first moment of the area A' beyond the point about the N.A., Q = y'A'
          (A' shaded, centroid dot, y' dimension)
       I  moment of inertia of the whole section about the N.A. (whole section outlined)
       t  width of the section at the point (arrow across)
  7  A line sweeps down a rectangular section b x h; for the line at height y:
       A' = b (h/2 - y), y' = (h/2 + y)/2, Q = (b/2)(h^2/4 - y^2), t = b
     so tau = VQ/It follows Q: zero at top and bottom, largest at the N.A. The tau curve is
     drawn as the line moves.
  8  Sign convention as two tests (looping): +V tips the piece clockwise (left piece: V down
     on its right end; right piece: V up on its left end, both tip clockwise); +M bends the
     piece into a smile (left piece: M counterclockwise on its right end; right piece: M
     clockwise on its left end). Same test, same sign, for either piece.

Writes ../slides/separate/02c_slide3_shear.html.
Run:  python3 09_make_slide3_shear.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SIG, TAU = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SIG, lib.TAU
QC = "#c27c0e"   # amber: Q, A', y' (colour-coded with the equation)
WOOD = lib.WOOD
sym = lib.sym

# section figure (svg in the lower left, page left 48, top 300)
SX0, SY0, SB, SH = 70, 40, 130, 250        # section rectangle: left, top, width b, height h
PX0, PW = 300, 150                         # tau plot axis x, width of tau_max


def build():
    yc = SY0 + SH / 2
    sec = f"""<svg class="fig" style="left:48px; top:300px" width="700" height="395" viewBox="0 0 700 395">
  <defs>{lib.markers(RED, SIG, TAU, NAVY, "#000000", QC)}</defs>
  <g data-step="3">
    <rect x="{SX0}" y="{SY0}" width="{SB}" height="{SH}" fill="{S['inner']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <line x1="{SX0 - 20}" y1="{yc}" x2="{SX0 + SB + 30}" y2="{yc}" stroke="{GREY}" stroke-width="1" stroke-dasharray="5 4"/>
    <text x="{SX0 + SB + 34}" y="{yc + 5}" font-size="14" fill="{GREY}">N.A.</text>
    <text x="{SX0 + SB / 2}" y="{SY0 + SH + 26}" font-size="15" fill="{GREY}" font-style="italic" text-anchor="middle">cross section (the cut face)</text>
    <line x1="{SX0 - 34}" y1="{yc - 50}" x2="{SX0 - 34}" y2="{yc + 50}" stroke="{TAU}" stroke-width="3.5" marker-end="url(#a_{TAU[1:]})"/>
    <text x="{SX0 - 40}" y="{yc - 58}" font-size="20" fill="{TAU}" text-anchor="middle">{sym('V')}</text>
  </g>
  <g data-step="4">
    <path id="aPrime" fill="{QC}" fill-opacity="0.3" stroke="{QC}" stroke-width="1.5"/>
    <text id="aLbl" font-size="18" fill="{QC}" font-weight="bold">A′</text>
    <line id="ybar" stroke="{QC}" stroke-width="1.3" marker-start="url(#a_{QC[1:]})" marker-end="url(#a_{QC[1:]})"/>
    <circle id="cen" r="4.5" fill="{QC}"/>
    <text id="ybarLbl" font-size="17" fill="{QC}">{sym('ȳ′')}</text>
    <line id="cutLine" x1="{SX0 - 10}" x2="{SX0 + SB + 10}" stroke="{RED}" stroke-width="2.2"/>
    <circle id="ptDot" cx="{SX0 + SB / 2}" r="5" fill="{RED}"/>
  </g>
  <g data-step="5">
    <rect x="{SX0 - 6}" y="{SY0 - 6}" width="{SB + 12}" height="{SH + 12}" fill="none" stroke="{NAVY}" stroke-width="2" stroke-dasharray="7 4"/>
    <text x="{SX0 + SB / 2}" y="{SY0 + SH + 50}" font-size="17" fill="{NAVY}" text-anchor="middle">{sym('I')}: the whole section (dashed)</text>
  </g>
  <g data-step="6">
    <line id="tArrow" stroke="{RED}" stroke-width="2" marker-start="url(#a_C00000)" marker-end="url(#a_C00000)"/>
    <text id="tLbl" font-size="18" fill="{RED}" text-anchor="middle">{sym('t')}</text>
  </g>
  <g data-step="7">
    <text x="{PX0}" y="{SY0 - 14}" font-size="16" font-weight="bold" fill="{TAU}">Shear stress {sym('τ')} at the red line</text>
    <line x1="{PX0}" y1="{SY0}" x2="{PX0}" y2="{SY0 + SH}" stroke="#000" stroke-width="1.5"/>
    <path id="tauTrace" fill="none" stroke="{TAU}" stroke-width="3"/>
    <path id="tauGhost" fill="none" stroke="{TAU}" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.5"/>
    <circle id="tauDot" r="5.5" fill="{RED}"/>
    <text id="qTxt" x="{PX0 + PW + 20}" y="{SY0 + 60}" font-size="17"></text>
    <text id="tTxt" x="{PX0 + PW + 20}" y="{SY0 + 90}" font-size="17" fill="{TAU}"></text>
    <text x="{PX0 + PW + 20}" y="{SY0 + 150}" font-size="15" fill="{GREY}" font-style="italic">top, bottom: A′ = 0,</text>
    <text x="{PX0 + PW + 20}" y="{SY0 + 170}" font-size="15" fill="{GREY}" font-style="italic">so τ = 0</text>
    <text x="{PX0 + PW + 20}" y="{SY0 + 200}" font-size="15" fill="{GREY}" font-style="italic">N.A.: Q largest,</text>
    <text x="{PX0 + PW + 20}" y="{SY0 + 220}" font-size="15" fill="{GREY}" font-style="italic">so τ largest</text>
  </g>
</svg>"""

    boards = f"""<svg class="fig" data-step="1" style="left:770px; top:112px" width="460" height="260" viewBox="0 0 460 260">
  <defs>{lib.markers(RED, TAU)}</defs>
  <text x="0" y="16" font-size="17" font-weight="bold">Why is there shear stress?</text>
  <text x="115" y="48" font-size="15" text-anchor="middle" fill="{GREY}" font-style="italic">loose boards</text>
  <text x="345" y="48" font-size="15" text-anchor="middle" fill="{GREY}" font-style="italic">glued together</text>
  <g id="loose"></g><g id="glued"></g>
  <text id="slipTxt" x="115" y="204" font-size="16" font-weight="bold" fill="{RED}" text-anchor="middle">they slide</text>
  <text id="tauTxtB" x="345" y="204" font-size="16" font-weight="bold" fill="{TAU}" text-anchor="middle">no sliding: τ in the glue</text>
  <text x="230" y="240" font-size="15" text-anchor="middle">The material must stop the layers sliding: that is the shear stress τ.</text>
</svg>"""

    conv = f"""<svg class="fig" data-step="8" style="left:770px; top:380px" width="460" height="240" viewBox="0 0 460 240">
  <defs>{lib.markers(TAU, SIG, GREY)}</defs>
  <text x="0" y="16" font-size="17" font-weight="bold">Which sign? Look at what it does to the piece</text>
  <text x="0" y="42" font-size="16" fill="{TAU}"><tspan font-weight="bold">+{sym('V')}</tspan> tips the piece clockwise</text>
  <g id="testV"></g>
  <text x="0" y="148" font-size="16" fill="{SIG}"><tspan font-weight="bold">+{sym('M')}</tspan> bends the piece: it smiles</text>
  <g id="testM"></g>
</svg>"""

    eq = (f'<math displaystyle="true"><mi style="color:{TAU}">τ</mi><mo>=</mo><mfrac><mrow><mi id="tV" style="color:{TAU}">V</mi><mi id="tQ" style="color:{QC}">Q</mi></mrow>'
          f'<mrow><mi id="tI" style="color:{NAVY}">I</mi><mi id="tT" style="color:{RED}">t</mi></mrow></mfrac></math>')
    labels = f"""  <div id="eqn" class="eqn" data-step="2">{eq}</div>
  <div class="lbl" id="lV" data-step="3" style="left:60px; top:112px; color:{TAU}"><b>{lib.mi('V')}</b>: shear force at the cut<br><span class="cap">(from the V diagram)</span></div>
  <div class="lbl" id="lQ" data-step="4" style="left:486px; top:112px; color:{QC}"><b>{lib.mi('Q')} = {lib.mi('ȳ′')}{lib.mi('A′')}</b>: first moment of the area <i>beyond</i> the point, about the N.A.</div>
  <div class="lbl" id="lI" data-step="5" style="left:60px; top:262px; color:{NAVY}"><b>{lib.mi('I')}</b>: moment of inertia of the <i>whole</i> section</div>
  <div class="lbl" id="lT" data-step="6" style="left:486px; top:262px; color:{RED}"><b>{lib.mi('t')}</b>: width of the section at the point</div>
  <svg class="fig" style="left:0; top:0; pointer-events:none" width="1280" height="720" viewBox="0 0 1280 720">
    <defs>{lib.markers(TAU, NAVY, RED, QC)}</defs>
    <path id="arV" data-step="3" fill="none" stroke="{TAU}" stroke-width="2.2" marker-end="url(#a_{TAU[1:]})"/>
    <path id="arQ" data-step="4" fill="none" stroke="{QC}" stroke-width="2.2" marker-end="url(#a_{QC[1:]})"/>
    <path id="arI" data-step="5" fill="none" stroke="{NAVY}" stroke-width="2.2" marker-end="url(#a_{NAVY[1:]})"/>
    <path id="arT" data-step="6" fill="none" stroke="{RED}" stroke-width="2.2" marker-end="url(#a_{RED[1:]})"/>
  </svg>
  <div class="cv" data-step="8">
    <div>Same test for either piece. Draw V, M this way on any FBD; a negative answer means the opposite way.</div>
    <div><math><mi>σ</mi><mo>=</mo><mo>−</mo><mi>M</mi><mi>y</mi><mo>/</mo><mi>I</mi></math>: the minus turns a smile (+M) into compression on top.</div>
  </div>"""

    js = f"""<script>
{lib.ELASTIC_JS}
(() => {{
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1);
  const TAU = "{TAU}", RED = "{RED}", SIG = "{SIG}", WF = "{WOOD['face']}", WE = "{WOOD['edge']}";
  const SX0 = {SX0}, SY0 = {SY0}, SB = {SB}, SH = {SH}, YC = SY0 + SH / 2, PX0 = {PX0}, PW = {PW};

  // ---- arrows from each label to its term (positions measured from the rendered MathML) ----
  function termArrows() {{
    const sl = $('slide').getBoundingClientRect(), k = sl.width / 1280;
    const box = el => {{ const r = el.getBoundingClientRect();
      return {{l: (r.left - sl.left) / k, r: (r.right - sl.left) / k, t: (r.top - sl.top) / k, b: (r.bottom - sl.top) / k}}; }};
    const firstLine = el => {{ const rs = el.getClientRects(); return rs.length ? rs[0] : el.getBoundingClientRect(); }};
    const arrow = (term, lbl, path) => {{
      const a = box($(term)), L = $(lbl), lb = box(L), fl = firstLine(L.querySelector('b') || L);
      const ly = ((fl.top + fl.bottom) / 2 - sl.top) / k;               // middle of the label's first line
      const left = lb.l < a.l;                                           // label left of the term?
      // left labels: start just past the end of their first line of text; right labels: just before their left edge
      let lineEnd = fl.right;
      const rg = document.createRange(); rg.selectNodeContents(L);
      for (const r of rg.getClientRects()) if (Math.abs((r.top + r.bottom) / 2 - (fl.top + fl.bottom) / 2) < 12) lineEnd = Math.max(lineEnd, r.right);
      const sx = left ? ((lineEnd - sl.left) / k) + 8 : lb.l - 8;
      const ex = left ? a.l - 4 : a.r + 4, ey = (a.t + a.b) / 2;         // end at the side of the term
      const cx = (sx + ex) / 2, cy = ly + (ey - ly) * 0.15 - (ey > ly ? 0 : 18);
      $(path).setAttribute('d', `M${{f1(sx)}},${{f1(ly)}} Q${{f1(cx)}},${{f1(cy)}} ${{f1(ex)}},${{f1(ey)}}`);
    }};
    arrow('tV', 'lV', 'arV'); arrow('tQ', 'lQ', 'arQ'); arrow('tI', 'lI', 'arI'); arrow('tT', 'lT', 'arT');
  }}
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => requestAnimationFrame(termArrows));
  addEventListener('resize', termArrows);

  // ---- boards: loose (each bends about its own middle) vs glued (one piece) ----
  const BL = 180, BH = 24, NB = 3, TH = 0.62;
  function stack(g, cx, cy, u, loose) {{
    const k = u * TH / (BL / 2), n = 30;
    let out = '';
    for (let i = 0; i < NB; i++) {{
      const yi = (1 - i) * BH;                               // board middle above the stack middle
      const P = (s, yl) => {{                                 // s along the board, yl up from the board middle
        if (k < 1e-7) return [cx + s, cy - (yi + yl)];
        const R = 1 / k, Ri = loose ? R - yi : R, a = s / Ri, r = Ri - yl - (loose ? 0 : yi);
        return [cx + r * Math.sin(a), cy - (R - r * Math.cos(a))];
      }};
      const top = [], bot = [];
      for (let j = 0; j <= n; j++) {{ const s = -BL / 2 + BL * j / n; top.push(P(s, BH / 2)); bot.unshift(P(s, -BH / 2)); }}
      out += `<path d="M${{top.concat(bot).map(p => f1(p[0]) + ',' + f1(p[1])).join(' L')}}Z" fill="${{WF}}" stroke="${{WE}}" stroke-width="1.3"/>`;
    }}
    // loose: dashed line square to the middle board at each end; the outer boards' ends step past it
    if (loose && k > 1e-7) {{
      const R = 1 / k;
      for (const side of [-1, 1]) {{
        const a = side * BL / 2 / R, r1 = R - 1.6 * BH, r2 = R + 1.6 * BH;
        out += `<line x1="${{f1(cx + r1 * Math.sin(a))}}" y1="${{f1(cy - (R - r1 * Math.cos(a)))}}" x2="${{f1(cx + r2 * Math.sin(a))}}" y2="${{f1(cy - (R - r2 * Math.cos(a)))}}" stroke="${{RED}}" stroke-width="1.6" stroke-dasharray="4 3" opacity="${{f1(Math.min(1, 3 * u))}}"/>`;
      }}
    }}
    g.innerHTML = out;
  }}
  // shear arrows on the glue planes near the ends of the glued stack
  function glueArrows(cx, cy, u) {{
    if (u < 0.2) return '';
    const k = u * TH / (BL / 2), R = 1 / k;
    let g = '';
    for (const side of [-1, 1]) for (const yi of [BH / 2, -BH / 2]) {{
      const s = side * BL * 0.34, r = R - yi, a = s / R;
      const x = cx + r * Math.sin(a), y = cy - (R - r * Math.cos(a)), tx = -side * Math.cos(a), ty = -side * Math.sin(a), L = 14 * u;   // toward mid-span
      g += `<line x1="${{f1(x - tx * L)}}" y1="${{f1(y - ty * L)}}" x2="${{f1(x + tx * L)}}" y2="${{f1(y + ty * L)}}" stroke="${{TAU}}" stroke-width="2.4" marker-end="url(#a_${{TAU.slice(1)}})"/>`;
    }}
    return g;
  }}

  // sign convention arcs are static: left face clockwise (6 -> 9 -> 12 o'clock), right face counterclockwise

  // ---- sign tests: +V tips each piece clockwise, +M bends each piece into a smile ----
  const c8 = revealClock(8);
  const GREY = "#555555";
  function piecePath(cx, cy, L, h, k) {{                         // straight (k = 0) or bent piece, pure bending
    const n = 24, P = (s, y) => {{
      if (Math.abs(k) < 1e-7) return [cx + s, cy - y];
      const R = 1 / k, a = s / R; return [cx + (R - y) * Math.sin(a), cy - (R - (R - y) * Math.cos(a))];
    }};
    const top = [], bot = [];
    for (let j = 0; j <= n; j++) {{ const s = -L / 2 + L * j / n; top.push(P(s, h / 2)); bot.unshift(P(s, -h / 2)); }}
    return {{d: 'M' + top.concat(bot).map(q => f1(q[0]) + ',' + f1(q[1])).join(' L') + 'Z', P}};
  }}
  function signTests(t) {{
    const c = t % 6, u = c < 1.5 ? smooth(c / 1.5) : c < 4 ? 1 : c < 5.2 ? 1 - smooth((c - 4) / 1.2) : 0;
    const L = 150, h = 26;
    let gv = '', gm = '';
    for (const [cx, right] of [[115, false], [345, true]]) {{   // right = false: left piece (cut face on its right end)
      const name = right ? 'right piece' : 'left piece';
      // --- V test (row 1, centre y 88): piece tips clockwise by up to 7 deg about its centre
      const cy = 86, ang = 7 * u, ex = right ? cx - L / 2 : cx + L / 2;
      const v = right ? [cy + 18, cy - 18] : [cy - 18, cy + 18];   // up on a left end, down on a right end
      gv += `<g transform="rotate(${{f1(ang)}} ${{cx}} ${{cy}})">` +
        `<rect x="${{cx - L / 2}}" y="${{cy - h / 2}}" width="${{L}}" height="${{h}}" fill="#c3c9d1" stroke="#3f4650" stroke-width="1.3"/>` +
        `<line x1="${{ex + (right ? -8 : 8)}}" y1="${{v[0]}}" x2="${{ex + (right ? -8 : 8)}}" y2="${{v[1]}}" stroke="${{TAU}}" stroke-width="2.8" marker-end="url(#a_${{TAU.slice(1)}})"/>` +
        `<line x1="${{ex}}" y1="${{cy - h / 2 - 4}}" x2="${{ex}}" y2="${{cy + h / 2 + 4}}" stroke="${{RED}}" stroke-width="2"/></g>`;
      gv += `<text x="${{cx}}" y="${{cy - 24}}" font-size="13" fill="${{GREY}}" font-style="italic" text-anchor="middle">${{name}}</text>`;
      gv += `<text x="${{cx}}" y="${{cy + 40}}" font-size="15" font-weight="bold" fill="${{TAU}}" text-anchor="middle" opacity="${{f1(u)}}">clockwise: +V ✓</text>`;
      // --- M test (row 2, centre y 192): piece bends into a smile under M at its cut end
      const cy2 = 194, k = u * 0.5 / (L / 2), pp = piecePath(cx, cy2, L, h, k);
      gm += `<path d="${{pp.d}}" fill="#c3c9d1" stroke="#3f4650" stroke-width="1.3"/>`;
      const e = pp.P(right ? -L / 2 : L / 2, 0), r = 15, x = e[0] + (right ? -6 : 6);
      // left piece, right end: counterclockwise (bottom -> right -> top); right piece, left end: clockwise (bottom -> left -> top)
      gm += `<path d="M${{f1(x)}},${{f1(e[1] + r)}} A${{r}},${{r}} 0 0 ${{right ? 1 : 0}} ${{f1(x)}},${{f1(e[1] - r)}}" fill="none" stroke="${{SIG}}" stroke-width="2.6" marker-end="url(#a_${{SIG.slice(1)}})"/>`;
      gm += `<text x="${{cx}}" y="${{cy2 + 40}}" font-size="15" font-weight="bold" fill="${{SIG}}" text-anchor="middle" opacity="${{f1(u)}}">smiles: +M ✓</text>`;
    }}
    $('testV').innerHTML = gv; $('testM').innerHTML = gm;
  }}

  // ---- section sweep ----
  const c1 = revealClock(1), c7 = revealClock(7);
  const Qn = y => 1 - (2 * y / SH) ** 2;                           // Q / Q_max for the line at height y (px up from N.A.)
  function draw() {{
    // boards loop
    const tb = c1() % 7, u = tb < 2 ? smooth(tb / 2) : tb < 4.5 ? 1 : tb < 6 ? 1 - smooth((tb - 4.5) / 1.5) : 0;
    stack($('loose'), 115, 128, u, true); stack($('glued'), 345, 128, u, false);
    $('glued').innerHTML += glueArrows(345, 128, u);
    $('slipTxt').setAttribute('opacity', f1(u));
    signTests(c8()); $('tauTxtB').setAttribute('opacity', f1(u));

    // line height: rests at h/4 (step 4-6 pictures), sweeps once clicked to 7
    const t7 = c7(), sweeping = t7 > 0.05;
    const y = sweeping ? (SH / 2) * Math.cos(2 * Math.PI * (t7 % 8) / 8) : SH / 4;
    const yy = YC - y;
    $('aPrime').setAttribute('d', `M${{SX0}},${{SY0}} L${{SX0 + SB}},${{SY0}} L${{SX0 + SB}},${{f1(yy)}} L${{SX0}},${{f1(yy)}} Z`);
    $('aLbl').setAttribute('x', SX0 + 8); $('aLbl').setAttribute('y', f1(Math.min(SY0 + 22, (SY0 + yy) / 2 + 6)));
    $('aLbl').setAttribute('opacity', yy - SY0 > 24 ? 1 : 0);
    const ycen = (SY0 + yy) / 2;                                     // centroid of A'
    $('cen').setAttribute('cx', SX0 + SB / 2 + 30); $('cen').setAttribute('cy', f1(ycen));
    const show = Math.abs(ycen - YC) > 14;
    $('ybar').setAttribute('x1', SX0 + SB / 2 + 30); $('ybar').setAttribute('x2', SX0 + SB / 2 + 30);
    $('ybar').setAttribute('y1', f1(YC)); $('ybar').setAttribute('y2', f1(ycen + (ycen < YC ? 5 : -5)));
    $('ybar').setAttribute('opacity', show ? 1 : 0);
    $('ybarLbl').setAttribute('x', SX0 + SB / 2 + 38); $('ybarLbl').setAttribute('y', f1((YC + ycen) / 2 + 6));
    $('ybarLbl').setAttribute('opacity', show ? 1 : 0);
    $('cutLine').setAttribute('y1', f1(yy)); $('cutLine').setAttribute('y2', f1(yy));
    $('ptDot').setAttribute('cy', f1(yy));
    $('tArrow').setAttribute('x1', SX0 + 3); $('tArrow').setAttribute('x2', SX0 + SB - 3);
    const below = yy + 40 < SY0 + SH;                                // t arrow under the line, or above it near the bottom
    const ta = below ? yy + 14 : yy - 14, tl = below ? yy + 34 : yy - 22;
    $('tArrow').setAttribute('y1', f1(ta)); $('tArrow').setAttribute('y2', f1(ta));
    $('tLbl').setAttribute('x', SX0 + SB / 2); $('tLbl').setAttribute('y', f1(tl));

    // tau plot: dashed full curve, solid trace down to the line
    let g = '', tr = '';
    for (let i = 0; i <= 60; i++) {{
      const yv = SY0 + SH * i / 60, x = PX0 + PW * Qn(YC - yv);
      g += (i ? ' L' : 'M') + f1(x) + ',' + f1(yv);
      if (yv <= yy + 0.01) tr += (tr ? ' L' : 'M') + f1(x) + ',' + f1(yv);
    }}
    $('tauGhost').setAttribute('d', g);
    $('tauTrace').setAttribute('d', tr);
    $('tauDot').setAttribute('cx', f1(PX0 + PW * Qn(y))); $('tauDot').setAttribute('cy', f1(yy));
    $('qTxt').innerHTML = `<tspan class="sym">Q</tspan> = ${{Qn(y).toFixed(2)}} <tspan class="sym">Q</tspan><tspan baseline-shift="sub" font-size="70%">max</tspan>`;
    $('tTxt').innerHTML = `<tspan class="sym">τ</tspan> = ${{Qn(y).toFixed(2)}} <tspan class="sym">τ</tspan><tspan baseline-shift="sub" font-size="70%">max</tspan>`;
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + f"""
  .eqn {{ position: absolute; left: 250px; top: 150px; font-size: 54px; }}
  .lbl {{ position: absolute; width: 270px; font-size: 18px; line-height: 1.3; }}
  .cv {{ position: absolute; left: 770px; top: 624px; width: 460px; font-size: 14.5px; line-height: 1.3; }}
  .cv div {{ margin-bottom: 3px; }}
"""
    title = 'Shear stress: <span class="key">τ = VQ/It</span>'
    body = sec + "\n" + boards + "\n" + conv + "\n" + labels + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, shear formula, Ch. 7; sign convention, Ch. 6. '
        'Rectangular section; board bending exaggerated.</div>')
    lib.write_page("02c_slide3_shear.html", "Slide 3 - Shear formula", title, body, 3, css)


if __name__ == "__main__":
    build()
