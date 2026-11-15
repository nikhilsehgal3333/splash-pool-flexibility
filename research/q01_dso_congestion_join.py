"""
Q0.1 - Where is Schleswig-Holstein's curtailment actually caused, and what can a pool reach?

Two parts.
(1) Causation arithmetic from the primary statements: how much of SH curtailment is transmission-
    caused (and therefore reachable only through the TSO instrument, §13k) versus distribution-
    caused (for which no instrument exists).
(2) A join of the FAG pool list to SH Netz's twelve medium-voltage congestion regions from the
    Netzausbauplan 2024 (Tabelle 6). Those regions are county-shaped, so the join is by county,
    not by distance. The percentages are projected overloaded line elements in the 2045 scenario,
    not current curtailment.

Run: py q01_dso_congestion_join.py
"""
import os as _os, sys as _sys
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")

import csv, collections, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --- (1) causation ----------------------------------------------------------------------------
SH_CURTAILED_2025_GWH = 802.0      # SH Netz, on-land RE. MEKUN 15.04.2026. VERIFIED
TENNET_ORDERED_MIN = 0.65          # "Über 65% dieser Abregelungen ... auf Anforderung des ... Tennet". VERIFIED
SHN_OWN_CASES_EHV_CAUSED = 0.90    # "in über 90 Prozent der Fälle nicht im 110-kV-Netz von SH Netz". 2017. [verify: dated]

# --- (2) SH Netz MV congestion regions, Netzausbauplan 2024 Tabelle 6, 2045 scenario -----------
# region number: (county as named by SH Netz, Netzcenter(s), share of overloaded MV line elements)
REGIONS = {
    "1":  ("Dithmarschen",          "Meldorf",                 0.48),
    "2":  ("Herzogtum Lauenburg",   "Schwarzenbek",            0.55),
    "3":  ("Nordfriesland",         "Friedrichstadt, Niebüll", 0.29),
    "4":  ("Ostholstein",           "Pönitz",                  0.72),
    "5":  ("Pinneberg",             "Uetersen",                0.63),
    "6":  ("Plön",                  "Plön",                    0.29),
    "7":  ("Rendsburg-Eckernförde", "Fockbek",                 0.38),
    "8":  ("Schleswig-Flensburg",   "Schuby, Süderbrarup",     0.35),
    "9":  ("Segeberg",              "Segeberg, Kaltenkirchen", 0.67),
    "10": ("Steinburg",             "Dägeling",                0.26),
    "11": ("Stormarn",              "Ahrensburg",              0.52),
    "12": ("Neumünster (Stadt)",    "Neumünster",              0.34),
}
BY_KREIS = {county: (n, nc, share) for n, (county, nc, share) in REGIONS.items()}
# Not in SH Netz's plan: the three cities served by other distribution operators.
OTHER_DSO = {"Flensburg (Stadt)": "Stadtwerke Flensburg", "Kiel (Stadt)": "Stadtwerke Kiel / SH Netz [verify]",
             "Lübeck (Stadt)": "TraveNetz"}

print("Q0.1  Where SH curtailment is caused, and what a distribution-connected pool can reach")
print("=" * 94)
tennet = SH_CURTAILED_2025_GWH * TENNET_ORDERED_MIN
own = SH_CURTAILED_2025_GWH - tennet
own_ehv = own * SHN_OWN_CASES_EHV_CAUSED
dso_caused = own - own_ehv
print(f"  SH Netz on-land curtailment 2025                      {SH_CURTAILED_2025_GWH:7.0f} GWh   VERIFIED")
print(f"  of which ordered by TenneT (transmission congestion)   {tennet:7.0f} GWh   at least 65 %, VERIFIED")
print(f"  remainder instructed by SH Netz itself                 {own:7.0f} GWh")
print(f"    of that, caused by EHV unavailability, not 110 kV    {own_ehv:7.0f} GWh   >90 % of cases, [verify] 2017 figure")
print(f"    genuinely caused in the distribution network         {dso_caused:7.0f} GWh   ~{dso_caused/SH_CURTAILED_2025_GWH:.0%} of the total")
print()
print("  Indicative only: the 65 % is a 2026 volume share, the 90 % a 2017 case share. Both are")
print("  lower bounds on transmission causation, so the distribution residual is an upper bound.")
print("  Independent confirmation: the distribution operators told the TSOs at the end of 2025 that")
print("  they see no case of their own for a §13k Abs. 8 instrument (VERIFIED, ÜNB concept).")
print()

# --- (3) pools against projected MV congestion -------------------------------------------------
rows = list(csv.DictReader(open("r2_fag_pools_wind_proximity.csv", encoding="utf-8-sig")))
ind = lambda r: r["art"] == "Hallenbad"
for r in rows:
    hit = BY_KREIS.get(r["kreis"])
    r["mv_region"], r["mv_netzcenter"], r["mv_overload_2045"] = (hit[0], hit[1], hit[2]) if hit else ("", OTHER_DSO.get(r["kreis"], ""), "")
print("Indoor units by projected 2045 MV overload share of their county, with §13k eligibility:")
print(f"  {'county':24s} {'reg':>4s} {'overload':>9s} {'indoor':>7s} {'§13k':>6s}")
agg = collections.defaultdict(int)
for r in rows:
    if ind(r): agg[r["kreis"]] += 1
for kreis, n in sorted(agg.items(), key=lambda kv: -(BY_KREIS.get(kv[0], ("", "", -1))[2])):
    hit = BY_KREIS.get(kreis)
    reg = hit[0] if hit else "-"
    ov = f"{hit[2]:.0%}" if hit else "n/a"
    elig = "yes" if kreis in ("Dithmarschen", "Nordfriesland", "Neumünster (Stadt)", "Lübeck (Stadt)", "Pinneberg",
                              "Rendsburg-Eckernförde", "Schleswig-Flensburg", "Segeberg", "Steinburg", "Stormarn") else "no"
    print(f"  {kreis:24s} {reg:>4s} {ov:>9s} {n:7d} {elig:>6s}")
print()
print("  Counties with the highest projected MV overload (Ostholstein 72 %, Segeberg 67 %,")
print("  Pinneberg 63 %) are not the counties with today's transmission-caused curtailment.")
print("  Ostholstein, Plön and Herzogtum Lauenburg are outside the §13k relief regions entirely.")
with open("q01_fag_pools_dso_congestion.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("\nsaved q01_fag_pools_dso_congestion.csv")
