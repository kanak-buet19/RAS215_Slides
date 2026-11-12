"""Slide 3 - Stress changes from point to point in a section (Sec. 15.1, p. 688-689, Fig. 15-2).

Cantilever, rectangular section b x h, load P at the free (left) end, section a-a.
Clicks:
  1  cantilever, P, section a-a
  2  free-body diagram of the left part: V (up) and M (clockwise) at the cut
  3  shear stress over the section: tau = (3V / 2A)(1 - 4y^2/h^2)   (parabola)
  4  bending stress over the section: sigma = M y / I, tension on top   (straight line)
  5  stress elements at points 1-5 (top, h/4, N.A., -h/4, bottom)
  6-10 a marker steps to point 1, 2, 3, 4, 5 (one click each, smooth move), the element in the
     column is boxed, and a large element on the right shows the stresses at that point
All stresses are computed from the two formulas above. sigma arrows and tau arrows
each use their own scale (lengths proportional within each kind); the scales are
different because sigma_max / tau_max = 4x/h depends on where a-a is.
Orientation as Hibbeler Fig. 15-2: P at the free left end, wall on the right, free body
of the left part. On its cut (right) face V acts up, so tau_xy > 0 (right face up, left face
down, top face right, bottom face left). By the sign convention V < 0 (V up on a right end
tips the piece counterclockwise) and M < 0 (hogging, top in tension).

Writes ../slides/separate/03_slide3_section.html.
Run:  python3 05_make_slide3_section.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SUP = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT
SIG, TAU = lib.SIG, lib.TAU
sym = lib.sym

# section drawing (svg px)
SEC_TOP, SEC_H = 290, 220           # section from y = 290 to 510
HEAD_Y = 186                        # row of plot titles (formulas sit under them)
# three panels, each heading / formula / caption left-aligned at the panel's left edge,
# with thin grey dividers between them (DIV1, DIV2)
TAU_L, SIG_L, COL_L = 150, 400, 635 # left edges of the shear, bending and element panels
DIV1, DIV2 = 372, 608               # dividers
TAU_X, TAU_W = 150, 110             # tau plot: axis x, width of tau_max
SIG_X, SIG_W = 490, 90              # sigma plot: axis x, width of sigma_max (each side)
COL_X = 715                         # column of small elements (centre)
LIVE = (1040, 395)                  # centre of the live element


def build():
    yc = SEC_TOP + SEC_H / 2
    # cantilever (top row): free end x=20, wall x=440, depth 60
    cant = f"""
  <g data-step="1">
    <path id="cantBody" d="M20,52 H440 V112 H20 Z" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <rect x="440" y="20" width="16" height="124" fill="url(#hatch)" stroke="{SUP}" stroke-width="1.5"/>
    <line id="pA1" x1="26" y1="0" x2="26" y2="48" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>
    <text x="36" y="20" font-size="20" fill="{RED}">{sym('P')}<tspan id="pPct" font-size="14" font-style="italic"></tspan></text>
    <line x1="230" y1="38" x2="230" y2="126" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="5 4"/>
    <text x="230" y="32" font-size="17" fill="{NAVY}" text-anchor="middle">a</text>
    <text x="230" y="144" font-size="17" fill="{NAVY}" text-anchor="middle">a</text>
  </g>
  <g data-step="2">
    <line id="cutFlash" x1="230" y1="44" x2="230" y2="120" stroke="{RED}" stroke-width="3.5"/>
    <g id="piece">
      <rect id="pieceRect" x="20" y="52" width="210" height="60" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
      <line id="pA2" x1="26" y1="0" x2="26" y2="48" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>
      <text x="36" y="20" font-size="20" fill="{RED}">{sym('P')}</text>
    </g>
    <g id="vm">
      <line id="vA" x1="738" y1="110" x2="738" y2="56" stroke="{TAU}" stroke-width="3" marker-end="url(#a_{TAU.strip('#')})"/>
      <text x="712" y="140" font-size="20" fill="{TAU}">{sym('V')}</text>
      <path id="mA" d="M748,40 A46,46 0 0 1 748,124" fill="none" stroke="{SIG}" stroke-width="2.5" marker-end="url(#a_{SIG.strip('#')})"/>
      <text x="790" y="88" font-size="20" fill="{SIG}">{sym('M')}</text>
      <text x="520" y="160" font-size="15" fill="{GREY}" font-style="italic">Left part, cut at a–a: internal V and M</text>
      <!-- sign tags (slide 3 tests): V up on the piece's RIGHT end tips it counterclockwise -> V < 0;
           held at the cut, pushed down at its free left end, the piece droops into a frown -> M < 0 -->
      <path d="M685,44 A90,90 0 0 0 565,44" fill="none" stroke="{TAU}" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#a_{TAU.strip('#')})"/>
      <text x="575" y="12" font-size="14" font-weight="bold" fill="{TAU}">tips counterclockwise: V &lt; 0</text>
      <path d="M730,52 Q625,52 520,68 L520,128 Q625,112 730,112 Z" fill="none" stroke="{SIG}" stroke-width="1.6" stroke-dasharray="6 4"/>
      <text x="625" y="88" font-size="15" font-weight="bold" fill="{SIG}" text-anchor="middle">frown: M &lt; 0</text>
    </g>
  </g>"""

    # section and plots (bottom row)
    sec = f"""
  <g data-step="3">
    <rect x="225" y="52" width="10" height="60" fill="{RED}" fill-opacity="0.3" stroke="{RED}" stroke-width="1.5"/>
    {''.join(f'<circle cx="230" cy="{52 + 15 * i}" r="2.6" fill="{RED}"/><text x="240" y="{56 + 15 * i}" font-size="10.5" fill="{RED}">{i + 1}</text>' for i in range(5))}
    <path d="M230,118 L230,166 L62,166 L62,{SEC_TOP - 8}" fill="none" stroke="{RED}" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#a_C00000)"/>
    <rect x="34" y="{SEC_TOP}" width="56" height="{SEC_H}" fill="{S['inner']}" stroke="{RED}" stroke-width="2"/>
    {''.join(f'<circle cx="62" cy="{SEC_TOP + SEC_H * i / 4}" r="4" fill="{RED}"/><text x="98" y="{SEC_TOP + SEC_H * i / 4 + 5}" font-size="14" font-weight="bold" fill="{RED}">{i + 1}</text>' for i in range(5))}
    <text x="20" y="{SEC_TOP + SEC_H + 22}" font-size="16" font-weight="bold">Section a–a</text>
    <text x="20" y="{SEC_TOP + SEC_H + 40}" font-size="13" fill="{GREY}" font-style="italic">(the cut face)</text>
    <line x1="24" y1="{yc}" x2="{COL_X + 50}" y2="{yc}" stroke="{GREY}" stroke-width="1" stroke-dasharray="4 4"/>
    <text x="0" y="{yc + 5}" font-size="13" fill="{GREY}">N.A.</text>
    <text x="{TAU_L}" y="{HEAD_Y}" font-size="16" font-weight="bold" fill="{TAU}">Shear stress {sym('τ')}</text>
    <line x1="{TAU_X}" y1="{SEC_TOP}" x2="{TAU_X}" y2="{SEC_TOP + SEC_H}" stroke="#000" stroke-width="1.5"/>
    <path id="tauCurve" fill="{TAU}" fill-opacity="0.18" stroke="{TAU}" stroke-width="2.5"/>
    <g id="tauHatch" stroke="{TAU}" stroke-width="1.5"></g>
    <text x="{TAU_X + TAU_W + 6}" y="{yc - 8}" font-size="15" fill="{TAU}">max at N.A.</text>
    <text x="{TAU_X + 18}" y="{SEC_TOP + SEC_H + 22}" font-size="14" fill="{GREY}">zero at top and bottom</text>
  </g>
  <g data-step="4">
    <line x1="{DIV1}" y1="{HEAD_Y - 22}" x2="{DIV1}" y2="{SEC_TOP + SEC_H + 30}" stroke="#c8c8c8" stroke-width="1.2"/>
    <text x="{SIG_L}" y="{HEAD_Y}" font-size="16" font-weight="bold" fill="{SIG}">Bending stress {sym('σ')}</text>
    <line x1="{SIG_X}" y1="{SEC_TOP}" x2="{SIG_X}" y2="{SEC_TOP + SEC_H}" stroke="#000" stroke-width="1.5"/>
    <path id="sigFill" fill="{SIG}" fill-opacity="0.15" stroke="none"/>
    <line id="sigLine" stroke="{SIG}" stroke-width="2.5"/>
    <g id="sigHatch" stroke="{SIG}" stroke-width="1.5"></g>
    <!-- labels on the white side of the axis (tension fill is right of the axis at the top, compression left at the bottom) -->
    <text x="{SIG_X - 8}" y="{SEC_TOP + 18}" font-size="15" font-weight="bold" fill="{SIG}" text-anchor="end">tension</text>
    <text x="{SIG_X + 8}" y="{SEC_TOP + SEC_H - 8}" font-size="15" font-weight="bold" fill="{SIG}">compression</text>
  </g>
  <g data-step="5">
    <line x1="{DIV2}" y1="{HEAD_Y - 22}" x2="{DIV2}" y2="{SEC_TOP + SEC_H + 30}" stroke="#c8c8c8" stroke-width="1.2"/>
    <text x="{COL_L}" y="{HEAD_Y}" font-size="16" font-weight="bold">Stress elements</text>
    <g id="col"></g>
  </g>
  <g data-step="6">
    <line id="mk" x1="30" x2="{COL_X - 90}" stroke="{RED}" stroke-width="2" stroke-dasharray="6 4"/>
    <circle id="mkTau" r="5" fill="{RED}"/><circle id="mkSig" r="5" fill="{RED}"/>
    <circle cx="{LIVE[0]}" cy="{LIVE[1]}" r="122" fill="#ffffff" stroke="{RED}" stroke-width="1.5"/>
    <g id="live"></g>
    <text x="{LIVE[0]}" y="{LIVE[1] + 144}" font-size="15" fill="{GREY}" font-style="italic" text-anchor="middle" id="liveCap">stresses at the red line</text>
  </g>
  <g data-step="6"><rect id="colHi" x="{COL_X - 96}" width="236" height="44" rx="6" fill="none" stroke="{RED}" stroke-width="2.2"/></g>
  <g data-step="7"></g><g data-step="8"></g><g data-step="9"></g><g data-step="10"></g>"""

    svg = f"""<svg class="fig" style="left:48px; top:112px" width="1184" height="590" viewBox="0 0 1184 590">
  <defs>{lib.markers(RED, SIG, TAU)}
    <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="8" stroke="{SUP}" stroke-width="1.5"/></pattern>
  </defs>
  {cant}
  {sec}
</svg>"""

    js = f"""<script>
{lib.ELASTIC_JS}
(() => {{
  const TOP = {SEC_TOP}, H = {SEC_H}, YC = TOP + H / 2;
  const TX = {TAU_X}, TW = {TAU_W}, SX = {SIG_X}, SW = {SIG_W}, CX = {COL_X};
  const SIG = "{SIG}", TAU = "{TAU}", EDGE = "{S['edge']}";
  const $ = id => document.getElementById(id);
  const TSIGN = 1;    // tau_xy > 0 (Hibbeler Fig. 15-2): right face up, left face down, top face right, bottom face left
  // nondimensional stresses at height y (px from the N.A., up positive): sigma/sigma_max, tau/tau_max
  const sig = y => y / (H / 2);
  const tau = y => 1 - (2 * y / H) ** 2;
  const f1 = v => v.toFixed(1);

  // stress plots at load level p (both scale with P)
  function plots(p) {{
    let d = 'M' + TX + ',' + TOP;
    for (let i = 0; i <= 60; i++) {{ const yy = TOP + H * i / 60; d += ' L' + f1(TX + p * TW * tau(YC - yy)) + ',' + f1(yy); }}
    $('tauCurve').setAttribute('d', d + ' Z');
    let hs = '', ss = '';
    for (let i = 1; i < 12; i++) {{
      const yy = TOP + H * i / 12;
      hs += `<line x1="${{TX}}" y1="${{f1(yy)}}" x2="${{f1(TX + p * TW * tau(YC - yy))}}" y2="${{f1(yy)}}"/>`;
      ss += `<line x1="${{SX}}" y1="${{f1(yy)}}" x2="${{f1(SX + p * SW * sig(YC - yy))}}" y2="${{f1(yy)}}"/>`;
    }}
    $('tauHatch').innerHTML = hs; $('sigHatch').innerHTML = ss;
    $('sigFill').setAttribute('d', `M${{SX}},${{TOP}} L${{f1(SX + p * SW)}},${{TOP}} L${{f1(SX - p * SW)}},${{TOP + H}} L${{SX}},${{TOP + H}} Z`);
    const L = $('sigLine');
    L.setAttribute('x1', f1(SX + p * SW)); L.setAttribute('y1', TOP); L.setAttribute('x2', f1(SX - p * SW)); L.setAttribute('y2', TOP + H);
  }}

  // stress element: square of half-side a at (cx, cy); s = sigma/sigma_max, t = tau/tau_max
  // ls, lt: arrow length for sigma_max, tau_max
  // The square deforms (exaggerated): stretched / squashed along x by sigma (with a little Poisson
  // contraction in y) and leaned by tau (top face moves right, right face moves up for tau_xy > 0).
  function elem(cx, cy, a, s, t, ls, lt, sw) {{
    const ex = 0, ey = 0, gm = 0;   // no shape change (user request): the square stays square
    const corner = (x, yu) => [cx + x * (1 + ex) + gm / 2 * yu, cy - (yu * (1 + ey) + gm / 2 * x)];
    const poly = [[-a, -a], [a, -a], [a, a], [-a, a]].map(([x, yu]) => corner(x, yu).map(f1).join(',')).join(' ');
    let g = `<polygon points="${{poly}}" fill="#e8ecf1" stroke="${{EDGE}}" stroke-width="1.5"/>`;
    const gap = 3, L = Math.abs(s) * ls, o = a * (1 + Math.abs(ex)) + gap + 2, so = o + 6 + sw;   // tau arrows hug the faces at o; sigma starts outside them at so
    if (L > 2) {{
      for (const side of [-1, 1]) {{
        const xin = cx + side * so, xout = cx + side * (so + L);
        const [x1, x2] = s > 0 ? [xin, xout] : [xout, xin];          // tension points out
        g += `<line x1="${{f1(x1)}}" y1="${{cy}}" x2="${{f1(x2)}}" y2="${{cy}}" stroke="${{SIG}}" stroke-width="${{f1(sw * (0.3 + 0.9 * Math.abs(s)))}}" marker-end="url(#a_{SIG.strip('#')})"/>`;   // line and tip grow with |sigma|
      }}
    }}
    const T = t * lt * TSIGN;
    if (Math.abs(T) > 2) {{
      const ln = (x1, y1, x2, y2) => `<line x1="${{f1(x1)}}" y1="${{f1(y1)}}" x2="${{f1(x2)}}" y2="${{f1(y2)}}" stroke="${{TAU}}" stroke-width="${{f1(sw * (0.3 + 0.9 * Math.abs(t)))}}" marker-end="url(#a_{TAU.strip('#')})"/>`;   // line and tip grow with |tau|
      g += ln(cx + o, cy + T / 2, cx + o, cy - T / 2);      // right face: up
      g += ln(cx - o, cy - T / 2, cx - o, cy + T / 2);      // left face: down
      g += ln(cx - T / 2, cy - o, cx + T / 2, cy - o);      // top face: right
      g += ln(cx + T / 2, cy + o, cx - T / 2, cy + o);      // bottom face: left
    }}
    return g;
  }}

  function column(p) {{
    let col = '';
    [1, 0.5, 0, -0.5, -1].forEach((r, i) => {{
      const y = r * H / 2, cy = YC - y;
      col += `<text x="${{CX - 80}}" y="${{cy + 5}}" font-size="16" font-weight="bold">${{i + 1}}</text>`;
      col += elem(CX, cy, 11, p * sig(y), p * tau(y), 30, 26, 2);
      col += `<text x="${{CX + 58}}" y="${{cy + 5}}" font-size="14" fill="#555555">y = ${{['h/2', 'h/4', '0', '−h/4', '−h/2'][i]}}</text>`;
    }});
    $('col').innerHTML = col;
  }}

  // load cycle (from click 1): P rises, holds, drops, rests; every stress follows P
  const lclock = revealClock(1), clock = revealClock(6), cclock = revealClock(2);
  // which point (0-4) the marker is on: from the deck's click count, or (single file) every 2.5 s
  let stepK = null;
  addEventListener('buildstep', e => {{ stepK = e.detail.k; }});
  const pointIdx = () => stepK !== null ? Math.min(4, Math.max(0, stepK - 6))
                                        : Math.floor((isNaN(FIXED_T) ? clock() : FIXED_T) / 2.5) % 5;
  let yCur = H / 2;
  function loadLevel(t) {{
    const c = t % 8;
    return c < 2 ? smooth(c / 2) : c < 5 ? 1 : c < 6.5 ? 1 - smooth((c - 5) / 1.5) : 0;
  }}
  plots(1);
  function draw() {{
    const p = stepK !== null && stepK >= 6 ? 1 : loadLevel(lclock());   // full load while stepping through the points
    for (const id of ['pA1', 'pA2']) $(id).setAttribute('y1', f1(48 - 8 - 40 * p));
    // cantilever bends with P (exaggerated): wall at x = 440, free end at x = 20, length L = 420.
    // Tip load: w(s) = P s^2 (3L - s) / (6EI), s from the wall; scaled so the tip moves DTIP px at full load.
    const CL = 420, DTIP = 24, wv = x => {{ const s = (440 - x) / CL; return DTIP * p * s * s * (3 - s) / 2; }};
    let top = '', bot = '';
    for (let i = 0; i <= 42; i++) {{ const x = 440 - CL * i / 42; top += ` L${{f1(x)}},${{f1(52 + wv(x))}}`; }}
    for (let i = 42; i >= 0; i--) {{ const x = 440 - CL * i / 42; bot += ` L${{f1(x)}},${{f1(112 + wv(x))}}`; }}
    $('cantBody').setAttribute('d', 'M' + top.slice(2) + bot + ' Z');
    const tip = wv(20);
    $('pA1').setAttribute('y1', f1(48 - 8 - 40 * p + tip)); $('pA1').setAttribute('y2', f1(48 + tip));
    $('pPct').textContent = '  ' + Math.round(100 * p) + '%';
    // click 2: cut flashes (0-0.6 s), the right part slides out to the FBD place (0.6-1.9 s), V and M appear (1.9-2.7 s)
    const tc = cclock(), mv = smooth((tc - 0.6) / 1.3), ap = smooth((tc - 1.9) / 0.8);
    $('cutFlash').setAttribute('opacity', f1(tc < 0.6 ? 0.5 + 0.5 * Math.sin(tc * 20) : 1 - smooth((tc - 0.6) / 0.5)));
    $('piece').setAttribute('transform', `translate(${{f1(500 * mv)}}, ${{f1(-46 * Math.sin(Math.PI * mv))}})`);
    $('pieceRect').setAttribute('stroke', mv > 0 && mv < 1 ? '{RED}' : '{S['edge']}');
    $('vm').setAttribute('opacity', f1(ap));
    $('vA').setAttribute('y2', f1(110 - 54 * p)); $('vA').setAttribute('opacity', p > 0.05 ? 1 : 0);
    $('mA').setAttribute('opacity', f1(p)); $('mA').setAttribute('stroke-width', f1(1 + 2 * p));
    column(p);                                  // the curves stay fixed (drawn once at full load, user request)
    // marker steps through points 1-5, one per click (clicks 6-10); smooth move to the new point
    const target = (idx => [1, 0.5, 0, -0.5, -1][idx] * H / 2)(pointIdx());
    yCur += (target - yCur) * (isNaN(FIXED_T) ? 0.12 : 1);
    const y = yCur, yy = YC - y;
    $('colHi').setAttribute('y', f1(yy - 22));
    $('liveCap').textContent = 'stresses at point ' + (pointIdx() + 1);
    $('mk').setAttribute('y1', f1(yy)); $('mk').setAttribute('y2', f1(yy));
    $('mkTau').setAttribute('cx', f1(TX + TW * tau(y))); $('mkTau').setAttribute('cy', f1(yy));
    $('mkSig').setAttribute('cx', f1(SX + SW * sig(y))); $('mkSig').setAttribute('cy', f1(yy));
    $('live').innerHTML = elem({LIVE[0]}, {LIVE[1]}, 32, p * sig(y), p * tau(y), 60, 56, 3.5) +
      `<text x="{LIVE[0]}" y="{LIVE[1] - 92}" font-size="18" fill="${{SIG}}" text-anchor="middle"><tspan class="sym">σ</tspan> = ${{(p * sig(y)).toFixed(2).replace('-', '−')}} <tspan class="sym">σ</tspan><tspan baseline-shift="sub" font-size="70%">max</tspan></text>` +
      `<text x="{LIVE[0]}" y="{LIVE[1] + 104}" font-size="18" fill="${{TAU}}" text-anchor="middle"><tspan class="sym">τ</tspan> = ${{(p * tau(y)).toFixed(2)}} <tspan class="sym">τ</tspan><tspan baseline-shift="sub" font-size="70%">max</tspan></text>`;
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + """
  .pts { font-size: 18px; }
  .fm { position: absolute; font-size: 19px; }
  .fcap { position: absolute; left: 198px; top: 360px; width: 205px; line-height: 1.3; font-size: 12.5px; color: #555555; }
"""
    pts_f = (f'  <div class="fm" data-step="3" style="left:198px; top:304px; color:{TAU}"><math displaystyle="true"><mi>τ</mi><mo>=</mo><mfrac><mrow><mi>V</mi><mi>Q</mi></mrow><mrow><mi>I</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>V</mi></mrow><mrow><mn>2</mn><mi>A</mi></mrow></mfrac><mrow><mo>(</mo><mn>1</mn><mo>−</mo><mfrac><mrow><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><msup><mi>h</mi><mn>2</mn></msup></mfrac><mo>)</mo></mrow></math></div>\n'
             f'  <div class="fm" data-step="4" style="left:448px; top:304px; color:{SIG}"><math displaystyle="true"><mi>σ</mi><mo>=</mo><mo>−</mo><mfrac><mrow><mi>M</mi><mi>y</mi></mrow><mi>I</mi></mfrac></math></div>\n'
             '  <div class="fcap" data-step="3" style="width:218px"><i>y</i>: height above the N.A.<br>rectangle: <i>t</i> = <i>b</i>, '
             '<i>Q</i> = (<i>b</i>/2)(<i>h</i>²/4 − <i>y</i>²)</div>\n'
             '  <div class="fcap" data-step="4" style="left:448px; width:195px"><i>M</i> &lt; 0 here (hogging):<br>top in tension</div>\n')
    pts = f"""  <ul class="pts" style="left:870px; top:122px; width:360px">
    <li data-step="3"><b style="color:{TAU}">Shear stress</b>: a parabola, largest at the neutral axis, zero at the top and bottom.</li>
    <li data-step="4"><b style="color:{SIG}">Bending stress</b>: a straight line, largest at the top and bottom, zero at the neutral axis.</li>
    <li data-step="5"><b>1, 5</b>: bending only. <b>3</b>: shear only. <b>2, 4</b>: both.</li>
    <li data-step="5">Stress <b><math><mo>∝</mo><mi>P</mi></math></b>: double the load, double σ and τ.</li>
  </ul>"""
    title = 'Stress <span class="key">changes</span> from point to point in a section'
    body = svg + "\n" + pts_f + js + "\n" + pts + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.1, pp. 688–689, Fig. 15-2. From ' + lib.M_FLEX + ', ' + lib.M_SHEAR +
        '; σ, τ arrows on separate scales; deflection exaggerated.</div>')
    lib.write_page("03_slide3_section.html", "Slide 6 - Stress in a section", title, body, 6, css)


if __name__ == "__main__":
    build()
