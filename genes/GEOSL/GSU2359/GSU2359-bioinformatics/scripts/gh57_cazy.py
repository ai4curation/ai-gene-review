"""CAZy GH57 subfamily placement of GSU2359, A2cp1_1916, DVU_2472 and the activities of
characterized GH57 members (www.cazy.org GH57_characterized.html and GH57_bacteria.html).
Tests: which GH57 subfamily (Polacek et al. 2025, PMID:40187459) contains the queries; which
characterized enzymes share it; whether any characterized GH57 member is an alpha-mannosidase
(EC 3.2.1.24 / 3.2.1.113 / 3.2.1.114 / 3.2.1.170) or acts on trehalose-related substrates.
Writes $BERIL_RUN_DIR/results.json and characterized.tsv."""
import html, json, os, re, collections, urllib.request
OUT = os.environ.get("BERIL_RUN_DIR", "/tmp/gh57_cazy")
def page(u):
    with urllib.request.urlopen(u, timeout=300) as r: return r.read().decode("latin1")
def rows(s):
    out = []
    for r in re.split(r"<tr", s):
        t = html.unescape(re.sub(r"<[^>]+>", "|", r)); t = re.sub(r"(\s*\|\s*)+", "|", t).strip("|")
        f = [x for x in t.split("|") if x and not x.startswith(" valign") and "onmouseover" not in x]
        if len(f) >= 3: out.append((f, r))
    return out
char = page("http://www.cazy.org/GH57_characterized.html")
crow = []
for f, raw in rows(char):
    if f[-1].isdigit() and len(f[-1]) <= 2 and len(f) > 3:
        ecs = re.findall(r"\b\d+\.\d+\.\d+\.\d+\b", " ".join(f))
        crow.append({"name": f[0], "ec": sorted(set(ecs)), "subfamily": f[-1], "fields": f})
with open(os.path.join(OUT, "characterized.tsv"), "w") as fh:
    fh.write("name\tec\tsubfamily\n")
    for c in crow: fh.write(f"{c['name']}\t{','.join(c['ec'])}\t{c['subfamily']}\n")
bac = page("http://www.cazy.org/GH57_bacteria.html")
QUERY = {"AAR35733": "GSU2359", "ACL65258": "A2cp1_1916", "AAS96944": "DVU_2472"}
place, sub_counts = {}, collections.Counter()
for f, raw in rows(bac):
    if f[-1].isdigit() and len(f[-1]) <= 2: sub_counts[f[-1]] += 1
    for k, v in QUERY.items():
        if k in raw: place[v] = {"fields": f, "subfamily": f[-1]}
MANNO = {"3.2.1.24", "3.2.1.113", "3.2.1.114", "3.2.1.170"}
res = {"query_subfamily": place,
       "bacterial_entries_per_subfamily": dict(sub_counts),
       "n_characterized": len(crow),
       "characterized_ecs": dict(collections.Counter(e for c in crow for e in c["ec"])),
       "characterized_alpha_mannosidase": [c["name"] for c in crow if MANNO & set(c["ec"])],
       "characterized_mentioning_trehalose_or_mannos": [c["name"] for c in crow if re.search("trehal|mannos", " ".join(c["fields"]), re.I)],
       "characterized_in_query_subfamilies": [{"name": c["name"], "ec": c["ec"], "subfamily": c["subfamily"]}
                                              for c in crow if c["subfamily"] in {p["subfamily"] for p in place.values()}]}
json.dump(res, open(os.path.join(OUT, "results.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
