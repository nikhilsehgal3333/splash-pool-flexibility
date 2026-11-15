# Provenance: R1 electrification-conditional flexibility

- **Date:** 2026-09-11
- **Prompted by:** Nikhil asked whether the SPLASH research questions could be worked, starting
  with the lowest-hanging fruit. R1 chosen because it needs no proprietary data.
- **Method:** re-run of Wohlfarth, Klobasa & Eßer's potential-assessment logic on an electrified
  counterfactual, with the published table as the fixed point. Lead-owned; no delegation.
- **Rounds:** 6 searches, 4 PDF downloads with local `pdftotext` extraction (browser-route fetches
  fail on PDFs), 1 reproducible script.
- **Sources consulted:** 5 primary or official (Wohlfarth, Schlomann, UBA 2024, Bekanntmachung
  2021, EN 17645 via search), plus trade sources for JAZ ranges.
- **Sources accepted:** all, at the status labels stated per input.
- **Sources rejected:** none. One tool gap: `pdftoppm` not installed, so the Schlomann Tabelle 3
  column assignment for the 7.1% remainder could not be confirmed from the page image. Left
  `[verify]`; does not affect the result.
- **Verification:** PASS WITH NOTES. All quantities entering the calculation are VERIFIED by local
  extraction except the JAZ band, which is `[verify]` from trade sources, and the Schlomann carrier
  split, which is `[verify]` on column order. Both are stated as such in the result.
- **Evidence files:** `research/.drafts/evidence/` holds the two PDFs and five text extractions the
  numbers were read from, so every input can be re-checked without a network.
- **Script:** `research/r1_flexibility_calc.py`. Run with `py r1_flexibility_calc.py`.
- **Corrections log:** `programs/EUF-SPLASH-Flensburg/verification_log.md`, third pass.

## Open checks

1. A measured seasonal JAZ from one German indoor-pool heat-pump installation. Would narrow the
   headline band by roughly a third. Candidates: Passive House pool monitoring (Lünen Bambados),
   DGfdB case studies, BAFA-funded retrofits with metering obligations.
2. The Schlomann Langfassung (full report), which may state the Bäder confidence band numerically
   and may give the Tabelle 3 split unambiguously.
3. Whether a later GHD survey wave (post-2013) has superseded Schlomann 2015 as the basis for
   tertiary-sector flexibility accounting, and if so whether Baths still scores zero there.
