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

**Visual first**
- Every idea and every problem step gets a picture or animation. Words support the picture.
- Animate the physics: the load goes on, the beam bends, stresses grow, the cut moves.
- Compute every animation from the real equations, never hand-drawn shapes:
  - σ = My/I and τ = VQ/It
  - the elastic curve
  - V and M by the method of sections
- Only the deflection may be exaggerated, and the slide says so.
- Stress arrows scale with the stress, so "σ ≫ τ" can be seen.
- Link the views: a point on the beam, its stress element and its spot on the plot light up together.
- Each example step points at its part of the figure: reactions on the FBD, the peak on V/M, the area for Q shaded, the nails drawn at spacing *s*.
- Failures and checks are shown, not only stated:
  - a boxed red **FAILS** next to the redesign
  - an OK bar staying under the allowable line

**Click by click**
- One idea per click; worked examples go one step per click.
- Animations run step by step on clicks rather than as unexplained loops.
- When a simplification is in play, grey out what it replaces. Example: the distributed load fades while its resultant is shown.

**Equations**
- General form first, then the numbers.
- Label each equation's role as **Compute** (navy) or **Check** (red).
- Define every symbol the first time it appears, including words like "prismatic". Show what a symbol is in the figure, e.g. *s* drawn as the gap between two nails.
- Use one naming scheme everywhere:
  - R_Ay, R_By, R_Dy for vertical reactions
  - R_Ax = 0 shown at pins (ΣF_x = 0)
  - pin + roller supports drawn correctly

**Colour meaning, kept on every slide**
- Navy: titles, structure, bending stress σ
- Green: shear stress τ
- Purple: σ_y
- Red: the single emphasis colour (key word, failures, checks)

**Structure**
- Title page:
  - photo background
  - lecture date on its own row
  - TA name, role, school, email as a blue link
  - PI line last, smaller
- "Today" slide at the start.
- "Today's outcome" slide before the end, mirroring "Today" with the key equations and sections.
- "Thank you! / Questions?" closing page.
- Slide numbers shown as "n / total".

**Tone**
- Titles are statements, with the key word in red italic.
  - Example: "Example 15.2 (2/2): the bending design fails in shear".
- Professional, neutral wording:
  - "design for bending: select the section", not "size a beam"
  - no first person, no "my code", no "made up"
- Bottom note: one grey line, never wraps, with:
  - the source and page
  - what is schematic or exaggerated
  - anything not from the textbook

**Layout**
- Uncluttered: cut bullets before shrinking text.
- Columns are clearly separated (dashed dividers or spacing) and aligned.
- Labels never overlap arrows, cut lines or the page number.

## Files

One folder per chapter, e.g. `ch15/`, with:
- `scripts/`: one script per slide, plus the lib and the deck builder
- `fig/`
- `slides/`

## Working rules

- Never build, render or run anything yourself. Write the scripts, then give me the exact commands to build the deck and render previews.
