# Slide style guide

Taken from the reference deck
`reference_slide/Dimensionless learning3.pptx` (Gan & Wei, ASU). Every slide
in this talk follows these rules. Numbers below were read from the deck's
XML, not guessed.

## 1. Look in one line

White page, big navy bold title at the top left, ASU logo at the top right,
the slide filled mostly by figures, a few short bullet points, key words in
red italic, the reference in small underlined italic at the bottom.
No title bar, no coloured background, no footer text.

## 2. Page

| Item | Value |
|---|---|
| Size | 16:9, 13.33 x 7.5 in |
| Background | plain white |
| Font | Arial everywhere (text); Cambria Math for maths |
| Margins | left edge of text 0.6-0.67 in; right edge ~12.7 in |

## 3. Fixed parts on every slide

- **Title**: Arial, **bold**, navy `#002060`, 36 pt; 28-32 pt when it needs
  two lines. Box at x = 0.67 in, y = 0.19 in, left aligned, top of the page.
  - A title is either a short topic (`Ex1: Turbulent Rayleigh-Bénard
    convection`) or a full statement (`Symmetries lie at the heart of the
    laws of nature`). Prefer the statement: it tells the audience the point.
  - The key word may be in red italic bold `#C00000`
    (`*Symmetry* is the property that ...`). Text after a dash (`- any
    physical law must ...`) may be smaller (24 pt).
- **ASU logo**: top right, x = 11.88 in, y = 0 in, 1.45 x 1.09 in (file
  `ppt/media/image5.jpeg` inside the reference deck). Left out when a figure
  needs the corner.
- **Slide number**: bottom right corner, Arial 12 pt, black. Nothing else in
  the footer.

## 4. Text

| Use | Size | Style |
|---|---|---|
| Lead sentence under the title | 24 pt | regular, black |
| Bullet points | 20 pt (24 pt if few) | black, `•` bullet; sub-level `–` or `•` indented |
| Bullet heading (the point of a group) | 20 pt | **bold** black, e.g. **Dimensionless learning** |
| Sub-heading over a column | 18-20 pt | **bold italic red** `#C00000`, ends with `:` |
| Labels inside figures | 14-16 pt | regular or bold black |
| Reference / source | 11-14 pt | *italic, underlined*, dark grey `#222222` |

- Little text. A slide has at most ~5 bullet points of one or two short
  lines each. Often the bullets are spaced apart in groups (blank line
  between groups).
- Black text, no grey body text.

## 5. Emphasis

- One colour for emphasis: red `#C00000`.
- Key phrase in running text: ***red, bold, italic, underlined***
  (`fundamental azimuthal *rotational invariance*`).
- Highlight one item in a list or figure: thin red rectangle around it
  (no fill), or a red dashed box around a part of a diagram.
- Red arrow + short red bold label to point at a part of a figure or an
  equation term (`Orbit direction`, `Polynomial functions`).
- A speech bubble (light blue fill, black outline) for a quote from a
  person, used once at most.

## 6. Equations

- Native PowerPoint equations (Cambria Math), never pictures of maths.
- Display equations stand on their own line, centred under the bullet that
  introduces them (`Rediscover Rayleigh number:` then the formula).
- Symbols in a sentence are inline maths too ($Re < 2000$).
- One or two equations per slide. Name the parts with red labels and
  arrows rather than with extra text.

## 7. Layout

Figures carry the slide; text explains them. Common layouts in the deck:

1. **Figure left, bullets right** (most used): figure block ~60 % width on
   the left, bullet list ~40 % on the right, reference under the bullets.
2. **Two columns of evidence**: each column has a red bold italic
   sub-heading, an image, a one-line source under it; columns split by a
   thin dashed grey vertical line.
3. **Bullets with equations**: full-width bullet list, each bullet followed
   by its centred equation.
4. **One big diagram**: a flow chart of rounded boxes with soft fills
   (light blue, light green, light red, yellow), dark outline, block arrows,
   numbered module names (`1. Data Preprocessing Module`).

- Multi-panel figures use bold lower-case panel letters `a.`, `b.`, `c.`
  at the top left of each panel.
- A portrait or photo gets a caption: **name** in bold, years in regular
  (`**G. I. Taylor** (1886-1975)`).
- Items line up on a clean grid; figures fill the space, little empty white.

## 8. Sources

- Every borrowed figure or number has its source on the same slide: short
  citation or URL, 11-14 pt italic underlined, directly under the figure or
  at the bottom left.
- Last slide: summary picture on the left, `Selected References:` list
  (14 pt, `•` bullets) on the right.

## 9. Our own rules on top of the reference

- All figures we make use `code_base/toolbox/phoenix.mplstyle`, sized for
  their real width on the slide (no stretching).
- Schematic pictures are labelled `Schematic, not to scale`.
- Build each slide with a script (python-pptx, native shapes and native
  equations), then render a PNG preview with LibreOffice and check it for
  overlaps and clipped text before showing it.
