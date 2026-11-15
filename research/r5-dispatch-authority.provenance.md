# Provenance: R5 dispatch authority and cost of participation

- **Date:** 2026-09-11
- **Prompted by:** Nikhil asked for the next step after R2; R5 was next in the sequence and the
  §13k eligibility rules had become concrete enough to test against a pool.
- **Method:** desk legal-institutional analysis from primary texts (statute, regulator's
  determination, TSO concept, IfSG, the KOK table as reproduced by the Städtetag, the ministry's
  guidance on enterprise forms), plus a first-order single-site cost-benefit with every input
  labelled. Lead-owned; no delegation.
- **Rounds:** 4 searches, 3 statute or determination fetches, 2 PDF downloads with local
  extraction, 5 failed portal fetches (juris redirect loop, umwelt-online certificate, gesetze.io
  and Haufe JavaScript shells, ministry page 404), 1 reproducible script.
- **Sources consulted:** 9 listed in the deliverable.
- **Sources accepted:** all, at the status labels stated.
- **Sources rejected:** none; the GO SH statute text could not be retrieved from any portal and
  its wording is carried at `[verify]` on two consistent secondary summaries.
- **Verification:** PASS WITH NOTES. Statute, Tenor, concept mechanics, IfSG §37 and the KOK
  table are VERIFIED verbatim. §101a wording, the EigVO reserved-decision list, the BDEW price
  figure, the aggregator fee band and the Legionella threshold are `[verify]`. The cost model's
  one-off and annual costs, the residual 10 EUR/MWh, the headroom fractions and the plant sizes
  are stated assumptions.
- **Corrections in this pass:** C12 (scope of the CHP exclusion), C13 (scope of the 2% rule),
  C14 (R4's charge assumption against the KOK band), C15 (minimum availability applies to
  fixed-charge compensation only). All logged.
- **Evidence files:** `research/.drafts/evidence/` now holds 30 files.
- **Script:** `r5_participation_cost.py`. Run with `py r5_participation_cost.py`.
- **Corrections log:** `programs/EUF-SPLASH-Flensburg/verification_log.md`, seventh pass.

## Open checks

1. Read §5 EigVO SH (council-reserved decisions) and §101a GO SH from the juris portal in a
   browser; both resisted scripted retrieval.
2. Obtain one real aggregator term sheet for a 100 to 200 kW steerable heat load.
3. Ask SH Netz whether a connection confirmation for §13k loads has been adopted.
4. Read the BDEW Strompreisanalyse PDF for the exact 2025/2026 figures by consumption band.
5. Confirm the Legionella temperature threshold from DIN 19643 or the UBA recommendation.
