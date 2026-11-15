# R1: Electrification-conditional flexibility potential of German swimming baths

**A first-order re-run of a published potential-assessment method on an electrified counterfactual.**
Desk result, reproducible from `r1_flexibility_calc.py` and the evidence files in
`.drafts/evidence/`. Status labels per `README.md`.

---

## 1. The claim being tested

German reference demand-response accounting for the tertiary sector assigns swimming baths a
flexible-technology share of zero. The hypothesis from the gap map: the zero is an artefact of the
method, which counts flexible *electric* appliances while pool flexibility is *thermal* and the heat
is fossil. If so, the flexibility that appears only after a fuel switch is invisible to the standard
method, for pools and for every other gas-heated public building class.

This document tests whether the artefact is real and how large the invisible quantity is.

## 2. Method

Take the published method exactly as its authors define it, and change one thing: the fuel.

**The published method.** Wohlfarth, Klobasa and Eßer, "Setting course for demand response in the
service sector", *Energy Efficiency* (2019) 12, 327-341, online-first 2018,
doi:10.1007/s12053-018-9728-3. Their Table 3 lists the appliances they treat as flexible. Their
Table 4 takes each subsector's 2013 electricity consumption by end use from Schlomann et al. (2015)
and sums the consumption falling into those flexible appliance categories; that sum is the "sum of
relevant shares", which they describe as the available *theoretical* flexibility potential, to be
revised downward for technical limits.

**The one change.** Table 3 includes "Heat pump/recirculation pump" (category: space heating) and
"Electric water heating" (category: hot water) as flexible appliances. So if pool heat were
delivered by heat pumps, that electricity would sit inside the flexible categories under their own
rules. The counterfactual replaces the fossil heat supply with heat pumps, converts the heat to
electricity at a seasonal performance factor, and re-reads the table.

**Two heat bases**, because the survey behind Table 4 flags baths as its least certain group:

- **Basis A**, like-for-like with Table 4: the same Schlomann survey's fuel and district-heat
  consumption for the "Bäder" group in 2013, covering all baths.
- **Bases B and C**, a modern narrower cross-check: the 2024 Umweltbundesamt extrapolation for
  municipal indoor and combination pools only, model and simple variants.

## 3. Inputs

| Input | Value | Source | Status |
|---|---|---|---|
| Baths electricity, 2013 | 1.4 TWh/a | Wohlfarth Table 4 | **VERIFIED** (local extraction) |
| Baths sum of relevant shares, 2013 | 0.0 TWh/a | Wohlfarth Table 4 | **VERIFIED** |
| Baths fuels + district heat, 2013 | 2.9 TWh/a | Schlomann et al. 2015, Kurzfassung, Tabelle 1, group 5/3 | **VERIFIED** (local extraction) |
| Baths total end energy, 2013 | 4.3 TWh/a | same | **VERIFIED** |
| Share of baths fuel use that is process heat (water heating) | 92.9% | Schlomann Tabelle 3 | **VERIFIED** for the figure; the column carrying the remaining 7.1% is **[verify]** (extraction layout) |
| Baths fuel carriers, 2013 | gas 0.9, district heat 1.6, wood 0.3 TWh (sum 2.8) | Schlomann Tabelle 2 | **[verify]** on the carrier assignment; column order checked against a neighbouring row |
| Municipal indoor + combi pools, heat | 1,340 GWh (model) to 1,636 GWh (simple) | Weinfurter, Thieme, Wallrodt, UBA TEXTE 139/2024, Tabelle 4, n = 1,390 | **VERIFIED** (local extraction) |
| Municipal indoor + combi pools, electricity | 396 to 482 GWh | same | **VERIFIED** |
| Per-pool mean heat / electricity (n = 67 respondents) | 1.21 / 0.36 GWh/a | same, Tabelle 1 | **VERIFIED** |
| Carrier mix among respondents (by count) | 53.7% gas, 44.8% district heat | same | **VERIFIED** |
| Seasonal heat-pump performance (JAZ) | 3.0 / 3.5 / 4.5 | trade-source ranges: air-water 3.1-3.3, ground-coupled 4.0-4.6, groundwater and wastewater 4.5-5.0+; no pool-specific measured value found | **[verify]** |
| Electrification share | 100% / 50% / 25% | assumption, sensitivity only | n/a |

Two caveats on the inputs, stated rather than buried:

- Schlomann et al. report that the confidence deviation on specific fuel and district-heat
  consumption is ±5% to just under ±15% for most groups "with the exception of the baths", meaning
  the 2.9 TWh figure carries a wider band than that. Its 2008 to 2013 series also falls from 7.2 to
  4.3 TWh total, which is steep enough to suspect survey composition effects. This is why Bases B
  and C exist. **VERIFIED** as the authors' own statement.
- Bases B and C cover a narrower population (municipal indoor and combination pools, n = 1,390)
  than Basis A (all baths, including outdoor, leisure and non-municipal). They should be read as a
  floor for the sector, not as a disagreement with Basis A. Per-pool sanity check: the UBA mean of
  1.21 GWh heat per municipal indoor pool against roughly 0.5 GWh per bath implied by Basis A over
  the national stock is consistent with outdoor pools being seasonal and small.

## 4. Result

Flexible sum ("sum of relevant shares") after electrification, TWh/a, full fuel switch:

| Heat basis | JAZ 3.0 | JAZ 3.5 | JAZ 4.5 |
|---|---|---|---|
| A: all baths, 2013 (2.90 TWh heat) | 0.97 | **0.83** | 0.64 |
| B: municipal indoor + combi, model (1.34 TWh) | 0.45 | 0.38 | **0.30** |
| C: municipal indoor + combi, simple (1.64 TWh) | 0.55 | 0.47 | 0.36 |

At 50% electrification, halve every cell; at 25%, quarter it. The full sensitivity grid is in the
script output.

**Headline.** Under the published method's own rules, electrifying pool heat moves Baths from
**0.0 to between 0.30 and 0.97 TWh/a** of theoretical flexible electricity, with a central estimate
of **0.83 TWh/a**. The band is wide because both the heat basis and the performance factor are
uncertain, and it is stated as a band for that reason.

**Where that sits in Table 4.** Ranked by sum of relevant shares, TWh/a, with flexible fraction of
subsector electricity:

| Subsector | Electricity | Flexible sum | Fraction |
|---|---|---|---|
| Retail trade | 22.5 | 6.8 | 30% |
| Hotels, restaurants, homes | 18.5 | 5.4 | 29% |
| Office-like enterprises | 29.5 | 3.6 | 12% |
| Agriculture | 4.3 | 1.3 | 30% |
| Construction industry | 3.8 | 0.9 | 24% |
| **Baths, electrified, central** | **2.2** | **0.83** | **37%** |
| Hospitals | 6.1 | 0.8 | 13% |
| Schools | 3.9 | 0.3 | 8% |
| Airports | 1.3 | 0.3 | 23% |
| **Baths, electrified, most conservative corner** | **1.7** | **0.30** | **18%** |
| Baths, as published | 1.4 | 0.0 | 0% |
| Laundries, as published | 0.3 | 0.0 | 0% |

Two readings.

**In absolute terms**, the central case places baths level with Hospitals and Construction. Even
the most conservative corner (narrowest population, highest performance factor) matches Schools and
Airports, both of which the published method scores as non-zero.

**In flexible fraction**, the central case exceeds every subsector in the table. This is the more
telling number, and it has a physical reason: roughly 93% of a bath's heat goes into water, and
water is a storage-capable medium, so almost the entire electrified load falls into flexible
categories. Retail's 30% is limited by how much of a shop's electricity is cooling; a bath's is
limited only by how much of its heat is water heating, which is nearly all of it.

## 5. What the result establishes, and what it does not

**Established.** The zero in the published table is an artefact of the method, not a property of
the asset. The method is blind to flexibility that exists only after a fuel switch. For baths, the
quantity hidden by that blindness is of the same order as the entire published flexible potential
of hospitals, and larger than that of schools by a factor of one to three. Both zeros in Table 4
(Baths, Laundries) are heat-and-water-dominated subsectors, which is consistent with the
blindness being to thermal flexibility under fossil supply rather than to baths in particular.

**Not established, and the actual research content of a paper on this.**

1. **The technical revision.** Table 4 is theoretical; the authors say so. The technical fraction
   for pools depends on how far and for how long water and hall temperature may deviate within
   hygiene rules (DIN 19643), user comfort and the recovery time of the plant. That is the
   flexibility envelope, gap R4 in the map, and it is where the physics and the regulation meet.
   Hypothesis, not finding: the technical fraction for pools may be *higher* than for retail
   cooling, because water thermal mass permits multi-hour shifting where a chiller permits minutes.
2. **The electrification trajectory.** The counterfactual is a full switch. Who electrifies, by
   when, under which grant regime and which municipal heat plan, is the quantity that turns a
   potential into a forecast. Kommunale Wärmeplanung and the renovation backlog decide it.
3. **Stock heterogeneity.** The sector figure hides the spread. The UBA respondents range from
   0.17 to 3.11 GWh of heat per pool. Flexibility value is not linear in size.
4. **The performance factor.** No measured seasonal JAZ for a German indoor pool heat pump was
   found. The 3.0 to 4.5 band is from general installation types. One instrumented site would
   narrow the headline by a third.
5. **Interaction with existing CHP.** Many pools run combined heat and power. A heat pump beside a
   CHP unit makes the site a generator and a load with opposing signals, and installations under
   existing TSO contracts with CHP plants are excluded from §13k EnWG. Not modelled here.

## 6. Generalisation

The same survey gives Schools 16.5 TWh/a of fuels and district heat in 2013, against 3.9 TWh/a of
electricity and 0.3 TWh/a flexible. Applying the same counterfactual to schools would produce a
number that dwarfs the pool result. **[verify]** before doing so: school heat is mostly space
heating with far less thermal storage than a pool, so the technical fraction would be much lower,
and the like-for-like comparison holds only at the theoretical level. The correct general statement
is that the reference method under-counts every gas-heated building class in proportion to its heat
demand, and the *usable* share of that under-count is asset-specific. Pools are the clearest case
because their heat is process heat into water.

## 7. What this means for the project

The advertised "Data Acquisition & Profiling" package is written as a collection task. This result
converts it into a research input: the stock-level parameters it would produce (heat demand,
carrier, plant type, water volume, opening pattern) are exactly what is needed to compute
electrification-conditional potential at state scale and to replace the sector-level band above
with a distribution. The "Technical Assessment" package supplies the envelope that turns
theoretical into technical. The two packages together are the paper.

---

## Sources

1. Wohlfarth, K., Klobasa, M., Eßer, A. (2019). Setting course for demand response in the service
   sector. *Energy Efficiency* 12, 327-341. Online-first 2018. doi:10.1007/s12053-018-9728-3.
   Open-access PDF: https://www.isi.fraunhofer.de/content/dam/isi/dokumente/ccx/2018/Wohlfarth2018_Article_SettingCourseForDemandResponse.pdf
   Local extraction: `.drafts/evidence/wohlfarth2018_energy-efficiency_pdftotext-layout.txt`
2. Schlomann, B. et al. (2015). Energieverbrauch des Sektors Gewerbe, Handel, Dienstleistungen
   (GHD) in Deutschland für die Jahre 2011 bis 2013, Kurzfassung. Fraunhofer ISI for BMWi.
   https://www.isi.fraunhofer.de/content/dam/isi/dokumente/ccx/2015/Schlussbericht-GHD_2006-2013_Kurzfassung_Februar2015.pdf
   Local: `.drafts/evidence/schlomann2015.pdf` and two text extractions (layout, raw).
3. Weinfurter, M., Thieme, L., Wallrodt, S. (2024). Ermittlung der Datenverfügbarkeit und
   Bestimmung des Endenergieverbrauchs der kommunalen Hallen- und Kombibäder in Deutschland.
   Umweltbundesamt, TEXTE 139/2024, Hochschule Koblenz.
   https://www.umweltbundesamt.de/system/files/medien/11850/publikationen/139_2024_energieverbrauch_schwimmbaeder.pdf
   Local: `.drafts/evidence/uba2024_pools.pdf` and text extraction.
4. Bekanntmachung der Regeln für Energieverbrauchswerte und der Vergleichswerte im
   Nichtwohngebäudebestand, BAnz AT 03.05.2021 B1. Category 32 Schwimmhallen. Not used in the
   calculation; retained for the flexibility-envelope work (R4), where its dehumidification
   partial value of 30.0 kWh/m²a is directly relevant.
   https://geg-info.de/geg/210503_bmwi_bmi_regeln_energieverbrauchskennwerte_nichtwohnbestand.pdf
5. Heat-pump JAZ ranges, trade sources, **[verify]**:
   https://www.heizungsfinder.de/waermepumpe/wirtschaftlichkeit/jahresarbeitszahl ;
   https://greenox-group.de/grundwasserwaermepumpe ;
   https://www.energiefluss24.de/waermepumpe/jahresarbeitszahl
