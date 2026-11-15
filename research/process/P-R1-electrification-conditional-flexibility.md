# Process record R1: Electrification-conditional flexibility potential

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. Result document: `../r1-electrification-conditional-flexibility.md`. Worked
2026-09-11.

---

## Part A. One-page method summary

**Question.** German reference demand-response accounting scores swimming baths at zero flexible
electricity. Is that a property of the asset or an artefact of the method, and how large is the
quantity the method cannot see?

**Sources.** Wohlfarth, Klobasa and Eßer, *Energy Efficiency* 12 (2019) 327-341, Tables 3 and 4;
Schlomann et al. (2015), Fraunhofer ISI GHD energy survey 2006-2013, Kurzfassung, Tabellen 1-3;
Weinfurter, Thieme and Wallrodt (2024), UBA TEXTE 139/2024, municipal indoor pools, Tabellen 1
and 4; Bekanntmachung Energieverbrauchswerte Nichtwohngebäude (2021), category 32; trade sources
for heat-pump seasonal performance. All PDFs downloaded and text-extracted locally; the browser
route does not parse PDFs.

**Method.** The published potential-assessment method was kept unchanged and one input was
switched: the fuel. Table 3 of the reference paper lists heat pumps and electric water heating as
flexible appliances, so pool heat delivered by heat pumps falls inside the method's own flexible
categories. Pool heat was taken from the same survey that feeds the reference table (like for
like) and from a 2024 official extrapolation (modern cross-check), converted to electricity at
three seasonal performance factors, and re-read against the table.

**Result.** Baths move from 0.0 to between 0.30 and 0.97 TWh/a of theoretical flexible
electricity, central 0.83. In absolute terms that is level with Hospitals (0.8) and Construction
(0.9); in flexible fraction (37%) it exceeds every subsector in the table, because about 93% of a
bath's heat is process heat into water.

**Status.** Every quantity entering the calculation is VERIFIED by local extraction except the
performance-factor band (`[verify]`, trade sources) and the fuel-carrier split (`[verify]`, column
order). The Schlomann heat figure carries a confidence band wider than plus or minus 15% by the
authors' own statement; the UBA basis exists for that reason.

**Limits.** Theoretical potential, like the reference table itself; the technical fraction depends
on the storage envelope (R4). Full fuel switch is an upper bound; 50% and 25% cases are in the
script. No pool-specific measured seasonal performance factor was found.

**Files.** `r1_flexibility_calc.py` (reproduces every number); `.drafts/evidence/` holds the two
source PDFs and five text extractions; `verification_log.md` third pass; corrections C3, C4, C5.

---

## Part B. Full trail

### B.1 Origin of the question

1. The independent multi-perspective scan (`perspectives_splash.md`) reported as its strongest
   finding that the reference German demand-response accounting lists "Baths" at 1.4 TWh/a
   electricity with 0.0 TWh/a of flexible technologies, attributing the zero to the method
   counting electric cross-sectoral technologies while pool heat is thermal and gas-fired.
2. Before the finding was accepted, it was checked. Two browser-route attempts on the paper failed:
   the Fraunhofer ISI open-access PDF would not parse through the fetch tool, and the Springer
   landing page redirected to an authentication endpoint. The PDF saved by the failed fetch was
   located on disk and text-extracted with `pdftotext -layout`.
3. Table 4 was found and read directly. Row "Baths": lighting 0.2, mechanical power 1.1, all other
   end uses 0.0, total 1.4 TWh/a, sum of relevant shares 0.0. The finding was confirmed.
4. Two corrections arose from the same read. The scan had called Baths "the only zero in the
   table"; Laundries is also 0.0 (on 0.3 TWh/a). Logged as C3 with the restatement "the larger of
   only two zeros." The scan cited the paper as 2018 with author "Esser"; the PDF carries the
   2018 online-first notice and DOI, the journal issue is 2019, volume 12, pages 327-341, and the
   third author is Eßer. Logged as C4.
5. R1 was selected as the first question to work because it needs no proprietary data: the
   reference table was already on disk, and the two missing inputs (pool heat consumption and a
   heat-pump performance factor) are public.

### B.2 Establishing the method to be re-run

6. The reference paper's method section was extracted from the local text. Table 3 defines the
   flexible appliances: cold storage, retail and hotel cooling, ventilation, air conditioning,
   electric water heating, storage heaters, and heat pump or recirculation pump. The text defines
   the last column of Table 4, "sum of relevant shares", as "the sum of the consumption of the
   flexible appliances", indicating "the available theoretical flexibility potential", which
   "needs to be revised downwards, as not the whole consumption of an appliance is technically
   flexible."
7. Decision: because heat pumps and electric water heating are on the flexible list, an
   electrified pool's heat-pump consumption would enter the sum under the authors' own rules. The
   counterfactual was therefore defined as: keep the method, replace fossil pool heat with heat
   pumps, convert heat to electricity at a seasonal performance factor, re-read the table.
   Comparisons would be theoretical to theoretical, which is the like-for-like comparison.

### B.3 Finding the heat behind the electricity

8. Three searches were run in parallel: the Schlomann 2015 GHD survey (the data source named
   under Table 4); the official German non-residential energy benchmark rules for swimming halls;
   and heat-pump seasonal performance for pool water.
9. The Schlomann Kurzfassung PDF was located on the Fraunhofer ISI site, downloaded with `curl`
   and extracted with `pdftotext -layout`. A first search of the text for "Bäder" returned nothing.
   Cause: the extraction had rendered the umlaut as a replacement character. A looser pattern
   ("B.der") found the group "5/3 Bäder" in all three tables.
10. Tabelle 1 (energy by consumer group 2006-2013) was read with its header. Bäder row, 2013:
    electricity 1.4 TWh, fuels plus district heat 2.9 TWh, total 4.3 TWh. The 1.4 matched the
    reference table exactly, confirming the two are the same dataset. The series 2008 to 2013
    (7.2 to 4.3 TWh total) was noted as steep.
11. Tabelle 2 (by energy carrier) and Tabelle 3 (by application) were garbled in layout mode. A
    second extraction in reading order (`pdftotext -raw`) put each row on one line. Tabelle 2:
    gas 0.9, wood 0.3, district heat 1.6, fuels sum 2.8, electricity 1.4, total 4.2; reference
    unit 4,650 thousand m² of water surface. Column order was checked against the neighbouring
    hotels row, whose components summed correctly. Tabelle 3: electricity 14.3% lighting and 78.6%
    mechanical power, which reproduces the reference table's 0.2 and 1.1 of 1.4; fuels 7.1% in one
    column and 92.9% "sonstige Prozesswärme" in another.
12. The 7.1% column could not be assigned with certainty (hot water or space heating) from
    either extraction. An attempt to render the page as an image failed: `pdftoppm` is not
    installed. The 92.9% process-heat figure was carried as VERIFIED, the 7.1% assignment as
    `[verify]`. The result does not depend on it.
13. The Schlomann text was read for its own confidence statement: fuel and district-heat
    deviations are plus or minus 5% to just under 15% for the remaining groups "mit Ausnahme der
    Bäder". The Bäder fuel figure therefore carries a wider band. Combined with the steep series,
    this motivated a second, modern heat basis.
14. A search for national pool heat surfaced the Umweltbundesamt study TEXTE 139/2024 on the
    energy consumption of municipal indoor and combination pools. Downloaded and extracted.
    Tabelle 1 (n = 67 complete responses): mean heat 1.21 GWh, electricity 0.36 GWh, total
    1.57 GWh per pool; median 1.01 and 0.30. Tabelle 4 (extrapolation to n = 1,390 municipal
    indoor and combination pools in the Bäderleben database): heat 1,339.93 GWh by the model
    route and 1,636.22 GWh by the simple route; electricity 396.28 and 482.07 GWh. Carrier mix
    among respondents by count: 53.7% gas, 44.8% district heat. Pools were stated as 0.55 to
    0.65% of tertiary final energy and 0.08 to 0.09% of national final energy in 2022.
15. The two bases were reconciled by scope: Schlomann covers all baths including outdoor, leisure
    and non-municipal; UBA covers municipal indoor and combination pools only. A per-pool sanity
    check (UBA mean 1.21 GWh heat against roughly 0.5 GWh implied per bath by Schlomann over the
    national stock) is consistent with outdoor pools being seasonal and small.
16. The Bekanntmachung 2021 was downloaded and extracted for category 32 Schwimmhallen. Its
    partial values (heating 63.8, hot water 8.3, ventilation 13.4, lighting 1.9, cooling 1.1,
    dehumidification 30.0, other 7.3 kWh/m²a, plus a 90 kWh/m²a surcharge for pool-water heating
    when not separately metered) were not needed for R1 and were parked for R4, where the
    dehumidification value later served as a calibration anchor.

### B.4 The performance factor

17. Three searches for a measured seasonal performance factor of a German indoor-pool heat pump
    returned general installation ranges only: air-water 3.1 to 3.3, ground-coupled 4.0 to 4.6,
    groundwater and wastewater 4.5 to 5.0 and above; EN 17645 test conditions at 26 °C water. No
    pool-specific measured value was found. Pool water at 26 to 30 °C is a low sink temperature,
    favourable to performance. Three cases were fixed: 3.0 (conservative air-source), 3.5
    (central), 4.5 (ground or water source). Labelled `[verify]`.

### B.5 Calculation

18. A script was written (`r1_flexibility_calc.py`) with every input carrying its source and
    status. Inputs: Baths electricity 1.4 and flexible sum 0.0 (reference table); the full
    comparator table; heat 2.90 TWh (basis A, Schlomann 2013, all baths), 1.34 TWh (basis B, UBA
    model) and 1.64 TWh (basis C, UBA simple); performance factors 3.0, 3.5, 4.5; electrification
    shares 1.0, 0.5, 0.25.
19. For each combination, heat-pump electricity = heat × share ÷ factor; new sector electricity =
    1.4 + that; new flexible sum = 0.0 + that (theoretical, per the method).
20. Output at full switch: basis A 0.97 / 0.83 / 0.64 TWh/a; basis B 0.45 / 0.38 / 0.30; basis C
    0.55 / 0.47 / 0.36. Central case 0.83 TWh/a, flexible fraction 37%; most conservative corner
    0.30 TWh/a, fraction 18%. Placed in the reference table, the central case sits between
    Construction (0.9) and Hospitals (0.8); the conservative corner matches Schools and Airports
    (0.3); in flexible fraction the central case exceeds Retail (30%), the highest published.
21. The script was re-run from the programme folder to confirm the headline reproduces.

### B.6 Corrections logged in this pass

22. C5: the "heat is roughly four times electricity" figure carried from trade press was found
    not to hold at sector level. UBA respondents give a ratio of about 3.4 per indoor pool (the
    authors' own text says "knapp über ein Vierfaches", which their means do not quite support);
    the Schlomann sector ratio is about 2.1, because outdoor pools are electricity-heavier.
    Restated as "three to four for indoor pools, about two at sector level."

### B.7 How the conclusion was derived

The chain of inference is short and each link is documented. The reference method's own
definition of flexible appliances includes heat pumps (step 6). The same survey that feeds the
reference table reports baths' heat separately from their electricity (step 10), and states that
almost all of it is process heat (step 11). Converting that heat to heat-pump electricity at
public performance factors (step 17) and placing it in the reference table under the reference
rules (steps 18 to 20) yields a non-zero flexible sum of the same order as sectors the method
already scores as significant. Because the only thing changed was the fuel, the zero is shown to be
a property of the method, not the asset. The second heat basis (step 14) guards against the
acknowledged weakness of the first (step 13); both give the same qualitative answer.

### B.8 Final conclusion

The reference method is blind to flexibility that exists only after a fuel switch. For German
swimming baths the hidden quantity is 0.30 to 0.97 TWh/a of theoretical flexible electricity
(central 0.83), comparable to the entire published potential of hospitals, with a flexible fraction
above every listed subsector. Both zeros in the reference table (Baths, Laundries) are
heat-and-water sectors, consistent with the blindness being to thermal flexibility under fossil
supply rather than to baths in particular. The method under-counts every gas-heated building class
in proportion to its heat demand; how much of the under-count is usable is asset-specific, and for
pools it depends on the comfort and hygiene envelope (R4, and later R5's finding on the KOK
design bands).

**Status of the conclusion.** VERIFIED as to the artefact and its order of magnitude. Estimate as
to the exact figure (band stated). Not established: the technical revision, the electrification
trajectory, stock heterogeneity, a measured performance factor, the interaction with existing CHP.

### B.9 What would change it

A later GHD survey wave superseding Schlomann 2015 in which baths are no longer scored zero; a
measured pool heat-pump seasonal performance factor outside 3.0 to 4.5; a technical-fraction study
showing pool storage envelopes are narrow enough to remove most of the theoretical potential.
