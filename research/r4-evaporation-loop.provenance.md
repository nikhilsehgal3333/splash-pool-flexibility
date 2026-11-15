# Provenance: R4 evaporation loop

- **Date:** 2026-09-11
- **Prompted by:** Nikhil chose R4 as the second research question to work, after R1.
- **Method:** first-order steady-state physical model. Evaporation per VDI 2089 (via DGfdB) with
  Shah 2014 as cross-check; losses from latent heat and makeup water; vapour removal by fresh-air
  dilution or heat-pump condensing at datasheet specific energies. Calibrated against the official
  Schwimmhallen benchmark and the UBA 2024 facility mean before any result was read.
  Lead-owned; no delegation.
- **Rounds:** 6 searches, 4 PDF downloads with local `pdftotext`, 3 HTML fetches (2 failed:
  redirect loop, paywall), 1 reproducible script.
- **Sources consulted:** 8 listed in the deliverable.
- **Sources accepted:** all, at the status labels stated.
- **Sources rejected:** none. Two fetch failures (tga-fachplaner VDI 2089 article, tab.de
  dehumidifier article) left the "0.71 kWh/kg specific heat requirement" figure at `[verify]`; it
  is not used, since latent heat is a physical constant.
- **Verification:** PASS WITH NOTES. VDI coefficients, Shah constants, datasheet figures, and the
  Benakcha et al. statements are VERIFIED by local extraction. The 14.3 g/kg humidity cap, the
  specific fan power, the fan-power attribution in recirculation mode, the heat-recovery
  efficiency, the occupancy density and the pool geometry are `[verify]` or stated assumptions.
  Benakcha et al.'s numerical results are UNRESOLVED (illegible in extraction).
- **Evidence files:** `research/.drafts/evidence/` now holds 15 files including the four new PDFs
  and their extractions.
- **Script:** `research/r4_evaporation_loop.py`. Run with `py r4_evaporation_loop.py`.
- **Corrections log:** `programs/EUF-SPLASH-Flensburg/verification_log.md`, fourth pass.

## Open checks

1. Read Benakcha et al. (2025) visually for the overheating temperatures tested, the percentage
   savings, and the evaporation reduction from setpoint decrease. The PDF is on disk.
2. Confirm the VDI 2089 absolute-humidity limit (14.3 g/kg) from the standard itself or a
   secondary source that quotes it.
3. One measured dynamic response from a German indoor pool (temperature rise and fall times) to
   replace the steady-state assumption. The Eckernförde case named in the original gap file is a
   candidate if it exists.
4. A dehumidification unit's control logic across a year, to place real hours inside the 0.12 to
   0.38 kWh/kg band.
