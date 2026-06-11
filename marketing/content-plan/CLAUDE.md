# Identity

You are helping Travis plan, schedule, and operationalize Cerkl's organic content — the cross-channel orchestration layer that sits between SEO briefs and channel writing pipelines. Output of this folder is the weekly Jira-importable CSV plus everything produced behind it, all driven by one ritual: the weekly content session.

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for `content-plan/`. Individual process files declare any additional loads they need.)

## Routing Table

| Task | Go to |
|---|---|
| **Run the weekly content session** (review → decide → scaffold → produce → import) | [`weekly-content-process.md`](weekly-content-process.md) |
| Understand how the whole content system fits together (orientation) | [`content-lifecycle-process.md`](content-lifecycle-process.md) |
| Generate the weekly Jira CSV scaffold (invoked by the session, also runnable standalone) | [`jira/jira-scaffold-process.md`](jira/jira-scaffold-process.md) |
| Dump a new idea/signal for session triage; check what's coming up | [`inputs.md`](inputs.md) |
| See what's scheduled (blogs) | brief frontmatter in [`../seo/briefs/`](../seo/briefs/) — canonical; the session presents it as a table |
| Write an SEO brief (normally Wave 1 of the session; standalone batch possible) | [`../seo/seo-brief-production-process.md`](../seo/seo-brief-production-process.md) |
| See the annual campaign arc (suggestion only — goes stale fast) | [`2026-content-plan.md`](2026-content-plan.md) |
| Look up Jira field rules, capacity ceilings, ownership | [`jira-csv-guidelines.md`](jira-csv-guidelines.md) |

## File Structure

```
content-plan/
├── CLAUDE.md                              ← you are here (router)
├── CONTEXT.md                             ← stable knowledge about the system
├── weekly-content-process.md              ← THE weekly ritual (review → decide → scaffold → produce → import)
├── content-lifecycle-process.md           ← narrative spine: brief → publish (orientation)
├── 2026-content-plan.md                   ← annual themes + Epics + ICP context
├── jira-csv-guidelines.md                 ← Jira field rules + capacity ceilings
├── inputs.md                              ← Upcoming (dated) · Ideas (mailbox) · Theme & stance
└── jira/                                  ← weekly Jira CSV import context
    ├── CONTEXT.md
    ├── jira-scaffold-process.md
    ├── _template.csv
    ├── imports/                           ← weekly CSVs
    └── archive/                           ← CSVs older than ~3 months
```

## Rules

- Brief lifecycle changes (queued → scheduled → in-progress → shipped) always touch the brief's frontmatter in [`../seo/briefs/`](../seo/briefs/) — the brief file is canonical for the blog schedule; nothing re-records it.
- Slug threading is the system's identity model. Slug stays exactly the same string from brief → Jira CSV → publishing skill → Webflow URL. If you're tempted to "fix" a slug downstream, you're introducing drift — fix the source instead. See [`jira/CONTEXT.md`](jira/CONTEXT.md#slug-threading-the-canonical-identity).
- The weekly session creates and restructures CSV rows; channel processes only fill their placeholder tokens.
