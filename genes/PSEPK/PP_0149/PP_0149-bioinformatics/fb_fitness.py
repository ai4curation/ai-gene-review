"""Pull KT2440 (orgId Putida) Fitness Browser data for PP_0149, its neighbours, cofitness partners,
and the genome-wide context of quaternary-ammonium (QAC) experiments from BERDL
(kescience.fitnessbrowser via the BERDL MCP REST query endpoint). Token from env KBASE_AUTH_TOKEN.
Usage: python3 -I fb_fitness.py OUTDIR"""
import json, os, sys, urllib.request, urllib.error

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"
ORG = "Putida"
GENE = "PP_0149"


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
genes = ["PP_0145", "PP_0146", "PP_0147", "PP_0148", "PP_0149", "PP_0150", "PP_0151", "PP_0152", "PP_0153"]
inlist = ",".join("'%s'" % g for g in genes)
res = {}
res["genes"] = q(f"SELECT * FROM {DB}.gene WHERE orgId='{ORG}' AND locusId IN ({inlist})")
fit = q(f"""SELECT g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup, e.condition_1
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='{ORG}' AND g.locusid IN ({inlist})""")
json.dump(fit, open(os.path.join(out, "fitness_neighbourhood.json"), "w"), indent=1)
by = {}
for r in fit:
    by.setdefault(r["locusid"], []).append(r)
summ = {}
for g, rows in by.items():
    rows.sort(key=lambda r: r["fit"])
    strong = [r for r in rows if abs(r["fit"]) >= 1 and abs(r["t"]) >= 4]
    summ[g] = {"n_experiments": len(rows),
               "n_abs_fit_ge1_and_abs_t_ge4": len(strong),
               "strong": [{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")} for r in strong],
               "lowest5": [{k: r[k] for k in ("expname", "expdesc", "fit", "t")} for r in rows[:5]],
               "min_fit": rows[0]["fit"], "max_fit": rows[-1]["fit"]}
res["per_gene_summary"] = summ
res["specificphenotype"] = q(f"""SELECT s.locusid, s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='{ORG}' AND s.locusid IN ({inlist})""")
res["cofit_top20"] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g.sysname, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='{ORG}' AND c.locusid='{GENE}' ORDER BY CAST(c.rank AS INT) LIMIT 20""")
# QAC experiments in KT2440, and genome-wide context of each
qac = q(f"""SELECT expname, expdesc, expgroup, condition_1 FROM {DB}.experiment WHERE orgid='{ORG}'
AND (lower(expdesc) LIKE '%benz%onium%' OR lower(condition_1) LIKE '%benz%onium%' OR lower(expdesc) LIKE '%cetyl%' OR lower(expdesc) LIKE '%ammonium bromide%')""")
res["qac_experiments"] = qac
ctx = {}
for e in qac:
    ex = e["expname"]
    rows = q(f"""SELECT g.locusid, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, ge.sysname, ge."desc" FROM {DB}.genefitness g
JOIN {DB}.gene ge ON ge.orgid=g.orgid AND ge.locusid=g.locusid
WHERE g.orgid='{ORG}' AND g.expname='{ex}' AND CAST(g.fit AS DOUBLE) <= -1 AND CAST(g.t AS DOUBLE) <= -4 ORDER BY CAST(g.fit AS DOUBLE)""")
    n = q(f"SELECT count(*) n FROM {DB}.genefitness WHERE orgid='{ORG}' AND expname='{ex}'")[0]["n"]
    loci = [r["locusid"] for r in rows]
    ctx[ex] = {"expdesc": e["expdesc"], "n_genes_measured": n, "n_genes_fit_le_m1_t_le_m4": len(rows),
               "PP_0149_rank_among_strong": (1 + loci.index(GENE)) if GENE in loci else None,
               "PP_0149": [r for r in fit if r["locusid"] == GENE and r["expname"] == ex],
               "top25": rows[:25]}
res["qac_experiment_context"] = ctx
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps({g: {k: v for k, v in s.items() if k not in ("strong",)} for g, s in summ.items()}, indent=1)[:6000])
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "top25"} for k, v in ctx.items()}, indent=1)[:4000])
