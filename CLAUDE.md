# RAS 215: TA lecture slides (template)

I make these lecture slides as the TA for RAS 215, built from the course textbook. Each lecture is one case of this template. The first finished case is Ch. 15 (see the end). For a new lecture, follow this file and copy `ch15/scripts/` as the starting code.

## 1. Source rules

- **Textbook:** R. C. Hibbeler, *Statics and Mechanics of Materials*, 6th ed. (Pearson).
- **What counts as source:** only the pages listed in that lecture's case section below.
  - Anything from outside those pages is flagged, on the slide or to me.
  - Never make up textbook numbers.
- **Matching the book:** every equation, number and example result matches the book.
- **Citations:** every slide cites its page, e.g. "Hibbeler, 6th ed., Ex. 15.2, p. 695".
- **Figures:** textbook figures are redrawn as SVG. No photos of the book.

## 2. Design

- **The look** comes from `docs/presentation-guideline.md`, Part A2–A13 plus Part B, and `docs/slide_style.md`. Both are copied from the PHOENIX project.
- **Not used:** the guideline's storytelling (A1: story order, goal-line chaining).
- **Order:** each lecture follows the textbook's section order:
  1. concept
  2. key equation(s)
  3. procedure
  4. worked examples
- **Audience:** undergraduate engineering students.

### Fixed pages
- **Title page:**
  - photo background
  - lecture title
  - date on its own row
  - TA name, role, school
  - email as a blue link
  - PI line last, smaller
- **"Today" slide** first.
- **"Today's outcome" slide** before the end: it mirrors "Today" and lists the key equations and sections.
- **Closing page:** "Thank you! / Questions?"
- **Page numbers:** "n / total" (the deck builder adds the total).

### Visuals
- Every idea and every example step gets a picture or animation. Words support it.
- Animations are computed from the real equations, never drawn by hand.
- Only magnitudes that can't be seen (e.g. deflection) are exaggerated, and the note says so.
- Stress arrows scale with the stress.
- Views are linked: a point on the part, its element and its spot on the plot highlight together.
- Each example step points at its part of the figure, e.g. reactions on the FBD, the peak on V/M, the area used for Q.
- Every symbol is shown in the figure, e.g. *s* drawn as the gap between two nails.
- A simplification greys out what it replaces, e.g. the distributed load fades while its resultant is shown.
- Failures get a boxed red **FAILS**, next to the fix.

### Clicks
- One idea per click.
- Worked examples go one step per click.
- Animations advance on clicks instead of unexplained loops.

### Equations
- General form first, then the numbers.
- Each equation is labelled **Compute** (navy) or **Check** (red).
- Every symbol is defined once, including words like "prismatic".
- **How they are drawn:** hand-written MathML in the Python scripts, rendered natively by the browser.
  - The STIX Two Math font is embedded (`math_font_css()` in `01_slide_lib.py`).
  - Possible but not used: Latin Modern Math for a LaTeX look, or KaTeX/MathJax to write LaTeX source.

### Consistency
- **Colour meaning** stays the same on every slide:
  - σ navy
  - τ green
  - σ_y purple
  - red only for emphasis
- **One naming scheme** everywhere:
  - R_Ay, R_By for vertical reactions
  - R_Ax = 0 shown at pins
- **Supports:** pin + roller, drawn correctly.

### Tone and layout
- Titles are statements, with the key word in red italic.
- Wording is professional and neutral: no first person, no "my code", no "made up".
- The bottom note is one grey line that never wraps. It gives:
  - the source page
  - what is schematic or exaggerated
  - what is not from the text
- Cut bullets before shrinking text.
- Columns are clearly separated and aligned.
- Labels never overlap arrows, cut lines or the page number.

## 3. Files and build

One folder per lecture, `chNN/`:
- `scripts/01_slide_lib.py`: the shared page frame:
  - colours, logo, page number
  - `write_page`, `sym`
  - `revealClock`, `elasticCurve`
- `scripts/NN_make_slideK_*.py`: one script per slide. Each writes `slides/separate/*.html`.
  - Elements with `data-step="N"` appear on click N.
  - `?t=SECONDS` freezes an animation for previews.
- `scripts/90_make_deck.py`: joins the slides in its `DECK` list into one self-contained `slides/<Course>_ChNN_<Title>.html`. It checks that the numbering runs 1..N.
- `plan.md`: the slide plan.
- `log.md`: a dated change log.
- Shared images go in `assets/` at the repo root.

Build (from `chNN/scripts/`):
```
python3 NN_make_slideK_*.py      # each changed slide
python3 90_make_deck.py          # the deck
```
Preview one slide:
```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --window-size=1280,720 --virtual-time-budget=5000 --screenshot=out.png ../slides/separate/<slide>.html
```

## 4. Working rules

- Never build, render or run anything yourself. Write the scripts, then give me the exact commands.
- Log every change in `chNN/log.md`.

## Case: Ch. 15, Design of Beams and Shafts (Nov 12, 2026)

- **Source:** `Hibbler ch 15.pdf`, 7 phone photos of pp. 687–697 (15.1, 15.2, Examples 15.1–15.3).
  - It is kept out of git.
  - p. 687 is too blurry to read.
  - 15.3 and 15.4 are not in the photos.
- **Deck:** `ch15/slides/RAS215_Ch15_Design_of_Beams_and_Shafts.html`, 20 numbered slides plus the title page.
