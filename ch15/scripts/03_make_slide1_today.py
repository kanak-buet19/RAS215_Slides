"""Slide 1 - Today: the four things this lecture covers.

Four rows, one per click. Each row has a small looping sketch (SVG SMIL
animation, about 150 x 80 px) beside one short line of text:
  1. a beam under load bends                (what limits a beam, 15.1)
  2. a rectangle grows until S = S_req      (sizing with the section modulus, 15.2)
  3. a square element shears                (checking shear stress, 15.2)
  4. W, rectangular and T sections appear   (three worked examples, Ex 15.1-15.3)
Sketches are illustrations, not to scale.

Writes ../slides/separate/01_slide1_today.html.
Run:  python3 03_make_slide1_today.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, S = lib.NAVY, lib.RED, lib.GREY, lib.STEEL

ROW_TOP, ROW_H = 150, 120
W, H = 170, 90                     # sketch box


def sketch_bend():
    flat = "M15,40 L155,40 L155,54 L15,54 Z"
    bent = "M15,40 Q85,62 155,40 L155,54 Q85,76 15,54 Z"
    arrows = "".join(f'<line x1="{x}" y1="8" x2="{x}" y2="34" stroke="{RED}" stroke-width="2" marker-end="url(#a_C00000)">'
                     f'<animate attributeName="y2" values="34;34;{34 + round(22 * (1 - ((x - 85) / 70) ** 2))};'
                     f'{34 + round(22 * (1 - ((x - 85) / 70) ** 2))};34" keyTimes="0;0.2;0.5;0.8;1" dur="4s" repeatCount="indefinite"/></line>'
                     for x in range(25, 150, 20))
    return f"""<path fill="{S['front']}" stroke="{S['edge']}" stroke-width="1.5" d="{flat}">
      <animate attributeName="d" values="{flat};{flat};{bent};{bent};{flat}" keyTimes="0;0.2;0.5;0.8;1" dur="4s" repeatCount="indefinite"/></path>
    {arrows}
    <polygon points="15,56 7,72 23,72" fill="#fff" stroke="{lib.SUPPORT}" stroke-width="1.5"/>
    <polygon points="155,56 147,70 163,70" fill="#fff" stroke="{lib.SUPPORT}" stroke-width="1.5"/>
    <circle cx="151" cy="74" r="2.5" fill="#fff" stroke="{lib.SUPPORT}"/><circle cx="159" cy="74" r="2.5" fill="#fff" stroke="{lib.SUPPORT}"/>"""


def sketch_size():
    return f"""<rect x="22" y="30" width="26" height="30" fill="{lib.WOOD['face']}" stroke="{lib.WOOD['edge']}" stroke-width="1.5">
      <animate attributeName="height" values="20;20;58;58;20" keyTimes="0;0.15;0.6;0.85;1" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="y" values="35;35;16;16;35" keyTimes="0;0.15;0.6;0.85;1" dur="4s" repeatCount="indefinite"/></rect>
    <text x="70" y="40" font-size="17">{lib.sym('S')}</text>
    <text x="70" y="64" font-size="17">{lib.sym('S', 'req')}</text>
    <rect x="98" y="28" height="14" fill="{NAVY}"><animate attributeName="width" values="12;12;56;56;12" keyTimes="0;0.15;0.6;0.85;1" dur="4s" repeatCount="indefinite"/></rect>
    <rect x="98" y="52" height="14" width="50" fill="{RED}" opacity="0.85"/>"""


def sketch_shear():
    sq = "M60,22 L110,22 L110,72 L60,72 Z"
    sh = "M72,22 L122,22 L98,72 L48,72 Z"
    return f"""<path d="{sq}" fill="#e8ecf1" stroke="{S['edge']}" stroke-width="1.5">
      <animate attributeName="d" values="{sq};{sq};{sh};{sh};{sq}" keyTimes="0;0.2;0.5;0.8;1" dur="4s" repeatCount="indefinite"/></path>
    <line x1="64" y1="12" x2="112" y2="12" stroke="{lib.TAU}" stroke-width="2.2" marker-end="url(#a_{lib.TAU[1:]})"/>
    <line x1="106" y1="82" x2="58" y2="82" stroke="{lib.TAU}" stroke-width="2.2" marker-end="url(#a_{lib.TAU[1:]})"/>
    <line x1="132" y1="70" x2="132" y2="24" stroke="{lib.TAU}" stroke-width="2.2" marker-end="url(#a_{lib.TAU[1:]})"/>
    <line x1="38" y1="24" x2="38" y2="70" stroke="{lib.TAU}" stroke-width="2.2" marker-end="url(#a_{lib.TAU[1:]})"/>"""


def sketch_examples():
    w = (f'<path d="M14,22 h40 v6 h-17 v32 h17 v6 h-40 v-6 h17 v-32 h-17 z" fill="{S["front"]}" stroke="{S["edge"]}" stroke-width="1.3"/>')
    r = f'<rect x="72" y="20" width="26" height="48" fill="{lib.WOOD["face"]}" stroke="{lib.WOOD["edge"]}" stroke-width="1.3"/>'
    t = (f'<path d="M114,20 h44 v9 h-17 v39 h-10 v-39 h-17 z" fill="{lib.WOOD["face"]}" stroke="{lib.WOOD["edge"]}" stroke-width="1.3"/>')
    def fade(el, b):
        # all three visible at rest; each dims and comes back in turn
        return (f'<g>{el}<animate attributeName="opacity" values="1;1;0.2;1;1" '
                f'keyTimes="0;{b};{b + 0.1:.2f};{b + 0.25:.2f};1" dur="4.5s" repeatCount="indefinite"/></g>')
    return fade(w, 0.05) + fade(r, 0.25) + fade(t, 0.45)


ROWS = [
    (sketch_bend, f"<b>What limits a beam:</b> bending stress, shear stress, buckling, deflection", "15.1"),
    (sketch_size, f"<b>Design for bending</b> using the section modulus: select {lib.mi('S')} ≥ {lib.mi('S', 'req')}", "15.2"),
    (sketch_shear, f"<b>Check shear:</b> make sure the shear stress stays under {lib.mi('τ', 'allow')}", "15.2"),
    (sketch_examples, "<b>Three worked examples:</b> a steel W-beam, a wood beam, a nailed T-beam", "Ex. 15.1–15.3"),
]


def build():
    css = lib.TEXT_CSS + f"""
  .row {{ position: absolute; left: 48px; width: 1184px; height: {ROW_H - 16}px; }}
  .row svg {{ position: absolute; left: 0; top: 0; }}
  .row .txt {{ position: absolute; left: 210px; top: 30px; font-size: 24px; width: 820px; }}
  .row .sec {{ position: absolute; right: 0; top: 34px; font-size: 18px; color: {GREY}; }}
  .row .rule {{ position: absolute; left: 210px; right: 0; top: {ROW_H - 12}px; border-top: 1px solid #d5d8dc; }}
"""
    rows = ""
    for i, (fn, txt, sec) in enumerate(ROWS):
        rows += f"""  <div class="row" data-step="{i + 1}" style="top:{ROW_TOP + i * ROW_H}px">
    <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>{lib.markers(RED, lib.TAU)}</defs>{fn()}</svg>
    <div class="txt">{txt}</div><div class="sec">{sec}</div>{'' if i == 3 else '<div class="rule"></div>'}
  </div>
"""
    title = 'Today: how to <span class="key">design</span> a beam against failure'
    body = rows + f'  <div class="note">{lib.SOURCE}, Ch. 15. Sketches not to scale.</div>'
    lib.write_page("01_slide1_today.html", "Slide 1 - Today", title, body, 1, css)


if __name__ == "__main__":
    build()
