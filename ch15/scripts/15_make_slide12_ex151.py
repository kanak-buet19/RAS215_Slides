"""Slide 12 - Example 15.1: choose the lightest W-shape (Hibbeler 6th ed., Ex. 15.1, p. 694, Fig. 15-7).

Book data (checked against the photo of p. 694):
  beam: pin A at x = 0, roller B at x = 12 ft, 40 kip at x = 6 ft, 20 kip at the free end x = 18 ft
  sigma_allow = 24 ksi, tau_allow = 14.5 ksi
  reactions A = 10 kip, B = 50 kip (sum M_A: 12 B = 40(6) + 20(18) -> B = 50)
  V: +10 (0-6), -30 (6-12), +20 (12-18);  M: 60 at 6 ft, 0 at 8 ft, -120 at B, 0 at the end
  V_max = 30 kip, M_max = 120 kip.ft
  S_req'd = 120(12)/24 = 60 in^3; adequate: W18x40 68.4, W16x45 72.7, W14x43 62.7, W12x50 64.7, W8x67 60.4
  lightest: W18x40, d = 17.90 in, t_w = 0.315 in; tau_avg = 30/(17.90 x 0.315) = 5.32 ksi < 14.5 OK
Clicks: 1 problem, 2 reactions + V and M diagrams (drawn left to right once), 3 bending + table (lightest
lights up), 4 shear check (web of W18x40 shaded), 5 answer.

Writes ../slides/separate/13_slide12_ex151.html.
Run:  python3 15_make_slide12_ex151.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, ST, SUP, TAU = lib.NAVY, lib.RED, lib.GREY, lib.STEEL, lib.SUPPORT, lib.TAU
sym = lib.sym
MC = "#c27c0e"

X0, PF = 70, 24                 # x of A (svg px), px per ft
BY = 70                         # beam top
VB, VS = 232, 1.6               # V baseline, px per kip
MB, MS = 368, 0.6               # M baseline, px per kip.ft
X = lambda ft: X0 + PF * ft

# book data
CANDS = [("W18 × 40", 68.4, 40), ("W16 × 45", 72.7, 45), ("W14 × 43", 62.7, 43),
         ("W12 × 50", 64.7, 50), ("W8 × 67", 60.4, 67)]
SREQ_V = 120 * 12 / 24
TAVG = 30 / (17.90 * 0.315)


def M_at(x):
    return 10 * x - 40 * max(0, x - 6) + 50 * max(0, x - 12)


def svg():
    s = f'<defs>{lib.markers(RED, NAVY, GREY)}<clipPath id="clipD"><rect id="cr" x="0" y="{VB - 80}" width="0" height="400"/></clipPath></defs>'
    # click 1: beam, supports, loads, dimensions
    s += '<g data-step="1">'
    s += lib.wbeam_elev(X(0), BY, PF * 18, 26)
    s += lib.wbeam_end_view(X(18), X(18) + 70, BY, 26, 'end view', 'W-shape: ?')
    s += f'<polygon points="{X(0)},{BY + 26} {X(0) - 10},{BY + 42} {X(0) + 10},{BY + 42}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
    s += f'<polygon points="{X(12)},{BY + 26} {X(12) - 10},{BY + 39} {X(12) + 10},{BY + 39}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
    s += f'<circle cx="{X(12) - 5}" cy="{BY + 42}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/><circle cx="{X(12) + 5}" cy="{BY + 42}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'
    for ft, P in ((6, 40), (18, 20)):
        s += f'<line x1="{X(ft)}" y1="{BY - 44}" x2="{X(ft)}" y2="{BY - 3}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>'
        s += f'<text x="{X(ft)}" y="{BY - 50}" font-size="17" fill="{RED}" text-anchor="middle" font-weight="bold">{P} kip</text>'
    s += f'<text x="{X(0) - 6}" y="{BY - 8}" font-size="17" text-anchor="end" font-style="italic">A</text>'
    s += f'<text x="{X(12) + 14}" y="{BY - 6}" font-size="17" font-style="italic">B</text>'
    for a in (0, 6, 12):
        s += f'<line x1="{X(a) + 2}" y1="{BY + 58}" x2="{X(a + 6) - 2}" y2="{BY + 58}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X(a + 3)}" y="{BY + 74}" font-size="14" fill="{GREY}" text-anchor="middle">6 ft</text>'
    s += '</g>'
    # click 2: reactions, V and M diagrams
    s += '<g data-step="2">'
    for ft, R in ((0, 10), (12, 50)):
        s += f'<line x1="{X(ft)}" y1="{BY + 112}" x2="{X(ft)}" y2="{BY + 48}" stroke="{NAVY}" stroke-width="3" marker-end="url(#a_002060)"/>'
        s += f'<text x="{X(ft) + 8}" y="{BY + 108}" font-size="16" fill="{NAVY}" font-weight="bold">{R} kip</text>'
    vp = [(0, 10), (6, 10), (6, -30), (12, -30), (12, 20), (18, 20)]
    vpts = " ".join(f"{X(x):.1f},{VB - VS * v:.1f}" for x, v in vp)
    mpts = " ".join(f"{X(i / 4):.1f},{MB - MS * M_at(i / 4):.1f}" for i in range(73))
    s += f'<g clip-path="url(#clipD)">'
    s += f'<polygon points="{X(0)},{VB} {vpts} {X(18)},{VB}" fill="{TAU}" fill-opacity="0.15" stroke="{TAU}" stroke-width="2.2"/>'
    s += f'<polygon points="{X(0)},{MB} {mpts} {X(18)},{MB}" fill="{MC}" fill-opacity="0.15" stroke="{MC}" stroke-width="2.2"/></g>'
    for y, lab, unit in ((VB, "V", "kip"), (MB, "M", "kip·ft")):
        s += f'<line x1="{X(0)}" y1="{y}" x2="{X(18) + 22}" y2="{y}" stroke="#000" stroke-width="1.2" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X(0) - 10}" y="{y + 5}" font-size="16" text-anchor="end">{sym(lab)} ({unit})</text>'
        s += f'<text x="{X(18) + 26}" y="{y + 5}" font-size="15">{sym("x")} (ft)</text>'
    s += '<g id="vals" opacity="0" font-size="15">'
    s += f'<text x="{X(3)}" y="{VB - VS * 10 - 6}" fill="{TAU}" text-anchor="middle">10</text>'
    s += f'<text x="{X(15)}" y="{VB - VS * 20 - 6}" fill="{TAU}" text-anchor="middle">20</text>'
    s += f'<text x="{X(6)}" y="{MB - MS * 60 - 8}" fill="{MC}" text-anchor="middle">60</text>'
    s += f'<text x="{X(8)}" y="{MB + 18}" fill="{GREY}" text-anchor="middle" font-size="13">8 ft</text>'
    # the governing values
    s += f'<text x="{X(9)}" y="{VB - VS * -30 + 20}" fill="{RED}" text-anchor="middle" font-weight="bold">−30 → {sym("V", "max")} = 30 kip</text>'
    s += f'<circle cx="{X(12)}" cy="{MB - MS * -120}" r="5" fill="{RED}"/>'
    s += f'<text x="{X(12) + 10}" y="{MB - MS * -120 + 6}" fill="{RED}" font-weight="bold">−120 → {sym("M", "max")} = 120 kip·ft</text>'
    s += '</g></g>'
    return f'<svg class="fig" style="left:40px; top:96px" width="620" height="520" viewBox="0 0 620 520">{s}</svg>'


def decoder():
    """What 'W18 x 40' means (p. 691: a W18 x 46 is a wide-flange section 18 in. deep weighing 46 lb/ft),
    with a W18 x 40 section: d = 17.90 in., t_w = 0.315 in. (Ex. 15.1). Flange width and thickness are drawn
    to rough proportion only (not given in the photographed pages)."""
    C1, C2, C3 = NAVY, RED, "#1f7a5a"
    s = (f'<text x="0" y="30" font-size="30" font-weight="bold"><tspan fill="{C1}">W</tspan><tspan fill="{C2}">18</tspan>'
         f'<tspan fill="#333"> × </tspan><tspan fill="{C3}">40</tspan></text>')
    rows = [(C1, "W", "wide-flange shape"), (C2, "18", f"about 18 in. deep (actual {sym('d')} = 17.90 in.)"),
            (C3, "40", "weighs 40 lb per foot")]
    for n, (c, k, t) in enumerate(rows):
        y = 60 + n * 22
        s += (f'<text x="0" y="{y}" font-size="17" font-weight="bold" fill="{c}">{k}</text>'
              f'<text x="34" y="{y}" font-size="16" fill="{c}">{t}</text>')
    # section, 4.3 px/in (d = 17.90 in.; flange approx. 6 in. x 0.5 in.)
    k, cx, top = 5.6, 470, 14
    d, bf, tf, tw = 17.90 * k, 6.0 * k, 0.53 * k, 0.315 * k
    H = d / 2
    cy = top + H
    pts = [(-bf / 2, -H), (bf / 2, -H), (bf / 2, -H + tf), (tw / 2, -H + tf), (tw / 2, H - tf), (bf / 2, H - tf), (bf / 2, H),
           (-bf / 2, H), (-bf / 2, H - tf), (-tw / 2, H - tf), (-tw / 2, -H + tf), (-bf / 2, -H + tf)]
    s += '<path d="M' + " L".join(f"{cx + a:.1f},{cy + b:.1f}" for a, b in pts) + f' Z" fill="#b4bac2" stroke="{ST["edge"]}" stroke-width="1.3"/>'
    s += (f'<line x1="{cx - bf / 2 - 12:.1f}" y1="{top + 1}" x2="{cx - bf / 2 - 12:.1f}" y2="{top + d - 1:.1f}" stroke="{C2}" stroke-width="1.3" '
          f'marker-start="url(#a_C00000)" marker-end="url(#a_C00000)"/>'
          f'<text x="{cx - bf / 2 - 18:.1f}" y="{cy + 5:.1f}" font-size="14" fill="{C2}" text-anchor="end">{sym("d")} = 17.90 in.</text>'
          f'<line x1="{cx + 2}" y1="{cy + 8:.1f}" x2="{cx + 22}" y2="{cy + 18:.1f}" stroke="#333" stroke-width="1"/>'
          f'<text x="{cx + 24}" y="{cy + 23:.1f}" font-size="14">{sym("t", "w")} = 0.315 in.</text>'
          f'<text x="{cx + 24}" y="{cy - 14:.1f}" font-size="13" fill="{GREY}">W18 × 40</text>')
    return (f'<svg class="fig" data-step="3" style="left:48px; top:566px" width="620" height="128" viewBox="0 0 620 128">'
            f'<defs>{lib.markers(RED)}</defs>{s}</svg>')


def m(x):
    return f"<math>{x}</math>"


def ds(x):
    return f'<math><mstyle displaystyle="true">{x}</mstyle></math>'


def build():
    SREQ = "<msub><mi>S</mi><mtext>req’d</mtext></msub>"
    MMAX = "<msub><mi>M</mi><mtext>max</mtext></msub>"
    VMAX = "<msub><mi>V</mi><mtext>max</mtext></msub>"
    SALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
    TALL = "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
    TAV = "<msub><mi>τ</mi><mtext>avg</mtext></msub>"
    rows = "".join(f'<tr class="{"best" if i == 0 else ""}"><td>{n}</td><td>{S}</td><td>{w}</td></tr>'
                   for i, (n, S, w) in enumerate(CANDS))
    u = lambda t: f"<mspace width='0.22em'/><mtext>{t}</mtext>"
    right = f"""
  <div class="given" data-step="1"><div class="gh">Problem</div>
    A steel beam carries the loads shown (Fig. 15-7). Allowable stresses:
    <div class="gv">{m(SALL + '<mo>=</mo><mn>24</mn>' + u('ksi'))}<span class="sep"></span>{m(TALL + '<mo>=</mo><mn>14.5</mn>' + u('ksi'))}</div>
    <div class="gf"><b>Find:</b> the lightest W-shape that works</div></div>
  <div class="step" data-step="2" style="top:226px"><span class="no">1</span><b>Diagrams</b> (slide 12):&nbsp; {m(VMAX + '<mo>=</mo><mn>30</mn>' + u('kip'))},&nbsp; {m(MMAX + '<mo>=</mo><mn>120</mn>' + u('kip·ft'))}
    <div class="cap2">use the size; the sign only says which side is in tension</div></div>
  <div class="step" data-step="3" style="top:300px"><span class="no">2</span><b>Bending</b>
    <div class="row"><span class="tag calc">Compute</span>{ds(SREQ + '<mo>=</mo><mfrac>' + MMAX + SALL + '</mfrac><mo>=</mo><mfrac><mrow><mn>120</mn>' + u('kip·ft') + '<mo>(</mo><mn>12</mn>' + u('in./ft') + '<mo>)</mo></mrow><mrow><mn>24</mn>' + u('kip/in.²') + '</mrow></mfrac><mo>=</mo><mn>60</mn>' + u('in.³'))}</div>
    <div class="row"><span class="tag req">Check</span>
      <table class="tb"><tr><th>shape</th><th><i>S</i> (in.³)</th><th>lb/ft</th></tr>{rows}</table>
      <div class="pick" id="pick">all have <i>S</i> ≥ 60 in.³<br><b style="color:{RED}">W18 × 40 is the lightest</b></div></div></div>
  <div class="step" data-step="4" style="top:516px"><span class="no">3</span><b>Shear</b> (W-shape: the web carries it)
    <div class="cap2">W18 × 40 (Appendix C): depth <i>d</i> = 17.90 in., web thickness <i>t</i><sub>w</sub> = 0.315 in.</div>
    <div class="row"><span class="tag calc">Compute</span>{ds(TAV + '<mo>=</mo><mfrac>' + VMAX + '<mrow><mi>d</mi><msub><mi>t</mi><mi>w</mi></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>30</mn>' + u('kip') + '</mrow><mrow><mo>(</mo><mn>17.90</mn>' + u('in.') + '<mo>)</mo><mo>(</mo><mn>0.315</mn>' + u('in.') + '<mo>)</mo></mrow></mfrac><mo>=</mo><mn>{TAVG:.2f}</mn>'.replace('{TAVG:.2f}', f'{TAVG:.2f}') + u('ksi'))}</div>
    <div class="row"><span class="tag req">Check</span>{ds('<mn>5.32</mn>' + u('ksi') + '<mo>≤</mo><mn>14.5</mn>' + u('ksi'))}<span class="ok">OK</span></div></div>
  <div class="ans" data-step="5">Use a <b>W18 × 40</b></div>"""

    js = "<script>\n" + lib.ELASTIC_JS + """
(() => {
  const $ = id => document.getElementById(id);
  const clamp = v => Math.min(1, Math.max(0, v));
  const c2 = revealClock(2), c3 = revealClock(3);
  function draw() {
    $('cr').setAttribute('width', (620 * smooth(clamp((c2() - 0.3) / 1.6))).toFixed(1));
    $('vals').setAttribute('opacity', clamp((c2() - 2.0) / 0.4));
    const p = clamp((c3() - 1.2) / 0.4);
    document.querySelector('tr.best').style.background = `rgba(192,0,0,${(0.13 * p).toFixed(3)})`;
    document.querySelector('tr.best').style.fontWeight = p > 0.5 ? 'bold' : 'normal';
    $('pick').style.opacity = p;
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>"""

    css = lib.TEXT_CSS + f"""
  .given {{ position: absolute; left: 672px; top: 104px; width: 540px; padding: 6px 14px 8px; font-size: 17px; line-height: 1.4;
            border: 2px solid {NAVY}; border-left-width: 7px; border-radius: 6px; }}
  .gh {{ font-size: 14px; font-weight: bold; color: {NAVY}; text-transform: uppercase; letter-spacing: 1px; }}
  .gv {{ margin: 2px 0; }}
  .gv math {{ font-size: 22px; font-weight: bold; }}
  .sep {{ display: inline-block; width: 36px; }}
  .gf {{ color: {RED}; font-size: 18px; }}
  .step {{ position: absolute; left: 680px; width: 560px; font-size: 18px; }}
  .step math {{ font-size: 20px; }}
  .no {{ display: inline-block; min-width: 22px; margin-right: 4px; color: {NAVY}; font-weight: bold; }}
  .no::after {{ content: "."; }}
  .row {{ display: flex; align-items: center; margin-top: 6px; }}
  .tag {{ width: 82px; flex: none; font-size: 13px; font-weight: bold; text-transform: uppercase; }}
  .tag.calc {{ color: {NAVY}; }}
  .tag.req {{ color: {RED}; }}
  .cap2 {{ font-size: 14px; color: {GREY}; margin: 2px 0 0 34px; }}
  .tb {{ border-collapse: collapse; font-size: 16px; }}
  .tb th {{ font-weight: normal; color: {GREY}; border-bottom: 1px solid #999; padding: 1px 12px; }}
  .tb td {{ padding: 1px 12px; text-align: center; }}
  .pick {{ margin-left: 18px; font-size: 16px; line-height: 1.4; opacity: 0; }}
  .ok {{ color: {TAU}; font-weight: bold; margin-left: 12px; font-size: 19px; }}
  .ans {{ position: absolute; left: 880px; top: 668px; padding: 4px 18px; font-size: 20px; color: {RED};
         border: 2px solid {RED}; border-radius: 6px; }}
"""
    title = 'Example 15.1 (2/2): pick the <span class="key">lightest</span> W-shape'
    body = svg() + "\n" + decoder() + "\n" + right + "\n" + js + (
        f'\n  <div class="note">{lib.SOURCE}, Ex. 15.1, p. 694, Fig. 15-7; W designation, p. 691. W18 × 40 drawn to approximate proportion.</div>')
    lib.write_page("13_slide12_ex151.html", "Slide 12 - Example 15.1", title, body, 13, css)
    print(f"S_req = {SREQ_V:.1f} in^3, tau_avg = {TAVG:.3f} ksi, M(6) = {M_at(6)}, M(12) = {M_at(12)}, M(18) = {M_at(18)}")


if __name__ == "__main__":
    build()
