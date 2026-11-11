"""Pull KT2440 (orgId Putida) Fitness Browser data for PP_3231 and neighbours from BERDL
(kescience.fitnessbrowser via the BERDL MCP REST query endpoint). Token from env KBASE_AUTH_TOKEN.
Usage: python3 -I fb_fitness.py OUTDIR"""
import json, os, sys, urllib.request, urllib.error

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"


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


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
genes = ["PP_3228", "PP_3229", "PP_3230", "PP_3231", "PP_3232", "PP_3233"]
inlist = ",".join("'%s'" % g for g in genes)
res = {}
res["genes"] = q(f"SELECT * FROM {DB}.gene WHERE orgId='Putida' AND locusId IN ({inlist})")
fit = q(f"""SELECT g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='Putida' AND g.locusid IN ({inlist})""")
json.dump(fit, open(os.path.join(out, "fitness_all.json"), "w"), indent=1)
by = {}
for r in fit:
    by.setdefault(r["locusid"], []).append(r)
summ = {}
for g, rows in by.items():
    rows.sort(key=lambda r: r["fit"])
    strong = [r for r in rows if abs(r["fit"]) >= 1 and abs(r["t"]) >= 4]
    summ[g] = {"n_experiments": len(rows),
               "n_abs_fit_ge1_and_abs_t_ge4": len(strong),
               "strong": [{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")} for r in sorted(strong, key=lambda r: -r["fit"])],
               "min_fit": rows[0]["fit"], "max_fit": rows[-1]["fit"]}
res["per_gene_summary"] = summ
# Specific phenotypes
res["specificphenotype"] = q(f"""SELECT s.locusid, s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='Putida' AND s.locusid IN ({inlist})""")
# Cofitness partners of PP_3231
res["cofit_PP_3231"] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='Putida' AND c.locusid='PP_3231' ORDER BY CAST(c.rank AS INT) LIMIT 20""")
res["cofit_PP_3230"] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='Putida' AND c.locusid='PP_3230' ORDER BY CAST(c.rank AS INT) LIMIT 10""")
# How unusual are these positive scores? Genome-wide counts per experiment of strong positive genes
pos_exps = sorted({r["expname"] for r in by.get("PP_3231", []) if abs(r["fit"]) >= 1 and abs(r["t"]) >= 4})
ctx = {}
for ex in pos_exps:
    rows = q(f"""SELECT g.locusid, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, ge."desc" FROM {DB}.genefitness g
JOIN {DB}.gene ge ON ge.orgid=g.orgid AND ge.locusid=g.locusid
WHERE g.orgid='Putida' AND g.expname='{ex}' AND ABS(CAST(g.fit AS DOUBLE)) >= 1 AND ABS(CAST(g.t AS DOUBLE)) >= 4 ORDER BY CAST(g.fit AS DOUBLE) DESC""")
    n = q(f"SELECT count(*) n FROM {DB}.genefitness WHERE orgid='Putida' AND expname='{ex}'")[0]["n"]
    ctx[ex] = {"n_genes_measured": n, "n_genes_fit_ge1_t_ge4": len(rows), "top": rows[:15]}
res["positive_experiment_context"] = ctx
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps({g: {k: v for k, v in s.items() if k != "strong"} for g, s in summ.items()}, indent=1))
