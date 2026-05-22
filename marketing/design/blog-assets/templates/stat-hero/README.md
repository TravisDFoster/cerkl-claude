# stat-hero — template

> A 50/50 dark-cobalt OG/social card built around one dominant stat. The number is the visual anchor; the framing text on the right tells the audience what the stat *means*. Used for blog post hero images, OG meta images, and LinkedIn / X share previews.

## When to use

Use this template when the post is **anchored by one number** and that number is the strongest "scroll-stopper" in the article. Specifically:

- The post leads with a striking financial figure ($X spent / lost / wasted)
- The post leads with a percentage that flips a default assumption
- The post leads with a magnitude (M employees, B dollars, X% gap)
- You need an OG/social preview that earns the click

The takeaway side is what does the *work* — the number alone is just an attention grab. The right column must answer the audience's "so what?" in one short title + one punchline.

## When NOT to use

- The post has **multiple supporting stats** without a clear hero number — use a hero-stats strip (not yet built)
- The post has **no quantitative anchor** — use [`numbered-stack`](../numbered-stack/README.md) or [`letter-strip`](../letter-strip/README.md)
- The post is **in-body educational** rather than social-shareable — stat-hero is built for thumbnails, not for diagrams

## Layout

```
┌────────────────────────────────────────────────────────────┐  1200×627
│ OVERLINE                                                    │
│                                                             │
│                          │                                  │
│   $28,250                │  Most never use what they have.  │
│                          │                                  │
│   ▎ Spent per US         │  A benefit nobody knows about    │
│     employee, per year.  │  is, financially, a benefit      │
│                          │  that does not exist.            │
│                                                             │
│ ▣ Logo                                          Source: ... │
└────────────────────────────────────────────────────────────┘
```

- **Top**: overline (butter, uppercase)
- **Middle (50/50)**:
  - **Left**: huge stat number (156px butter, letter-spacing -5px) + butter-bordered "qualifier" line (18px)
  - **Right**: takeaway headline (40px, optional butter `accent` word) + 2-3 line punchline (18.5px muted)
- **Bottom**: white broadcast logo bottom-left, source attribution bottom-right (e.g., "Source: U.S. Bureau of Labor Statistics")

A subtle butter radial-glow sits behind the number to make it feel hot — see the body's gradient stack.

## Content slots to fill

| Slot | What to write | Length |
|---|---|---|
| `.overline` | Category + frame, e.g., "INTERNAL COMMS · THE HIDDEN COST" | 30-50 chars |
| `.stat` | The hero number. Include currency symbol or unit if relevant. | ≤8 chars (e.g., `$28,250`, `74M`, `350+`) |
| `.stat-tag` | One-sentence qualifier: what does the number measure? | 6-12 words |
| `.takeaway` | The "so what?" — the headline insight the stat unlocks. Wrap key word in `<span class="accent">` for butter highlight. | 6-10 words |
| `.punchline` | One short paragraph (2-3 lines) that gives the article's framing. | 18-30 words |
| `.source` | Source/attribution, e.g., "Source: U.S. Bureau of Labor Statistics" | ≤40 chars |

## Stat sizing

The stat font-size is `156px` by default — sized for `$XX,XXX` (8 characters). If the stat is longer or shorter, adjust:

| Stat length | Suggested font-size |
|---|---|
| 1-3 chars (e.g., `74M`, `8%`) | 200px |
| 4-6 chars (e.g., `$1,250`, `350+`) | 180px |
| 7-8 chars (e.g., `$28,250`, `74M USD`) | 156px (default) |
| 9-10 chars (e.g., `$1,234,567`) | 124px |

Letter-spacing scales with size — keep it negative (-3 to -6px) for tight numeric set.

## Type scale

| Element | Size | Weight | Notes |
|---|---|---|---|
| `.stat` | 156px (default) | 700 | butter, letter-spacing -5px |
| `.takeaway` | 40px | 700 | white, letter-spacing -0.6px |
| `.punchline` | 18.5px | 400 | white @ 72% |
| `.stat-tag` | 18px | 500 | white, butter left border |
| `.overline` | 13.5px | 600 | butter, uppercase |
| `.source` | 12.5px | 500 | dim, uppercase |

## When to use light theme instead

The default is dark cobalt (matches the rest of the template set). If the post requires a softer/friendlier feel — e.g., a feature story rather than a problem-frame — swap to a light theme by flipping the body background to white and adjusting text colors to ink. Not currently built; copy the example, change `--white: ...` references, and re-render.

## Worked example

The included `example.html` / `example.png` is the $28,250 hero from *The Hidden Cost of Benefits Communication* (2026-05-21). Demonstrates:

- 8-character stat at default 156px
- Single butter-accent word in the takeaway ("use")
- BLS attribution in the footer
