"""Slide 9 - Size the beam for bending first: S_req'd = M_max / sigma_allow (Sec. 15.2, p. 690).

Clicks:
  1  simply supported beam under a uniform load w, its moment diagram, M_max at midspan
  2  what S is: the section at M_max, I shaded by distance from the N.A., c, the linear
     bending stress, S = I/c and sigma_max = M/S
  3  Eq. (15-1) with its terms colour-coded to the figure
  4-6  step by step (was a loop): w grows, M_max grows with it, S_req'd = M_max/sigma_allow rises past
     the S of the section and sigma_max passes sigma_allow; then a taller section is chosen
     until S = S_req'd and sigma_max is back at sigma_allow
  5  beam weight; prismatic beam: one S, the M_max section governs

Everything is computed from the formulas, in relative units (no textbook numbers):
  M(x) = w x (L - x) / 2, M_max = w L^2 / 8, S = I/c = b h^2 / 6 for the rectangle,
  sigma_max = M_max / S, deflection from the uniform-load elastic curve (exaggerated).

Writes ../slides/separate/10_slide9_design.html.
Run:  python3 12_make_slide9_design.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S, SUP, SIG = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT, lib.SIG
sym = lib.sym
MC = "#c27c0e"            # M_max (moment diagram) colour, amber as Q on slide 3

# geometry (svg px)
BX0, BX1, BY = 60, 540, 78          # beam ends and top of the beam
MB, MH = 238, 92                    # moment diagram baseline and height at w = 1
SCX, SCY, SB, H0 = 140, 445, 66, 96 # section centre, width, starting depth
PX, PW = 300, 58                    # stress profile axis x and length for sigma_allow
G1X, G2X, GB, GU = 520, 650, 520, 100  # gauges: x, base y, px per unit


def build():
    sreq = "<msub><mi>S</mi><mtext>req’d</mtext></msub>"
    mmax = "<msub><mi>M</mi><mtext>max</mtext></msub>"
    sall = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
    smax = "<msub><mi>σ</mi><mtext>max</mtext></msub>"

    svg = f"""<svg class="fig" style="left:40px; top:108px" width="800" height="590" viewBox="0 0 800 590">
  <defs>{lib.markers(RED, NAVY, MC, GREY)}
    <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="8" stroke="{MC}" stroke-width="1.2" opacity="0.5"/></pattern>
    <linearGradient id="ishade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{NAVY}" stop-opacity="0.55"/><stop offset="0.5" stop-color="{NAVY}" stop-opacity="0"/>
      <stop offset="1" stop-color="{NAVY}" stop-opacity="0.55"/></linearGradient>
  </defs>
  <g data-step="1">
    <g id="load" stroke="{RED}" stroke-width="2"></g>
    <line id="wLine" stroke="{RED}" stroke-width="2"/>
    <text id="wLbl" font-size="20" fill="{RED}">{sym('w')}</text>
    <path id="beam" fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <polygon points="{BX0},{BY + 18} {BX0 - 11},{BY + 36} {BX0 + 11},{BY + 36}" fill="#fff" stroke="{SUP}" stroke-width="2"/>
    <polygon points="{BX1},{BY + 18} {BX1 - 11},{BY + 33} {BX1 + 11},{BY + 33}" fill="#fff" stroke="{SUP}" stroke-width="2"/>
    <circle cx="{BX1 - 5}" cy="{BY + 36}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>
    <circle cx="{BX1 + 5}" cy="{BY + 36}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>
    <line x1="{BX0}" y1="{MB}" x2="{BX1 + 30}" y2="{MB}" stroke="#000" stroke-width="1.3" marker-end="url(#a_555555)"/>
    <line x1="{BX0}" y1="{MB + 4}" x2="{BX0}" y2="{MB - MH - 18}" stroke="#000" stroke-width="1.3" marker-end="url(#a_555555)"/>
    <text x="{BX1 + 36}" y="{MB + 6}" font-size="18">{sym('x')}</text>
    <text x="{BX0 - 24}" y="{MB - MH - 10}" font-size="18">{sym('M')}</text>
    <path id="mDia" fill="url(#hatch)" stroke="{MC}" stroke-width="2.5"/>
    <circle id="mDot" r="5" fill="{MC}"/>
    <text id="mLbl" font-size="19" fill="{MC}" font-weight="bold" text-anchor="middle">{sym('M', 'max')}</text>
    <line x1="{(BX0 + BX1) / 2}" y1="{BY + 22}" x2="{(BX0 + BX1) / 2}" y2="{MB}" stroke="{GREY}" stroke-width="1" stroke-dasharray="4 4"/>
  </g>
  <g data-step="2">
    <path d="M{(BX0 + BX1) / 2},{MB + 4} C{(BX0 + BX1) / 2},{MB + 60} {SCX + 40},{SCY - 150} {SCX + 20},{SCY - 85}" fill="none" stroke="{GREY}" stroke-width="1.2" stroke-dasharray="4 4" marker-end="url(#a_555555)"/>
    <text x="{SCX + 40}" y="{SCY - 100}" font-size="15" fill="{GREY}" font-style="italic">section where M is largest</text>
    <rect id="sec" fill="{S['inner']}" stroke="{S['edge']}" stroke-width="2"/>
    <rect id="secI" fill="url(#ishade)"/>
    <line id="cFib" stroke="{GREY}" stroke-width="1.2" stroke-dasharray="3 3"/>
    <text x="{SCX - 85}" y="{SCY + 86}" font-size="14" font-style="italic"><tspan font-weight="bold" fill="{RED}">{sym('c')}</tspan>: N.A. to the farthest fibre, where σ is largest</text>
    <line id="na" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text id="naLbl" font-size="14" fill="{NAVY}">N.A.</text>
    <rect id="cHi" fill="{RED}" opacity="0"/>
    <line id="cDim" stroke="{RED}" stroke-width="1.8" marker-start="url(#a_C00000)" marker-end="url(#a_C00000)"/>
    <text id="cLbl" font-size="22" font-weight="bold" fill="{RED}" text-anchor="middle">{sym('c')}</text>
    <line id="pAx" stroke="#000" stroke-width="1.3"/>
    <polygon id="pTop" fill="{SIG}" fill-opacity="0.18" stroke="{SIG}" stroke-width="2"/>
    <polygon id="pBot" fill="{SIG}" fill-opacity="0.18" stroke="{SIG}" stroke-width="2"/>
    <line id="allL" stroke="{RED}" stroke-width="1.5" stroke-dasharray="5 4"/>
    <line id="allR" stroke="{RED}" stroke-width="1.5" stroke-dasharray="5 4"/>
    <text id="sTop" font-size="17" fill="{SIG}" text-anchor="end">−{sym('σ', 'max')} <tspan font-size="14">(compression)</tspan></text>
    <text id="sBot" font-size="17" fill="{SIG}">+{sym('σ', 'max')} <tspan font-size="14">(tension)</tspan></text>
  </g>
  <g data-step="4">
    <line x1="{G1X - 40}" y1="{GB}" x2="{G2X + 130}" y2="{GB}" stroke="#000" stroke-width="1.3"/>
    <rect id="g1" x="{G1X}" width="56" fill="{SIG}"/>
    <line x1="{G1X - 14}" y1="{GB - GU}" x2="{G1X + 70}" y2="{GB - GU}" stroke="{RED}" stroke-width="2.5" stroke-dasharray="7 4"/>
    <text x="{G1X - 18}" y="{GB - GU + 6}" font-size="18" fill="{RED}" text-anchor="end">{sym('σ', 'allow')}</text>
    <text x="{G1X + 28}" y="{GB + 24}" font-size="18" fill="{SIG}" text-anchor="middle">{sym('σ', 'max')}</text>
    <rect id="g2" x="{G2X}" width="56" fill="{S['inner']}" stroke="{S['edge']}" stroke-width="1.5"/>
    <line id="g2r" x1="{G2X - 14}" x2="{G2X + 70}" stroke="{NAVY}" stroke-width="3"/>
    <text id="g2rL" x="{G2X + 76}" font-size="18" fill="{NAVY}" font-weight="bold">{sym('S', 'req’d')}</text>
    <text x="{G2X + 28}" y="{GB + 24}" font-size="18" text-anchor="middle">{sym('S')} of section</text>
    <g data-step="5"></g><g data-step="6"></g>
    <text id="stat" x="{(G1X + G2X) / 2 + 28}" y="{GB - 1.5 * GU - 14:.0f}" font-size="18" font-weight="bold" text-anchor="middle"></text>
  </g>
</svg>"""

    js = """<script>
""" + lib.ELASTIC_JS + """
(() => {
  const BX0 = %BX0%, BX1 = %BX1%, BY = %BY%, MB = %MB%, MH = %MH%, SCX = %SCX%, SCY = %SCY%,
        SB = %SB%, H0 = %H0%, PX = %PX%, PW = %PW%, G1X = %G1X%, G2X = %G2X%, GB = %GB%, GU = %GU%;
  const RED = "%RED%", SIG = "%SIG%", NAVY = "%NAVY%";
  const $ = id => document.getElementById(id);
  const set = (id, a) => { const e = $(id); for (const k in a) e.setAttribute(k, a[k]); };
  const f1 = v => v.toFixed(1);
  const c5 = revealClock(5), c6 = revealClock(6), c2 = revealClock(2);
  const W0 = 0.5, W1 = 1.0, RATIO1 = 1.5;   // sigma_max / sigma_allow with the first section at w = 1
  // step by step (one click each): 4 gauges at the design load, 5 load doubles -> too small,
  // 6 deeper section until S = S_req'd. K = click count from the deck (single file: final state).
  let K = 99;
  addEventListener('buildstep', ev => { K = ev.detail.k; });

  function state() {
    const w = K >= 5 ? W0 + (W1 - W0) * smooth(c5() / 1.5) : W0;
    const g = K >= 6 ? smooth(c6() / 1.5) : 0;      // 0 = first section, 1 = section with S = S_req'd
    const h = H0 * (1 + (Math.sqrt(RATIO1) - 1) * g);
    return {w, h, g};
  }

  function draw() {
    const {w, h, g} = state();
    const S = (h / H0) ** 2;                  // S / S_first   (S = b h^2 / 6)
    const I = (h / H0) ** 3;                  // I / I_first
    const sreq = RATIO1 * w;                  // S_req'd / S_first = M_max / sigma_allow
    const ratio = sreq / S;                   // sigma_max / sigma_allow = M_max / (S sigma_allow)

    // beam, deflected (uniform-load elastic curve, exaggerated, stiffer with I)
    const L = BX1 - BX0, n = 48, d0 = 14 * w / I, top = [], bot = [];
    for (let i = 0; i <= n; i++) {
      const xi = i / n, d = d0 * 3.2 * (xi - 2 * xi ** 3 + xi ** 4), x = BX0 + L * xi;
      top.push([x, BY + d]); bot.unshift([x, BY + 18 + d]);
    }
    set('beam', {d: 'M' + top.concat(bot).map(p => f1(p[0]) + ',' + f1(p[1])).join(' L') + 'Z'});
    // uniform load arrows, length grows with w
    const al = 14 + 34 * w; let la = '';
    for (let i = 0; i <= 12; i++) {
      const xi = i / 12, x = BX0 + L * xi, yb = BY - 3 + d0 * 3.2 * (xi - 2 * xi ** 3 + xi ** 4);
      la += `<line x1="${f1(x)}" y1="${f1(yb - al)}" x2="${f1(x)}" y2="${f1(yb)}" marker-end="url(#a_C00000)"/>`;
    }
    $('load').innerHTML = la;
    set('wLine', {x1: BX0, x2: BX1, y1: f1(BY - 3 - al), y2: f1(BY - 3 - al)});
    set('wLbl', {x: BX1 + 14, y: f1(BY - al + 4)});

    // moment diagram M = w x (L - x) / 2, peak w L^2 / 8 at midspan
    let md = `M${BX0},${MB}`;
    for (let i = 0; i <= n; i++) { const xi = i / n; md += ` L${f1(BX0 + L * xi)},${f1(MB - MH * w * 4 * xi * (1 - xi))}`; }
    set('mDia', {d: md + ' Z'});
    const pk = MB - MH * w;
    set('mDot', {cx: (BX0 + BX1) / 2, cy: f1(pk)});
    set('mLbl', {x: (BX0 + BX1) / 2 + 52, y: f1(pk - 6)});

    // section b x h at M_max
    set('sec', {x: SCX - SB / 2, y: f1(SCY - h / 2), width: SB, height: f1(h)});
    set('secI', {x: SCX - SB / 2 + 1, y: f1(SCY - h / 2 + 1), width: SB - 2, height: f1(h - 2)});
    set('na', {x1: SCX - SB / 2 - 14, x2: PX + PW + 30, y1: SCY, y2: SCY});
    set('naLbl', {x: PX + PW + 34, y: SCY + 5});
    set('cDim', {x1: SCX - SB / 2 - 20, x2: SCX - SB / 2 - 20, y1: SCY - 2, y2: f1(SCY - h / 2 + 2)});
    set('cFib', {x1: SCX + SB / 2 + 4, x2: f1(PX - PW * ratio), y1: f1(SCY - h / 2), y2: f1(SCY - h / 2)});
    // c: pulses (jumps) for 3 s after click 2, then stays red
    const t2 = c2(), p = t2 < 3 ? Math.abs(Math.sin(Math.PI * t2 * 1.5)) * (1 - t2 / 3) : 0;
    const cx = SCX - SB / 2 - 20;
    set('cLbl', {x: cx - 22, y: f1(SCY - h / 4 + 8 - 10 * p), 'font-size': f1(22 * (1 + 0.6 * p))});
    set('cHi', {x: SCX - SB / 2 - 32, y: f1(SCY - h / 2), width: 30, height: f1(h / 2), opacity: f1(0.1 + 0.3 * p)});
    // linear bending stress: compression on top (to the left), tension below (to the right)
    const sl = PW * ratio, yt = SCY - h / 2, yb = SCY + h / 2;
    set('pAx', {x1: PX, x2: PX, y1: f1(yt - 10), y2: f1(yb + 10)});
    set('pTop', {points: `${PX},${SCY} ${PX},${f1(yt)} ${f1(PX - sl)},${f1(yt)}`});
    set('pBot', {points: `${PX},${SCY} ${PX},${f1(yb)} ${f1(PX + sl)},${f1(yb)}`});
    const over = ratio > 1.005;
    for (const id of ['pTop', 'pBot']) set(id, {stroke: over ? RED : SIG, fill: over ? RED : SIG});
    set('allL', {x1: PX - PW, x2: PX - PW, y1: f1(yt - 16), y2: SCY});
    set('allR', {x1: PX + PW, x2: PX + PW, y1: SCY, y2: f1(yb + 16)});
    set('sTop', {x: f1(PX - sl + 30), y: f1(yt - 12)});
    set('sBot', {x: f1(PX + sl + 6), y: f1(yb + 18)});

    // gauges
    set('g1', {y: f1(GB - GU * ratio), height: f1(GU * ratio), fill: over ? RED : SIG});
    set('g2', {y: f1(GB - GU * S / RATIO1), height: f1(GU * S / RATIO1)});
    const yr = GB - GU * sreq / RATIO1;
    set('g2r', {y1: f1(yr), y2: f1(yr)});
    set('g2rL', {y: f1(yr + 6)});
    const sb = (b, x) => `<tspan class="sym">${b}</tspan><tspan baseline-shift="sub" font-size="70%">${x}</tspan>`;
    let msg = '', col = '#000';
    if (K <= 4) { msg = `${sb('S', '')} &gt; ${sb('S', 'req’d')}  so  ${sb('σ', 'max')} &lt; ${sb('σ', 'allow')}: OK`; col = '#1f7a5a'; }
    else if (K === 5) { msg = over ? `load doubled: ${sb('σ', 'max')} &gt; ${sb('σ', 'allow')}, too small` : 'load grows …'; col = over ? RED : '#000'; }
    else if (g < 0.999) { msg = 'deeper section …'; col = NAVY; }
    else { msg = `${sb('S', '')} = ${sb('S', 'req’d')}  so  ${sb('σ', 'max')} = ${sb('σ', 'allow')}`; col = NAVY; }
    set('stat', {fill: col}); $('stat').innerHTML = msg;
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>"""
    vals = dict(BX0=BX0, BX1=BX1, BY=BY, MB=MB, MH=MH, SCX=SCX, SCY=SCY, SB=SB, H0=H0, PX=PX, PW=PW,
                G1X=G1X, G2X=G2X, GB=GB, GU=GU, RED=RED, SIG=SIG, NAVY=NAVY)
    for k, v in vals.items():
        js = js.replace(f"%{k}%", str(v))

    css = lib.TEXT_CSS + f"""
  .pts {{ font-size: 18px; }}
  .pts li {{ margin-bottom: 6px; }}
  .box {{ position: absolute; left: 862px; top: 262px; width: 360px; padding: 8px 14px 10px; font-size: 17px;
         border: 2px solid {RED}; border-radius: 6px; background: #fbecec; line-height: 1.35; }}
  .box math[display="block"] {{ font-size: 34px; margin: 4px 0 8px; }}
  .eqn {{ position: absolute; right: 14px; top: 34px; font-size: 17px; }}
"""
    smod = ("<math><mi>S</mi><mo>=</mo><mi>I</mi><mo>/</mo><mi>c</mi></math>")
    sflex = (f"<math>{smax}<mo>=</mo><mi>M</mi><mi>c</mi><mo>/</mo><mi>I</mi><mo>=</mo>"
             f"<mi>M</mi><mo>/</mo><mi>S</mi></math>")
    eq = (f'<math display="block"><mstyle mathcolor="{NAVY}">{sreq}</mstyle><mo>=</mo>'
          f'<mfrac><mstyle mathcolor="{MC}">{mmax}</mstyle><mstyle mathcolor="{RED}">{sall}</mstyle></mfrac></math>')
    pts = f"""  <ul class="pts" style="left:862px; top:116px; width:370px">
    <li data-step="1">Most beams are long and ductile: <span class="em">design for bending</span> first, then check shear.</li>
    <li data-step="2"><b>Section modulus</b> {smod}, so {sflex}</li>
  </ul>
  <div class="box" data-step="3"><span class="eqn">(15–1)</span>{eq}
    <span style="color:{MC}"><b><math>{mmax}</math></b>: from the moment diagram</span><br>
    <span style="color:{RED}"><b><math>{sall}</math></b>: from a design code</span><br>
    <span style="color:{NAVY}"><b><math>{sreq}</math></b>: the smallest <i>S</i> the section may have</span></div>
  <ul class="pts" style="left:862px; top:452px; width:370px">
    <li data-step="6">Pick a section with <math><mi>S</mi><mo>≥</mo>{sreq}</math>.</li>
    <li data-step="7">Beam weight: pick <i>S</i> slightly above <math>{sreq}</math>.</li>
    <li data-step="7"><b>Prismatic</b> beam: same cross section along its length, so the section at <math>{mmax}</math> governs.</li>
  </ul>"""
    title = 'Design the beam for <span class="key">bending</span> first'
    body = svg + "\n" + js + "\n" + pts + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.2, Eq. (15–1), p. 690. '
        'Beam, load and sizes illustrative (relative units); deflection exaggerated.</div>')
    lib.write_page("10_slide9_design.html", "Slide 9 - S required", title, body, 9, css)


if __name__ == "__main__":
    build()
