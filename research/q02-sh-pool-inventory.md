# Q0.2: Does a usable Schleswig-Holstein pool inventory exist?

**Answer: for counts, locations and ownership, yes, and it is four months old. For technical
attributes, no, and the state itself says so.** Desk result, reproducible from `q02_fag_pools.py`
and `q02_osm_pools.py`; evidence in `.drafts/evidence/`. Status labels per
`README.md`.

---

## 1. The question

The SPLASH "Data Acquisition & Profiling" package assumes the project must build the pool inventory
from scratch. The first gap map treated that as a work task and the scan asked whether the fleet is
even known as a population. This pass establishes what exists, how good it is, and what remains.

## 2. Sources found

Three, of very different quality.

### 2.1 Landtag Drucksache 20/4417 (29 April 2026): the state's own answer

The state government's reply to the SPD's Große Anfrage "Schwimmstätten in Schleswig-Holstein",
covering stock as of 1 January 2026. **VERIFIED**, full text extracted locally. Three things in it
matter, and the first is the most important finding of this pass.

**The state does not hold a current inventory, and says so in writing.** From the Vorbemerkung:
the data lie exclusively with the municipalities; the state's own figures rest on the **2016**
survey (Drs. 18/5297) and the **2019** Sportstättenstatistik; and "die vorliegende Datenlage nicht
auskömmlich ist bzw. aktualisiert werden muss." The government therefore announces that the
**next FAG data request at the end of 2026 will be run and expanded by the Statistikamt** to
collect, per facility: counts per Kreis by type, basin counts and teaching basins, **basin and water
depths**, locations, **build year and last general renovation**, current renovation measures with
costs, decided future renovations, closures since 2006, and accessibility.

That is a large part of the SPLASH inventory package, run by the state statistical office, starting
in the project's first quarter. A project that builds its own inventory in parallel would duplicate
it; a project that feeds its parameter needs into that survey's design would get state-wide
coverage it could never achieve alone. This is the single most actionable finding for the post.

**The 2026 request itself got 34 replies.** Municipal participation was voluntary; 34 administrative
units answered, and the summary tallies 32 of them: **82 facilities, 25 Hallenbäder, 26 Freibäder,
12 Naturbäder, 19 Lehrschwimmbecken**, 66 of them publicly accessible. **VERIFIED.** This is a
partial, self-selected sample, not an inventory, and it must not be scaled.

**It carries the only technical information found anywhere.** In the free-text answers, nine
municipalities describe their heat supply or energetic renovation. **VERIFIED**, all from prose:
Wesselburen installed a heat pump for pool-water heating in 2023/24; Büdelsdorf runs an air-source
heat pump with PV; Süderbrarup plans a heat pump at EUR 930,957; Plön renewed its CHP-based heat
supply in 2021-22; Bargteheide's external supplier plans to decarbonise the CHP; Heide is looking
for industrial waste heat; Wyk auf Föhr plans to move to "PV, Wärmepumpe, BHKW und Strom"; Kiel and
Quarnstedt report PV. Nine of 82 responding facilities. That is the whole technical inventory of
the state, as far as public documents go.

### 2.2 Anlage 2 of the same Drucksache: the 2025 FAG funding list

The state distributes about EUR 7.5 m per year to pool operators under § 24 FAG, on the basis of
annually reported water surface and supervised swimming-lesson hours. Anlage 2 prints the 2025
distribution: **every funded facility with municipality, address, name, type, lesson hours and
funding amount.** This is an administrative record, not a survey, so within its scope it is
complete. **VERIFIED**, parsed from the reading-order extraction and reconciled against the printed
totals to 99.9% (126,251 of 126,342 hours; EUR 7,494,598 of 7,499,999.94; one row unmatched).

| | Rows | Notes |
|---|---|---|
| Funded units, total | **166** | some facilities appear per basin (Campusbad Flensburg, Plönbad, Badebucht Wedel) |
| Distinct facilities after basin de-duplication | **~153** | municipality plus name stem |
| Administrative units | **107** | of the state's roughly 1,100 municipalities, via Ämter |
| Typed Hallenbad | 76 | includes teaching basins, which the list types as Hallenbad |
| Typed Freibad | 77 | |
| Typed Naturbad | 13 | |
| Offering supervised lessons | 166 of 166 | it is the funding criterion, so the list excludes pools without lessons |

By Kreis (rows, indoor / outdoor, 2025 lesson hours, 2025 funding):

| Kreis | Indoor | Outdoor | Rows | Lesson h | FAG EUR |
|---|---|---|---|---|---|
| Nordfriesland | 11 | 13 | 24 | 10,661 | 632,866 |
| Rendsburg-Eckernförde | 4 | 14 | 18 | 7,735 | 459,170 |
| Dithmarschen | 4 | 13 | 17 | 6,587 | 391,022 |
| Segeberg | 6 | 11 | 17 | 12,182 | 723,156 |
| Pinneberg | 11 | 4 | 15 | 19,527 | 1,159,175 |
| Schleswig-Flensburg | 7 | 8 | 15 | 11,858 | 703,923 |
| Steinburg | 5 | 8 | 13 | 6,157 | 365,496 |
| Herzogtum Lauenburg | 3 | 8 | 11 | 6,555 | 389,122 |
| Ostholstein | 7 | 3 | 10 | 5,715 | 339,258 |
| Stormarn | 7 | 2 | 9 | 14,005 | 831,374 |
| Plön | 3 | 2 | 5 | 4,398 | 261,077 |
| Kiel | 2 | 2 | 4 | 5,200 | 308,686 |
| Lübeck | 3 | 1 | 4 | 6,005 | 356,473 |
| Flensburg | 2 | 0 | 2 | 5,390 | 319,965 |
| Neumünster | 1 | 1 | 2 | 4,276 | 253,835 |
| **Total** | **76** | **90** | **166** | **126,251** | **7,494,598** |

Steinburg includes one unit with the placeholder municipality ID 9999 (Steinburgschule, Itzehoe,
546 hours, EUR 32,412), which is owned by Kreis Steinburg and not by a municipality. Resolved
15 November 2026, correction C21.

The geography is itself a finding for the geospatial package: the indoor stock concentrates in the
Hamburg belt (Pinneberg, Stormarn, Segeberg) and Nordfriesland, while the west-coast wind counties
Dithmarschen and Nordfriesland carry mostly outdoor pools. Outdoor pools run May to September, when
wind curtailment is lowest. The heated year-round stock near the wind is small.

**What the FAG list lacks.** Water surface per facility, although it is reported to the state every
year and is the basis of the Maßzahl; it is simply not printed. Coordinates (addresses are given;
geocoding is mechanical). Anything technical: volume, temperature, plant, carrier, age.

### 2.3 Anlage 1: the 2019 Sportstättenerhebung (Statistikamt Nord)

The last full survey, December 2019, **71.3% response rate** (down from 87.6% in 2014).
**VERIFIED.** Pool-relevant rows:

| Quantity, 2019 | Value |
|---|---|
| Hallenbäder (Typ 11) by owner | 32 municipal, 11 other public, 5 club = **48** |
| Freibäder (Typ 12) by owner | 53 municipal, 5 other public, 8 club = **66** |
| Swimming basins, Typ 11 + 12 | 257 |
| Teaching basins, Typ 11 + 12 | 100 |
| **Water surface, Typ 11 + 12** | **76,488 m²** |
| Hallenbäder with renovation or modernisation need | 43.4% |
| Hallenbad users | 41.2% schools, 57.1% clubs |
| Change in recorded facilities 2014 to 2019 | Hallenbad −22.6%, Freibad −19.5% (confounded by the response-rate fall) |

The Freibad renovation-need figure and the 2019 absolute counts in table 5.2 are **[verify]**: the
extraction garbles those cells.

### 2.4 OpenStreetMap

Overpass query on the DE-SH boundary, 11 September 2026: 1,180 elements; after removing private
pools and natural bathing waters and clustering basins into facilities, **239 named facilities**
(60 tagged indoor, 69 outdoor, 110 unknown) plus 258 unnamed orphans. **VERIFIED** as a query
result. Attribute coverage among the 239: opening hours 73, website 77, operator 42, building 50,
length 2, **depth 0, heating 0, heated 0, water temperature 0**. OSM gives coordinates and names
and nothing SPLASH needs technically. Its count is higher than the FAG list because it includes
hotel, campsite, club and leisure pools that receive no lesson funding.

### 2.5 Bäderleben

The national citizen-science database (Hochschule Koblenz, BISp, Bäderallianz), over 9,300 pools
with 140+ attributes, searchable by Bundesland with Excel export (sheets "Bäder" and "Becken").
**VERIFIED** that the interface exists; the form is JavaScript-driven and would not answer a scripted
request, so the SH extract was not obtained here. It is a two-minute browser task: Bundesland =
Schleswig-Holstein, alle Badtypen, Suchen, Daten exportieren. The UBA 2024 energy study used this
database as its population frame, so its basin-level fields (per-basin dimensions and type) are the
best available bridge from the FAG list to water volume.

## 3. Reconciling 2019 and 2025

The 2019 survey is the only source with water surface and basin counts, and it is six years old at
71% response. The 2025 FAG list is complete within scope but carries no such fields. The natural
question is whether the 2019 figures can be carried forward.

The check: correct the 2019 facility counts for non-response and compare with 2025.

| | 2019 recorded | ÷ 0.713 | 2025 FAG rows | 2025 after basin de-dup |
|---|---|---|---|---|
| Indoor | 48 | 67 | 76 | roughly 60-65 |
| Outdoor | 66 | 93 | 90 | roughly 88-90 |

Both types land within a few units of the 2025 record once non-response is corrected, under the
assumption that non-responding municipalities resemble responding ones. That assumption is stated,
not proven, but the agreement on two independent types is reassuring. On that basis:

- **Water surface, 2025 estimate: about 107,000 m²** (76,488 ÷ 0.713), or 112,000 m² by the
  per-facility route (671 m² per facility × 167). **Estimate**, labelled as such. The indoor share is
  **UNRESOLVED**; the 2019 table does not split it and the extraction of the basin rows is unclear.
- **Heated indoor facilities, 2025: about 60**, from either route. Cross-check: the UBA 2024 frame of
  1,390 municipal indoor and combination pools nationally, scaled by Schleswig-Holstein's 3.5% of
  population, gives 49, close to the 2019 count of 48 before correction.

**None of this survives the end-2026 Statistikamt survey, and none of it should.** The
reconciliation is what to use between now and then, and it is what a candidate can say in the room.

## 4. What the fleet is worth, to first order

With about 60 heated indoor facilities, the UBA 2024 per-pool mean heat of 1.21 GWh/yr (median
1.01) gives **61 to 73 GWh of heat per year** for the Schleswig-Holstein municipal indoor stock.
Electrified through heat pumps at seasonal performance 3.5, that is **17 to 21 GWh of electricity
per year**, essentially all of it the process-heat load that R1 showed the reference method cannot
see.

Against 802 GWh of on-land curtailment in 2025 (**VERIFIED**, MEKUN), the entire electrified indoor
fleet's annual heat-pump consumption is **2.1 to 2.6% of curtailed energy**. That is the ceiling if
every kilowatt-hour of pool heat were timed into a curtailment window.

The portion that can actively be *shifted* into such windows by water-temperature storage is
smaller. At about 750 kWh per kelvin per facility (a 25 m pool plus a teaching pool), the fleet holds
about 45 MWh per kelvin; a fleet-wide +2 K overnight charge is about 90 MWh of heat, 26 MWh of
electricity; 150 such nights a year is about 3.9 GWh, or **0.5% of curtailment**. R4 established that
overnight is the regime in which this is cheap.

Two readings, both stated plainly. Schleswig-Holstein's pool fleet is not a volume solution to
curtailment; low single digits of percent is the bound, and the sharper of the two numbers is the
storage-shift one. What the fleet can be is an asset-class template: a publicly owned, uniformly
governed, heat-dominated building class on which electrification-conditional flexibility (R1) and
the storage regime (R4) can be demonstrated and then generalised to schools, sports halls and
hospitals, which are the same governance shape at ten times the heat.

## 5. What this means for the project

**The inventory package should not build an inventory.** It should (1) take the 2025 FAG list as
the population frame, which is what the state itself uses to distribute money; (2) obtain the
per-facility water surface that the FAG already collects but does not print, by request to MIKWS or
the Statistikamt; (3) pull the Bäderleben basin-level export for dimensions; (4) geocode the FAG
addresses; and (5) **negotiate the technical parameters SPLASH needs into the end-2026 Statistikamt
survey** before its questionnaire is fixed: heat carrier, plant type and age, presence of CHP,
water volume, set temperature, operating hours. Item 5 has a deadline measured in weeks from the
project start and is the difference between a 60-facility sample and state-wide coverage.

**The willingness package has its contact frame.** 107 administrative units, with the Amt named,
already reporting annually to the state on their pools. The 34 that answered the Landtag request
voluntarily are the warm start.

---

## Sources

1. Schleswig-Holsteinischer Landtag, Drucksache 20/4417, 29 April 2026, Antwort der Landesregierung
   (MIKWS) auf die Große Anfrage der SPD "Schwimmstätten in Schleswig-Holstein" (Drs. 20/4017),
   including Anlage 1 (Sportstättenerhebung 2019, Statistikamt Nord) and Anlage 2 (FAG 2025).
   https://www.landtag.ltsh.de/infothek/wahl20/drucks/04400/drucksache-20-04417.pdf
   Local: `.drafts/evidence/ltsh_drucksache_20-4417_schwimmstaetten_2026-04-29.pdf`, layout and
   raw text extractions, and `ltsh_20-4417_anlage2_fag2025_extract.txt`.
2. OpenStreetMap via Overpass API, query of 11 September 2026. Query and raw JSON in
   `.drafts/evidence/osm_overpass_sh_pools_query.ql` and `osm_overpass_sh_pools_2026-09-11.json`.
   © OpenStreetMap contributors, ODbL.
3. Bäderleben, Hochschule Koblenz / BISp / Bäderallianz Deutschland. https://baederleben.de/ and
   https://baederleben.de/abfragen/baeder-suche.php
4. Weinfurter, Thieme, Wallrodt (2024), UBA TEXTE 139/2024 (as in R1), for the per-pool heat mean
   and the national municipal indoor frame.
5. MEKUN Schleswig-Holstein, Stromnetz-Engpassmanagement, 15 April 2026 (as in the gap map), for
   the 802 GWh curtailment figure.

## Outputs

- `q02_fag2025_sh_pools.csv`: 166 funded units with municipality ID, Kreis, address, name, type,
  supervised-lesson flag, 2025 lesson hours, Maßzahl and funding amount.
- `q02_osm_sh_facilities.csv`: 239 OSM facilities with coordinates and class.
- `q02_fag_pools.py`, `q02_osm_pools.py`: reproduce both from the evidence files.
