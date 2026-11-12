# Presentation guideline

How every talk from this group is designed and built, whatever the topic: a
conference talk, a class presentation, a group meeting or a defence. It
collects the rules that were worked out slide by slide for the EGR 520 talk
(project 38, November 2026), written so they apply to any subject.

Read Part A for the design rules and Part B for how the slides are built. Use
the checklist in Part C before every talk.

**Worked example.** The full EGR 520 deck and the scripts that build it are in
`projects/38_20261030_PHOENIX_EGR520_Presentation/task1_slides/`. That folder
is local-only (git-ignored), so it may not exist on every machine. Its
`scripts/02_slide_lib.py` is the shared page frame, `scripts/10_make_deck.py`
is the deck builder and each `scripts/NN_make_slide*.py` writes one slide.
The look was taken from the group's reference deck
`reference_slide/Dimensionless learning3.pptx` (Gan & Wei, ASU).

---

## Part A. Design rules

### A1. The story comes first

1. **One talk, one story.** Before making any slide, write the story as five
   to eight sentences, one per slide. Each slide answers one question and
   hands over to the next. A good order for a technical talk:

    | # | Slide | Question it answers |
    |---|---|---|
    | 0 | Title page | What is this talk, who gives it |
    | 1 | The application | What happens in the real world, why it matters |
    | 2 | The physics / the model | Which equation or idea describes it |
    | 3 | Simple answer | What the textbook (exact, analytical) answer gives |
    | 4 | Where it fails | Compared with a measurement, what is missing and why |
    | 5 | The tool | What our method or code adds |
    | 6 | How it works | The method in one picture (for example a grid of cells) |
    | 7 | What it computes | The result, shown as it happens |
    | 8 | Is it right | Comparison with an experiment, with errors |
    | 9 | Takeaway | What the analysis let us understand, predict or design |
    | 10 | Thank you | Questions, contact |

2. **About one slide per 1.5 to 2 minutes.** A 15-minute talk has 8 to 10
   content slides plus the title page and the closing page.
3. **The audience is general.** Unless told otherwise, speak to a general STEM
   audience, not to experts in the topic. Every special term is explained the
   first time, in plain words. If a plain word exists, use it.
4. **Each slide ends with a goal line** (see A3) that says what the slide
   showed or what comes next, so the slides join up into one chain.
5. **Slides refer to each other by number** ("slide 4", "the run of slides
   7-8"). When a slide is added or moved, update every such reference and
   every page number. A title page has no number, so adding one does not
   shift the others.
6. **Depth over breadth.** One or two well-chosen equations, figures or
   examples per slide. Leave out everything that does not serve the story.

### A2. Page

| Item | Value |
|---|---|
| Size | 16:9, built as a 1280 x 720 px page (= 13.33 x 7.5 in at 96 px/in); the page is scaled to fit any screen |
| Background | plain white (title and closing page: washed-out photo, see A12) |
| Left margin | 48 px; content right edge at 1232 px |
| Title | top 16 px |
| Content area | from about 104-120 px (below the title) to about 630 px |
| Goal line | top about 640-664 px |
| Source / note line | top 698 px, bottom left |
| Page number | bottom right, 16 px from the right, 8 px from the bottom |
| Logo | top right, 22 px from the right, 10 px from the top, 92 px high |

- Everything sits on this grid. Left edges of text blocks and figures line up
  at 48 px or at a clear column edge.
- Leave no big empty areas, but never let two items touch. Keep at least
  8-10 px between neighbouring items and between text and a frame.
- No title bar, no coloured background bands, no footer text other than the
  source line and the page number.

### A3. Fixed parts of every content slide

- **Title** (top left): Arial, bold, navy `#002060`, 40 px, line height 1.12.
  It may take two lines. Prefer a **statement** that gives the point of the
  slide ("One equation tells us where the metal melts: the heat equation")
  over a bare topic ("Heat equation"). The single key word or phrase is in
  **red italic** `#C00000`.
- **Logo** (top right): the ASU logo as a PNG with a **transparent**
  background, so it also sits cleanly on photos. Never a JPEG with a white
  box.
- **Page number** (bottom right): 16 px, black.
- **Goal line** (bottom left, above the source line): one sentence, 21-22 px,
  bold italic red. It states what the slide showed ("Exact, but only for a
  simplified problem: the depth comes out 40 % too small") or leads to the
  next slide ("Next: how it solves the heat equation on a grid of cells"). It
  is always the last thing revealed on the slide.
- **Source / note line** (bottom left, 12-13 px, italic, grey `#555555`):
  where borrowed data come from, and "Schematic, not to scale" for drawings.

### A4. Text

| Use | Size | Style |
|---|---|---|
| Title | 40 px | bold navy, key word red italic |
| Lead sentence under the title | 20-24 px | regular, black |
| Bullet points | 18-22 px | black, line height 1.3-1.4, 4-6 px between items |
| Block heading (the point of a group of bullets) | 19-24 px | bold black |
| Column / panel heading | 18-20 px | bold black, with a bold panel letter `a.` / `(a)` |
| Table text | 17-20 px | regular; header bold with a 1.5 px rule under it |
| Labels inside figures | 14-16 px | regular or bold |
| Secondary notes, captions | 14-15 px | grey `#555555`, italic for remarks |
| Source line | 12-13 px | italic grey |
| Smallest text anywhere | 11-12 px | only for tiny sketch labels |

- **Little text.** At most about five bullets of one or two short lines each.
  Group bullets under a bold heading when there are two groups.
- **Short sentences, one idea each.** Plain, everyday words. No stacks of
  nouns ("the wrong-physics contamination path"); write a sentence instead.
- **Body text is black.** Grey is only for secondary remarks, captions and
  the source line.
- **Explain every symbol once**, either in a small "Symbols" list beside the
  equation or in a "What each symbol means" block. Symbols are listed in a
  fixed-width grid (symbol column about 34-70 px, text after it) with fixed
  row heights, so lines never crowd.
- **Lists of numbers** ("Numbers used") are a two-column grid: grey label on
  the left, value on the right, fixed row height (about 29 px).
- Units always written: "0.96 m/s", "140 µm", "1571 K". Use the same units
  for the same quantity on every slide.
- Names of people and the course are written in full on the title page; a
  name is never shortened differently on different slides.

### A5. Colour

One emphasis colour, one structure colour, and fixed colours for the things
that appear on many slides.

| Role | Colour |
|---|---|
| Titles, headings of tables, structure lines, "what our method does" | navy `#002060` |
| The **only** emphasis colour: key words, warnings, limits, goal line, red braces and outlines | red `#C00000` |
| Body text | black `#000000` |
| Secondary text | grey `#555555` |
| Light rules in tables | `#c9ccd1` / `#d5d8dc` |
| Laser / energy input in drawings | orange-red `#e8481c` (gradient cone, light at the top) |
| Cold solid in drawings | grey-blue `#c9d3df` |
| Hot / molten in drawings | orange `#f39a3c`, liquid yellow `#f6c35a` |
| Powder | warm grey with grains |
| Temperature fields from data | `inferno` colour map, one fixed scale for the whole talk |
| Schematic temperature (made-up fields) | cool grey-blue → yellow → orange → dark red |

- **Keep a colour's meaning across the talk.** If light blue is "our model's
  edge" on one slide, it is that on every slide. A third model in a
  comparison gets its own colour, kept everywhere (for example green
  `#2fd36a` for the textbook solution), and its row in a table uses the same
  colour.
- Limitation / warning boxes: red 2 px border, light red fill `#fbecec`,
  rounded 6 px, red heading.
- Never use colour alone to carry a meaning that is not also written in a
  label or legend.

### A6. Emphasis devices

- **Key phrase in text:** red, bold, italic (optionally underlined).
- **Name the parts of an equation:** a red brace (2.5 px, rounded corners)
  under each term, a red bold label under the brace ("Heat stored") and one
  plain line under it ("how fast the metal heats up"). Reveal the terms one
  per click.
- **Point at a part of a figure:** red arrow plus a short red bold label.
- **Highlight one item:** thin red rectangle around it, no fill; or a red
  dashed outline around part of a drawing.
- **Numbered marks on a drawing** (circled ① ② ③, 12 px radius) with a key
  under the drawing, coloured red for what matters most and navy for the rest.
- **Limits of a method:** the red "Why it misses" box: two or three bullets
  with the limits in bold red, then one bold closing line under a thin rule
  that says the consequence ("... it can no longer be solved exactly. We have
  to solve it numerically.").

### A7. Equations

- Write equations as real maths (MathML in HTML, native equations in
  PowerPoint), never as pictures and never as plain text.
- Embed the maths font in the page (Latin Modern Math as a data URI) so
  formulas look the same in every browser. Wrap each formula in a plain block
  for layout; do not set flex layout on the maths element itself.
- **One main equation per slide**, large (about 50 px), centred, with its
  number "(1)" to the right. Its terms are named with red braces (A6).
- **Derivations** are numbered steps. Each step has a bold one-line heading
  saying what is done ("Ride with the laser: ...") and, in grey italic, the
  tool used ("change of variables, chain rule"). Under it, one to three
  equation lines at about 21 px. Short plain sentences between lines say what
  is put into what.
- **Nothing may silently disappear.** If a term of the main equation is
  dropped or moved (for example a source term that becomes a boundary
  condition), say so on the slide where it happens and point to the step
  where it comes back.
- Use the same symbols on every slide. Symbols in a sentence are written in
  italics like the maths ($T$, $k$, $c_p$).
- The final result of a derivation sits in a red-framed box with its name and
  year ("Rosenthal (1946)").

### A8. Figures and plots

- **Matplotlib with the group style** `code_base/toolbox/phoenix.mplstyle`
  (its own STIX font; do not override it with Arial inside plots).
- **Size the figure for its place on the slide.** Work in page pixels: with
  `dpi = 100`, one figure inch is 100 page px, so the style's point sizes read
  as on paper. Save the PNG at twice that (`dpi = 200`) for a sharp page.
  Never stretch or squeeze a figure on the slide.
- **Exact size matters:** when the picture must keep its shape, turn off the
  tight crop (`savefig.bbox = "standard"`). A tight crop changes the picture's
  shape when a panel changes, and then it overlaps the text under it.
- **Stacked panels that share an axis are aligned**: same left edge, same
  width, ticks under each other. With an equal-aspect panel, draw once, call
  `apply_aspect()`, then set the other panel's position to the same x and
  width.
- **Axis labels:** quantity, then unit in brackets: "Temperature (K)",
  "Depth (µm)". Symbols in LaTeX maths.
- **Panel letters:** "(a)", "(b)" as left-aligned panel titles, or bold `a.` /
  `b.` for HTML/SVG panels. Letters follow the order in which panels appear
  on screen.
- **Direct labels** next to lines when there are about five lines or fewer;
  no legend on top of data. A legend that would cover data moves outside the
  plot area (above or below it).
- **Reference values as lines:** a melting point as a dotted black line with a
  short label at the end where the data are cold. Labels never touch a curve.
- **Comparison with experiment:** the experiment and the model in one
  picture, split down the middle (experiment left, model right), with the
  model's outline drawn dashed on the experiment and solid on the model. A
  second model gets its own line style and colour across both halves.
- **Brighten dark micrographs** (contrast stretch and gamma) so the feature
  that matters is clearly visible; say in the script how it was done.
- **Tables of results:** measured value first, then each model; after each
  model value its signed error in brackets, $(\text{model} - \text{measured})/\text{measured}$
  in percent ("145 (+4 %)", "83 (−41 %)"), with a caption that defines the
  error. If two models used different input values, write that on the slide.
- **Show only what supports the story.** A run that was only a step on the
  way (a wrong parameter, a failed attempt) stays off the slides unless the
  failure is the point.
- **Every plotted quantity comes from a saved file** (table, `.npz`, log);
  the script names it in its docstring. Nothing is re-computed by hand.

### A9. Drawings and sketches

- Drawings are inline SVG made by the slide script, in the colours of A5.
- **Schematic drawings say so**: "Schematic, not to scale" or "Panel b:
  schematic temperature, not a simulation result" in the source line.
- **Physically correct, even when schematic.** Examples learned the hard way:
  metal that melted and froze stays visible as a solidified track; a powder
  bed is a solid block (top, front and side faces), not an empty box; a flat
  part is printed lying flat, layer after layer of its full outline; holes in
  a part are holes, not a different shade.
- **A small sketch beside each line of text** helps more than a big diagram
  when a slide lists several ideas: one 120 x 66 px sketch per table row
  (a heated volume under a beam, a rising line against a flat dashed one,
  solid → $+L$ → liquid, flow loops in a pool).
- **Use a fixed visual vocabulary**: laser = gradient cone (light at the top)
  with a bright spot; heat flow = thick grey block arrows with orange dots
  moving along them; pool edge = red line; cut planes and links between views
  = dashed lines.
- **Multi-view figures**: a 3-D view first, then the 2-D views taken from it
  (top view, cross section). The cutting plane is drawn dashed in the 3-D view
  and dashed lines join it to the 2-D view it produces.
- When a technical drawing is unwanted (the audience asked for plain text),
  state the point cleanly in words instead. Do not force a picture.

### A10. Animation

Animation is for explaining a process, never for decoration alone.

- **Animate a process when the process is the point**: heat flowing in and
  out of a small cube, a pool opening and freezing, a printer spreading
  powder and scanning, a result field moving with the laser.
- **Tell it as a story.** The animation follows the spoken order: each phase
  has a status line in grey italic ("laser on: the metal heats up", "laser
  gone: heat spreads, the pool solidifies from its edge").
- **Calm speed.** One event every 0.5-1.5 s; a pause of 1.5-5 s at the end
  before it loops. Ease in and out (smoothstep) instead of jumps. Values that
  change in steps (layer height, powder level) rise smoothly.
- **Smooth playback from data.** Result animations play the saved frames of a
  real run and blend neighbouring frames, so motion is smooth; curves are
  drawn up to the current time with a time cursor.
- **Start on reveal.** An animation starts from its beginning when the click
  that shows it happens, not when the slide loads.
- **Freeze for checking.** Every animated slide accepts `?t=SECONDS` in its
  address to show one fixed moment; this is how still pictures are checked.
- Illustrative animations (not simulation output) say so in the source line
  or the script docstring.

### A11. Click-by-click build-up

- **Nothing appears before its click.** The slide opens with the title only
  (plus fixed parts). Every figure, text block and table is revealed by a
  click, including the main picture.
- **A picture appears together with the words that explain it.** The term of
  an equation and the part of the drawing that shows it come with the same
  click (heat stored → the cube warms; heat conducted → the arrows; laser
  heat → the laser).
- **One idea per click**; usually four to eight clicks per slide; the goal
  line is the last click.
- **Back goes back** one click at a time; going back into the previous slide
  shows it complete.
- Slides that tell a step-by-step method (for example the sweeps of a solver)
  can pause their animation at each click, so the speaker controls the pace.

### A12. Title page and closing page

**Title page** (no page number):

- Full-page campus photo washed with 68 % white, logo top right.
- Title in navy bold (about 38 px, two lines allowed) starting about 170 px
  from the top; under it a "**-** subtitle" line in navy regular (about 30 px)
  that names the parts of the story.
- For a course presentation, the title follows the assignment's wording
  (for example "Using Differential Equations to Model Heat Transfer in ...").
- Presenter block: **full name** (30 px bold), then role, school, university
  and "Email: ..." each on its own line (22 px). People from the same school
  are not repeated: the school is written once.
- The advisor / PI on one small grey line (18 px) under the presenter block
  ("PI: Dr. Zhengtao Gan, Assistant Professor").
- Event line at the bottom left ("EGR 520 class presentation, Fall 2026").
- Optional: a small, calm, physically correct animation in the empty space
  right of the name block (for example a laser powder bed printer building
  the logo), with no text under it.

**Closing page** (numbered, last slide):

- Same washed photo; "**Thank you!**" (about 88 px, navy bold), "*Questions?*"
  under it (about 48 px, red bold italic), then name, school and university,
  and email.

### A13. Honesty on the slides

- Every borrowed figure or number has its source on the same slide (source
  line or caption).
- Simulation results, measurements and schematic drawings are always told
  apart in words.
- If two compared models used different inputs, the slide says so.
- Numbers on the slides come from the saved output, and the same number has
  the same value on every slide.
- A limitation is stated plainly, not hidden.

---

## Part B. How the slides are built

### B1. Files

- One project folder per talk, following the project rules in `CLAUDE.md`
  (`projects/NN_YYYYMMDD_NAME/task1_slides/` with `scripts/`, `fig/`,
  `slides/`). Files are numbered in creation order.
- **One Python script per slide** writes one self-contained HTML page into
  `slides/separate/`. The page needs no external file: images and fonts are
  inlined as data URIs, drawings are inline SVG, animation code is inline.
- **A shared library** (`02_slide_lib.py` in the example) holds the colours,
  fonts, the logo (cut from the reference deck and made transparent), arrow
  markers, the label helper and `write_page(...)`, which wraps a slide body in
  the common frame (title, logo, page number, scaling to the window).
- **A deck builder** (`10_make_deck.py`) lists the slides in talk order,
  checks that the page numbers run 1, 2, 3, ... (an unnumbered title page may
  come first), and writes one deck file that shows each slide in its own
  frame.
- **Each figure has its own script** that reads saved data and writes a PDF
  and a PNG, so the figure can be re-made in one command.

### B2. Deck behaviour

- Keys: → / Space / Page Down / click = next; ← / Page Up = back; Home / End;
  F = full screen; R = restart the current slide; `#N` in the address opens
  slide N.
- Elements marked `data-step="N"` stay hidden until the N-th click on that
  slide and fade in (0.4 s). After the last step, "next" goes to the next
  slide.
- The deck tells each slide which step is showing (a `buildstep` event), so a
  slide can restart or pause its animation at a given click.
- A slide shown on its own (not in the deck) shows everything, which is handy
  for checking.

### B3. Layout techniques that avoid surprises

- Absolute positions for the big blocks (figures, columns, goal line), so the
  layout is the same on every screen.
- Inside a text column, blocks **follow each other in the page flow** with
  fixed gaps, and grids use **fixed row heights**. Maths fonts have different
  line heights in different browsers; fixed rows stop a taller formula from
  pushing one block onto another.
- A class name used for a slide element must not clash with a class of the
  common frame (the frame uses `title`, `logo`, `num`, `note`, `fig`, `key`,
  `em`).
- Live fields (animations from data) are drawn on a canvas exactly under the
  plot area of a transparent matplotlib PNG that carries the axes, so axes,
  labels and fonts stay matplotlib's.

### B4. Checking

1. Re-build the slide and the deck.
2. Render a still picture of the slide in a headless browser
   (`google-chrome --headless=new --window-size=1280,720 --screenshot=...`);
   for animated slides render two or three moments with `?t=SECONDS`.
3. To check something that is hidden at the end of a slide (for example text
   under a picture that covers it later), render a copy with that picture
   hidden.
4. **Look at every picture** and fix overlaps, clipped text, labels touching
   lines, legends on data, and text running past the page edge.
5. Click through the whole deck once in a real browser: real-time playback,
   font differences and click order cannot be checked headless.
6. Write in the project `log.md` what changed and what was checked; write
   what was **not** checked too.

### B5. Other formats

The HTML deck is the master. A PowerPoint copy (native shapes and equations,
animated GIFs for moving parts) can be built from the same content when a
`.pptx` is required; rebuild it after the last change to the HTML, because it
does not update itself.

---

## Part C. Checklist before the talk

**Story**

- [ ] The story is written as one sentence per slide, and each slide answers
      one question.
- [ ] Every slide ends with a goal line that joins it to the next.
- [ ] Every special term is explained the first time, in plain words.
- [ ] Slide references ("slide 4") and page numbers are right after the last
      change.

**Each slide**

- [ ] Title is a statement, key word red italic, at most two lines.
- [ ] Nothing shows before its click; each picture comes with the words that
      explain it; the goal line is last.
- [ ] At most about five bullets; body text black; sizes as in A4.
- [ ] Red is the only emphasis colour; colours mean the same on every slide.
- [ ] Equations are real maths; every symbol is explained once; no term
      disappears without a word.
- [ ] Figures in the group style, sized for the slide, axes labelled with
      units, stacked panels aligned, no legend on data.
- [ ] Schematic drawings and illustrative animations are labelled; drawings
      are physically correct.
- [ ] Sources of all borrowed numbers and figures are on the slide.
- [ ] Comparison tables show signed percent errors, and any difference in
      inputs between models is stated.

**Title and closing pages**

- [ ] Title follows the event or assignment wording; full name, role,
      school, university, email; PI line; event line.
- [ ] Closing page with "Thank you!", "Questions?" and contact.

**Build and check**

- [ ] Every slide and the deck rebuilt from the scripts.
- [ ] Still pictures of every slide (and of two or three moments of each
      animation) looked at; no overlaps or clipped text.
- [ ] Whole deck clicked through once in a real browser, in full screen.
- [ ] `log.md` updated, including what was not checked.
