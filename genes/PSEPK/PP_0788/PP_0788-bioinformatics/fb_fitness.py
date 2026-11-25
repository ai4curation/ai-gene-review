"""Pull Fitness Browser data for KT2440 PP_0788 (orgId Putida), its neighbours, and its
orthologs in other FB organisms (incl. P. simiae WCS417) from BERDL kescience.fitnessbrowser
via the BERDL MCP REST query endpoint. Token from env KBASE_AUTH_TOKEN.
Adapted from genes/PSEPK/yedI/yedI-bioinformatics/fb_fitness.py.
Usage: python3 -I fb_fitness.py OUTDIR"""
import json, os, sys, urllib.request, urllib.error

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"
ORG, TARGET = "Putida", "PP_0788"


def q(sql):
    out, off = [], 0
    while True:
        d = q1(sql, off)
        out += d["result"]
        if not d.get("pagination", {}).get("has_more"):
            return out
        off += 1000


def q1(sql, offset):
    req = urllib.request.Request(URL, data=json.dumps({"query": sql, "limit": 1000, "offset": offset}).encode(),
                                 headers={"Authorization": "Bearer " + os.environ["KBASE_AUTH_TOKEN"],
                                          "Content-Type": "application/json", "User-Agent": "curl/8.5.0"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(sql + "\n" + e.read().decode()[:2000])
    if "result" not in d:
        raise RuntimeError(d)
    return d


def fitness(org, loci):
    inlist = ",".join("'%s'" % g for g in loci)
    return q(f"""SELECT g.orgid, g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='{org}' AND g.locusid IN ({inlist})""")


def summarise(rows):
    rows = sorted(rows, key=lambda r: r["fit"])
    strong = [r for r in rows if abs(r["fit"]) >= 1 and abs(r["t"]) >= 4]
    groups = {}
    for r in strong:
        groups[r["expgroup"]] = groups.get(r["expgroup"], 0) + 1
    return {"n_experiments": len(rows), "n_abs_fit_ge1_and_abs_t_ge4": len(strong),
            "strong_by_expgroup": groups,
            "strong": [{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")} for r in strong],
            "min_fit": rows[0]["fit"] if rows else None, "max_fit": rows[-1]["fit"] if rows else None,
            "lowest10": [{k: r[k] for k in ("expdesc", "expgroup", "fit", "t")} for r in rows[:10]],
            "highest5": [{k: r[k] for k in ("expdesc", "expgroup", "fit", "t")} for r in rows[-5:]]}


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
res = {"target": TARGET, "org": ORG}
genes = ["PP_%04d" % i for i in range(784, 794)]
inlist = ",".join("'%s'" % g for g in genes)
res["genes"] = q(f"SELECT * FROM {DB}.gene WHERE orgId='{ORG}' AND locusId IN ({inlist}) ORDER BY CAST(begin AS INT)")
fit = fitness(ORG, genes)
json.dump(fit, open(os.path.join(out, "fitness_putida_neighbours.json"), "w"), indent=1)
by = {}
for r in fit:
    by.setdefault(r["locusid"], []).append(r)
res["per_gene_summary"] = {g: summarise(rows) for g, rows in sorted(by.items())}
res["specificphenotype"] = q(f"""SELECT s.orgid, s.locusid, s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='{ORG}' AND s.locusid IN ({inlist})""")
res["cofit_" + TARGET] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='{ORG}' AND c.locusid='{TARGET}' ORDER BY CAST(c.rank AS INT) LIMIT 20""")
# orthologs (BBH) of PP_0788 in other FB organisms
orth = q(f"""SELECT o.orgid2, o.locusid2, CAST(o.ratio AS DOUBLE) ratio, g."desc" FROM {DB}.ortholog o
JOIN {DB}.gene g ON g.orgid=o.orgid2 AND g.locusid=o.locusid2 WHERE o.orgid1='{ORG}' AND o.locusid1='{TARGET}'""")
res["orthologs"] = orth
res["ortholog_fitness_summary"] = {}
for o in orth:
    rows = fitness(o["orgid2"], [o["locusid2"]])
    s = summarise(rows)
    s["specificphenotype"] = q(f"""SELECT s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='{o["orgid2"]}' AND s.locusid='{o["locusid2"]}'""")
    res["ortholog_fitness_summary"][o["orgid2"] + ":" + o["locusid2"]] = s
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps({"putida": {g: {k: v for k, v in s.items() if k in ("n_experiments", "n_abs_fit_ge1_and_abs_t_ge4", "strong_by_expgroup", "min_fit", "max_fit")}
                             for g, s in res["per_gene_summary"].items()},
                  "orthologs": {k: {kk: vv for kk, vv in s.items() if kk in ("n_experiments", "n_abs_fit_ge1_and_abs_t_ge4", "strong_by_expgroup", "min_fit", "max_fit")}
                                for k, s in res["ortholog_fitness_summary"].items()}}, indent=1))
