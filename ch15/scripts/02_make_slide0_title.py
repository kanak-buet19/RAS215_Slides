"""Title page (no page number), laid out as in presentation-guideline.md A12.

Campus photo (../../assets/campus_photo.jpeg, from the reference deck) washed
with 85 % white so it stays faint (user choice 2026-11-10); navy bold title
with a subtitle line; presenter block; event line bottom left.

Right of the name block: a looping animation (illustration, not a simulation)
of a simply supported wide-flange (W) beam drawn in 3-D (oblique view: the
beam axis stays level, depth recedes up-right; front, top and right end face visible). Each 8 s cycle:
  0.0-1.0 s  the uniform load drops onto the beam
  1.0-3.0 s  the beam bends (smoothstep)
  3.0-5.0 s  hold
  5.0-6.5 s  load removed, the beam springs back
  6.5-8.0 s  pause
Deflection follows the elastic curve of a simply supported beam under a
uniform load, w(x) proportional to x - 2x^3 + x^4 (x = position / span),
exaggerated (26 px at mid-span). Plane sections stay plane: each section
turns by the slope w'(x), so the top fibres move toward mid-span and the bottom
fibres away from it. The pin end stays fixed and the roller end rolls outward.
?t=SECONDS in the address freezes the animation at that time (for checking).

Writes ../slides/separate/00_slide0_title.html.
Run:  python3 02_make_slide0_title.py
"""
import importlib
import json

lib = importlib.import_module("01_slide_lib")

NAVY, RED, GREY = lib.NAVY, lib.RED, lib.GREY
WASH = 0.85             # white over the campus photo (guideline default 0.68; fainter on request)

# Beam geometry in svg px (world units), and the view
GEO = dict(L=440, d=56, bf=84, tf=9, tw=8,     # span, depth, flange width, flange thickness, web thickness
           A=24,                                # mid-span deflection at full load (exaggerated)
           X0=96, Y0=118,                       # svg position of the left end, neutral axis
           cx=0.62, cy=0.38,                    # oblique view: depth axis z drawn as (-cx*z, +cy*z)
           N=48, nArrows=13, T=8.0)
STEEL = {"top": "#c3c9d1", "front": "#9aa1aa", "web": "#868d97", "inner": "#aeb4bc",
         "end": "#737a84", "edge": "#3f4650"}


def beam_animation():
    faces = "\n    ".join(f'<path id="{k}" fill="{c}" stroke="{STEEL["edge"]}" stroke-width="1" stroke-linejoin="round"/>'
                           for k, c in [("f0", STEEL["inner"]), ("f1", STEEL["web"]), ("f2", STEEL["inner"]),
                                        ("f3", STEEL["front"]), ("f4", STEEL["front"]), ("f5", STEEL["top"]),
                                        ("f6", STEEL["end"])])
    svg = f"""<svg class="fig" style="left:590px; top:290px" width="640" height="245" viewBox="0 0 640 245">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
  </defs>
  <g id="beam">
    {faces}
    <line id="na" stroke="{NAVY}" stroke-width="1.3" stroke-dasharray="5 4"/>
  </g>
  <g id="supports" fill="#ffffff" stroke="{STEEL['edge']}" stroke-width="2"></g>
  <text id="naLbl" font-size="14" fill="{NAVY}">N.A.</text>
  <g id="load"></g>
  <text id="status" x="320" y="232" font-size="15" font-style="italic" fill="{GREY}" text-anchor="middle"></text>
</svg>"""
    js = """<script>
(() => {
  const G = %s;
  const {L, d, bf, tf, tw, A, X0, Y0, cx, cy, N, nArrows, T} = G;
  const RED = "%s";
  const $ = id => document.getElementById(id);
  const sm = u => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };   // smoothstep

  // elastic curve, simply supported beam, uniform load: w = (16/5)(x - 2x^3 + x^4), max 1 at mid-span
  const w  = xi => 3.2 * (xi - 2 * xi ** 3 + xi ** 4);
  const wp = xi => 3.2 * (1 - 6 * xi * xi + 4 * xi ** 3) / L;          // dw/dX

  // world point (X along span, y up from the N.A., z toward the viewer) -> svg, at load level s (0..1)
  function P(X, y, z, s) {
    const xi = X / L, a = A * s;
    const shift = (d / 2) * a * wp(0);          // keep the pin (bottom fibre at X = 0) in place
    const Xd = X + y * a * wp(xi) + shift;      // plane sections turn by the slope
    const Yd = y - a * w(xi);
    // oblique view: the beam axis stays level, the depth axis recedes up and to the right
    return [X0 + Xd - cx * z, Y0 - Yd + cy * z];
  }
  const pts = a => a.map(p => p[0].toFixed(1) + "," + p[1].toFixed(1)).join(" L");
  function strip(y1, z1, y2, z2, s) {            // face swept along the span between two section points
    const A1 = [], A2 = [];
    for (let i = 0; i <= N; i++) { const X = L * i / N; A1.push(P(X, y1, z1, s)); A2.unshift(P(X, y2, z2, s)); }
    return "M" + pts(A1.concat(A2)) + "Z";
  }
  const h = d / 2, b = bf / 2, t = tw / 2;
  const SECTION = [[h, -b], [h, b], [h - tf, b], [h - tf, t], [-h + tf, t], [-h + tf, b], [-h, b], [-h, -b],
                   [-h + tf, -b], [-h + tf, -t], [h - tf, -t], [h - tf, -b]];

  function draw(time) {
    const tc = ((time %% T) + T) %% T;
    let s, arrowIn, status;
    if (tc < 1.0)      { s = 0;                 arrowIn = sm(tc / 1.0);         status = "Load applied"; }
    else if (tc < 3.0) { s = sm((tc - 1) / 2);  arrowIn = 1;                    status = "The beam bends: top squeezed, bottom stretched"; }
    else if (tc < 5.0) { s = 1;                 arrowIn = 1;                    status = "The beam bends: top squeezed, bottom stretched"; }
    else if (tc < 6.5) { s = 1 - sm((tc - 5) / 1.5); arrowIn = 1 - sm((tc - 5) / 1.0); status = "Load removed: the beam springs back"; }
    else               { s = 0;                 arrowIn = 0;                    status = ""; }

    // faces, drawn back to front
    $("f0").setAttribute("d", strip(-h + tf, -b, -h + tf, -t, s));   // bottom flange, top face, behind the web
    $("f1").setAttribute("d", strip(h - tf, t, -h + tf, t, s));      // web, front face
    $("f2").setAttribute("d", strip(-h + tf, t, -h + tf, b, s));     // bottom flange, top face, in front
    $("f3").setAttribute("d", strip(-h + tf, b, -h, b, s));          // bottom flange, front face
    $("f4").setAttribute("d", strip(h, b, h - tf, b, s));            // top flange, front face
    $("f5").setAttribute("d", strip(h, -b, h, b, s));                // top flange, top face
    $("f6").setAttribute("d", "M" + pts(SECTION.map(([y, z]) => P(L, y, z, s))) + "Z");   // right end face
    const n1 = P(L, 0, -t - 10, s), n2 = P(L, 0, t + 10, s);
    $("na").setAttribute("x1", n1[0]); $("na").setAttribute("y1", n1[1]);
    $("na").setAttribute("x2", n2[0]); $("na").setAttribute("y2", n2[1]);
    const nl = P(L, 0, -b, s);
    $("naLbl").setAttribute("x", nl[0] + 14); $("naLbl").setAttribute("y", nl[1] + 5);

    // supports: pin at X = 0 (fixed), roller at X = L (moves with the bottom fibre)
    const pa = P(0, -h, b, s), pb = P(L, -h, b, s);      // under the front bottom edge, so they are not hidden
    $("supports").innerHTML =
      `<polygon points="${pa[0]},${pa[1]} ${pa[0] - 14},${pa[1] + 24} ${pa[0] + 14},${pa[1] + 24}"/>` +
      `<line x1="${pa[0] - 24}" y1="${pa[1] + 25}" x2="${pa[0] + 24}" y2="${pa[1] + 25}"/>` +
      `<polygon points="${pb[0]},${pb[1]} ${pb[0] - 13},${pb[1] + 17} ${pb[0] + 13},${pb[1] + 17}"/>` +
      `<circle cx="${pb[0] - 7}" cy="${pb[1] + 21}" r="3.5" stroke-width="1.5"/>` +
      `<circle cx="${pb[0] + 7}" cy="${pb[1] + 21}" r="3.5" stroke-width="1.5"/>` +
      `<line x1="${pb[0] - 24}" y1="${pa[1] + 25}" x2="${pb[0] + 24}" y2="${pa[1] + 25}"/>`;

    // uniform load: arrows on the centre line of the top face; they drop in and lift off
    let g = "";
    const lift = 30 * (1 - arrowIn), len = 40;
    const tails = [];
    for (let i = 0; i < nArrows; i++) {
      const X = 12 + (L - 24) * i / (nArrows - 1);
      const tip = P(X, h + 3, 0, s);
      const y2 = tip[1] - lift, y1 = y2 - len;
      tails.push([tip[0], y1]);
      g += `<line x1="${tip[0]}" y1="${y1}" x2="${tip[0]}" y2="${y2}" stroke="${RED}" stroke-width="2" marker-end="url(#ar)"/>`;
    }
    g += `<path d="M${pts(tails)}" fill="none" stroke="${RED}" stroke-width="2"/>`;
    const mid = tails[(nArrows - 1) / 2];
    g += `<text x="${mid[0]}" y="${mid[1] - 10}" font-size="16" font-weight="bold" fill="${RED}" text-anchor="middle">Load</text>`;
    $("load").innerHTML = g;
    $("load").setAttribute("opacity", arrowIn.toFixed(3));
    $("status").textContent = status;
  }

  const fixed = parseFloat(new URLSearchParams(location.search).get("t"));
  if (!isNaN(fixed)) { draw(fixed); return; }
  let t0 = null;
  function frame(now) { if (t0 === null) t0 = now; draw((now - t0) / 1000); requestAnimationFrame(frame); }
  draw(0);
  requestAnimationFrame(frame);
})();
</script>""" % (json.dumps(GEO), RED)
    return svg + "\n" + js


def build():
    photo = lib.data_uri(lib.ASSETS / "polytechnic_photo.jpeg", "image/jpeg")
    css = f"""
  .bg {{ position: absolute; left: 0; top: 0; width: 1280px; height: 720px; object-fit: cover; }}
  .wash {{ position: absolute; left: 0; top: 0; width: 1280px; height: 720px;
           background: rgba(255, 255, 255, {WASH}); }}
  .title {{ top: 168px; width: 1080px; font-size: 38px; z-index: 1; }}
  .sub {{ position: absolute; left: 48px; top: 222px; margin: 0; font-size: 30px; color: {NAVY}; }}
  .who {{ position: absolute; left: 48px; top: 330px; font-size: 22px; line-height: 1.45; color: #000; }}
  .who b {{ font-size: 30px; }}
  .who a {{ color: #0563c1; text-decoration: underline; }}
  .who .pi {{ margin-top: 14px; font-size: 18px; }}
  .event {{ position: absolute; left: 48px; top: 612px; font-size: 20px; line-height: 1.45; color: #000; }}
"""
    title = "Chapter 15: Design of Beams and Shafts"
    body = f"""  <img class="bg" src="{photo}" alt="">
  <div class="wash"></div>
  <p class="sub">Basis for beam design, prismatic beam design, worked examples</p>
  <div class="who"><b>Rakibul Islam Kanak</b><br>
    Teaching Assistant, RAS 215<br>
    School of Manufacturing Systems and Networks<br>
    Arizona State University<br>
    Email: <a href="mailto:rkanak@asu.edu">rkanak@asu.edu</a>
    <div class="pi">PI: Zhengtao Gan, Assistant Professor</div></div>
{beam_animation()}
  <div class="event">RAS 215 lecture<br>Thursday, November 12, 2026</div>
  <div class="note">Based on {lib.SOURCE}, Ch. 15. Animation not to scale.</div>"""
    lib.write_page("00_slide0_title.html", "Ch 15 - Title", title, body, "", css)


if __name__ == "__main__":
    build()
