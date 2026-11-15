# R5: Who can commit a municipal pool to a grid signal, and what it costs to do so

**Desk analysis of the institutional chain between a Schleswig-Holstein municipal pool and the
§13k EnWG instrument: who decides, what participation requires, where the hygiene floor sits,
and whether the value covers the fixed cost.** Reproducible in its numerical part from
`r5_participation_cost.py`; sources in `.drafts/evidence/`. Status labels per
`README.md`.

---

## 1. The question

"Operator willingness" treats an organisation as though it had preferences. A municipal pool has a
council, a treasury, an operating entity, a plant manager, a health authority looking over its
shoulder, and a network operator at the connection point. R5 asks: who holds the right to let an
external signal move the heat plant, what the instrument actually demands of them, what legal
floor the water temperature has, and whether a single pool's value clears the fixed cost of taking
part. R1 and R4 establish what a pool can offer; R5 asks whether anyone can lawfully and
economically offer it.

## 2. What §13k participation requires, from the primary texts

**The statute** (§13k EnWG, current text, **VERIFIED**):
- Eligible participants are "ausschließlich Betreiber von registrierten zusätzlich zuschaltbaren
  Lasten in Entlastungsregionen (Entlastungsanlagen) oder Aggregatoren solcher Anlagen" (Abs. 3).
- Excluded are installations "für die eine vertragliche Vereinbarung nach § 13 Absatz 6a zwischen
  Betreibern von Übertragungsnetzen mit Betreibern von KWK-Anlagen besteht." The exclusion is
  specific to CHP plants under a §13(6a) TSO redispatch contract. A municipal pool's own CHP unit
  is not, by itself, excluded. This corrects a claim carried since the independent scan.
- The metering point must serve no other consumption; measurement is quarter-hourly; the TSO may
  set a minimum size not exceeding 500 kW; registration is monthly; unconsumed allocations carry a
  penalty (Abs. 5, 6).

**The additionality determination** (Bundesnetzagentur, Az. 4.12.05.04/1, 28 June 2024,
**VERIFIED**, Tenor verbatim). A load must fall into one of three segments, and in every case
"der Betreiber einer Anlage kann diese technisch steuern; alternativ kann sein Lieferant oder ...
der Aggregator, die Anlage technisch und rechtlich steuern."

| Segment | What a pool would field | Special conditions |
|---|---|---|
| 1, Substitution fossiler Wärmeerzeugung | An electric heater (Heizstab, Elektrodenkessel) beside the existing gas boiler or CHP | The *electric heater* may run at most 2% of the month's hours at full load outside §13k (about 15 h in a 31-day month); all of the operator's qualifying installations on the same heat system must participate |
| 3, Elektrolyseure und Großwärmepumpen | A heat pump of at least 100 kW electrical | First commissioned after 29 December 2023; no 2% rule |

The 2% rule therefore constrains a dedicated §13k heater, not the pool's total load. A pool that
electrifies with a new heat pump of 100 kW or more enters Segment 3 on investment additionality
alone. This corrects the first gap map's reading that the 2% test "sits awkwardly against a
near-constant load."

**The TSO concept** (Umsetzungskonzept v2.0, 1 April 2026, **VERIFIED**), what the installation
and the participant must show:
- Installation (5.2.1): commissioned; inside a relief region; "einen eigenen Anschluss an das Netz
  der allgemeinen Versorgung"; "in ihrer Fahrweise flexibel (steuerbar und nicht
  lastprofilgebunden)"; at least 100 kW electrical, or aggregated into an Entlastungsgruppe of at
  least 100 kW within one region; not under a §13(6a) contract.
- Participant (5.1): takes the market role Einsatzverantwortlicher "unabhängig von den
  Eigentumsverhältnissen", signs the Rahmenvertrag with the TSO, builds and tests a communication
  channel (cyclic data, activation, confirmation), proves data provision for settlement.
- Process (6.2): monthly bid price at or above a Mindestpreis fixed per calendar year; daily
  availability report before 10:00 for the next day; the participant procures its own energy
  ("bilanzieller Ausgleich erfolgt eigenverantwortlich"); refund = max(reference price − bid, 0)
  per MWh actually consumed, reference price = day-ahead capped at about 400 EUR/MWh; variable
  levies compensated; fixed grid charges compensated only if an annual minimum availability set by
  the TSO is met; penalty = max(day-ahead − bid, 0) on every allocated MWh not consumed.
- Mindestpreis 2027 in the worked example: **21.68 EUR/MWh**, derived from a coal-CHP heat-cost
  comparison with a 50% discount.

**What that adds up to for a pool.** It must have, or add, a steerable electric heat source of
100 kW or more on its own metering point; hand technical and legal steering to itself, its supplier
or an aggregator; report every day whether it can absorb energy tomorrow; buy the energy itself;
consume what it is allocated or pay the refund back. Nothing here is beyond a municipal utility.
All of it is beyond a Bäderbetrieb acting alone.

## 3. Who decides

**The forms** (Ministry of the Interior's own guidance page, **VERIFIED** as that page):

| Form | Runs it | Oversight | Legal personality | Basis |
|---|---|---|---|---|
| Regiebetrieb (part of the administration) | Amt / Fachbereich | Gemeindevertretung | none | GO |
| Eigenbetrieb | Werkleitung | Werkausschuss, Gemeindevertretung | none; "ausgegliedertes Sondervermögen" (§97 GO) | §106 GO, EigVO |
| Kommunalunternehmen (AöR) | Vorstand | Verwaltungsrat | own | §106a GO, KUVO |
| GmbH (e.g. Stadtwerke, Schleswiger Kommunalbetriebe GmbH) | Geschäftsführung | Aufsichtsrat | own | §§101 ff. GO, Schrankentrias |
| Zweckverband / gemeinsames Kommunalunternehmen | per statute | Verbandsversammlung | own | §2, §19b GkZ |

Energy activity by a municipality (generation, procurement, distribution, supply of electricity,
gas, heat or cold) is presumed to serve a public purpose under §101a GO, so participation is
lawful in principle; the wording is **[verify]** (two consistent secondary sources; the statute
portal was not reachable).

**Three parties can stop it, and they are different parties.**

1. **The political body.** Signing a Rahmenvertrag with a TSO and an aggregator agreement that
   transfers "technische und rechtliche" steering of the heat plant to a third party is not routine
   operation. For an Eigenbetrieb the day-to-day is the Werkleitung's, but the EigVO reserves
   matters of fundamental significance to the Werkausschuss or the Gemeindevertretung
   (**[verify]** on the exact §5 list). Expect a committee decision, a public paper, and a cycle
   measured in months.
2. **The operator's non-delegable duty.** §37(2) IfSG (**VERIFIED**): water in public pools "muss so
   beschaffen sein, dass durch seinen Gebrauch eine Schädigung der menschlichen Gesundheit,
   insbesondere durch Krankheitserreger, nicht zu besorgen ist"; disinfection is mandatory; the
   Gesundheitsamt supervises (Abs. 3). No aggregator contract moves that duty. Whoever steers the
   plant, the operator answers for the water, so the steering right has to be bounded by
   temperature limits the operator sets. That is the contractual shape of blind spot A.
3. **The connecting network operator.** The concept records that a DSO confirmation in
   registration, "ein Veto-Recht zur Wahrung der Betriebshoheit des Anschlussnetzbetreibers", was
   discussed with distribution operators (**VERIFIED** as recorded discussion, not as an adopted
   rule). SH Netz can, at minimum, condition the connection of a 100 kW+ steerable load.

The dispatch right, in other words, is not held by anyone. It is assembled from a council
resolution, an operator's reserved temperature floor, and a network operator's connection
consent, and it can be withdrawn at any of the three.

## 4. The temperature floor

No statute fixes pool water temperature. The law fixes hygiene (IfSG §37, DIN 19643 as the
recognised standard). Temperature enters through design guidance and through hygiene indirectly.

The KOK-Richtlinien für den Bäderbau, 6th edition 2022, Table 22, as reproduced by the Deutscher
Städtetag (Hinweise 4.2, 2025, **VERIFIED**):

| Basin | Water °C | Hall air °C |
|---|---|---|
| Kleinkinderbecken | 28 to 32 | 30 to 34 |
| Nichtschwimmer-, Mehrzweck-, Schwimmerbecken | 24 to 28 | 26 to 30 |
| Freibad, all basins | 24 to 26 | |

Hall air two to four kelvin above water, never above 34 °C. Legionella controls apply from
23 °C in aerosol-forming circuits (**[verify]**, search-level).

**Consequence for R4, and for which pools to pilot.** A sports pool run at 28 °C sits at the top of
its design band. A +2 K charge takes it outside guidance; the operator's upward headroom is zero
and its flexibility is discharge-only. A children's or teaching pool at 28 to 30 °C has two to four
kelvin of headroom within guidance. The storage envelope is therefore asymmetric and pool-type
specific, and the pools with the most headroom are the ones whose users are most sensitive. This
refines R4's assumption of a +2 K charge from 28 °C: it applies cleanly to teaching and children's
pools, and to sports pools only where they run below 28 °C.

## 5. Does the value cover the fixed cost?

First-order model, one site, every input labelled in `r5_participation_cost.py`.

**Value per allocated MWh.** Normal supply at 17.2 ct/kWh (BDEW Strompreisanalyse 2026, small and
mid-size industry contracts, **[verify]** from summary) against a §13k net cost of the bid floor
21.68 EUR/MWh plus about 10 EUR/MWh of uncompensated residuals (assumption): **about
140 EUR/MWh**.

**Volume.** Plant size × allocated hours × storage headroom. Allocated hours from the concept's
worked example: 900 per region-year. Headroom 1.0 for a pool with KOK band to spare, 0.35 for a
sports pool at 28 °C (assumption).

**Cost.** One-off about 18,000 EUR per site (separate metering point, aggregator onboarding and
communication test, the council and contract process); annual fixed about 4,600 EUR; aggregator
fee 25% of gross (**[verify]**, typical band 15 to 30%). All assumptions, stated as such.

| Plant | Allocated h | Headroom | MWh/yr | Gross EUR/yr | Net EUR/yr | 8-year, undiscounted, after one-off |
|---|---|---|---|---|---|---|
| Large Hallenbad heat pump, 150 kW | 900 | 1.00 | 135 | 18,900 | **9,600** | **+58,900** |
| same | 900 | 0.35 | 47 | 6,600 | 400 | −15,000 |
| same | 450 | 1.00 | 68 | 9,500 | 2,500 | +2,000 |
| Teaching-pool plant, 60 kW (below 100 kW, must aggregate) | 900 | 1.00 | 54 | 7,600 | 1,100 | −9,300 |
| same | 450 | 0.35 | 9 | 1,300 | −3,600 | −46,800 |

**Reading.** Value scales with kilowatts, allocated hours and headroom; cost is fixed per site. A
large Hallenbad with a 150 kW heat pump and room in its KOK band clears its costs with a modest
surplus. A sports pool at the top of its band roughly breaks even at best. Anything under 100 kW
cannot participate alone and does not pay for its own onboarding. Halve the allocated hours, which
is what a continuing fall in curtailment would do, and only the best case survives.

The scan's economist lens said the transaction cost per kilowatt-hour for a 1 to 3 GWh/a heat
consumer with no trading desk was the real question. To first order: yes, and the answer is that
it works only as a fleet. One aggregator, one council paper per Zweckverband, one metering
standard, many pools.

## 6. What this establishes, and what it does not

**Established.** The legal path exists and is not exotic; the practical path runs through an
aggregator taking the EIV role; the dispatch right is a three-party construction, not a thing an
operator has; the temperature floor is design guidance rather than statute, which makes it
negotiable in a way hygiene is not, and makes the envelope pool-type specific; and single-site
economics are marginal outside the best case, so the willingness question is really a
consolidation question.

**Not established.**
1. The EigVO's exact list of council-reserved decisions and whether a steering-right transfer sits
   on it. **[verify]** by reading §5 EigVO.
2. §101a's wording and any Örtlichkeit or approval condition. **[verify]**.
3. Actual aggregator terms for a load of this size; the 25% is a band, not a quote.
4. Whether SH Netz has adopted a connection confirmation for §13k loads or only discussed one.
5. The residual uncompensated cost per MWh, taken as 10 EUR.
6. Allocated hours in T5 and T6 specifically; the 900 is a generic worked example.

## 7. What this means for the project

The willingness package should not survey preferences. It should map, per municipality, which of
the five forms runs the pool, which body would have to resolve, who the plant manager reports to,
and whether a Stadtwerk already holds an aggregator or EIV role it could extend. The 107
administrative units in the FAG list are the frame; the 34 that answered the Landtag are the warm
start. The instrument to build is an *authority-and-capacity* instrument, and the deliverable is a
contract architecture with a reserved temperature floor, not an attitude scale.

For piloting: screen on three things this pass makes explicit. A heat pump of 100 kW or more
commissioned after 29 December 2023, or a plan for one. A Kreis inside T5 or T6 (R2). And a KOK
band with headroom, which points to teaching and children's pools first, with the service-quality
question that raises put on the table rather than avoided.

---

## Sources

1. § 13k EnWG, current text. https://www.gesetze-im-internet.de/enwg_2005/__13k.html
   Local: `.drafts/evidence/enwg_13k_text.txt`.
2. Bundesnetzagentur, Festlegung Zusätzlichkeitskriterien § 13k EnWG, Az. 4.12.05.04/1,
   28 June 2024.
   https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Versorgungssicherheit/NSA/Festlegungskriterien.pdf
   Local: `.drafts/evidence/bnetza_13k_zusaetzlichkeit_2024-06-28.pdf` and text.
3. ÜNB Umsetzungskonzept § 13k EnWG, v2.0, 1 April 2026 (as in R2), sections 5 and 6.
4. § 37 IfSG. https://www.gesetze-im-internet.de/ifsg/__37.html  Local: `.drafts/evidence/ifsg_37_text.txt`.
5. Deutscher Städtetag, Arbeitskreis Energiemanagement, Hinweise 4.2 "Raumtemperaturen und
   Beleuchtungsstärken im Gebäudebestand" (2025), reproducing KOK-Richtlinien 6th ed. 2022, Table 22.
   https://www.staedtetag.de/files/dst/docs/Dezernat-6/2025/Hinweise_4_2_Raumtemperaturen.pdf
   Local: `.drafts/evidence/staedtetag_raumtemperaturen_2025.pdf` and text.
6. Schleswig-Holstein, Ministerium für Inneres, "Aufgabenerfüllung durch die Gemeinden als
   öffentlich-rechtliche oder privatrechtliche Unternehmen".
   https://www.schleswig-holstein.de/DE/landesregierung/themen/inneres-sicherheit-verwaltung/kommunales/kommunaleWirtschaft/_documents/durchfuehrung.html
7. § 101, § 101a GO SH, **[verify]** wording: Haufe norm pages and lexsoft (search-level).
8. BDEW Strompreisanalyse 2026, **[verify]** from summary. https://www.bdew.de/service/daten-und-grafiken/bdew-strompreisanalyse/
9. UBA, Regelwerke und Normen (DIN 19643 context).
   https://www.umweltbundesamt.de/themen/wasser/schwimmen-baden/regelwerke-normen

## Outputs

- `r5_participation_cost.py`: the single-site cost-benefit with all assumptions in one place.
