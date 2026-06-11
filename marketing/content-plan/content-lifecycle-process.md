# Content Lifecycle — the narrative

> How a piece of content travels from SEO brief to published post. This is orientation, not implementation — the implementation is the [weekly content session](weekly-content-process.md) plus the channel processes it invokes.

---

## Weekly cadence

The system runs on a **1-week lead time**: Week N content is produced during Week N−1, in one session (pausable).

| Day | Activity |
|---|---|
| **Mon** (week N−1) | [Weekly content session](weekly-content-process.md): review → decide the slate → scaffold the Jira CSV → produce (blogs, LinkedIn copy, assets). |
| **Mon–Tue** | Production finishes; Travis imports the CSV to Jira in whatever state it's in. |
| **Wed** | Review drafts with Furqan. |
| **Thu–Fri** | Furqan does Webflow/Wix publishing prep (CMS properties, schema, internal links, scheduling) + Canva finishing. |
| **Mon–Fri** (week N) | Content publishes on its scheduled dates. |

If Monday is a federal holiday, the session slides to Tuesday and the back half compresses.

---

## The lifecycle of one post

1. **SEO writes the brief** → `../seo/briefs/<slug>.md`, `status: queued`. (Triggered when the queue runs low — see the session's Phase 0 — via [`../seo/seo-brief-production-process.md`](../seo/seo-brief-production-process.md).)
2. **The session schedules it** → frontmatter becomes `status: scheduled` + `scheduled_for: YYYY-MM-DD`. The brief file is canonical for the blog schedule.
3. **The session scaffolds the week's CSV** → a Task row with `Slug: <slug>` + `[DRIVE_URL_PLACEHOLDER]`, subtasks, dates, owners, Epic pre-filled.
4. **The writing pipeline runs** → pre-write → draft → edit → publish ([`seo-blog-process.md`](../channels/seo-blog/seo-blog-process.md)). Publish uploads the `_live.md` to Drive and swaps the CSV token for the real Drive URL, matched by slug. Brief goes `in-progress` at pre-write. LinkedIn wraps get copy ([`linkedin-process.md`](../channels/linkedin/linkedin-process.md)) and Canva asset URLs ([`linkedin-asset-process.md`](../channels/linkedin/linkedin-asset-process.md)) the same way.
5. **Travis imports the CSV to Jira.** Unfilled tokens are fine — the team fills gaps in Jira.
6. **Furqan publishes** — opens the Jira task → Drive Doc → copies into Webflow/Wix, sets CMS properties from the brief, publishes on the due date; finishes Canva assets from the `Asset:` URL.
7. **Brief closes** — `status: shipped` + `shipped_date:`, moved to `briefs/archive/` at a session. Jira (and git) are the shipped record — nothing else is archived.

**Slug threading** holds the whole chain together without a database: the slug is the same string in the brief filename, frontmatter, CSV `Slug:` line, pipeline filenames, and the Webflow URL. See [`jira/CONTEXT.md`](jira/CONTEXT.md#slug-threading-the-canonical-identity).

---

## Where state lives

| State | Lives in |
|---|---|
| Queued / scheduled / in-progress briefs | `../seo/briefs/` frontmatter |
| Shipped briefs | `../seo/briefs/archive/` |
| Annual theme + Epics | [`2026-content-plan.md`](2026-content-plan.md) |
| Dated commitments + week sketches | [`inputs.md`](inputs.md) § Upcoming |
| Idea mailbox + editorial stance | [`inputs.md`](inputs.md) § Ideas / § Theme & stance |
| The locked week | `jira/imports/YYYY-Www.csv` |
| Drafts in production | `../channels/seo-blog/blog-posts-*`, `../channels/icpro-blog/blog-posts-*`, `../channels/linkedin/drafts/` |
| Final drafts for Furqan | Google Drive (Claude-Uploads) |
| Shipped content | Webflow / Wix; Jira is the record |

---

## Cross-channel notes

- **LinkedIn wraps** are a menu per blog week (theme / blog link / poll / carousel — pick what fits; no quota). The short video is out-of-band: barebones Jira row for capacity tracking only.
- **ICPro** (internalcommspro.com) has no brief queue — topics are decided at the session; the scaffold synthesizes the slug once and downstream reads it from the CSV.
- **Versus pages + landing pages** have briefs in `../seo/briefs/` but flow into their own channel pipelines; they still get scheduled through the session so frontmatter stays canonical.
- **Webinars, PR, emails** are surfaced at the session (Phase 0 date sweep) and produced in their own channels; deeper integration is future work.
