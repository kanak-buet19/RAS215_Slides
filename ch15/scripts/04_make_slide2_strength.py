"""Slide 2 - Beams are designed for bending and shear stress (Sec. 15.1, p. 688, Fig. 15-1).

Left: a simply supported beam with a point load P and a uniform load w on the
right part (as in Fig. 15-1). On its click the loads drop in and the beam bends.
The deflected shape is the elastic curve computed from M(x) for these loads
(01_slide_lib.ELASTIC_JS), exaggerated to 14 px.
Then two zoom bubbles show stress elements:
  - top fibre under P: sigma_x (compression) and a small sigma_y (the load pressing in)
  - bottom fibre: sigma_x (tension)
Arrow lengths are illustrative (sigma_x >> sigma_y), not computed.
Last panel: point load vs bearing plate. The same force P on a wider plate gives
a lower contact pressure: the pressure block keeps its area (force) while its
width grows, so its height (stress) drops.

Writes ../slides/separate/02_slide2_strength.html.
Run:  python3 04_make_slide2_strength.py
"""
import importlib
import json

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SUP, SIGY = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT, lib.SIGY
sym = lib.sym

G = dict(x0=40, L=600, yT=190, D=36, A=14,          # beam: left end, span, top edge, depth (svg px), max deflection
         Pa=180, wa=380, wb=560,                    # P position, uniform load from wa to wb (from the left end)
         N=120)


def element(cx, cy, kind):
    """Stress element (square) with arrows; kind 'top' (compression + sigma_y) or 'bot' (tension)."""
    s = 20     # half side
    out = f'<rect x="{cx - s}" y="{cy - s}" width="{2 * s}" height="{2 * s}" fill="#e8ecf1" stroke="{S["edge"]}" stroke-width="1.5"/>'
    if kind == "top":   # sigma_x pushes in (compression), small sigma_y presses the top and bottom faces
        out += (f'<line x1="{cx - s - 40}" y1="{cy}" x2="{cx - s - 3}" y2="{cy}" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#a_002060)"/>'
                f'<line x1="{cx + s + 40}" y1="{cy}" x2="{cx + s + 3}" y2="{cy}" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#a_002060)"/>'
                f'<line x1="{cx}" y1="{cy - s - 14}" x2="{cx}" y2="{cy - s - 3}" stroke="{SIGY}" stroke-width="2.5" marker-end="url(#a_{SIGY[1:]})"/>'
                f'<line x1="{cx}" y1="{cy + s + 14}" x2="{cx}" y2="{cy + s + 3}" stroke="{SIGY}" stroke-width="2.5" marker-end="url(#a_{SIGY[1:]})"/>'
                f'<text x="{cx - s - 26}" y="{cy + 24}" font-size="17" fill="{NAVY}" text-anchor="middle">{sym("σ", "x")}</text>'
                f'<text x="{cx + 8}" y="{cy - s - 8}" font-size="17" fill="{SIGY}">{sym("σ", "y")}</text>')
    else:               # tension: arrows point out
        out += (f'<line x1="{cx - s - 3}" y1="{cy}" x2="{cx - s - 40}" y2="{cy}" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#a_002060)"/>'
                f'<line x1="{cx + s + 3}" y1="{cy}" x2="{cx + s + 40}" y2="{cy}" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#a_002060)"/>'
                f'<text x="{cx + s + 22}" y="{cy + 24}" font-size="17" fill="{NAVY}" text-anchor="middle">{sym("σ", "x")}</text>')
    return out


def build():
    x0, L, yT, D = G["x0"], G["L"], G["yT"], G["D"]
    # zoom bubbles (fixed), leaders drawn by JS to the moving beam
    b1 = (95, 92)       # top element bubble centre
    b2 = (470, 335)     # bottom element bubble centre
    R = 60
    bubbles = f"""
  <g data-step="2">
    <circle cx="{b1[0]}" cy="{b1[1]}" r="{R}" fill="#ffffff" stroke="{NAVY}" stroke-width="1.5"/>
    <line id="lead1" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="4 3"/>
    <circle id="dot1" r="4" fill="{NAVY}"/>
    {element(*b1, "top")}
    <text x="{b1[0] + R + 8}" y="{b1[1] - 30}" font-size="15" fill="{GREY}" font-style="italic">top, under the load</text>
  </g>
  <g data-step="3">
    <circle cx="{b2[0]}" cy="{b2[1]}" r="{R}" fill="#ffffff" stroke="{NAVY}" stroke-width="1.5"/>
    <line id="lead2" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="4 3"/>
    <circle id="dot2" r="4" fill="{NAVY}"/>
    {element(*b2, "bot")}
    <text x="{b2[0]}" y="{b2[1] + R + 18}" font-size="15" text-anchor="middle" fill="{GREY}" font-style="italic">bottom</text>
  </g>"""

    # bearing plate panel (step 4), drawn at y >= 420
    py = 505              # beam top in the panel
    panel = f"""
  <g data-step="4">
    <text x="20" y="432" font-size="18" font-weight="bold">a.</text><text x="42" y="432" font-size="18" font-weight="bold">Point load</text>
    <text x="350" y="432" font-size="18" font-weight="bold">b.</text><text x="372" y="432" font-size="18" font-weight="bold">With a bearing plate</text>
    <rect x="20" y="{py}" width="290" height="30" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <rect x="350" y="{py}" width="290" height="30" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <line x1="165" y1="{py - 52}" x2="165" y2="{py - 4}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>
    <text x="175" y="{py - 30}" font-size="18" fill="{RED}">{sym("P")}</text>
    <rect x="160" y="{py}" width="10" height="64" fill="{SIGY}" opacity="0.75"/>
    <text x="180" y="{py + 52}" font-size="15" fill="{SIGY}">high {sym("σ", "y")}</text>
    <text x="180" y="{py + 70}" font-size="13" fill="{GREY}" font-style="italic">(purple = contact pressure = σ<tspan baseline-shift="sub" font-size="70%">y</tspan>)</text>
    <line x1="495" y1="{py - 52}" x2="495" y2="{py - 16}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>
    <text x="505" y="{py - 30}" font-size="18" fill="{RED}">{sym("P")}</text>
    <rect id="plate" y="{py - 12}" height="12" fill="#5d646e" stroke="{S['edge']}"/>
    <rect id="press" y="{py}" fill="{SIGY}" opacity="0.75"/>
    <text id="pressLbl" font-size="15" fill="{SIGY}">low {sym("σ", "y")}</text>
  </g>"""

    svg = f"""<svg class="fig" style="left:48px; top:112px" width="680" height="590" viewBox="0 0 680 590">
  <defs>{lib.markers(RED, NAVY, "#000000", SIGY)}
    <radialGradient id="syg"><stop offset="0" stop-color="{SIGY}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{SIGY}" stop-opacity="0.3"/><stop offset="1" stop-color="{SIGY}" stop-opacity="0"/></radialGradient>
    <clipPath id="beamClip"><use href="#beam"/></clipPath>
  </defs>
  <g data-step="1">
    <g id="sup" fill="#ffffff" stroke="{SUP}" stroke-width="2"></g>
    <path id="beam" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <g id="loads"></g>
    <g transform="translate(40, 368)">
      <line x1="0" y1="0" x2="74" y2="0" stroke="#000" stroke-width="2" marker-end="url(#a_000000)"/>
      <line x1="0" y1="0" x2="0" y2="-74" stroke="#000" stroke-width="2" marker-end="url(#a_000000)"/>
      <circle cx="0" cy="0" r="8" fill="#fff" stroke="#000" stroke-width="1.8"/><circle cx="0" cy="0" r="2.5" fill="#000"/>
      <text x="82" y="6" font-size="20">{sym('x')}</text>
      <text x="-6" y="-84" font-size="20">{sym('y')}</text>
      <text x="-26" y="24" font-size="20">{sym('z')}</text>
      <text x="120" y="-58" font-size="14" fill="{GREY}" font-style="italic">x: along the beam</text>
      <text x="120" y="-38" font-size="14" fill="{GREY}" font-style="italic">y: up</text>
      <text x="120" y="-18" font-size="14" fill="{GREY}" font-style="italic">z: out of the page</text>
    </g>
  </g>
  <g data-step="2">
    <g clip-path="url(#beamClip)"><ellipse id="bP" fill="url(#syg)"/><ellipse id="bA" fill="url(#syg)"/><ellipse id="bB" fill="url(#syg)"/></g>
    <g id="squeeze"></g>
    <text id="syLbl" font-size="16" font-weight="bold" fill="{SIGY}" text-anchor="middle">{sym('σ', 'y')} <tspan font-size="14" font-weight="normal" font-style="italic">(vertical squeeze, only here)</tspan></text>
    <text id="syA" font-size="16" font-weight="bold" fill="{SIGY}">{sym('σ', 'y')}</text>
    <text id="syB" font-size="16" font-weight="bold" fill="{SIGY}" text-anchor="end">{sym('σ', 'y')}</text>
  </g>
  {bubbles}
  {panel}
</svg>"""

    js = f"""<script>
{lib.ELASTIC_JS}
(() => {{
  const G = {json.dumps(G)};
  const {{x0, L, yT, D, A, Pa, wa, wb, N}} = G;
  const RED = "{RED}", SIGY = "{SIGY}";
  const shape = elasticCurve(L, [{{type: 'P', a: Pa, P: 1}}, {{type: 'w', a: wa, b: wb, w: 1 / 120}}], N);
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1);
  const clock1 = revealClock(1), clock2 = revealClock(2), clock4 = revealClock(4);
  const defl = (X, s) => A * s * shape[Math.round(X / L * N)];

  function draw() {{
    const t = clock1();
    const drop = smooth(t / 0.8), s = smooth((t - 0.8) / 1.4);
    // beam outline
    const top = [], bot = [];
    for (let i = 0; i <= N; i++) {{ const X = L * i / N, d = A * s * shape[i];
      top.push((x0 + X).toFixed(1) + ',' + (yT + d).toFixed(1));
      bot.unshift((x0 + X).toFixed(1) + ',' + (yT + D + d).toFixed(1)); }}
    $('beam').setAttribute('d', 'M' + top.concat(bot).join(' L') + 'Z');
    // supports: pin at 0, roller at L (ends do not deflect)
    const ys = yT + D;
    $('sup').innerHTML =
      `<polygon points="${{x0}},${{ys}} ${{x0 - 13}},${{ys + 22}} ${{x0 + 13}},${{ys + 22}}"/>` +
      `<line x1="${{x0 - 22}}" y1="${{ys + 23}}" x2="${{x0 + 22}}" y2="${{ys + 23}}"/>` +
      `<polygon points="${{x0 + L}},${{ys}} ${{x0 + L - 12}},${{ys + 16}} ${{x0 + L + 12}},${{ys + 16}}"/>` +
      `<circle cx="${{x0 + L - 6}}" cy="${{ys + 20}}" r="3.5" stroke-width="1.5"/><circle cx="${{x0 + L + 6}}" cy="${{ys + 20}}" r="3.5" stroke-width="1.5"/>` +
      `<line x1="${{x0 + L - 22}}" y1="${{ys + 24}}" x2="${{x0 + L + 22}}" y2="${{ys + 24}}"/>`;
    // loads drop in from 40 px above
    const lift = 40 * (1 - drop);
    let g = '';
    const px = x0 + Pa, py = yT + defl(Pa, s) - 3 - lift;
    g += `<line x1="${{px}}" y1="${{py - 70}}" x2="${{px}}" y2="${{py}}" stroke="${{RED}}" stroke-width="3" marker-end="url(#a_C00000)"/>`;
    g += `<text x="${{px + 10}}" y="${{py - 50}}" font-size="20" fill="${{RED}}"><tspan class="sym">P</tspan></text>`;
    const tails = [];
    for (let X = wa; X <= wb + 0.1; X += (wb - wa) / 6) {{
      const y = yT + defl(X, s) - 3 - lift;
      tails.push(`${{x0 + X}},${{y - 36}}`);
      g += `<line x1="${{x0 + X}}" y1="${{y - 36}}" x2="${{x0 + X}}" y2="${{y}}" stroke="${{RED}}" stroke-width="2" marker-end="url(#a_C00000)"/>`;
    }}
    g += `<polyline points="${{tails.join(' ')}}" fill="none" stroke="${{RED}}" stroke-width="2"/>`;
    g += `<text x="${{x0 + (wa + wb) / 2}}" y="${{yT - 50 - lift}}" font-size="20" fill="${{RED}}" text-anchor="middle"><tspan class="sym">w</tspan></text>`;
    $('loads').innerHTML = g;
    $('loads').setAttribute('opacity', drop.toFixed(3));
    // sigma_y: strong at the contact, fades with depth, zero at the free bottom face (clipped to the beam)
    const yP = yT + defl(Pa, s);
    const el = (id, cx, cy, rx, ry) => {{ const e = $(id); e.setAttribute('cx', f1(cx)); e.setAttribute('cy', f1(cy));
      e.setAttribute('rx', rx); e.setAttribute('ry', ry); e.setAttribute('opacity', drop.toFixed(2)); }};
    el('bP', x0 + Pa, yP, 48, D);
    el('bA', x0, yT + D, 30, D * 0.8); el('bB', x0 + L, yT + D, 30, D * 0.8);
    $('syLbl').setAttribute('x', x0 + Pa); $('syLbl').setAttribute('y', f1(yP + D + 24));
    $('syA').setAttribute('x', x0 + 22); $('syA').setAttribute('y', yT + D + 20);
    $('syB').setAttribute('x', x0 + L - 22); $('syB').setAttribute('y', yT + D + 20);
    // small purple arrows inside the shading: the material is pushed down under P
    let sq = '';
    for (const dx of [-20, 20]) sq += `<line x1="${{x0 + Pa + dx}}" y1="${{f1(yP + 5)}}" x2="${{x0 + Pa + dx}}" y2="${{f1(yP + 22)}}" stroke="${{SIGY}}" stroke-width="2.2" marker-end="url(#a_${{SIGY.slice(1)}})" opacity="${{drop.toFixed(2)}}"/>`;
    $('squeeze').innerHTML = sq;
    // sigma_x / sigma_y vs span: L/h runs from 1 to 12
    const tr = clock2() % 9, r = 1 + 11 * smooth(tr / 5), K = 3.4;
    $('barY').setAttribute('width', Math.max(3, K).toFixed(1));
    $('barX').setAttribute('width', f1(K * 0.75 * r * r));
    $('ratTxt').textContent = Math.round(0.75 * r * r) + '×';
    $('ratTxt').setAttribute('x', f1(60 + K * 0.75 * r * r + 8));
    $('lhTxt').textContent = 'L/h = ' + r.toFixed(1);
    $('mini').setAttribute('width', f1(10 * r)); $('lhTxt').setAttribute('x', f1(60 + 10 * r + 8));
    // leaders from the bubbles to the beam
    const p1 = [x0 + Pa - 10, yT + defl(Pa - 10, s) + 5], p2 = [x0 + 430, yT + D + defl(430, s) - 4];
    $('dot1').setAttribute('cx', p1[0]); $('dot1').setAttribute('cy', p1[1]);
    $('lead1').setAttribute('x1', {b1[0] + R * 0.8:.1f}); $('lead1').setAttribute('y1', {b1[1] + R * 0.6:.1f});
    $('lead1').setAttribute('x2', p1[0]); $('lead1').setAttribute('y2', p1[1]);
    $('dot2').setAttribute('cx', p2[0]); $('dot2').setAttribute('cy', p2[1]);
    $('lead2').setAttribute('x1', {b2[0]:.1f}); $('lead2').setAttribute('y1', {b2[1] - R:.1f});
    $('lead2').setAttribute('x2', p2[0]); $('lead2').setAttribute('y2', p2[1]);
    // bearing plate grows from 10 to 160 px wide; pressure block keeps its area (640 px^2, as in panel a)
    const u = smooth((clock4() - 0.6) / 1.6), pw = 10 + 150 * u, ph = 640 / pw;
    $('plate').setAttribute('x', 495 - pw / 2); $('plate').setAttribute('width', pw);
    $('press').setAttribute('x', 495 - pw / 2); $('press').setAttribute('width', pw); $('press').setAttribute('height', ph);
    $('pressLbl').setAttribute('x', 495 + pw / 2 + 8); $('pressLbl').setAttribute('y', {py} + Math.max(16, ph));
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + f"""
  .ratio {{ position: absolute; left: 930px; top: 456px; font-size: 20px; }}
  .concl {{ position: absolute; left: 770px; top: 612px; width: 440px; padding: 10px 14px; font-size: 20px;
           border: 2px solid {RED}; border-radius: 6px; background: #fbecec; }}
"""
    ratio = f"""  <svg class="fig" data-step="2" style="left:770px; top:474px" width="460" height="118" viewBox="0 0 460 118">
    <text x="0" y="22" font-size="16" font-weight="bold">How much bigger?</text>
    <text x="0" y="64" font-size="16" fill="{SIGY}">{sym('σ', 'y')}</text><rect id="barY" x="60" y="51" height="16" fill="{SIGY}"/>
    <text x="0" y="88" font-size="16" fill="{NAVY}">{sym('σ', 'x')}</text><rect id="barX" x="60" y="75" height="16" fill="{NAVY}"/>
    <text id="ratTxt" y="89" font-size="16" font-weight="bold" fill="{RED}"></text>
    <rect id="mini" x="60" y="104" height="8" fill="{S['front']}" stroke="{S['edge']}"/>
    <text x="0" y="113" font-size="14" fill="{GREY}">beam</text><text id="lhTxt" y="113" font-size="14" fill="{GREY}"></text>
  </svg>
"""
    ratio += '  <div class="ratio" data-step="2"><math displaystyle="true"><mfrac><msub><mi>σ</mi><mi>x</mi></msub><msub><mi>σ</mi><mi>y</mi></msub></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mrow><mo>(</mo><mfrac><mi>L</mi><mi>h</mi></mfrac><mo>)</mo></mrow><mn>2</mn></msup></math></div>\n'
    pts = ratio + f"""  <ul class="pts" style="left:770px; top:130px; width:450px">
    <li data-step="1">Loads act <b>perpendicular</b> to the beam axis, so the beam <b>bends</b>.</li>
    <li data-step="2">Where a load presses on the beam, the material is also squeezed vertically: <span style="color:{SIGY}">{lib.mi('σ', 'y')}</span>. It fades within about one depth and is zero at the bottom. It does not grow with the span: <span class="em">{lib.mi('σ', 'x')} ≫ {lib.mi('σ', 'y')}</span>.</li>
    <li data-step="3">Everywhere else: bending stress {lib.mi('σ', 'x')} (tension at the bottom here) and shear stress {lib.mi('τ', 'xy')}.</li>
    <li data-step="4"><b>Bearing plates</b> spread a concentrated load over a larger area: same force, bigger area, so {lib.mi('σ', 'y')} drops even more.</li>
  </ul>
  <div class="concl" data-step="5"><b>So beams are designed for bending stress {lib.mi('σ', 'x')} and shear stress {lib.mi('τ')}.</b></div>"""
    title = 'Beams are designed for <span class="key">bending</span> and shear stress'
    body = svg + "\n" + pts + "\n" + js + (f'\n  <div class="note">{lib.SOURCE}, Sec. 15.1, p. 688, Fig. 15-1. '
                                         'Deflection exaggerated; σ<sub>y</sub> shading schematic; ratio for a rectangular beam, uniform load.</div>')
    lib.write_page("02_slide2_strength.html", "Slide 5 - Designed for strength", title, body, 5, css)


if __name__ == "__main__":
    build()
