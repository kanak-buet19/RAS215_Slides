"""Slide 5 - Strength is not the only limit (Sec. 15.1, p. 688).

Two looping illustrations (not simulations), each starting on its click:
a. Sideways buckling. Two 3-D W-beams under the same growing load
   (01_slide_lib.IBEAM_JS). The unbraced one stays straight at first, then
   suddenly moves sideways and twists, the top (compression) flange the most:
   shift u(x) and twist phi(x) both follow sin(pi x / L), with fork supports
   at the ends (no shift, no twist there). The braced one has cross members
   tied to its top flange and stays straight.
b. Deflection. A beam with a plaster ceiling hung under it. Under a uniform load
   it sags along the elastic curve (01_slide_lib.ELASTIC_JS), exaggerated. When the
   sag passes the allowable line the brittle ceiling cracks.

Writes ../slides/separate/05_slide5_limits.html.
Run:  python3 07_make_slide5_limits.py
"""
import importlib
import json

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SUP = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT

BEAM = dict(L=330, d=40, bf=58, tf=7, tw=6, cx=0.62, cy=0.38, N=40, col=S)
UNBR = dict(BEAM, X0=50, Y0=150)
BRAC = dict(BEAM, X0=50, Y0=370)
EV_X = 500                     # x of the mid-span end views
DEF = dict(x0=640, L=480, yT=150, D=26, hang=34, ceil=10, A=26, lim=13)   # panel b: beam, ceiling, sag (px)


def build():
    svg = f"""<svg class="fig" style="left:48px; top:112px" width="1184" height="590" viewBox="0 0 1184 590">
  <defs>{lib.markers(RED, NAVY)}</defs>
  <g data-step="1">
    <text x="10" y="18" font-size="20" font-weight="bold">a.</text>
    <text x="34" y="18" font-size="20" font-weight="bold">Sideways buckling</text>
    <text x="34" y="52" font-size="16" fill="{GREY}" font-style="italic">Not braced</text>
    <g id="unbr"></g><g id="unbrLoad"></g><g id="unbrSup" fill="#fff" stroke="{SUP}" stroke-width="2"></g>
    <text id="bkl" x="190" y="52" font-size="16" font-weight="bold" fill="{RED}">buckles sideways and twists</text>
    <g id="ev1"></g><text x="{EV_X}" y="232" font-size="13" fill="{GREY}" text-anchor="middle">mid-span section</text>
    <text x="34" y="276" font-size="16" fill="{GREY}" font-style="italic">Braced along its length</text>
    <g id="braces"></g>
    <g id="brac"></g><g id="bracLoad"></g><g id="bracSup" fill="#fff" stroke="{SUP}" stroke-width="2"></g>
    <text x="240" y="276" font-size="16" font-weight="bold" fill="{NAVY}">stays straight</text>
    <g id="ev2"></g><text x="{EV_X}" y="452" font-size="13" fill="{GREY}" text-anchor="middle">mid-span section</text>
  </g>
  <line x1="590" y1="0" x2="590" y2="470" stroke="#c9ccd1" stroke-width="1.2" stroke-dasharray="5 5"/>
  <g data-step="2">
    <text x="620" y="18" font-size="20" font-weight="bold">b.</text>
    <text x="644" y="18" font-size="20" font-weight="bold">Too much deflection</text>
    <g id="defLoad"></g>
    <path id="defBeam" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <g id="hangers" stroke="#7a7f86" stroke-width="1.5"></g>
    <path id="ceil" fill="#f2efe8" stroke="#a49e90" stroke-width="1.5"/>
    <g id="defSup" fill="#fff" stroke="{SUP}" stroke-width="2"></g>
    <line id="limLine" stroke="{RED}" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text id="limTxt" font-size="15" fill="{RED}">allowable sag</text>
    <g id="cracks" stroke="{RED}" stroke-width="2.5" fill="none" stroke-linejoin="round"></g>
    <text id="crTxt" font-size="16" font-weight="bold" fill="{RED}">plaster cracks</text>
    <text x="{DEF['x0']}" y="{DEF['yT'] + 160}" font-size="15" fill="{GREY}" font-style="italic">plaster ceiling hung under the beam</text>
  </g>
</svg>"""

    js = f"""<script>
{lib.ELASTIC_JS}
{lib.IBEAM_JS}
(() => {{
  const UN = {json.dumps(UNBR)}, BR = {json.dumps(BRAC)}, DF = {json.dumps(DEF)};
  const RED = "{RED}", SUP = "{SUP}";
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1);
  const c1 = revealClock(1), c2 = revealClock(2);
  const T = 9;

  function loads(P, o, s, n) {{       // load arrows on the top flange centre line
    let g = '', tails = [];
    for (let i = 0; i < n; i++) {{
      const X = 12 + (o.L - 24) * i / (n - 1), tip = P(X, o.d / 2 + 2, 0);
      const len = 14 + 22 * s;
      tails.push(f1(tip[0]) + ',' + f1(tip[1] - len));
      g += `<line x1="${{f1(tip[0])}}" y1="${{f1(tip[1] - len)}}" x2="${{f1(tip[0])}}" y2="${{f1(tip[1])}}" stroke="${{RED}}" stroke-width="2" marker-end="url(#a_C00000)"/>`;
    }}
    return g + `<polyline points="${{tails.join(' ')}}" fill="none" stroke="${{RED}}" stroke-width="2"/>`;
  }}
  function supports(P, o) {{
    let g = '';
    for (const X of [0, o.L]) {{
      const p = P(X, -o.d / 2, o.bf / 2);
      const h = X ? 14 : 18;                         // pin at 0, roller at L (triangle on two wheels)
      g += `<polygon points="${{f1(p[0])}},${{f1(p[1])}} ${{f1(p[0] - 11)}},${{f1(p[1] + h)}} ${{f1(p[0] + 11)}},${{f1(p[1] + h)}}"/>`;
      if (X) g += `<circle cx="${{f1(p[0] - 5.5)}}" cy="${{f1(p[1] + 17.5)}}" r="3.3"/><circle cx="${{f1(p[0] + 5.5)}}" cy="${{f1(p[1] + 17.5)}}" r="3.3"/>`;
    }}
    return g;
  }}

  // braces: short cross members tied to the top flange, going back (-z)
  const braceX = [66, 132, 198, 264];
  function bracesSvg(P, o) {{
    let g = '';
    for (const X of braceX) {{
      const a = P(X, o.d / 2, -o.bf / 2), b = P(X, o.d / 2, -o.bf / 2 - 70);
      g += `<line x1="${{f1(a[0])}}" y1="${{f1(a[1])}}" x2="${{f1(b[0])}}" y2="${{f1(b[1])}}" stroke="#6b737d" stroke-width="6" stroke-linecap="round"/>`;
    }}
    return g;
  }}

  // end view of the mid-span section: z drawn to the left (-z to the right, as in the 3-D view), y up
  function endView(g, cx, cy, q) {{
    const k = 1.15, h = UN.d / 2, b = UN.bf / 2, tf = UN.tf, t = UN.tw / 2;
    const SEC = [[h, -b], [h, b], [h - tf, b], [h - tf, t], [-h + tf, t], [-h + tf, b], [-h, b], [-h, -b],
                 [-h + tf, -b], [-h + tf, -t], [h - tf, -t], [h - tf, -b]];
    const pt = (y, z, c, sn, u) => [cx - k * (y * sn + z * c + u), cy - k * (y * c - z * sn)];
    const poly = (c, sn, u) => SEC.map(([y, z]) => pt(y, z, c, sn, u).map(f1).join(',')).join(' ');
    g.innerHTML = `<polygon points="${{poly(1, 0, 0)}}" fill="none" stroke="#9aa1aa" stroke-width="1.2" stroke-dasharray="4 3"/>` +
      `<polygon points="${{poly(Math.cos(q.phi), Math.sin(q.phi), q.u)}}" fill="${{'{S['front']}'}}" stroke="${{'{S['edge']}'}}" stroke-width="1.5"/>`;
  }}

  function draw() {{
    // ----- a. buckling -----
    const t = c1() % T;
    const s = t < 3 ? smooth(t / 3) : t < 6.5 ? 1 : 1 - smooth((t - 6.5) / 1.5);     // load level
    const b = smooth((s - 0.6) / 0.25);                                                // buckling sets in suddenly near full load
    const unDisp = X => {{ const m = Math.sin(Math.PI * X / UN.L); return {{w: 0, u: -34 * b * m, phi: -0.42 * b * m}}; }};
    const P1 = drawIBeam($('unbr'), UN, unDisp);
    $('unbrLoad').innerHTML = loads(P1, UN, s, 11);
    $('unbrSup').innerHTML = supports(P1, UN);
    $('bkl').setAttribute('opacity', b.toFixed(2));
    endView($('ev1'), {EV_X}, 160, unDisp(UN.L / 2));
    // braced: braces drawn first (behind), beam stays straight
    const still = X => ({{w: 0, u: 0, phi: 0}});
    const P2 = drawIBeam($('brac'), BR, still);
    $('braces').innerHTML = bracesSvg(P2, BR);
    $('bracLoad').innerHTML = loads(P2, BR, s, 11);
    $('bracSup').innerHTML = supports(P2, BR);
    endView($('ev2'), {EV_X}, 380, still(0));

    // ----- b. deflection -----
    const t2 = c2() % T;
    const s2 = t2 < 3.5 ? smooth(t2 / 3.5) : t2 < 7 ? 1 : 1 - smooth((t2 - 7) / 1.5);
    const N = 80, {{x0, L, yT, D, hang, ceil, A, lim}} = DF;
    const shape = elasticCurve(L, [{{type: 'w', a: 0, b: L, w: 1}}], N);
    const top = [], bot = [], ct = [], cb = [];
    for (let i = 0; i <= N; i++) {{
      const x = x0 + L * i / N, dv = A * s2 * shape[i];
      top.push(f1(x) + ',' + f1(yT + dv)); bot.unshift(f1(x) + ',' + f1(yT + D + dv));
      ct.push(f1(x) + ',' + f1(yT + D + hang + dv)); cb.unshift(f1(x) + ',' + f1(yT + D + hang + ceil + dv));
    }}
    $('defBeam').setAttribute('d', 'M' + top.concat(bot).join(' L') + 'Z');
    $('ceil').setAttribute('d', 'M' + ct.concat(cb).join(' L') + 'Z');
    let hg = '';
    for (let i = 1; i < 8; i++) {{
      const X = L * i / 8, dv = A * s2 * shape[Math.round(i * N / 8)];
      hg += `<line x1="${{f1(x0 + X)}}" y1="${{f1(yT + D + dv)}}" x2="${{f1(x0 + X)}}" y2="${{f1(yT + D + hang + dv)}}"/>`;
    }}
    $('hangers').innerHTML = hg;
    let lg = '', tails = [];
    for (let i = 0; i <= 10; i++) {{
      const X = L * i / 10, y = yT + A * s2 * shape[Math.round(i * N / 10)] - 3, len = 12 + 22 * s2;
      tails.push(f1(x0 + X) + ',' + f1(y - len));
      lg += `<line x1="${{f1(x0 + X)}}" y1="${{f1(y - len)}}" x2="${{f1(x0 + X)}}" y2="${{f1(y)}}" stroke="${{RED}}" stroke-width="2" marker-end="url(#a_C00000)"/>`;
    }}
    $('defLoad').innerHTML = lg + `<polyline points="${{tails.join(' ')}}" fill="none" stroke="${{RED}}" stroke-width="2"/>`;
    const ys = yT + D;
    $('defSup').innerHTML =
      `<polygon points="${{x0}},${{ys}} ${{x0 - 12}},${{ys + 20}} ${{x0 + 12}},${{ys + 20}}"/>` +
      `<polygon points="${{x0 + L}},${{ys}} ${{x0 + L - 12}},${{ys + 15}} ${{x0 + L + 12}},${{ys + 15}}"/>` +   // roller
      `<circle cx="${{x0 + L - 6}}" cy="${{ys + 18.5}}" r="3.5"/><circle cx="${{x0 + L + 6}}" cy="${{ys + 18.5}}" r="3.5"/>`;
    // allowable sag line at mid-span, under the unloaded ceiling
    const yl = yT + D + hang + ceil + lim;
    $('limLine').setAttribute('x1', x0 + L * 0.3); $('limLine').setAttribute('x2', x0 + L * 0.7);
    $('limLine').setAttribute('y1', yl); $('limLine').setAttribute('y2', yl);
    $('limTxt').setAttribute('x', x0 + L * 0.3 - 8); $('limTxt').setAttribute('text-anchor', 'end'); $('limTxt').setAttribute('y', yl + 5);
    const over = A * s2 > lim;
    let cr = '';
    if (over) {{
      const ym = yT + D + hang + A * s2;
      for (const xc of [0.4, 0.5, 0.6]) {{
        const x = x0 + L * xc;
        cr += `<polyline points="${{f1(x)}},${{f1(ym + ceil + 1)}} ${{f1(x - 3)}},${{f1(ym + 7)}} ${{f1(x + 3)}},${{f1(ym + 4)}} ${{f1(x)}},${{f1(ym - 1)}}"/>`;
      }}
    }}
    $('cracks').innerHTML = cr;
    $('crTxt').setAttribute('x', x0 + L * 0.5 - 52); $('crTxt').setAttribute('y', yT + D + hang + ceil + A * s2 + 28);
    $('crTxt').setAttribute('opacity', over ? 1 : 0);
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>"""

    css = lib.TEXT_CSS + "\n  .pts { font-size: 19px; }\n"
    pts = f"""  <ul class="pts" style="left:82px; top:600px; width:540px" data-step="1">
    <li>Long, slender beams can <b>buckle sideways</b> before the stress limit is reached. Brace them along their length.</li>
  </ul>
  <ul class="pts" style="left:672px; top:600px; width:540px" data-step="2">
    <li>Beams under brittle finishes (plaster) must <b>not sag too much</b>. Deflection: Chapter 16.</li>
  </ul>"""
    title = 'Strength is not the only <span class="key">limit</span>'
    body = svg + "\n" + js + "\n" + pts + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.1, p. 688. Schematic; '
        'buckling shape <math><mi>sin</mi><mo>(</mo><mi>π</mi><mi>x</mi><mo>/</mo><mi>L</mi><mo>)</mo></math> and sag from the elastic curve, both exaggerated.</div>')
    lib.write_page("05_slide5_limits.html", "Slide 8 - Other limits", title, body, 8, css)


if __name__ == "__main__":
    build()
