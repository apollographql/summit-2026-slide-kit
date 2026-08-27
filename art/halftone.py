"""Generate Apollo Summit halftone artwork as inline SVG.
The template's decorative language is printed-halftone: a dot grid whose dot
radius ramps across the shape, filled with a two-stop accent gradient."""
import math

def dots(w, h, step, r0, r1, ramp, clip=None, gid="g"):
    """ramp: 'lr','rl','tb','bt','radial' - direction dot radius grows."""
    out = []
    cols = int(w // step) + 1
    rows = int(h // step) + 1
    cx0, cy0 = w / 2, h / 2
    maxd = math.hypot(cx0, cy0)
    for i in range(cols):
        for j in range(rows):
            x = i * step + step / 2
            y = j * step + step / 2
            if x > w or y > h:
                continue
            if   ramp == 'lr': t = x / w
            elif ramp == 'rl': t = 1 - x / w
            elif ramp == 'tb': t = y / h
            elif ramp == 'bt': t = 1 - y / h
            else:              t = 1 - math.hypot(x - cx0, y - cy0) / maxd
            t = max(0.0, min(1.0, t))
            r = r0 + (r1 - r0) * t
            if r <= 0.06:
                continue
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}"/>')
    body = "".join(out)
    clipattr = f' clip-path="url(#{clip})"' if clip else ""
    return f'<g fill="url(#{gid})"{clipattr}>{body}</g>'

def grad(gid, c1, c2, x2=1, y2=0):
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')

ORANGE, YELLOW, CYAN, GREY, BONE = "#FF7B3C", "#FFD900", "#6FEBFF", "#B8B8B8", "#F5F5F0"

defs, syms = [], []

# 1. orange -> yellow halftone square, dots grow to the top-right
defs.append(grad("gOY", "#FF3005", YELLOW, 1, -1))
syms.append(f'<symbol id="ht-sq-oy" viewBox="0 0 200 200">{dots(200,200,7,0.6,3.1,"lr",gid="gOY")}</symbol>')

# 2. cyan halftone square, dots grow downward
defs.append(grad("gCY", CYAN, "#2FB8CC", 0, 1))
syms.append(f'<symbol id="ht-sq-cy" viewBox="0 0 200 200">{dots(200,200,7,3.1,0.9,"tb",gid="gCY")}</symbol>')

# 3. grey halftone circle
defs.append(grad("gGR", BONE, "#8A8A8A", 0, 1))
defs.append('<clipPath id="cCirc"><circle cx="100" cy="100" r="100"/></clipPath>')
syms.append(f'<symbol id="ht-circ" viewBox="0 0 200 200">{dots(200,200,6,0.5,2.7,"bt",clip="cCirc",gid="gGR")}</symbol>')

# 4. orange halftone quarter-round (corner radius at bottom-left)
defs.append(grad("gOR", ORANGE, "#FF3005", 1, 1))
defs.append('<clipPath id="cQtr"><path d="M200 0 L200 200 L0 200 A200 200 0 0 1 200 0 Z"/></clipPath>')
syms.append(f'<symbol id="ht-qtr" viewBox="0 0 200 200">{dots(200,200,7,0.7,3.0,"rl",clip="cQtr",gid="gOR")}</symbol>')

# 5. full-bleed gradient halftone strip, orange -> yellow, dots fade downward
defs.append(grad("gStrip", ORANGE, YELLOW, 1, 0))
syms.append(f'<symbol id="ht-strip" viewBox="0 0 1200 60" preserveAspectRatio="none">'
            f'{dots(1200,60,7,3.4,0.7,"tb",gid="gStrip")}</symbol>')

# 5b. cyan -> yellow halftone square, the headshot backdrop
defs.append(grad("gCYY", CYAN, YELLOW, 0.4, 1))
syms.append(f'<symbol id="ht-sq-cyy" viewBox="0 0 200 200">{dots(200,200,7,2.9,1.4,"tb",gid="gCYY")}</symbol>')

# 6. faint page texture for section dividers
syms.append('<symbol id="ht-tex" viewBox="0 0 200 200">'
            '<g fill="#FFFFFF" opacity="0.05">'
            + "".join(f'<circle cx="{i*10+5}" cy="{j*10+5}" r="1.1"/>' for i in range(20) for j in range(20))
            + '</g></symbol>')

svg = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
       + "".join(defs) + "".join(syms) + '</defs></svg>')
open(__import__("pathlib").Path(__file__).parent / "halftone.svg", "w").write(svg)
print("bytes:", len(svg))
