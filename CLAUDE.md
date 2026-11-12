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

- Use the **look** from `/Users/rakibul/work/Research/PHOENIX/docs/presentation-guideline.md`:
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
  - `slide_style.md`: visual reference
- Audience: undergraduate engineering students. Define every symbol once. Show worked examples step by step, one step per click.
- Redraw textbook figures (beams, loads, cross sections, V and M diagrams) as SVG. Don't paste photos of the book.

## Files

One folder per chapter, e.g. `ch15/`, with:
- `scripts/`: one script per slide, plus the lib and the deck builder
- `fig/`
- `slides/`

## Working rules

- Never build, render or run anything yourself. Write the scripts, then give me the exact commands to build the deck and render previews.
