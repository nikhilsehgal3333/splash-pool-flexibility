# Process record R4: The evaporation loop

Neutral record of how the question was worked, how the conclusion was derived, and what the
conclusion is. Part A is a one-page summary. Part B is the full trail including dead ends and
corrections. Result document: `../r4-evaporation-loop.md`. Worked 2026-09-11.

---

## Part A. One-page method summary

**Question.** Raising pool water temperature stores heat but increases evaporation, which both
accelerates the leak and raises the electrical load of dehumidification. What does the loop cost,
and does it decide whether pool-as-storage works?

**Sources.** VDI 2089 evaporation coefficients as reproduced in the Deutsche Gesellschaft für das
Badewesen calculation note; Shah (2014), ASHRAE Transactions 120(2), SE-14-001, for the
independent correlation; Benakcha, Labat, Hazyuk and Ginestet (2025), arXiv:2512.02586, the
nearest prior work; Menerga ThermoCond 19/29 datasheet (2016) for dehumidification specific
energy; Bekanntmachung Energieverbrauchswerte (2021) category 32 and UBA TEXTE 139/2024 as
calibration anchors; AIVC and CIBSE for specific fan power.

**Method.** A first-order steady-state model of one 25 m pool (312.5 m² water, 562.5 m³,
654 kWh/K). Evaporation by the Dalton form used in VDI 2089, cross-checked against Shah.
Additional losses from a charge: latent heat of the extra evaporation plus makeup-water heating.
Vapour removal in two bracketing modes: winter fresh-air dilution (electricity is fan power, cost
is thermal) and heat-pump condensing at datasheet specific energies (0.12 to 0.38 kWh/kg), with
and without a pool-water condenser. Charging at seasonal performance 3.5 to convert stored heat
into electricity shifted. The baseline was calibrated against two independent anchors before any
result was read.

**Result.** Evaporation rises about 31% for a 2 K charge. For a +2 K charge (1,308 kWh stored,
374 kWh electricity shifted): overnight at rest, thermal loss 2 to 3% and electricity 0.5 to 4.4%
of what was shifted; held through 12 bathing hours, thermal loss 19 to 25% and, in summer
recirculation, electricity about 35% of what was shifted. A pool-water condenser cuts the thermal
loss from 19% to 4% and does not change the electrical penalty. The penalty fraction is almost
independent of charge depth.

**Status.** VDI coefficients, Shah constants, datasheet figures and the prior work's own statement
that the air-circuit consequence is unanalysed are VERIFIED by local extraction. The humidity cap,
specific fan power, fan-power attribution, heat-recovery efficiency, occupancy density and pool
geometry are `[verify]` or stated assumptions. The prior work's numerical results are UNRESOLVED
(equations illegible in extraction).

**Limits.** Steady state; no dynamics, stratification or envelope transmission; the +2 K charge
assumption was later bounded by R5's finding on the KOK design bands.

**Files.** `r4_evaporation_loop.py`; evidence: four source PDFs and their extractions;
`verification_log.md` fourth pass; correction C6 and a status upgrade on the scan's blind spot B.

---

## Part B. Full trail

### B.1 Origin

1. The independent scan named as its second blind spot that no pool-flexibility model closes the
   coupled water, humidity and electricity loop, carrying it at `[verify]` with the note that the
   nearest paper might already model the HVAC side. It was selected as the second question to work
   because the physics is standard, the coefficients are published, and one real anchor already
   existed: the official benchmark for Schwimmhallen lists dehumidification at 30 kWh/m²a, the
   second-largest electrical item.

### B.2 Sourcing the evaporation model

2. Four pulls in parallel: VDI 2089 coefficients; the Shah correlation; pool dehumidifier specific
   energy; and the share of pool heat loss attributable to evaporation.
3. The DGfdB calculation note was downloaded and extracted. It gives the Dalton form
   W = ε · A · (Ps − Pd) in g/h and the VDI 2089 coefficients: 5 g/(hPa·m²·h) at rest, 15
   residential, 15 to 20 hotel, 20 indoor pool in operation, 28 leisure pool, 35 wave pool. Its
   worked example (water 27 °C giving 35.6 hPa, air 30 °C at 52% giving 22.48 hPa, the
   "Schwülegrenze") yields 262.4 g/m²h in operation and 66.0 at rest. The note itself warns the
   formula is for plant sizing and actual losses may deviate.
4. Shah (2014) was downloaded and extracted for an independent cross-check. Equations 1 and 2 give
   the unoccupied rate as the larger of a natural-convection term with C = 35 in SI and a
   forced-convection term with b = 0.00005 (pressures in Pa); equation 5 gives the occupied
   multiplier 1.9 − 21·Δρ + 5.3·N*. Shah reports the ASHRAE handbook method (Carrier equation with
   activity factors) as inaccurate against test data.
5. Two HTML fetches failed and were abandoned: a trade article on VDI 2089 dehumidification hit a
   redirect loop, and a dehumidifier article was paywalled. Their target figure, a 0.71 kWh/kg
   specific heat requirement, was not needed, because latent heat is a physical constant.
6. The EnergyPlus engineering reference was fetched for model structure only, confirming the same
   decomposition (evaporation, convection, radiation, conduction, makeup water) without supplying
   constants.

### B.3 The nearest prior work

7. A search on pool flexibility surfaced arXiv:2512.02586, a 2025 numerical study of water
   temperature setpoint strategies for an indoor pool. Downloaded and extracted.
8. It uses Shah for evaporation, finds evaporation to be about two thirds of water heat loss, and
   tests deliberate overheating as a way to store solar heat. Its numerical results are illegible
   in extraction (equations rendered as glyphs) and were marked UNRESOLVED.
9. Two verbatim statements were recovered and are decisive for the status of the gap. The authors
   discarded unoccupied measurements because the air-handling unit's energy-recovery strategy
   complicated them, considering that the impact on the water balance "could be neglected as a
   first approximation". And: "further investigations are required to confirm whether the
   repercussions of overheating on the air circuit can be managed for a low energy cost. This
   falls within the perspectives of this work and the future scope of a second article."
10. The scan's blind spot B was upgraded from `[verify]` to VERIFIED as an open question in the
    nearest prior work. The broader absence claim across the whole literature remained UNRESOLVED,
    since no systematic search protocol was run.

### B.4 Dehumidification energy

11. A search for German pool ventilation equipment found the Menerga ThermoCond 19/29 datasheet.
    Downloaded and extracted. Five sizes: dehumidification capacity per VDI 2089 of 7.1, 9.7,
    12.9, 16.2 and 22.6 kg/h with total electrical input 0.94 to 2.66 kW; recirculation-mode
    capacity 4.6 to 12.0 kg/h; compressor input 1.3 to 2.9 kW; fan units 0.60 to 1.70 kW; heat-pump
    coefficient of performance 5.14 to 6.61; an optional pool-water condenser rated 6.4 to 15.5 kW.
12. Two specific energies were derived: 22.6 kg/h for 2.66 kW gives 0.118 kWh/kg at the VDI design
    point; 12.0 kg/h in recirculation with compressor plus fans gives about 0.38 kWh/kg. The
    attribution of fan power to recirculation mode was labelled `[verify]`. A mid value of
    0.25 kWh/kg was added to give a band.
13. Specific fan power for the fresh-air mode was taken as 2.0 kW per m³/s from AIVC and CIBSE
    ranges of 2 to 2.5, labelled `[verify]`.

### B.5 Model construction

14. `r4_evaporation_loop.py` was written. Reference pool 25 m by 12.5 m, mean depth 1.8 m, giving
    654 kWh/K; water 28 °C; hall air water plus 2 K; hall absolute humidity capped at 14.3 g/kg
    (the commonly cited VDI comfort limit, `[verify]`), which yields a partial pressure of about
    22.8 hPa, close to the DGfdB example's 22.48.
15. Saturation pressure by the Magnus formula. A check was built into the output: p_sat(27 °C)
    computes to 35.6 hPa, reproducing the DGfdB example exactly.
16. For a charge of ΔT held for h hours: extra evaporation from the VDI form at the two
    coefficients; latent loss at 2,440 kJ/kg; makeup water heated from 10 °C. In heat-pump mode
    electricity is the extra evaporation times the specific energy, with optional 80% latent
    recovery through a pool-water condenser. In fresh-air mode the dilution air mass is computed
    from the humidity difference against winter outdoor air (0 °C, 80% relative humidity),
    electricity is fan power at the specific fan power, and the thermal cost is heating that air
    net of 70% recovery.
17. Charging converts stored heat to electricity shifted at seasonal performance 3.5, the same
    central value as R1, so the two questions use one consistent assumption.

### B.6 Calibration before results

18. The baseline was run first and compared with independent anchors. At 28 °C with 10 operating
    and 14 rest hours a day: 460 t/yr evaporation, 312 MWh/yr latent, 10 MWh/yr makeup, and 55 to
    175 MWh/yr of dehumidification electricity across the specific-energy band.
19. Anchor one: the Bekanntmachung's 30.0 kWh/m²a for dehumidification in category 32, at roughly
    3,000 m² net floor area, gives about 90 MWh/yr, inside the band. Anchor two: the UBA 2024 mean
    facility heat of 1.21 GWh/yr, with the prior work's finding that evaporation is about two
    thirds of water heat loss, is consistent with 312 MWh of latent loss. The model was judged
    right to within a factor of about 1.5 and the results were then read.

### B.7 Results and reading

20. Evaporation against water temperature: from 28 °C, a 2 K rise increases the operating-mode
    rate by 31% (93.4 to 122.3 kg/h) and a 2 K fall reduces it by 28%. Shah's correlation gives a
    steeper slope through its buoyancy term. Both agree on direction and magnitude class.
21. Charge cases for +2 K (1,308 kWh stored, 374 kWh shifted): overnight 6 h at rest, winter
    fresh-air, thermal loss 41 kWh (3.1%) and electricity 1.9 kWh (0.5% of shifted); overnight 6 h
    with heat-pump recirculation, 30 kWh (2.3%) and 16.5 kWh (4.4%); held 12 h through operation,
    winter fresh-air, 326 kWh (25%) and 14.9 kWh (4.0%); held 12 h, summer recirculation, 243 kWh
    (18.6%) and 131.8 kWh (35.3%); the same with a pool-water condenser, 55 kWh (4.2%) and
    131.8 kWh (35.3%).
22. Two structural observations were read off the grid. The penalty fraction varies by only a few
    tenths of a point across charge depths of 0.5 to 2 K, so the envelope question and the loop
    question separate cleanly. And the loop is cheapest in winter, when outdoor air is dry and
    dehumidification is by ventilation at fan cost only, which is the season in which
    Schleswig-Holstein's wind curtailment occurs.

### B.8 Correction logged

23. C6. The scan had framed the loop as something that "may decide whether the asset class is
    viable". The model shows it decides the operating regime, not viability: overnight charging is
    cheap, day-long holding in summer is expensive. Restated accordingly.

### B.9 Later bound from R5

24. R5 subsequently established that the KOK design band for sports and multipurpose basins is 24
    to 28 °C, so a sports pool at 28 °C has no upward headroom under guidance, while children's and
    teaching basins at 28 to 32 °C have two to four kelvin. R4's physics is unaffected; its
    applicability is pool-type specific. Logged as C14 in the seventh pass.

### B.10 How the conclusion was derived

The evaporation model is the one German practice uses for plant sizing, taken with its published
coefficients (step 3) and cross-checked against the most validated correlation in the literature
(step 4). The removal energy is taken from a real machine's datasheet at two operating modes
(step 12), which brackets rather than assumes. The whole model was calibrated against an official
benchmark and a national survey before any result was inspected (steps 18 to 19), so the numbers
are anchored rather than free-floating. The conclusion then follows from reading one grid: the
same charge costs a few percent overnight and a third of the shifted electricity when held through
summer bathing hours (step 21). The seasonal alignment (step 22) is an observation about when the
cheap regime coincides with the resource, not a modelled result.

### B.11 Final conclusion

The evaporation loop does not decide whether pool-as-storage works; it decides the regime in which
it works. Charging overnight at rest costs 2 to 3% of the stored heat and 0.5 to 4.4% of the
electricity shifted. Holding a charge through bathing hours costs a fifth to a quarter of the
stored heat, and in summer recirculation about a third of the electricity shifted, because the
store leaks harder the harder it is charged and the leak runs the compressor. A pool-water
condenser recovers the heat but not the electricity. The cost is set by mode, duration and season
rather than by charge depth, which separates the envelope question from the loop question. Pool
flexibility should therefore be dispatched as an overnight product, and an energy-system model
treating pool storage as lossless overstates summer daytime flexibility by roughly a third in
electrical terms. The nearest prior work states in its own text that this air-circuit consequence
is unanalysed and deferred, so the gap is real by the nearest authors' own account.

**Status of the conclusion.** VERIFIED as to coefficients, datasheet figures and the openness of
the gap. ESTIMATE as to the percentages, on a calibrated first-order steady-state model with
stated assumptions. Applicability bounded by pool type per R5.

### B.12 What would change it

A reading of the nearest prior work's numerical results (currently unresolved); a measured dynamic
response from a German indoor pool replacing the steady-state assumption; a dehumidification unit's
real annual control logic placing hours inside the 0.12 to 0.38 kWh/kg band; inclusion of envelope
transmission, which would make the penalty somewhat worse.
