"""
Q0.2 - Parse Anlage 2 of Landtag Drucksache 20/4417 (29 Apr 2026): the 2025 FAG swimming-lesson
funding list, i.e. every publicly funded swimming facility/basin in Schleswig-Holstein.

Input: reading-order text of the Drucksache (pdftotext -raw). Layout mode clips the landscape page
at 256 characters and breaks the second half of the list; raw mode puts each row on one line:
  N. VVVV Amt/Gemeinde Strasse PLZ Ort Name Ort2 Art [Ja] [Stunden] Masszahl Foerderbetrag
Run: py q02_fag_pools.py .drafts/evidence/ltsh_drucksache_20-4417_pdftotext-raw.txt
"""
import os as _os, sys as _sys
_os.chdir(_os.path.dirname(_os.path.abspath(__file__)) or ".")

import sys, re, csv, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
src = sys.argv[1] if len(sys.argv) > 1 else ".drafts/evidence/ltsh_drucksache_20-4417_pdftotext-raw.txt"
KREIS = {"01":"Flensburg (Stadt)","02":"Kiel (Stadt)","03":"Lübeck (Stadt)","04":"Neumünster (Stadt)","51":"Dithmarschen",
         "53":"Herzogtum Lauenburg","54":"Nordfriesland","55":"Ostholstein","56":"Pinneberg","57":"Plön","58":"Rendsburg-Eckernförde",
         "59":"Schleswig-Flensburg","60":"Segeberg","61":"Steinburg","62":"Stormarn"}
ROW = re.compile(r'^(\d{1,3})\. (\d{4}) (.*?) (\d{5}) (.*?) (Hallenbad|Freibad|Naturbad|Kombibad|Lehrschwimmbecken|Freizeitbad|Erlebnisbad|Schwimmhalle|Therme|Sportbecken|Bewegungsbad)'
                 r'(?: (Ja|Nein))?(?: (\d+\.\d))? (\d\.\d{4,6}) ([\d,]+\.\d{2})\s*$')
recs, seen = [], set()
def _read(path):
    b = open(path, "rb").read()
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252", errors="replace")
for line in _read(src).splitlines():
    m = ROW.match(line.strip())
    if not m: continue
    nr, vid, amt_str, plz, mid, art, ja, std, mass, foe = m.groups()
    if nr in seen: continue          # the raw text repeats one page; keep first occurrence
    seen.add(nr)
    toks = mid.split()
    ort = toks[0] if toks else ""
    if ort in ("Bad", "Sankt", "St.", "Wyk", "Hohenwestedt-Land") and len(toks) > 1: ort = " ".join(toks[:2]) if toks[0] != "Wyk" else " ".join(toks[:3])
    name_ort2 = mid[len(ort):].strip()
    ort2 = name_ort2.split()[-1] if name_ort2 else ""
    name = name_ort2[: -len(ort2)].strip() if ort2 else name_ort2
    amt = re.sub(r'\s+\S.*$', '', amt_str) if False else amt_str
    kreis = KREIS.get(vid[:2])
    if kreis is None:
        # ID 9999 marks a unit whose Traeger is a Kreis, not a municipality (row 168, Steinburgschule
        # Itzehoe, Traeger "Kreis Steinburg"). Take the county from the Traeger name. Correction C21.
        km = re.match(r"Kreis (\S+(?: \S+)?)", amt_str)
        kreis = next((k for k in KREIS.values() if km and km.group(1).startswith(k)), "?" + vid[:2])
    recs.append(dict(nr=int(nr), vid=vid, kreis=kreis, amt_und_strasse=amt_str, plz=plz, ort=ort,
                     name=name, ort2=ort2, art=art, angeleitet=ja or "", stunden=float(std) if std else None,
                     masszahl=float(mass), foerderbetrag=float(foe.replace(",", ""))))
recs.sort(key=lambda r: r["nr"])
S = sum(r["stunden"] or 0 for r in recs); F = sum(r["foerderbetrag"] for r in recs); M = sum(r["masszahl"] for r in recs)
print(f"rows: {len(recs)} | Verwaltungseinheiten: {len(set(r['vid'] for r in recs))}")
print(f"sum Stunden {S:,.0f} vs printed 126,342 ({S/126342:.2%}) | sum Foerderbetrag {F:,.2f} vs printed 7,499,999.94 ({F/7499999.94:.2%}) | sum Masszahl {M:.4f}")
print("Art:", collections.Counter(r["art"] for r in recs).most_common())
print("angeleitet=Ja:", sum(1 for r in recs if r["angeleitet"] == "Ja"), "| rows with Stunden:", sum(1 for r in recs if r["stunden"]))
# facility dedupe: same municipality + same name stem (before ',' or ';' or ' Schwimmerbecken/Lehrschwimmbecken/Sportbecken')
def stem(n):
    n = re.split(r'[,;]', n)[0]
    n = re.sub(r'\s*(Schwimmerbecken|Lehrschwimmbecken|Lehrbecken|Sportbecken|Nichtschwimmerbecken|Außenbecken|Innenbecken|Hallenbad|Freibad)\s*$', '', n, flags=re.I)
    return n.strip().lower()
fac = collections.OrderedDict()
for r in recs:
    k = (r["vid"], stem(r["name"]) or r["name"].lower())
    fac.setdefault(k, []).append(r)
print(f"distinct facilities (municipality + name stem): {len(fac)}")
ind = {"Hallenbad","Kombibad","Lehrschwimmbecken","Freizeitbad","Erlebnisbad","Schwimmhalle","Therme","Sportbecken","Bewegungsbad"}
tab = collections.defaultdict(collections.Counter); fk = collections.Counter(); hk = collections.Counter()
for r in recs:
    tab[r["kreis"]]["indoor" if r["art"] in ind else "outdoor"] += 1; fk[r["kreis"]] += r["foerderbetrag"]; hk[r["kreis"]] += r["stunden"] or 0
print(f"\n  {'Kreis':26s} {'indoor':>7s} {'outdoor':>8s} {'rows':>5s} {'lesson h 2025':>14s} {'FAG EUR 2025':>13s}")
for k in sorted(tab, key=lambda k: -sum(tab[k].values())):
    c = tab[k]; print(f"  {k:26s} {c['indoor']:7d} {c['outdoor']:8d} {sum(c.values()):5d} {hk[k]:14,.0f} {fk[k]:13,.0f}")
c = collections.Counter(); [c.update(v) for v in tab.values()]
print(f"  {'TOTAL':26s} {c['indoor']:7d} {c['outdoor']:8d} {sum(c.values()):5d} {S:14,.0f} {F:13,.0f}")
print("\nlargest 12 funding units:")
for r in sorted(recs, key=lambda r: -r["foerderbetrag"])[:12]:
    print(f"  {r['foerderbetrag']:>12,.0f}  {r['stunden'] or 0:>7.0f} h  {r['name'][:46]:46s} {r['ort'][:16]:16s} {r['art']}")
with open("q02_fag2025_sh_pools.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(recs[0].keys())); w.writeheader(); w.writerows(recs)
print("\nsaved q02_fag2025_sh_pools.csv")
