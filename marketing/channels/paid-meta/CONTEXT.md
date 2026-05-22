# Paid Meta — Channel Context

> What we build for Meta (Facebook + Instagram) paid campaigns and the constraints those decisions sit inside.

---

## Channel goal

Drive **Foundations sign-ups** via Meta paid ads, targeting the Foundations / Subscriber Growth ICP. Foundations is the free-forever on-ramp; paid Meta is a low-friction acquisition channel for SMB and mid-market internal-comms owners dissatisfied with Outlook / Gmail.

Why Meta vs. other paid channels:
- Foundations buyer titles are wide (Internal Comms Director → office manager / chief of staff / founder). Meta's interest + lookalike graph covers more of that range than LinkedIn's title-only targeting
- Free CTA matches Meta's strength at high-volume / low-intent traffic — easier to test than a demo-request CTA
- Cerkl already has Pixel coverage + ~115 Foundations sign-up / demo-request emails as first-party seed data

## What we run

- **Objective:** Leads (form / landing-page conversion)
- **Creative direction:** Pains concept — employee comms pain points with Outlook / Gmail, CTA = Foundations sign-up
- **Audiences:** see [audience-guidelines.md](audience-guidelines.md) — 3-cell test design for test 1
- **Geo:** US + CA
- **Placements:** Advantage+ Placements (Meta picks across Feed / Stories / Reels / IG) until reporting flags a junk placement
- **Bid strategy:** "Highest volume" (default) until CPL benchmark stabilizes; revisit cost / bid cap after 2–3 weeks of data
- **Budget structure:** **ABO** (ad-set budget optimization), not CBO — clean per-cell reads during testing. Move to CBO when scaling a proven audience.

## Key constraints

- **Free-CTA risk.** Free Foundations sign-up attracts junk traffic on Meta, especially under Advantage+ Audience. Default to constrained audiences; add quality gates (first email send within 30 days) to filter sign-ups that never use the product.
- **TK owns targeting controls.** Audience definitions for any new test need TK sign-off before spend.
- **Conversion event reliability is a hard prerequisite.** Leads-objective requires Foundations sign-up firing reliably into Pixel + Conversions API. See [system-status.md](system-status.md).
- **iOS 14.5+ aggregated event measurement.** Post-iOS attribution gaps reduce conversion signal. Use 7-day click attribution window unless TK directs otherwise. Verify domain is verified and event-priority order is correct in `system-status.md`.

## What to avoid

- **Don't default to Advantage+ Audience** on a free CTA — Meta will burn budget on consumer audiences that sign up and never return
- **Don't run more than 3 ad sets in a single test** unless the budget supports learning-phase exit per cell (~50 conversions; at $30 CPL that's ~$1,500/cell)
- **Don't optimize purely on CPL** for a free CTA — pair with a quality gate (first email send within 30 days, or engagement signal)
- **Don't add new audiences mid-test** — wait for the current test to conclude, then design the next one. Mid-test changes reset the learning phase.

## Adjacent / related work

- **Pains creative concept** — tracked in [meta-ads-channel-launch.md](../../../personal-assistant/projects/meta-ads-channel-launch.md)
- **AI video tooling** — [design-tools.md](../../../personal-assistant/projects/design-tools.md); HeyGen + alternatives exploration. Feeds the Pains-concept video asset.
- **Ad Conversion Tracking** — separate project (Segment → Google Ads). Check current state to see if Meta CAPI shares any plumbing we can reuse.
- **LinkedIn Ads** — tracked under the broader Advertising project in PA. Not in this channel's scope.

## Future work

- **paid-meta-strategy.md** — channel-level strategy doc (audience splits, campaign architecture, budget allocation rules). Add once test results give us patterns to commit to.
- **paid-meta-* creative skills** — Meta-specific storyboard + prompt skills with native aspect-ratio framing (9:16 / 1:1 / 4:5) and placement-aware composition. Fork from paid-youtube skills when divergence justifies.
- **Performance ingestion skill** — once Meta Ads API access or a stable export workflow is in place, build a skill that ingests data-exports/ CSVs and auto-appends an `Observations` block to the active experiment in `experiments-log.md`.
- **Quality-gate measurement plumbing** — wire "first email send within 30 days" as a downstream signal we can join to Meta lead data, to grade sign-up quality not just sign-up count.
