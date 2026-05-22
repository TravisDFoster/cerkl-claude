# Organic Content Plan Context

## What this folder is

This folder contains the full system for planning, structuring, and operationalizing Cerkl's organic content. The output is a Jira-importable CSV that creates Tasks and subtasks under existing campaign Epics for a given month.

Jira is the operational record of what shipped and when. The content plan is the source of truth for what gets built and why.

---

## How the system works

There are three layers:

### 1. Annual content plan (`2026-content-plan.md`)

Defines the full-year campaign arc — monthly themes, campaign Epics, ICP pain points, key topics, and important dates. This is the strategic input. It does not change month to month.

### 2. Monthly content plan (`monthly-content-plans/[month-year].md`)

A week-by-week breakdown of every deliverable for a given month. Each row includes: deliverable name, channel, publish date, and owner. This is generated from the annual plan and any month-specific context (product launches, events, calendar constraints).

Monthly plans follow these rules:
- Weekly capacity limits apply (see `jira-csv-guidelines.md`)
- Social posts publish Tuesday–Friday by default
- No sends on federal holidays or blackout dates noted in the annual plan
- Each week has a narrative arc (e.g., Build the Problem → Launch → Deepen → Reinforce)

### 3. Jira CSV

Generated from the monthly plan using the rules in `jira-csv-guidelines.md`. One row per Task and subtask. Importable without manual cleanup except for:
- Adding the Epic ID
- Adding subtask owner IDs (see ownership table in guidelines)

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
- [content-lifecycle-process.md](content-lifecycle-process.md) — End-to-end narrative spine (brief queue → schedule → write → Jira → publish); read first to see how the layers connect
- [plan-reconcile-process.md](plan-reconcile-process.md) — Weekly Monday reconcile: triage briefs, process inputs, lock next week, generate Jira scaffold
- [monthly-plan-generation-process.md](monthly-plan-generation-process.md) — Generate a month's week-by-week plan from the annual plan
- [jira/jira-scaffold-process.md](jira/jira-scaffold-process.md) — Generate the weekly Jira CSV scaffold (invoked by plan reconcile)

Knowledge and inputs:
- [2026-content-plan.md](2026-content-plan.md) — Annual themes, Epics, ICP context, and important dates by month
- [jira-csv-guidelines.md](jira-csv-guidelines.md) — Field mappings, subtask templates, ownership, capacity limits, CSV output rules
- [jira/CONTEXT.md](jira/CONTEXT.md) — Weekly Jira import context: cadence, naming, scaffold contents, slug threading, lifecycle
- [jira/_template.csv](jira/_template.csv) — Canonical CSV template with placeholder Work Item IDs (T###/S###)

Operational ledgers:
- [rolling-4week.md](rolling-4week.md) — Source of truth for what gets made and when; Travis writes here at Monday reconcile
- [inputs.md](inputs.md) — Mailbox for raw ideas; triaged into the plan each Monday
- [monthly-content-plans/](monthly-content-plans/) — Generated monthly plans, one file per month
