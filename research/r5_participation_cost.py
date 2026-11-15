"""
R5 - Cost of participation in §13k EnWG for one municipal indoor pool, first order.

Value side from the TSO implementation concept (2026-04-01) and BDEW price data; cost side from
the concept's participation requirements with stated assumptions. Every input is labelled.
Run: py r5_participation_cost.py
"""
import os as _os, sys as _sys
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")

import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --- VALUE PER MWh ---------------------------------------------------------------------------
PRICE_NORMAL_CT = 17.2        # BDEW Strompreisanalyse 2026, small/mid industry supply contracts, ct/kWh [verify: summary]
BID_FLOOR_EUR_MWH = 21.68     # Mindestpreis 2027 worked example, ÜNB concept 6.3.1 / ch. 11. VERIFIED
NONCOMP_EUR_MWH = 10.0        # procurement above day-ahead, supplier margin, uncompensated residuals [assumption]
net_cost_eur_mwh = BID_FLOOR_EUR_MWH + NONCOMP_EUR_MWH
saving_eur_mwh = PRICE_NORMAL_CT * 10 - net_cost_eur_mwh

# --- VOLUME ----------------------------------------------------------------------------------
HP_KW_EL = {"large Hallenbad heat pump": 150.0, "small facility / teaching pool": 60.0}   # [assumption]; Segment 3 needs >= 100 kW
ALLOC_H = {"concept example region-year": 900.0, "half of that": 450.0}                 # Bhx example, ÜNB ch. 11. VERIFIED as example
STORAGE_HEADROOM = {"children/teaching pool, KOK 28-32 C (+2 K usable)": 1.0,
                    "sports pool at 28 C, KOK 24-28 C (no upward headroom)": 0.35}      # fraction of allocated hours the plant can actually absorb [assumption]

# --- COSTS (per site) ------------------------------------------------------------------------
ONE_OFF = {"separate Marktlokation + RLM sub-meter for the heat pump": 4000.0,           # [assumption]
           "aggregator onboarding / communication test (5.1.3)": 8000.0,                  # [assumption]
           "council decision, contract review, steering-right agreement": 6000.0}         # [assumption: staff time]
ANNUAL_FIXED = {"metering operation and data provision (5.1.4)": 600.0,                   # [assumption]
                "in-house admin: monthly bid, daily availability, settlement (0.05 FTE)": 4000.0}  # [assumption]
AGGREGATOR_SHARE = 0.25       # of gross value, typical DSM aggregator fee band 15-30 % [verify]
LIFETIME_Y = 8


def run(hp_kw, alloc_h, headroom):
    mwh = hp_kw * alloc_h * headroom / 1000.0
    gross = mwh * saving_eur_mwh
    agg = gross * AGGREGATOR_SHARE
    annual_net = gross - agg - sum(ANNUAL_FIXED.values())
    one_off = sum(ONE_OFF.values())
    return mwh, gross, agg, annual_net, annual_net * LIFETIME_Y - one_off


print("R5  Cost of §13k participation, one municipal indoor pool, first order")
print("=" * 92)
print(f"Saving per allocated MWh: {PRICE_NORMAL_CT*10:.0f} (normal) - {net_cost_eur_mwh:.0f} (bid floor {BID_FLOOR_EUR_MWH} + residuals {NONCOMP_EUR_MWH:.0f}) = {saving_eur_mwh:.0f} EUR/MWh")
print(f"One-off per site: {sum(ONE_OFF.values()):,.0f} EUR | annual fixed: {sum(ANNUAL_FIXED.values()):,.0f} EUR | aggregator {AGGREGATOR_SHARE:.0%} of gross")
print()
print(f"  {'plant':32s} {'alloc h':>8s} {'headroom':>9s} {'MWh/yr':>7s} {'gross':>8s} {'agg fee':>8s} {'net/yr':>8s} {'8-yr NPV0':>10s}")
for pn, kw in HP_KW_EL.items():
    for an, ah in ALLOC_H.items():
        for hn, hr in STORAGE_HEADROOM.items():
            mwh, gross, agg, net, npv = run(kw, ah, hr)
            tag = "" if kw >= 100 else "  (<100 kW: aggregation required)"
            print(f"  {pn[:32]:32s} {ah:8.0f} {hr:9.2f} {mwh:7.0f} {gross:8,.0f} {agg:8,.0f} {net:8,.0f} {npv:10,.0f}{tag}")
        print()
print("Reading: value is (kW x allocated hours x headroom) x price spread; costs are fixed per site.")
print("A large Hallenbad with storage headroom clears its costs; a sports pool at the top of its KOK")
print("band, or any plant under 100 kW, does not on its own. The economics are a fleet question.")
