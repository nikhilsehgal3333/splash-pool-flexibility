# Process record R2: Locational value

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. Result document: `../r2-locational-value.md`. Worked 2026-09-11.

---

## Part A. One-page method summary

**Question.** The advertised geospatial package uses proximity of pools to wind and solar farms.
The regulator's own criterion for where curtailed energy may be absorbed is the §13k EnWG relief
region. How often do the two agree, for every publicly funded pool in Schleswig-Holstein?

**Sources.** Übertragungsnetzbetreiber, Umsetzungskonzept §13k EnWG, version 2.0, 1 April 2026,
section 3.3 (relief regions by Landkreis) and section 1 (target model from 1 October 2026);
netztransparenz.de relief-region page; OpenStreetMap wind generators inside the DE-SH boundary via
the Overpass API (3,521 elements, 11 September 2026); Nominatim geocoding; the 2025 FAG pool list
from Q0.2 (166 funded units).

**Method.** Each pool's Kreis was joined to the relief-region table (T5, T6, none). Each pool was
geocoded at postcode-and-town level (facility addresses are not printed in the FAG list) with a
plausibility rule that the geocode must name the facility town, the office town or the Kreis, and
was re-queried on failure. Distance to the nearest onshore turbine and the count within 5 and
10 km were computed. "Near wind" was defined as at least 10 turbines within 5 km. A 2 by 2 of
proximity against eligibility was tabulated for the 76 indoor units.

**Result.** 59 of 76 indoor units (78%) are inside a relief region. The proximity proxy agrees with
eligibility for 24 of 76 (32%): 48 units are eligible and far from wind (mostly the Hamburg belt), 4 are
near wind and ineligible, among them the Baltic-coast pools on Fehmarn, at Heiligenhafen and at
Grömitz with 18 to 27 turbines within 5 km. Campusbad Flensburg and both Kiel units are outside
any relief region. The operators' concept explains the exclusions: parts of the north were left out
because loads there would worsen congestion or TenneT never curtailed there.

**Status.** Target-model date, region list and exclusion rationale VERIFIED from the primary
document. Turbine coverage VERIFIED as a query, incomplete (about 6.6 of roughly 9 GW tagged).
Geocoding at centroid level. The "near wind" threshold is a stated choice.

**Limits.** Relief regions are a county-level regulatory criterion for one instrument, not a map
of distribution-network constraints; the operators state that distribution-level curtailment was
derived "teilweise mit Faktoren". Whether a specific pool relieves its own feeder needs SH Netz
data, which are not public.

**Files.** `r2_locational_value.py`; `r2_fag_pools_wind_proximity.csv`; evidence: concept PDF and
text, Overpass query and JSON, geocode cache; `verification_log.md` sixth pass; corrections C9,
C10, C11.

---

## Part B. Full trail

### B.1 Origin and prerequisites

1. Both research passes had flagged that distance to a generator is not the variable that
   determines congestion relief, and the state's own report attributes over 65% of Schleswig-
   Holstein's curtailment to transmission congestion ordered by TenneT, partly outside the state.
   R2 was formulated as a falsifiable test of the advertised proxy. It could not be worked until
   Q0.2 produced an address-level pool list; it was started immediately after.
2. The desk version was scoped: no distribution-network data are public, so the test would be
   the ad's variable (turbine proximity) against the best public topology-adjacent variable, the
   §13k relief regions, which are the regulator's geographic participation criterion.

### B.2 Data pulls, first round

3. Four pulls were issued in parallel. A search for the relief regions found the netztransparenz.de
   page and two versions of the operators' implementation concept (2024 and 1 April 2026). A
   search for SH Netz congestion-area designations found only network-map and expansion-plan
   pages, nothing usable at municipality level. An Overpass query for `power=generator` with
   `generator:source=wind` inside `ISO3166-2=DE-SH` returned 3,521 elements, of which 2,131 carry a
   rated-power tag summing to 6,571 MW and 7 are tagged offshore. A Nominatim geocoding pass at
   postcode-and-town level resolved 139 of 166 FAG units.
4. Decision on geocoding level: the FAG list prints the municipal office address, not the
   facility address, so facility-level coordinates were not available; postcode-and-town
   centroids were accepted with the stated consequence that distances are accurate to a few
   kilometres.

### B.3 The relief regions

5. The netztransparenz.de page was fetched. It describes the regions as "a geographic
   participation criterion", says the eight regions were "slightly expanded" for 1 October 2026,
   and refers to a map image; it does not enumerate districts in text.
6. The 1 April 2026 concept was downloaded and extracted. Section 3.3 states the regions were
   defined "auf Ebene von Landkreisen". Section 3.3.3 lists the TenneT regions in
   Schleswig-Holstein: T5 = Dithmarschen, Nordfriesland; T6 = Neumünster, Lübeck, Pinneberg,
   Rendsburg-Eckernförde, Schleswig-Flensburg, Segeberg, Steinburg, Stormarn; T6 is pooled with
   Hamburg's H1 for forecasting and tendering. A whole-document search for Flensburg (Stadt),
   Kiel, Plön, Ostholstein and Herzogtum Lauenburg returned nothing: those five are outside any
   region.
7. The same document settled an item carried at `[verify]` since the first pass: "Ab dem
   1. Oktober 2026 wechselt das Instrument in das sogenannte Zielmodell", with competitive
   tendering replacing the flat allocation. Logged as closing B2.
8. The concept's own rationale for exclusions was extracted verbatim: parts of the north of the
   TenneT zone were not included "weil dort angesiedelte Lasten einen engpassverstärkenden Effekt
   hätten oder dort durch TenneT in der Vergangenheit keine Abregelungen vorgenommen wurden"; and
   for Hamburg, loads there reduce redispatch "aufgrund von Netzengpässen südlich von Hamburg".
   Two caveats were also extracted: distribution-level curtailment volumes were derived
   "teilweise mit Faktoren", and the analyses "können in dieser Form nicht direkt auf die Zukunft
   angewendet werden".
9. One inconsistency was noted: the figure in section 3.3 is captioned "für die Erprobungsphase",
   while the section text says the regions were reviewed and updated for the Zielphase and the
   version history records "Update der Entlastungsregionen". The district list was taken as the
   target-phase designation; the caption inconsistency was logged as C11 with a `[verify]` against
   the map image.

### B.4 Geocoding, errors caught, and the parse fix upstream

10. The 27 unresolved units were retried with postcode-only queries and resolved. A provisional
    join and 2 by 2 were computed.
11. A sanity print of the city rows showed Lübeck (postcode 23552) resolving to Bordelum in
    Nordfriesland, at 54.635, 8.932, with 105 turbines within 5 km. The free-text query
    "23552 Lübeck, Schleswig-Holstein" had matched the wrong place. Logged as C10. The provisional
    T6 "near wind" count of 7 was therefore wrong.
12. A plausibility rule was added: a geocode is accepted only if its returned name contains the
    facility town, the office town or the Kreis; otherwise structured queries (city, postcode,
    state) are tried in order, then the office town. The consolidated script
    `r2_locational_value.py` was written with this rule and run.
13. The run resolved only 138 of 166. Every failure was a town with an umlaut (Lübeck, Büsum,
    Viöl, Tönning, Niebüll, Grömitz, Plön, Eckernförde, Barsbüttel, Mölln). Cause: the FAG CSV
    from Q0.2 carried replacement characters because the reading-order text extraction is
    Latin-1 and had been read as UTF-8. The script also crashed on a format directive applied to
    an empty coordinate.
14. The fix was made upstream. The FAG parser was made encoding-aware (try UTF-8, fall back to
    cp1252), the CSV was regenerated with correct umlauts and unchanged counts, hours and euros
    (166 rows, 99.93% reconciliation to the printed totals), the format guard was added, and R2 was
    re-run. Logged as C9. All 166 units resolved; Lübeck at 53.866, 10.685 with 0 turbines within
    5 km; Kiel at 54.323, 10.136 with 0; Flensburg at 54.783, 9.433 with 2.

### B.5 Analysis

15. Relief-region membership: T5 15 indoor and 26 outdoor units; T6 43 and 49; none 18 and 15.
    Indoor units inside a relief region: 58 of 76, 76%.
16. Proximity by eligibility, indoor units: T5 median nearest turbine 2.4 km (IQR 1.8 to 3.5),
    median 8 turbines within 5 km, 7 units "near wind"; T6 median 5.3 km (3.0 to 8.5), median 0
    within 5 km, 4 near; none median 5.4 km (1.9 to 6.3), median 0, 4 near.
17. The 2 by 2 for indoor units: near and eligible 11; near and ineligible 4; far and eligible 47;
    far and ineligible 14. Agreement 25 of 76, 33%.
    *Steps 15 to 17 give the figures of the first run. On 15 November 2026 one unit with an
    unresolved county (Steinburgschule, Itzehoe, owner Kreis Steinburg) was assigned to Steinburg
    and so to T6 (correction C21). Corrected: T6 44 indoor, none 17; 59 of 76 inside a relief
    region (78%); far and eligible 48; far and ineligible 13; agreement 24 of 76, 32%.*
18. Indoor units outside any relief region were listed with their turbine counts: FehMare 27,
    Aktiv-Hus Heiligenhafen 24, Grömitzer Welle 18, Möllner Welle 20, Niendorf 5, Campusbad
    Flensburg 2, Kiel 0, Plön 0, Bad Schwartau, Kirsten-Bruhn-Bad, Dahme, Aqua Siwa and Wentorf 0.
19. Evidence files were copied: concept PDF and text, Overpass query and JSON, geocode cache. The
    CSV with coordinates, geocode match, relief region and proximity metrics was written.

### B.6 How the conclusion was derived

The eligibility variable is the regulator's own criterion, taken verbatim from the operators'
concept (steps 6 to 8). The proximity variable is the ad's, computed from a complete public turbine
inventory (step 3) at a stated resolution (step 4). Because both variables are defined for every
unit, their agreement is a direct count (step 17), and the disagreement decomposes into two named
groups: the Hamburg belt, eligible because of the bottleneck south of Hamburg rather than nearby
wind, and the Baltic coast, excluded despite dense wind for the reasons the operators give
(step 8). The result is robust to the geocoding errors found and fixed (steps 11 to 14), which
moved a handful of units and did not change the direction of any cell.

### B.7 Final conclusion

In Schleswig-Holstein the geography of where curtailed energy may be absorbed under §13k is a
transmission-relief geography drawn by county. More than three quarters of the publicly funded indoor pool
stock is inside it. The advertised proximity variable predicts membership for one unit in three,
worse than chance, and it fails in both directions: it would rank the Baltic-coast leisure pools
first, which are excluded, and it would rank the Hamburg-belt pools last, which are eligible. A
geospatial package built on distance to generation would select the wrong pools. Campusbad
Flensburg and Kiel's pools are outside any relief region. The target model starts 1 October 2026.

**Status of the conclusion.** VERIFIED as to the region list, the date and the operators'
rationale; VERIFIED as a computed result on stated inputs; ESTIMATE as to distances (centroid
level). Not established: physical relief at the distribution feeder (Q0.1 stands); adjustment of
regions over time (six months' notice); facility-level proximity; OSM coverage against the
Marktstammdatenregister.

### B.8 What would change it

Facility-level coordinates from a Bäderleben export; SH Netz constraint locations to build a
topology proxy in place of county membership; a revised region cut communicated for a later
period; a substantially different turbine inventory from the official register.
