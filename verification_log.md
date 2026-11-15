# Verification log: EUF SPLASH (Flensburg)

**Date:** 2026-09-08
**Prompted by:** research-gap map for the SPLASH interview, and assessment of
`splash-gaps.md`.
**Method:** `README.md`.

## Corrections

**C1: The curtailment premise in `splash-gaps.md` is stated without its trend or its cause.**
The document says Schleswig-Holstein "still experiences significant curtailment of onshore
renewables" (§1). True but incomplete in two ways that change the argument.
*What is true:* on-land curtailment by SH Netz AG fell from roughly 3,350 GWh in 2019 to 825 GWh in
2025 across all on-land sources, about 75% down. Onshore-specific: 812 GWh / EUR 78.4m in 2024,
802 GWh / EUR 74.2m in 2025. **More than 65% of these curtailments are carried out at the request of
the upstream operator TenneT and stem from transmission-network congestion, partly outside
Schleswig-Holstein.** VERIFIED, Schleswig-Holstein state grid-expansion report, page updated
15 Apr 2026.
*Consequence:* the geospatial work package as framed ("proximity of pools to local wind/solar
farms") may be measuring the wrong adjacency. If two-thirds of curtailment is instructed from the
transmission level, a distribution-connected pool near a wind farm has no automatic claim on that
energy. This is the load-bearing finding of the pass and it should be raised as an open research
question, not hidden.

**C2: `splash-gaps.md` describes the post as half-time.**
*What it says:* "one half-time research associate" (§2.2.9, and implied in §8.6).
*What is true:* the advertisement states Vollzeit (full-time), fixed term to 30 Sep 2027.
*Consequence:* minor factually, but it is the kind of slip that reads as not having read the ad.

## Blocked checks

**B1: Finland swimming-hall paper, quantitative results. UNRESOLVED.**
Hasan et al., *Energy and Buildings* 248, 111149 (2021). Citation VERIFIED from two independent
listings (ScienceDirect and the Aalto repository). Both returned HTTP 403 on fetch, so the reported
shifted energy, temperature bands and cost savings could not be read. Do not cite figures from this
paper until it has been read.

**B2: §13k EnWG phase-3 / target-model start date. [verify].**
A dena workshop deck was reported in search as giving phase 3 (target model) from October 2026. The
PDF would not parse. Independently VERIFIED from FfE: the trial phase began October 2024 and runs
about two years, so a transition around October 2026 is consistent, but the specific phase-3 label
and date are unconfirmed. Confirm from the Bundesnetzagentur determination.

## VERIFIED findings

- **§13k EnWG "Nutzen statt Abregeln" eligibility and non-use.** Eligible loads include
  fossil-heat-replacing installations (heating rods, hybrid heat pumps), grid-connected storage, and
  electrolysers and large heat pumps above 100 kW. Additionality: at most 2% full-load hours in the
  previous month, or investment additionality through operation after 29 Dec 2023. Trial from
  October 2024, roughly two years. **"The instrument has not yet been used despite the existing
  supply"**: essentially no allocations to loads since October 2024. Source: FfE assessment.
- **Schleswig-Holstein curtailment volumes and costs**, as in C1. Source: state government
  Engpassmanagement page, updated 15 Apr 2026.
- **OSeEM-SN and OSeEM-DE exist** as open sector-coupled models from ZNES Flensburg, oemof-tabular
  based, OSeEM-SN validated on Schleswig-Holstein. Existence VERIFIED from public repositories plus
  an associated preprint (arXiv:2102.07267). Contents of the heat representation remain `[verify]`.
- **Hasan et al. (2021) exists** in *Energy and Buildings* 248, 111149, on demand-response potential
  of district heating in a Finnish swimming hall. Citation VERIFIED, contents UNRESOLVED per B1.

## DO NOT CITE

- **Every `[web:N]` marker in `splash-gaps.md`.** Roughly 100 markers, no source list anywhere in the
  document's 286 lines. None resolves to a checkable source. Under `verification.md` none may enter
  a deliverable, and none should be asserted in the interview. This is the document's FATAL defect
  in the sense of `critique.md`.

## Carried at [verify]: plausible, unchecked, must not enter a deliverable

Pool heat demand roughly four times electrical demand; average German indoor pool around
2,400 MWh/yr; about 6,000 public pools in Germany; a 2 K water-temperature reduction saving roughly
a quarter to a third of thermal energy; KfW figures of 14% of indoor and 16% of outdoor pools facing
closure within three years without renovation; the Hamburger Energiewerke "Karoline" §13k precedent
of March 2025; the pool flexibility-savings-index study. All from trade, press or search-summary
sources only.

---

# Second pass: 2026-09-08, independent multi-perspective scan

**Prompted by:** an isolated cold-context scan run to cross-check the first gap map
(`perspectives_splash.md`). Isolation held: the scan did not read the first map, its provenance,
plan, this log, or `splash-gaps_ORIGINAL.md`.

## VERIFIED by direct extraction (this session)

**Wohlfarth Table 4, the "Baths" zero row.** The scan's headline finding is correct. Confirmed by
downloading the Fraunhofer ISI PDF and extracting text locally with `pdftotext -layout`, after two
browser-route fetches failed to parse.

Table 4, "Electricity consumption in tertiary sectors (including service) 2013
(Schlomann et al. 2015)". Row `Baths`: lighting 0.2, mechanical power 1.1, hot water 0.0, other
process heat 0.0, process cold 0.0, AC 0.0, ICT 0.0, space heating 0.0, **total 1.4 TWh/a, sum of
relevant shares 0.0**. The final column is defined in the text as "the sum of the consumption of the
flexible appliances". **VERIFIED.**

## CORRECTED

**C3: "the only zero in the table" is wrong.** The scan (F1, and its report) states that Baths is
the only tertiary subsector with a zero flexible share.
*What is true:* **Laundries also scores 0.0**, on 0.3 TWh/a total. Two subsectors score zero, not
one.
*Consequence:* the finding survives and should be restated as **"Baths is the larger of only two
tertiary subsectors scoring zero flexible electricity, at 1.4 TWh/a against Laundries' 0.3 TWh/a."**
Do not say "the only zero" out loud. The methodological point is unaffected, and arguably
strengthened: both zeros are heat-and-water-dominated subsectors, which is consistent with the
claim that the method is blind to thermal flexibility under fossil supply rather than blind to
baths specifically.

**C4: citation version and author name.** The scan cites "Wohlfarth, Klobasa, Esser (2018),
*Energy Efficiency*, doi:10.1007/s12053-018-9728-3".
*What is true:* the PDF carries "© The Author(s) 2018" and the DOI above, so 2018 is the
online-first year; the journal issue is **Energy Efficiency (2019) 12, 327-341** **[verify]** on the
exact page range, which came from a search summary. Third author is **Anke Eßer**, not "Esser".
*Consequence:* per `verification.md` check 1, cite the issue and note the online-first date. Fix the
eszett before this appears in anything.

## Convergent findings across two independent passes

Reached separately, from separate contexts, by separate search paths. Convergence means reachable
by more than one route, not confirmed: both passes share the same model priors.

- **SH curtailment figures and their upstream cause.** 802 GWh / EUR 74.2 m (2025) and 812 GWh /
  EUR 78.4 m (2024) from SH Netz AG; 825 GWh across all on-land sources in 2025; **over 65% ordered
  by TenneT for transmission congestion partly outside the state.** Both passes reached the same
  MEKUN report. The second pass adds: 3.6% of onshore generation curtailed in 2025 against over 17%
  in 2015, onshore generation at an all-time high of 22.3 TWh, and the state's expectation that
  volumes may rise again until post-2028 HVDC commissioning. **VERIFIED.**
- **The geospatial work package uses the wrong proximity variable.** Both passes independently
  concluded that distance to a generator is not the variable that determines congestion relief.
- **Fleet-scale, congestion-driven pool flexibility is untested.** Both found the prior literature
  single-asset and price-driven. The second pass adds two anchors the first missed: Banaei et al.,
  *IJEPES* 145, 108643, and Almassalkhi et al. 2026, arXiv:2604.19933.
- **§13k EnWG is live and relevant.** Both found it. The second pass adds the BNetzA determination
  of 28 June 2024, the restriction to relief regions and aggregators, and **the exclusion of
  installations under existing TSO contracts with CHP plants**, which matters, because pools
  commonly have CHP.
- **The §13k phase-3 October 2026 date remains [verify] in both passes.** Two independent runs both
  failed to source it beyond the dena slides. Treat as unconfirmed.
- **No public description of SPLASH exists.** Neither pass found the project on any EUF department
  page. **UNRESOLVED.** All analysis rests on the advertisement alone.

## Findings unique to the second pass, carried forward

- **F1 electrification-conditional flexibility potential** (above). The strongest single finding of
  either pass.
- **Blind spot B, the evaporation-humidity-electricity loop.** Raising water temperature to charge
  the store raises evaporation, which raises the dehumidification and ventilation electrical load in
  the same building. No pool-flexibility model closes this loop. **[verify]**: Yuan et al. use IDA
  ICE and may already model the HVAC side, so read that paper before asserting the absence.
- **The winter 2022/23 EnSikuMaV episode as a natural experiment.** Roughly 2 K fleet-wide
  reductions in the exact control variable, with pre-period, dated treatment and outcomes
  municipalities already record. **VERIFIED** for the regulation (in force 26 Aug 2022, last amended
  13 Feb 2023); **[verify]** for the 2 K figure and the visitor and staff reactions, which come from
  regional press. Data availability is **UNRESOLVED** and perishable.
- **Blind spot A, the service-quality exchange rate.** Water temperature in a public pool is a
  health and access parameter for infants, therapy users and school swimming, not a comfort dial.
  Nobody has priced what is spent per kWh shifted, or asked which user group pays.
- **The efficiency-flexibility frontier.** Every kWh of heat demand removed by retrofit is a kWh of
  flexibility that no longer exists. The 1979-1984 EU pool programme chose efficiency; the retrofit
  wave will choose it again. Frontier undrawn for this asset class.
- **Flensburg already runs SPREAD.SH and reGon** alongside oemof and OSeEM. **VERIFIED** from
  department pages. Proposing to build what the group already has would read badly.

## Standing methodological warning, from the scan's own self-review

Its absence claims (no German public-pool fleet study, no institutional-operator instrument, no
service-quality costing) rest on keyword search, not a documented protocol. They are **UNRESOLVED**,
not established. State them as "I did not find", never as "there is not". This applies equally to
the first pass's equivalent claims.

---

# Third pass: 2026-09-11, R1 desk calculation

**Prompted by:** working the first research question (electrification-conditional flexibility).
All PDFs read by local `pdftotext` after browser fetches failed to parse them. Extractions filed in
`research/.drafts/evidence/`.

## VERIFIED by direct extraction

- **Schlomann et al. 2015, Kurzfassung, Tabelle 1, group 5/3 Bäder (TWh):** 2013 = Strom 1.4,
  Brennstoffe/Kraftstoffe/Fernwärme 2.9, Summe 4.3. Series 2006 to 2013: 5.7, 6.4, 7.2, 6.7, 6.1,
  5.2, 4.3, 4.3. The 1.4 TWh electricity matches Wohlfarth Table 4 exactly, confirming the two are
  the same dataset.
- **Schlomann Tabelle 3, Bäder application split:** electricity 14.3% lighting, 78.6% mechanical
  power (matches Wohlfarth's 0.2 and 1.1 of 1.4 TWh); fuels 92.9% "sonstige Prozesswärme". The
  column carrying the remaining 7.1% (Warmwasser or Raumheizung) could not be pinned from the
  extraction layout; `pdftoppm` is not installed to check the page image. **[verify]** on that
  column only.
- **Schlomann Tabelle 2, Bäder carriers 2013:** gas 0.9, wood 0.3, district heat 1.6, sum 2.8 TWh;
  Bezugseinheit 4,650 thousand m² water surface. Column order checked against the Beherbergung row
  (sums correctly). Carried at **[verify]** because the DH-over-gas ordering is surprising and the
  wood figure is unexpected for this group.
- **Schlomann's own confidence statement:** fuel and district-heat deviations are ±5% to just
  under ±15% for the remaining groups "mit Ausnahme der Bäder". The Bäder fuel figure therefore
  carries a wider band than ±15%. Stated in the R1 result as a caveat.
- **Weinfurter, Thieme & Wallrodt 2024, UBA TEXTE 139/2024, Tabelle 4 (n = 1,390 municipal indoor
  and combi pools, Bäderleben):** heat 1,339.93 GWh (model) / 1,636.22 GWh (simple); electricity
  396.28 / 482.07 GWh; total 1,791.40 / 2,118.29 GWh. Survey years 2019 and 2022; n = 67 complete
  responses; water surface known for n = 526. Per-pool mean heat 1.21 GWh, electricity 0.36 GWh
  (Tabelle 1). Carrier mix by count: 53.7% gas, 44.8% district heat. Pools = 0.55 to 0.65% of GHD
  final energy and 0.08 to 0.09% of national final energy (2022, AGEB).
- **Wohlfarth Table 3 flexible appliances** include "Heat pump/recirculation pump" (space heating)
  and "Electric water heating" (hot water). This is what licenses the counterfactual: electrified
  pool heat falls inside the authors' own flexible categories.
- **Bekanntmachung 2021, category 32 Schwimmhallen, Teilenergiekennwerte (kWh/m²a):** Heizung
  63.8, Warmwasser 8.3, Lüftung 13.4, Beleuchtung 1.9, Kälte 1.1, Be- und Entfeuchtung 30.0,
  Sonstiges 7.3; plus a 90 kWh/m²a surcharge for pool-water heating where not separately metered.
  Not used in R1. The 30.0 dehumidification value is direct evidence for the R4 evaporation loop.

## CORRECTED

**C5: the "heat is roughly four times electricity" figure.** Carried at `[verify]` from trade
press in the first pass.
*What is true:* the UBA 2024 respondents (n = 67) show mean heat 1.21 GWh against mean electricity
0.36 GWh per pool, a ratio of about 3.4; the authors themselves write "knapp über ein Vierfaches",
which their own means do not quite support. At sector level (Schlomann 2013, all baths) the ratio
is 2.9 to 1.4, about 2.1, because outdoor pools are electricity-heavier.
*Consequence:* say "three to four times for indoor pools, about two at sector level", not "four".

## Carried at [verify]

- Seasonal heat-pump performance for pool water: 3.0 / 3.5 / 4.5 used as low / central / high.
  General installation-type ranges from trade sources; no pool-specific measured JAZ found.

## UNRESOLVED

- Whether a post-2013 GHD survey wave has replaced Schlomann 2015 in tertiary flexibility
  accounting, and whether Baths still scores zero there.

---

# Fourth pass: 2026-09-11, R4 evaporation loop model

**Prompted by:** working the second research question. All PDFs read by local `pdftotext`;
extractions filed in `research/.drafts/evidence/`.

## VERIFIED by direct extraction

- **VDI 2089 evaporation coefficients** (via the DGfdB calculation note): Dalton form
  W = ε·A·(Ps − Pd) in g/h; ε = 5 g/(hPa·m²·h) at rest, 15 residential, 15 to 20 hotel, 20 Hallenbad
  in operation, 28 Freizeitbad, 35 Wellenbad. Worked example: water 27 °C (35.6 hPa), air 30 °C at
  52% (22.48 hPa, "Schwülegrenze"): 262.4 g/m²h in operation, 66.0 at rest. The note itself warns the
  formula is for plant sizing and actual losses may deviate.
- **Shah 2014 (ASHRAE SE-14-001) correlation constants:** E0 = larger of
  C·ρw·(ρr − ρw)^(1/3)·(Ww − Wr) with C = 35 SI, and b·(pw − pr) with b = 0.00005 SI (p in Pa);
  occupied multiplier Eocc/E0 = 1.9 − 21·(ρr − ρw) + 5.3·N* for N* ≥ 0.05. Shah reports the Carrier
  and ASHRAE handbook method as inaccurate against test data.
- **Benakcha, Labat, Hazyuk, Ginestet (2025), arXiv:2512.02586:** semi-Olympic pool, Toulouse; uses
  Shah; evaporation about two-thirds of water heat loss; overheating tested as solar storage;
  unoccupied measurements discarded because the AHU's energy-recovery strategy complicated them,
  AHU impact "neglected as a first approximation"; and verbatim: "further investigations are
  required to confirm whether the repercussions of overheating on the air circuit can be managed
  for a low energy cost. This falls within the perspectives of this work and the future scope of a
  second article." Numerical results (overheating temperatures, % savings) are illegible in the
  extraction: **UNRESOLVED** pending a visual read.
- **Menerga ThermoCond 19 datasheet (2016), five sizes:** Entfeuchtungsleistung nach VDI 2089
  7.1 / 9.7 / 12.9 / 16.2 / 22.6 kg/h; elektr. Gesamtaufnahmeleistung 0.94 (smallest) to 2.66 kW
  (largest); Entfeuchtungsleistung im Umluftbetrieb 4.6 / 5.2 / 6.9 / 8.5 / 12.0 kg/h;
  Verdichteraufnahmeleistung 1.4 / 1.3 / 1.7 / 1.9 / 2.9 kW; Ventilatoreinheiten 0.60 / 0.65 /
  0.89 / 1.00 / 1.70 kW; Heizleistungszahl Wärmepumpe (COP) 5.14 / 6.42 / 5.82 / 6.61 / 6.14;
  Beckenwasserkondensator option 6.4 to 15.5 kW. Derived specific electricity: 0.118 kWh/kg at the
  VDI point, about 0.38 kWh/kg in recirculation (compressor plus fans; the fan attribution is
  **[verify]**).
- **Model calibration:** baseline 460 t/yr evaporation, 312 MWh_th/yr latent, 55 to 175 MWh_el/yr
  dehumidification across the specific-energy band, against the Bekanntmachung's 30 kWh/m²a
  (about 90 MWh/yr at 3,000 m² NGF) and the UBA facility mean of 1.21 GWh heat. Within a factor of
  about 1.5 on both.

## Status change on a scan finding

**Blind spot B of `perspectives_splash.md`** ("no pool-flexibility model closes the
water-heat-humidity-electricity loop") was carried at `[verify]` with the note that Yuan et al. 2021
might already model the HVAC side. It is now better supported than that: the nearest paper to
have tested pool overheating states in its own text that the air-circuit consequence is unanalysed
and deferred to a future article. Upgrade to **VERIFIED as an open question in the nearest prior
work**. The absence claim across the whole literature remains **UNRESOLVED** (no systematic
protocol); Yuan et al. 2021 still unread.

## CORRECTED

**C6: the scan's framing that the loop "may decide whether the asset class is viable".**
*What the model shows:* the loop does not decide viability; it decides the operating regime.
Overnight charging at rest costs 2 to 3% of stored heat and 0.5 to 4.4% of shifted electricity.
A charge held through twelve bathing hours costs 19 to 25% of stored heat and, in summer with
recirculation dehumidification, about 35% of shifted electricity.
*Consequence:* state it as a regime constraint (overnight product, seasonal), not as a viability
threat. The scan's instinct was right in direction and overstated in degree.

## Carried at [verify] or as stated assumptions

14.3 g/kg absolute-humidity cap (VDI 2089 comfort limit, commonly quoted, not read from the
standard); specific fan power 2.0 kW/(m³/s); heat-recovery efficiency 70%; occupancy density
0.10 per m²; reference geometry 312.5 m² by 1.8 m; the Eckernförde dynamic-response claim from the
original gap file; the 0.71 kWh/kg "specific heat requirement" figure from the unreachable
tga-fachplaner article (not used).

---

# Fifth pass: 2026-09-11, Q0.2 inventory

**Prompted by:** working the inventory question. Drucksache read by local `pdftotext` in layout and
raw modes; Overpass queried directly; Bäderleben probed by HTTP.

## VERIFIED by direct extraction or query

- **Landtag Drucksache 20/4417 (29 Apr 2026), Vorbemerkung:** the state's pool data rest on the
  2016 survey (Drs. 18/5297) and the 2019 Sportstättenstatistik; the government calls the data
  "nicht auskömmlich"; the end-2026 FAG request will be run and expanded by the Statistikamt to
  collect counts per Kreis by type, basin counts, basin and water depths, locations, build year and
  last general renovation, current and decided renovations with costs, closures since 2006, and
  accessibility. 34 administrative units answered the 2026 request voluntarily.
- **Drucksache summary of the 2026 replies (32 units):** 82 facilities; 25 Hallenbäder, 26 Freibäder,
  12 Naturbäder, 19 Lehrschwimmbecken; 66 publicly accessible; 22 of 25 Hallenbäder public; 6 of 19
  Lehrschwimmbecken public.
- **Heat-supply mentions in the 2026 replies (prose):** Wesselburen heat pump 2023/24; Büdelsdorf
  air-source heat pump plus PV; Süderbrarup heat pump planned, EUR 930,957; Plön CHP renewed
  2021-22; Bargteheide CHP decarbonisation planned by external supplier; Heide seeking industrial
  waste heat; Wyk auf Föhr plans PV, heat pump, CHP and electricity; Kiel and Quarnstedt PV. Nine
  municipalities in total.
- **Anlage 2, FAG 2025 list:** printed totals 126,342 supervised lesson hours and EUR 7,499,999.94
  (target 7,500,000). Parsed 166 of 167 rows: 126,251 hours (99.93%), EUR 7,494,597.94 (99.93%),
  Maßzahl sum 0.9992 (confirming Maßzahl = funding share). 107 administrative units. Types:
  Hallenbad 76, Freibad 77, Naturbad 13; teaching basins are typed Hallenbad; some facilities are
  listed per basin. All 166 rows flagged "angeleitet = Ja".
- **Anlage 1, Sportstättenerhebung Dezember 2019 (Statistikamt Nord):** response 71.3% (87.6% in
  2014). Hallenbad Typ 11: 32 municipal, 11 other public, 5 club = 48. Freibad Typ 12: 53, 5, 8 = 66.
  Swimming basins Typ 11+12: 257; teaching basins: 100; water surface Typ 11+12: 76,488 m².
  Hallenbad renovation/modernisation need 43.4%. Hallenbad users 41.2% schools, 57.1% clubs.
  Recorded facilities 2014 to 2019: Hallenbad −22.6%, Freibad −19.5%.
- **OpenStreetMap, Overpass, 11 Sep 2026:** 1,180 elements in DE-SH across pool tags; 714 after
  removing private pools and natural waters; 239 named facilities after clustering; technical
  attribute coverage effectively zero (depth 0, heating 0, water_temperature 0).
- **Bäderleben:** search form exists with Bundesland/Kreis/Gemeinde/Badtyp filters and Excel or CSV
  export; the form is JavaScript-driven and returned the unchanged page to six scripted POSTs.

## CORRECTED

**C7: layout-mode extraction of Anlage 2 is wrong for rows 86 to 167.** The landscape page is
wider than pdftotext's layout buffer (lines clipped at 256 characters), so type and figures were
lost for the second half and the type column slid by one row on the boundary page (e.g. "Freibad
Quickborn" typed Hallenbad). *What is true:* reading-order extraction (`-raw`) has every row on one
line, and parsing it reconciles to the printed totals at 99.9%. *Consequence:* the earlier
half-total parses were discarded; only `q02_fag2025_sh_pools.csv` from the raw parse stands.

**C8: "no inventory exists" (first gap map §7, and the scan) is too strong.** *What is true:* an
address-level administrative list of every publicly funded pool exists and is current to 2025; a
2019 survey gives water surface, basin counts and ownership at 71% response; what does not exist is
any technical inventory (carrier, plant, volume, temperature), and the state confirms its own data
are inadequate and is about to re-survey. *Consequence:* restate the gap as "no technical inventory,
and a state survey about to run without the technical fields SPLASH needs."

## Estimates (stated assumptions, not findings)

- 2019 counts ÷ 0.713 response: indoor 67, outdoor 93; against 2025 FAG rows 76 indoor (about
  60-65 facilities after basin de-duplication) and 90 outdoor. Assumes non-responders resemble
  responders.
- Water surface 2025: about 107,000 m² (76,488 ÷ 0.713) or 112,000 m² (671 m² per facility × 167).
  Indoor share **UNRESOLVED**.
- Fleet heat: about 60 indoor facilities × 1.01 to 1.21 GWh (UBA 2024 median and mean) = 61 to
  73 GWh/yr; electrified at JAZ 3.5 = 17 to 21 GWh_el/yr = 2.1 to 2.6% of 802 GWh on-land
  curtailment 2025. Storage-shift capacity at 750 kWh/K per facility, +2 K, 150 nights: about
  3.9 GWh_el/yr, 0.5% of curtailment.

## UNRESOLVED

One FAG row of 167 unparsed; the municipality ID 99xx row; the Freibad renovation-need and 2019
absolute counts in Anlage 1 tables 2.1 and 5.2; the indoor share of the 2019 water surface; the
questionnaire timeline of the end-2026 Statistikamt survey.

---

# Sixth pass: 2026-09-11, R2 locational value

**Prompted by:** working the locational-value question on the Q0.2 address list.

## VERIFIED by direct extraction or query

- **§13k target model from 1 October 2026.** ÜNB Umsetzungskonzept v2.0, Stand 01.04.2026: "Ab dem
  1. Oktober 2026 wechselt das Instrument in das sogenannte Zielmodell, in denen die
  Abregelungsstrommengen wettbewerblich ausgeschrieben und zugeteilt werden." Also: "Nach Ablauf
  der zweijährigen Erprobungsphase erfolgt gemäß Gesetzesvorgabe ab dem 1. Oktober 2026 die
  Ausschreibung der Abregelungsstrommengen nach einem wettbewerblichen Verfahren."
  **Closes B2** (open since the first pass, carried `[verify]` through five passes).
- **Relief regions by Landkreis, target phase.** Version 2.0 lists "Update der Entlastungsregionen";
  section 3.3.3: T5 = Dithmarschen, Nordfriesland; T6 = Neumünster, Lübeck, Pinneberg,
  Rendsburg-Eckernförde, Schleswig-Flensburg, Segeberg, Steinburg, Stormarn; T6 pooled with H1
  (Hamburg). Flensburg (Stadt), Kiel, Plön, Ostholstein and Herzogtum Lauenburg appear nowhere in
  the document. Amprion and TransnetBW designate no regions for 01.10.2026. Adjustments are
  announced with six months' notice.
- **Operators' rationale for exclusions, verbatim:** "Teilweise wurden im Norden der TenneT
  Regelzone Gebiete nicht mit in die Entlastungsregionen aufgenommen. Dies liegt darin begründet
  das dort angesiedelte Lasten einen engpassverstärkenden Effekt hätten oder dort durch TenneT in
  der Vergangenheit keine Abregelungen vorgenommen wurden." And for Hamburg: loads there reduce
  redispatch "aufgrund von Netzengpässen südlich von Hamburg."
- **Operators' caveat on their own basis:** distribution-level curtailment was derived "teilweise
  mit Faktoren"; the analyses "können in dieser Form nicht direkt auf die Zukunft angewendet
  werden."
- **OSM wind turbines in DE-SH, 11 Sep 2026:** 3,521 elements, 7 offshore; 2,131 with rated power
  summing to 6,571 MW.
- **Join results, 166 FAG units, all geocoded and plausibility-checked:** indoor units in a relief
  region 58 of 76 (76%). Proximity ("near wind" = ≥10 turbines within 5 km of the town centroid)
  against eligibility, indoor: near and eligible 11; near and ineligible 4; far and eligible 47;
  far and ineligible 14; agreement 25 of 76 (33%). Campusbad Flensburg and both Kiel units are
  outside any relief region; FehMare, Heiligenhafen and Grömitz have 18 to 27 turbines within 5 km
  and are outside.

## CORRECTED

**C9: the FAG CSV carried replacement characters in place of umlauts.** The raw pdftotext output
is Latin-1; it had been read as UTF-8 with replacement. *Consequence:* 28 town names failed to
geocode until the parser was made encoding-aware and the CSV regenerated. Counts, hours and euros
are unchanged (166 rows, 99.93% reconciliation); only text fields changed.

**C10: Lübeck rows had geocoded to Bordelum, Nordfriesland.** The free-text query "23552 Lübeck"
resolved to the wrong county, giving those units 105 turbines within 5 km. Caught by the
plausibility rule (geocode must name the facility town, office town or Kreis) and re-queried in
structured form; Lübeck now resolves to 53.866, 10.685 with 0 turbines within 5 km. *Consequence:*
the earlier provisional T6 "near wind" count of 7 is now 4. Every result in the R2 document is from
the corrected run.

**C11: the concept's figure caption reads "für die Erprobungsphase".** Section 3.3 text and the
version history state the regions were reviewed and updated for the Zielphase, and the web page
describes the map as the 1 October 2026 state. Carried as a caption inconsistency in the source;
the district list is taken as the target-phase designation. `[verify]` against the map image.

## Stated limits (not findings)

Centroid-level geocoding (facility addresses are not printed in the FAG list); OSM turbine
coverage about 70% by capacity; the "near wind" threshold is a choice; relief regions are a
regulatory eligibility criterion at county level and not a physical map of distribution
constraints.

---

# Seventh pass: 2026-09-11, R5 dispatch authority

**Prompted by:** working the institutional question. Statute and determination fetched from
gesetze-im-internet.de and bundesnetzagentur.de; concept already on disk.

## VERIFIED by direct extraction

- **§13k EnWG:** eligible participants are operators of registered additional switchable loads in
  relief regions, or their aggregators (Abs. 3 S. 1); exclusion applies to installations under a
  §13 Abs. 6a TSO-CHP contract (Abs. 3 S. 2); high additionality requirements for loads existing
  on 29 Dec 2023 that regularly buy on markets (Abs. 3 S. 5); dedicated metering point,
  quarter-hourly measurement, TSO minimum size up to 500 kW, monthly registration (Abs. 6 Nr. 3);
  penalty for unconsumed allocations (Abs. 5); daily competitive tenders in the target model,
  flat allocation in the two-year trial (Abs. 2).
- **BNetzA Festlegung 28.06.2024, Tenor:** general conditions (technical control by operator, or
  technical and legal control by supplier or aggregator; no §13(6a) contract); Segment 1 fossil
  heat substitution with the 2% full-load-hour rule in the prior month (worked example: 10 MW,
  October, 14.88 h, 148.8 MWh) and mandatory participation of all qualifying installations on the
  same heat system; Segment 2 storage; Segment 3 electrolysers and heat pumps ≥100 kW first
  commissioned after 29.12.2023, no 2% rule. Standard-load-profile operation is incompatible with
  the flexibility requirement.
- **ÜNB concept 5.1 to 6.3:** installation requirements a to f (own grid connection, flexible and
  not profile-bound, ≥100 kW, in a relief region, no 6a contract); participant as
  Einsatzverantwortlicher regardless of ownership, Rahmenvertrag with the TSO, tested
  communication channel; monthly bid ≥ Mindestpreis (2027 example 21.68 EUR/MWh = 43.37 × 0.5);
  daily availability before 10:00; self-procurement of energy; refund = max(reference − bid, 0)
  with reference = min(day-ahead, cap ≈ 400 EUR/MWh); variable levies compensated; fixed grid
  charges compensated only if the TSO-set annual minimum availability is met (example 3,000 h);
  penalty = max(day-ahead − bid, 0) × unconsumed allocation per hour; aggregation of <100 kW loads
  into groups ≥100 kW within one region; DSO confirmation with veto right discussed.
- **§37 IfSG (2) and (3):** operator duty that pool water cause no harm to health, mandatory
  disinfection, supervision by the health authority.
- **KOK-Richtlinien 6th ed. 2022, Table 22, via Städtetag Hinweise 4.2 (2025):** Kleinkinderbecken
  28 to 32 °C water / 30 to 34 °C air; all other indoor basins 24 to 28 / 26 to 30; Freibad 24 to
  26; hall air 2 to 4 K above water, max 34 °C.
- **Ministry guidance on enterprise forms:** Eigenbetrieb §106 GO (Werkleitung, Werkausschuss,
  Sondervermögen §97), Kommunalunternehmen §106a GO and KUVO (Vorstand, Verwaltungsrat),
  gemeinsames Kommunalunternehmen §19b GkZ, GmbH under §§101 ff. Schrankentrias, Zweckverband
  §2 GkZ.

## CORRECTED

**C12: scope of the CHP exclusion.** The scan, and my summaries of it, said installations under
existing TSO contracts with CHP plants are excluded "and pools commonly run CHP", implying pools
with CHP were at risk. *What is true:* the exclusion (statute Abs. 3 S. 2, Tenor 1b) is confined to
CHP plants that hold a §13 Abs. 6a redispatch contract with a TSO. A municipal pool's own CHP unit
carries no such contract unless separately concluded. *Consequence:* pools with CHP are not
excluded by that clause; the CHP interacts with Segment 1 only through the "same heat system"
participation rule.

**C13: scope of the 2% rule.** The first gap map wrote that the 2% full-load-hour test "sits
awkwardly against a near-constant load" like a pool. *What is true:* the rule applies to the
*additional electric heater* in Segment 1 (and to storage in Segment 2), not to the facility's
total consumption, and does not apply at all to a Segment 3 heat pump ≥100 kW commissioned after
29.12.2023. *Consequence:* the additionality path for an electrified pool is straightforward; the
binding constraints are the 100 kW threshold, the dedicated metering point and the flexible
(non-profile) operation requirement.

**C14: R4's charge assumption against the design band.** R4 modelled a +2 K charge from a
28 °C sports pool. *What is true:* the KOK design range for sports and multipurpose basins is 24 to
28 °C; 28 °C is the top of the band, so upward headroom under guidance is zero there. Children's
and teaching basins (28 to 32 °C) carry two to four kelvin of headroom. *Consequence:* R4's numbers
stand as physics; their applicability is pool-type specific. Storage-shift capacity in Q0.2 §4
(fleet 45 MWh/K, +2 K) is an upper bound that assumes headroom everywhere; the realistic fleet
figure is lower and concentrated in teaching and children's pools. Not recomputed here; flagged.

**C15: the minimum availability.** Stated in passing as something "a pool cannot ignore."
*What is true:* the TSO-set annual minimum availability (example 3,000 h) is a precondition for
compensation of *fixed* grid charges only; participation and the per-MWh refund do not depend on
it. *Consequence:* a pool with limited availability can participate and forgo that component.

## Estimates (stated assumptions, not findings)

Single-site cost-benefit: saving ≈ 140 EUR/MWh (17.2 ct/kWh normal supply less 21.68 bid floor
and 10 EUR/MWh residual); 150 kW plant × 900 allocated hours × headroom 1.0 → 135 MWh, gross
18,900, net ≈ 9,600 EUR/yr after a 25% aggregator fee and 4,600 EUR fixed; one-off ≈ 18,000 EUR;
sports-pool headroom 0.35 → net ≈ 400 EUR/yr; 60 kW plants negative in every case and unable to
participate alone.

## [verify] and UNRESOLVED

§101a GO SH wording and conditions; EigVO §5 reserved decisions; BDEW 17.2 ct/kWh figure (summary
only); aggregator fee band; Legionella threshold at 23 °C; whether SH Netz adopted a §13k
connection confirmation; allocated hours in T5 and T6 specifically.

---

# Eighth pass: 2026-09-12, Q0.1 addressable curtailment

**Prompted by:** working the second Tier 0 question, previously recorded as blocked on non-public
data. All documents fetched and extracted locally.

## VERIFIED by direct extraction

- **MEKUN report, 15 Apr 2026, full text.** "Über 65% dieser Abregelungen werden von der SH Netz
  auf Anforderung des vorgelagerten Netzbetreibers Tennet durchgeführt und resultieren aus
  Engpässen im Übertragungsnetz (teilweise außerhalb Schleswig-Holsteins)." Also: "Der überwiegende
  Anteil der Abregelungen wird durch Engpässe im Übertragungsnetz ausgelöst"; on-land RE generation
  at an all-time high of 22.3 TWh in 2025 despite a poor wind year; 3.6% of on-land RE curtailed in
  2025 against over 17% in 2015; 825 GWh compensable on-land curtailment plus 1,605 GWh offshore
  with SH grid connection; Bavaria, Lower Saxony and Schleswig-Holstein all in the 2.0 to 2.4 TWh
  range in 2025; national measure volume 30.3 TWh in both 2024 and 2025 at EUR 3.0 and 3.1 bn
  against a 2022 peak of EUR 4.1 bn; state-level cost attribution impossible since Redispatch 2.0
  in 2021; relief from the large HVDC links expected only after 2028. The report also calls for
  "zuschaltbare Lasten" at lower network levels and for flexible connection agreements.
- **SH Netz, Netzsituation und Besonderheiten (2017):** "Die Verursachung für diese Abregelungen
  liegt in über 90 Prozent der Fälle nicht im 110-kV-Netz von SH Netz, sondern in der noch nicht
  ausreichend vorhandenen Verfügbarkeit des Höchstspannungsnetzes." Also: over 90% of the state's
  renewable capacity is connected to SH Netz networks, about 34,000 installations and over 8 GW as
  of May 2017.
- **SH Netz Netzausbauplan 2022 and 2024:** the same causal statement without the percentage, so
  current in direction. NAP 2024 adds that curtailment is expected to rise again given accelerated
  renewable targets.
- **SH Netz Netzausbauplan 2024, Tabelle 6:** twelve medium-voltage congestion regions for the 2045
  scenario with shares of overloaded line elements: 1 Dithmarschen (NC Meldorf) 48%, 2 Herzogtum
  Lauenburg (Schwarzenbek) 55%, 3 Nordfriesland (Friedrichstadt and Niebüll) 29%, 4 Ostholstein
  (Pönitz) 72%, 5 Pinneberg (Uetersen) 63%, 6 Plön (Plön) 29%, 7 Rendsburg-Eckernförde (Fockbek)
  38%, 8 Schleswig-Flensburg (Schuby and Süderbrarup) 35%, 9 Segeberg (Segeberg and Kaltenkirchen)
  67%, 10 Steinburg (Dägeling) 26%, 11 Stormarn (Ahrensburg) 52%, 12 Neumünster 34%. High-voltage
  measures 2024 to 2028: 282 km of lines at EUR 552 m plus 61 installation sites at EUR 379 m.
- **§13k Abs. 8 EnWG:** distribution operators with 110 kV networks and more than 100,000 customers
  may run their own instrument from 1 April 2025, conditional on curtailment caused in their own
  network over the previous two calendar years.
- **ÜNB concept on the distribution route:** "Die Abstimmung der ÜNB mit den VNB Ende 2025 ... hat
  ergeben, dass die VNB absehbar keinen eigenständigen Anwendungsfall für 'Nutzen statt Abregeln'
  und Ausweisung von VNB-Entlastungsregionen gem. §13k Abs. 8 EnWG sehen."
- **Bundesnetzagentur Tabellen Q4 2023, Tabelle 4:** redispatch with renewables, measures 1,657 GWh
  at transmission level against 1,154.8 GWh at distribution level; causation 2,193.1 GWh in the
  transmission network against 618.7 GWh in the distribution network. Tabelle 9: Schleswig-Holstein
  950.1 GWh of instructed reductions in Q4 2023, second only to Lower Saxony.
- **OSM substations in DE-SH:** 4,776 total, 222 at 110 kV and 41 at 220 kV or above; operator tags
  give SH Netz 106, TraveNetz 18, TenneT 12, confirming that Lübeck is a separate operator
  territory.

## CORRECTED

**C16: "Q0.1 is blocked on non-public SH Netz data".** Recorded in R2, in the sequencing document
and repeated in conversation. *What is true:* the causation question is answered in public
documents by the network operator itself, by the state ministry and, independently, by the
distribution operators' declared position on §13k Abs. 8. Only the feeder-level assignment of
individual facilities remains operator-held. *Consequence:* the question was workable from the desk
and has now been worked; the residual request to SH Netz is much narrower than previously stated.

**C17: the framing of the 65% finding as a threat to the project premise.** The first gap map
treated transmission causation as evidence that a distribution-connected pool "may have no claim
whatever" on curtailed energy. *What is true:* where a constraint is caused and where a load must
sit to relieve it are different questions. §13k exists to let additional switchable loads, mostly
distribution-connected, absorb transmission-caused curtailment; the federal data show
distribution-connected assets already carry 41% of renewable redispatch measures against 22%
distribution-caused congestion. *Consequence:* transmission causation is the project's addressable
market, not an obstacle. The finding that survives is R2's: eligibility is regulatory, not
geographic. Restate accordingly wherever the earlier framing appears.

**C18: the first Q0.1 join used distance to a Netzcenter town.** The twelve congestion regions are
county-shaped, so distance to the centre town adds nothing beyond county membership and implies a
spatial precision the source does not carry. *Consequence:* the script was rewritten to join by
county and to report the projected overload share per county. The distance figures (22 of 76 indoor
units within 10 km, 40 within 15 km) are discarded.

## Estimates (stated assumptions, not findings)

Composite causation: 802 GWh, at least 65% TenneT-ordered (521 GWh), remainder 281 GWh of which
over 90% of cases are EHV-caused, leaving on the order of 28 GWh or about 3% genuinely
distribution-caused. Indicative: combines a 2026 volume share with a 2017 case share; both are
lower bounds on transmission causation, so the residual is an upper bound.

## [verify] and UNRESOLVED

The 2017 over-90% figure as a current value; the load-versus-generation trigger split for the
twelve congestion regions (garbled in extraction); the distribution operator for Kiel; whether the
§13k Abs. 8 threshold was formally tested for SH Netz; feeder-level assignment for any individual
pool.

---

# Ninth pass: 2026-09-12, R3 premise check

**Prompted by:** before scoping R3, the claim that winter 2022/23 was an involuntary, mandated
fleet-wide temperature reduction was tested against the regulation itself.

## CORRECTED

**C19: public swimming pools were EXEMPT from the EnSikuMaV pool provision.** The independent
scan described winter 2022/23 as "a near-universal, involuntary, dated, roughly 2 K step change" in
public pool water temperature, and the sequencing document and conversation repeated it as a
natural experiment with the regulation as the instrument.

*What is true*, from § 4 EnSikuMaV verbatim (**VERIFIED**, regulation downloaded and extracted):
"In Gebäuden oder zugehörigen privaten Gärten ist die Beheizung von **privaten, nichtgewerblichen**,
innen- oder außenliegenden Schwimm- und Badebecken einschließlich Aufstellbecken mit Gas oder mit
Strom aus dem Stromnetz untersagt." The explanatory note is explicit about who is outside it: "Von
der Regelung nicht betroffen sind Schwimmbecken in Nichtwohngebäuden, die Nutzern kommerziell zur
Verfügung gestellt werden, insbesondere in Rehazentren, Hotels und Freizeiteinrichtungen. Dies
folgt der Überlegung, dass alle Schwimm- und Badebecken, die kommerziell genutzt und der
Öffentlichkeit entgeltlich zur Verfügung gestellt werden, nicht mit einem Verbot belegt werden
sollen." The ban also exempts therapeutic heating, and covers only gas and grid electricity, not
district heat, heat pumps, solar or wood. § 6 caps air temperature in *Arbeitsräume* of public
non-residential buildings, which is a workroom provision and not a bathing-hall provision.

*Consequence:* the federal regulation did not mandate anything for public pools. Whatever
temperature reductions municipal pools made in winter 2022/23 were decisions taken under cost
pressure, not compliance with EnSikuMaV. R3 is therefore **not** a clean exogenous natural
experiment and must not be presented as one. What it can be is a revealed-preference study of
municipal decisions under a common cost shock, which aligns it with R5 rather than with a
difference-in-differences design, and which needs an identification strategy built on variation
that municipalities did not choose (energy carrier, supply-contract renewal timing, ownership
form) rather than on a mandate.

*Status of the earlier claim:* the regulation's dates (in force 26 Aug 2022, last amended
13 Feb 2023) stand. The "roughly 2 K" reduction and the visitor and staff reactions were always
`[verify]` from regional press and remain so, now without any regulatory basis for assuming they
were universal.

---

# Tenth pass: 2026-09-12, R3 desk checks

**Prompted by:** the three desk checks named at the end of the ninth pass, run before scoping R3.

## Check 1: did Schleswig-Holstein or its associations mandate anything?

No binding state rule was found. Two coordinating signals were. The Minister-President publicly
proposed that saunas and wellness areas across the state could close for the winter, and the
Deutsche Gesellschaft für das Badewesen issued temperature-reduction recommendations that the
sector followed. **[verify]** on the status and reach of both; search-level sources only.

*Consequence for identification:* the cuts were **coordinated but not compelled**. Pools were
responding to a common public signal rather than deciding independently, which is a third case
between the mandate that was assumed and the free choice that C19 established. It weakens any
assumption that decisions are independent across pools, and it gives a common date.

## Check 2: what actually happened in Schleswig-Holstein

Substantial and, importantly, **heterogeneous**. All **[verify]**, regional press and trade press:
Bäder Pinneberg closed entirely from 5 December 2022 to 31 March 2023; the Dünen-Therme in
St. Peter-Ording closed, with January gas costs alone reported at EUR 330,000; saunas were closed
in Schleswig, Rendsburg and Eckernförde until March; Arriba Norderstedt lowered both water and air
temperature. The commonly reported pattern is a 2 K cut, typically 28 °C to 26 °C, following the
bathing association's recommendation.

*Consequence:* the response varied across three levels (full closure, temperature reduction, sauna
only). That variation is what makes the episode analysable at all, now that a uniform mandate has
been ruled out.

## Check 3: VERIFIED: a public two-year panel of per-pool activity exists

**Drucksache 20/2279 of 8 July 2024** (Kleine Anfrage, Annabell Krämer FDP; answer by MIKWS)
carries the identical per-facility annex for calendar year 2023: Laufende Nr., Amt/Gemeinde, Name
der Schwimmstätte, Art, Schwimmunterrichtsstunden 2023, Förderbetrag. Parsed: **169 facilities,
127,791.0 hours, EUR 7,500,000.00**, both reconciling exactly to the printed totals. Types:
84 Freibad, 75 Hallenbad, 10 Naturbad.

Set against the 2025 annex already parsed from Drs. 20/4417, this gives **a public panel of
per-pool teaching hours for 2023 and 2025 that needs nobody's permission to use**. 131 facilities
match by name across both years; the matched subset falls 1.3% overall (103,008 to 101,692 hours),
with individual movements from -2,173 hours (Schaulandhalle Jarplund) to +1,965 (Lehrschwimmbecken
Klausdorf).

Drs. 20/2038 of 17 April 2024 asks the same question but predates the data, so it carries no list.

*What is still missing:* a 2021 or 2022 observation, which is what a clean pre-period requires.
The 2023 figures sit during and after the episode, not before it. Note also that teaching hours are
an **activity** measure, a proxy for whether the pool was open and usable, not a measure of visits,
revenue or energy.

*Files:* `research/r3_fag2023_sh_pools.csv`;
`research/.drafts/evidence/ltsh_drucksache_20-2279_fag2023_2024-07-08.pdf` and its raw extraction.

---

# Eleventh pass: 2026-09-12, R3 panel, closer look

**Prompted by:** hunting a pre-episode baseline year for the teaching-hours panel, and testing the
panel on the named crisis cases rather than on aggregates.

## What was established

- **No pre-2023 list was found.** Drs. 20/2038 (17 Apr 2024) asks about 2023 hours as a new
  question and records that the Statistikamt evaluation was still running, which is why Drs.
  20/2279 (8 Jul 2024) followed with the data. No earlier parliamentary answer carrying an
  hours-and-funding list was located. The FAG of 12 Nov 2020 (in force 1 Jan 2021) created the
  EUR 7.5 m pre-deduction, but whether the Zeitstunden criterion applied from the start could not
  be confirmed: both statute portals defeated retrieval (redirect loop; timeout). **[verify]**
- **Drs. 20/2905 (14 Feb 2025) is a different annex.** It lists facilities with place, type and
  whether guided instruction is offered, and carries no hours and no funding. Useful as a facility
  roster, not as a panel year. No 2024 hours list was found.
- **Panel as it stands: 2023 and 2025 only**, both parsed and reconciling to their printed totals.

## CORRECTED

**C20: the two-year panel was described more confidently than it deserves.** Earlier today it was
recorded, and stated to Nikhil, as "a public panel of teaching hours per pool for 2023 and 2025,
requiring nobody's permission to use", with only two caveats (no pre-period; an activity rather
than a visits measure). Testing it against the named crisis cases shows a third problem that is
more serious than either.

*What is true:* **the unit of observation is not stable between years.** Bäder Pinneberg is one row
in 2023 (2,837 hours) and three in 2025 (Schwimmhalle 2,437, Sprunghalle/Lehrschwimmbecken 689,
Außenbecken 41). That is why 38 of 169 facilities failed to match by name, and it means some of the
131 matches are also partial. Two further problems surfaced in the same check: some entries look
nominal rather than measured (Arriba Norderstedt shows exactly 30 and 150 hours in both years), and
the direction of change does not track the crisis narrative (the Dünen-Therme, which closed in the
crisis, rises from 219 to 340; Grömitz falls from 1,588 to 459).

*Consequence:* the panel is a usable activity series **only after facility-level unit
reconciliation**, which is real work. It is not a ready-made outcome measure for the 2022/23
episode. The earlier statement that the matched subset "falls 1.3%" should not be quoted: that
figure is computed across an unstable unit definition.

## Status of R3 after this pass

Public data exist and are worth having, but they answer a different question than the one R3 was
posed to answer. With no pre-2023 observation, the episode cannot be measured before and after from
this source. What the series can support is **recovery dynamics from 2023 to 2025**, once units are
reconciled. A genuine pre-period would have to come from operator records, Bäderleben visitor data
or municipal annual accounts, none of which is in hand.

---

# Twelfth pass: 2026-11-15, review of the whole folder before publication

**Prompted by:** a full re-read of every result document and a re-run of all seven scripts, before
the material is shown outside. All seven scripts reproduce their published figures from the saved
evidence files.

## CORRECTED

**C21: one indoor unit was counted as outside any relief region because its county was never
resolved.** Row 168 of the FAG 2025 list, the Steinburgschule teaching pool in Itzehoe, carries
the placeholder municipality ID 9999. The parser derives the county from the first two digits of
the ID, found no county for "99", and wrote "?99". The R2 and Q0.1 joins then treated "?99" as
"not in a relief region". The fifth pass had recorded the row as UNRESOLVED; the sixth and eighth
passes used it anyway.

*What is true:* the printed row reads "Kreis Steinburg, Viktoriastraße 16-18, 25524 Itzehoe". The
owner is the county itself, which is why no municipality ID applies. Itzehoe is the county town of
Kreis Steinburg, and Steinburg is in relief region T6. **VERIFIED** from the row as printed in
Drs. 20/4417, Anlage 2.

*Consequence:* every R2 count that includes this unit moves by one.

| Quantity | First run | Corrected |
|---|---|---|
| Indoor units in T6 | 43 | 44 |
| Indoor units outside any relief region | 18 | 17 |
| Indoor units inside a relief region | 58 of 76 (76%) | 59 of 76 (78%) |
| Far from wind and eligible | 47 | 48 |
| Far from wind and ineligible | 14 | 13 |
| Proximity agrees with eligibility | 25 of 76 (33%) | 24 of 76 (32%) |
| Indoor units in Steinburg (Q0.1 table, Q0.2 table) | 4 | 5 |

The conclusion of R2 is unchanged and slightly stronger. `q02_fag_pools.py` now takes the county
from the owner name when the ID is 9999, and the three CSV files were regenerated. The R2, Q0.1 and
Q0.2 result documents carry the corrected figures. The figures in the sixth pass above are left as
first recorded.

**C22: R2 attributed all 47 far-and-eligible units to T6.** The sentence read "the 47 units in T6
that are eligible and nowhere near a turbine". *What is true:* T6 held 43 indoor units in that
run, of which 39 were far from wind; the other 8 were in T5. Corrected figures: 48 far-and-eligible
units, 40 in T6 and 8 in T5. *Consequence:* the sentence in the R2 result was reworded.

## Stale statements brought up to date

- `research/process/README.md` said seven records, 41 evidence files, eight verification passes and
  eighteen corrections, and listed R3 as not worked. There are eight records (R3 has one), 44
  evidence files, twelve passes and twenty-two corrections.
- The Q0.1 source list named a local PDF of the SH Netz 2017 paper. Only the text extraction is on
  disk. The source list now says so.
- R2 section 5 said "Q0.1 stands" as an open question. It was worked in the eighth pass; the
  sentence now points there.
- `q02_osm_pools.py` queried Overpass live when run without an argument, so a re-run returned
  today's OpenStreetMap (1,183 elements on 15 November 2026 against 1,180 on 11 September) and
  overwrote the CSV. It now reads the saved evidence copy unless `--live` is passed.

## Still open, not changed by this pass

`research/splash-what-how-when.md` and `research/splash-pool-flexibility.md` are the first-week
planning documents. They still carry the framings that C12, C13, C16, C17 and C19 later corrected
(the CHP exclusion, the 2% rule, Q0.1 as blocked, transmission causation as a threat, and winter
2022/23 as a mandated experiment). They are kept as the record of what was believed at the time.
Each now opens with a notice that names the corrections. Do not quote from them without reading
the notice.
