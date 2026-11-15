"""
R1 - Electrification-conditional flexibility potential of German swimming baths.

Re-runs the potential-assessment logic of Wohlfarth, Klobasa & Esser (Energy Efficiency 2019,
12:327-341, online-first 2018, doi:10.1007/s12053-018-9728-3) on an electrified counterfactual.

Their Table 4 (after Schlomann et al. 2015) lists Baths at 1.4 TWh/a electricity with a
"sum of relevant shares" of flexible appliances of 0.0 TWh/a. Their Table 3 defines the flexible
appliances; "Heat pump/recirculation pump" (space heating) and "Electric water heating" (hot water)
are on that list. So if pool heat were supplied by heat pumps, that electricity would count as
flexible under their own rules. This script computes how much.

Every input carries its source and status label. Run: py r1_flexibility_calc.py
"""
import os as _os, sys as _sys
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")


# ----------------------------------------------------------------------------------------------
# INPUTS
# ----------------------------------------------------------------------------------------------

# Wohlfarth Table 4, row "Baths", 2013. VERIFIED by local extraction of the Fraunhofer ISI PDF.
BATHS_ELEC_TWH_2013 = 1.4          # total electricity, TWh/a
BATHS_FLEX_TWH_2013 = 0.0          # "sum of relevant shares" of flexible appliances, TWh/a

# Comparators from the same table (total electricity, sum of relevant shares). VERIFIED.
TABLE4 = {
    "Office-like enterprises":    (29.5, 3.6),
    "Retail trade":               (22.5, 6.8),
    "Hotels, restaurants, homes": (18.5, 5.4),
    "Hospitals":                  (6.1, 0.8),
    "Agriculture":                (4.3, 1.3),
    "Schools":                    (3.9, 0.3),
    "Construction industry":      (3.8, 0.9),
    "Baths":                      (1.4, 0.0),
    "Airports":                   (1.3, 0.3),
    "Laundries":                  (0.3, 0.0),
}

# Baths HEAT (fuels + district heat), same survey the table draws on.
# Schlomann et al. 2015, Fraunhofer ISI, GHD survey 2006-2013, Kurzfassung, Tabelle 1, group 5/3
# "Baeder": 2013 = Strom 1.4 / Brennstoffe+Fernwaerme 2.9 / Summe 4.3 TWh. VERIFIED by local
# extraction. Scope: ALL baths (indoor, outdoor, leisure, non-municipal included).
# Tabelle 3 (same source): ~93% of Baeder fuel use is "sonstige Prozesswaerme", i.e. water heating.
BATHS_HEAT_TWH_2013_ALL = 2.9
PROCESS_HEAT_SHARE = 0.929         # VERIFIED for the 92.9 figure; column of the remaining 7.1 [verify]

# Modern cross-check, narrower scope: MUNICIPAL INDOOR + COMBI pools only (n = 1,390).
# Weinfurter, Thieme & Wallrodt (2024), UBA TEXTE 139/2024, Tabelle 4. Two extrapolations:
# simple (per m2 water surface) and model (degressive). Authors use the range between them.
# VERIFIED by local extraction. Survey years 2019 and 2022.
UBA_HEAT_GWH_MODEL  = 1339.93
UBA_HEAT_GWH_SIMPLE = 1636.22
UBA_ELEC_GWH_MODEL  = 396.28
UBA_ELEC_GWH_SIMPLE = 482.07

# Seasonal heat-pump performance (JAZ = heat out / electricity in). Pool water sits at 26-30 C, so
# the sink temperature is low and favourable. General German ranges from trade sources [verify]:
# air-water 3.1-3.3, ground-coupled 4.0-4.6, groundwater/wastewater 4.5-5.0+.
# No pool-specific measured JAZ was found; three cases bracket it.
JAZ_CASES = {"low (air-source, conservative)": 3.0,
             "central":                        3.5,
             "high (ground/water-source)":     4.5}

# Share of the heat that is actually electrified. 1.0 = full fuel switch (upper bound).
ELECTRIFICATION_SHARES = [1.0, 0.5, 0.25]

# ----------------------------------------------------------------------------------------------
# CALCULATION
# ----------------------------------------------------------------------------------------------

def electrified(heat_twh, jaz, share):
    """Return (new heat-pump electricity, new total electricity, new flexible sum) in TWh/a.

    Under the Wohlfarth method the whole heat-pump consumption enters the 'sum of relevant
    shares' (theoretical potential, before the technical downward revision they note)."""
    e_hp = heat_twh * share / jaz
    return e_hp, BATHS_ELEC_TWH_2013 + e_hp, BATHS_FLEX_TWH_2013 + e_hp


def main():
    print("R1  Electrification-conditional flexibility potential, German baths")
    print("=" * 78)
    print(f"Status quo (Wohlfarth Table 4, 2013): electricity {BATHS_ELEC_TWH_2013:.1f} TWh/a, "
          f"flexible sum {BATHS_FLEX_TWH_2013:.1f} TWh/a")
    print(f"Heat demand behind it (Schlomann Tab.1, 2013, all baths): "
          f"{BATHS_HEAT_TWH_2013_ALL:.1f} TWh/a fuels + district heat, "
          f"of which ~{PROCESS_HEAT_SHARE:.0%} process heat (water heating)")
    print()

    bases = {
        "A  Schlomann 2013, ALL baths (like-for-like with Table 4)": BATHS_HEAT_TWH_2013_ALL,
        "B  UBA 2024 model extrapolation, municipal indoor+combi":   UBA_HEAT_GWH_MODEL / 1000,
        "C  UBA 2024 simple extrapolation, municipal indoor+combi":  UBA_HEAT_GWH_SIMPLE / 1000,
    }

    for label, heat in bases.items():
        print(f"Basis {label}: heat = {heat:.2f} TWh/a")
        print(f"  {'JAZ':<34}{'elec. share':>12}{'HP elec':>10}{'new total':>11}{'flex sum':>10}"
              f"{'flex frac':>11}")
        for jname, jaz in JAZ_CASES.items():
            for share in ELECTRIFICATION_SHARES:
                e_hp, tot, flex = electrified(heat, jaz, share)
                print(f"  {jname:<34}{share:>11.0%}{e_hp:>10.2f}{tot:>11.2f}{flex:>10.2f}"
                      f"{flex / tot:>11.0%}")
        print()

    # Headline: central JAZ, full switch, basis A; and the conservative corner.
    e_a, tot_a, flex_a = electrified(BATHS_HEAT_TWH_2013_ALL, 3.5, 1.0)
    e_c, tot_c, flex_c = electrified(UBA_HEAT_GWH_MODEL / 1000, 4.5, 1.0)
    print("Headline")
    print("-" * 78)
    print(f"Central case (basis A, JAZ 3.5, full switch): flexible sum 0.0 -> {flex_a:.2f} TWh/a; "
          f"flexible fraction of sector electricity {flex_a / tot_a:.0%}")
    print(f"Most conservative corner (basis B, JAZ 4.5, full switch): 0.0 -> {flex_c:.2f} TWh/a; "
          f"fraction {flex_c / tot_c:.0%}")
    print()

    print("Where that would place Baths in Table 4 (sum of relevant shares, TWh/a)")
    print("-" * 78)
    rows = dict(TABLE4)
    rows["Baths (electrified, central)"] = (tot_a, flex_a)
    rows["Baths (electrified, conservative)"] = (tot_c, flex_c)
    for name, (tot, flex) in sorted(rows.items(), key=lambda kv: -kv[1][1]):
        frac = flex / tot if tot else 0
        print(f"  {name:<38}{tot:>8.1f}{flex:>8.2f}{frac:>9.0%}")
    print()
    print("Reading: the standard method scores Baths at 0.0 because it counts flexible ELECTRIC")
    print("appliances and the heat is fossil. Electrify the heat and the same method places Baths")
    print("alongside Hospitals and Construction in absolute terms, and above every subsector in")
    print("flexible FRACTION, because ~93% of the load is process heat into a storage-capable medium.")
    print("These are theoretical potentials, like Table 4 itself. The technical revision depends on")
    print("the comfort/hygiene envelope (R4), which is the open research question.")


if __name__ == "__main__":
    main()
