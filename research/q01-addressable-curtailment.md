# Q0.1: What share of Schleswig-Holstein's curtailment can a distribution-connected pool reach?

**The question inverts on contact with the primary sources. Almost all of the curtailment is
transmission-caused, and that is the part a pool can reach; the distribution-caused residual is a
few percent and has no instrument at all.** Reproducible from `q01_dso_congestion_join.py`;
sources in `.drafts/evidence/`. Status labels per `README.md`.

---

## 1. The question, and why it was thought to be blocked

The first gap map treated the state's "over 65% ordered by TenneT" figure as a threat to the
project's premise: if the binding constraint sits in the transmission network, a pool hanging off a
distribution feeder may have no claim on the curtailed energy. R2 tested the advertised proximity
proxy and found it predicts §13k eligibility 32% of the time, but left the underlying physical
question open, and both R2 and the sequencing document recorded Q0.1 as needing SH Netz data that
are not public.

That was too pessimistic. Three public sources bear on it directly, and they agree.

## 2. Where the curtailment is caused

**The state ministry, 15 April 2026.** "Über 65% dieser Abregelungen werden von der SH Netz auf
Anforderung des vorgelagerten Netzbetreibers Tennet durchgeführt und resultieren aus Engpässen im
Übertragungsnetz (teilweise außerhalb Schleswig-Holsteins)." And, separately, "Der überwiegende
Anteil der Abregelungen wird durch Engpässe im Übertragungsnetz ausgelöst." **VERIFIED**, full
report extracted locally.

**The network operator's own planning documents.** SH Netz has published the same causal statement
in three successive documents. The 2017 network-situation paper quantifies it:

> "Eine Besonderheit in Schleswig-Holstein ist, dass einige 110-kV-Freileitungen vor Überlastung
> geschützt und somit Einspeiseleistungen reduziert werden müssen, weil der Abtransport in das
> Höchstspannungsnetz noch nicht möglich ist. Die Verursachung für diese Abregelungen liegt **in
> über 90 Prozent der Fälle nicht im 110-kV-Netz von SH Netz**, sondern in der noch nicht
> ausreichend vorhandenen Verfügbarkeit des Höchstspannungsnetzes."

**VERIFIED.** The Netzausbauplan 2022 and the Netzausbauplan 2024 (Stand 30.04.2024) repeat the
statement verbatim without the percentage, so the direction is current and only the figure is
dated. The same documents note that SH Netz carries over 90% of the state's renewable capacity,
about 8 GW across 34,000 installations as of 2017, so this is not a marginal operator.

**The arithmetic.** Of 802 GWh curtailed on land in 2025, at least 521 GWh is TenneT-ordered. Of
the roughly 281 GWh SH Netz instructs itself, over 90% of cases are caused by the extra-high-voltage
network rather than its own 110 kV network. That leaves **on the order of 28 GWh, about 3%,
genuinely caused in the distribution network.** Indicative only: the 65% is a 2026 volume share and
the 90% a 2017 case share, and both are lower bounds on transmission causation, so the residual is
an upper bound.

**Independent confirmation, and the strongest single piece of evidence.** §13k Abs. 8 EnWG lets
distribution operators with 110 kV networks and more than 100,000 customers run their own
"Nutzen statt Abregeln" from 1 April 2025, conditional on curtailment **caused in their own
network** reaching a threshold over the previous two calendar years. The transmission operators'
implementation concept records the outcome of their coordination with the distribution operators at
the end of 2025:

> "Die Abstimmung der ÜNB mit den VNB Ende 2025 zur weiteren Ausgestaltung des Umsetzungskonzeptes
> hat ergeben, dass die VNB **absehbar keinen eigenständigen Anwendungsfall** für 'Nutzen statt
> Abregeln' und Ausweisung von VNB-Entlastungsregionen gem. §13k Abs. 8 EnWG sehen."

**VERIFIED.** The distribution operators, given a statutory route to monetise their own congestion,
declined it. That is a market participant's revealed judgment on exactly the quantity this question
asks about, and it agrees with the 3%.

## 3. Why that is good news, not bad

The original worry conflated two different questions. *Where is the constraint caused* is not the
same as *where must a load sit to relieve it*.

A load that consumes energy north of a transmission bottleneck relieves that bottleneck regardless
of which voltage level it hangs off. This is not an argument, it is what the instrument is built to
do: §13k designates relief regions precisely so that additional switchable loads, most of them
distribution-connected, can absorb energy that transmission congestion would otherwise waste. The
concept's own explanation for including the Hamburg belt says so directly, that loads there reduce
redispatch needs "aufgrund von Netzengpässen südlich von Hamburg".

The federal data confirm the pattern at national scale. In Q4 2023, redispatch with renewables
split 1,657 GWh of measures at transmission level against 1,155 GWh at distribution level, while
causation split 2,193 GWh in the transmission network against 619 GWh in the distribution network.
**VERIFIED** from the Bundesnetzagentur tables. Distribution-connected assets are already the main
physical instrument through which transmission-level constraints are managed.

**So the answer to Q0.1 is: essentially all of the addressable curtailment in Schleswig-Holstein is
transmission-caused, and a distribution-connected pool reaches it through §13k, provided it sits in
a relief region.** The addressable quantity is not a fraction of 802 GWh but the large majority of
it. What is *not* addressable is the small distribution-caused residual, and that is the part with
no instrument.

This sharpens R2 rather than softening it. Relief-region membership is not a proxy for the right
variable; it **is** the right variable, because it is a certificate that consumption there relieves
the binding constraint. Turbine proximity is not a worse proxy for the same thing, it is a proxy for
a different thing that does not matter.

## 4. The future distribution case, which is elsewhere

SH Netz's Netzausbauplan 2024 identifies **twelve medium-voltage congestion regions** for the 2045
scenario, each described by the share of its line elements projected to be overloaded.
**VERIFIED** (the trigger columns for load and generation are garbled in extraction and are not
used here).

| Region | County | Netzcenter | Overloaded MV lines, 2045 | Indoor pools | In a §13k relief region |
|---|---|---|---|---|---|
| 4 | Ostholstein | Pönitz | **72%** | 7 | **no** |
| 9 | Segeberg | Segeberg, Kaltenkirchen | 67% | 6 | yes |
| 5 | Pinneberg | Uetersen | 63% | 11 | yes |
| 2 | Herzogtum Lauenburg | Schwarzenbek | 55% | 3 | **no** |
| 11 | Stormarn | Ahrensburg | 52% | 7 | yes |
| 1 | Dithmarschen | Meldorf | 48% | 4 | yes |
| 7 | Rendsburg-Eckernförde | Fockbek | 38% | 4 | yes |
| 8 | Schleswig-Flensburg | Schuby, Süderbrarup | 35% | 7 | yes |
| 12 | Neumünster | Neumünster | 34% | 1 | yes |
| 3 | Nordfriesland | Friedrichstadt, Niebüll | 29% | 11 | yes |
| 6 | Plön | Plön | 29% | 3 | **no** |
| 10 | Steinburg | Dägeling | 26% | 5 | yes |

Flensburg, Kiel and Lübeck do not appear: they are served by other distribution operators
(TraveNetz in Lübeck, confirmed from the substation operator tags; Stadtwerke Flensburg;
Kiel `[verify]`). Any pool study in those cities faces a different operator and a different plan.

Two things follow. First, the counties with the worst projected future distribution congestion are
not the counties with today's transmission-caused curtailment, and three of them (Ostholstein,
Herzogtum Lauenburg, Plön) are outside the §13k relief regions entirely. Ostholstein tops the list
at 72% and holds seven indoor pools that can claim nothing today. Second, these are 2045 scenario
projections, not current constraints, so they describe a value proposition on a different timescale
through a different mechanism.

That mechanism is named by the state ministry in the same report, and it is quotable:

> "Kurz- und mittelfristig müssen zudem verstärkt Anstrengungen unternommen werden, EE-Leistung
> bereits auf der unteren Netzebene zu nutzen. Dies können neue industrielle Großverbraucher sein,
> aber auch eine flexiblere Integration von bestehenden Verbrauchern, z.B. durch **zuschaltbare
> Lasten** ..."

and, on connection to already-full networks, "flexible Netzanschlussvereinbarungen". **VERIFIED.**
The state is asking for switchable loads at lower network levels; the instrument for the
distribution case is flexible connection agreements rather than §13k.

## 5. What this establishes, and what it does not

**Established.** The transmission share of Schleswig-Holstein's curtailment causation is not a
problem for the project, it is the project's addressable market, reachable through §13k inside the
relief regions. The distribution-caused residual is a few percent and the distribution operators
have formally declined to build an instrument for it. Future distribution congestion is projected
across all twelve SH Netz regions and is worst in three counties that cannot participate in §13k
today.

**Not established.**
1. The exact current split. The 90% figure is from 2017 and no later quantification was found. The
   qualitative statement is repeated in 2022 and 2024, so the direction holds; a current number
   would need to come from SH Netz.
2. Whether any individual pool sits on a feeder that is itself constrained. The congestion regions
   are county-shaped, so they locate the question and do not answer it. This is the part that still
   needs operator data, and it is now a narrower request: not "attribute your curtailment" but
   "is this facility's feeder in region N's overloaded set".
3. The twelve regions' trigger split between load-driven and generation-driven congestion, which
   the extraction garbled and which bears on whether an added load helps or hurts.
4. Whether the §13k Abs. 8 threshold was ever formally tested for SH Netz, or whether the operators
   simply judged it not worth pursuing.

## 6. What this means for the project

The geospatial package should stop asking how far a pool is from generation and start asking two
questions on two timescales. Today: is the pool in a §13k relief region, which is public and
decisive, and which R2 has already answered for all 166 units. Toward 2045: is the pool in a
medium-voltage congestion region, and on which of its feeders, which is the question to put to SH
Netz under the collaboration the post anticipates.

For the roadmap, the two timescales point at partly different pools. The §13k case is available now
and covers 59 of 76 indoor units. The distribution case is a 2045 proposition, runs through flexible
connection agreements rather than §13k, and is strongest in Ostholstein, Segeberg and Pinneberg.
A roadmap that offers only the first leaves the counties with the worst projected future congestion
with nothing to do.

---

## Sources

1. MEKUN Schleswig-Holstein, "Stromnetz-Engpassmanagement in Schleswig-Holstein: Übersicht über
   Erzeugung und Abregelungen von Strom aus Erneuerbaren Energien in den Jahren 2015 bis 2025",
   Kiel, 15 April 2026.
   https://www.schleswig-holstein.de/DE/fachinhalte/N/netzausbau/Downloads/bericht_engpassmanagement_sh.pdf
   Local: `.drafts/evidence/mekun_engpassmanagement_sh_2026-04-15.pdf` and text.
2. Schleswig-Holstein Netz AG, "Netzsituation und Besonderheiten der Schleswig-Holstein Netz AG"
   (NAP110, 2017), for the over-90% statement.
   https://www.sh-netz.com/content/dam/revu-global/sh-netz/Documents/Schleswig-Holstein-Netz/Netzausbau110/NAP110kV/Netzsituation%20und%20Besonderheiten%20NAP110%202017%20SHN%20Internet.pdf
   Local: text extraction only, `.drafts/evidence/shnetz_netzsituation_besonderheiten_2017_pdftotext.txt`.
3. Schleswig-Holstein Netz AG, Netzausbauplan 2024 (Netzbericht nach § 14d Abs. 4 EnWG, Stand
   30.04.2024), sections 4 and 5.3 and Tabelle 6.
   https://www.sh-netz.com/content/dam/revu-global/sh-netz/Documents/Schleswig-Holstein-Netz/Netzausbau110/NAP110kV/Netzausbauplan_2024.pdf
   Local: text extraction only (the PDF is 55 MB).
4. Schleswig-Holstein Netz AG, Netzausbauplan 2022. Local: PDF and text.
5. ÜNB Umsetzungskonzept § 13k EnWG v2.0, 1 April 2026, on §13k Abs. 8 and the distribution
   operators' position (as in R2 and R5).
6. § 13k Abs. 8 EnWG. Local: `.drafts/evidence/enwg_13k_text.txt`.
7. Bundesnetzagentur, Netzengpassmanagement, Tabellen Q4 2023, Tabelle 4 (causation) and Tabelle 9
   (by federal state).
   https://data.bundesnetzagentur.de/Bundesnetzagentur/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/Versorgungssicherheit/Engpassmanagement/TabellenQ4in2023.xlsx
   Local: `.drafts/evidence/bnetza_netzengpassmanagement_tabellen_q4_2023.xlsx`.
8. SMARD, "Maßnahmenvolumen im Gesamtjahr stabil" (2025 figures), for the national trend.
9. OpenStreetMap substations in DE-SH via Overpass, 11 September 2026, for distribution-operator
   territories. Local: query and JSON in `.drafts/evidence/`.

## Outputs

- `q01_dso_congestion_join.py`: the causation arithmetic and the county join.
- `q01_fag_pools_dso_congestion.csv`: 166 units with relief region, wind proximity, and their
  county's medium-voltage congestion region and projected 2045 overload share.
