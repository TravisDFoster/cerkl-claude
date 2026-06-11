# Organic Content Plan Context

## What this folder is

The orchestration layer for Cerkl's organic content. One ritual — the [weekly content session](weekly-content-process.md) — turns the annual plan, the brief queue, and the inputs mailbox into a Jira-importable CSV plus the drafts, Drive docs, and Canva assets behind it.

Jira is the operational record of what shipped and when. This folder holds the planning state and the process.

---

## How the system works

Three pieces of state, each with one owner:

1. **`../seo/briefs/`** — the canonical cerkl.com blog schedule (frontmatter) + per-post SEO contract (body). Briefs are written **just-in-time inside the weekly session** (Wave 1), from topics approved in the session conversation and grounded in the SEO research set (`../seo/keyword-strategy.md` + `../seo/inventory/` — staleness checked every Monday). "What's coming up" is computed live from frontmatter, never written down a second time.
2. **[`inputs.md`](inputs.md)** — Upcoming (dated commitments + future-week sketches), Ideas (the mailbox), Theme & stance (standing editorial direction). Items pulled into a week's slate are deleted at lock — the CSV owns them from there.
3. **`jira/imports/YYYY-Www.csv`** — the locked week. During the session the orchestrator is the only writer; production subagents return values and the orchestrator fills the placeholder tokens. The CSV goes to Jira in whatever state it's in; the team fills gaps there.

The **annual plan** (`2026-content-plan.md`) is a suggestion, not an input — campaign Epics, ICP pain points, blackout dates. Consult on demand; it goes stale fast and never overrides inputs + SEO status + Travis's call. (Monthly plans and `rolling-4week.md` were retired 2026-06-10 — git history has them.)

Standing rules:
- Weekly capacity limits are ceilings, not quotas (see `jira-csv-guidelines.md`)
- Social posts publish Tuesday–Friday by default
- No sends on federal holidays or blackout dates noted in the annual plan

---

## Ownership

| Channel | Owner | Jira ID |
|---|---|---|
| Social Media | Furqan Iqbal | `712020:77c51683-fca4-4aee-9e06-929c5b3042ea` |
| Blog Posts | Furqan Iqbal | `712020:77c51683-fca4-4aee-9e06-929c5b3042ea` |
| Marketing Emails | Travis Foster | `62bb263d268cac6e31c40941` |
| SEM | Travis Foster | `62bb263d268cac6e31c40941` |
| Press Releases | Travis Foster | `62bb263d268cac6e31c40941` |
| Webinars | Travis Foster | `62bb263d268cac6e31c40941` |
| Cerkl.com Website Pages | Tarek Kamil | `5aa490a9f958b02df135afac` |
| Videos (Explainer, Product Showcase) | Travis Foster | `62bb263d268cac6e31c40941` |

---

## Resources

Processes (executors):
- [weekly-content-process.md](weekly-content-process.md) — THE weekly ritual: review → decide → scaffold → produce → import
- [jira/jira-scaffold-process.md](jira/jira-scaffold-process.md) — Generate the weekly Jira CSV from the session's slate (invoked by the session; runnable standalone)
- [content-lifecycle-process.md](content-lifecycle-process.md) — End-to-end narrative (brief → publish); orientation read

Knowledge and inputs:
- [2026-content-plan.md](2026-content-plan.md) — Annual themes, Epics, ICP context, important dates by month
- [jira-csv-guidelines.md](jira-csv-guidelines.md) — Field mappings, subtask templates, ownership, capacity ceilings, CSV output rules
- [jira/CONTEXT.md](jira/CONTEXT.md) — Weekly Jira import context: cadence, naming, scaffold contents, slug threading, lifecycle
- [jira/_template.csv](jira/_template.csv) — Canonical CSV template with placeholder Work Item IDs (T###/S###)
- [inputs.md](inputs.md) — Upcoming / Ideas / Theme & stance
