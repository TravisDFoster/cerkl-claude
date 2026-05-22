# Experiments Log

> Living record of Meta paid experiments. Tests move between sections as their state changes: **Designed → Active → Completed → Archive**. Update each test's block as data comes in — not just at completion.

---

## Active

*(none yet)*

---

## Designed (pre-launch)

### Test 1 — 3-cell audience read

**Hypothesis:** Among (A) 1% LAL of Foundations sign-ups + demo emails, (B) cold interest stack, and (C) retargeting, cell C will produce the lowest CPC and set the floor benchmark; A will beat B if Meta can extrapolate from our seed; B's performance tells us whether Meta's interest graph is usable for cold internal-comms-buyer acquisition.

**Hard blocker (must clear before launch):** Foundations sign-up event firing into Pixel + Conversions API — see [system-status.md](system-status.md).

**Design:**
- **Objective:** Leads
- **Cells:** A (1% US+CA LAL), B (cold interest stack), C (retargeting) — full definitions in [audience-guidelines.md](audience-guidelines.md)
- **Creative:** one Pains-concept video (audience-agnostic for test 1; audience is the variable)
- **Budget structure:** ABO, $30/day total = ~$10/day per cell
- **Geo:** US + CA
- **Bid strategy:** Highest volume
- **Placements:** Advantage+ Placements
- **Exclusions:** existing Foundations users + paid customers (cells A and B)
- **Run length:** 14 days
- **Primary success metric:** CPC, low $3 target
- **Secondary metric:** CPL — pulled in if clicks look junky
- **Expected end:** launch date + 14 days

**Known constraint:** at $10/day per cell, no cell will exit Meta's learning phase within 14 days (need ~50 conversions/cell; at $30 CPL that's ~$1,500/cell, far above the per-cell envelope). Treat results as **directional CPC + creative read**, not CPL truth. Plan test 2 with consolidated budget on the winning cell.

**TK sign-off:** ✅ 2026-05-21 (decisions table in [meta-ads-channel-launch.md](../../../personal-assistant/projects/meta-ads-channel-launch.md))

**Launch date:** TBD — pending conversion event verification

---

## Completed

*(none yet)*

---

## Archive

*(none yet)*

---

## How to use this log

- **When a test launches:** move its block from "Designed" to "Active." Add launch date.
- **When data comes in:** edit the block in place. Add an `### Observations` subsection with dated bullets (e.g., `- 2026-06-01: cell B CPC trending high at $5.40; junk-click hypothesis worth checking`).
- **Mid-flight decisions** (pause a cell, kill a creative, shift budget): record as a dated bullet under Observations *and* update the relevant design field if the change is durable.
- **When a test ends:** move to "Completed." Add `### Results` (with link to `data-exports/<YYYY-MM-DD>-<scope>.csv`) and `### Learnings` sections.
- **When a test is more than ~6 months old or has been fully superseded:** move to "Archive." Keep the block intact for historical reference.
