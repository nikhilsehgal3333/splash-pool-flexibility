# Provenance: Q0.2 Schleswig-Holstein pool inventory

- **Date:** 2026-09-11
- **Prompted by:** Nikhil chose the next question after R1 and R4; Q0.2 was first on the list and is
  the foundation R2 needs. Mid-task he asked whether current figures must be extrapolated from the
  2019 baseline; §3 of the result answers that.
- **Method:** desk inventory from three source classes: an official parliamentary document with two
  statistical annexes, an OpenStreetMap extract, and the national pool database. The FAG annex was
  parsed from a reading-order text extraction after layout-mode extraction proved to clip the
  landscape page at 256 characters; the parse was reconciled against the annex's own printed
  totals. Lead-owned; no delegation.
- **Rounds:** 5 searches, 1 Overpass query, 1 PDF download with two extraction modes, 6 HTTP
  probes of Bäderleben (all returned the unchanged form), 2 reproducible scripts.
- **Sources consulted:** 5 listed in the deliverable.
- **Sources accepted:** all, at the status labels stated.
- **Sources rejected:** none. Bäderleben's SH extract was not obtained (JavaScript-driven form);
  documented as a browser task rather than scripted.
- **Verification:** PASS WITH NOTES. The Drucksache's 2026 sample, the FAG 2025 list, the 2019
  Sportstättenerhebung counts and water surface, and the OSM query are VERIFIED by local extraction
  or direct query. The 2019-to-2025 reconciliation and the water-surface carry-forward are
  labelled estimates resting on a stated non-response assumption. The indoor share of the 2019
  water surface is UNRESOLVED. One FAG row of 167 did not parse (0.07% of hours).
- **Evidence files:** `research/.drafts/evidence/` now holds 21 files, including the Drucksache PDF,
  both text extractions, the Anlage 2 extract, the Overpass query and its JSON.
- **Scripts:** `q02_fag_pools.py` (FAG parse, reconciliation, Kreis table, CSV) and
  `q02_osm_pools.py` (Overpass query, cleaning, clustering, attribute coverage, CSV).
- **Corrections log:** `programs/EUF-SPLASH-Flensburg/verification_log.md`, fifth pass.

## Open checks

1. Identify the one unparsed FAG row (about 91 hours, EUR 5,400) by comparing the CSV's 166 running
   numbers against 1 to 167.
2. Resolved 15 Nov 2026 (C21): the row with municipality ID 99xx (one Hallenbad, 546 hours) is
   the Steinburgschule in Itzehoe, owner Kreis Steinburg.
3. Obtain per-facility water surface from MIKWS or the Statistikamt; it is reported annually for the
   FAG and is the basis of the Maßzahl, but is not printed in Anlage 2.
4. Export the Bäderleben SH list in a browser (Bundesland = Schleswig-Holstein, alle Badtypen,
   Suchen, Daten exportieren) for basin-level dimensions.
5. Read the 2019 Anlage 1 tables 2.1 (Freibad renovation need) and 5.2 (2019 absolute counts) from
   the PDF page images; the text extraction garbles those cells.
6. Find the questionnaire design timeline for the end-2026 Statistikamt FAG survey; the window to
   add SPLASH's parameters closes before the project's first quarter ends.
