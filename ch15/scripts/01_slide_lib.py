"""Shared parts of every Ch 15 slide.

Look follows /Users/rakibul/work/Research/PHOENIX/docs/presentation-guideline.md
(design only): a fixed 1280 x 720 px page, navy bold title top left, ASU logo
top right, page number bottom right, grey source line bottom left.

Standard library only (no numpy / PIL):
- logo: ../../assets/asu_logo.jpeg (taken from the reference deck
  "Dimensionless learning3.pptx", ppt/media/image5.jpeg). Its white background
  is dropped with CSS mix-blend-mode: multiply, so it also sits cleanly on
  the title-page photo; the 'Arizona State University' wordmark is kept, the
  empty margin is cut off by the wrapper box.
- maths font: macOS STIX Two Math, embedded as a data URI on slides with MathML.

Slide scripts load this file with importlib.import_module("01_slide_lib").
"""
import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
CH = HERE.parent                       # ch15/
ROOT = CH.parent                       # RAS_215/
ASSETS = ROOT / "assets"
SLIDES = CH / "slides" / "separate"    # one file per slide; the deck goes in ../slides/

NAVY = "#002060"   # titles, structure
RED = "#C00000"    # the one emphasis colour
INK = "#000000"
GREY = "#555555"
FONT = "Arial, Helvetica, sans-serif"
MATH_FONTS = [Path("/System/Library/Fonts/Supplemental/STIXTwoMath.otf"),
              Path("/usr/share/texmf/fonts/opentype/public/lm-math/latinmodern-math.otf")]

SOURCE = "R. C. Hibbeler, <i>Statics and Mechanics of Materials</i>, 6th ed., Pearson"

# Logo crop: the ink of asu_logo.jpeg (900 x 900 px) spans about x 160-830, y 210-725.
LOGO_H = 92                                  # shown height (page px)
_CROP = (160, 210, 830, 725)                 # left, top, right, bottom in image px
_S = LOGO_H / (_CROP[3] - _CROP[1])
LOGO_W = round((_CROP[2] - _CROP[0]) * _S)


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(Path(path).read_bytes()).decode()


def logo_html():
    """ASU logo, top right, white made see-through by multiply blending."""
    img = data_uri(ASSETS / "asu_logo.jpeg", "image/jpeg")
    return (f'<div class="logo"><img src="{img}" alt="Arizona State University" '
            f'style="width:{900 * _S:.1f}px;left:{-_CROP[0] * _S:.1f}px;top:{-_CROP[1] * _S:.1f}px"></div>')


BASE_CSS = f"""
  html, body {{ margin: 0; height: 100%; background: #e5e7eb; }}
  body {{ display: flex; align-items: center; justify-content: center; overflow: hidden; }}
  .slide {{ position: relative; width: 1280px; height: 720px; background: #ffffff; flex: none;
           font-family: {FONT}; color: {INK}; transform-origin: center; overflow: hidden; }}
  .title {{ position: absolute; left: 48px; top: 16px; width: 1050px; margin: 0;
           font-size: 40px; line-height: 1.12; font-weight: bold; color: {NAVY}; }}
  .key {{ color: {RED}; font-style: italic; }}
  .logo {{ position: absolute; right: 22px; top: 10px; width: {LOGO_W}px; height: {LOGO_H}px;
          overflow: hidden; mix-blend-mode: multiply; z-index: 2; }}
  .logo img {{ position: absolute; }}
  .fig {{ position: absolute; overflow: visible; }}
  .em {{ color: {RED}; font-weight: bold; font-style: italic; }}
  .note {{ position: absolute; left: 48px; top: 698px; max-width: 1150px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-size: 13px; color: {GREY}; font-style: italic; }}
  .num {{ position: absolute; right: 16px; bottom: 8px; font-size: 16px; }}
  math {{ font-family: "Slide Math", "STIX Two Math", "Latin Modern Math", "Cambria Math", math; }}
"""


STEEL = {"top": "#c3c9d1", "front": "#9aa1aa", "web": "#868d97", "inner": "#aeb4bc",
         "end": "#737a84", "edge": "#3f4650"}
WOOD = {"face": "#e2c28f", "edge": "#8a6a3b"}
SUPPORT = "#3f4650"
SIG = NAVY         # bending (normal) stress, on every slide
TAU = "#1f7a5a"    # shear stress, on every slide (green)
SIGY = "#7b3fa0"   # sigma_y, the local vertical squeeze under a load (purple)

# Shared CSS for text blocks on content slides
TEXT_CSS = f"""
  .pts {{ position: absolute; margin: 0; padding: 0; list-style: none; font-size: 20px; line-height: 1.35; }}
  .pts li {{ position: relative; padding-left: 20px; margin-bottom: 10px; }}
  .pts li::before {{ content: "•"; position: absolute; left: 0; }}
  .head {{ position: absolute; font-size: 20px; font-weight: bold; margin: 0; }}
  .cap {{ font-size: 15px; color: {GREY}; font-style: italic; }}
  svg text {{ font-family: {FONT}; }}
  .sym {{ font-family: "Times New Roman", "STIX Two Text", serif; font-style: italic; }}
"""


def mi(base, sub=None):
    """Inline maths symbol in HTML text, e.g. mi('σ', 'x')."""
    b = f"<mi>{base}</mi>"
    return f"<math>{f'<msub>{b}<mi>{sub}</mi></msub>' if sub else b}</math>"


# Inline MathML formulas used in text and source lines
M_FLEX = '<math><mi>σ</mi><mo>=</mo><mi>M</mi><mi>y</mi><mo>/</mo><mi>I</mi></math>'
M_SHEAR = '<math><mi>τ</mi><mo>=</mo><mi>V</mi><mi>Q</mi><mo>/</mo><mi>I</mi><mi>t</mi></math>'


def hreact(x, ybot, name, val_step, color=None):
    """Horizontal pin reaction R_<name>x: short arrow pointing right into the pin at (x, ybot), ybot = beam bottom.
    Label 'R_<name>x' under the arrow; '= 0' beside it appears on click val_step (from sum F_x = 0)."""
    c = color or NAVY
    y = ybot + 7
    return (f'<line x1="{x - 46}" y1="{y}" x2="{x - 5}" y2="{y}" stroke="{c}" stroke-width="3" marker-end="url(#a_{c[1:]})"/>'
            f'<text x="{x - 33}" y="{y + 22}" font-size="17" fill="{c}" font-weight="bold" text-anchor="end">{sym("R", name + "x")}</text>'
            f'<text data-step="{val_step}" x="{x - 30}" y="{y + 22}" font-size="16" fill="{c}" font-weight="bold">= 0</text>')


def sym(base, sub=None, size=None):
    """Symbol inside SVG text: italic serif base with a subscript."""
    fs = f' font-size="{size}"' if size else ""
    out = f'<tspan class="sym"{fs}>{base}</tspan>'
    if sub:
        # one- and two-letter subscripts are symbols (italic, e.g. A, Ax); words like max, allow, web are upright, as in the book
        cls = ' class="sym"' if len(sub) <= 2 else ' font-family="Times New Roman, STIX Two Text, serif"'
        out += f'<tspan baseline-shift="sub" font-size="70%"{cls}>{sub}</tspan>'
    return out


def markers(*colors):
    """SVG arrow-head markers named a_<hex> for each colour."""
    return "".join(
        f'<marker id="a_{c.strip("#")}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
        f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in colors)


# JavaScript helpers shared by animated slides (added once per page with ELASTIC_JS).
ELASTIC_JS = """
// Elastic curve of a simply supported beam (pin at 0, roller at L) by integrating -M(x) twice.
// loads: [{type:'P', a, P}] point loads and [{type:'w', a, b, w}] uniform loads, downward positive.
// Returns N+1 deflections (downward positive), scaled so the largest is 1.
function elasticCurve(L, loads, N) {
  let R1 = 0;
  for (const q of loads) {
    if (q.type === 'P') R1 += q.P * (L - q.a) / L;
    else R1 += q.w * (q.b - q.a) * (L - (q.a + q.b) / 2) / L;
  }
  const M = x => {
    let m = R1 * x;
    for (const q of loads) {
      if (q.type === 'P') { if (x > q.a) m -= q.P * (x - q.a); }
      else { const p1 = Math.max(0, x - q.a), p2 = Math.max(0, x - q.b); m -= q.w * (p1 * p1 - p2 * p2) / 2; }
    }
    return m;
  };
  const dx = L / N, th = [0], w = [0];
  for (let i = 1; i <= N; i++) {
    th.push(th[i - 1] - M((i - 0.5) * dx) * dx);       // w'' = -M/EI with w downward
    w.push(w[i - 1] + (th[i - 1] + th[i]) / 2 * dx);
  }
  const out = w.map((v, i) => v - w[N] * i / N);   // w(0) = w(L) = 0
  const mx = Math.max(...out.map(Math.abs)) || 1;
  return out.map(v => v / mx);
}
const smooth = u => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
// time source: ?t=SECONDS freezes, else seconds since the page (or the click that showed it) started
const FIXED_T = parseFloat(new URLSearchParams(location.search).get('t'));
// Seconds since build step `step` was revealed (deck), or since page load (single file).
// Going back into a slide (shown complete) jumps to the end state.
function revealClock(step) {
  let t0 = performance.now();
  addEventListener('buildstep', e => {
    const {k, jump} = e.detail;
    if (k < step) t0 = Infinity;
    else if (t0 === Infinity) t0 = jump ? -1e9 : performance.now();
  });
  return () => !isNaN(FIXED_T) ? FIXED_T : Math.max(0, (performance.now() - t0) / 1000);
}
function loop(draw) {
  if (!isNaN(FIXED_T)) { draw(FIXED_T); return; }
  let t0 = null;
  const f = now => { if (t0 === null) t0 = now; draw((now - t0) / 1000); requestAnimationFrame(f); };
  requestAnimationFrame(f);
}
"""


TERM_ARROWS_JS = """
// Curved arrows from labels to terms of a rendered equation (positions measured after layout).
// pairs: [[termId, labelId, pathId], ...]. Left labels start after their first text line, right labels at their left edge.
function termArrows(pairs) {
  const sl = document.getElementById('slide').getBoundingClientRect(), k = sl.width / 1280;
  const box = el => { const r = el.getBoundingClientRect();
    return {l: (r.left - sl.left) / k, r: (r.right - sl.left) / k, t: (r.top - sl.top) / k, b: (r.bottom - sl.top) / k}; };
  for (const [term, lbl, path] of pairs) {
    const T = document.getElementById(term), L = document.getElementById(lbl), a = box(T), lb = box(L);
    const rs = document.createRange(); rs.selectNodeContents(L);
    const rects = [...rs.getClientRects()]; if (!rects.length) continue;
    const fl = rects[0], ly = ((fl.top + fl.bottom) / 2 - sl.top) / k;
    let lineEnd = fl.right;
    for (const r of rects) if (Math.abs((r.top + r.bottom) / 2 - (fl.top + fl.bottom) / 2) < 12) lineEnd = Math.max(lineEnd, r.right);
    const left = lb.l < a.l;
    const sx = left ? (lineEnd - sl.left) / k + 8 : lb.l - 8;
    const ex = left ? a.l - 4 : a.r + 4, ey = (a.t + a.b) / 2;
    const cx = (sx + ex) / 2, cy = ly + (ey - ly) * 0.15 - (ey > ly ? 0 : 18);
    document.getElementById(path).setAttribute('d',
      `M${sx.toFixed(1)},${ly.toFixed(1)} Q${cx.toFixed(1)},${cy.toFixed(1)} ${ex.toFixed(1)},${ey.toFixed(1)}`);
  }
}
function termArrowsWhenReady(pairs) {
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => requestAnimationFrame(() => termArrows(pairs)));
  addEventListener('resize', () => termArrows(pairs));
}
"""

IBEAM_JS = """
// 3-D wide-flange beam in an oblique view (beam axis level, depth axis z drawn as (-cx z, +cy z)).
// g: <g> element to fill. o: {L, d, bf, tf, tw, X0, Y0, cx, cy, N, col}. disp(X) -> {w, u, phi}:
// w downward deflection, u sideways shift (z, + toward the viewer), phi twist (rad, + turns the top toward +z).
function drawIBeam(g, o, disp) {
  const {L, d, bf, tf, tw, X0, Y0, cx, cy, N, col} = o;
  const h = d / 2, b = bf / 2, t = tw / 2;
  const P = (X, y, z) => {
    const q = disp(X), c = Math.cos(q.phi), s = Math.sin(q.phi);
    const yr = y * c - z * s, zr = y * s + z * c + q.u;
    return [X0 + X - cx * zr, Y0 - (yr - q.w) + cy * zr];
  };
  const f = p => p[0].toFixed(1) + ',' + p[1].toFixed(1);
  const strip = (y1, z1, y2, z2) => {
    const A = [], B = [];
    for (let i = 0; i <= N; i++) { const X = L * i / N; A.push(f(P(X, y1, z1))); B.unshift(f(P(X, y2, z2))); }
    return 'M' + A.concat(B).join(' L') + 'Z';
  };
  const SEC = [[h, -b], [h, b], [h - tf, b], [h - tf, t], [-h + tf, t], [-h + tf, b], [-h, b], [-h, -b],
               [-h + tf, -b], [-h + tf, -t], [h - tf, -t], [h - tf, -b]];
  const face = (dd, c) => `<path d="${dd}" fill="${c}" stroke="${col.edge}" stroke-width="1" stroke-linejoin="round"/>`;
  g.innerHTML =
    face(strip(-h + tf, -b, -h + tf, -t), col.inner) + face(strip(h - tf, t, -h + tf, t), col.web) +
    face(strip(-h + tf, t, -h + tf, b), col.inner) + face(strip(-h + tf, b, -h, b), col.front) +
    face(strip(h, b, h - tf, b), col.front) + face(strip(h, -b, h, b), col.top) +
    face('M' + SEC.map(([y, z]) => f(P(L, y, z))).join(' L') + 'Z', col.end);
  return P;
}
"""


def math_font_css():
    """@font-face rule with the first maths font found, as a data URI."""
    for p in MATH_FONTS:
        if p.exists():
            return ('\n  @font-face { font-family: "Slide Math"; '
                    f'src: url({data_uri(p, "font/otf")}) format("opentype"); }}')
    return ""


def wbeam_side(x, y, w, h=14):
    """Side view of a W-shape beam: darker flange strips top and bottom, lighter web between."""
    tf = h * 0.25
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{STEEL["top"]}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{tf:.1f}" fill="{STEEL["end"]}"/>'
            f'<rect x="{x}" y="{y + h - tf:.1f}" width="{w}" height="{tf:.1f}" fill="{STEEL["end"]}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{STEEL["edge"]}" stroke-width="1.5"/>')


def wsection_icon(cx, cy, d=34, bf=24, tf=5, tw=4):
    """Small W-shape cross-section (end view), centred at (cx, cy)."""
    H, w, b, t = d / 2, d / 2 - tf, bf / 2, tw / 2
    pts = [(-b, -H), (b, -H), (b, -w), (t, -w), (t, w), (b, w), (b, H), (-b, H), (-b, w), (-t, w), (-t, -w), (-b, -w)]
    dd = "M" + " L".join(f"{cx + a:.1f},{cy + c:.1f}" for a, c in pts) + " Z"
    return f'<path d="{dd}" fill="{STEEL["inner"]}" stroke="{STEEL["edge"]}" stroke-width="1.5"/>'


def wbeam_elev(x, y, w, h=26):
    """Engineering-drawing elevation of a W-beam, shaded like real steel: the flanges stand out toward the
    viewer (lit faces), the web sits back in their shadow. Flange inner edges drawn as visible lines."""
    tf = 0.2 * h
    return (f'<defs><linearGradient id="wbFl" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#eef0f3"/><stop offset="1" stop-color="#a7adb6"/></linearGradient>'
            f'<linearGradient id="wbWeb" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#596069"/><stop offset="0.3" stop-color="#7f868f"/>'
            f'<stop offset="1" stop-color="#959ca5"/></linearGradient></defs>'
            f'<rect x="{x}" y="{y + tf:.1f}" width="{w}" height="{h - 2 * tf:.1f}" fill="url(#wbWeb)"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{tf:.1f}" fill="url(#wbFl)"/>'
            f'<rect x="{x}" y="{y + h - tf:.1f}" width="{w}" height="{tf:.1f}" fill="url(#wbFl)"/>'
            f'<line x1="{x}" y1="{y + tf:.1f}" x2="{x + w}" y2="{y + tf:.1f}" stroke="{STEEL["edge"]}" stroke-width="1"/>'
            f'<line x1="{x}" y1="{y + h - tf:.1f}" x2="{x + w}" y2="{y + h - tf:.1f}" stroke="{STEEL["edge"]}" stroke-width="1"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{STEEL["edge"]}" stroke-width="1.6"/>')


def wbeam_end_view(x_end, cx, y, h=26, label="", label2=""):
    """End view (cross-section) of the W-beam to the right of the elevation, with dashed projection lines."""
    tf, bf, tw = 0.2 * h, 0.62 * h, 0.1 * h
    H = h / 2
    cy = y + H
    out = ""
    for yy in (y, y + tf, y + h - tf, y + h):
        out += (f'<line x1="{x_end + 4}" y1="{yy:.1f}" x2="{cx - bf / 2 - 3:.1f}" y2="{yy:.1f}" stroke="#7a808a" '
                f'stroke-width="0.8" stroke-dasharray="3 3"/>')
    w = H - tf
    pts = [(-bf / 2, -H), (bf / 2, -H), (bf / 2, -w), (tw / 2, -w), (tw / 2, w), (bf / 2, w), (bf / 2, H), (-bf / 2, H),
           (-bf / 2, w), (-tw / 2, w), (-tw / 2, -w), (-bf / 2, -w)]
    d = "M" + " L".join(f"{cx + a:.1f},{cy + b:.1f}" for a, b in pts) + " Z"
    out += f'<path d="{d}" fill="#b4bac2" stroke="{STEEL["edge"]}" stroke-width="1.4"/>'
    out += (f'<line x1="{cx - bf / 2 - 6:.1f}" y1="{cy}" x2="{cx + bf / 2 + 6:.1f}" y2="{cy}" stroke="#7a808a" stroke-width="0.8" stroke-dasharray="6 2 2 2"/>'
            f'<line x1="{cx}" y1="{y - 6}" x2="{cx}" y2="{y + h + 6}" stroke="#7a808a" stroke-width="0.8" stroke-dasharray="6 2 2 2"/>')
    if label:
        out += f'<text x="{cx}" y="{y - 10}" font-size="13" fill="{GREY}" text-anchor="middle">{label}</text>'
    if label2:
        out += f'<text x="{cx}" y="{y + h + 20}" font-size="14" fill="{GREY}" text-anchor="middle">{label2}</text>'
    return out


def write_page(out_name, page_title, title_html, body_html, num, css=""):
    """Write one slide as a self-contained HTML file in ../slides/separate/.
    num = "" for the title page (no page number)."""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<style>{math_font_css() if "<math" in body_html + title_html else ""}{BASE_CSS}{css}</style>
</head>
<body>
<div class="slide" id="slide">
  <h1 class="title">{title_html}</h1>
  {logo_html()}
{body_html}
  <div class="num">{num}</div>
</div>
<script>
  // Scale the fixed 1280 x 720 slide to fit the window.
  function fit() {{
    const s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
    document.getElementById('slide').style.transform = 'scale(' + s + ')';
  }}
  window.addEventListener('resize', fit); fit();
</script>
</body>
</html>
"""
    out = SLIDES / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB)")
    return out
