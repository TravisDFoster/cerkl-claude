# numbered-stack — template

> A 40/60 dark-cobalt blog image: title block on the left, ordered vertical stack of named concepts on the right. Used to illustrate frameworks, maturity ladders, named steps, and any "N concepts in a meaningful order."

## When to use

Use this template when the blog post contains an **ordered list of 3-5 named concepts** that benefits from visual hierarchy. The order can be:

- **Progression / maturity** — e.g., Compliance → Clarity → Relevance → Connection (the "ladder" reading)
- **Sequence of steps** — e.g., the four moves to fight for attention: Interesting → Meaningful → Emotive → Findable
- **Priority or importance** — e.g., a 3-tier hierarchy of comms layers
- **Acronym letters with content** — only when each letter carries enough description to fill a row (otherwise use the horizontal letter-strip template)

The template assumes you can mark a "where most people are" point in the middle. If the content has no such marker, omit the `.stuck-divider` and the rungs will distribute evenly.

## When NOT to use

- The content is a **list without order** — use a bulleted list-card template instead
- The content is a **5-letter acronym** (V-A-L-U-E, etc.) where the letters themselves are the visual anchor — use the horizontal letter-strip template
- The content is a **comparison** (A vs B) — use the comparison-table template
- The content is **one big number / one stat** — use the stat-hero template
- There are **more than 5 items** — the rungs become illegibly small at 1200×627

## Layout

```
┌───────────────────────────────────────────────┐  1200×627
│                                                │
│  OVERLINE                                      │
│                          [04 Top item ───────] │  ← butter accent (destination)
│  Big title with                                │
│  [accented word]         [03 Item ──────────]  │
│                                                │
│  Short lede.            [● MOST STAY HERE ●]   │  ← optional inline pill
│                                                │
│  ▣ Logo                  [02 Item ──────────]  │
│                                                │
│                          [01 Bottom (dashed)]  │  ← muted (baseline)
└───────────────────────────────────────────────┘
```

- **Left (40%, ~470px)**: overline, title (~50px), lede (~19px), broadcast logo bottom-left
- **Right (60%, ~660px)**: 3-5 stacked rungs, rendered **bottom-up** (rung-1 visually at bottom)
- **Rungs**: cobalt-circle number badge (42px) + name (23px) + 1-line description (15.5px)
- **Top rung**: butter background, dark ink text — the "destination" pops
- **Bottom rung**: dashed outline, muted text — the "baseline"
- **Optional marker pill**: butter, all-caps, inline between two rungs to mark "where most teams sit"

## Content slots to fill

When using this template for a new blog post, swap these:

| Slot | What to write | Length |
|---|---|---|
| `.overline` | Category + frame, e.g., "INTERNAL COMMS · MATURITY MODEL" | 30-50 chars |
| `.title` | Main headline. Wrap the key concept word in `<span class="accent">...</span>` for butter highlight | 4-8 words, ≤2 lines at 50px |
| `.lede` | One-sentence framing of the WHY the diagram exists | 12-20 words |
| `.rung-name` (×4) | Name of each concept | 1 word ideal, 2 max |
| `.rung-desc` (×4) | One-line description in plain language | 8-14 words |
| `.stuck-pill` | "MOST X SIT HERE" or omit entirely | 3-5 words, all caps |

## Type scale (locked v2.1)

| Element | Size | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| `.title` | 50px | 700 | -0.8px | 1.05 |
| `.lede` | 19px | 400 | normal | 1.4 |
| `.overline` | 13.5px | 600 | 0.12em | 1.0 |
| `.rung-name` | 23px | 600 | -0.4px | 1.0 |
| `.rung-desc` | 15.5px | 400 | normal | 1.4 |
| `.rung-num` | 17px | 700 | -0.2px | 1.0 |
| `.stuck-pill` | 13px | 700 | 0.08em | 1.0 |

## Worked example

The included `example.html` / `example.png` is the four-rung maturity ladder from the blog post *The Hidden Cost of Benefits Communication* (2026-05-21). It demonstrates:

- All 4 rungs filled
- Optional `.stuck-pill` divider between rungs 2 and 3
- Butter-accent word ("benefits comms") in the title

## How to use this template for a new post

1. Copy `example.html` to a new sibling-of-blog folder, e.g., `blog-posts-live/YYYY-MM-DD_<slug>_images/numbered-stack.html`
2. Replace the 6 content slots above
3. Render: `bash /Users/travisfoster/claude-code/cerkl/marketing/design/blog-assets/render.sh <new-html-path>`
4. Resulting PNG is a sibling at the same basename
