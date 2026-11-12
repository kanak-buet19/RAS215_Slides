"""Slide 4 - What a stress element is, which faces we see, and how to draw tau on it.

Added because "which plane is the element's surface?" and "which side are we looking at?"
were unclear. Clicks:
  1  The whole cantilever (P at the free left end, wall on the right, as in Hibbeler Fig. 15-2)
     in 3-D. A cut flashes at a-a, the right (wall) part slides away and fades, and the left
     part stays with its cut face (red outline), V on it (up) and a point on the cut face.
  2  A tiny cube is cut out at the point and pulled out, growing to a large cube. Faces are
     colour-coded: x-faces (normal x: parallel to the cut, carry sigma_x and tau),
     y-faces (normal y: horizontal layers, carry tau), z-faces (normal z: toward the
     viewer, no stress: plane stress).
  3  The view turns to face-on (the depth axis shrinks to zero): the cube becomes the
     square we always draw; its four edges are the x- and y-faces seen edge-on.
  4-7 Drawing tau: (1) on the x-face that lies on the cut, tau points like V (up);
     (2) opposite x-face: equal and opposite (down); (3) y-faces: the opposite pair so the
     element cannot spin (top right, bottom left); (4) check: arrows meet tip-to-tip or
     tail-to-tail at the corners (marked: tips at top right, tails at bottom right;
     the other two corners are the same).

Writes ../slides/separate/02d_slide4_element.html.
Run:  python3 11_make_slide4_element.py
"""
import importlib
import json

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SIG, TAU = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SIG, lib.TAU
sym = lib.sym

XF, YF, ZF = "#9aa1aa", "#cfe6dc", "#eef0f3"     # face colours: x-faces (same grey as the beam's cut face), y-faces, z-faces
G = dict(BX0=70, BY0=200, L=290, H=60, Z=40, cx=0.6, cy=0.4,    # beam piece (world half-depth H, half-width Z)
         PY=30,                                                  # point on the cut face (height above N.A.)
         CX=560, CY=330, A=72)                                   # big cube centre (svg) and half-size


def build():
    sq = G["A"]
    cx, cy = G["CX"], G["CY"]
    # tau arrows on the flat element (final, face-on), steps 4-7
    o = sq + 12
    arrows = f"""
  <g data-step="4">
    <line x1="{cx + o}" y1="{cy + 38}" x2="{cx + o}" y2="{cy - 38}" stroke="{TAU}" stroke-width="4" marker-end="url(#a_{TAU[1:]})"/>
    <text x="{cx + o + 12}" y="{cy + 6}" font-size="20" font-weight="bold" fill="{TAU}">1</text>
  </g>
  <g data-step="5">
    <line x1="{cx - o}" y1="{cy - 38}" x2="{cx - o}" y2="{cy + 38}" stroke="{TAU}" stroke-width="4" marker-end="url(#a_{TAU[1:]})"/>
    <text x="{cx - o - 26}" y="{cy + 6}" font-size="20" font-weight="bold" fill="{TAU}">2</text>
  </g>
  <g data-step="6">
    <line x1="{cx - 38}" y1="{cy - o}" x2="{cx + 38}" y2="{cy - o}" stroke="{TAU}" stroke-width="4" marker-end="url(#a_{TAU[1:]})"/>
    <line x1="{cx + 38}" y1="{cy + o}" x2="{cx - 38}" y2="{cy + o}" stroke="{TAU}" stroke-width="4" marker-end="url(#a_{TAU[1:]})"/>
    <text x="{cx - 6}" y="{cy - o - 12}" font-size="20" font-weight="bold" fill="{TAU}">3</text>
    <text x="{cx - 6}" y="{cy + o + 30}" font-size="20" font-weight="bold" fill="{TAU}">3</text>
  </g>
  <g data-step="7">
    <circle cx="{cx + o}" cy="{cy - o}" r="20" fill="none" stroke="{RED}" stroke-width="2.5"/>
    <circle cx="{cx + o}" cy="{cy + o}" r="20" fill="none" stroke="{RED}" stroke-width="2.5"/>
    <text x="{cx + o + 26}" y="{cy - o + 5}" font-size="16" font-weight="bold" fill="{RED}">tips meet</text>
    <text x="{cx + o + 26}" y="{cy + o + 5}" font-size="16" font-weight="bold" fill="{RED}">tails meet</text>
  </g>"""

    svg = f"""<svg class="fig" style="left:48px; top:112px" width="830" height="590" viewBox="0 0 830 590">
  <defs>{lib.markers(RED, TAU, SIG, GREY, "#000000")}
    <pattern id="hatchW" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#3f4650" stroke-width="1.5"/></pattern></defs>
  <g data-step="1">
    <g id="beam"></g>
    <text x="70" y="316" font-size="15" fill="{GREY}" font-style="italic">cantilever; we keep the left part</text>
  </g>
  <g data-step="1"><g id="axes"></g></g>
  <g data-step="2"><g id="cube"></g><g id="lbl3d"></g></g>
  <g data-step="3"><g id="lbl2d"></g></g>
  {arrows}
</svg>"""

    js = f"""<script>
{lib.ELASTIC_JS}
(() => {{
  const G = {json.dumps(G)};
  const {{BX0, BY0, L, H, Z, cx, cy, PY, CX, CY, A}} = G;
  const RED = "{RED}", TAU = "{TAU}", SIG = "{SIG}", GREY = "{GREY}", EDGE = "{S['edge']}";
  const XF = "{XF}", YF = "{YF}", ZF = "{ZF}";
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1);
  const P = (X, Y, Zw) => [BX0 + X - cx * Zw, BY0 - Y + cy * Zw];      // beam: oblique view
  const poly = (pts, fill, stroke = EDGE, sw = 1.4) => `<polygon points="${{pts.map(q => f1(q[0]) + ',' + f1(q[1])).join(' ')}}" fill="${{fill}}" stroke="${{stroke}}" stroke-width="${{sw}}" stroke-linejoin="round"/>`;

  // ---- beam (click 1): whole cantilever -> cut at a-a -> right part slides away -> left part with V ----
  const LR = 180, WALL = L + LR;                                   // right part length, wall position
  const c1 = revealClock(1);
  function beam(t) {{
    const cut = t < 0.8 ? 0 : t < 1.5 ? 0.5 + 0.5 * Math.sin((t - 0.8) * 18) : 0;     // cut line flashes
    const go = smooth((t - 1.5) / 1.1), show = smooth((t - 2.5) / 0.6);              // right part leaves, then V appears
    let b = '';
    // left part (always)
    b += poly([P(0, H, -Z), P(L, H, -Z), P(L, H, Z), P(0, H, Z)], '#d6dbe1');                 // top
    b += poly([P(0, -H, Z), P(L, -H, Z), P(L, H, Z), P(0, H, Z)], '#b3bac3');                 // front
    if (go > 0) b += poly([P(L, -H, -Z), P(L, H, -Z), P(L, H, Z), P(L, -H, Z)], '#9aa1aa', RED, 2.6);   // cut face
    // right part (wall side): slides right and fades
    if (go < 1) {{
      const dx = 90 * go, op = 1 - go;
      const Q = (X, Y, Zw) => {{ const q = P(X, Y, Zw); return [q[0] + dx, q[1]]; }};
      b += `<g opacity="${{f1(op)}}">` +
        poly([Q(L, H, -Z), Q(WALL, H, -Z), Q(WALL, H, Z), Q(L, H, Z)], '#d6dbe1') +
        poly([Q(L, -H, Z), Q(WALL, -H, Z), Q(WALL, H, Z), Q(L, H, Z)], '#b3bac3');
      // wall: a 3-D slab the beam runs into (X from WALL to WALL + T), drawn over the beam end
      const T = 18, WY = H + 34, WZ = Z + 26;
      b += poly([Q(WALL, WY, -WZ), Q(WALL + T, WY, -WZ), Q(WALL + T, WY, WZ), Q(WALL, WY, WZ)], '#d6dbe1');          // top
      b += poly([Q(WALL + T, -WY, -WZ), Q(WALL + T, WY, -WZ), Q(WALL + T, WY, WZ), Q(WALL + T, -WY, WZ)], '#c3c9d1'); // side
      const wf = [Q(WALL, -WY, WZ), Q(WALL + T, -WY, WZ), Q(WALL + T, WY, WZ), Q(WALL, WY, WZ)];
      b += poly(wf, '#e9ecef') + poly(wf, 'url(#hatchW)');                                                          // front: solid, then hatched
      // the beam's front and top faces end at the wall's front face (z = WZ is in front of the beam), so the joint is closed
      b += `<text x="${{f1(Q(L + LR / 2, -H, Z)[0])}}" y="${{f1(Q(L + LR / 2, -H, Z)[1] + 24)}}" font-size="14" fill="${{GREY}}" font-style="italic" text-anchor="middle">right part (wall side)</text></g>`;
    }}
    // cut line a-a
    if (cut > 0 || t < 1.5) {{
      const a1 = P(L, H + 14, Z), a2 = P(L, -H - 14, Z);
      b += `<line x1="${{f1(a1[0])}}" y1="${{f1(a1[1])}}" x2="${{f1(a2[0])}}" y2="${{f1(a2[1])}}" stroke="${{RED}}" stroke-width="2.5" stroke-dasharray="6 4" opacity="${{f1(t < 0.8 ? 0.6 : cut)}}"/>`;
      b += `<text x="${{f1(a1[0])}}" y="${{f1(a1[1] - 6)}}" font-size="16" fill="${{RED}}" text-anchor="middle">a</text>`;
    }}
    // load P at the free end
    const p0 = P(14, H, 0);
    b += `<line x1="${{f1(p0[0])}}" y1="${{f1(p0[1] - 60)}}" x2="${{f1(p0[0])}}" y2="${{f1(p0[1] - 4)}}" stroke="${{RED}}" stroke-width="3" marker-end="url(#a_${{RED.slice(1)}})"/>`;
    b += `<text x="${{f1(p0[0] + 10)}}" y="${{f1(p0[1] - 42)}}" font-size="20" fill="${{RED}}"><tspan class="sym">P</tspan></text>`;
    // point, V and label on the cut face of the left part
    const pt = P(L, PY, 0), vb = P(L, -H + 12, 0), vt = P(L, H - 12, 0), ct = P(L, -H, Z);
    b += `<g opacity="${{f1(show)}}"><circle cx="${{f1(pt[0])}}" cy="${{f1(pt[1])}}" r="5" fill="${{RED}}"/>` +
      `<line x1="${{f1(vb[0] + 30)}}" y1="${{f1(vb[1])}}" x2="${{f1(vt[0] + 30)}}" y2="${{f1(vt[1])}}" stroke="${{TAU}}" stroke-width="4" marker-end="url(#a_${{TAU.slice(1)}})"/>` +
      `<text x="${{f1(vt[0] + 40)}}" y="${{f1(vt[1] + 14)}}" font-size="20" fill="${{TAU}}"><tspan class="sym">V</tspan></text>` +
      `<text x="${{f1(ct[0] + 4)}}" y="${{f1(ct[1] + 22)}}" font-size="15" fill="${{RED}}">cut face (a–a)</text></g>`;
    $('beam').innerHTML = b;
  }}
  const pt = P(L, PY, 0);

  // ---- cube: centre (ux, uy), half-size a, depth factor f (1 = oblique, 0 = face-on) ----
  function cube(ux, uy, a, f) {{
    const fx = cx * f, fy = cy * f;
    const Q = (x, y, z) => [ux + x - fx * z, uy - y + fy * z];
    let g = '';
    if (f > 0.02) {{
      g += poly([Q(-a, a, -a), Q(a, a, -a), Q(a, a, a), Q(-a, a, a)], YF);        // top: y-face
      g += poly([Q(a, -a, -a), Q(a, a, -a), Q(a, a, a), Q(a, -a, a)], XF, RED, 2.2); // right: x-face (on the cut), styled like the cut face
    }}
    g += poly([Q(-a, -a, a), Q(a, -a, a), Q(a, a, a), Q(-a, a, a)], ZF);          // front: z-face
    return {{g, Q}};
  }}

  const c2 = revealClock(2), c3 = revealClock(3);
  function draw() {{
    beam(c1());
    const m = smooth((c2() - 0.3) / 1.8);                        // pull out and grow
    const f = 1 - smooth((c3() - 0.3) / 1.5);                    // turn face-on
    const ux = pt[0] + (CX - pt[0]) * m, uy = pt[1] + (CY - pt[1]) * m - 40 * Math.sin(Math.PI * m);
    const a = 6 + (A - 6) * m;
    const c = cube(ux, uy, a, f);
    $('cube').innerHTML = c.g;

    // x-y-z axes in the same view: z drawn as (-cx, +cy) when oblique, shrinking to a dot (out of the page) face-on
    const ox = 90, oy = 520, La = 62;
    const zx = ox - cx * La * f * 1.6, zy = oy + cy * La * f * 1.6;
    let ax = `<line x1="${{ox}}" y1="${{oy}}" x2="${{ox + La}}" y2="${{oy}}" stroke="#000" stroke-width="2" marker-end="url(#a_000000)"/>` +
      `<line x1="${{ox}}" y1="${{oy}}" x2="${{ox}}" y2="${{oy - La}}" stroke="#000" stroke-width="2" marker-end="url(#a_000000)"/>` +
      `<text x="${{ox + La + 8}}" y="${{oy + 6}}" font-size="19"><tspan class="sym">x</tspan></text>` +
      `<text x="${{ox - 5}}" y="${{oy - La - 10}}" font-size="19"><tspan class="sym">y</tspan></text>`;
    if (f > 0.15) ax += `<line x1="${{ox}}" y1="${{oy}}" x2="${{f1(zx)}}" y2="${{f1(zy)}}" stroke="#000" stroke-width="2" marker-end="url(#a_000000)"/>` +
      `<text x="${{f1(zx - 16)}}" y="${{f1(zy + 14)}}" font-size="19"><tspan class="sym">z</tspan></text>`;
    else ax += `<circle cx="${{ox}}" cy="${{oy}}" r="8" fill="#fff" stroke="#000" stroke-width="1.8"/><circle cx="${{ox}}" cy="${{oy}}" r="2.6" fill="#000"/>` +
      `<text x="${{ox - 26}}" y="${{oy + 24}}" font-size="19"><tspan class="sym">z</tspan></text>`;
    ax += `<text x="${{ox + 100}}" y="${{oy - 20}}" font-size="14" fill="${{GREY}}" font-style="italic">${{f > 0.15 ? 'z toward you' : 'z out of the page (⊙)'}}</text>`;
    $('axes').innerHTML = ax;

    // 3-D labels (fade out as the view turns face-on)
    const Q = c.Q, op3 = m > 0.95 ? f : 0;
    const lab = (x1, y1, x2, y2, txt, col, anchor) =>
      `<line x1="${{f1(x1)}}" y1="${{f1(y1)}}" x2="${{f1(x2)}}" y2="${{f1(y2)}}" stroke="${{col}}" stroke-width="1.4"/>` +
      `<text x="${{f1(x2 + (anchor === 'end' ? -6 : 6))}}" y="${{f1(y2 + 5)}}" font-size="16" font-weight="bold" fill="${{col}}" text-anchor="${{anchor}}">${{txt}}</text>`;
    const tp = Q(0, a, 0), rp = Q(a, 0, 0), fp = Q(-a * 0.4, -a * 0.5, a);
    $('lbl3d').innerHTML = `<g opacity="${{f1(op3)}}">` +
      lab(tp[0], tp[1], tp[0] + 40, tp[1] - 60, 'y-face: a horizontal layer', '#1f7a5a', 'start') +
      lab(rp[0], rp[1], rp[0] + 24, rp[1] + 128, 'x-face: on the cut', NAVY_C, 'start') +
      lab(fp[0], fp[1], fp[0] - 60, fp[1] + 70, 'z-face: faces you, no stress', GREY, 'end') + '</g>';

    // 2-D labels once face-on
    const op2 = 1 - f;
    $('lbl2d').innerHTML = `<g opacity="${{f1(op2)}}" font-size="15" font-style="italic">` +
      `<text x="${{CX}}" y="${{CY - A - 46}}" fill="#1f7a5a" text-anchor="middle">top and bottom edges: y-faces</text>` +
      `<text x="${{CX}}" y="${{CY + A + 72}}" fill="${{NAVY_C}}" text-anchor="middle">left and right edges: x-faces</text>` +
      `<text x="${{CX}}" y="${{CY + A + 94}}" fill="${{GREY}}" text-anchor="middle">you look at the z-face (front)</text></g>`;
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  const NAVY_C = "{NAVY}";
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + f"""
  .pts {{ font-size: 18px; }}
  .pts li {{ margin-bottom: 9px; }}
  .sw {{ display: inline-block; width: 14px; height: 14px; border: 1px solid #3f4650; vertical-align: -2px; margin-right: 4px; }}
"""
    pts = f"""  <ul class="pts" style="left:900px; top:122px; width:330px">
    <li data-step="2">A <b>stress element</b> is a tiny cube cut out at one point.
      <br><span class="sw" style="background:{XF}"></span><b>x-faces</b>: on the cut: σ<sub>x</sub>, τ
      <br><span class="sw" style="background:{YF}"></span><b>y-faces</b>: horizontal layers: τ
      <br><span class="sw" style="background:{ZF}"></span><b>z-faces</b>: no stress</li>
    <li data-step="3">We look at it <b>from the front</b>: the square's edges are faces seen edge-on.</li>
    <li data-step="4"><b style="color:{TAU}">1</b> On the x-face on the cut, τ points the same way as {lib.mi('V')}.</li>
    <li data-step="5"><b style="color:{TAU}">2</b> Opposite x-face: equal and opposite.</li>
    <li data-step="6"><b style="color:{TAU}">3</b> y-faces: the opposite pair, so the cube cannot spin.</li>
    <li data-step="7"><b style="color:{RED}">4</b> Check: arrows meet <b>tip to tip</b> or <b>tail to tail</b> at the corners.</li>
  </ul>"""
    title = 'A stress element is a tiny <span class="key">cube</span> at one point'
    body = svg + "\n" + pts + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.1, Fig. 15-2; stress elements, Ch. 9. Not to scale.</div>')
    lib.write_page("02d_slide4_element.html", "Slide 4 - Stress element", title, body, 4, css)


if __name__ == "__main__":
    build()
