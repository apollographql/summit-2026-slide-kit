# Apollo Summit 2026 — agentic slide kit

Everything a Summit speaker needs to build an on-brand deck **with an AI assistant** instead of by hand in Google Slides.

Speakers get a Google Slides template in their enablement kit, and most will use it. This is for the ones who would rather describe their talk to Claude, ChatGPT or Cursor and have it generate the slides — as HTML, as a PDF, or as anything else. Hand the model [`SLIDE-DESIGN-SYSTEM.md`](SLIDE-DESIGN-SYSTEM.md) together with your talk outline and it has everything it needs. No other file is required.

> **Status: proposed, pending design review.** Every number in the guide was measured from the official 2026 speaker template, but five open questions are flagged `[CONFIRM]` at the bottom of the guide and still need a decision from design.

---

## What's here

| Path | What it is |
|---|---|
| [`SLIDE-DESIGN-SYSTEM.md`](SLIDE-DESIGN-SYSTEM.md) | **The one file that matters.** Canvas, grid, palette, type ramp, slide archetypes, halftone rules, writing rules, and a pre-flight checklist. Self-contained. |
| `example/deck.src.html` | A worked 23-slide example exercising every archetype: title, agenda, section dividers, statement, quote, card rows, stat rows, arrow list, split code panel, diagrams, takeaways, resources. |
| `example/deck.html` | The same file with artwork and logos inlined, ready to open or print. |
| `art/halftone.py` | Generates the halftone artwork as SVG. See below. |
| `art/apollo-logo.svg`, `art/summit-logo.svg` | The two wordmarks used in the lockup. |
| `build.py` | Assembles `deck.src.html` into a standalone `deck.html`. |

## Quick start

```bash
python3 build.py
```

Then open `example/deck.html`, or export a PDF:

```bash
chrome --headless --no-pdf-header-footer --print-to-pdf=example/deck.pdf "file://$PWD/example/deck.html"
```

The page is built at 1920×1080 with everything sized in `em` off a single root, so it scales to any width without reflowing. Print CSS pins it to exact 16:9 pages.

## The halftone

The decorative language of Summit 2026 is **printed halftone**: a dot grid whose radius ramps across the shape, under a two-stop accent gradient. Squares, circles, quarter-rounds, and a full-bleed band.

The real artwork ships as ~30 MB of PNGs in the Slides template, which is impractical to embed in an HTML deck. `art/halftone.py` generates the same shapes as SVG instead — a few hundred circles, ~240 KB, resolution-independent:

```bash
cd art && python3 halftone.py     # writes halftone.svg
```

Symbols it defines: `ht-sq-oy` (orange→yellow square), `ht-sq-cy` (cyan square), `ht-sq-cyy` (cyan→yellow, the portrait backdrop), `ht-circ` (grey circle), `ht-qtr` (orange quarter-round), `ht-strip` (full-bleed band), `ht-tex` (faint page texture).

Tune dot pitch and radius ramp at the call sites in `halftone.py` if you need a different density.

## About the example

**The example deck is fictional.** "Northstar Robotics", "Alex Rivera" and every figure in it are invented. It exists to show what each archetype looks like with real prose in it, not to represent any company or talk. The portrait slot is a neutral placeholder, which is what the design system calls for until real photography lands.

Replace the copy with your own. Keep the structure.

## If you are not using this

That is fine. The Google Slides template in your enablement kit is the default path and it is fully supported. You can also use your own company branding, or Keynote, or present from your own laptop. Talk to your Speaker Buddy about anything outside the default setup.

The one hard rule either way: **use the provided title slide.**
