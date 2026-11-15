"""
Q0.2 - OpenStreetMap pool facilities in Schleswig-Holstein (Overpass API).

Pulls every pool-related element inside the DE-SH boundary, removes private pools and natural
bathing sites, clusters basins into facilities, classifies indoor/outdoor from tags and names, and
reports attribute coverage. The finding this script documents: OSM gives names and coordinates,
and essentially none of the technical attributes SPLASH needs.

Run: py q02_osm_pools.py            (queries Overpass live; ~30 s)
     py q02_osm_pools.py cached.json (re-uses a saved Overpass JSON)
Evidence copy of the 2026-09-11 query result: .drafts/evidence/osm_overpass_sh_pools_2026-09-11.json
"""
import os as _os, sys as _sys
# Resolve any command-line path against the caller's directory BEFORE moving to our own,
# so that both "py research/q02_osm_pools.py cached.json" and a bare run work.
_sys.argv[1:] = [_os.path.abspath(a) for a in _sys.argv[1:]]
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")

import sys, json, re, math, collections, urllib.request, urllib.parse, csv

QUERY = """
[out:json][timeout:180];
area["ISO3166-2"="DE-SH"]->.sh;
(
  nwr["leisure"="sports_centre"]["sport"~"swimming"](area.sh);
  nwr["leisure"="swimming_pool"](area.sh);
  nwr["leisure"="water_park"](area.sh);
  nwr["amenity"="public_bath"](area.sh);
  nwr["leisure"="swimming_area"](area.sh);
  nwr["sport"="swimming"]["leisure"!="sports_centre"]["leisure"!="swimming_pool"](area.sh);
);
out center tags;
"""

NATURAL = {"swimming_area", "bathing_place", "beach_resort"}
NAME_POOL = re.compile(r"(hallenbad|freibad|schwimmbad|schwimmhalle|erlebnisbad|spa[ßs]bad|freizeitbad|therme|badeland|"
                       r"bad\b|aquapark|wellenbad|kombibad|naturbad|strandbad|meerwasser)", re.I)
IND = re.compile(r"(hallenbad|schwimmhalle|therme|badeland|badezentrum)", re.I)
OUT = re.compile(r"(freibad|naturbad|strandbad|seebad|waldbad|meerwasserwellenbad)", re.I)
TECH_KEYS = ["opening_hours", "website", "phone", "operator", "length", "depth", "swimming_pool:type",
             "heating", "heated", "water_temperature", "capacity", "building", "start_date", "source"]


def fetch():
    data = urllib.parse.urlencode({"data": QUERY}).encode()
    req = urllib.request.Request("https://overpass-api.de/api/interpreter", data=data,
                                 headers={"User-Agent": "phd-research-splash/1.0"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.load(r)


def latlon(e):
    if "lat" in e:
        return e["lat"], e["lon"]
    c = e.get("center")
    return (c["lat"], c["lon"]) if c else (None, None)


def dist_m(a, b):
    if None in a or None in b:
        return 1e9
    R = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dl, dp = math.radians(b[1] - a[1]), p2 - p1
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def classify(t, name):
    if t.get("indoor") == "yes" or t.get("covered") == "yes" or t.get("building") not in (None, "no") or IND.search(name):
        return "indoor"
    if t.get("outdoor") == "yes" or OUT.search(name):
        return "outdoor"
    return "unknown"


def main():
    # Default: the saved 2026-09-11 evidence copy, so that a re-run reproduces the published counts.
    # Pass --live to query Overpass again (counts drift as OpenStreetMap is edited).
    live = "--live" in sys.argv[1:]
    args = [x for x in sys.argv[1:] if not x.endswith("--live")]
    d = fetch() if live else json.load(open(
        args[0] if args else ".drafts/evidence/osm_overpass_sh_pools_2026-09-11.json", encoding="utf-8"))
    els = d["elements"]
    print("raw elements:", len(els))
    rows = []
    for e in els:
        t = e.get("tags", {})
        lat, lon = latlon(e)
        lei, acc, name = t.get("leisure", ""), t.get("access", ""), t.get("name", "")
        if acc == "private":
            continue
        if lei in NATURAL and not NAME_POOL.search(name):
            continue
        if t.get("natural") == "water" or t.get("water"):
            continue
        rows.append(dict(id=f"{e['type']}/{e['id']}", name=name, lat=lat, lon=lon, leisure=lei,
                         access=acc, cls=classify(t, name), operator=t.get("operator", ""), tags=t))
    print("after removing private pools and natural water:", len(rows))

    named = [r for r in rows if r["name"]]
    unnamed = [r for r in rows if not r["name"]]
    merged = []
    for r in sorted(named, key=lambda x: (x["leisure"] != "sports_centre", x["leisure"] != "water_park")):
        hit = None
        for m in merged:
            dm = dist_m((r["lat"], r["lon"]), (m["lat"], m["lon"]))
            same = r["name"].lower() == m["name"].lower()
            if dm < 300 and (same or (NAME_POOL.search(r["name"]) and NAME_POOL.search(m["name"]) and dm < 120)):
                hit = m
                break
        if hit:
            hit["members"].append(r["id"])
            if hit["cls"] == "unknown" and r["cls"] != "unknown":
                hit["cls"] = r["cls"]
            hit["operator"] = hit["operator"] or r["operator"]
        else:
            r = dict(r)
            r["members"] = [r["id"]]
            merged.append(r)
    attached, orphans = 0, []
    for u in unnamed:
        near = [m for m in merged if dist_m((u["lat"], u["lon"]), (m["lat"], m["lon"])) < 150]
        if near:
            near[0]["members"].append(u["id"])
            attached += 1
            if near[0]["cls"] == "unknown" and u["cls"] != "unknown":
                near[0]["cls"] = u["cls"]
        else:
            orphans.append(u)
    print(f"named facilities: {len(merged)} | basins attached: {attached} | unnamed orphans: {len(orphans)}")
    print("facilities by class:", collections.Counter(m["cls"] for m in merged).most_common())
    print("facilities with operator tag:", sum(1 for m in merged if m["operator"]))
    print("attribute coverage (named facilities):")
    for k in TECH_KEYS:
        print(f"  {k:20s} {sum(1 for m in merged if k in m['tags']):4d}")

    with open("q02_osm_sh_facilities.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["osm_id", "name", "lat", "lon", "class", "leisure", "access", "operator", "n_members"])
        for m in sorted(merged, key=lambda x: x["name"]):
            w.writerow([m["id"], m["name"], m["lat"], m["lon"], m["cls"], m["leisure"], m["access"], m["operator"], len(m["members"])])
    print("saved q02_osm_sh_facilities.csv")


if __name__ == "__main__":
    main()
