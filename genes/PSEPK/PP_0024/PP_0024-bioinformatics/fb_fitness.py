"""Pull KT2440 (orgId Putida) Fitness Browser data for PP_0024 (EptA-like PEA transferase),
its neighbours and its COG2194 paralogs from BERDL kescience.fitnessbrowser (MCP REST query
endpoint; token from env KBASE_AUTH_TOKEN). Usage: python3 -I fb_fitness.py OUTDIR"""
import json, os, sys, urllib.request, urllib.error

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"


def q(sql):
    out, off = [], 0
    while True:
        req = urllib.request.Request(URL, data=json.dumps({"query": sql, "limit": 1000, "offset": off}).encode(),
                                     headers={"Authorization": "Bearer " + os.environ["KBASE_AUTH_TOKEN"],
                                              "Content-Type": "application/json", "User-Agent": "curl/8.5.0"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.load(r)
        except urllib.error.HTTPError as e:
            raise RuntimeError(sql + "\n" + e.read().decode()[:2000])
        if "result" not in d:
            raise RuntimeError(d)
        out += d["result"]
        if not d.get("pagination", {}).get("has_more"):
            return out
        off += 1000


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
res = {}
# neighbourhood PP_0019..PP_0030 and candidate paralogs by description
neigh = ["PP_%04d" % i for i in range(19, 31)]
res["neighbourhood_genes"] = q(f"""SELECT locusId, sysName, gene, "begin", "end", strand, "desc" FROM {DB}.gene
WHERE orgId='Putida' AND locusId IN ({','.join("'%s'" % g for g in neigh)}) ORDER BY CAST("begin" AS BIGINT)""")
res["paralog_candidates_by_desc"] = q(f"""SELECT locusId, sysName, gene, "desc" FROM {DB}.gene WHERE orgId='Putida' AND
(lower("desc") LIKE '%phosphoethanolamine%' OR lower("desc") LIKE '%metal-dependent hydrolase%' OR lower("desc") LIKE '%sulfatase%')""")
genes = sorted(set(neigh) | {"PP_4592"} | {r["locusId"] for r in res["paralog_candidates_by_desc"]})
inlist = ",".join("'%s'" % g for g in genes)
# one query per gene (<=1000 rows each, ORDER BY) - paging an unordered multi-gene join over offsets
# returned duplicated/missing rows
fit = []
for gname in genes:
    fit += q(f"""SELECT g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='Putida' AND g.locusid='{gname}' ORDER BY g.expname""")
json.dump(fit, open(os.path.join(out, "fitness_all.json"), "w"), indent=1)
by = {}
for r in fit:
    by.setdefault(r["locusid"], []).append(r)
summ = {}
for g, rows in by.items():
    rows.sort(key=lambda r: r["fit"])
    strong = [r for r in rows if abs(r["fit"]) >= 1 and abs(r["t"]) >= 4]
    summ[g] = {"n_experiments": len(rows), "n_abs_fit_ge1_and_abs_t_ge4": len(strong),
               "strong": [{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")} for r in strong],
               "n_distinct_experiments": len({r["expname"] for r in rows}),
               "min_fit": rows[0]["fit"], "max_fit": rows[-1]["fit"]}
res["per_gene_summary"] = summ
# all PP_0024 values in cationic / metal / membrane-stress experiments
kw = ["polymyxin", "colistin", "alumin", "zinc", "cadmium", "iron", "manganese", "cobalt", "copper", "nickel",
      "deoxycholate", "bile", "sds", "lactoferrin", "edta", "phenol", "chloride", "ferric", "lauryl"]
res["PP_0024_selected_conditions"] = sorted([{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")}
    for r in by.get("PP_0024", []) if any(k in (r["expdesc"] or "").lower() for k in kw)], key=lambda r: r["fit"])
res["PP_4592_selected_conditions"] = sorted([{k: r[k] for k in ("expname", "expdesc", "expgroup", "fit", "t")}
    for r in by.get("PP_4592", []) if any(k in (r["expdesc"] or "").lower() for k in kw)], key=lambda r: r["fit"])
res["PP_0024_all_sorted"] = [{k: r[k] for k in ("expname", "expdesc", "fit", "t")} for r in by.get("PP_0024", [])]
res["specificphenotype"] = q(f"""SELECT s.locusid, s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='Putida' AND s.locusid IN ({inlist})""")
res["cofit_PP_0024"] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g."desc" FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='Putida' AND c.locusid='PP_0024' ORDER BY CAST(c.rank AS INT) LIMIT 20""")
# experiment list for the conditions of interest (does KT2440 have polymyxin/Al/Zn experiments at all?)
res["putida_experiments_of_interest"] = q(f"""SELECT expname, expdesc, expgroup FROM {DB}.experiment WHERE orgid='Putida' AND
(lower(expdesc) LIKE '%polymyxin%' OR lower(expdesc) LIKE '%colistin%' OR lower(expdesc) LIKE '%alumin%' OR lower(expdesc) LIKE '%zinc%')""")
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps({g: {k: v for k, v in s.items() if k != "strong"} for g, s in summ.items()}, indent=1))
print(json.dumps(res["neighbourhood_genes"], indent=0))
print(json.dumps(res["paralog_candidates_by_desc"], indent=0))
