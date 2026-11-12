"""Slide 19 - Today's outcome: what students can do after this lecture (mirror of slide 1).

Four rows, one per click, each with the same looping sketch style as slide 1, one line of text,
the key equation and the section it came from:
  1  what limits a beam                     (15.1)
  2  size for bending: S_req = M_max / sigma_allow, lightest section with S >= S_req   (15.2, Eq. 15-1)
  3  check shear: tau_max = V_max Q / (I t) <= tau_allow, else a bigger section         (15.2)
  4  built-up beams: q = V Q / I, fastener spacing s = F / q                            (Ex. 15.3)
Every equation is one already shown in the deck (slides 9, 11, 15, 17, 18).

Writes ../slides/separate/19_slide19_outcome.html.
Run:  python3 24_make_slide19_outcome.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
today = importlib.import_module("03_make_slide1_today")      # same sketches as slide 1
NAVY, RED, GREY, WOOD = lib.NAVY, lib.RED, lib.GREY, lib.WOOD

ROW_TOP, ROW_H = 150, 120
W, H = 170, 90


def sketch_nails():
    """T-beam side view: flange on the web, nails at spacing s; the s dimension pulses."""
    s = (f'<rect x="12" y="24" width="146" height="14" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.3"/>'
         f'<rect x="12" y="38" width="146" height="34" fill="#d6b27a" stroke="{WOOD["edge"]}" stroke-width="1.3"/>')
    for x in (30, 70, 110, 150):
        s += (f'<line x1="{x}" y1="21" x2="{x}" y2="52" stroke="#333" stroke-width="2"/>'
              f'<line x1="{x - 5}" y1="21" x2="{x + 5}" y2="21" stroke="#333" stroke-width="2.4"/>')
    s += (f'<g><line x1="32" y1="9" x2="68" y2="9" stroke="{RED}" stroke-width="1.6" '
          f'marker-start="url(#a_C00000)" marker-end="url(#a_C00000)"/>'
          f'<text x="50" y="6" font-size="13" fill="{RED}" text-anchor="middle" font-style="italic" font-family="Times New Roman, serif">s</text>'
          f'<animate attributeName="opacity" values="1;1;0.25;1" keyTimes="0;0.5;0.75;1" dur="3s" repeatCount="indefinite"/></g>')
    return s


def m(x):
    return f'<math displaystyle="true">{x}</math>'


SALL = "<msub><mi>σ</mi><mtext>allow</mtext></msub>"
TALL = "<msub><mi>τ</mi><mtext>allow</mtext></msub>"
ROWS = [
    (today.sketch_bend, "<b>Name what limits a beam:</b> bending and shear stress; also buckling and deflection",
     "", "15.1"),
    (today.sketch_size, "<b>Design for bending:</b> select the lightest adequate section",
     m("<msub><mi>S</mi><mtext>req’d</mtext></msub><mo>=</mo><mfrac><msub><mi>M</mi><mtext>max</mtext></msub>" + SALL
       + "</mfrac><mo>,</mo><mspace width='0.5em'/><mi>S</mi><mo>≥</mo><msub><mi>S</mi><mtext>req’d</mtext></msub>"), "15.2"),
    (today.sketch_shear, "<b>Check shear;</b> if it fails, choose a bigger section",
     m("<msub><mi>τ</mi><mtext>max</mtext></msub><mo>=</mo><mfrac><mrow><msub><mi>V</mi><mtext>max</mtext></msub><mi>Q</mi></mrow>"
       "<mrow><mi>I</mi><mi>t</mi></mrow></mfrac><mo>≤</mo>" + TALL), "15.2"),
    (sketch_nails, "<b>Space the fasteners</b> of a built-up beam from the shear flow",
     m("<mi>q</mi><mo>=</mo><mfrac><mrow><mi>V</mi><mi>Q</mi></mrow><mi>I</mi></mfrac><mo>,</mo><mspace width='0.5em'/>"
       "<mi>s</mi><mo>≤</mo><mfrac><mi>F</mi><mi>q</mi></mfrac>"), "Ex. 15.3"),
]


def build():
    css = lib.TEXT_CSS + f"""
  .row {{ position: absolute; left: 48px; width: 1184px; height: {ROW_H - 16}px; }}
  .row svg {{ position: absolute; left: 0; top: 0; }}
  .row .txt {{ position: absolute; left: 210px; top: 0; height: {ROW_H - 24}px; display: flex; align-items: center; font-size: 22px; width: 520px; line-height: 1.35; }}
  .row .eq {{ position: absolute; left: 760px; top: 0; height: {ROW_H - 24}px; display: flex; align-items: center; font-size: 24px; color: {NAVY}; }}
  .row .sec {{ position: absolute; right: 0; top: 0; height: {ROW_H - 24}px; display: flex; align-items: center; font-size: 18px; color: {GREY}; }}
  .row .rule {{ position: absolute; left: 210px; right: 0; top: {ROW_H - 12}px; border-top: 1px solid #d5d8dc; }}
"""
    rows = ""
    for i, (fn, txt, eq, sec) in enumerate(ROWS):
        rows += f"""  <div class="row" data-step="{i + 1}" style="top:{ROW_TOP + i * ROW_H}px">
    <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>{lib.markers(RED, lib.TAU)}</defs>{fn()}</svg>
    <div class="txt"><span>{txt}</span></div><div class="eq">{eq}</div><div class="sec">{sec}</div>{'' if i == len(ROWS) - 1 else '<div class="rule"></div>'}
  </div>
"""
    title = 'Today’s <span class="key">outcome</span>: design a beam and verify it'
    body = rows + (f'  <div class="note">{lib.SOURCE}, Secs. 15.1–15.2, pp. 688–697; Eq. (15–1); '
                   f'<i>s</i> = <i>F</i>/<i>q</i>, Ex. 15.3, p. 697. Sketches not to scale.</div>')
    lib.write_page("19_slide19_outcome.html", "Slide 19 - Outcome", title, body, 19, css)


if __name__ == "__main__":
    build()
