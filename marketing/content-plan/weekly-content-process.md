# Weekly Content Session

> The one content ritual: review → decide → scaffold → produce → import. Run once a week (usually Monday of the lead week), start to finish in one sitting — pausable anywhere. Output: `jira/imports/YYYY-Www.csv` imported to Jira, with drafts / Drive docs / Canva URLs behind it, and a chat handoff summary for Furqan.
>
> Replaced `plan-reconcile-process.md`, `monthly-plan-generation-process.md`, and `rolling-4week.md` on 2026-06-10 (git history has them). The state they carried now lives in three places, each with one owner — see State model.

## Trigger

- "Run the weekly content session"
- "Plan the content week"
- "Monday content session"

## Inputs

1. **Target publish week** — defaults to next ISO week.
2. **Anything Travis wants to flag** — slips, urgent insertions, capacity changes.

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/inputs.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/2026-content-plan.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira-csv-guidelines.md

(Per PRINCIPLES.md #4, this list is authoritative for this scope.)

## State model

| State | Lives in | Owner |
|---|---|---|
| Blog schedule (status + dates) | `../seo/briefs/` frontmatter | this session |
| Dated commitments + week sketches | [`inputs.md`](inputs.md) § Upcoming | this session |
| Idea mailbox | [`inputs.md`](inputs.md) § Ideas | anyone appends; this session triages |
| Editorial stance | [`inputs.md`](inputs.md) § Theme & stance | Travis |
| The locked week | `jira/imports/YYYY-Www.csv` | this session creates rows; channels fill tokens |
| What shipped | Jira (and git) | — |

No other plan files. "What's scheduled in the next 4 weeks" is computed live from brief frontmatter, never written down a second time.

---

## Phase 0 — Review (read-only, ~5 min)

1. **Brief queue:** `grep -H "status:\|scheduled_for:" ../seo/briefs/*.md` (skip `_template.md`, `archive/`). Show scheduled briefs for the next ~4 weeks + queued count. **If queued < 4, flag it** and offer to run [`../seo/seo-brief-production-process.md`](../seo/seo-brief-production-process.md) after the session.
2. **Upcoming:** read `inputs.md` § Upcoming — what's dated for this week and next? Anything needing rework (delays, launches, brief-needed deadlines)?
3. **Theme:** one-line check against [`2026-content-plan.md`](2026-content-plan.md) for the month's theme, and § Theme & stance for standing editorial rules.

Only if Travis asks: scan a prior week's CSV for leftover tokens, or recap what shipped.

## Phase 1 — Decide (the conversation)

Propose a slate for the target week and let Travis edit:

- **cerkl.com blog(s)** — from scheduled briefs (or promote a queued one)
- **ICPro blog** — topic from Upcoming or decided here
- **LinkedIn wraps** — a menu, not a quota: theme / blog link / poll / carousel — pick what fits the week. Short video is out-of-band (barebones Jira row only).
- **Anything from Upcoming that's due** — webinar emails, press releases, launch coverage

Apply the decisions as they're made:
- Brief scheduled → set `status: scheduled` + `scheduled_for:` in its frontmatter
- Idea approved for later → move to § Upcoming with a date
- Idea dead → prune; brief shipped → `status: shipped`, move to `archive/`
- Future-week sketches in § Upcoming → update to match what was decided

Slate confirmed in chat = the week is locked.

## Phase 2 — Scaffold

Run [`jira/jira-scaffold-process.md`](jira/jira-scaffold-process.md) with the slate. Pre-fill `Epic Link` (current campaign Epic key) and subtask `Owner` IDs from the ownership table in `jira-csv-guidelines.md` — Travis overrides at import only when something varies.

## Phase 3 — Produce (checkpoint after each step; pause anytime)

1. **Blogs:** [`../channels/seo-blog/seo-blog-process.md`](../channels/seo-blog/seo-blog-process.md) and [`../channels/icpro-blog/icpro-blog-process.md`](../channels/icpro-blog/icpro-blog-process.md) — pre-write → draft → edit → publish; each post's Drive URL fills its CSV token.
2. **LinkedIn copy:** [`../channels/linkedin/linkedin-process.md`](../channels/linkedin/linkedin-process.md) — fills the `Copy:` lines.
3. **LinkedIn assets:** [`../channels/linkedin/linkedin-asset-process.md`](../channels/linkedin/linkedin-asset-process.md) — fills the `Asset:` lines.

**Resuming after a pause:** the remaining `[…_PLACEHOLDER]` tokens in the CSV are the to-do list — scan and continue. Unfilled tokens at import time are fine; the team fills gaps in Jira.

## Phase 4 — Import + handoff

1. Travis imports the CSV to Jira (upload-only if Phase 2 pre-fills held).
2. Print the handoff summary: slate table (deliverable · date · Drive doc · Canva URL · anything left unfilled) + notes for Furqan. The summary is the record that the week went out.

---

## Rules

- **This session is the only thing that creates or restructures CSV rows**; channel processes only fill tokens. Forgot a row mid-week? Re-open the session and patch it here.
- **Briefs are canonical for blog scheduling** — date and status changes happen in frontmatter, nowhere else.
- **Capacity limits in `jira-csv-guidelines.md` are ceilings, not quotas.** A thin week is a valid week.

## Future work

- Wire to `/schedule` for a Monday-morning nudge (holiday slide built in: if Monday is a federal holiday, run Tuesday).
- Fold webinar/PR/email production deeper into Phase 3 — today they're surfaced in Phase 0/1 and produced in their own channels.

## Learnings

<!-- append "what broke / what we changed" notes here as the session runs -->
