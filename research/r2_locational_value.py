"""
R2 - Locational value, desk version: does proximity to wind generation predict §13k eligibility?

Joins (a) the 2025 FAG pool list (q02_fag2025_sh_pools.csv), (b) OpenStreetMap wind turbines in
Schleswig-Holstein, and (c) the §13k EnWG relief regions (Entlastungsregionen) designated by the
TSOs by Landkreis in the 2026-04-01 implementation concept, effective with the target model from
1 October 2026. Proximity is measured from postcode/town centroids because the FAG list prints the
municipal office address, not the facility address; treat distances as +/- a few km.

Run: py r2_locational_value.py     (uses .drafts/geocode_cache.json; queries Nominatim for misses)
"""
import os as _os, sys as _sys
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")

import csv, json, math, os, sys, time, collections, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIND = ".drafts/evidence/osm_overpass_sh_wind_turbines_2026-09-11.json"
POOLS = "q02_fag2025_sh_pools.csv"
CACHE = ".drafts/geocode_cache.json"
# ÜNB Umsetzungskonzept §13k EnWG, Stand 01.04.2026, section 3.3.3, TenneT regions in SH. VERIFIED.
REGION = {"Dithmarschen": "T5", "Nordfriesland": "T5",
          "Neumünster (Stadt)": "T6", "Lübeck (Stadt)": "T6", "Pinneberg": "T6", "Rendsburg-Eckernförde": "T6",
          "Schleswig-Flensburg": "T6", "Segeberg": "T6", "Steinburg": "T6", "Stormarn": "T6"}
KREIS_TOWN = {"Flensburg (Stadt)": "Flensburg", "Kiel (Stadt)": "Kiel", "Lübeck (Stadt)": "Lübeck", "Neumünster (Stadt)": "Neumünster"}
NEAR_N, NEAR_KM = 10, 5.0


def nominatim(params):
    key = "S:" + json.dumps(params, sort_keys=True)
    if key in cache:
        return cache[key]
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(dict(params, format="json", limit=1, countrycodes="de"))
    req = urllib.request.Request(url, headers={"User-Agent": "phd-research-splash/1.0 (research)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            js = json.load(r)
        res = [float(js[0]["lat"]), float(js[0]["lon"]), js[0].get("display_name", "")] if js else None
    except Exception:
        res = None
    cache[key] = res
    time.sleep(1.1)
    return res


def plausible(r, match):
    """The geocode must name the facility town, the office town, or the Kreis."""
    m = match.lower()
    for cand in (r["ort2"], r["ort"], KREIS_TOWN.get(r["kreis"], r["kreis"].split(" (")[0])):
        if cand and cand.lower().split("/")[0].strip() in m:
            return True
    return False


def dist_km(a, b):
    dl, dp = b[1] - a[1], b[0] - a[0]
    h = math.sin(dp / 2) ** 2 + math.cos(a[0]) * math.cos(b[0]) * math.sin(dl / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
rows = list(csv.DictReader(open(POOLS, encoding="utf-8-sig")))

# --- geocode with plausibility check; structured query first, then free text ---
fixed = 0
for r in rows:
    town = r["ort2"] or r["ort"]
    tries = [{"city": town, "postalcode": r["plz"], "state": "Schleswig-Holstein"},
             {"city": town, "state": "Schleswig-Holstein"},
             {"q": f"{r['plz']} {town}, Schleswig-Holstein"}]
    g = None
    for t in tries:
        g = nominatim(t)
        if g and plausible(r, g[2]):
            break
        g = None
    if g is None:  # fall back to the office town
        g = nominatim({"city": r["ort"], "state": "Schleswig-Holstein"})
        if g and not plausible(r, g[2]):
            g = None
    r["lat"], r["lon"], r["geo_match"] = (g[0], g[1], g[2][:70]) if g else ("", "", "UNRESOLVED")
    r["relief_region"] = REGION.get(r["kreis"], "none")
json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
print("geocoded:", sum(1 for r in rows if r["lat"]), "/", len(rows), "| unresolved:", [r["name"][:30] for r in rows if not r["lat"]])

# --- turbines ---
els = json.load(open(WIND, encoding="utf-8"))["elements"]
tur = []
for e in els:
    t = e.get("tags", {})
    if t.get("location") == "offshore" or t.get("offshore") == "yes":
        continue
    lat = e.get("lat") or (e.get("center") or {}).get("lat")
    lon = e.get("lon") or (e.get("center") or {}).get("lon")
    if lat and lon:
        tur.append((math.radians(lat), math.radians(lon)))
for r in rows:
    if not r["lat"]:
        r["nearest_turbine_km"] = r["turbines_5km"] = r["turbines_10km"] = ""
        continue
    p = (math.radians(float(r["lat"])), math.radians(float(r["lon"])))
    ds = [dist_km(p, t) for t in tur]
    r["nearest_turbine_km"] = round(min(ds), 2)
    r["turbines_5km"] = sum(1 for d in ds if d <= 5)
    r["turbines_10km"] = sum(1 for d in ds if d <= 10)
print("onshore turbines:", len(tur))

# --- analysis ---
ind = lambda r: r["art"] == "Hallenbad"
q = lambda v, p: sorted(v)[int(p * (len(v) - 1))] if v else float("nan")
print("\nsanity, city rows:")
for r in rows:
    if r["kreis"] in ("Lübeck (Stadt)", "Kiel (Stadt)", "Flensburg (Stadt)") and ind(r) and r["lat"]:
        print(f"  {r['name'][:34]:34s} {r['plz']} -> {r['lat']:.3f},{r['lon']:.3f} turb5km={r['turbines_5km']} | {r['geo_match'][:40]}")
print("\nrelief-region membership (indoor / outdoor units):")
c = collections.Counter((r["relief_region"], "indoor" if ind(r) else "outdoor") for r in rows)
for reg in ("T5", "T6", "none"):
    print(f"  {reg:5s} indoor {c[(reg, 'indoor')]:3d}  outdoor {c[(reg, 'outdoor')]:3d}")
n_in = sum(1 for r in rows if ind(r)); e_in = sum(1 for r in rows if ind(r) and r["relief_region"] != "none")
print(f"  indoor units in a relief region: {e_in}/{n_in} = {e_in / n_in:.0%}")
print("\nproximity by eligibility, indoor units:")
for reg in ("T5", "T6", "none"):
    sel = [r for r in rows if ind(r) and r["relief_region"] == reg and r["lat"]]
    nd = [float(r["nearest_turbine_km"]) for r in sel]; t5 = [int(r["turbines_5km"]) for r in sel]
    print(f"  {reg:5s} n={len(sel):2d}  nearest median {q(nd, .5):4.1f} km (IQR {q(nd, .25):.1f}-{q(nd, .75):.1f}) | within 5 km median {q(t5, .5):3.0f} | near wind (>= {NEAR_N} within {NEAR_KM:.0f} km): {sum(1 for x in t5 if x >= NEAR_N)}")
near = lambda r: r["lat"] and int(r["turbines_5km"]) >= NEAR_N
elig = lambda r: r["relief_region"] != "none"
cc = collections.Counter(("near" if near(r) else "far", "eligible" if elig(r) else "ineligible") for r in rows if ind(r) and r["lat"])
print("\n2x2, indoor units:")
for k in [("near", "eligible"), ("near", "ineligible"), ("far", "eligible"), ("far", "ineligible")]:
    print(f"  {k[0]:4s} & {k[1]:10s}: {cc[k]:3d}")
tot = sum(cc.values()); agree = cc[("near", "eligible")] + cc[("far", "ineligible")]
print(f"  proximity proxy agrees with eligibility in {agree}/{tot} = {agree / tot:.0%}; disagrees in {tot - agree}/{tot}")
print("\nindoor units OUTSIDE any relief region:")
for r in rows:
    if ind(r) and not elig(r):
        print(f"  {r['kreis']:22s} {r['name'][:44]:44s} nearest {float(r['nearest_turbine_km']) if r['lat'] else float('nan'):4.1f} km, within 5 km {r['turbines_5km']}")
with open("r2_fag_pools_wind_proximity.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("\nsaved r2_fag_pools_wind_proximity.csv")
