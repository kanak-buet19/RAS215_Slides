"""Slide 4 - Principal stresses and stress trajectories (Sec. 15.1, p. 689, Fig. 15-2e, Fig. 15-3).

Same cantilever as slide 3: rectangular section, depth h, load P at the free end
(left), wall at the right, length 4h. Nondimensional stresses (b = h = P = 1):
    sigma_x = 12 x y        (M y / I with M = P x hogging: tension on top)
    tau_xy  = 1.5 (1 - 4 y^2)
x from the free end, y up from the neutral axis.
Left: the five elements of slide 3 at the section x = h/2 (there sigma_max = 2 tau_max),
first with their x-y stresses, then (click 2) each turns by its principal angle
    theta_p = 1/2 atan2(2 tau, sigma)
and shows sigma_1 (tension, out) and sigma_2 (compression, in), from
    sigma_1,2 = sigma/2 +- sqrt((sigma/2)^2 + tau^2).
Arrows on this slide all use one scale.
Right (click 3): stress trajectories traced through the computed principal
directions (Euler steps of 0.004 h from seeds on the neutral axis), tension solid,
compression dashed. Click 4: the 45 deg crossing at the N.A. is marked. Click 5:
short crack marks across the tension lines near the top, where a brittle beam would crack.

Writes ../slides/separate/04_slide4_trajectories.html.
Run:  python3 06_make_slide4_trajectories.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SUP = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT
SIG, TAU = lib.SIG, lib.TAU
sym = lib.sym

# trajectory plot: beam from (BX, BY) with h = BH px, length 4h
BX, BY, BH = 540, 120, 150
COL_X, ROW_Y0, ROW_DY = 120, 150, 78


def build():
    svg = f"""<svg class="fig" style="left:48px; top:112px" width="1184" height="590" viewBox="0 0 1184 590">
  <defs>{lib.markers(RED, SIG, TAU)}
    <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="8" stroke="{SUP}" stroke-width="1.5"/></pattern>
  </defs>
  <g data-step="1">
    <text x="10" y="{ROW_Y0 - 70}" font-size="16" font-weight="bold">Elements at section a–a (slide 6)</text>
    <text id="colHead" x="10" y="{ROW_Y0 - 46}" font-size="15" fill="{GREY}" font-style="italic">x–y stresses</text>
    <g id="els"></g>
  </g>
  <g data-step="3">
    <rect x="{BX}" y="{BY}" width="{4 * BH}" height="{BH}" fill="#eef1f5" stroke="{S['edge']}" stroke-width="1.5"/>
    <rect x="{BX + 4 * BH}" y="{BY - 30}" width="16" height="{BH + 60}" fill="url(#hatch)" stroke="{SUP}" stroke-width="1.5"/>
    <line x1="{BX + 6}" y1="{BY - 62}" x2="{BX + 6}" y2="{BY - 4}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>
    <text x="{BX + 16}" y="{BY - 42}" font-size="20" fill="{RED}">{sym('P')}</text>
    <line x1="{BX + BH / 2}" y1="{BY - 10}" x2="{BX + BH / 2}" y2="{BY + BH + 10}" stroke="{GREY}" stroke-width="1.2" stroke-dasharray="4 3"/>
    <text x="{BX + BH / 2}" y="{BY - 14}" font-size="14" fill="{GREY}" text-anchor="middle">a–a</text>
    <line x1="{BX}" y1="{BY + BH / 2}" x2="{BX + 4 * BH}" y2="{BY + BH / 2}" stroke="{GREY}" stroke-width="1" stroke-dasharray="2 4"/>
    <g id="traj" fill="none" stroke="{SIG}" stroke-width="2"></g>
    <g transform="translate({BX}, {BY + BH + 34})">
      <line x1="0" y1="0" x2="40" y2="0" stroke="{SIG}" stroke-width="2.5"/><text x="48" y="5" font-size="15">tension (σ₁) trajectory</text>
      <line x1="250" y1="0" x2="290" y2="0" stroke="{SIG}" stroke-width="2.5" stroke-dasharray="7 5"/><text x="298" y="5" font-size="15">compression (σ₂) trajectory</text>
    </g>
  </g>
  <g data-step="4">
    <circle id="c45" r="20" fill="none" stroke="{RED}" stroke-width="2.5"/>
    <text id="t45" font-size="16" font-weight="bold" fill="{RED}">45° at the N.A., 90° to each other</text>
  </g>
  <g data-step="5" id="cracks" stroke="{RED}" stroke-width="3" stroke-linecap="round"></g>
</svg>"""

    js = f"""<script>
{lib.ELASTIC_JS}
(() => {{
  const SIG = "{SIG}", TAU = "{TAU}", EDGE = "{S['edge']}", RED = "{RED}";
  const BX = {BX}, BY = {BY}, BH = {BH};
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1), deg = r => r * 180 / Math.PI;
  // nondimensional stresses (b = h = P = 1), x from the free end, y up from the N.A.
  const sx = (x, y) => 12 * x * y, txy = (x, y) => 1.5 * (1 - 4 * y * y);
  const th1 = (x, y) => 0.5 * Math.atan2(2 * txy(x, y), sx(x, y));       // sigma_1 direction (rad, CCW from x)

  // ---------- elements at x = h/2 ----------
  const XA = 0.5, ROWS = [0.5, 0.25, 0, -0.25, -0.5];
  const K = 12;          // px of arrow per unit stress (sigma_max = 3 here)
  function arrow(x1, y1, x2, y2, c, op) {{
    return `<line x1="${{f1(x1)}}" y1="${{f1(y1)}}" x2="${{f1(x2)}}" y2="${{f1(y2)}}" stroke="${{c}}" stroke-width="2.5" opacity="${{op}}" marker-end="url(#a_${{c.slice(1)}})"/>`;
  }}
  // normal stress pair along unit vector (ux, uy) (screen coords), magnitude v (+ out, - in)
  function normalPair(cx, cy, ux, uy, start, v, c, op) {{
    const L = Math.abs(v) * K; if (L < 2) return '';
    let g = '';
    for (const s of [-1, 1]) {{
      const a = [cx + s * ux * start, cy + s * uy * start], b = [cx + s * ux * (start + L), cy + s * uy * (start + L)];
      g += v > 0 ? arrow(...a, ...b, c, op) : arrow(...b, ...a, c, op);
    }}
    return g;
  }}
  function elements(u) {{          // u = 0: x-y stresses, u = 1: principal
    let g = '';
    ROWS.forEach((y, i) => {{
      const cx = {COL_X}, cy = {ROW_Y0} + i * {ROW_DY}, a = 15;
      const s = sx(XA, y), t = txy(XA, y), th = th1(XA, y);
      const c = s / 2, r = Math.hypot(s / 2, t), s1 = c + r, s2 = c - r;
      const ang = th * u;                                     // CCW in the math sense
      g += `<text x="${{cx - 100}}" y="${{cy + 5}}" font-size="16" font-weight="bold">${{i + 1}}</text>`;
      g += `<rect x="${{cx - a}}" y="${{cy - a}}" width="${{2 * a}}" height="${{2 * a}}" fill="#e8ecf1" stroke="${{EDGE}}" stroke-width="1.5" transform="rotate(${{f1(-deg(ang))}} ${{cx}} ${{cy}})"/>`;
      // x-y set (fades out)
      const o = a + 6;
      g += normalPair(cx, cy, 1, 0, o + 8, s, SIG, 1 - u);
      const T = t * K;
      if (T > 2) {{
        g += arrow(cx + o, cy + T / 2, cx + o, cy - T / 2, TAU, 1 - u) + arrow(cx - o, cy - T / 2, cx - o, cy + T / 2, TAU, 1 - u);
        g += arrow(cx - T / 2, cy - o, cx + T / 2, cy - o, TAU, 1 - u) + arrow(cx + T / 2, cy + o, cx - T / 2, cy + o, TAU, 1 - u);
      }}
      // principal set (fades in): sigma_1 along the turned x', sigma_2 along y'
      const ux = Math.cos(th), uy = -Math.sin(th);             // screen y is down
      g += normalPair(cx, cy, ux, uy, a + 4, s1, SIG, u) + normalPair(cx, cy, -uy, ux, a + 4, s2, SIG, u);
      if (u > 0.01) g += `<text x="${{cx + 92}}" y="${{cy + 5}}" font-size="15" opacity="${{u}}">θ<tspan baseline-shift="sub" font-size="70%">p</tspan> = ${{Math.round(deg(th))}}°</text>`;
    }});
    return g;
  }}

  // ---------- trajectories ----------
  function trace(x0, y0, fam) {{     // fam 0: sigma_1, 1: sigma_2; returns screen points
    const pts = [];
    for (const dir of [1, -1]) {{
      let x = x0, y = y0, px = null, py = null;
      const seg = [];
      for (let k = 0; k < 4000; k++) {{
        let a = th1(x, y) + fam * Math.PI / 2, dx = Math.cos(a), dy = Math.sin(a);
        if (px === null) {{ dx *= dir; dy *= dir; }}
        else if (dx * px + dy * py < 0) {{ dx = -dx; dy = -dy; }}
        px = dx; py = dy;
        x += 0.004 * dx; y += 0.004 * dy;
        if (x < 0 || x > 4 || y > 0.5 || y < -0.5) break;
        seg.push([BX + x * BH, BY + (0.5 - y) * BH]);
      }}
      if (dir === 1) pts.push(...seg.reverse()); else pts.push(...seg);
      if (dir === 1) pts.push([BX + x0 * BH, BY + (0.5 - y0) * BH]);
    }}
    return pts;
  }}
  let tr = '';
  for (let xs = 0.25; xs < 4; xs += 0.5) {{
    for (const fam of [0, 1]) {{
      const p = trace(xs, 0, fam);
      tr += `<path class="${{fam ? 'tj2' : 'tj1'}}" d="M${{p.map(q => f1(q[0]) + ',' + f1(q[1])).join(' L')}}" ${{fam ? 'stroke-dasharray="7 5"' : ''}}/>`;
    }}
  }}
  $('traj').innerHTML = tr;

  // 45 deg marker at the N.A. crossing near x = 2.25 h, and cracks across tension lines near the top
  const cxs = BX + 2.25 * BH, cys = BY + 0.5 * BH;
  $('c45').setAttribute('cx', cxs); $('c45').setAttribute('cy', cys);
  $('t45').setAttribute('x', cxs - 60); $('t45').setAttribute('y', BY + BH + 72);
  let ck = '';
  for (const x of [1.0, 1.75, 2.5, 3.25]) {{
    const y = 0.42, a = th1(x, y) + Math.PI / 2, L = 9;          // crack runs across sigma_1
    const X = BX + x * BH, Y = BY + (0.5 - y) * BH;
    ck += `<line x1="${{f1(X - L * Math.cos(a))}}" y1="${{f1(Y + L * Math.sin(a))}}" x2="${{f1(X + L * Math.cos(a))}}" y2="${{f1(Y - L * Math.sin(a))}}"/>`;
  }}
  $('cracks').innerHTML = ck;

  // ---------- animation ----------
  const c2 = revealClock(2), c3 = revealClock(3);
  const solid = [...document.querySelectorAll('.tj1')], dashed = [...document.querySelectorAll('.tj2')];
  solid.forEach(p => {{ const L = p.getTotalLength(); p.setAttribute('stroke-dasharray', `${{L}} ${{L}}`); p.dataset.len = L; }});
  function draw() {{
    const u = smooth((c2() - 0.3) / 1.6);
    $('els').innerHTML = elements(u);
    $('colHead').textContent = u < 0.5 ? 'x–y stresses' : 'turned to the principal directions';
    const v = smooth(c3() / 2.5);
    solid.forEach(p => p.setAttribute('stroke-dashoffset', f1(+p.dataset.len * (1 - v))));   // tension lines draw on
    const w = smooth((c3() - 1.5) / 1.5);
    dashed.forEach(p => {{ p.style.opacity = w; }});                                         // then compression lines fade in
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + "\n  .pts { font-size: 19px; }\n"
    pts = f"""  <ul class="pts" style="left:588px; top:470px; width:640px">
    <li data-step="2">Every element can be <b>turned</b> to a direction where only normal stresses act: the principal stresses {lib.mi('σ', '1')} (pull) and {lib.mi('σ', '2')} (push).</li>
    <li data-step="3"><b>Stress trajectories</b> follow those directions through the whole beam.</li>
    <li data-step="5">A brittle beam (concrete) <b>cracks across the tension lines</b>, so steel reinforcement is placed along them.</li>
  </ul>"""
    title = 'Principal stresses follow <span class="key">stress trajectories</span>'
    body = svg + "\n" + js + "\n" + pts + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.1, p. 689, Figs. 15-2e, 15-3. From ' + lib.M_FLEX + ', ' + lib.M_SHEAR +
        '; rectangular cantilever, <i>L</i> = 4<i>h</i>; elements at <i>x</i> = <i>h</i>/2.</div>')
    lib.write_page("04_slide4_trajectories.html", "Slide 7 - Stress trajectories", title, body, 7, css)


if __name__ == "__main__":
    build()
