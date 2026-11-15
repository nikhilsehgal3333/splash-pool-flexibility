# Process record Q0.1: Addressable curtailment

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. Result document: `../q01-addressable-curtailment.md`. Worked 2026-09-11 to
2026-09-12.

---

## Part A. One-page method summary

**Question.** What share of Schleswig-Holstein's curtailed renewable energy can a
distribution-connected swimming pool actually reach? Recorded through five earlier passes as
blocked on non-public network-operator data.

**Sources.** MEKUN, Stromnetz-Engpassmanagement in Schleswig-Holstein, 15 April 2026 (full report,
not just the web page); Schleswig-Holstein Netz AG, Netzsituation und Besonderheiten (2017) and
Netzausbauplan 2022 and 2024; § 13k Abs. 8 EnWG; the transmission operators' implementation
concept v2.0 on the distribution-operator route; Bundesnetzagentur congestion-management tables
Q4 2023; SMARD 2025 figures; OpenStreetMap substations for operator territories.

**Method.** Primary-source causation analysis rather than modelling. The causal statements of the
network operator, the state ministry and the regulator were read verbatim and cross-checked against
each other and against federal data. A composite arithmetic was then computed and labelled
indicative. The spatial component was a county-level join of the 166-unit pool list to the
operator's twelve medium-voltage congestion regions.

**Result.** Of 802 GWh curtailed on land in 2025, at least 521 GWh is ordered by the transmission
operator; of the remainder, the network operator states that over 90% of its own cases are caused
by extra-high-voltage unavailability rather than its own 110 kV network. That leaves on the order
of 28 GWh, about 3%, genuinely distribution-caused. The distribution operators told the
transmission operators at the end of 2025 that they see no case for their own §13k Abs. 8
instrument, which independently confirms the same conclusion.

**The question inverts.** Where a constraint is caused is not where a load must sit to relieve it.
§13k exists precisely so that distribution-connected loads can absorb transmission-caused
curtailment. So essentially all of the addressable volume is transmission-caused, reachable through
§13k inside a relief region, and the unaddressable part is the small distribution residual.

**Status.** Every source statement VERIFIED by local extraction. The composite arithmetic is
indicative, combining a 2026 volume share with a 2017 case share. Feeder-level assignment remains
operator-held.

**Files.** `q01_dso_congestion_join.py`; `q01_fag_pools_dso_congestion.csv`;
`verification_log.md` eighth pass; corrections C16, C17, C18.

---

## Part B. Full trail

### B.1 Revisiting the blockage

1. Q0.1 had been recorded in the sequencing document as a Tier 0 question, restated in R2 as
   still standing, and described in conversation as blocked on non-public SH Netz data. Before
   accepting that a second time, the claim was tested: what exactly would the missing data be, and
   is there genuinely nothing public that bears on it.
2. Three source classes were identified as unpulled. The state report had only ever been read as a
   web page, not as the full PDF, and the "over 65%" figure in it *is* a causation attribution.
   Distribution operators have published redispatch measures since October 2021 under
   Redispatch 2.0. And the network operator's own 110 kV development plan, published under
   § 14d EnWG, must discuss where its congestion is.
3. The assessment was recorded as too strong and the question reopened. Logged afterwards as C16.

### B.2 The state report

4. The full report was downloaded and extracted. It is four pages of text plus an annex and it
   carries considerably more than the web page. Beyond the 802 GWh and the 65% attribution it
   states that the overwhelming share of curtailment is triggered by transmission congestion, that
   on-land renewable generation reached an all-time high of 22.3 TWh in 2025 despite a poor wind
   year, that 3.6% of on-land renewable generation was curtailed against over 17% in 2015, that
   state-level cost attribution has been impossible since Redispatch 2.0 in 2021, and that relief
   from the large direct-current links is expected only after 2028.
5. Two passages were noted for later use. The report calls for greater use of renewable output at
   lower network levels "z.B. durch zuschaltbare Lasten", and names flexible connection agreements
   for connecting to already-full networks. That is the state ministry asking for exactly the asset
   class the project studies.

### B.3 The network operator's own documents

6. A first download of the Netzausbauplan 2024 returned an HTML error page rather than a PDF. The
   request was retried with browser-like headers (user agent, accept, accept-language, referer),
   which returned the real file, 55 MB. The 2022 plan and the 2017 network-situation paper were
   retrieved the same way.
7. All three carry the same causal statement. The 2017 paper quantifies it: the cause of these
   curtailments lies "in über 90 Prozent der Fälle nicht im 110-kV-Netz von SH Netz, sondern in der
   noch nicht ausreichend vorhandenen Verfügbarkeit des Höchstspannungsnetzes". The 2022 and 2024
   plans repeat the statement without the percentage, so the direction is current and only the
   figure is dated.
8. The same 2017 paper records that over 90% of the state's renewable capacity is connected to SH
   Netz networks, about 34,000 installations and over 8 GW, which establishes that this operator's
   statement is about the great majority of the state's curtailment rather than a corner of it.
9. Per-county measure pages on the operator's site were attempted for seven counties. All returned
   404 with a 158 kB error page. The network-information page returned 403. These were abandoned;
   the plan PDFs carry the same material.

### B.4 The federal cross-check

10. The Bundesnetzagentur congestion page was fetched and found to carry nothing later than 2023,
    directing users to SMARD for current data. The Q4 2023 tables were downloaded as a spreadsheet
    and read with openpyxl.
11. Tabelle 4 gives the split that matters: redispatch with renewables, 1,657 GWh of measures at
    transmission level against 1,154.8 GWh at distribution level, while causation splits 2,193.1 GWh
    in the transmission network against 618.7 GWh in the distribution network. Tabelle 9 shows
    Schleswig-Holstein at 950.1 GWh of instructed reductions in that quarter, second only to Lower
    Saxony.
12. The SMARD 2025 article was fetched for the current national picture: 30.3 TWh of measures at
    EUR 3.07 bn, 9.38 TWh of renewable curtailment, 3.5% of renewable generation curtailed, and a
    shift of causation toward distribution networks, about 35% in 2025 against 26% in 2024.
13. This established an important contrast rather than a confirmation. Nationally, congestion
    causation is moving into the distribution networks. Schleswig-Holstein is the opposite case, the
    state where transmission causation dominates most heavily. The national trend does not transfer.

### B.5 The decisive independent check

14. § 13k Abs. 8 EnWG was read in the statute text already on disk. It permits distribution
    operators with 110 kV networks and more than 100,000 customers to run their own instrument from
    1 April 2025, conditional on curtailment **caused in their own network** reaching a threshold
    over the previous two calendar years.
15. The transmission operators' implementation concept was searched for their treatment of it and
    yielded a recorded outcome: the coordination with the distribution operators at the end of 2025
    found that the distribution operators "absehbar keinen eigenständigen Anwendungsfall" for their
    own relief regions under § 13k Abs. 8.
16. This was taken as the strongest single piece of evidence in the pass, because it is not a
    statement about causation at all but a revealed decision by the parties who would profit. Given
    a statutory route to monetise their own congestion, the distribution operators declined it. That
    agrees with the roughly 3% residual computed from the other sources.

### B.6 The inversion

17. At this point the original framing was re-examined. The first gap map had treated transmission
    causation as a threat, writing that a pool near a wind farm "may have no claim whatever" on that
    energy.
18. The two questions were separated explicitly. Where a constraint is caused is a question about
    the network. Where a load must sit to relieve it is a question about power flow, and the answer
    is that a load consuming north of a bottleneck relieves that bottleneck whatever voltage level
    it hangs off. The instrument is built on exactly this: relief regions exist so that additional
    switchable loads, mostly distribution-connected, can absorb transmission-caused curtailment, and
    the concept's stated reason for including the Hamburg belt is that loads there reduce redispatch
    caused by bottlenecks south of Hamburg.
19. The federal numbers corroborate the mechanism at scale: distribution-connected assets already
    carry 41% of renewable redispatch measures against 22% distribution-caused congestion.
20. The conclusion therefore inverted. Transmission causation is the addressable market, not the
    obstacle, and R2's finding sharpens: relief-region membership is not a proxy for the right
    variable, it is the right variable. Logged as C17.

### B.7 The spatial component, built twice

21. The Netzausbauplan 2024 was searched for congestion structure and yielded Tabelle 6: twelve
    medium-voltage congestion regions for the 2045 scenario, each with the share of its line
    elements projected to be overloaded, and each named by county and Netzcenter.
22. A first join geocoded the fifteen Netzcenter towns and measured each pool's distance to the
    nearest one, reporting 22 of 76 indoor units within 10 km and 40 within 15 km.
23. That approach was then rejected on inspection. The congestion regions are county-shaped, so
    distance to the centre town adds nothing beyond county membership while implying a spatial
    precision the source does not carry. The script was rewritten to join by county and to report
    the projected overload share per county. The distance figures were discarded. Logged as C18.
24. The rewritten join produced the finding that matters: the counties with the worst projected
    2045 distribution congestion are not those with today's transmission-caused curtailment.
    Ostholstein tops the list at 72% with seven indoor pools, and it, Herzogtum Lauenburg (55%) and
    Plön (29%) are outside the § 13k relief regions entirely.
25. Flensburg, Kiel and Lübeck do not appear in the operator's plan at all, because they are served
    by other distribution operators. The OpenStreetMap substation pull corroborated this through
    operator tags: SH Netz 106 substations at 110 kV and above, TraveNetz 18 in the Lübeck area,
    TenneT 12.

### B.8 A robustness fix

26. On a final verification run the script failed when invoked from outside its own folder, because
    every script in the set used paths relative to the working directory. All five were patched to
    resolve paths against their own location and re-run from the parent directory. This is not a
    finding but it matters for reproducibility, since the documents tell a reader to run them.

### B.9 How the conclusion was derived

Three independent parties are on record about the same quantity: the network operator that performs
the curtailment, the ministry that reports it, and the distribution operators collectively, who
declined a statutory instrument that would only pay if the quantity were material. They agree, and
they agree with the federal causation split for the country as a whole once the state's atypical
position is accounted for. The composite arithmetic is then simple and its weakness is disclosed:
it mixes a volume share from 2026 with a case share from 2017, and both are lower bounds on
transmission causation, so the distribution residual is an upper bound rather than a point
estimate. The inversion was not a new source but a re-reading of what the existing ones imply, and
it was checked against the instrument's own stated design rationale rather than asserted.

### B.10 Final conclusion

Essentially all of Schleswig-Holstein's curtailment is transmission-caused: at least 65% ordered by
the transmission operator, and over 90% of the network operator's own remaining cases caused by
extra-high-voltage unavailability rather than its own network, leaving on the order of 3% genuinely
distribution-caused. That residual has no instrument, because the distribution operators have
formally declined to create one. This is favourable rather than fatal for the project, because the
transmission-caused portion is precisely what § 13k makes available to distribution-connected
switchable loads inside a relief region. The addressable quantity is therefore the large majority of
802 GWh rather than a fraction of it, and the variable that decides access is regulatory
designation, not geography. A second and separate value proposition exists on the 2045 horizon in
the twelve projected medium-voltage congestion regions, strongest in three counties that cannot
participate in § 13k today, and it runs through flexible connection agreements rather than through
the tender.

**Status of the conclusion.** VERIFIED as to every underlying statement and as to the inversion,
which follows from the instrument's own design. ESTIMATE as to the roughly 3% residual, labelled
indicative with its two vintages disclosed. UNRESOLVED as to feeder-level assignment for any
individual facility.

### B.11 What would change it

A current quantification from SH Netz of curtailment caused in its own network, replacing the 2017
figure; the load-versus-generation trigger split for the twelve congestion regions, which decides
whether an added load in each region helps or worsens the projection; a change of position by the
distribution operators on § 13k Abs. 8, which would create an instrument for the residual; and
feeder-level data, which alone can move the question from county scale to facility scale.
