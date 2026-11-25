"""Pull KT2440 (orgId Putida) Fitness Browser data for the PP_4570-PP_4580 locus (PP_4572 DUF748,
PP_4575 PxpC-like, PP_4576 PxpB-like, PP_4577 PxpA2), cofitness partners of PP_4572 and PP_4575,
the genome-wide context of the L-pyroglutamate and urea experiments, and the other KT2440
PxpA/B/C-family genes, from BERDL (kescience.fitnessbrowser via the BERDL MCP REST query
endpoint). Token from env KBASE_AUTH_TOKEN.
Usage: python3 -I fb_fitness.py OUTDIR"""
import json, os, sys, urllib.request, urllib.error

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"
ORG = "Putida"
FOCAL = ["PP_4572", "PP_4575"]


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
genes = ["PP_%04d" % i for i in range(4568, 4582)]
inlist = ",".join("'%s'" % g for g in genes)
res = {}
res["genes"] = q(f"SELECT * FROM {DB}.gene WHERE orgId='{ORG}' AND locusId IN ({inlist})")
# other PxpA (LamB/UPF0271), PxpB/PxpC (allophanate hydrolase subunit) and urea carboxylase genes in KT2440
res["family_genes"] = q(f"""SELECT locusid, sysname, "desc" FROM {DB}.gene WHERE orgid='{ORG}' AND (
 lower("desc") LIKE '%allophanate%' OR lower("desc") LIKE '%oxoprolinase%' OR lower("desc") LIKE '%lamb%'
 OR lower("desc") LIKE '%upf0271%' OR lower("desc") LIKE '%urea%' OR lower("desc") LIKE '%carboxyltransferase%'
 OR lower("desc") LIKE '%kipi%' OR lower("desc") LIKE '%kipa%' OR lower("desc") LIKE '%amidolyase%'
 OR lower("desc") LIKE '%asma%' OR lower("desc") LIKE '%duf748%')""")
fam = sorted({r["locusid"] for r in res["family_genes"]} | set(genes))
famlist = ",".join("'%s'" % g for g in fam)
fit = q(f"""SELECT g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup, e.condition_1
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='{ORG}' AND g.locusid IN ({famlist}) ORDER BY g.locusid, g.expname""")
res["n_unique_experiments_per_locus"] = {g: len({r["expname"] for r in fit if r["locusid"] == g}) for g in fam}
json.dump(fit, open(os.path.join(out, "fitness_locus_and_family.json"), "w"), indent=1)
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
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='{ORG}' AND s.locusid IN ({famlist}) ORDER BY s.locusid, s.expname""")
res["cofit_top20"] = {}
for gene in FOCAL:
    res["cofit_top20"][gene] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g.sysname, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='{ORG}' AND c.locusid='{gene}' ORDER BY CAST(c.rank AS INT) LIMIT 20""")
exps = q(f"""SELECT expname, expdesc, expgroup, condition_1 FROM {DB}.experiment WHERE orgid='{ORG}'
AND (lower(expdesc) LIKE '%pyroglut%' OR lower(condition_1) LIKE '%pyroglut%' OR lower(expdesc) LIKE '%oxoprol%'
 OR lower(expdesc) LIKE '%urea%' OR lower(expdesc) LIKE '%proline%' OR lower(expdesc) LIKE '%glutam%')""")
res["selected_experiments"] = exps
ctx = {}
for e in exps:
    ex = e["expname"]
    rows = q(f"""SELECT g.locusid, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, ge.sysname, ge."desc" FROM {DB}.genefitness g
JOIN {DB}.gene ge ON ge.orgid=g.orgid AND ge.locusid=g.locusid
WHERE g.orgid='{ORG}' AND g.expname='{ex}' AND CAST(g.fit AS DOUBLE) <= -1 AND CAST(g.t AS DOUBLE) <= -4 ORDER BY CAST(g.fit AS DOUBLE), g.locusid""")
    loci = [r["locusid"] for r in rows]
    ctx[ex] = {"expdesc": e["expdesc"], "expgroup": e["expgroup"], "n_genes_fit_le_m1_t_le_m4": len(rows),
               "rank_among_strong": {g: (1 + loci.index(g)) if g in loci else None for g in genes},
               "locus_values": [r for r in fit if r["expname"] == ex and r["locusid"] in genes],
               "top25": rows[:25]}
res["experiment_context"] = ctx
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps([{k: r[k] for k in ("locusId", "sysName", "desc") if k in r} for r in res["genes"]], indent=0)[:3000])
print(json.dumps({g: {k: v for k, v in s.items() if k not in ("strong",)} for g, s in summ.items()}, indent=1)[:8000])
