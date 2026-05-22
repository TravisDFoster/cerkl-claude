# LinkedIn Writing Guide

> Voice and structure rules for LinkedIn posts. Per-post-type skeletons live in [`templates/`](templates/).

## Voice

Cerkl voice — matches the blog. Apply the [`seo-blog-editing` references](/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/skills/seo-blog-editing/references/) verbatim:

- No em-dashes
- No "actually," "really," "just," "genuinely," "simply"
- No "it's not X, it's Y" or "Not X. Y." binary contrasts
- No LLM filler ("at its core," "when it comes to," "in the world of")
- Direct, plain, zero-fluff
- Date format `YYYY-MM-DD`

**Future work:** Decide whether LinkedIn voice should diverge from blog voice (shorter sentences, more hook energy, more line breaks). For now they are identical. Revisit after 2–3 weeks of posts.

## Universal structure

Every LinkedIn post has two pieces:

1. **Caption** — the text above the asset / poll / link card
2. **Asset or asset spec** — for carousels, statics, videos, this is the visual; for polls, it's the question + options; for link posts, it's the link card LinkedIn auto-renders

## Caption length rules

- **Asset-heavy posts (carousel, short video):** caption is short. A tight hook, optional 1-line setup, and a downward pointer. The visual carries the content.
- **Light-asset posts (static-theme, static-blog, poll):** caption is longer. The caption carries the argument. Use line breaks; 4–8 short paragraphs is typical.

No fixed character cap — write to the post, not to a limit.

## Hashtag policy

Restrained. Two to three hashtags max, only the high-relevance ones. Default set for Cerkl:

- `#InternalCommunications`
- `#EmployeeEngagement`

Add one topical hashtag where it fits (e.g., `#EmployeeBenefits` for a benefits-comms post, `#HRTech` for a platform-positioning post). Never tag-bomb.

## Link policy

LinkedIn suppresses reach when external links sit in the post body. Default: put the link in the first comment, and write the caption with a downward pointer:

> *Link in comments ↓*

**Exception:** link posts (`static-blog`) where the link card *is* the asset. There the link goes in the post body, because the card is the point.

## Per-post-type table

| Type | Asset weight | Caption length | Template |
|---|---|---|---|
| Carousel | Heavy (8–12 slides) | Short (3–5 lines) | [`templates/carousel.md`](templates/carousel.md) |
| Static — theme | Light (1 graphic) | Long (4–8 short paragraphs) | [`templates/static-theme.md`](templates/static-theme.md) |
| Static — blog link | Light (link card) | Medium (3–5 paragraphs) | [`templates/static-blog.md`](templates/static-blog.md) |
| Poll | Light (poll widget) | Long (4–6 paragraphs) | [`templates/poll.md`](templates/poll.md) |
| Short video | Heavy (video) | Short (2–4 lines) | [`templates/short-video.md`](templates/short-video.md) |

## Banned moves (from blog editing, carried over)

- Em-dashes (use periods or parentheses)
- Banned adverbs: "actually," "really," "just," "genuinely," "simply"
- Binary contrasts: "It's not X, it's Y" / "Not X. Y."
- Filler openers: "At its core," "when it comes to," "in the world of"
- Engagement-bait: "comment YES if you...", "tag someone who..."
- Lowercase-i-am-a-thought-leader voice
