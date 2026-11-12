"""Slide 3 - Why a vertical load makes a horizontal stress sigma_x (bending, Sec. 15.1).

Added after slide 2 because "the load is vertical, why sigma_x?" was not obvious.
Clicks:
  1  the loaded beam (small, top) with a dashed zoom box around a short piece
  2  the piece, drawn large with vertical grid lines, bends and unbends in a loop.
     Kinematics of pure bending: the neutral axis follows a circle of radius R
     (centre above, sagging); a point (s, y) of the straight piece (s along the
     axis, y up from the N.A.) goes to ((R - y) sin(s/R), R - (R - y) cos(s/R)).
     Plane sections stay plane, top fibres get shorter, bottom fibres longer,
     the N.A. keeps its length. Curvature exaggerated (end slope 0.4 rad).
  3  labels: shorter / same length / longer
  4  sigma_x arrows on both end faces, normal to the face, length proportional to
     y times the curvature (compression on top pushes in, tension below pulls out)
  5  the flexure formula and why sigma_x >> sigma_y
Illustration of the textbook kinematics (Hibbeler Ch. 6 flexure), not a simulation.

Writes ../slides/separate/02b_slide3_bending.html.
Run:  python3 08_make_slide3_bending.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SUP, SIG = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT, lib.SIG
sym = lib.sym

CX, CY, L0, H = 330, 340, 420, 130     # big piece: centre of the N.A. (svg px), length, depth
NGRID = 13
THETA = 0.40                            # end slope at full bending (rad)


def build():
    # overview beam (click 1)
    ov = f"""
  <g data-step="1">
    <rect x="40" y="40" width="520" height="20" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <polygon points="40,60 30,78 50,78" fill="#fff" stroke="{SUP}" stroke-width="2"/>
    <polygon points="560,60 550,74 570,74" fill="#fff" stroke="{SUP}" stroke-width="2"/>
    <circle cx="555" cy="77" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/><circle cx="565" cy="77" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>
    <line x1="300" y1="0" x2="300" y2="36" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>
    <text x="310" y="18" font-size="20" fill="{RED}">{sym('P')}</text>
    <rect x="250" y="32" width="38" height="36" fill="none" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>
    <line x1="250" y1="68" x2="{CX - L0 / 2}" y2="{CY - H / 2 - 40}" stroke="{NAVY}" stroke-width="1" stroke-dasharray="4 3"/>
    <line x1="288" y1="68" x2="{CX + L0 / 2}" y2="{CY - H / 2 - 40}" stroke="{NAVY}" stroke-width="1" stroke-dasharray="4 3"/>
    <text x="600" y="56" font-size="15" fill="{GREY}" font-style="italic">zoom on a short piece</text>
  </g>"""
    piece = f"""
  <g data-step="2">
    <path id="pc" fill="{S['inner']}" stroke="{S['edge']}" stroke-width="2"/>
    <g id="grid" stroke="#4b525b" stroke-width="1.3"></g>
    <path id="na" fill="none" stroke="{NAVY}" stroke-width="1.6" stroke-dasharray="7 5"/>
    <text id="naLbl" font-size="15" fill="{NAVY}">N.A.</text>
  </g>
  <g data-step="3" font-size="17" font-weight="bold">
    <text id="lTop" fill="{SIG}" text-anchor="middle">top: shorter (pushed)</text>
    <text id="lBot" fill="{SIG}" text-anchor="middle">bottom: longer (pulled)</text>
    <text id="lNa" font-size="14" font-weight="normal" fill="{NAVY}" text-anchor="middle">same length</text>
  </g>
  <g data-step="4" id="arrows"></g>"""

    svg = f"""<svg class="fig" style="left:48px; top:112px" width="800" height="590" viewBox="0 0 800 590">
  <defs>{lib.markers(RED, SIG)}</defs>
  {ov}
  {piece}
</svg>"""

    js = f"""<script>
{lib.ELASTIC_JS}
(() => {{
  const CX = {CX}, CY = {CY}, L0 = {L0}, H = {H}, NG = {NGRID}, TH = {THETA};
  const SIG = "{SIG}";
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1);
  const c2 = revealClock(2);

  // point (s, y) of the straight piece -> screen, for curvature k = 1/R (sagging: centre above)
  function P(s, y, k) {{
    let px, py;
    if (k < 1e-7) {{ px = s; py = y; }}
    else {{ const R = 1 / k, a = s / R; px = (R - y) * Math.sin(a); py = R - (R - y) * Math.cos(a); }}
    return [CX + px, CY - py];
  }}
  const line = (pts) => 'M' + pts.map(p => f1(p[0]) + ',' + f1(p[1])).join(' L');

  function draw() {{
    const t = c2() % 7;
    const u = t < 2 ? smooth(t / 2) : t < 4.5 ? 1 : t < 6 ? 1 - smooth((t - 4.5) / 1.5) : 0;
    const k = u * TH / (L0 / 2);
    const h = H / 2, n = 60;
    const top = [], bot = [], na = [];
    for (let i = 0; i <= n; i++) {{ const s = -L0 / 2 + L0 * i / n; top.push(P(s, h, k)); bot.unshift(P(s, -h, k)); na.push(P(s, 0, k)); }}
    $('pc').setAttribute('d', line(top.concat(bot)) + 'Z');
    $('na').setAttribute('d', line(na));
    let g = '';
    for (let j = 1; j < NG - 1; j++) {{
      const s = -L0 / 2 + L0 * j / (NG - 1), a = P(s, h, k), b = P(s, -h, k);
      g += `<line x1="${{f1(a[0])}}" y1="${{f1(a[1])}}" x2="${{f1(b[0])}}" y2="${{f1(b[1])}}"/>`;
    }}
    $('grid').innerHTML = g;
    const pr = P(-L0 / 2 + 14, 0, k);
    $('naLbl').setAttribute('x', f1(pr[0])); $('naLbl').setAttribute('y', f1(pr[1] - 8));
    const tp = P(0, h, k), bp = P(0, -h, k), np = P(0, 0, k);
    $('lTop').setAttribute('x', f1(tp[0])); $('lTop').setAttribute('y', f1(tp[1] - 14));
    $('lBot').setAttribute('x', f1(bp[0])); $('lBot').setAttribute('y', f1(bp[1] + 28));
    $('lNa').setAttribute('x', f1(np[0])); $('lNa').setAttribute('y', f1(np[1] - 8));

    // sigma_x on both end faces: along the beam axis there (normal to the face), length ~ -y * k
    let ar = '';
    for (const side of [-1, 1]) {{
      const s = side * L0 / 2, a = s * k;                 // face angle
      const tx = Math.cos(a), ty = -Math.sin(a);         // outward axis direction on screen, for side = +1
      for (let m = -4; m <= 4; m++) {{
        if (m === 0) continue;
        const y = h * m / 4, p = P(s, y, k);
        const L = 95 * (y / h) * u;                       // + compression (top, sagging), - tension (bottom)
        if (Math.abs(L) < 3) continue;
        const ox = side * tx, oy = side * ty;             // outward from the piece
        const far = [p[0] + ox * (Math.abs(L) + 4), p[1] + oy * (Math.abs(L) + 4)], near = [p[0] + ox * 4, p[1] + oy * 4];
        const [A, B] = L > 0 ? [far, near] : [near, far]; // compression points at the face, tension away
        ar += `<line x1="${{f1(A[0])}}" y1="${{f1(A[1])}}" x2="${{f1(B[0])}}" y2="${{f1(B[1])}}" stroke="${{SIG}}" stroke-width="2.5" marker-end="url(#a_{SIG[1:]})"/>`;
      }}
    }}
    $('arrows').innerHTML = ar;
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + f"""
  .pts {{ font-size: 20px; }}
  .box {{ position: absolute; left: 880px; top: 520px; width: 330px; padding: 10px 14px; font-size: 19px;
         border: 2px solid {RED}; border-radius: 6px; background: #fbecec; }}
  .box math[display="block"] {{ font-size: 30px; margin: 6px 0; }}
"""
    formula = ('<math display="block"><msub><mi>σ</mi><mi>x</mi></msub><mo>=</mo><mo>−</mo>'
               '<mfrac><mrow><mi>M</mi><mi>y</mi></mrow><mi>I</mi></mfrac></math>')
    pts = f"""  <ul class="pts" style="left:880px; top:130px; width:340px">
    <li data-step="1">The load is vertical, but it makes the beam <b>bend</b>.</li>
    <li data-step="2">Lines drawn across the beam stay straight but <b>fan out</b>.</li>
    <li data-step="3">Top fibres get <b>shorter</b>, bottom fibres get <b>longer</b>. The middle layer (neutral axis) keeps its length.</li>
    <li data-step="4">Squeezing or stretching along x means a stress along x: <span class="em">{lib.mi('σ', 'x')}</span>.</li>
  </ul>
  <div class="box" data-step="5">{formula}
    {lib.mi('M')} comes from the vertical load and grows with the span, so {lib.mi('σ', 'x')} grows with the span too.</div>"""
    title = 'A vertical load makes a <span class="key">horizontal</span> stress by bending the beam'
    body = svg + "\n" + js + "\n" + pts + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.1; flexure formula, Ch. 6. '
        'Bending exaggerated; arrow length proportional to σ<sub>x</sub>.</div>')
    lib.write_page("02b_slide3_bending.html", "Slide 2 - Why sigma_x", title, body, 2, css)


if __name__ == "__main__":
    build()
