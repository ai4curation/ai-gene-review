"""Pull KT2440 (orgId Putida) Fitness Browser data for PP_4704 (DUF748/AsmA-like), its neighbours,
its top cofitness partners, and the other KT2440 AsmA-like (PTHR30441/DUF748/TamB) genes, from the
BERDL lakehouse (kescience.fitnessbrowser via the BERDL MCP REST endpoint). Token: env KBASE_AUTH_TOKEN.
Usage: python3 -I fb_fitness.py OUTDIR"""
import json, os, sys, urllib.request, urllib.error

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"
ORG = "Putida"
GENE = "PP_4704"


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


def q(sql):
    out, off = [], 0
    while True:
        d = q1(sql, off)
        out += d["result"]
        if not d.get("pagination", {}).get("has_more"):
            return out
        off += 1000


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
res = {}
# AsmA-like / DUF748 / TamB-like genes in KT2440 by description
res["asma_like_genes"] = q(f"""SELECT locusid, sysname, "desc" FROM {DB}.gene WHERE orgid='{ORG}' AND
 (lower("desc") LIKE '%asma%' OR lower("desc") LIKE '%duf748%' OR lower("desc") LIKE '%tamb%' OR lower("desc") LIKE '%duf490%'
  OR lower("desc") LIKE '%yhdp%' OR lower("desc") LIKE '%translocation and assembly%' OR lower("desc") LIKE '%duf3971%')""")
genes = ["PP_4700", "PP_4701", "PP_4702", "PP_4703", "PP_4704", "PP_4705", "PP_4706", "PP_4707", "PP_4708"]
genes += [g["locusid"] for g in res["asma_like_genes"] if g["locusid"] not in genes]
inlist = ",".join("'%s'" % g for g in genes)
res["genes"] = q(f"SELECT * FROM {DB}.gene WHERE orgId='{ORG}' AND locusId IN ({inlist})")
fit = q(f"""SELECT g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup, e.condition_1
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='{ORG}' AND g.locusid IN ({inlist})""")
json.dump(fit, open(os.path.join(out, "fitness_rows.json"), "w"), indent=1)
res["n_experiments_org"] = q(f"SELECT count(*) n FROM {DB}.experiment WHERE orgid='{ORG}'")[0]["n"]
by = {}
for r in fit:
    by.setdefault(r["locusid"], []).append(r)
summ = {}
for g in genes:
    rows = sorted(by.get(g, []), key=lambda r: r["fit"])
    if not rows:
        summ[g] = {"n_experiments": 0}
        continue
    strong = [r for r in rows if abs(r["fit"]) >= 1 and abs(r["t"]) >= 4]
    summ[g] = {"n_experiments": len(rows),
               "n_abs_fit_ge1_and_abs_t_ge4": len(strong),
               "n_fit_le_m1_t_le_m4": sum(1 for r in strong if r["fit"] < 0),
               "strong": [{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")} for r in strong],
               "lowest5": [{k: r[k] for k in ("expname", "expdesc", "fit", "t")} for r in rows[:5]],
               "highest3": [{k: r[k] for k in ("expname", "expdesc", "fit", "t")} for r in rows[-3:]],
               "min_fit": rows[0]["fit"], "max_fit": rows[-1]["fit"],
               "mean_fit": sum(r["fit"] for r in rows) / len(rows)}
res["per_gene_summary"] = summ
res["specificphenotype"] = q(f"""SELECT s.locusid, s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='{ORG}' AND s.locusid IN ({inlist})""")
res["cofit_top20"] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g.sysname, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='{ORG}' AND c.locusid='{GENE}' ORDER BY CAST(c.rank AS INT) LIMIT 20""")
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps(res["asma_like_genes"], indent=1))
print(json.dumps({g: {k: v for k, v in s.items() if k != "strong"} for g, s in summ.items()}, indent=1)[:8000])
print(json.dumps(res["specificphenotype"], indent=1)[:2000])
print(json.dumps(res["cofit_top20"], indent=1)[:4000])
