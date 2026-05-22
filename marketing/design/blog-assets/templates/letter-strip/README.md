# letter-strip — template

> A horizontal strip of 3–6 cards, each anchored by a large character (letter or number) at the top. Used to illustrate acronyms, named pillars, and short ordered horizontal sequences.

## When to use

Use this template when the blog post contains a **short horizontal sequence of 3–6 named concepts** where each item has:

- A single-character anchor (letter for an acronym, digit for a pillar number)
- A short name (1–2 words)
- A short description or framing question (≤14 words, fits 2–3 lines at 14.5px)

The strongest fit is **acronym frameworks** — every letter carries content (V-A-L-U-E, S-M-A-R-T, A-I-D-A). The next-best fit is **N pillars** or **N steps** when the horizontal flow reads naturally left-to-right.

## When NOT to use

- The content is **a progression / ladder where order is meaningful vertically** — use [`numbered-stack`](../numbered-stack/README.md) instead
- The content has **6+ items** — the cards become illegibly thin at 1200×627
- The descriptions need **more than ~14 words** to make sense — the cards will overflow or text will shrink to unreadable
- The content is **one big number or stat** — use [`stat-hero`](../stat-hero/README.md)
- The content is a **comparison** (A vs B) — different template (not yet built)

## Layout

```
┌────────────────────────────────────────────────────────────┐  1200×627
│ OVERLINE                                                    │
│ Title with optional [accent word]                           │
│ Short lede (one sentence).                                  │
│                                                             │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐               │
│ │  V   │ │  A   │ │  L   │ │  U   │ │  E   │               │
│ │ Name │ │ Name │ │ Name │ │ Name │ │ Name │               │
│ │ Desc │ │ Desc │ │ Desc │ │ Desc │ │ Desc │               │
│ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘               │
│                                                             │
│ ▣ Logo                                              source  │
└────────────────────────────────────────────────────────────┘
```

- **Header (top)**: overline (butter), title (~44px), lede (~17.5px)
- **Strip (middle)**: 5 equal-width cards by default; grid is `repeat(N, 1fr)` so 3, 4, or 6 cards work by changing N
- **Cards**: 3px butter top accent line, big anchor character (76px butter), name (20px), description (14.5px muted)
- **Footer**: white broadcast logo bottom-left, source/URL bottom-right

## Content slots to fill

| Slot | What to write | Length |
|---|---|---|
| `.overline` | Category + frame, e.g., "INTERNAL COMMS · MEASUREMENT FRAMEWORK" | 30-55 chars |
| `.title` | Headline. Wrap the acronym (or key word) in `<span class="accent">` | 4-7 words |
| `.lede` | One-sentence framing of what the strip shows | 10-16 words |
| `.letter` (×N) | Single character (letter or digit) | 1 char |
| `.name` (×N) | Concept name | 1-2 words |
| `.question` (×N) | Short description or framing question | 6-12 words |
| `.footer-source` | Source URL or attribution | ≤20 chars |

## Card count variants

Change `grid-template-columns: repeat(5, 1fr)` to match item count:

- **3 cards**: card width ~363px — text can be longer (~16 words per description)
- **4 cards**: card width ~270px — moderate text (~12 words)
- **5 cards** (default): card width ~217px — short text (~10 words)
- **6 cards**: card width ~180px — very short (~7 words); avoid if possible

## Type scale

| Element | Size | Weight | Notes |
|---|---|---|---|
| `.title` | 40px | 700 | Smaller than numbered-stack title (50px) since header is full-width and the strip is the visual workhorse |
| `.lede` | 17px | 400 | |
| `.overline` | 13.5px | 600 | butter, uppercase |
| `.letter` | 110px | 700 | butter, letter-spacing -3px |
| `.name` | 27px | 600 | letter-spacing -0.4px |
| `.question` | 18px | 400 | white @ 72%, ≤ 6 words for clean 1-2 line wrap at 5-card width |

**Question copy tip**: at 5-card width (217px), keep questions ≤6 words so they land on 1-2 lines. Longer questions read as gray text-blocks that dilute the letter's impact. Adjust upward for 3 or 4 cards.

**Letter alignment**: cards use `align-items: center` + `text-align: center` so letters and text sit on the card's center axis. A `min-height: 2.7em` on `.question` locks each card's content block to a 2-line height — without it, cards with 1-line questions render shorter, and their (vertically centered) letters drift up relative to cards with longer questions. The min-height is what keeps all letters level across the row. If you change `.question`'s line-height or font-size, recompute the min-height to match (`2 × line-height` is the rule).

**Letter-to-name spacing (phantom-whitespace trap)**: the letter uses `line-height: 0.82` (tight) paired with `margin-bottom: 56px`. Don't be tempted to relax the line-height back to 0.95+ "for safety" — uppercase glyphs in Work Sans (and most modern grotesques) sit in a line-box that reserves ~25px of vertical room for ascender/descender extents the cap never uses. With a relaxed line-height, that phantom whitespace **absorbs `margin-bottom` increases**: bumping margin from 14 → 32 produces only ~+18px of *visible* gap. The recipe — tight line-height + explicit margin — is what makes the letter sit close to the top of its box and lets `margin-bottom` translate 1:1 into visible separation from the name below. Reuse this combo whenever a big display character needs deliberate spacing under it.

## Worked example

The included `example.html` / `example.png` is the VALUE measurement framework from *The Hidden Cost of Benefits Communication* (2026-05-21). All 5 letters, with framing questions matching the post.

## How to use this template for a new post

1. Copy `example.html` to a new sibling-of-blog folder
2. Replace the slots above
3. If item count ≠ 5, update `grid-template-columns: repeat(N, 1fr)`
4. Render: `bash /Users/travisfoster/claude-code/cerkl/marketing/design/blog-assets/render.sh <new-html-path>`
