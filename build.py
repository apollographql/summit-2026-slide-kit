#!/usr/bin/env python3
"""Assemble example/deck.src.html into a standalone example/deck.html.

Artwork lives in art/ as real files so it stays editable; this inlines each one
as a data URI so the built page is self-contained and can be opened or hosted
anywhere. Tokens in the source map to files as listed in ASSETS below.

Run:  python3 build.py
"""
import base64, mimetypes, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
ART, EX = ROOT / "art", ROOT / "example"

ASSETS = {
    "__LOCKUP__":     "lockup.png",       # Apollo Summit stacked lockup
    "__TRIO__":       "trio.png",         # title-slide shape trio
    "__PBG__":        "portrait-bg.jpg",  # speaker headshot backdrop
    "__STRIP__":      "strip.jpg",        # agenda top band
    "__BARCYAN__":    "bar-cyan.jpg",     # statement slide accent bar
    "__BARORANGE__":  "bar-orange.jpg",
    "__CIRCLE__":     "circle-grey.png",  # quote-slide dome
    "__EDGE__":       "edge-stack.png",   # section-divider right edge
    "__CLUSTERA__":   "cluster-a.png",    # takeaways corner cluster
    "__CLUSTERB__":   "cluster-b.png",    # closing corner cluster
}


def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def main():
    html = (EX / "deck.src.html").read_text()

    missing = [f for f in ASSETS.values() if not (ART / f).exists()]
    if missing:
        sys.exit(f"missing artwork in art/: {', '.join(missing)}")

    for token, filename in ASSETS.items():
        html = html.replace(token, data_uri(ART / filename))

    leftover = set(re.findall(r"__[A-Z_]+__", html))
    if leftover:
        sys.exit(f"unresolved tokens: {leftover}")

    out = EX / "deck.html"
    out.write_text(html)
    print(f"wrote {out.relative_to(ROOT)}  ({len(html) // 1024} KB)")
    print("export a PDF with:")
    print(f'  chrome --headless --no-pdf-header-footer --print-to-pdf=deck.pdf "file://{out.resolve()}"')


if __name__ == "__main__":
    main()
