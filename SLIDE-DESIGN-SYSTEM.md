# Apollo Summit 2026 — Slide Design System

**For speakers building slides with an AI assistant.** Paste this file into Claude, ChatGPT or Cursor together with your talk outline, and it has everything it needs to build an on-brand deck. No other file is required.

Every number below was measured from the official 2026 speaker template (`PRIMARY - [Apollo Summit] 2026 Speaker Slide Template [MAKE A COPY]`). Where the template has an opinion, it wins. Items marked **[CONFIRM]** are places the template is silent or inconsistent and a designer decision is still needed.

> **What changed from v1.** v1 was the website design system with a four line slide footnote. Its orange, its teal, its font weights and its footer rule all disagreed with the actual template. Corrections are noted inline as *was:*.

---

## 0. The talk comes before the deck

- Your mainstage block is **30 minutes**. There is no formal per session Q&A. The audience is directed to the stage front or the Apollo lounge afterwards.
- Budget **1 to 2 minutes per slide**, so aim for **15 to 30 slides**.
- Structure: **intro** (grab attention, set the stage, establish credibility, preview the roadmap), **body** (three strong points, each tied back to your goal), **conclusion** (recap, reinforce, call to action, end with impact).
- Go deep. Audiences ask for more technical content every year. Show the code.
- Keep text minimal. One idea per slide. Spread a complex point across several slides rather than crowding one.
- Close a deep section with the takeaway you want people to keep.

---

## 1. Non negotiables

1. **The first title slide must be used.** Everything after it is yours.
2. **The Apollo Summit lockup appears on every content slide.** Bottom left. Details in §6.
3. **No emoji.** Not in slides, not in headings.
4. **Sentence case for everything except mono labels**, which are uppercase.

You may use your own company branding, and you may use Keynote or another tool. If you do, you present from your own laptop and the confidence monitor may not be available.

---

## 2. Canvas and grid

| Measure | Value |
|---|---|
| Size | **10 × 5.625 in** |
| Points | **720 × 405 pt** |
| Pixels at 96 dpi | **960 × 540 px** |
| Aspect | **16:9** |

*was: v1 gave no slide size at all, only a 1440 px web frame.*

Building in HTML instead? Use **1920 × 1080** and multiply every point value below by **2.667** to get pixels. Proportions are identical.

**The grid**, in inches from the top left:

| Guide | Value | What sits there |
|---|---|---|
| Outer gutter | **0.50 in** | Left and right. Symmetric. |
| Title top | **0.50 in** | Slide title baseline block |
| Content top | **1.38 in** | Cards, lists, diagrams |
| Footer top | **5.25 in** | The lockup |
| Bottom clearance | **0.18 in** | Air below the lockup |
| Text column | **8.96 in** | Full width inside the gutters |
| Column gutter | **0.23 in** | Between cards in a row |

Card column widths: **4.47 in** (two up), **2.91 in** (three up), **2.10 in** (four up).

> The template applies this by hand and the left gutter drifts between 0.47 and 0.53 in. **Snap to 0.50.**

---

## 3. Color

### The palette

| Role | Hex | Notes |
|---|---|---|
| **Canvas** | `#1A1A1A` | The default ground. Nearly every slide. |
| **Terminal ground** | `#18181B` | Only behind a terminal window. |
| **Card surface** | `#2B2B2B` | Code cards, step boxes. |
| **Card outline** | `#444444` | 0.75 pt. |
| **Type, primary** | `#FFFFFF` | |
| **Type, bone** | `#F5F5F0` | Interchangeable with white. Used on section titles and micro labels. |
| **Type, muted** | `#999999` | Captions, subtitles, supporting body. |
| **Accent 1, orange** | **`#FF7B3C`** | *was: `#E75E15`* |
| **Accent 3, cyan** | **`#6FEBFF`** | *was: teal `#3BD6E5`* |
| **Accent 4, yellow** | **`#FFD900`** | *was: absent from v1 entirely* |
| Hairline rule | `#595959` | Rules only. Never type. |

Three theme slots exist that the template never uses: `#4CA6B5`, `#FF3005`, `#D3F1FA`. **Do not use them.**

### Using accents

- **One accent leads per slide.** Pick orange, cyan or yellow and let it carry.
- **The exception is a card row**, where the template deliberately rotates the top rules **orange → cyan → bone → yellow** across two, three or four columns. This is the house pattern. Use it.

  *was: "orange appears once per composition" and "never stack accents." The template contradicts both on every card row. The rotation is intended.*
- **Text on an accent fill is always black.** Black on orange is 8.15:1. White on orange is 2.58:1 and fails. Black on yellow is 15.18:1.
- Mono labels are orange or cyan, never yellow, never white on a colored fill.

### Contrast, measured on `#1A1A1A`

| Color | Ratio | Normal text |
|---|---|---|
| White `#FFFFFF` | 17.40 | pass |
| Bone `#F5F5F0` | 15.91 | pass |
| Yellow `#FFD900` | 12.58 | pass |
| Cyan `#6FEBFF` | 12.43 | pass |
| Orange `#FF7B3C` | 6.75 | pass |
| Muted `#999999` | 6.11 | pass |
| Rule `#595959` | 2.48 | **fail. rules only** |

Every type color in the palette passes. Keep it that way: do not introduce opacity based greys. A white at 42% on canvas measures 4.05:1 and fails.

---

## 4. Type

**Two families do the work.** Inter for everything structural. Fira Code for every label.

- **Inter 400** carries titles, statements, body and stat numerals.
- **Inter 700** is reserved for card headings, speaker names and stat labels.
- **Fira Code 400** is the deck's small caps: eyebrows, section tags, role lines, agenda numerals, captions and all code.
- **Georgia 700** appears once, as the oversized quote mark on a quote slide. Nowhere else.

*was: v1 specified Aeonik substituted with Inter, at Medium 500, "never bold." The template contains no 500 at all. It is 400 and 700 only, and 700 is used deliberately.* **[CONFIRM]** *whether 700 is intended or an artifact of building in Google Slides.*

**There is no letter spacing.** Google Slides has no such property, so the template applies none. If you build in HTML you may apply `-0.02em` to type above 36 pt, but it is optional and not part of the spec.

### The ramp

Sizes in points are what you type into Google Slides. The percentage is of canvas width, so it scales to any canvas. Pixels are for a 1920 px wide HTML build.

| Role | Font | pt | % width | px @1920 |
|---|---|---|---|---|
| Quote mark | Georgia 700 | 96 | 13.3% | 256 |
| Hero numeral | Inter 400 | 90 | 12.5% | 240 |
| Big stat, three up | Inter 400 | 44 | 6.1% | 117 |
| Section title, large | Inter 400 | 41 | 5.7% | 109 |
| **Talk title** | Inter 400 | 36 | 5.0% | 96 |
| Statement | Inter 400 | 30 | 4.2% | 80 |
| Big stat, four up | Inter 400 | 29 | 4.0% | 77 |
| **Slide title** | Inter 400 | **24** | 3.3% | 64 |
| Image caption | Inter 400 | 21 | 2.9% | 56 |
| Talk subtitle | Inter 400 | 18 | 2.5% | 48 |
| **Body, list item** | Inter 400 | **18** ⬆ | 2.5% | 48 |
| Speaker name | Inter **700** | 14 | 1.9% | 37 |
| Card heading | Inter **700** | 14 ⬆ | 1.9% | 37 |
| Stat label | Inter **700** | 12 ⬆ | 1.7% | 32 |
| Card body | Inter 400 | 12 ⬆ | 1.7% | 32 |
| **Eyebrow, label** | **Fira Code** 400 | 11 ⬆ | 1.5% | 29 |
| Speaker role | **Fira Code** 400 | 11 | 1.5% | 29 |
| Code | **Fira Code** 400 | 10–12 | 1.4–1.7% | 27–32 |
| Caption | Inter 400 | 10 ⬆ | 1.4% | 27 |

**⬆ marks a deliberate step up from the template.** The 2026 Slides template sets body and list items at 14 pt. That is legible on a laptop and too small from the back of a session room, so this kit specifies **18 pt** and lifts the supporting sizes with it. Everything above body — titles, statements, stats — matches the template exactly.

If you are filling in the Google Slides template by hand rather than generating slides, bumping body text from 14 to 18 pt is the single highest-value change you can make.

*was: v1 gave body as 14–18 **px**, which is roughly 9 pt on a slide. Unreadable from row four.*

**Give 18 pt text room.** A list or body column set at 18 pt needs roughly **64–76 em** of measure (about 1,000–1,200 px at 1920) to avoid wrapping every line. Measures tuned for 14 pt will break the moment you scale the type up.

Line spacing **100** for headings and tight blocks, **115** for running body. Align **left**. Center only on a quote, a centered section title, or a symmetric diagram.

**No text box auto shrinks.** Overflow clips. Cut words rather than trusting the box.

---

## 5. Slide archetypes

The template ships 31 reusable pages. **Duplicate the page you want and replace its contents.** Choosing a layout from the Layout menu gives you a blank dark page, because the custom layouts carry background art only and no placeholders.

| Archetype | Use it for |
|---|---|
| **Title** | Your opening slide. Mandatory. Talk title, subtitle, headshot, name, role, company. |
| **Agenda** | Numbered 01–05 roadmap. Orange or cyan variant. |
| **Section divider** | Three styles: numbered with a hairline rule, a short accent tick with `PART 01`, or a centered title on framed art. |
| **Statement** | One sentence that has to land. Accent bar at the left edge. |
| **Quote** | A customer or team quote with an oversized Georgia quote mark. |
| **Two / three / four cards** | Parallel points. Colored top rule per card, rotating. |
| **Arrow list** | Four or five points, each led by a `→` in orange. |
| **Title break plus list** | Left side title and subhead, right side a hairline separated list. |
| **Split code panel** | Half dark panel, syntax highlighted code. |
| **Two code cards** | Schema beside query. |
| **Terminal window** | Command line output, with macOS traffic lights. |
| **Step diagram** | Five boxes left to right, outlines rotating through the accents. |
| **Flowchart** | Four icon slots joined by cyan connectors. |
| **Timeline** | A horizontal axis with accent stems and halftone dots. |
| **Three / four stats** | Big numerals over bold labels over muted captions. |
| **Customer proof** | A statement plus three inline stat pairs. |
| **Image** | Full bleed, image with caption, image left, or image right. |
| **Things to remember** | Numbered takeaways, numerals in Fira Code orange. |
| **Resources** | Docs, repo, example, contact. This is the closing slide. |

**There is no thank you or Q&A slide.** The resources page ends the deck. **[CONFIRM]** whether a closing slide should be added, given there is no formal Q&A in 2026.

### Anatomy of a content slide

Four rules that are easy to get wrong and that the template is completely consistent about:

1. **No eyebrow.** A content slide opens with its title at the top left, 24 pt, and nothing above it. Mono eyebrows belong to section dividers (`PART 01`), the speaker's role line, and attribution. Putting an orange label above every title is the fastest way to look off brand.
2. **A stat takes the color of its rule.** On a stat row the big numeral is set in the same accent as the 2.25 pt rule above it, orange under orange, cyan under cyan. A white numeral means a white rule.
3. **Captions pin to the bottom.** Card and stat columns are tall, and the 9 pt grey caption sits at the foot of the column with a real gap above it, not tucked under the body text.
4. **The bottom third is usually empty.** Content occupies the upper two thirds and the page is allowed to end. Do not fill the space.

---

## 6. Furniture

**The lockup.** The stacked Apollo Summit mark, bone `#F5F5F0`.

- Content slides: bottom left at **(0.245, 5.249) in**, sized **0.563 × 0.195 in**.
- Title slides: the **large** lockup, top left at **(0.493, 0.500) in**, **1.191 × 0.412 in**. Title slides carry no bottom lockup.
- Full bleed image slides: omit it.
- **Full opacity.** It is not faded.

*was: v1 said "low opacity," and said title slides carry no footer at all. The template renders the mark at 100% and gives title slides a larger mark instead.*

**Page numbers: there are none.** No slide in the template renders one.

*was: v1 specified a page number bottom right on every content slide. Do not add one.*

### Halftone: the one decorative device

Everything decorative in this system is **printed halftone**: a dot grid whose dot radius ramps across the shape, filled with a two stop accent gradient. There are four shapes and nothing else.

| Shape | Fill | Where it goes |
|---|---|---|
| **Square** | orange to yellow, or cyan | Corners of a section divider. Bleeds off the edge. |
| **Circle** | grey, bone to `#8A8A8A` | Mid right of a section divider. Cropped to a dome cresting the bottom edge on a quote slide. |
| **Quarter round** | orange to `#FF3005` | Corner clusters. Arc faces into the slide. |
| **Full bleed band** | orange to yellow, dots fading downward | Top edge of an agenda slide, about 0.5 in tall. |

**Placement rules**

- Art lives in the **corners and edges**, never behind or across the type. It bleeds off the slide rather than floating inside it.
- A section divider carries **three shapes** down the right side: square top, circle middle, square bottom, alternating accent.
- A closing or takeaways slide carries a **cluster of three** in one corner: solid circle, halftone quarter round, halftone square, overlapping.
- Content slides carry **no art at all**. Cards, stats, code, diagrams and lists sit on flat `#1A1A1A`.
- Section dividers also carry a **faint dot texture** across the whole page, white at about 5% on a 14 px grid. Content slides do not.
- The title slide carries a small **trio** under the subtitle: solid orange quarter round, cyan halftone square, solid grey circle, each about 0.26 in.
- The speaker headshot on a title slide sits on a **cyan to yellow halftone square**, with the portrait cut out on top.

**The real artwork ships with this kit**, extracted from the official template and resized to the dimensions the slides actually use — see `art/`. Use those files rather than approximating them. The template's halftone is a genuine rotated two-colour print screen (red dots over a yellow ground, offset at an angle); a flat one-colour orthogonal dot grid reads as an imitation next to it.

**Do not** draw new geometry, use stock illustration, use icons as decoration, or add drop shadows. `art/halftone.py` remains in the kit as a fallback that generates approximate shapes as SVG, for cases where you cannot ship ~1.4 MB of raster art.

*was: v1 said both "modular block shapes carry the personality" and "no shapes anywhere." Resolved: halftone is the shape language, it is strictly positional, and it never touches the type.*

---

## 7. Code slides

The template contains three code slides using two different color schemes. **Standardize on VS Code Dark+**, which is what two of the three already use.

| Token | Hex |
|---|---|
| Keyword | `#569CD6` |
| Type | `#4EC9B0` |
| Directive, function | `#DCDCAA` |
| Field, property | `#9CDCFE` |
| String | `#CE9178` |
| Punctuation, plain | `#CCCCCC` |

Fira Code 400, **10 to 12 pt**. On a `#2B2B2B` card with a `#444444` 0.75 pt outline, or on a flat `#1A1A1A` half panel.

Two things to avoid, both present in the template today: a flat `#CFEEF3` with no tokenizing, and directives colored `#15252D` on a `#2B2B2B` card, which measures **1.11:1** and is invisible.

Keep snippets under about **20 lines**. Cut imports and boilerplate. Highlight the line that matters by leaving everything else in `#CCCCCC`.

---

## 8. Writing

Four words: **direct, confident, curious, grounded.**

- **Sentence case everywhere.** Mono eyebrows and metadata are uppercase.
- **Do not hedge.** Short declarative sentences. No "helping to," no "aiming to," no "we believe."
- **Scale before emphasis.** If something matters, make it bigger. Do not reach for bold, italics or underlines.
- **Punctuation of the brand:** `·` between metadata items, `+` as "and" in a headline, `→` on list items and links.
- **No marketing language.** Write for someone who reads docs for fun.
- Retired terms: **supergraph** (say graph or federated graph), **Apollo Studio** (now Apollo GraphOS), **data graph**.

---

## 9. If your agent is generating HTML rather than Slides

- Canvas **1920 × 1080**. Multiply every pt value in §4 by **2.667**.
- Fonts: **Inter** and **Fira Code**, both on Google Fonts. Load weights **400 and 700** only.
- Do not use Aeonik. It is licensed and not redistributable, and the template does not use it.
- Reserve the footer band so content cannot collide with the lockup.
- Do not build in opacity based greys. Use the literal hexes in §3.
- Export to PDF at 1920 × 1080 and check every slide before sending it to your Speaker Buddy.

---

## 10. Before you send it

- [ ] The provided title slide is still slide 1, filled in.
- [ ] 15 to 30 slides for a 30 minute talk.
- [ ] The lockup is bottom left on every content slide, full opacity. No page numbers.
- [ ] One accent leads each slide. Card rows rotate orange, cyan, bone, yellow.
- [ ] Any text on an accent fill is black.
- [ ] Body is 14 pt or larger. Nothing is clipped.
- [ ] Code is Fira Code 10 to 12 pt, VS Code Dark+, under 20 lines.
- [ ] Sentence case. No emoji. No page numbers. No new shapes.
- [ ] Read the smallest text on the smallest screen you own.

---

## Open questions for the designer

1. **[CONFIRM] Inter 700.** Intended, or an artifact? v1 said Medium 500 never bold. The template has no 500 and uses 700 on card headings, speaker names and stat labels.
2. **[CONFIRM] The accent rule.** v1 said one accent per composition, never stacked. The template rotates up to four across a card row. Confirm the rotation is house style.
3. **[CONFIRM] A closing slide.** The deck ends on Resources. With no formal Q&A in 2026, is a thank you or contact slide wanted?
4. **[CONFIRM] Yellow `#FFD900`.** Absent from v1, used throughout the template. Is it a full peer of orange and cyan, or reserved for card rotations and diagrams?
5. **[CONFIRM] Bone versus white.** The template uses `#F5F5F0` and `#FFFFFF` interchangeably for type. Is there a rule, or is either fine?
