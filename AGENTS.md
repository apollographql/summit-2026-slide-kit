# AGENTS.md

Instructions for a coding agent working in this repo.

## What you are being asked to do

Build a conference talk deck for Apollo Summit 2026 from a speaker's outline, matching the official template. The speaker supplies the content. You supply the structure and the styling.

## Read these, in this order

1. **`SLIDE-DESIGN-SYSTEM.md`** is the specification. Canvas, grid, palette, type ramp, slide archetypes, halftone rules, writing rules, pre-flight checklist. Read all of it before writing a slide.
2. **`example/deck.src.html`** is the reference implementation. Every archetype in §5 is built there. When the spec names a slide type but not its geometry, take the geometry from this file. Card widths, gutters, rule thicknesses, column padding and caption placement are all encoded in its CSS.

The spec wins on rules. The example wins on measurements the spec does not state.

## Hard constraints

These are not stylistic preferences. A deck that breaks one gets sent back.

- **Canvas 1920 x 1080.** Everything sized in `em` off a single root of `16px`, so the page scales without reflowing.
- **pt to px is `x 2.667`.** The spec is written in points because the Google Slides template is. Body is 16 pt, which is 43 px, which is `2.667em`.
- **Fonts are Inter and Fira Code**, weights 400 and 700 only. Both are on Google Fonts. There is no 500. Do not use Aeonik, which is licensed and not redistributable.
- **Ground is `#1A1A1A`.** Use the literal hexes in §3. Never build greys out of opacity.
- **The provided title slide is slide 1**, filled in, always.
- **The Apollo Summit lockup sits bottom left on every content slide**, at full opacity.
- **No emoji. No page numbers. Sentence case**, except mono labels, which are uppercase.
- **Yellow `#FFD900` is structural only.** Never set type in it.
- **Card accent rules rotate** orange, cyan, bone, yellow, in that order, truncated to the column count.

## Things that are easy to get wrong

Four rules the template is completely consistent about, and that a generated deck usually breaks:

1. **Content slides carry no eyebrow.** The title sits at top left, 24 pt, with nothing above it. Mono eyebrows belong to section dividers, speaker role lines and attribution only.
2. **A stat numeral takes the colour of its rule.** Orange rule, orange numeral.
3. **Captions pin to the bottom of their column**, with a real gap above, not tucked under the body text.
4. **The bottom third is usually empty.** Content occupies the upper two thirds. Do not fill the space.

## Building

```bash
python3 build.py
```

This reads `example/deck.src.html`, inlines every `art/` asset as a data URI, and writes a standalone `example/deck.html`. Artwork is referenced in the source by token, for example `__LOCKUP__`. The token to file mapping is the `ASSETS` dict at the top of `build.py`.

Export a PDF with:

```bash
chrome --headless --no-pdf-header-footer --print-to-pdf=example/deck.pdf "file://$PWD/example/deck.html"
```

## Do not

- **Do not edit anything in `art/`.** Those files were extracted from the official template. Reference them by token.
- **Do not edit `example/deck.html` directly.** It is generated. Edit `deck.src.html` and rebuild.
- **Do not invent shapes, gradients or icons.** The decorative language is halftone only, and §6 says where it may go.
- **Do not put halftone behind type.** It is cornered and edged, never underneath text.
- **Do not use the three unused theme colours** `#4CA6B5`, `#FF3005`, `#D3F1FA`.

## Before you hand it back

Run the checklist in §10 of the spec. The two that catch the most problems: nothing is clipped, because no text box auto shrinks and overflow simply disappears; and 15 to 30 slides for a 30 minute talk.
