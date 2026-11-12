"""Combine the single slides into one presentation file (guideline Part B1-B2).

Reads the slides listed in DECK (lecture order) from ../slides/separate/,
checks the printed page numbers run 1, 2, 3, ... (an unnumbered title page may
come first) and writes ../slides/RAS215_Ch15_Design_of_Beams_and_Shafts.html, one self-contained file.

Each slide runs in its own iframe (srcdoc). Elements marked data-step="N" stay
hidden until the N-th "next" on that slide and fade in; after the last step
"next" goes to the next slide. "Back" hides the last step, then goes to the
previous slide, shown complete.

Keys: -> / Space / PageDown / click = next, <- / PageUp = back, Home / End,
F = full screen, R = restart the current slide. #N in the URL opens slide N.

Run:  python3 90_make_deck.py   (after rebuilding any single slide)
"""
import importlib
import json
import re

lib = importlib.import_module("01_slide_lib")

OUT = lib.CH / "slides" / "RAS215_Ch15_Design_of_Beams_and_Shafts.html"
DECK = ["00_slide0_title.html",            # title page (no number)
        "01_slide1_today.html",            # 1 today
        "02b_slide3_bending.html",         # 2 why a vertical load gives sigma_x (bending)
        "02c_slide3_shear.html",           # 3 shear formula tau = VQ/It, sign convention
        "02d_slide4_element.html",         # 4 what a stress element is, how to draw tau
        "02_slide2_strength.html",         # 3 designed for bending and shear (15.1), sigma_y
        "03_slide3_section.html",          # 4 stress varies over the section
        "04_slide4_trajectories.html",     # 5 principal stresses, trajectories
        "05_slide5_limits.html",           # 8 buckling and deflection limits
        "10_slide9_design.html",           # 9 S_req = M_max / sigma_allow
        "11_slide10_bigger_s.html",        # 10 three ways to a bigger S
        "12_slide11_procedure.html",       # 11 design procedure
        "13a_slide12_vm.html",             # 12 how to draw V and M (Ex 15.1 beam)
        "13_slide12_ex151.html",           # 13 Example 15.1 (2/2)
        "14a_slide14_vm152.html",          # 14 Example 15.2 (1/2): V and M
        "14_slide14_ex152.html",           # 15 Example 15.2 (2/2)
        "16_slide16_ex153a.html",          # 16 Example 15.3 (1/2): checks
        "16b_slide17_shearflow.html",      # 17 why nails carry the shear flow
        "17_slide17_ex153b.html",          # 18 Example 15.3 (2/2): nails
        "19_slide19_outcome.html",         # 19 today's outcome
        "20_slide20_thanks.html"]          # 20 thank you, questions

BUILD_JS = """<script>
(() => {
  const els = [...document.querySelectorAll('[data-step]')];
  const last = Math.max(0, ...els.map(e => +e.dataset.step));
  let k = 0;
  const apply = (jump = false) => {
    els.forEach(e => { e.style.opacity = +e.dataset.step <= k ? 1 : 0; });
    dispatchEvent(new CustomEvent('buildstep', {detail: {k, jump}}));
  };
  apply();
  requestAnimationFrame(() => els.forEach(e => { e.style.transition = 'opacity 0.4s'; }));
  addEventListener('message', ev => {
    if (ev.source !== parent) return;
    let reply = 'ok';
    if (ev.data === 'next') { if (k < last) k++; else reply = 'end'; }
    else if (ev.data === 'prev') { if (k > 0) k--; else reply = 'start'; }
    else if (ev.data === 'all') { k = last; reply = null; }
    else return;
    apply(ev.data !== 'next');
    if (reply) parent.postMessage(reply, '*');
  });
})();
</script>
"""


def main():
    pages = []
    for name in DECK:
        html = (lib.SLIDES / name).read_text(encoding="utf-8")
        num = int(re.search(r'<div class="num">(\d*)</div>', html).group(1) or 0)   # 0 = title page
        assert html.count("</body>") == 1, f"{name}: expected one </body>"
        pages.append((num, name, html.replace("</body>", BUILD_JS + "</body>")))
    nums = [p[0] for p in pages]
    first = 0 if nums[0] == 0 else 1
    assert nums == list(range(first, first + len(pages))), f"slide numbers not 1..N: {nums}"
    total = nums[-1]                                   # show "n / total" on every numbered page
    pages = [(n, nm, h.replace(f'<div class="num">{n}</div>', f'<div class="num">{n} / {total}</div>') if n else h)
             for n, nm, h in pages]
    data = json.dumps([p[2] for p in pages]).replace("</", "<\\/").replace("<!--", "<\\!--")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RAS 215 – Chapter 15: Design of Beams and Shafts</title>
<style>
  html, body {{ margin: 0; height: 100%; background: #000000; overflow: hidden; }}
  body {{ display: flex; align-items: center; justify-content: center; cursor: pointer; }}
  #stage {{ width: 1280px; height: 720px; flex: none; transform-origin: center center; background: #ffffff; }}
  #stage iframe {{ width: 1280px; height: 720px; border: 0; display: block; pointer-events: none; }}
</style>
</head>
<body>
<div id="stage"><iframe id="view" title="slide"></iframe></div>
<script>
  const SLIDES = {data};
  const NUMS = {json.dumps(nums)};
  const view = document.getElementById('view');
  let cur = 0;

  function fit() {{
    const s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
    document.getElementById('stage').style.transform = 'scale(' + s + ')';
  }}
  function show(n, complete) {{
    cur = Math.max(0, Math.min(SLIDES.length - 1, n));
    view.onload = complete ? () => view.contentWindow.postMessage('all', '*') : null;
    view.srcdoc = SLIDES[cur];
    history.replaceState(null, '', '#' + NUMS[cur]);
  }}
  const next = () => view.contentWindow.postMessage('next', '*');
  const prev = () => view.contentWindow.postMessage('prev', '*');
  window.addEventListener('message', e => {{
    if (e.source !== view.contentWindow) return;
    if (e.data === 'end' && cur < SLIDES.length - 1) show(cur + 1);
    else if (e.data === 'start' && cur > 0) show(cur - 1, true);
  }});
  document.addEventListener('keydown', e => {{
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].includes(e.key)) next();
    else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(e.key)) prev();
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(SLIDES.length - 1);
    else if (e.key === 'r' || e.key === 'R') show(cur);
    else if (e.key === 'f' || e.key === 'F') {{
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    }} else return;
    e.preventDefault();
  }});
  document.addEventListener('click', next);
  window.addEventListener('resize', fit);
  fit();
  show(Math.max(0, NUMS.indexOf(parseInt(location.hash.slice(1)))));
</script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(pages)} slides, {OUT.stat().st_size / 1024:.0f} KB)")
    for num, name, _ in pages:
        print(f"  {num}: {name}")


if __name__ == "__main__":
    main()
