# Blog asset design principles

Reusable principles for HTML-rendered blog-post images (in-body diagrams, OG/social cards). Extracted from a working Canva reference set (DAGOaSILq2k — "Internal and External Communication blog post") and Cerkl brand guidelines.

## Canvas

- **Default size: 1200×627** (OG-image ratio, 1.91:1). Matches what cerkl.com blog OG previews crop to. Use this unless the concept requires more vertical space.
- **Margins: ~40px sides, ~32px top/bottom.** Fill the canvas. Canva refs leave very little perimeter whitespace; chrome (title bands, footers) eats budget that should belong to content.
- **No grey footer bands.** Put the broadcast logo as a small mark in the bottom-right corner instead — Canva refs don't ring-fence the logo with a strip.

## Color

- **Dark cobalt is the workhorse background.** 4 of 5 Canva refs use it. Higher contrast and more brand-distinctive than white. Use `#0c1159` base with a subtle freeform gradient up to `#3547c4`.
- **Light theme** works only when paired with a strong photo or photo-style asset. Reserve for in-body images that need to feel "softer" than social cards.
- **Butter (`#ffaa22` / `#80550f`) is the directional accent.** Use sparingly: arrows, "where you are" markers, "destination" rung in the ladder. Same role as Canva's orange arrows.
- **One accent does the heavy lifting** — cobalt for body, butter for direction/destination. Don't introduce a third.

## Layout

- **Two-column workhorse layout.** 50/50 (symmetric "vs" or comparison) or 40/60 (asymmetric title-left + content-right). Single-column with a floating side callout wastes space.
- **Title block left, content right.** Mirrors Canva pages 4 and 5. Title + 1-2 line lede + optional directional arrow.

## Components

- **Cobalt circle badges with white glyphs** are the standard "bullet" form. Check-circles for lists. Number-circles for ordered steps.
- **Pill labels as structural devices.** Canva page 3 uses center pills ("Purpose / Frequency / Focus / Formality") to label each row of a comparison. The pill IS the label — not a separate column.
- **Highlight pills around key words inside titles.** Canva page 2: "What is `Internal` Communication?" — the highlighted word sits in a pill within the heading. Use to anchor the concept.
- **Cards have subtle inner borders or glow**, not drop shadows. Drop shadows feel webby; inner borders feel printed.

## Typography

- **Work Sans throughout** (per `cerkl/marketing/design/branding-assets/Brand Guidelines/typography.md`).
- **Titles 36-44px, SemiBold/Bold, letter-spacing -0.5px.** Tight.
- **Body 15-17px, line-height 1.4-1.5.** Smaller than web body — these are images.
- **Overline/breadcrumb 12-13px, SemiBold, all-caps, letter-spacing 0.08-0.1em.** Use to label the asset ("MATURITY MODEL", "FRAMEWORK", etc.).

## Logo placement

- **Broadcast horizontal lockup, white variant on dark bg / full-color on light bg.**
- **28-32px height, anchored at the bottom of the title column** (bottom-left in 40/60 asymmetric layouts; bottom-right or bottom-center is fine when the layout warrants it). ~24-32px in from the edges.
- **No "Powered by" or attribution text bands** — the logo alone is enough; the source link belongs in the blog post body, not in the image.

## Anti-patterns

These are the things the v1 ladder did that the Canva refs would not:

- Big grey footer band with source text + logo — wastes 70+px of canvas
- 140px gradient header band just to hold a title and breadcrumb — the title can sit in-line with content
- 64px+ margins on all sides — Canva refs use ~40px
- 4:3 canvas (1200×900) — taller than the OG/social standard
- Floating side callout with arrow — works in a slide deck, looks orphaned in a blog image. Put the indicator INSIDE the structure (a divider tag between rungs, an inline pill, a highlighted row).
- Multiple shadow layers / soft glows everywhere — Canva refs use inner borders.

## Sizes other than 1200×627

| Use case | Size | When to deviate from default |
|---|---|---|
| Default blog hero / OG image | 1200×627 | (default) |
| In-body diagram with vertical concept (ladder, timeline, stack) | 1200×800 | When 4+ stacked rows can't read tight in 627px |
| Square social (Instagram, LinkedIn carousel) | 1080×1080 | Channel-specific, request explicitly |
| Pinterest / vertical Instagram story | 1080×1920 | Channel-specific, request explicitly |

When deviating, document why in the template's example file.

## Type scale (default)

This is the locked default type scale, derived from the `numbered-stack` v2.1 build. Other templates may deviate when content demands (e.g., a stat-hero template will have a much larger headline number) — document the deviation in the template's README.

| Role | Size | Weight | Letter-spacing | Line-height | Color |
|---|---|---|---|---|---|
| Title | 50px | 700 | -0.8px | 1.05 | white (or `--ink` on light bg) |
| Lede | 19px | 400 | normal | 1.4 | white @ 70% |
| Overline / breadcrumb | 13.5px | 600 | 0.12em (uppercase) | 1.0 | butter |
| Item / row name | 23px | 600 | -0.4px | 1.0 | white |
| Item / row description | 15.5px | 400 | normal | 1.4 | white @ 70% |
| Number badge | 17px | 700 | -0.2px | 1.0 | white on cobalt-60 |
| Marker pill | 13px | 700 | 0.08em (uppercase) | 1.0 | ink on butter |

Font: **Work Sans** (Google Fonts via `<link>`, with the fallback stack from the brand typography spec).

## Templates available

Each template is a self-contained HTML + example PNG + README explaining when to use it. Future agents: read each template's README before picking — names are descriptive of layout, not of one specific blog topic.

> **Auto-suggested per post.** The SEO blog editing skill ([`channels/seo-blog/skills/seo-blog-editing/SKILL.md`](../../channels/seo-blog/skills/seo-blog-editing/SKILL.md), step 6 of Finalize) scans every post on the way to `_live.md` and appends an `**Image candidates**` block listing 0-3 of these templates with content slots pre-filled. The block sits inside the publishing-skill strip zone, so it's QA-side only — it never reaches the Drive doc Furqan sees. Rendering remains a separate manual step via `render.sh`.

| Template | What it solves | Folder |
|---|---|---|
| `numbered-stack` | Ordered **vertical** list of 3-5 named concepts (maturity ladders, named steps, priority hierarchies) | [`templates/numbered-stack/`](templates/numbered-stack/README.md) |
| `letter-strip` | **Horizontal** strip of 3-6 acronym letters or named pillars, each anchored by a large character | [`templates/letter-strip/`](templates/letter-strip/README.md) |
| `stat-hero` | One **dominant stat** + takeaway framing. Built for blog OG / social previews where the number is the scroll-stopper | [`templates/stat-hero/`](templates/stat-hero/README.md) |

### Picking a template

- **Vertical progression / order matters** (e.g., maturity ladder) → `numbered-stack`
- **Horizontal sequence, equal weight per item** (e.g., acronym, pillars) → `letter-strip`
- **One number is the story** (hero stat, OG card) → `stat-hero`

When a new layout pattern shows up across 2+ blog posts that none of the existing templates fit, productionize it as a new template folder following the same shape (`example.html`, `example.png`, `README.md`).

## Pipeline

```bash
# 1. Copy a template's example.html to the blog-post's images folder
cp templates/numbered-stack/example.html \
   ../../channels/seo-blog/blog-posts-live/YYYY-MM-DD_slug_images/numbered-stack.html

# 2. Edit the content slots (see the template's README)

# 3. Render to PNG
bash render.sh ../../channels/seo-blog/blog-posts-live/YYYY-MM-DD_slug_images/numbered-stack.html
```

The render script is `blog-assets/render.sh`. Defaults to 1200×627 output. Pass `width height` as args 3-4 to override.
