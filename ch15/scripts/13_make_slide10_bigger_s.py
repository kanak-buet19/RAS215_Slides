"""Slide 10 - Three ways to get a bigger S (follows slide 9, Sec. 15.2, p. 690-691).

Kept deliberately simple (user: the busier version was hard to follow). On each click the right-hand
section grows/reshapes out of the left one (2.2 s, no loop), S and weight count up live, then the
take-away fades in. Three panels, each one
before -> after pair of sections drawn to scale, one S value under each and one take-away line.
  1  deeper: b x h -> b x 2h, S 1x -> 4x, weight 2x   (rectangle S = b h^2 / 6)
  2  material away from the N.A.: 1 x 4 rectangle -> I-shape of the same area and depth,
     S 1x -> 2x, same weight   (I = bf d^3/12 - (bf - tw)(d - 2 tf)^3/12, S = I/(d/2): 1.98x)
  3  just add material: section scaled by 2^(1/3) = 1.26, S 1x -> 2x, weight 1.59x
  4  conclusion: deep, with material far from the N.A. -> W-shapes

Sections and ratios are illustrative, computed here from S = I/c; they are not textbook data.
Writes ../slides/separate/11_slide10_bigger_s.html.
Run:  python3 13_make_slide10_bigger_s.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, ST = lib.NAVY, lib.RED, lib.GREY, lib.STEEL
sym = lib.sym

U = 36                                    # px per unit
B2, D2, TF2, TW2 = 1.0, 4.0, 0.5, 0.25    # panel 2: rectangle 1 x 4 -> I-shape, same area and depth
BF2 = (B2 * D2 - TW2 * (D2 - 2 * TF2)) / (2 * TF2)
I_F = BF2 * D2 ** 3 / 12 - (BF2 - TW2) * (D2 - 2 * TF2) ** 3 / 12
S2 = (I_F / (D2 / 2)) / (B2 * D2 ** 2 / 6)
K3 = 2 ** (1 / 3)
SY = 200                                  # shape centre (svg y)


def rect(cx, w, h):
    return (f'<rect x="{cx - w / 2:.1f}" y="{SY - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'fill="{ST["inner"]}" stroke="{ST["edge"]}" stroke-width="2"/>')


def arrow(x0, x1):
    return f'<line x1="{x0}" y1="{SY}" x2="{x1}" y2="{SY}" stroke="{GREY}" stroke-width="2.5" marker-end="url(#a_555555)"/>'


def slabel(cx, txt, sid=None):
    if sid:
        return (f'<text x="{cx}" y="{SY + 115}" font-size="20" text-anchor="middle" font-weight="bold" fill="#C00000">'
                f'{sym("S")} = <tspan id="{sid}">{txt}</tspan></text>')
    return f'<text x="{cx}" y="{SY + 115}" font-size="20" text-anchor="middle">{sym("S")} = {txt}</text>'


def wlabel(cx, txt, wid=None):
    t = f'<tspan id="{wid}">{txt}</tspan>' if wid else txt
    return f'<text x="{cx}" y="{SY + 140}" font-size="17" text-anchor="middle" fill="{GREY}">weight = {t}</text>'


def panel(step, cx, head, left, sr, take, wr, sub):
    """Left: the start section (static). Right: the same section, reshaped by JS after the click."""
    return (f'<g data-step="{step}"><text x="{cx}" y="30" font-size="22" font-weight="bold" fill="{NAVY}" text-anchor="middle">{head}</text>'
            f'<text x="{cx}" y="58" font-size="17" fill="{GREY}" font-style="italic" text-anchor="middle">{sub}</text>'
            f'{left(cx - 95)}{arrow(cx - 40, cx + 30)}'
            f'<path id="r{step}" fill="{ST["inner"]}" stroke="{ST["edge"]}" stroke-width="2"/>'
            f'{slabel(cx - 95, "1×")}{slabel(cx + 100, "1×", f"s{step}")}{wlabel(cx - 95, "1×")}{wlabel(cx + 100, "1×", f"w{step}")}'
            f'<text id="t{step}" x="{cx}" y="{SY + 185}" font-size="20" text-anchor="middle" fill="{RED}" font-weight="bold" opacity="0">{take}</text></g>')


def build():
    b, h = 44, 72
    g1 = panel(1, 200, "1. Make it deeper", lambda x: rect(x, b, h),
               "4×", "4× the S for 2× the weight", "2×", "same width, depth × 2")
    g2 = panel(2, 600, "2. Move material away from the N.A.", lambda x: rect(x, B2 * U, D2 * U),
               f"{S2:.0f}×", "2× the S, same weight", "1×", "same area and depth, reshaped")
    g3 = panel(3, 1000, "3. Just add material", lambda x: rect(x, b, h),
               "2×", f"2× the S for {K3 ** 2:.1f}× the weight", f"{K3 ** 2:.1f}×", "same shape, width and depth × 1.26")
    finals = {1: ("4×", "2×"), 2: (f"{S2:.0f}×", "1×"), 3: ("2×", f"{K3 ** 2:.1f}×")}

    svg = f"""<svg class="fig" style="left:40px; top:120px" width="1200" height="420" viewBox="0 0 1200 420">
  <defs>{lib.markers(GREY)}</defs>
  {g1}
  <g data-step="2"><line x1="400" y1="8" x2="400" y2="{SY + 195}" stroke="#b5b5b5" stroke-width="1.4" stroke-dasharray="6 5"/></g>
  {g2}
  <g data-step="3"><line x1="800" y1="8" x2="800" y2="{SY + 195}" stroke="#b5b5b5" stroke-width="1.4" stroke-dasharray="6 5"/></g>
  {g3}
</svg>"""

    js = "<script>\n" + lib.ELASTIC_JS + """
(() => {
  const SY = %SY%, U = %U%, b = %b%, h = %h%, B2 = %B2%, D2 = %D2%, TF2 = %TF2%, TW2 = %TW2%, K3 = %K3%;
  const FIN = %FIN%;
  const $ = id => document.getElementById(id);
  const f1 = v => v.toFixed(1);
  // I-section path (a rectangle when tw = bf), centred at (cx, SY); all sizes in px
  const ipath = (cx, bf, tw, D, tf) => {
    const H = D / 2, w = H - tf, X = v => f1(cx + v), Y = v => f1(SY + v);
    return `M${X(-bf/2)},${Y(-H)} L${X(bf/2)},${Y(-H)} L${X(bf/2)},${Y(-w)} L${X(tw/2)},${Y(-w)} L${X(tw/2)},${Y(w)} ` +
           `L${X(bf/2)},${Y(w)} L${X(bf/2)},${Y(H)} L${X(-bf/2)},${Y(H)} L${X(-bf/2)},${Y(w)} L${X(-tw/2)},${Y(w)} ` +
           `L${X(-tw/2)},${Y(-w)} L${X(-bf/2)},${Y(-w)} Z`;
  };
  const shape = {
    1: g => { const D = h * (1 + g); return {d: ipath(300, b, b, D, D / 4), S: (1 + g) ** 2, W: 1 + g}; },
    2: g => { const tw = B2 + (TW2 - B2) * g, bf = (B2 * D2 - tw * (D2 - 2 * TF2)) / (2 * TF2);
              const I = bf * D2 ** 3 / 12 - (bf - tw) * (D2 - 2 * TF2) ** 3 / 12;
              return {d: ipath(700, bf * U, tw * U, D2 * U, TF2 * U), S: I / (D2 / 2) / (B2 * D2 * D2 / 6), W: 1}; },
    3: g => { const k = 1 + (K3 - 1) * g; return {d: ipath(1100, b * k, b * k, h * k, h * k / 4), S: k ** 3, W: k * k}; },
  };
  const clocks = {1: revealClock(1), 2: revealClock(2), 3: revealClock(3)};
  function draw() {
    for (const n of [1, 2, 3]) {
      const t = clocks[n](), g = smooth(Math.min(1, Math.max(0, (t - 0.5) / 2.2)));
      const r = shape[n](g);
      $('r' + n).setAttribute('d', r.d);
      $('s' + n).textContent = g >= 1 ? FIN[n][0] : r.S.toFixed(1) + '×';
      $('w' + n).textContent = g >= 1 ? FIN[n][1] : r.W.toFixed(1) + '×';
      $('t' + n).setAttribute('opacity', Math.min(1, Math.max(0, (t - 2.9) / 0.5)).toFixed(2));
    }
    if (isNaN(FIXED_T)) requestAnimationFrame(draw);
  }
  draw();
})();
</script>"""
    for k, v in dict(SY=SY, U=U, b=b, h=h, B2=B2, D2=D2, TF2=TF2, TW2=TW2, K3=K3,
                     FIN=str({k: list(v) for k, v in finals.items()}).replace("'", '"')).items():
        js = js.replace(f"%{k}%", str(v))
    css = lib.TEXT_CSS + f"""
  .concl {{ position: absolute; left: 140px; top: 598px; width: 1000px; padding: 12px 18px; font-size: 22px;
           text-align: center; border: 2px solid {RED}; border-radius: 6px; background: #fbecec; }}
"""
    concl = ('  <div class="concl" data-step="4">Best: a <b>deep</b> section with its material '
             '<b>far from the N.A.</b> → steel W-shapes</div>')
    title = 'Three ways to get a <span class="key">bigger</span> <i>S</i>'
    body = svg + "\n" + js + "\n" + concl + (
        f'\n  <div class="note">{lib.SOURCE}, Sec. 15.2, pp. 690–691. '
        'Sections to scale; illustrative ratios computed from <i>S</i> = <i>I</i>/<i>c</i>.</div>')
    lib.write_page("11_slide10_bigger_s.html", "Slide 10 - Bigger S", title, body, 10, css)
    print(f"I-shape S ratio {S2:.3f}; scaled section weight {K3 ** 2:.3f}")


if __name__ == "__main__":
    build()
