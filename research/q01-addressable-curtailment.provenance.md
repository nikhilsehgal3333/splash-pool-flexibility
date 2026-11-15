# Provenance: Q0.1 addressable curtailment

- **Date:** 2026-09-11 to 2026-09-12
- **Prompted by:** Nikhil asked what remained besides R3; Q0.1 was identified as the other
  unanswered Tier 0 question and he chose it. It had been recorded in R2 and in the sequencing
  document as blocked on non-public SH Netz data. That assessment was revisited at the start of
  this pass and found to be too strong: three public source classes bear on it directly and none
  had been pulled.
- **Method:** primary-source causation analysis rather than data modelling. The state ministry's
  full report, the network operator's own planning documents across three editions, the statutory
  distribution-operator provision and the TSO-DSO coordination outcome were read verbatim and
  cross-checked against federal figures. A county-level join of the pool list to the operator's
  medium-voltage congestion regions was added as the spatial component. Lead-owned; no delegation.
- **Rounds:** 5 searches, 6 PDF or spreadsheet downloads with local extraction, 4 HTML fetches
  (2 returned 403, 1 returned only pre-2024 data), 1 Overpass query (4,776 substations), 1
  reproducible script written twice (see corrections).
- **Sources consulted:** 9 listed in the deliverable.
- **Sources accepted:** all, at the status labels stated.
- **Sources rejected:** none. Several routes failed and are documented: the SH Netz per-county
  measure pages all return 404; the network-information page and the per-county pages return 403 to
  the fetch tool; the Bundesnetzagentur congestion page carries nothing later than 2023; the
  netztransparenz redispatch export covers transmission-operator measures only, so it cannot supply
  a distribution-level breakdown.
- **Verification:** PASS WITH NOTES. The 65% volume share, the over-90% case share, the repeated
  causal statement in three plan editions, the §13k Abs. 8 text, the distribution operators'
  declared position, the twelve congestion regions with their overload shares, and the federal
  causation split are all VERIFIED by local extraction. The composite arithmetic (about 3%
  distribution-caused) is labelled indicative, because it combines a 2026 volume share with a 2017
  case share. The Kiel distribution operator is `[verify]`.
- **Evidence files:** `research/.drafts/evidence/` now holds 41 files. The Netzausbauplan 2024 PDF
  is 55 MB and only its text extraction was kept.
- **Script:** `q01_dso_congestion_join.py`. Run with `py q01_dso_congestion_join.py`.
- **Corrections log:** `programs/EUF-SPLASH-Flensburg/verification_log.md`, eighth pass.

## Open checks

1. A current quantification of the distribution-caused share from SH Netz, replacing the 2017
   over-90% figure. The narrow version of the request is now: "of the curtailment you instructed in
   2024 and 2025, how much had its cause in your own network".
2. The trigger split (load-driven versus generation-driven) for each of the twelve congestion
   regions, garbled in extraction. It decides whether an added load in a region helps or worsens
   the projected congestion, which is the same question the TSOs answer for the relief regions.
3. Whether the §13k Abs. 8 threshold was formally tested for SH Netz or judged not worth pursuing.
4. The distribution operator for Kiel, and whether Kiel and Flensburg publish their own network
   development plans with congestion regions.
5. Feeder-level assignment for individual pools, which remains the only genuinely operator-held
   piece and is now a narrower ask than before this pass.
