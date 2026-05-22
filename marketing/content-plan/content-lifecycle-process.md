# Content Plan — End-to-End Process

> The full lifecycle of a piece of content, from SEO brief to published post. This is the spine that connects [`../seo/`](../seo/), [`./`](./), [`../channels/`](../channels/), and Jira. Each step points at where the work actually lives — this file is the narrative, not the implementation.

---

## Weekly cadence

The whole system runs on a **1-week lead time**: Week N content is created during Week N−1.

| Day | Activity |
|---|---|
| **Mon** (week N−1) | Monday reconcile: lock next week into [`rolling-4week.md`](rolling-4week.md). **Generate the Jira CSV scaffold** at [`jira/imports/YYYY-Www.csv`](jira/) — all rows present, blog Task Descriptions include `Slug: <slug>` and a `[DRIVE_URL_PLACEHOLDER]`. Trigger writing+publishing agent. |
| **Tue** (week N−1) | Writing+publishing agent finishes — every blog draft in Google Drive, every CSV row's placeholder replaced with the real Drive URL. CSV is now complete; Travis imports to Jira. |
| **Wed** (week N−1) | Review drafts with Furqan. |
| **Thu–Fri** (week N−1) | Furqan does Webflow/Wix publishing prep (CMS properties, schema, internal links, scheduling). |
| **Mon–Fri** (week N) | Content publishes on its scheduled dates. |

### Holiday gotcha

If Monday of week N−1 is a federal holiday, the cadence compresses: reconcile + writing shifts to Tue–Wed, Furqan review moves to Thu, publishing prep gets one day (Fri). Plan to pull the brief triage forward to the previous Friday if you can.

**Worked example — Week 1 June 2026 (Memorial Day in lead week):**
- Mon May 25 — federal holiday
- Tue May 26 — reconcile + writing agent starts
- Wed May 27 — writing agent finishes, Jira CSV imported
- Thu May 28 — review with Furqan
- Fri May 29 — Furqan publishing prep
- Mon Jun 1 onward — Week 1 June publishes

---

## The lifecycle

### 1. SEO writes the brief
- **Where:** [`../seo/briefs/`](../seo/briefs/) — one `.md` per topic, frontmatter follows [`../seo/briefs/_template.md`](../seo/briefs/_template.md)
- **Status:** `queued`
- **Owner:** SEO (Claude or human, working from [`../seo/keyword-strategy.md`](../seo/keyword-strategy.md))

### 2. Triage queue → schedule into a month
- **When:** Once per month during monthly plan generation, or rolling during Monday reconcile
- **Where:** This step touches both [`../seo/briefs/`](../seo/briefs/) and the relevant monthly plan in [`monthly-content-plans/`](monthly-content-plans/)
- **What happens:**
  - Open [`../seo/briefs/`](../seo/briefs/) and the target month's plan
  - Pick briefs that fit the month's theme + campaign Epic
  - For each match: update brief frontmatter to `status: scheduled` and `scheduled_for: YYYY-MM-DD` (publish date)
  - Monthly plan row uses the brief's title (not an invented one) and references the brief slug in the **Source brief** column
- **Gaps:** if a month has slots but no fitting briefs, that's a request to SEO to write more briefs

### 3. Monday reconcile → next week locks + Jira CSV scaffold created
- **Where:** [`rolling-4week.md`](rolling-4week.md) (rules in its header); [`jira/imports/`](jira/) (the new scaffold)
- **What happens:**
  - Row(s) for week N move from monthly plan into rolling-4week's "Week 1 — locked" section
  - Cross-channel posts (LinkedIn theme / link / poll / short video) that wrap the blog get scheduled into the same week
  - **Generate the week's Jira CSV scaffold** at `jira/imports/YYYY-Www.csv` per [`jira-csv-guidelines.md`](jira-csv-guidelines.md). All rows present and most fields filled — for each blog Task, the Description includes `Slug: <slug>` and a `[DRIVE_URL_PLACEHOLDER]` token. SEO-blog slug = brief slug (from `../seo/briefs/<slug>.md`); ICPro slug = synthesized from the deliverable title (lowercase, hyphenate, strip punctuation, ≤60 chars). The placeholder gets replaced by the publishing skill (step 4d below).

### 4. Writing pipeline runs for the locked week
- **Where:** [`../channels/seo-blog/seo-blog-process.md`](../channels/seo-blog/seo-blog-process.md) for cerkl.com; [`../channels/icpro-blog/icpro-blog-process.md`](../channels/icpro-blog/icpro-blog-process.md) for internalcommspro.com
- **What it does:** Each channel's process owns its own 4-substep pipeline (pre-write → draft → edit → publish). Publishing uploads `_live.md` to Drive and replaces `[DRIVE_URL_PLACEHOLDER]` in the week's Jira CSV with the actual Drive URL, matching rows by `Slug: <slug>`. Brief `status` advances from `scheduled → in-progress` at pre-write and stays `in-progress` through publish (SEO-blog only — ICPro has no brief). See each channel's process file for substep detail.

### 5. Travis imports the (now complete) CSV to Jira
- **Where:** Jira CSV importer (UI)
- **What happens:**
  - The CSV at `jira/imports/YYYY-Www.csv` now has every blog Task's Drive URL filled in
  - Travis imports; only manual fills at import time are Epic ID + subtask owner IDs (per the ownership table in [`jira-csv-guidelines.md`](jira-csv-guidelines.md))

### 6. Furqan publishes
- **Where:** Webflow (cerkl.com) or Wix (internalcommspro.com)
- **What happens:**
  - Furqan opens the Jira task → clicks the Drive Doc link → copies the draft into the CMS
  - Sets CMS properties from the brief frontmatter (`Primary Category`, `Primary Solution`, `All Categories`, `Keywords`)
  - Publishes on the Task due date

### 7. Brief closes
- **What happens:**
  - Brief frontmatter updated: `status: shipped`, `shipped_date: YYYY-MM-DD`
  - Brief moves to `../seo/briefs/archive/` on the next Monday reconcile
  - Rolling-4week row marked `shipped`; at month close, ship rows archive to `monthly-content-plans/YYYY-MM-posted.md`

---

## Where each piece of state lives

| State | Lives in |
|---|---|
| Queued briefs | [`../seo/briefs/`](../seo/briefs/) |
| Scheduled briefs (this month) | same — `status: scheduled` + `scheduled_for` |
| In-progress briefs | same — `status: in-progress` |
| Shipped briefs | [`../seo/briefs/archive/`](../seo/briefs/archive/) |
| Annual theme + Epic | [`2026-content-plan.md`](2026-content-plan.md) |
| Monthly plan (week-by-week) | [`monthly-content-plans/[month-year].md`](monthly-content-plans/) |
| What's locked next week | [`rolling-4week.md`](rolling-4week.md) — Week 1 |
| What's planned 2–4 weeks out | [`rolling-4week.md`](rolling-4week.md) — Weeks 2–4 |
| Research signals waiting for triage | [`inputs.md`](inputs.md) |
| Drafts in production | `../channels/seo-blog/blog-posts-draft/`, `../channels/icpro-blog/blog-posts-draft/` |
| Final drafts for Furqan | Google Drive (Claude-Uploads folder) |
| Weekly Jira imports | [`jira/imports/`](jira/) |
| Shipped content | Webflow / Wix (not stored in this repo) |

---

## Cross-channel orchestration

Content-plan is the **integration layer** because LinkedIn (and email, when active) wraps around each blog post. The four LinkedIn slots that pair with a typical blog week:

- **LinkedIn static/theme** — kicks off the blog's topic
- **LinkedIn static/blog** — links to the published blog
- **LinkedIn poll** — engagement around the blog's question
- **LinkedIn short video** — demo or quick framework tied to the blog's angle

When a blog brief schedules into a week, the matching LinkedIn rows schedule alongside it. **LinkedIn does not have its own brief queue** — the monthly plan author drafts LinkedIn topic lines directly, using the blog brief as context.

---

## Open process gaps

Track and close as we iterate.

- **icpro brief queue:** internalcommspro.com posts don't go through `../seo/briefs/` today (that folder is cerkl.com only). ICPro topics live in the monthly plan / rolling-4week directly; the slug is synthesized from the deliverable title at scaffold time (see [`jira/CONTEXT.md`](jira/CONTEXT.md#slug-threading-the-canonical-identity)). Worth spinning up `icpro-blog/briefs/` later when icpro grows enough to need keyword tracking + refresh management — for now the synthesized-slug path is sufficient.
- **LinkedIn briefs:** no brief queue today. Monthly plan author writes the LinkedIn topic line directly from the paired blog.
- **Versus pages + landing pages:** `comparison-seo` and `website` briefs exist in `../seo/briefs/` but flow into their own channel pipelines, not the seo-blog rotation. They should still go through the same triage step (`status: scheduled`, `scheduled_for`) so the writing agent and Jira CSV pick them up.
- **Brief → LinkedIn linkage:** no field on a brief that says "LinkedIn posts wrap this in week X." Today it's implicit in the monthly plan; consider making it explicit if it gets confusing.
