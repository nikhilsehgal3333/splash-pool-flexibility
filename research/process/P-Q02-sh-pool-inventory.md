# Process record Q0.2: Does a usable Schleswig-Holstein pool inventory exist?

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. Result document: `../q02-sh-pool-inventory.md`. Worked 2026-09-11.

---

## Part A. One-page method summary

**Question.** The project's data-acquisition package assumes the inventory must be built from
nothing. Does a usable inventory exist, at what quality, and what is genuinely missing?

**Sources.** Landtag Drucksache 20/4417 of 29 April 2026, the state government's answer on
swimming facilities, with Anlage 1 (Sportstättenerhebung 2019, Statistikamt Nord) and Anlage 2
(the 2025 FAG swimming-lesson funding list); OpenStreetMap via Overpass; Bäderleben (the national
pool database); UBA TEXTE 139/2024 for per-pool heat.

**Method.** The Drucksache was downloaded and extracted in two modes. Anlage 2 was parsed into a
table and reconciled against its own printed totals as a correctness test. Anlage 1's pool rows
were read for water surface, basin counts and ownership. An Overpass query pulled every
pool-related element inside the state boundary, which was cleaned, clustered into facilities and
scored for attribute coverage. The 2019 counts were corrected for the survey's stated 71.3%
response rate and compared with the 2025 record as a consistency check before any carry-forward
was proposed.

**Result.** An address-level administrative list of every publicly funded pool exists and is
current to 2025: 166 funded units, about 153 facilities, 107 administrative units, reconciling to
the printed totals at 99.93%. The 2019 survey supplies water surface (76,488 m²), basin counts and
ownership at 71% response. No technical inventory exists anywhere. The state says in writing that
its own data are inadequate and announces an expanded Statistikamt survey at the end of 2026. Only
nine municipalities describe their heat supply, in free text.

**Status.** All source figures VERIFIED by local extraction. The 2019-to-2025 reconciliation and
the water-surface carry-forward are labelled estimates resting on a stated non-response
assumption. The indoor share of water surface is UNRESOLVED.

**Limits.** The FAG list covers only pools receiving swimming-lesson funding; OSM includes hotel
and club pools and carries no technical attributes; the Bäderleben extract was not obtained by
script.

**Files.** `q02_fag_pools.py`, `q02_osm_pools.py`, `q02_fag2025_sh_pools.csv` (166 rows),
`q02_osm_sh_facilities.csv` (239 rows); `verification_log.md` fifth pass; corrections C7, C8.

---

## Part B. Full trail

### B.1 Origin

1. Q0.2 was one of the two Tier 0 questions in the sequencing document: everything downstream
   consumes the inventory, and if it does not exist the geospatial and modelling packages have no
   population. It was selected after R1 and R4 because it needs no proprietary data and it unblocks
   R2.

### B.2 First pulls

2. Four pulls in parallel: an Overpass query for pool-related tags inside the DE-SH boundary; a
   search for state-level pool counts; a search for the Bäderleben database; and a search for
   state pool funding programmes.
3. Overpass returned 1,180 elements. The tag distribution showed the cleaning problem immediately:
   285 elements tagged `access=private` (domestic pools), 82 `leisure=swimming_area` (natural
   bathing sites), and only 331 elements carrying a name.
4. The count search surfaced a figure of 169 indoor and outdoor pools receiving swimming-lesson
   funding in 2023, and, more importantly, Landtag Drucksache 20/4417. The Bäderleben search
   established the database's scale (over 9,300 pools, 140+ attributes) and its search interface.
   The funding search established the §24 FAG mechanism at about 7.5 m EUR a year.

### B.3 The Drucksache

5. The Drucksache PDF was downloaded and extracted in layout mode: 7,480 lines. Its structure was
   read from the table of contents: infrastructure by type, condition and age, closures,
   renovation need, school swimming, plus two annexes.
6. The Vorbemerkung was read in full and produced the pass's most consequential finding. The state
   holds no current inventory: the data lie with the municipalities, the state's figures rest on
   the 2016 survey and the 2019 Sportstättenstatistik, and the government states "die vorliegende
   Datenlage nicht auskömmlich ist bzw. aktualisiert werden muss". It then announces that the
   end-2026 FAG request will be run and expanded by the Statistikamt to collect counts per Kreis
   by type, basin counts and teaching basins, basin and water depths, locations, build year and
   last general renovation, current and decided renovations with costs, closures since 2006, and
   accessibility.
7. The summary of the 2026 replies was read: 34 administrative units answered voluntarily, 32 are
   tallied, giving 82 facilities (25 Hallenbäder, 26 Freibäder, 12 Naturbäder, 19
   Lehrschwimmbecken), 66 publicly accessible. This was recorded as a partial self-selected sample,
   explicitly not to be scaled.
8. The free-text answers were scanned for heat-supply and energetic-renovation mentions and
   attributed to their responding municipality by tracking the section headers. Nine
   municipalities: Wesselburen (heat pump for pool water, 2023/24), Büdelsdorf (air-source heat
   pump plus photovoltaics), Süderbrarup (heat pump planned, 930,957 EUR), Plön (CHP-based supply
   renewed 2021-22), Bargteheide (external supplier plans to decarbonise the CHP), Heide (seeking
   industrial waste heat), Wyk auf Föhr (planning photovoltaics, heat pump, CHP and electricity),
   Kiel and Quarnstedt (photovoltaics). This was recorded as the entire public technical inventory
   of the state.

### B.4 Anlage 2, and a parsing failure

9. Anlage 2 was located and isolated: the 2025 FAG distribution, printing every funded facility
   with municipality, address, name, type, supervised-lesson flag, lesson hours, a Maßzahl and a
   funding amount, with printed totals of 126,342 hours and 7,499,999.94 EUR against a target of
   7,500,000.
10. A first parse on the layout-mode text used a regular expression for the numeric tail. It
    returned 167 rows but only 49.7% of the printed hours and 51.9% of the funding, with 94 rows
    unclassified by type.
11. A second parse used fixed column offsets derived from the header. It reached 44.6% and 48.5%,
    worse, and produced an implausible type distribution.
12. A third parse split on runs of whitespace and consumed the row from the right. It reached
    44.6% of hours with 82 rows unclassified.
13. The failure was diagnosed rather than patched further. Line lengths were measured: rows up to
    85 were 256 characters, rows 87 onward were about 207. The landscape page is wider than the
    layout buffer, so the right-hand columns of the second half of the list were being clipped
    entirely, and on the boundary page the type column had slid by one row, mistyping for example
    "Freibad Quickborn" as Hallenbad.
14. The document was re-extracted in reading order (`pdftotext -raw`). Each facility row appeared
    complete on one line. A single regular expression matched the whole row shape, and one page's
    worth of repeated rows was de-duplicated by running number.
15. The fourth parse returned 166 rows and reconciled to 126,251 hours (99.93% of printed) and
    7,494,597.94 EUR (99.93%), with the Maßzahl column summing to 0.9992, which independently
    confirms that the Maßzahl is each facility's share of the funding pool. One row of 167 remained
    unparsed, about 91 hours and 5,400 EUR. Logged as C7; the earlier half-total parses were
    discarded.
16. The parsed table was tabulated by Kreis and type, and facilities were de-duplicated by
    municipality plus name stem (stripping basin suffixes) to separate funded units from
    facilities: 166 units, about 153 facilities, 107 administrative units, 76 Hallenbad rows,
    77 Freibad, 13 Naturbad, all flagged as offering supervised lessons.
17. A geographic pattern was noted for later use: the indoor stock concentrates in the Hamburg belt
    (Pinneberg 11, Stormarn 7, Segeberg 6) and Nordfriesland (11), while the west-coast wind
    counties carry mostly outdoor pools, which operate May to September when curtailment is lowest.

### B.5 Anlage 1

18. The 2019 Sportstättenerhebung rows were read: response rate 71.3%, down from 87.6% in 2014;
    Hallenbad (Typ 11) 32 municipal, 11 other public, 5 club, total 48; Freibad (Typ 12) 53, 5, 8,
    total 66; swimming basins 257; teaching basins 100; water surface for both types 76,488 m²;
    Hallenbad renovation or modernisation need 43.4%; users 41.2% schools and 57.1% clubs; recorded
    facilities 2014 to 2019 down 22.6% (Hallenbad) and 19.5% (Freibad), confounded by the response
    fall. The Freibad renovation cell and the 2019 absolute counts in table 5.2 were garbled in
    extraction and marked `[verify]`.

### B.6 OpenStreetMap

19. The Overpass result was cleaned: private pools and natural bathing sites removed unless the
    name contains a pool word, water features removed, leaving 714 elements. Named elements were
    clustered into facilities by name match within 300 m or pool-word match within 120 m; unnamed
    basins within 150 m of a facility were attached. Result: 239 named facilities (60 indoor,
    69 outdoor, 110 unknown), 206 basins attached, 258 unnamed orphans.
20. Attribute coverage was scored across the 239: opening hours 73, website 77, operator 42,
    building 50, length 2, and depth, heating, heated, water temperature and capacity all zero.
    This established what OSM can and cannot contribute: coordinates and names, nothing technical.
21. The OSM count exceeds the FAG count because it includes hotel, campsite, club and leisure pools
    that receive no lesson funding. The two are complementary rather than contradictory.

### B.7 Bäderleben

22. The search form was fetched and its fields identified (Bundesland, Kreis, Gemeinde, pool-type
    checkboxes, status radio, Excel and CSV export). Six scripted POST attempts with different
    parameter combinations all returned the unchanged form page; the select elements are populated
    by JavaScript and the submit path is script-driven. Two probable AJAX endpoints returned 404,
    and a state page returned 404.
23. The attempt was abandoned and documented as a two-minute browser task, with a note that
    Bäderleben was the population frame for the UBA 2024 study and is the best available bridge
    from the FAG list to basin dimensions.

### B.8 Reconciling 2019 and 2025

24. The carry-forward question was posed explicitly: the only source with water surface is six
    years old at 71% response. A consistency check was run before proposing any extrapolation.
    Correcting the 2019 counts for non-response gives 48 ÷ 0.713 = 67 indoor and 66 ÷ 0.713 = 93
    outdoor, against 2025 FAG rows of 76 indoor (about 60 to 65 facilities after basin
    de-duplication) and 90 outdoor.
25. Both types land within a few units on two independent counts, so the non-response correction
    was accepted, with the assumption that non-responders resemble responders stated rather than
    proven. On that basis water surface was carried forward to about 107,000 m² (76,488 ÷ 0.713)
    or about 112,000 m² by the per-facility route. The indoor share was left UNRESOLVED because the
    2019 table does not split it.
26. A third check: the UBA 2024 national frame of 1,390 municipal indoor and combination pools,
    scaled by the state's roughly 3.5% of national population, gives 49, close to the 2019 count
    of 48 before correction.

### B.9 Sizing the fleet

27. With about 60 heated indoor facilities and the UBA per-pool heat median 1.01 and mean
    1.21 GWh/yr, the fleet's heat is 61 to 73 GWh/yr. Electrified at seasonal performance 3.5 that
    is 17 to 21 GWh/yr of electricity, which is 2.1 to 2.6% of the 802 GWh curtailed on land in
    2025.
28. The actively shiftable portion was computed separately: about 750 kWh/K per facility (a 25 m
    pool plus a teaching pool), so about 45 MWh/K across the fleet; a fleet-wide +2 K overnight
    charge is about 90 MWh of heat and 26 MWh of electricity; 150 such nights a year gives about
    3.9 GWh, or 0.5% of curtailment. R5 later bounded this as an upper limit, because sports pools
    at 28 °C have no upward headroom within the KOK design band (C14).

### B.10 Correction logged

29. C8. The first gap map and the scan had said no inventory exists. Restated: an address-level
    administrative list exists and is current; a 2019 survey gives water surface and ownership at
    71% response; what does not exist is any technical inventory, and the state is about to
    re-survey without the technical fields the project needs.

### B.11 How the conclusion was derived

The question was answered by finding the administrative record rather than by building a list. The
FAG annex is a distribution of money, so within its scope it is complete by construction, and its
correctness was tested against its own printed totals rather than asserted (steps 9 to 15). The
older survey supplies the one quantity the funding list omits, and its usability was tested by a
non-response correction that had to agree with the current record on two independent types before
any figure was carried forward (steps 24 to 26). OSM was scored for attribute coverage rather than
counted, which is what established that it cannot contribute technically (step 20). The state's own
statement about its data (step 6) converts the finding from "the inventory is poor" into "the
inventory is about to be rebuilt by the statistical office, without the fields this project needs",
which is an actionable difference.

### B.12 Final conclusion

For counts, locations, types, ownership and funding, a usable inventory exists and is current to
2025: 166 funded units across 107 administrative units, reconciling to the state's own printed
totals at 99.93%. For water surface and basin counts, the 2019 survey carries forward defensibly
to about 107,000 m² once corrected for non-response. For technical attributes, nothing exists
anywhere: nine municipalities describe their heat supply in free text and that is the whole public
record. The state has stated its data are inadequate and is running an expanded survey at the end
of 2026 whose field list already covers much of the project's inventory package. The fleet's
electrified heat is 2.1 to 2.6% of on-land curtailment and its overnight storage shift about 0.5%,
so the pool fleet is not a volume solution to curtailment; its value is as an asset-class template
for publicly owned, uniformly governed, heat-dominated buildings.

**Status of the conclusion.** VERIFIED as to every source figure; ESTIMATE as to the carry-forward
and the fleet sizing, on stated assumptions; UNRESOLVED as to the indoor share of water surface,
one unparsed row, and the questionnaire timeline of the end-2026 survey.

### B.13 What would change it

Per-facility water surface obtained from the ministry or the statistical office, which is collected
annually for the FAG but not printed; a Bäderleben export with basin dimensions; the end-2026
survey itself, which supersedes the carry-forward entirely; and, for the fleet sizing, R5's
pool-type headroom bound applied properly rather than as an upper limit.
