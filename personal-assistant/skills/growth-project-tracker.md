# Skill: Growth Project Tracker (Leadership Review)

Triggered weekly (typically Thursday morning) to regenerate the **evergreen** growth-project-tracker artifact Travis takes into the leadership meeting with Tarek.

Output is **one file, updated in place**: `personal-assistant/growth-project-tracker.md` + sibling `.html`. No dated filenames. The doc's *content* carries the date in the meta header — the *filename* never changes.

Goal: produce a portfolio-level read of the active marketing & growth ops projects — what's shipping, what's at risk, what's on deck — derived entirely from INDEX + project Status blocks. No domain work; this is a view, not a source.

## Procedure

1. **Confirm INDEX is current**
   - Read `INDEX.md`. If `**Last refreshed:**` is older than ~5 days, run the [`refresh`](refresh.md) skill first so the tracker isn't built on stale state.

2. **Cheap reads only — Status blocks**
   - For each project listed in INDEX's Next Steps table, read the **Status block** (first ~10 lines) of its project file via `Read` with `limit: 10`. Do not load full project files.
   - Use the Status block to confirm: state, due date, on-track flag, and last-updated date. If INDEX and the Status block disagree, surface the conflict — don't paper over.

3. **Compute stats** (no fabrication — if a number isn't derivable, omit)
   - Active projects = count of rows in INDEX's Next Steps table (exclude archived).
   - Top of Mind = count of items in INDEX's "Top of Mind" section.
   - Hard deadlines in next 14 days = projects with a `Due` date inside `[today, today+14]`.
   - Blocked or at-risk = projects with `On track` value of `Blocked`, `No`, `Pending`, or `Paused`.

4. **Pull Recently Shipped** (~last 2 weeks)
   - For each project in INDEX, scan its `## Completed` section (or equivalent) for entries dated within the last ~14 days.
   - Aggregate as a flat dated list at the bottom of the tracker. Most recent first.

5. **Render the markdown** at `personal-assistant/growth-project-tracker.md` (overwrite in place). Required structure:
   ```
   # Marketing & Growth Ops — Portfolio Review

   > Personal Assistant · Growth Project Tracker
   > **Date:** YYYY-MM-DD (<Day>)
   > **Audience:** Tarek Kamil (CEO) + leadership team
   > **Author:** Travis Foster, Head of Marketing & Growth Ops

   ## TL;DR
   <2–3 sentences synthesizing portfolio state — what's shipping, what's blocked, what window is the team in. Avoid bullet-restating individual projects; that's what Top of Mind is for.>

   ## Stats
   - **N** active projects
   - **N** Top of Mind
   - **N** hard deadlines in the next 14 days (<window>)
   - **N** blocked or at-risk (<short list, e.g., "Cerkular — Blocked; YouTube — Pending TK">)

   ## Top of Mind
   <One subsection per INDEX Top-of-Mind item. Each has: Next step / Due / On track / Why it matters.>

   ## Upcoming Milestones (<today> → <today+30>)
   <Markdown table from INDEX's Calendar Anchors, filtered to the next ~30 days.>

   ## Full Project Ledger
   <Markdown table — copy of INDEX's Next Steps table minus the Owner column.>

   ## Recently Shipped
   <Flat dated list, most-recent first, ~last 2 weeks.>

   ---

   *Source ledger: [INDEX.md](INDEX.md) — refreshed YYYY-MM-DD*
   ```

6. **Render HTML via sub-agent** — dispatch `md-to-html` (do not render inline; protects parent context per [`cerkl/skills/md-to-html/SKILL.md`](../../skills/md-to-html/SKILL.md)). Brief:
   ```
   Run the md-to-html skill on /Users/travisfoster/claude-code/cerkl/personal-assistant/growth-project-tracker.md.
   artifact_type: dashboard
   theme: dark
   ```
   The dashboard reference template (`reference-dashboard.html`) is the right shape for a leadership briefing — number-led, chart-led, low prose. Dark theme is brand-approved for short, high-impact, external-facing artifacts.

7. **Surface to Travis** — terse confirm:
   ```
   ## Growth Project Tracker refreshed — <date>
   - Stats: N active / N top of mind / N deadlines in 14d / N at-risk
   - Top of Mind shifts since last refresh: <list>
   - Anything flagged for your call before the meeting: <list>
   ```

## Don't

- Don't author new content — this is a view of INDEX. If a project's state is wrong, the fix lives in the project file (and a `refresh` run), not here.
- Don't load full project files — Status block (top ~10 lines) only. Per [PRINCIPLES.md #4](../../PRINCIPLES.md) and PA's "Cheap reads first" rule.
- Don't load `shared/`, `marketing/`, `sales/`, `hubspot/`, `strategy/`, `research/` context — PA tracks state, doesn't execute domain work.
- Don't rename or date the output file. Evergreen filename is the whole point of this move.
- Don't render HTML inline — always dispatch the `md-to-html` sub-agent.

## Edge cases

- **INDEX is stale (last refreshed > 5 days ago):** run `refresh` first, then this skill. Don't skip — a tracker built on stale state misleads the meeting.
- **Project Status block disagrees with INDEX row:** surface the conflict to Travis; don't pick a winner.
- **Project has no Status block (rare, mostly team rollups like `allison-projects.md`):** skip — team rollups aren't projects.
- **Hard deadline outside the 14-day window:** include in Upcoming Milestones if within ~30 days, but don't count in the "deadlines in 14d" stat.
