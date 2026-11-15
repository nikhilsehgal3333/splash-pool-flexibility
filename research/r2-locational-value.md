# R2: Does proximity to wind predict where curtailed energy can be claimed?

**Desk test of the advertised geospatial method against the regulatory eligibility geography of
§13k EnWG, for every publicly funded pool in Schleswig-Holstein.** Reproducible from
`r2_locational_value.py`; evidence in `.drafts/evidence/`. Status labels per
`README.md`.

---

## 1. The question

The advertisement's geospatial package analyses "proximity of swimming pools to local wind/solar
farms and existing grid constraints." Both research passes flagged that distance to a generator is
not the variable that determines whether a load relieves a constraint. The desk version of that
claim: take the variable the ad proposes (distance to turbines), take the variable the regulator
actually uses to decide where curtailed energy may be absorbed (the §13k relief regions), and see
how often they agree.

## 2. The regulatory geography, and a closed verification item

**§13k EnWG moves to its target model on 1 October 2026.** From the transmission operators'
implementation concept, version 2.0 dated 1 April 2026: "Ab dem 1. Oktober 2026 wechselt das
Instrument in das sogenannte Zielmodell, in denen die Abregelungsstrommengen wettbewerblich
ausgeschrieben und zugeteilt werden." **VERIFIED**, primary document, local extraction. This closes
the item carried at `[verify]` since the first pass: the competitive tendering of curtailed energy
starts in the month SPLASH starts.

**Relief regions are designated by Landkreis.** "Zu diesem Zweck wurden geographische Gebiete auf
Ebene von Landkreisen bestimmt und zu Entlastungsregionen zusammengefasst." Version 2.0 records
"Update der Entlastungsregionen" for the target phase, and the regions "wurden für die Zielphase
entsprechend der Rahmenbedingungen überprüft und aktualisiert." **VERIFIED.** In Schleswig-Holstein:

| Region | Landkreise / kreisfreie Städte |
|---|---|
| **T5** | Dithmarschen, Nordfriesland |
| **T6** (pooled with Hamburg's H1 for forecasting and tendering) | Neumünster, Lübeck, Pinneberg, Rendsburg-Eckernförde, Schleswig-Flensburg, Segeberg, Steinburg, Stormarn |
| **not in any region** | Flensburg (Stadt), Kiel, Plön, Ostholstein, Herzogtum Lauenburg |

The concept explains the omissions in one sentence that is the whole of R2 in the operators' own
words: "Teilweise wurden im Norden der TenneT Regelzone Gebiete nicht mit in die
Entlastungsregionen aufgenommen. Dies liegt darin begründet das dort angesiedelte Lasten einen
engpassverstärkenden Effekt hätten oder dort durch TenneT in der Vergangenheit keine Abregelungen
vorgenommen wurden." **VERIFIED.** A load next to a wind farm can make congestion worse. And the
inclusion of the Hamburg belt is explained the same way: loads there "werden strombedingte
Redispatchbedarfe in anderen Regionen aufgrund von Netzengpässen südlich von Hamburg senken."
Eligibility follows the north-south bottleneck, not the turbines.

## 3. Method

- **Pools:** the 166 funded units of the 2025 FAG list (Q0.2), geocoded at postcode and town
  level because the list prints the municipal office address, not the facility. Every geocode was
  checked for plausibility against the facility town, the office town or the Kreis, and re-queried
  on failure; one systematic error (a postcode resolving to the wrong county) was caught this way.
  Distances are therefore accurate to a few kilometres, not metres.
- **Turbines:** 3,521 wind generators tagged in OpenStreetMap inside the DE-SH boundary on
  11 September 2026, 7 offshore removed; 2,131 carry a rated-power tag summing to 6.6 GW, against a
  state onshore fleet of roughly 9 GW, so coverage is high but not complete. **VERIFIED** as a query
  result.
- **Eligibility:** the pool's Kreis is in T5 or T6.
- **"Near wind":** at least 10 turbines within 5 km of the town centroid. The threshold is a
  choice; the result is not sensitive to it in direction.

## 4. Result

### 4.1 Where the indoor stock sits

| | Indoor units | Outdoor units |
|---|---|---|
| T5 (west coast) | 15 | 26 |
| T6 (Hamburg belt and centre) | 44 | 49 |
| Outside any relief region | 17 | 15 |
| **Indoor units able to claim §13k energy by location** | **59 of 76 (78%)** | |

### 4.2 Proximity against eligibility, indoor units

| Eligibility | n | Nearest turbine, median (IQR) | Turbines within 5 km, median | "Near wind" |
|---|---|---|---|---|
| T5 | 15 | 2.4 km (1.8 to 3.5) | 8 | 7 |
| T6 | 44 | 5.3 km (3.0 to 8.5) | 0 | 4 |
| none | 17 | 5.4 km (1.9 to 8.3) | 0 | 4 |

| | Eligible | Not eligible |
|---|---|---|
| Near wind | 11 | 4 |
| Far from wind | **48** | 13 |

**The proximity proxy agrees with eligibility for 24 of 76 indoor units, 32%.** It is wrong in
both directions and worse than a coin toss. The bulk of the disagreement is the 48 eligible units
that are nowhere near a turbine, 40 of them in T6: Pinneberg, Stormarn and Segeberg pools qualify
because they sit north of the bottleneck south of Hamburg, not because there is wind beside them.

*Corrected 15 November 2026 (C21 in `verification_log.md`).* One indoor unit, the Steinburgschule
teaching pool in Itzehoe, carries the placeholder municipality ID 9999 because its owner is Kreis
Steinburg. The first run left its county unresolved and counted it as outside any relief region.
Steinburg is in T6. The figures above are from the corrected run; the first run gave 58 of 76
(76%) and 25 of 76 (33%).

### 4.3 The pools nearest the wind are the ones excluded

Indoor units outside any relief region, with their turbine counts within 5 km:

| Kreis | Facility | Nearest turbine | Within 5 km |
|---|---|---|---|
| Ostholstein | FehMare (Fehmarn) | 1.2 km | 27 |
| Ostholstein | Aktiv-Hus Heiligenhafen | 1.1 km | 24 |
| Ostholstein | Grömitzer Welle | 1.3 km | 18 |
| Herzogtum Lauenburg | Möllner Welle | 3.8 km | 20 |
| Ostholstein | Meerwasserhallenbad Niendorf | 4.1 km | 5 |
| **Flensburg** | **Campusbad Flensburg** (two units) | 1.9 km | 2 |
| Kiel | Hörnbad, Max-Planck-Schule | 8.3 km | 0 |
| Plön | Plönbad (two units), Klausdorf | 5.4 to 9.6 km | 0 |
| Ostholstein | Bad Schwartau, Kirsten-Bruhn-Bad, StrandSpa Dahme | 6.2 km | 0 |
| Lauenburg | Aqua Siwa, Wentorf | 12 to 13 km | 0 |

The Baltic-coast leisure pools on Fehmarn, at Heiligenhafen and at Grömitz sit among the densest
turbine clusters of any indoor pool in the state, and they cannot claim a kilowatt-hour under
§13k. By the operators' own explanation, either loads there would aggravate the constraint or
TenneT has never curtailed there. Under the advertised method these would rank first.

**Campusbad Flensburg is outside any relief region.** The host university's own city cannot
participate in the instrument that would pay for the asset class the project studies. Kiel, the
state capital, likewise. That is worth knowing before anyone proposes either as the pilot site.

## 5. What this establishes, and what it does not

**Established, to first order.** In Schleswig-Holstein, the geography of where curtailed energy
may be absorbed is a transmission-relief geography drawn at Landkreis level, and the ad's
proximity variable predicts it at 32%. A geospatial package built on distance to generation would
rank the wrong pools. More than three quarters of the indoor stock is inside a relief region, which is good
news for the project's premise and bad news for the proposed method of finding it.

**Not established, and the actual research question underneath.**

1. **Eligibility is not topology.** The relief regions are a regulatory criterion for one
   instrument, drawn by county on historical transmission-level curtailment; the operators write
   that distribution-level curtailment was derived "teilweise mit Faktoren", and add a disclaimer
   that their analyses "können in dieser Form nicht direkt auf die Zukunft angewendet werden."
   **VERIFIED** as their statements. Whether a given pool physically relieves the feeder it hangs
   on is a distribution-network question that only SH Netz data can answer. (Q0.1 was worked
   afterwards from public sources, see `q01-addressable-curtailment.md`; only this feeder-level
   part remains operator-held.)
2. **Regions move.** Adjustments are announced with six months' notice. A one-year project would
   be wise to treat membership as a time series, not a constant.
3. **Centroid geocoding.** A facility on the edge of a town can be 3 to 5 km from the centroid.
   Enough to shift a few units across the 5 km threshold; not enough to change the 2 by 2.
4. **The proximity variable was the only one tested.** A better proxy, such as distance to the
   nearest 110 kV substation with a constrained feeder, could not be built here because the
   network data are not public. That is the version of R2 the project should actually run, with
   the grid-operator collaboration the post anticipates.

## 6. What this means for the project

The geospatial package should not start from turbine locations. It should start from the relief
regions, which are public and decisive for the funding channel, then add SH Netz constraint
locations under the collaboration the ad names, and only then ask what proximity adds. The
three-line version: 78% of the indoor stock is eligible by location; the eligible
pools are mostly far from the wind; the pools closest to the wind are excluded, and the operators
say why. That is a result, and it was reachable from public documents in an afternoon.

---

## Sources

1. Übertragungsnetzbetreiber, "§ 13k EnWG 'Nutzen statt Abregeln', Umsetzungskonzept gemäß § 13k
   Abs. 6 S. 2 EnWG", Stand 01.04.2026, version 2.0.
   https://www.netztransparenz.de/cdn/files/37bd9764-d02a-46de-fce9-08de8bf3161c/2026-04-01%20u%CC%88nb%20umsetzungskonzept%20%C2%A713k%20enwg.pdf
   Local: `.drafts/evidence/uenb_umsetzungskonzept_13k_2026-04-01.pdf` and text extraction.
2. netztransparenz.de, Entlastungsregionen (map as of 1 October 2026; the page text does not
   enumerate districts, the concept does).
   https://www.netztransparenz.de/de-de/Systemdienstleistungen/Betriebsfuehrung/Nutzen-statt-Abregeln/Entlastungsregionen
3. OpenStreetMap via Overpass API, wind generators in DE-SH, 11 September 2026. Query and JSON in
   `.drafts/evidence/osm_overpass_sh_wind_query.ql` and `osm_overpass_sh_wind_turbines_2026-09-11.json`.
   © OpenStreetMap contributors, ODbL.
4. Nominatim geocoding (OpenStreetMap), cached in `.drafts/geocode_cache.json`.
5. Landtag Drucksache 20/4417, Anlage 2 (FAG 2025 list), as in Q0.2.

## Outputs

- `r2_fag_pools_wind_proximity.csv`: 166 units with coordinates, geocode match, relief region,
  nearest-turbine distance, turbines within 5 and 10 km.
- `r2_locational_value.py`: reproduces geocoding (from cache), proximity and the tables.
