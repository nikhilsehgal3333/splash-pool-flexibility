# R4: The evaporation loop. What it costs to store heat in pool water

**A first-order steady-state model of the coupled water, humidity and electricity system, built on
the German design standard's own evaporation coefficients and a manufacturer's datasheet, and
calibrated against two independent anchors.** Reproducible from `r4_evaporation_loop.py`; sources
in `.drafts/evidence/`. Status labels per `README.md`.

---

## 1. The question

SPLASH treats pool water as thermal storage: raise the temperature when surplus electricity is
available, coast afterwards. The independent scan raised a blind spot: evaporation rises with water
temperature, so charging the store makes it leak faster, and the extra vapour has to be removed by
plant that runs on electricity. The "battery" charges its own discharge, and part of the leak comes
back as electricity in the same building.

Nobody had put numbers on it. The nearest published work, Benakcha et al. (2025, INSA Toulouse),
models a semi-Olympic pool with Shah's evaporation correlation, finds evaporation to be two-thirds
of water heat loss, tests deliberate overheating as a way to store solar heat, and then writes:
*"further investigations are required to confirm whether the repercussions of overheating on the
air circuit can be managed for a low energy cost. This falls within the perspectives of this work
and the future scope of a second article."* **VERIFIED** by local extraction. So the loop is open in
the literature by the nearest authors' own statement. This document is a first closure.

## 2. Model

**Reference pool.** One 25 m by 12.5 m sports pool, 312.5 m² of water, mean depth 1.8 m, 562.5 m³,
thermal capacity **654 kWh per kelvin**. Water at 28 °C; hall air at water plus 2 K with absolute
humidity capped at 14.3 g/kg, the VDI 2089 comfort limit (the DGfdB worked example uses 30 °C at
52%, equivalent). Results scale linearly with pool area and volume.

**Evaporation.** The Dalton form used by VDI 2089 and reproduced by the DGfdB:
`W = ε · A · (p_sat(T_water) − p_hall)` with ε = 5 g/(hPa·m²·h) at rest and 20 in bathing
operation. **VERIFIED** (DGfdB note, local extraction). Cross-checked against Shah's correlation
(ASHRAE 2014, SE-14-001): natural-convection term with C = 35 SI plus a forced-convection floor
with b = 0.00005, and the occupied-pool multiplier `1.9 − 21·Δρ + 5.3·N*`. **VERIFIED** (local
extraction). Saturation pressure by the Magnus formula, which reproduces the DGfdB example
(27 °C → 35.6 hPa) exactly.

**Losses from the extra evaporation.** Latent heat at 2,440 kJ/kg, plus heating of makeup water
from 10 °C to replace what evaporated.

**Removing the extra vapour.** Two technologies, bracketing real plant:

- *Fresh-air dilution (winter).* Cold outdoor air is dry, so dehumidification is by ventilation.
  Electricity is fan power only, at a specific fan power of 2.0 kW per m³/s **[verify]** (AIVC and
  CIBSE quote 2 to 2.5 for modern units). The cost is thermal: heating the extra outdoor air, net of
  70% heat recovery.
- *Heat-pump condensing.* Menerga ThermoCond 19, largest size: 22.6 kg/h at VDI 2089 conditions
  for 2.66 kW total electrical input, which is **0.12 kWh per kg**; 12.0 kg/h in pure recirculation
  mode with 2.9 kW compressor plus about 1.7 kW of fans, about **0.38 kWh per kg**. **VERIFIED**
  from the datasheet; the mode attribution of fan power is **[verify]**. The unit also offers a
  pool-water condenser, so the latent heat it captures can be pumped back into the pool. Modelled
  as 80% latent recovery when fitted.

**Charging.** Heat pump at seasonal performance 3.5, the same central value as R1, so that stored
heat converts to electricity shifted.

## 3. Calibration before results

Baseline at 28 °C with 10 h of bathing and 14 h of rest per day:

| Quantity | Model | Independent anchor |
|---|---|---|
| Evaporation | 460 t/yr | DGfdB example at 27 °C: 262 g/m²h in operation, 66 at rest; model gives 299 and 75 at 28 °C, consistent |
| Latent heat loss | 312 MWh_th/yr | Benakcha et al.: evaporation is about two-thirds of water heat loss; UBA 2024 mean facility heat 1.21 GWh/yr **VERIFIED**; 312 MWh as two-thirds of water loss inside a 1.21 GWh facility is plausible |
| Dehumidification electricity | 55 to 175 MWh_el/yr across the 0.12 to 0.38 kWh/kg band | Bekanntmachung 2021, category 32 Schwimmhallen, Be- und Entfeuchtung 30.0 kWh/m²a **VERIFIED**; at roughly 3,000 m² net floor area that is about 90 MWh/yr, inside the band |

The model is right to within a factor of about 1.5 on two independent anchors. Good enough for
first order, and stated as such.

## 4. Results

### 4.1 Evaporation is steep in water temperature

| Water °C | VDI, rest (kg/h) | VDI, operation (kg/h) | Change vs 28 °C |
|---|---|---|---|
| 26 | 16.8 | 67.3 | −28% |
| 28 | 23.3 | 93.4 | 0 |
| 30 | 30.6 | 122.3 | **+31%** |
| 32 | 38.6 | 154.2 | +65% |

A 2 K charge raises evaporation by about 31%. Shah's correlation, with its buoyancy term, gives a
steeper slope. Both agree the effect is large and monotonic. This also confirms the widely quoted
efficiency result from the other direction: a 2 K *reduction* cuts evaporation by 28%.

### 4.2 The penalty depends on when the charge is held, far more than on how deep it is

For a +2 K charge, 1,308 kWh of heat stored, 374 kWh of electricity shifted:

| Case | Extra evaporation | Thermal loss over the hold | Electricity to remove the vapour | Penalty as share of electricity shifted |
|---|---|---|---|---|
| Overnight, 6 h at rest, winter, fresh-air dilution | 7.2 kg/h | 41 kWh (3.1% of stored) | 1.9 kWh | **0.5%** |
| Overnight, 6 h at rest, heat-pump dehumidification at 0.38 kWh/kg | 7.2 kg/h | 30 kWh (2.3%) | 16.5 kWh | **4.4%** |
| Held through 12 h of bathing, winter, fresh-air dilution | 28.9 kg/h | 326 kWh (25%) | 14.9 kWh | **4.0%** |
| Held through 12 h of bathing, heat-pump dehumidification at 0.12 kWh/kg | 28.9 kg/h | 243 kWh (19%) | 41.6 kWh | **11%** |
| Held through 12 h of bathing, summer, recirculation heat pump at 0.38 kWh/kg | 28.9 kg/h | 243 kWh (19%) | 131.8 kWh | **35%** |
| Same, with pool-water condenser returning 80% of latent heat | 28.9 kg/h | 55 kWh (4%) | 131.8 kWh | **35%** |

Three things the table says.

**The loop is a small tax on an overnight charge.** At rest the pool loses 2 to 3% of the stored
heat over six hours and spends 0.5 to 4.4% of the shifted electricity removing the vapour. Charge
at night, use before opening, and the physics barely notices.

**The loop is a large tax on a charge held through bathing hours.** With the surface disturbed,
evaporation is four times higher. Held for twelve hours, the store loses a fifth to a quarter of its
heat, and in summer, when outdoor air is too humid to dilute with and the plant runs in
recirculation, removing the vapour costs **a third of the electricity that was shifted in the first
place**. The battery leaks, and the leak runs the compressor.

**A pool-water condenser fixes the thermal leak and not the electrical one.** Returning the latent
heat to the pool cuts the thermal loss from 19% to 4%, but the compressor still has to run to
condense it. The heat comes back; the electricity does not.

**The penalty fraction is almost independent of charge depth.** Across 0.5 to 2 K the share of
shifted electricity consumed by dehumidification moves by a few tenths of a point. In this regime
the cost of the loop is set by operating mode, hold duration and season, not by how hard the
store is charged. That is useful: it means the envelope question (R4 in the gap map, how far the
water may deviate) and the loop question separate cleanly. The envelope sets how much can be
stored; the loop sets when it is cheap to hold.

### 4.3 The seasonal alignment nobody had noticed

The loop is cheapest in winter, when outdoor air is dry and dehumidification is by ventilation at
fan cost only, and most expensive in summer, when the plant must condense. Schleswig-Holstein's
curtailment is a wind phenomenon and wind is a winter resource. So the season in which pool
flexibility is physically cheapest is the season in which the curtailed energy it would absorb
exists. That alignment is not designed; it falls out of the psychrometrics. It is also the reverse of
what a solar-driven pool strategy faces, which may be part of why the Toulouse group, working with
solar heat in a Mediterranean climate, flagged the air-circuit cost as a worry.

## 5. What this establishes, and what it does not

**Established, to first order.** The evaporation loop does not kill pool-as-storage; it constrains
its operating regime. Overnight charging is cheap. Day-long buffering is expensive in summer and
moderately expensive in winter, and the expensive part is electrical, which is the currency the
flexibility is measured in. The nearest published work names this exact loop as unanalysed. These
numbers, with their labelled inputs, are the first closure of it.

**Not established, and the content of a paper on this.**

1. **Dynamics.** The model is steady state. How fast the water actually rises and falls, how long
   the hall air takes to follow, and whether stratification limits the usable volume are all
   unmodelled. The scan's practitioner lens noted a claimed multi-hour response for a case pool at
   Eckernförde **[verify]**; that is the kind of data this needs.
2. **Envelope transmission.** Raising water temperature raises hall air temperature under VDI
   practice, which raises transmission and ventilation sensible losses. Not modelled; it makes the
   penalty somewhat worse.
3. **Occupancy.** N* = 0.10 occupants per m² is an assumption. Shah's multiplier is linear in it.
4. **The plant.** Real dehumidification units run in mixed modes that shift with outdoor
   conditions. The 0.12 to 0.38 band brackets that; a specific unit's control logic decides where in
   the band a given hour sits.
5. **Hygiene and comfort bounds.** This model assumes the +2 K is permitted. Whether it is, and for
   whom (infants, therapy users, school swimming), is the service-quality question in the gap map
   and is untouched here.

## 6. What this means for the project

The Technical Assessment package as advertised is an inventory of heating demand, storage
capacity and technologies. This result says the storage capacity number it produces is not the
number that matters. What matters is **storage capacity conditioned on hold window and season**,
which is a small table per pool rather than a single figure, and it is what the energy system model
needs if it is to represent pools honestly rather than as ideal thermal batteries. An energy-system
model that treats pool storage as lossless will overstate summer daytime flexibility by roughly a
third in electrical terms. That is the modelling correction this package should deliver.

It also gives the roadmap a concrete design recommendation that costs nothing: **pool flexibility
should be dispatched as an overnight product.**

---

## Sources

1. Deutsche Gesellschaft für das Badewesen, "Minderung der Abwassermengen durch Verdunstung in
   Hallen- und Freibädern", calculation note reproducing the VDI 2089 evaporation coefficients.
   https://www.dgfdb.de/fileadmin/user_upload/Verdunstungsmengen_in_Baedern_Berechnung.pdf
   Local: `.drafts/evidence/dgfdb_verdunstungsmengen_vdi2089.pdf` and text extraction.
2. Shah, M. M. (2014). Methods for Calculation of Evaporation from Swimming Pools and Other Water
   Surfaces. ASHRAE Transactions 120(2), SE-14-001.
   https://www.mmshah.org/publications/ASHRAE%202014%20Evaporation%20paper.pdf
   Local: `.drafts/evidence/shah2014_ashrae_evaporation_methods.pdf` and text extraction.
3. Benakcha, Y., Labat, M., Hazyuk, I., Ginestet, S. (2025). Numerical Analysis of the Impact of
   Water Temperature Setpoint and Energy Strategies on Indoor Pool Performance. arXiv:2512.02586.
   https://arxiv.org/abs/2512.02586
   Local: `.drafts/evidence/benakcha2025_arxiv2512.02586_pool_setpoint.pdf` and text extraction.
   Note: numerical results in the extraction are illegible (equations rendered as glyphs); the
   qualitative statements quoted are verbatim and the numbers are UNRESOLVED pending a visual read.
4. Menerga, ThermoCond 19/29 datasheet (2016).
   https://www.menerga-adria.com/wp-content/uploads/sites/2/2016/07/ThermoCond-19_29_2016_de.pdf
   Local: `.drafts/evidence/menerga_thermocond19_datasheet_2016.pdf` and text extraction.
5. Bekanntmachung der Regeln für Energieverbrauchswerte und der Vergleichswerte im
   Nichtwohngebäudebestand, BAnz AT 03.05.2021 B1, category 32.
   Local: `.drafts/evidence/bekanntmachung_energieverbrauchswerte_2021_pdftotext-layout.txt`
6. Weinfurter, Thieme, Wallrodt (2024), UBA TEXTE 139/2024. Local copy as in R1.
7. Specific fan power, **[verify]**: AIVC Technical Note 65,
   https://www.aivc.org/sites/default/files/members_area/medias/pdf/Technotes/TN65_Specific%20Fan%20Power.pdf ;
   CIBSE Journal CPD module 181, https://www.cibsejournal.com/cpd/modules/2021-06-swe/
8. EnergyPlus Engineering Reference 24.2, Indoor Swimming Pool (model structure only).
   https://bigladdersoftware.com/epx/docs/24-2/engineering-reference/indoor-swimming-pool.html
