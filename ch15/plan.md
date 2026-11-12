# Ch 15 slides — plan

The lecture is 75 min long and covers Hibbeler 6th ed. **15.1–15.2** (pp. 688–697), the pages in `Hibbler ch 15.pdf`. The look follows the PHOENIX guideline (design only). The order follows the textbook.

There are about 18 numbered slides plus the title page. Theory runs to about 25 min, the examples about 40 min, and wrap-up and questions about 10 min.

Every slide gets a statement title with its key word in red italic. Items appear one click at a time, and each slide has a source line with the book page. Figures are redrawn as SVG.

## Main rule: every idea is something students can see
Every concept and every problem step comes with a visual that makes it obvious, not just text and equations. A good illustration or animation comes first; words support it.
- **Animate the physics.** A load is applied, the beam bends, the stresses grow, an element rotates to its principal directions, a beam buckles sideways. Use a calm loop or step it by clicks.
- **Compute from the real equations.** Stress profiles, stress trajectories and deflection come from the textbook formulas (σ = My/I, τ = VQ/It, the elastic curve), not hand-drawn shapes. Exaggerate only the deflection, and say so on the slide.
- **Link the views.** A point on the beam ↔ its stress element ↔ its place on the stress plot. Pick one and the matching parts light up together.
- **Show stresses as arrows that scale with their size.** Make arrow length proportional to the stress, so "σ_x ≫ σ_y" can be seen.
- **Show what each number refers to.** In the examples, each step points at its part of the figure: the reactions on the FBD, the peak on the V/M diagram, the area used for Q shaded on the section, the nails drawn at their spacing.
- **Show diagrams being built.** V and M diagrams are drawn from left to right in step with a cut that moves along the beam.
- **Animate failures and checks.** "Fails in shear" shows the section too small next to the redesigned one. "OK" shows the stress bar staying under the allowable line.

## Revised plan (75-min cut, agreed in class prep)
The original table below listed 23 slides, too many for 75 min. Current deck:

| # | Slide | Status |
|---|---|---|
| 0–8 | title, today, 15.1 theory (bending, shear, element, strength, section, trajectories, limits) | done; keep 5 and 7 short |
| 9 | Size for bending first: S_req'd = M_max/σ_allow | done |
| 10 | Three ways to get a bigger S | done |
| 11 | Design procedure, one slide (replaces old 10–13) | done |
| 12 | Ex 15.1, one slide | done |
| 14 | Ex 15.2, one slide: bending size fails shear → redesign (a = 147 → 183 mm) | done |
| 16–17 | Ex 15.3: checks; nail spacing (13–15 are now Ex 15.1 2/2, Ex 15.2 V/M, Ex 15.2) | done |
| 16 | Key points + questions | to do |

Original plan (kept for reference):

| # | Slide | Content | Visual / animation | Source |
|---|---|---|---|---|
| 0 | Title | done | 3-D beam animation | — |
| 1 | Today | What we'll learn: (1) what limits a beam, (2) how to size it with S_req, (3) checking shear, (4) three worked examples | 4 rows, each with a small looping sketch (beam bending, S formula filling in, shear arrows, a W-shape being picked) | p. 687 (blurry, so worded in my own words) |
| **15.1 Basis for beam design** |||||
| 2 | Why a vertical load gives σ_x | The beam bends; top fibres get shorter, bottom fibres longer, the N.A. keeps its length → stress along x. σ_x = −My/I, and M grows with the span, so σ_x ≫ σ_y. | Animated: zoom on a short piece with grid lines; it bends (lines fan out); σ_x arrows on the end faces grow (push at the top, pull at the bottom) | p. 688 (+ Ch. 6) |
| 3 | Shear stress τ = VQ/It | Why shear stress exists (loose vs glued boards). V, Q = ȳ′A′, I, t explained one at a time. τ follows Q: zero at the edges, largest at the N.A. Sign convention for +V and +M, and why σ = −My/I has a minus. | Animated boards; colour-coded equation ↔ labels ↔ section parts; a line sweeps the section with A′, ȳ′ and t, and the τ curve traces | Ch. 7, Ch. 6 |
| 4 | A stress element is a tiny cube | What the element is, which faces we see (x, y, z) and how to draw τ on it (4 steps, corner check) | 3-D cantilever → cut at a–a → right part slides away → a cube is pulled out of a point on the cut face → it turns face-on into the square; xyz axes follow the view; the arrows are drawn one per click | Fig. 15-2, Ch. 9 |
| 5 | Beams are designed for strength | Loads act perpendicular to the beam axis. They produce a bending stress σ_x and a shear stress τ_xy. The local stress σ_y under a load is small, so σ_x ≫ σ_y, and bearing plates spread concentrated loads. | Animated: load applied → beam bends → zoom on an element under the load, with σ_x and σ_y arrows to scale. Then a point load vs a bearing plate: the pressure spike flattens out | p. 688 |
| 6 | Stress changes from point to point | Cantilever under P: shear stress follows a parabola, bending stress a straight line. Elements 1 and 5 carry only σ, element 3 (at the N.A.) only τ, and elements 2 and 4 carry both. | Interactive: cantilever + section a–a; σ (straight line) and τ (parabola) computed from the formulas. A marker moves up and down the section, and its stress element updates live (arrow lengths to scale). Elements 1–5 are pinned by clicks | p. 688–689 |
| 7 | Principal stresses and stress trajectories | Each element turns into principal stresses (Fig 15-2e). Stress trajectories cross the N.A. at 45° and meet each other at 90°. This is where reinforcement goes in brittle materials such as concrete. | Animated: each element rotates to its principal directions (angle computed). Then the trajectories are traced, integrated from the real stress field, solid for tension and dashed for compression, with the 45° crossing at the N.A. marked | p. 689 |
| 8 | Strength is not the only limit | Lateral bracing against sideways buckling. Deflection (Ch 16). Code limits. | Looping: (a) a long unbraced beam buckles sideways and twists, while the braced one stays straight; (b) the beam sags and the plaster ceiling under it cracks | p. 688 |
| **15.2 Prismatic beam design** |||||
| 9 | Design for bending first (done) | Ductile beams, long spans: bending controls. Main equation **S_req = M_max / σ_allow (15-1)**, with every term named by a red brace. S = I/c. | Equation with red braces. Animated: M_max grows → the S_req bar grows; choosing a bigger section brings σ back under σ_allow | p. 690 |
| 10 | Three ways to get a bigger S (done) | Deeper (S = bh²/6), material away from the N.A. (I-shape), just add material; weight needed for 2× S | Bars of S and A; rectangle morphs into an I-shape at constant area | p. 690–691 (illustration mine) |
| 10b | From S_req to a section | Simple shape (rectangle, circle): solve S = I/c for its size. Built-up or rolled shape: pick S > S_req from a table, and choose the lightest one. Allow a small margin for self-weight. | Animated: a rectangle grows until S = S_req; a W-shape list is filtered to S > S_req and the lightest one lights up | p. 690 |
| 11 | Steel W-shapes | Rolled shapes in the AISC manual / Appendix C. The flanges sit far from the N.A., so I and S are large. W18×46 means 18 in. deep and 46 lb/ft. A stiffener stops the web buckling at the supports. | A 3-D W-shape with its dimensions. Animation: the same area as a square vs as a W-shape, showing how material far from the N.A. raises I. The web buckles at the support → a stiffener stops it | p. 691 |
| 12 | Wood and built-up sections | Nominal vs actual size: a 2×4 is really 1.5 × 3.5 in., and the actual size goes in the calculations. Plate girders (welded or bolted), box beams, glulam. Fasteners must be checked too. | A 2×4 shrinks from nominal to actual size; plate girders, box beam and glulam built up layer by layer | p. 691–692 |
| 13 | Procedure for analysis | 1. V and M diagrams → 2. bending: S_req → 3. shear: τ_allow ≥ V_max Q/It (rectangle 1.5V/A, W-shape V/A_web) → 4. fasteners: q = VQ/I | Flowchart; each box shows a mini version of its picture (V/M diagram, section, shear profile, nail) | p. 693 |
| **Examples** |||||
| 14 | Ex 15.1 (1/2): steel beam, loads and diagrams | σ_allow = 24 ksi, τ_allow = 14.5 ksi. Reactions 10 and 50 kip; V_max = 30 kip, M_max = 120 kip·ft. | Beam → FBD → V and M drawn by a moving cut, one per click | p. 694 |
| 15 | Ex 15.1 (2/2): pick the lightest W | S_req = 60 in³. Table of 5 candidates with W18×40 highlighted. τ_avg = 30/(17.90·0.315) = 5.32 ksi < 14.5 ✓. Self-weight note. | Table filtered to S > 60 in³, sorted by weight; W18×40 lights up; then shear stress bar vs the allowable line | p. 694 |
| 16 | Ex 15.2 (1/2): wood beam, bending | 12 kN/m; reactions 32 and 16 kN; V_max = 20 kN, M_max = 10.67 kN·m. Section a × 1.5a: S_req = 0.00119 m³ → a = 0.147 m. | Moving-cut V and M; the section a × 1.5a grows until S = S_req | p. 695 |
| 17 | Ex 15.2 (2/2): shear governs | τ_max = 1.5V/A = 0.929 MPa > 0.6 MPa ✗. Redesign for shear: a = 183 mm. | τ bar shoots over the allowable line (red) → the section grows to 183 mm and the bar drops under the line | p. 695 |
| 18 | Ex 15.3 (1/3): T-beam, section properties | 2 boards, 200 × 30 mm. V_max = 1.5 kN, M_max = 2 kN·m. ȳ = 0.1575 m, I = 60.125(10⁻⁶) m⁴. | T-section from two boards; the centroid slides to ȳ; each board's I and Ad² term appear on it | p. 696 |
| 19 | Ex 15.3 (2/3): bending and shear check | σ = 5.24 MPa < 12 ✓. Q = 0.372(10⁻³) m³, τ = 309 kPa < 800 ✓. | σ and τ profiles over the T; the area used for Q is shaded; stress bars vs the allowable lines | p. 696–697 |
| 20 | Ex 15.3 (3/3): nail spacing | Q (flange) = 0.345(10⁻³) m³. q_BC = 8.61 kN/m and q_CD = 5.74 kN/m → s = 0.174 m and 0.261 m → use 150 mm and 250 mm. | The flange slips on the web without nails (animation), then nails pin it; nails drawn at 150 / 250 mm in their regions | p. 697 |
| **Wrap-up** |||||
| 21 | Key points + thank you | Design for bending, check shear, check fasteners. Lightest section that works. "Questions?" | Replay of the title animation + the 3 checks as icons | p. 692 (Important Points) |

## Still open
- **In-class practice problem?** It would have to be my own problem (no textbook problem pages were photographed), labelled as such. One option: a simply supported wood beam, L = 4 m, w = 8 kN/m, h = 2b, σ_allow = 10 MPa, τ_allow = 0.7 MPa. Answer: b = 134 mm, τ = 0.67 MPa (close to the limit). It would go between slides 19 and 20.
- **15.3–15.4** (fully stressed beams, shafts): not in the photos. Add them only if you send those pages.
- Merge slides 6 and 7 if time is tight.
- The Ex 15.1–15.3 numbers above were read from the photos and re-derived by hand (reactions, V, M, S, τ, q all agree with the book).

## Build order
Slides 1–12 first (shared beam and diagram helpers go into `01_slide_lib.py`), then 13–19, then 20. Each slide is built, rendered and checked before the next.
