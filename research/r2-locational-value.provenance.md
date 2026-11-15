# Provenance: R2 locational value

- **Date:** 2026-09-11
- **Prompted by:** Nikhil asked for the next best question after Q0.2; R2 was the load-bearing
  gap of both research passes and Q0.2 had just supplied the addresses it needs.
- **Method:** desk join of the FAG pool list, OSM wind turbines and the TSO relief regions; centroid
  geocoding with plausibility checks; a 2 by 2 of proximity against eligibility. Lead-owned; no
  delegation.
- **Rounds:** 2 searches, 1 Overpass query (3,521 elements), 1 PDF download with local extraction,
  1 HTML fetch, about 200 Nominatim calls at 1.1 s spacing, 1 reproducible script.
- **Sources consulted:** 5 listed in the deliverable.
- **Sources accepted:** all, at the status labels stated.
- **Sources rejected:** none. SH Netz distribution-constraint data were sought and are not public;
  this is stated as the limit of the desk version.
- **Verification:** PASS WITH NOTES. The Zielmodell date, the relief-region list and the operators'
  exclusion rationale are VERIFIED from the primary document. Turbine coverage is VERIFIED as a
  query and known to be incomplete (about 6.6 of roughly 9 GW tagged). Geocoding is at postcode or
  town level. The "near wind" threshold is a stated choice.
- **Corrections in this pass:** the FAG CSV was regenerated after the raw extraction was found to
  be Latin-1 rather than UTF-8 (umlauts had been replaced); a Lübeck postcode had geocoded to
  Nordfriesland and was caught by the plausibility check. Both logged as C9 and C10.
- **Evidence files:** `research/.drafts/evidence/` now holds 25 files.
- **Script:** `r2_locational_value.py`. Run with `py r2_locational_value.py`.
- **Corrections log:** `programs/EUF-SPLASH-Flensburg/verification_log.md`, sixth pass.

## Open checks

1. Compare the concept's 3.3.3 table with the map image on netztransparenz.de (which the page
   says is the 1 October 2026 state) to confirm no Schleswig-Holstein county differs. The table is
   captioned as the trial-phase figure while the section text says it was updated for the target
   phase; the version history supports the latter.
2. Replace centroid geocodes with facility addresses (Bäderleben export carries them).
3. Obtain SH Netz constraint or congestion-area designations to build the topology proxy that
   the desk version could not.
4. Check OSM turbine coverage against the Marktstammdatenregister for Schleswig-Holstein.
