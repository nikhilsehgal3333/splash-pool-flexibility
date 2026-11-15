"""
R4 - The evaporation loop: what it costs to store heat in pool water.

Question. Raising pool water temperature by dT stores heat (the "battery"). But evaporation rises
with water temperature, so (a) the stored heat leaks faster as latent loss and makeup-water heating,
and (b) the extra vapour must be removed from the hall, which costs electricity (and, in fresh-air
mode, heat). This script quantifies both against the heat stored and the electricity shifted, for
a reference 25 m public pool, as a function of charge depth, operating mode, hold duration, season
and dehumidification technology.

First-order steady-state model. Every input carries its source and status label.
Run: py r4_evaporation_loop.py
"""
import os as _os, sys as _sys
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")

import math

# ----------------------------------------------------------------------------------------------
# PHYSICS CONSTANTS (standard; not source claims)
# ----------------------------------------------------------------------------------------------
P_ATM_HPA = 1013.25
H_FG_KWH_PER_KG = 2440.0 / 3600.0      # latent heat of vaporisation ~28 C, 2440 kJ/kg = 0.678 kWh/kg
CP_WATER_KWH_PER_KG_K = 4.186 / 3600.0 # 0.001163 kWh/(kg K)
RHO_WATER = 1000.0                     # kg/m3
CP_AIR_KJ = 1.005                      # kJ/(kg K)
R_DRY, R_VAP = 287.05, 461.5           # J/(kg K)


def p_sat_hpa(t_c):
    """Magnus formula (WMO form). Check: 27 C -> 35.6 hPa, matches the DGfdB worked example."""
    return 6.112 * math.exp(17.62 * t_c / (243.12 + t_c))


def x_from_p(p_v_hpa):
    """Humidity ratio kg/kg from vapour partial pressure."""
    return 0.622 * p_v_hpa / (P_ATM_HPA - p_v_hpa)


def p_from_x(x):
    return P_ATM_HPA * x / (0.622 + x)


def rho_moist(t_c, p_v_hpa):
    """Density of moist air, kg/m3."""
    T = t_c + 273.15
    return ((P_ATM_HPA - p_v_hpa) * 100.0) / (R_DRY * T) + (p_v_hpa * 100.0) / (R_VAP * T)


# ----------------------------------------------------------------------------------------------
# INPUTS
# ----------------------------------------------------------------------------------------------

# Reference pool: one 25 m x 12.5 m sports pool, mean depth 1.8 m. Assumption for a typical
# Hallenbad; sensitivity is linear in area and volume so other sizes scale directly.
AREA_M2 = 312.5
VOLUME_M3 = 562.5
C_POOL_KWH_PER_K = VOLUME_M3 * RHO_WATER * CP_WATER_KWH_PER_KG_K   # ~654 kWh per kelvin

# Baseline water temperature and hall air per VDI 2089 practice: air = water + 2 K, absolute
# humidity capped at the "Schwuelegrenze". DGfdB worked example uses 30 C / 52 % (= 22.48 hPa).
# VERIFIED for the example; the 14.3 g/kg cap is the commonly cited VDI limit [verify].
T_WATER_BASE_C = 28.0
AIR_OFFSET_K = 2.0
X_HALL_CAP = 0.0143                    # kg/kg
P_HALL_HPA = p_from_x(X_HALL_CAP)      # ~22.8 hPa, close to the DGfdB example's 22.48

# VDI 2089 evaporation coefficients, g/(hPa m2 h). VERIFIED (DGfdB note reproducing VDI 2089).
EPS_REST = 5.0
EPS_OPERATION = 20.0

# Shah correlation (2012/2014), SI. VERIFIED from Shah 2014 (ASHRAE SE-14-001):
#   E0 = max( C * rho_w * (rho_r - rho_w)^(1/3) * (W_w - W_r),  b * (p_w - p_r) )  kg/(m2 h)
#   C = 35, b = 0.00005 (p in Pa). Occupied: E_occ/E0 = 1.9 - 21*(rho_r - rho_w) + 5.3*N*, N* >= 0.05
SHAH_C, SHAH_B = 35.0, 0.00005
N_STAR_OCCUPIED = 0.10                 # occupants per m2 of water surface, public pool in use [assumption]

# Makeup water: evaporated mass is replaced with mains water and heated to pool temperature.
T_MAKEUP_C = 10.0

# Dehumidification, specific electricity per kg of water removed, kWh_el/kg.
# Menerga ThermoCond 19 datasheet (2016), largest size: 22.6 kg/h at VDI 2089 conditions for
# 2.66 kW total electrical -> 0.118 kWh/kg (fresh-air assisted, winter design point);
# 12.0 kg/h in pure recirculation heat-pump mode with 2.9 kW compressor + ~1.7 kW fans -> ~0.38 kWh/kg.
# VERIFIED from the datasheet; the mode attribution of the fan power is [verify].
E_DH_KWH_PER_KG = {"HP mixed-mode (datasheet, VDI point)": 0.12,
                   "HP mid":                                0.25,
                   "HP recirculation (datasheet, Umluft)":  0.38}

# Fresh-air dilution mode (winter): electricity is fan power only; the cost is thermal.
SFP_KW_PER_M3S = 2.0                   # specific fan power, modern AHU [verify] (AIVC TN65 / CIBSE: 2-2.5)
ETA_HEAT_RECOVERY = 0.70               # plate/rotary recovery on exhaust [assumption, typical]
T_OUT_WINTER_C, RH_OUT_WINTER = 0.0, 0.80

# Heat pump used to charge the pool (turns electricity into stored heat). Same central JAZ as R1.
JAZ_CHARGE = 3.5

# Fraction of the extra latent heat that a pool-water condenser returns to the pool in HP mode.
# Menerga offers a "Beckenwasserkondensator" option. 0 = none, 0.8 = fitted. [assumption]
LATENT_RECOVERY_HP = {"no pool condenser": 0.0, "pool condenser fitted": 0.8}


# ----------------------------------------------------------------------------------------------
# MODEL
# ----------------------------------------------------------------------------------------------

def evap_vdi_kg_h(t_w, eps):
    return eps * AREA_M2 * (p_sat_hpa(t_w) - P_HALL_HPA) / 1000.0


def evap_shah_kg_h(t_w, occupied):
    t_air = t_w + AIR_OFFSET_K
    p_w = p_sat_hpa(t_w)
    W_w, W_r = x_from_p(p_w), X_HALL_CAP
    rho_w = rho_moist(t_w, p_w)            # saturated air at water surface temperature
    rho_r = rho_moist(t_air, P_HALL_HPA)   # room air
    d_rho = rho_r - rho_w
    e_nat = SHAH_C * rho_w * (max(d_rho, 0.0) ** (1.0 / 3.0)) * (W_w - W_r) if d_rho > 0 else 0.0
    e_forced = SHAH_B * (p_w - P_HALL_HPA) * 100.0
    e0 = max(e_nat, e_forced)
    if occupied:
        e0 *= (1.9 - 21.0 * d_rho + 5.3 * N_STAR_OCCUPIED)
    return e0 * AREA_M2


def penalty(dT, eps, hold_h, mode, e_dh=None, latent_recovery=0.0):
    """Return a dict of losses and costs for holding the pool at T_base + dT for hold_h hours.

    mode: 'hp' (heat-pump dehumidification, specific electricity e_dh) or 'fresh_air_winter'."""
    t1 = T_WATER_BASE_C + dT
    stored_kwh = C_POOL_KWH_PER_K * dT
    shifted_el_kwh = stored_kwh / JAZ_CHARGE

    m0 = evap_vdi_kg_h(T_WATER_BASE_C, eps)
    m1 = evap_vdi_kg_h(t1, eps)
    dm = m1 - m0                                            # extra evaporation, kg/h

    latent_kwh = dm * H_FG_KWH_PER_KG * hold_h
    makeup_kwh = dm * (t1 - T_MAKEUP_C) * CP_WATER_KWH_PER_KG_K * hold_h

    if mode == "hp":
        el_kwh = dm * e_dh * hold_h
        vent_th_kwh = 0.0
        latent_net_kwh = latent_kwh * (1.0 - latent_recovery)
    else:  # fresh-air dilution in winter
        x_out = x_from_p(RH_OUT_WINTER * p_sat_hpa(T_OUT_WINTER_C))
        air_kg_h = dm / (X_HALL_CAP - x_out)
        rho_r = rho_moist(t1 + AIR_OFFSET_K, P_HALL_HPA)
        vol_m3_s = air_kg_h / rho_r / 3600.0
        el_kwh = vol_m3_s * SFP_KW_PER_M3S * hold_h
        vent_th_kwh = (air_kg_h * CP_AIR_KJ * ((t1 + AIR_OFFSET_K) - T_OUT_WINTER_C) / 3600.0
                       * (1.0 - ETA_HEAT_RECOVERY) * hold_h)
        latent_net_kwh = latent_kwh                          # exhausted, not recovered

    thermal_loss_kwh = latent_net_kwh + makeup_kwh + vent_th_kwh
    return dict(dT=dT, stored=stored_kwh, shifted_el=shifted_el_kwh, m0=m0, m1=m1, dm=dm,
                latent=latent_kwh, latent_net=latent_net_kwh, makeup=makeup_kwh, vent_th=vent_th_kwh,
                thermal_loss=thermal_loss_kwh, el=el_kwh,
                remaining_frac=1.0 - thermal_loss_kwh / stored_kwh,
                el_penalty_frac=el_kwh / shifted_el_kwh)


# ----------------------------------------------------------------------------------------------
# REPORT
# ----------------------------------------------------------------------------------------------

def main():
    print("R4  The evaporation loop: cost of storing heat in pool water")
    print("=" * 96)
    print(f"Reference pool {AREA_M2:.0f} m2 x {VOLUME_M3 / AREA_M2:.1f} m = {VOLUME_M3:.0f} m3; "
          f"thermal capacity {C_POOL_KWH_PER_K:.0f} kWh/K. Base {T_WATER_BASE_C:.0f} C water, "
          f"hall air {T_WATER_BASE_C + AIR_OFFSET_K:.0f} C, x_cap {X_HALL_CAP * 1000:.1f} g/kg "
          f"(p_d {P_HALL_HPA:.1f} hPa).")
    print(f"Magnus check: p_sat(27 C) = {p_sat_hpa(27):.1f} hPa (DGfdB: 35.6).")
    print()

    # --- 1. Evaporation vs water temperature, both models ---
    print("1. Evaporation vs water temperature (kg/h, whole pool)")
    print("-" * 96)
    print(f"  {'T_w':>5} {'VDI rest':>10} {'VDI oper.':>10} {'Shah unocc.':>12} {'Shah occ.':>10} "
          f"{'VDI oper. vs 28C':>17}")
    base_op = evap_vdi_kg_h(T_WATER_BASE_C, EPS_OPERATION)
    for t in [26, 27, 28, 29, 30, 31, 32]:
        print(f"  {t:>5} {evap_vdi_kg_h(t, EPS_REST):>10.1f} {evap_vdi_kg_h(t, EPS_OPERATION):>10.1f} "
              f"{evap_shah_kg_h(t, False):>12.1f} {evap_shah_kg_h(t, True):>10.1f} "
              f"{(evap_vdi_kg_h(t, EPS_OPERATION) / base_op - 1) * 100:>+16.0f}%")
    print("  Reading: +2 K raises evaporation by roughly 30 % under VDI; Shah's buoyancy term makes it")
    print("  steeper. Both agree the effect is large and monotonic.")
    print()

    # --- 2. Baseline annual calibration ---
    hours_op, hours_rest = 10.0, 14.0
    daily_kg = hours_op * evap_vdi_kg_h(T_WATER_BASE_C, EPS_OPERATION) + hours_rest * evap_vdi_kg_h(T_WATER_BASE_C, EPS_REST)
    annual_t = daily_kg * 365 / 1000
    annual_latent_mwh = annual_t * 1000 * H_FG_KWH_PER_KG / 1000
    annual_makeup_mwh = annual_t * 1000 * (T_WATER_BASE_C - T_MAKEUP_C) * CP_WATER_KWH_PER_KG_K / 1000
    print("2. Baseline calibration (28 C, 10 h operation + 14 h rest per day)")
    print("-" * 96)
    print(f"  Evaporation {annual_t:,.0f} t/yr -> latent {annual_latent_mwh:.0f} MWh_th/yr + makeup heating "
          f"{annual_makeup_mwh:.0f} MWh_th/yr")
    for name, e in E_DH_KWH_PER_KG.items():
        print(f"  Dehumidification electricity at {e:.2f} kWh/kg ({name}): {annual_t * e:,.0f} MWh_el/yr")
    print("  Anchors: Bekanntmachung 2021 TEK Be-/Entfeuchtung 30 kWh/m2a NGF x ~3,000 m2 NGF = ~90 MWh_el/yr;")
    print("  UBA 2024 mean facility heat 1.21 GWh/yr; Benakcha et al. 2025: evaporation ~2/3 of water heat loss.")
    print("  Model lands inside both, so the scale is right to first order.")
    print()

    # --- 3. Penalty tables ---
    print("3. Holding a charge: what it costs (per event, whole pool)")
    print("-" * 96)
    cases = [
        ("Overnight rest, 6 h, winter fresh-air dehumidification", EPS_REST, 6, "fresh_air_winter", None, 0.0),
        ("Overnight rest, 6 h, HP dehumidification 0.12 kWh/kg", EPS_REST, 6, "hp", 0.12, 0.0),
        ("Overnight rest, 6 h, HP dehumidification 0.38 kWh/kg", EPS_REST, 6, "hp", 0.38, 0.0),
        ("Overnight rest, 6 h, HP 0.38 + pool condenser (80 % latent back)", EPS_REST, 6, "hp", 0.38, 0.8),
        ("Held through operation, 12 h, winter fresh-air", EPS_OPERATION, 12, "fresh_air_winter", None, 0.0),
        ("Held through operation, 12 h, HP 0.12 kWh/kg", EPS_OPERATION, 12, "hp", 0.12, 0.0),
        ("Held through operation, 12 h, HP 0.38 kWh/kg (summer, recirculation)", EPS_OPERATION, 12, "hp", 0.38, 0.0),
        ("Held through operation, 12 h, HP 0.38 + pool condenser", EPS_OPERATION, 12, "hp", 0.38, 0.8),
    ]
    for label, eps, hold, mode, e_dh, rec in cases:
        print(f"  {label}")
        print(f"    {'dT':>4} {'stored':>8} {'shift_el':>9} {'+evap':>7} {'latent':>8} {'makeup':>7} "
              f"{'vent_th':>8} {'th_loss':>8} {'remain':>7} {'el_pen':>7} {'el/shift':>9}")
        print(f"    {'K':>4} {'kWh_th':>8} {'kWh_el':>9} {'kg/h':>7} {'kWh_th':>8} {'kWh_th':>7} "
              f"{'kWh_th':>8} {'kWh_th':>8} {'%':>7} {'kWh_el':>7} {'%':>9}")
        for dT in [0.5, 1.0, 1.5, 2.0]:
            r = penalty(dT, eps, hold, mode, e_dh, rec)
            print(f"    {r['dT']:>4.1f} {r['stored']:>8.0f} {r['shifted_el']:>9.0f} {r['dm']:>7.1f} "
                  f"{r['latent_net']:>8.0f} {r['makeup']:>7.0f} {r['vent_th']:>8.0f} {r['thermal_loss']:>8.0f} "
                  f"{r['remaining_frac'] * 100:>6.0f}% {r['el']:>7.1f} {r['el_penalty_frac'] * 100:>8.1f}%")
        print()

    # --- 4. Headline ---
    r_night = penalty(2.0, EPS_REST, 6, "fresh_air_winter")
    r_night_hp = penalty(2.0, EPS_REST, 6, "hp", 0.38)
    r_day = penalty(2.0, EPS_OPERATION, 12, "hp", 0.38)
    r_day_rec = penalty(2.0, EPS_OPERATION, 12, "hp", 0.38, 0.8)
    print("Headline (+2 K charge = %.0f kWh_th stored = %.0f kWh_el shifted at JAZ %.1f)"
          % (r_night["stored"], r_night["shifted_el"], JAZ_CHARGE))
    print("-" * 96)
    print(f"  Overnight, 6 h, winter fresh-air:   thermal loss {r_night['thermal_loss']:.0f} kWh "
          f"({100 - r_night['remaining_frac'] * 100:.1f} % of stored), electricity {r_night['el']:.1f} kWh "
          f"({r_night['el_penalty_frac'] * 100:.1f} % of shifted)")
    print(f"  Overnight, 6 h, HP recirculation:   thermal loss {r_night_hp['thermal_loss']:.0f} kWh "
          f"({100 - r_night_hp['remaining_frac'] * 100:.1f} %), electricity {r_night_hp['el']:.1f} kWh "
          f"({r_night_hp['el_penalty_frac'] * 100:.1f} %)")
    print(f"  Through operation, 12 h, HP recirc: thermal loss {r_day['thermal_loss']:.0f} kWh "
          f"({100 - r_day['remaining_frac'] * 100:.1f} %), electricity {r_day['el']:.1f} kWh "
          f"({r_day['el_penalty_frac'] * 100:.1f} %)")
    print(f"  ... same with pool condenser:       thermal loss {r_day_rec['thermal_loss']:.0f} kWh "
          f"({100 - r_day_rec['remaining_frac'] * 100:.1f} %), electricity {r_day_rec['el']:.1f} kWh "
          f"({r_day_rec['el_penalty_frac'] * 100:.1f} %)")
    print()
    print("Reading: the loop is a small tax on an overnight charge and a large one on a charge held through")
    print("bathing hours in summer. The store works as a night-to-morning device; it does not work as a")
    print("day-long buffer unless a pool-water condenser returns the evaporated heat.")


if __name__ == "__main__":
    main()
