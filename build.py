#!/usr/bin/env python3
"""Assemble example/deck.src.html into a standalone example/deck.html.

The source file keeps three placeholder tokens so the artwork and logos stay
editable as real files rather than being buried in one giant HTML blob:

    __HALFTONE__       the generated halftone symbol library
    __APOLLO_PATHS__   the Apollo wordmark paths
    __SUMMIT_PATHS__   the SUMMIT wordmark paths

Run:  python3 build.py
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).parent
ART, EX = ROOT / "art", ROOT / "example"


def svg_inner(path):
    """Strip the outer <svg> wrapper and make fills inherit currentColor."""
    s = path.read_text()
    s = re.sub(r"^.*?<svg[^>]*>", "", s, flags=re.S)
    s = re.sub(r"</svg>\s*$", "", s, flags=re.S)
    return re.sub(r'fill="(?!none)[^"]*"', 'fill="currentColor"', s).strip()


def main():
    halftone = ART / "halftone.svg"
    if not halftone.exists():
        print("generating art/halftone.svg ...")
        subprocess.run([sys.executable, "halftone.py"], cwd=ART, check=True)

    html = (EX / "deck.src.html").read_text()
    html = (html
            .replace("__HALFTONE__", halftone.read_text())
            .replace("__APOLLO_PATHS__", svg_inner(ART / "apollo-logo.svg"))
            .replace("__SUMMIT_PATHS__", svg_inner(ART / "summit-logo.svg")))

    if "__" in re.sub(r"[a-z]__[a-z]", "", html):
        leftover = set(re.findall(r"__[A-Z_]+__", html))
        if leftover:
            sys.exit(f"unresolved tokens: {leftover}")

    out = EX / "deck.html"
    out.write_text(html)
    print(f"wrote {out.relative_to(ROOT)}  ({len(html) // 1024} KB)")
    print("to export a PDF: open it in Chrome and print to PDF at 1920x1080,")
    print("or run: chrome --headless --print-to-pdf=deck.pdf --no-pdf-header-footer file://<abs path>")


if __name__ == "__main__":
    main()
