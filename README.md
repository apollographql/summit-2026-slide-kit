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

The decorative language of Summit 2026 is **printed halftone**: a rotated two-colour dot screen, used as squares, circles, quarter-rounds and a full-bleed band.

`art/` holds the **real artwork**, extracted from the official Google Slides template and resized to the dimensions the slides actually use. The template ships these as ~36 MB of PNGs at up to 2048 px; this kit carries the same art at ~1.4 MB by cropping to the used region and sizing each file to roughly 1.4× its on-slide size. Opaque pieces are JPEG, anything needing transparency stays PNG.

| File | What it is |
|---|---|
| `lockup.png` | Apollo Summit stacked lockup, used on every slide |
| `trio.png` | The three-shape trio on the title slide |
| `portrait-bg.jpg` | Cyan-to-yellow halftone backdrop for the speaker headshot |
| `strip.jpg` | Full-bleed band across the top of an agenda slide |
| `bar-cyan.jpg`, `bar-orange.jpg` | Left-edge accent bar on a statement slide |
| `circle-grey.png` | Grey halftone circle, and the dome cresting a quote slide |
| `edge-stack.png` | The three shapes down the right edge of a section divider |
| `cluster-a.png`, `cluster-b.png` | Corner clusters for takeaways and closing slides |

`build.py` inlines all of it as data URIs, so the built `deck.html` is a single self-contained file you can open, host, or hand to anyone.

**`art/halftone.py` is a fallback**, not the main path. It generates approximate halftone shapes as SVG (~240 KB, resolution-independent) for cases where shipping raster art isn't practical. It is a decent imitation, but the real screen is a rotated two-colour print pattern and the difference shows side by side. Prefer the real files.

## About the example

**The example deck is fictional.** "Northstar Robotics", "Alex Rivera" and every figure in it are invented. It exists to show what each archetype looks like with real prose in it, not to represent any company or talk. The portrait slot is a neutral placeholder, which is what the design system calls for until real photography lands.

Replace the copy with your own. Keep the structure.

## If you are not using this

That is fine. The Google Slides template in your enablement kit is the default path and it is fully supported. You can also use your own company branding, or Keynote, or present from your own laptop. Talk to your Speaker Buddy about anything outside the default setup.

The one hard rule either way: **use the provided title slide.**
