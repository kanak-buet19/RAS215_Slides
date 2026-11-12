# RAS 215 — TA teaching slides

Lecture slides I make as TA for RAS 215, built from the course textbook.

## Source material

- Textbook: R. C. Hibbeler, *Statics and Mechanics of Materials*, 6th ed. (Pearson).
- `Hibbler ch 15.pdf`: 7 phone photos of Ch 15 "Design of Beams and Shafts", pp. 687–697 (15.1, 15.2, Examples 15.1–15.3).
  - p. 687 (objectives and the 15.1 intro) is too blurry to read.
  - 15.3 and 15.4 are not in the photos.
- Use only what is in the source pages. If something comes from outside them, say so on the slide or to me. Never make up textbook numbers.
- Every equation, number and example result on a slide must match the book. Give the source page on the slide (e.g. "Hibbeler, 6th ed., Ex. 15.2, p. 695").

## Slide design

The Ch 15 deck was built following every instruction in this file and the two style guides in `docs/`:
- `docs/presentation-guideline.md`: design rules (look only, not storytelling)
- `docs/slide_style.md`: visual reference

Both are copied from the PHOENIX project. The rules are implemented in `ch15/scripts/01_slide_lib.py`, the shared page frame.

- Use the **look** from `docs/presentation-guideline.md`:
  - page grid, fonts and text sizes, colours, title style
  - equations, figures and drawings
  - click-by-click reveal
  - title and closing pages
  - build method (Part B)
- **Do not** use its storytelling rules: no A1 story order, no goal-line chaining between slides. Structure each lecture the way a class needs it, following the textbook's section order:
  1. concept
  2. key equation(s)
  3. procedure
  4. worked examples
- Template code to reuse: `/Users/rakibul/work/Research/PHOENIX/projects/38_20261030_PHOENIX_EGR520_Presentation/task1_slides/`
  - `scripts/02_slide_lib.py`: shared frame
  - `scripts/10_make_deck.py`: deck builder
  - `slide_style.md`: visual reference (copy in `docs/slide_style.md`)
- Audience: undergraduate engineering students. Define every symbol once. Show worked examples step by step, one step per click.
- Redraw textbook figures (beams, loads, cross sections, V and M diagrams) as SVG. Don't paste photos of the book.

## Presentation style (as used in the Ch 15 deck)

Visual-first rules (animate the physics, compute from the real equations, link the views) are in `ch15/plan.md`. Title, click and symbol rules are in `docs/presentation-guideline.md`. Added on top of those:

- **Equations:**
  - General form first, then the numbers.
  - Each equation is labelled **Compute** (navy) or **Check** (red).
  - Show a symbol in the figure, e.g. *s* drawn as the gap between two nails.
- **Maths rendering:** equations are hand-written MathML in the Python scripts, drawn natively by the browser, with the STIX Two Math font embedded (`math_font_css()` in `01_slide_lib.py`).
  - Possible but not used:
    - Latin Modern Math (the LaTeX font) for a LaTeX look
    - KaTeX/MathJax to write LaTeX source
- **Simplifications:** grey out what a simplification replaces, e.g. the distributed load fades while its resultant is shown.
- **Failures:** shown as a boxed red **FAILS**.
- **Naming:**
  - R_Ay, R_By, R_Dy for vertical reactions
  - R_Ax = 0 shown at pins (ΣF_x = 0)
  - pin + roller supports drawn correctly
- **Colour meaning, kept on every slide:**
  - σ navy
  - τ green
  - σ_y purple
  - red only for emphasis
- **Fixed pages:**
  - Title page:
    - photo background
    - date on its own row
    - TA name, role, school
    - email as a blue link
    - PI line last, smaller
  - "Today" slide at the start
  - "Today's outcome" slide before the end, mirroring "Today"
  - "Thank you! / Questions?" closing page
  - page numbers as "n / total"
- **Tone:**
  - Professional, neutral wording, e.g. "design for bending: select the section".
  - No first person.
  - Bottom note: one grey line, never wraps; it gives the source page and what is schematic, exaggerated or not from the text.
- **Layout:**
  - Cut bullets before shrinking text.
  - Columns are clearly separated and aligned.
  - Labels never overlap arrows, cut lines or the page number.

## Files

One folder per chapter, e.g. `ch15/`, with:
- `scripts/`: one script per slide, plus the lib and the deck builder
- `fig/`
- `slides/`

## Working rules

- Never build, render or run anything yourself. Write the scripts, then give me the exact commands to build the deck and render previews.
