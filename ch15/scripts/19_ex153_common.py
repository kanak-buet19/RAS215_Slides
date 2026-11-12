"""Shared drawing pieces for Example 15.3 (Hibbeler 6th ed., p. 696-697, Fig. 15-9). Not a slide.

Book data (checked against the photo of p. 696-697):
  wooden T-beam from two 200 mm x 30 mm boards (flange on top of a vertical web); sigma_allow = 12 MPa,
  tau_allow = 800 kPa; each nail resists 1.50 kN in shear.
  span: pin B at the left end, roller D at the right end, 4 m; 0.5 kN/m over B-C (2 m), 1.5 kN at C (mid-span).
  reactions B = 1.5 kN, D = 1 kN; V: 1.5 -> 0.5 over B-C, -1 over C-D; M_max = 2 kN.m at C.
  y_bar = 0.1575 m from the bottom, I = 60.125(10^-6) m^4.
Used by 20_make_slide16_ex153a.py and 21_make_slide17_ex153b.py.
"""
import importlib

lib = importlib.import_module("01_slide_lib")
NAVY, RED, GREY, SUP, TAU, WOOD = lib.NAVY, lib.RED, lib.GREY, lib.SUPPORT, lib.TAU, lib.WOOD
sym = lib.sym
MC = "#c27c0e"

X0, PM = 80, 110                 # x of B, px per m
X = lambda xm: X0 + PM * xm
BY, FT, WT = 44, 7, 19           # beam top, flange and web depth in the elevation (not to scale)
BH = FT + WT
YBAR, I_SEC = 0.1575, 60.125e-6


def V_at(x):
    return 1.5 - 0.5 * min(x, 2) - 1.5 * (x > 2)


def M_at(x):
    return 1.5 * x - 0.5 * min(x, 2) * (x - min(x, 2) / 2) - 1.5 * max(0, x - 2)


def beam(loads=True, dims=True):
    """T-beam elevation: flange strip over the web (nailed joint between them), loads, supports (id sup), dims."""
    s = (f'<rect x="{X(0)}" y="{BY}" width="{PM * 4}" height="{FT}" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.4"/>'
         f'<rect x="{X(0)}" y="{BY + FT}" width="{PM * 4}" height="{WT}" fill="#d6b27a" stroke="{WOOD["edge"]}" stroke-width="1.4"/>')
    if loads:
        for i in range(9):
            x = X(2 * i / 8)
            s += f'<line x1="{x:.1f}" y1="{BY - 24}" x2="{x:.1f}" y2="{BY - 3}" stroke="{RED}" stroke-width="1.5" marker-end="url(#a_C00000)"/>'
        s += f'<line x1="{X(0)}" y1="{BY - 24}" x2="{X(2)}" y2="{BY - 24}" stroke="{RED}" stroke-width="1.5"/>'
        s += f'<text x="{X(0.9)}" y="{BY - 31}" font-size="16" fill="{RED}" font-weight="bold" text-anchor="middle">0.5 kN/m</text>'
        s += f'<line x1="{X(2)}" y1="{BY - 44}" x2="{X(2)}" y2="{BY - 3}" stroke="{RED}" stroke-width="3" marker-end="url(#a_C00000)"/>'
        s += f'<text x="{X(2) + 8}" y="{BY - 32}" font-size="16" fill="{RED}" font-weight="bold">1.5 kN</text>'
    s += ('<g id="sup" style="transition: opacity 0.5s">'
          f'<polygon points="{X(0)},{BY + BH} {X(0) - 10},{BY + BH + 16} {X(0) + 10},{BY + BH + 16}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
          f'<polygon points="{X(4)},{BY + BH} {X(4) - 10},{BY + BH + 13} {X(4) + 10},{BY + BH + 13}" fill="#fff" stroke="{SUP}" stroke-width="2"/>'
          f'<circle cx="{X(4) - 5}" cy="{BY + BH + 16}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/>'
          f'<circle cx="{X(4) + 5}" cy="{BY + BH + 16}" r="3" fill="#fff" stroke="{SUP}" stroke-width="1.5"/></g>')
    s += (f'<text x="{X(0) - 8}" y="{BY + 14}" font-size="17" text-anchor="end" font-style="italic">B</text>'
          f'<text x="{X(2) - 6}" y="{BY + BH + 18}" font-size="17" text-anchor="end" font-style="italic">C</text>'
          f'<text x="{X(4) + 8}" y="{BY + 14}" font-size="17" font-style="italic">D</text>')
    for a, b in (((0, 2), (2, 4)) if dims else ()):
        s += f'<line x1="{X(a) + 2}" y1="{BY + 92}" x2="{X(b) - 2}" y2="{BY + 92}" stroke="{GREY}" stroke-width="1" marker-start="url(#a_555555)" marker-end="url(#a_555555)"/>'
        s += f'<text x="{X((a + b) / 2)}" y="{BY + 108}" font-size="14" fill="{GREY}" text-anchor="middle">2 m</text>'
    return s


def reactions(val_step):
    s = lib.hreact(X(0), BY + BH, "B", val_step)      # pin B: horizontal reaction, 0 (no horizontal load)
    for xm, R, nm in ((0, 1.5, "B"), (4, 1, "D")):
        s += f'<line x1="{X(xm)}" y1="{BY + 80}" x2="{X(xm)}" y2="{BY + BH + 3}" stroke="{NAVY}" stroke-width="3" marker-end="url(#a_002060)"/>'
        if nm == "B":
            s += (f'<text x="{X(xm) + 8}" y="{BY + 74}" font-size="17" fill="{NAVY}" font-weight="bold">{sym("R", nm + "y")}</text>'
                  f'<text data-step="{val_step}" x="{X(xm) + 38}" y="{BY + 74}" font-size="16" fill="{NAVY}" font-weight="bold">= {R:g} kN</text>')
        else:
            s += (f'<text x="{X(xm) - 8}" y="{BY + 74}" font-size="17" fill="{NAVY}" font-weight="bold" text-anchor="end">{sym("R", nm + "y")}</text>'
                  f'<text data-step="{val_step}" x="{X(xm) - 42}" y="{BY + 74}" font-size="16" fill="{NAVY}" font-weight="bold" text-anchor="end">{R:g} kN =</text>')
    return s


def v_diagram(VB, VS):
    vp = [(0, 0), (0, 1.5), (2, 0.5), (2, -1), (4, -1), (4, 0)]
    s = '<polygon points="' + " ".join(f"{X(x):.1f},{VB - VS * v:.1f}" for x, v in vp) + f'" fill="{TAU}" fill-opacity="0.15" stroke="{TAU}" stroke-width="2.2"/>'
    s += f'<line x1="{X(0)}" y1="{VB}" x2="{X(4) + 22}" y2="{VB}" stroke="#000" stroke-width="1.2" marker-end="url(#a_555555)"/>'
    s += f'<text x="{X(0) - 8}" y="{VB + 5}" font-size="15" text-anchor="end">{sym("V")} (kN)</text>'
    s += (f'<text x="{X(0) + 6}" y="{VB - VS * 1.5 - 6}" font-size="14" fill="{TAU}" font-weight="bold">1.5</text>'
          f'<text x="{X(2) - 6}" y="{VB - VS * 0.5 - 6}" font-size="14" fill="{TAU}" font-weight="bold" text-anchor="end">0.5</text>'
          f'<text x="{X(4) - 6}" y="{VB + VS + 16}" font-size="14" fill="{TAU}" font-weight="bold" text-anchor="end">−1</text>')
    return s


def m_diagram(MB, MS):
    mp = [(X(4 * i / 80), MB - MS * M_at(4 * i / 80)) for i in range(81)]
    s = '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in [(X(0), MB)] + mp + [(X(4), MB)]) + f'" fill="{MC}" fill-opacity="0.15" stroke="{MC}" stroke-width="2.2"/>'
    s += f'<line x1="{X(0)}" y1="{MB}" x2="{X(4) + 22}" y2="{MB}" stroke="#000" stroke-width="1.2" marker-end="url(#a_555555)"/>'
    s += f'<text x="{X(0) - 8}" y="{MB + 5}" font-size="15" text-anchor="end">{sym("M")} (kN·m)</text>'
    return s


def tsec(cx, yb, K):
    """T cross section to scale (K px per m), bottom of the web at yb. Returns svg and the key y values."""
    top = yb - 0.23 * K
    s = (f'<rect x="{cx - 0.1 * K:.1f}" y="{top:.1f}" width="{0.2 * K:.1f}" height="{0.03 * K:.1f}" fill="{WOOD["face"]}" stroke="{WOOD["edge"]}" stroke-width="1.6"/>'
         f'<rect x="{cx - 0.015 * K:.1f}" y="{yb - 0.2 * K:.1f}" width="{0.03 * K:.1f}" height="{0.2 * K:.1f}" fill="#d6b27a" stroke="{WOOD["edge"]}" stroke-width="1.6"/>')
    return s, dict(top=top, fb=yb - 0.2 * K, na=yb - YBAR * K)


def m(x):
    return f"<math>{x}</math>"


def ds(x):
    return f'<math><mstyle displaystyle="true">{x}</mstyle></math>'


U = lambda t: f"<mspace width='0.2em'/><mtext>{t}</mtext>"
P = lambda t: f"<mo stretchy='false'>(</mo>{t}<mo stretchy='false'>)</mo>"
E = lambda e: f"<mo stretchy='false'>(</mo><msup><mn>10</mn><mn>{e}</mn></msup><mo stretchy='false'>)</mo>"
IMP = "<mspace width='0.4em'/><mo>⇒</mo><mspace width='0.2em'/>"

STEP_CSS = lib.TEXT_CSS + f"""
  .given {{ position: absolute; left: 48px; top: 104px; width: 1164px; box-sizing: border-box; padding: 7px 14px 8px; font-size: 16px; line-height: 1.45;
            border: 2px solid {NAVY}; border-left-width: 7px; border-radius: 6px; }}
  .given math {{ font-size: 19px; font-weight: bold; }}
  .gh {{ font-size: 13px; font-weight: bold; color: {NAVY}; text-transform: uppercase; letter-spacing: 1px; }}
  .gf {{ color: {RED}; }}
  .steps {{ position: absolute; left: 680px; top: 166px; width: 560px; display: flex; flex-direction: column; gap: 14px; }}  /* uniform step spacing */
  .step {{ font-size: 17px; }}
  .step math {{ font-size: 17px; }}
  .no {{ display: inline-block; min-width: 22px; margin-right: 4px; color: {NAVY}; font-weight: bold; }}
  .no::after {{ content: "."; }}
  .row {{ display: flex; align-items: center; margin-top: 3px; }}
  .tag {{ width: 78px; flex: none; font-size: 12px; font-weight: bold; text-transform: uppercase; }}
  .tag.calc {{ color: {NAVY}; }}
  .tag.req {{ color: {RED}; }}
  .si {{ font-size: 13px; color: {GREY}; }}
  .cap {{ font-size: 14px; color: {GREY}; margin: 1px 0 0 78px; }}
  .ok {{ color: {TAU}; font-weight: bold; margin-left: 12px; font-size: 18px; }}
  .ans {{ position: absolute; padding: 3px 16px; font-size: 19px; color: {RED}; border: 2px solid {RED}; border-radius: 6px; }}
"""
