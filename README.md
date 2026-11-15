# Swimming pools as flexible loads in Schleswig-Holstein: desk findings

Six questions about public swimming pools as power-to-heat flexibility in Schleswig-Holstein,
worked from public documents and open data in September 2026 and reviewed in November 2026.

This is preparatory work by an applicant, Nikhil Sehgal. It is not an output of project SPLASH or
of Europa-Universität Flensburg, and it uses no project data. All results are desk results:
first-order calculations and joins on public sources, with no measurement and no operator data.

## Results

| | Question | Answer in one line | Result | Script |
|---|---|---|---|---|
| Q0.1 | What share of the curtailment can a distribution-connected pool reach? | About 97% is transmission-caused, and that is the part §13k EnWG makes reachable in a relief region. The distribution-caused part is about 3% and has no instrument. | [q01](research/q01-addressable-curtailment.md) | [py](research/q01_dso_congestion_join.py) |
| Q0.2 | Does a usable pool inventory exist? | Yes for counts, locations and owners (166 funded units, 76 indoor, 2025). No for technical attributes. | [q02](research/q02-sh-pool-inventory.md) | [py](research/q02_fag_pools.py), [py](research/q02_osm_pools.py) |
| R1 | Is the zero flexibility score for baths a property of the asset or of the method? | Of the method. With the heat electrified, the same method gives 0.30 to 0.97 TWh/a. | [r1](research/r1-electrification-conditional-flexibility.md) | [py](research/r1_flexibility_calc.py) |
| R2 | Does proximity to wind predict where curtailed energy can be claimed? | No. Proximity agrees with §13k eligibility for 24 of 76 indoor units. 59 of 76 are eligible. | [r2](research/r2-locational-value.md) | [py](research/r2_locational_value.py) |
| R4 | What does the evaporation loop cost when heat is stored in pool water? | 2 to 3% on an overnight charge. About 35% of the shifted electricity on a charge held through summer bathing hours. | [r4](research/r4-evaporation-loop.md) | [py](research/r4_evaporation_loop.py) |
| R5 | Who can commit a municipal pool to a grid signal, and does it pay? | Nobody alone: council, operator and network operator each hold a veto. A single site clears its cost only in the best case. | [r5](research/r5-dispatch-authority.md) | [py](research/r5_participation_cost.py) |

R3, the winter 2022/23 temperature episode as a natural experiment, was not answered. Its premise
was checked and corrected: see [process record R3](research/process/P-R3-premise-and-panel.md).

## Layout

```
verification_log.md          twelve verification passes, 22 numbered corrections
research/
  <id>-<name>.md             result document, with sources
  <id>-<name>.provenance.md  sources consulted against sources accepted, and open checks
  <id>_<name>.py             script that reproduces the figures
  *.csv                      output tables (pool lists, joins)
  process/                   step-by-step record of how each question was worked
  .drafts/evidence/          the open input files the scripts read
  .drafts/geocode_cache.json cached Nominatim results, so the R2 join runs offline
site/                        the two web pages (findings, process record)
```

## Run

Python 3.10 or later. No packages outside the standard library. Each script runs from any
directory and reads the saved input files:

```
python research/q02_fag_pools.py
python research/r2_locational_value.py
python research/q01_dso_congestion_join.py
python research/r1_flexibility_calc.py
python research/r4_evaporation_loop.py
python research/r5_participation_cost.py
python research/q02_osm_pools.py          # add --live to query OpenStreetMap again
```

Run `q02_fag_pools.py` first: the R2 and Q0.1 joins read its output.

## Status labels

Each statement in the result documents carries one of these labels.

| Label | Meaning |
|---|---|
| **VERIFIED** | Read in the primary document or computed from it in this study. |
| **[verify]** | Plausible, from a secondary source or a summary. Not checked against the primary document. |
| **UNRESOLVED** | Could not be checked. This includes each statement that something does not exist in the literature: the searches were not systematic. |

## What is not in this repository

- Third-party reports, articles and datasheets. Each result document cites them with a URL. The
  documents name local copies under `.drafts/evidence/`; only the open inputs listed below are
  included here.
- The two early gap maps and the planning notes that the process records and the verification log
  refer to (`splash-pool-flexibility.md`, `perspectives_splash.md`, `splash-what-how-when.md`,
  `splash-gaps.md`). Several of their statements were corrected later; the corrections are in
  `verification_log.md`.

## Data sources and licences

- Pool lists: Landtag Schleswig-Holstein, Drucksache 20/4417 (29 April 2026), Anlage 2, and
  Drucksache 20/2279 (8 July 2024). Text extractions of the official documents.
- Wind turbines, pools and substations: © OpenStreetMap contributors, Open Database License
  (ODbL), queried through the Overpass API on 11 September 2026. Geocoding: Nominatim.
- §13k relief regions: transmission system operators, Umsetzungskonzept § 13k EnWG, version 2.0,
  1 April 2026, section 3.3.3.
