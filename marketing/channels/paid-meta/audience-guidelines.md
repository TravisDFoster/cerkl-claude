# Audience Guidelines

> Audience definitions, exclusion rules, and the system for adding / promoting audiences as test data accumulates.

**Last updated:** 2026-05-21

---

## Test 1 audiences (pre-launch — designed 2026-05-21)

| Cell | Audience | Definition | Hypothesis |
|---|---|---|---|
| **A** | 1% US + CA LAL | Lookalike (1%, US + CA), seeded from Foundations sign-up + demo-request emails (~115 records as of 2026-05-21) | Meta can extrapolate from existing-user shape to find similar internal-comms owners at scale |
| **B** | Cold interest stack | Title targets (Internal Communications, Employee Communications, Internal Comms Manager) **AND** interests (Employee engagement, Workplace from Meta, Slack as business interest, Microsoft Teams as business interest). US + CA. | Meta's title + interest graph is usable for cold acquisition of our buyer — independent of first-party seed |
| **C** | Retargeting (warm) | Pixel-fired Cerkl.com visitors past 180 days + IG/FB account engagers past 90 days. US + CA. | Warm audience sets the "hot floor" CPC / CPL benchmark to compare cold cells (A, B) against |

## Exclusion list (applies to all cold cells — A and B)

- Existing Foundations users (email list export from Foundations DB)
- Paid customers (email list export from CRM)

**Why:** don't pay to retarget current customers. Cell C is retargeting by design, so the exclusion applies to A and B only.

## System for adding new audiences

Each test cycle, new audiences enter via one of three paths:

1. **Variant of a winner** — narrow or broaden a cell that won test N. Example: if cell A (1% LAL) wins test 1, test 2 could compare 1% vs. 2% vs. 3% LAL. New audience block goes here with the parent winner referenced.
2. **Net-new hypothesis** — different angle, different data source. Example: lookalike seeded from email-engaged employees (if that data becomes available). New audience block lists the hypothesis explicitly so we know what we're learning.
3. **Promoted to production** — a cell that's won 2+ tests with stable CPC/CPL gets promoted to the "Production audiences" section below and runs as an always-on campaign.

**Every new audience must include:** definition, source data + freshness, hypothesis, success metric. **TK signs off** before the audience runs.

## Production audiences

*None yet — pending test 1 results.*

## Retired audiences

*None yet — track here as audiences are deprecated, with the reason and final CPC/CPL.*

## Source data inventory

| Source | Records | Freshness | Used for |
|---|---|---|---|
| Foundations sign-up emails | ~100 (as of 2026-05-21) | Refresh monthly from Foundations DB | LAL seed (cell A) |
| Demo-request emails | ~15 (as of 2026-05-21) | Refresh monthly from CRM | LAL seed (cell A) — included because many demos convert to Foundations |
| Cerkl.com visitors (Pixel) | Continuous | Auto via Pixel; 180-day lookback | Retargeting (cell C) |
| IG / FB account engagers | Continuous | Auto via Meta; 90-day lookback | Retargeting (cell C) |
| Existing Foundations users (exclusion) | All-time list | Refresh monthly | Exclusion from A, B |
| Paid customers (exclusion) | All-time list | Refresh quarterly | Exclusion from A, B |
