# Process record R5: Dispatch authority and cost of participation

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. Result document: `../r5-dispatch-authority.md`. Worked 2026-09-11.

---

## Part A. One-page method summary

**Question.** Who can lawfully commit a Schleswig-Holstein municipal pool's heat plant to an
external grid signal, what does §13k participation actually require, what legal floor does the
water temperature have, and does a single site's value cover the fixed cost of taking part?

**Sources.** §13k EnWG (statute text); Bundesnetzagentur Festlegung Zusätzlichkeitskriterien,
Az. 4.12.05.04/1, 28 June 2024 (operative Tenor); ÜNB Umsetzungskonzept v2.0, 1 April 2026,
sections 5 and 6 (registration, tender, remuneration, penalty); §37 IfSG; KOK-Richtlinien für den
Bäderbau 6th ed. 2022, Table 22, as reproduced in Deutscher Städtetag Hinweise 4.2 (2025); the
Schleswig-Holstein Interior Ministry's guidance page on municipal enterprise forms; BDEW
Strompreisanalyse 2026 (summary level); §101, §101a GO SH (secondary sources only; the statute
portals could not be retrieved by script).

**Method.** Primary legal texts were fetched and read verbatim. Participation requirements were
tabulated from statute, determination and concept. The legal forms a pool can take and the bodies
that decide were tabulated from the ministry's guidance. The hygiene duty and the temperature
design bands were separated (statute versus guidance). A first-order single-site cost-benefit was
built with every input labelled: value per allocated MWh from the price spread between normal
supply and the §13k bid floor; volume from plant size, allocated hours and storage headroom; costs
from the concept's requirements with stated assumptions.

**Result.** The dispatch right is not held by any one party; it is assembled from a council
resolution, the operator's non-delegable hygiene duty (which forces a reserved temperature floor),
and the connecting network operator's consent. Participation requires a steerable electric heat
source of at least 100 kW on its own metering point, an Einsatzverantwortlicher (operator or
aggregator), daily availability reporting, self-procurement of energy, and acceptance of a penalty
on unconsumed allocations. No statute sets water temperature; KOK design bands are 24 to 28 °C for
sports pools and 28 to 32 °C for children's pools, so a sports pool at 28 °C has no upward
headroom. A 150 kW heat pump with headroom nets about 9,600 EUR a year; a sports pool at the top
of its band roughly breaks even; anything under 100 kW cannot participate alone and does not pay
for its onboarding.

**Status.** Statute, Tenor, concept mechanics, IfSG §37 and the KOK table VERIFIED verbatim.
§101a wording, the EigVO reserved-decision list, the BDEW figure, the aggregator fee band and the
Legionella threshold `[verify]`. Cost-model inputs are stated assumptions.

**Files.** `r5_participation_cost.py`; evidence: statute text, determination PDF and text, IfSG
text, Städtetag PDF and text; `verification_log.md` seventh pass; corrections C12 to C15.

---

## Part B. Full trail

### B.1 Origin

1. The independent scan's economist and practitioner lenses had raised two questions the earlier
   passes could not answer from energy sources alone: whether a municipal organisation can commit
   an asset to an external signal at all, and whether the fixed cost of participation for a 1 to
   3 GWh/a heat load exceeds the value. R2 had made §13k eligibility concrete by Kreis; R5 was
   selected next to test the instrument's rules against a pool.

### B.2 Primary texts

2. Five pulls were issued in parallel: the statute from gesetze-im-internet.de (HTML, stripped to
   text); the Bundesnetzagentur determination PDF (downloaded, extracted); the participation
   sections of the concept already on disk (searched for registration, aggregator, metering,
   minimum size, penalty, remuneration, price definitions); a search on Schleswig-Holstein
   municipal law for pool operators; a search on the legal basis of pool water temperature.
3. Statute, read verbatim. Eligible participants are operators of registered additional switchable
   loads in relief regions, or their aggregators (Abs. 3 S. 1). Excluded are installations "für die
   eine vertragliche Vereinbarung nach § 13 Absatz 6a zwischen Betreibern von Übertragungsnetzen
   mit Betreibern von KWK-Anlagen besteht" (Abs. 3 S. 2). Registration requires a metering point
   serving no other consumption, quarter-hourly measurement, a TSO minimum size of at most
   500 kW, and monthly registration (Abs. 6 Nr. 3). Unconsumed allocations carry a penalty
   (Abs. 5). The target model uses daily competitive tenders (Abs. 2).
4. Determination, Tenor read verbatim. General conditions: the operator can technically control
   the installation, or the supplier or aggregator can control it "technisch und rechtlich"; no
   §13(6a) contract. Segment 1, substitution of fossil heat: the installation may consume at most
   the equivalent of 2% of the month's hours at full load outside §13k (worked example: 10 MW,
   October, 14.88 h, 148.8 MWh), and all of the operator's qualifying installations on the same
   heat system must participate. Segment 2, storage. Segment 3, electrolysers and heat pumps of at
   least 100 kW, first commissioned after 29 December 2023, with no 2% rule. The reasoning notes
   that operation on a standard load profile is incompatible with the flexibility requirement.
5. Concept sections 5 and 6 read. Installation requirements 5.2.1 a to f: commissioned; in a
   relief region; "einen eigenen Anschluss an das Netz der allgemeinen Versorgung"; "in ihrer
   Fahrweise flexibel (steuerbar und nicht lastprofilgebunden)"; at least 100 kW; no 6a contract.
   Loads under 100 kW may aggregate into a group of at least 100 kW within one region. The
   participant takes the role Einsatzverantwortlicher "unabhängig von den Eigentumsverhältnissen",
   signs the Rahmenvertrag with the TSO, builds and tests a communication channel (cyclic data,
   activation, confirmation), proves data provision for settlement. A DSO confirmation in
   registration with a veto right "zur Wahrung der Betriebshoheit des Anschlussnetzbetreibers" is
   recorded as discussed.
6. Concept remuneration read. Monthly bid at or above a Mindestpreis fixed per calendar year;
   daily availability before 10:00; the participant procures its own energy; refund =
   max(reference price minus bid, 0) on the minimum of consumed and allocated energy, reference
   price = day-ahead capped at about 400 EUR/MWh; variable levies compensated; fixed grid charges
   compensated only if a TSO-set annual minimum availability is met, worked example 3,000 h;
   penalty = max(day-ahead minus bid, 0) on the unconsumed part of each hour's allocation.
   Mindestpreis in the 2027 example 21.68 EUR/MWh, derived as 43.37 × (1 minus 0.5) from a
   coal-CHP heat-cost comparison with a 50% discount.

### B.3 Corrections to earlier claims arising from the texts

7. C12. The scan, and summaries of it, had stated that installations under existing TSO contracts
   with CHP plants are excluded and that pools commonly run CHP, implying exposure. The statute
   and Tenor confine the exclusion to CHP plants holding a §13(6a) redispatch contract with a TSO;
   a pool's own CHP unit carries no such contract unless separately concluded.
8. C13. The first gap map had written that the 2% full-load-hour rule "sits awkwardly against a
   near-constant load". The rule applies to the additional electric heater in Segment 1 (and to
   storage in Segment 2), not to the facility's total consumption, and not at all to a Segment 3
   heat pump.
9. C15. The 3,000-hour minimum availability had been described in passing as unavoidable. It is a
   precondition only for compensation of fixed grid charges; participation and the per-MWh refund
   do not depend on it.

### B.4 Municipal law: forms and decision bodies

10. The search on municipal law returned the Eigenbetrieb provision (§106 GO), the EigVO of
    5 December 2017, a ministry page on enterprise forms, and an example of a pool run as a GmbH
    (Schleswiger Kommunalbetriebe GmbH). A second search on §101 returned secondary summaries of
    §101 (public purpose, capacity, subsidiarity) and §101a (energy activities presumed to serve a
    public purpose).
11. Four attempts to retrieve statute text by script failed: gesetze.io returned an application
    shell; the juris portal returned a redirect loop; umwelt-online failed on a self-signed
    certificate; Haufe returned a script shell. The AA EigVO PDF on the ministry site was
    downloaded and found to contain model forms, not guidance. The ministry's page on
    "Aufgabenerfüllung durch die Gemeinden" was fetched and yielded the forms table: Eigenbetrieb
    (Werkleitung, Werkausschuss, Sondervermögen §97 GO), Kommunalunternehmen (§106a GO, KUVO,
    Vorstand, Verwaltungsrat), gemeinsames Kommunalunternehmen (§19b GkZ), GmbH (Schrankentrias
    §§101 ff.), Zweckverband (§2 GkZ). A retry of the ministry's page on the 2016 reform of
    municipal economic law returned 404.
12. Decision: §101a's substance (energy presumption) was carried on two consistent secondary
    sources at `[verify]`; the EigVO's list of council-reserved decisions was carried at
    `[verify]`; both were listed as open checks to be read in a browser.

### B.5 The temperature floor

13. §37 IfSG was fetched and read. Abs. 2: water in public pools "muss so beschaffen sein, dass
    durch seinen Gebrauch eine Schädigung der menschlichen Gesundheit, insbesondere durch
    Krankheitserreger, nicht zu besorgen ist"; disinfection is mandatory. Abs. 3: supervision by
    the health authority.
14. The search on temperature returned DIN 19643 materials (hygiene, not temperature), the UBA
    statement that health authorities orient on DIN 19643 and the UBA recommendation because
    there is no pool-water ordinance, and the Städtetag energy-management note. The UBA 2014
    recommendation PDF returned an HTML page and could not be read; the Legionella threshold at
    23 °C was carried at `[verify]` from search level.
15. The Städtetag Hinweise 4.2 (2025) was downloaded and extracted. Its table reproduces the
    KOK-Richtlinien 6th edition 2022, Table 22: Kleinkinderbecken 28 to 32 °C water, 30 to 34 °C
    air; all other indoor basins 24 to 28 and 26 to 30; outdoor 24 to 26; hall air two to four
    kelvin above water, not above 34 °C.
16. C14. R4 had modelled a +2 K charge from a 28 °C sports pool. Against the KOK band, 28 °C is
    the top of the sports-pool range, so upward headroom under guidance is zero; children's and
    teaching basins carry two to four kelvin. R4's physics stands; its applicability is
    pool-type specific; Q0.2's fleet storage figure is an upper bound. Logged; not recomputed.

### B.6 Cost of participation

17. A search for a commercial electricity price benchmark returned the BDEW Strompreisanalyse:
    17.2 ct/kWh for small and mid-size industry supply contracts in 2026 so far (summary level).
18. The script `r5_participation_cost.py` was written. Saving per allocated MWh = 172 minus
    (21.68 bid floor plus 10 residual) = 140 EUR/MWh. Volume = plant kW × allocated hours (900 from
    the concept's example, and 450) × storage headroom (1.0 with KOK band to spare, 0.35 for a
    sports pool at 28 °C). Costs: one-off 18,000 EUR (separate metering point 4,000, aggregator
    onboarding and communication test 8,000, council and contract process 6,000); annual fixed
    4,600 (metering 600, administration 4,000); aggregator 25% of gross. Eight-year undiscounted
    total after one-off. All labelled as assumptions where they are.
19. Output: 150 kW plant, 900 h, headroom 1.0: 135 MWh, gross 18,943, net 9,607 per year, eight-
    year +58,859. Same with headroom 0.35: net 373, eight-year −15,019. 150 kW, 450 h, headroom
    1.0: net 2,504, eight-year +2,030. 60 kW plants: negative in every case and below the 100 kW
    threshold.

### B.7 How the conclusion was derived

The requirements are read directly from the three primary instruments (steps 3 to 6) and
tabulated; nothing is inferred about what participation demands. The three veto points follow
from three separately sourced facts: the steering-right transfer is a contract outside routine
operation (step 11, forms and bodies); the hygiene duty sits on the operator by statute and is not
transferable (step 13); a DSO confirmation is recorded in the concept (step 5). The temperature
floor is shown to be guidance, not statute, by the absence of any statutory temperature and the
presence of the KOK bands (steps 13 to 15), which then bound R4's envelope (step 16). The economics
are a transparent product of price spread, volume and fixed cost (steps 17 to 19), sensitive
mainly to headroom and allocated hours.

### B.8 Final conclusion

The legal path for a municipal pool into §13k exists and is not exotic, but it runs through an
aggregator taking the Einsatzverantwortlicher role and through three parties who can each stop it:
the council or works committee that must resolve the contract and steering-right transfer, the
operator whose IfSG §37 duty forces a reserved temperature floor into any such contract, and the
connecting network operator. Water temperature is bounded by design guidance rather than statute,
which makes it negotiable in a way hygiene is not and makes the storage envelope pool-type
specific: sports pools at 28 °C have no upward headroom, children's and teaching pools have two to
four kelvin. Single-site economics are marginal outside the best case of a 150 kW heat pump with
headroom and full allocated hours; the willingness question is therefore a consolidation question,
to be answered per municipality by legal form and decision body rather than by attitude survey.

**Status of the conclusion.** VERIFIED as to requirements, duty and design bands; ESTIMATE as to
economics (assumptions stated); `[verify]` as to §101a wording, EigVO reserved decisions, the
aggregator band and the Legionella threshold.

### B.9 What would change it

A read of §5 EigVO placing steering-right transfers within the Werkleitung's routine authority; a
real aggregator term sheet well below 25%; allocated hours in T5 and T6 far from 900; adoption by
SH Netz of a connection confirmation with conditions that bind; a KOK revision to the sports-pool
band.
