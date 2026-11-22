"""DvH (Fitness Browser orgId 'DvH') RB-TnSeq data for DVU1219 (locusId 206658) from BERDL
kescience.fitnessbrowser via the BERDL MCP REST query endpoint. Token from env KBASE_AUTH_TOKEN.

Questions:
  1. Which experiments give DVU1219 strong phenotypes (|fit| >= 1 and |t| >= 4), and how many
     experiments were run? Is the phenotype broad (many conditions) or condition-specific?
  2. Specific-phenotype calls (FB 'specificphenotype' table).
  3. Top cofitness partners (what pathway/module DVU1219 travels with).
  4. In the tungstate and molybdate experiments, how many genes have strong phenotypes, and
     where does DVU1219 rank? Which genes are the top hits there?
  5. Fitness of the genomic neighbours DVU1210-DVU1228.
  6. Orthologues in other Fitness Browser organisms and their strongest phenotypes.

Usage: python3 -I fb_fitness.py OUTDIR
"""
import json
import os
import sys
import urllib.error
import urllib.request

URL = "https://hub.berdl.kbase.us/apis/mcp/delta/tables/query"
DB = "kescience.fitnessbrowser"
ORG = "DvH"
LOCUS = "206658"  # DVU1219


def q(sql):
    import time
    t0 = time.time()
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
            raise RuntimeError(sql + "\n" + json.dumps(d)[:2000])
        out += d["result"]
        if not d.get("pagination", {}).get("has_more"):
            print(f"[q {time.time() - t0:.1f}s, {len(out)} rows] {' '.join(sql.split())[:90]}", file=sys.stderr, flush=True)
            return out
        off += 1000


def strong(r):
    return abs(r["fit"]) >= 1 and abs(r["t"]) >= 4


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    res = {}
    # Joins are slow on the endpoint, so tables are fetched separately and joined here.
    exp = {e["expname"]: e for e in q(f"""SELECT expname, expdesc, expgroup, condition_1, media FROM {DB}.experiment
WHERE orgid='{ORG}' ORDER BY expname""")}
    gene_tab = {g["locusid"]: g for g in q(f"""SELECT locusid, sysname, gene, "desc" FROM {DB}.gene WHERE orgid='{ORG}'
ORDER BY locusid""")}

    def annot(rows):
        for r in rows:
            for k in ("expdesc", "expgroup", "condition_1", "media"):
                if "expname" in r and r["expname"] in exp:
                    r[k] = exp[r["expname"]][k]
            g = gene_tab.get(r.get("locusid") or r.get("hitid"), {})
            r["sysname"], r["desc"] = g.get("sysname"), g.get("desc")
        return rows

    fit = annot(q(f"""SELECT locusid, expname, CAST(fit AS DOUBLE) fit, CAST(t AS DOUBLE) t FROM {DB}.genefitness
WHERE orgid='{ORG}' AND locusid='{LOCUS}' ORDER BY expname"""))
    fit.sort(key=lambda r: r["fit"])
    n = len(fit)
    st = [r for r in fit if strong(r)]
    by_group = {}
    for r in fit:
        g = by_group.setdefault(r["expgroup"], {"n": 0, "n_strong_neg": 0, "n_strong_pos": 0})
        g["n"] += 1
        if strong(r):
            g["n_strong_neg" if r["fit"] < 0 else "n_strong_pos"] += 1
    # condition keyword tallies among strong phenotypes
    kw = {}
    for word in ["tungstate", "molybdate", "nitrate", "sulfite", "n2 gas", "serine", "valine", "urea", "fccp",
                 "ammonium", "lactate", "pyruvate", "formate", "chloride", "peroxide", "oxygen", "nitrite"]:
        rows = [r for r in fit if word in (r["expdesc"] or "").lower()]
        kw[word] = {"n_exps": len(rows), "n_strong": sum(strong(r) for r in rows),
                    "fits": sorted(round(r["fit"], 2) for r in rows)}
    res["DVU1219"] = {"n_experiments": n, "n_strong": len(st), "n_strong_neg": sum(r["fit"] < 0 for r in st),
                      "n_strong_pos": sum(r["fit"] > 0 for r in st), "min_fit": fit[0]["fit"],
                      "max_fit": fit[-1]["fit"], "by_expgroup": by_group, "keyword_tally": kw,
                      "strong_rows": st}
    json.dump(fit, open(os.path.join(out, "dvu1219_all_fitness.json"), "w"), indent=1)
    res["specificphenotype"] = annot(q(f"""SELECT locusid, expname FROM {DB}.specificphenotype
WHERE orgid='{ORG}' AND locusid='{LOCUS}' ORDER BY expname"""))
    cof = q(f"""SELECT hitid, CAST(rank AS INT) rank, CAST(cofit AS DOUBLE) cofit FROM {DB}.cofit
WHERE orgid='{ORG}' AND locusid='{LOCUS}' ORDER BY CAST(rank AS INT) LIMIT 30""")
    for r in cof:
        g = gene_tab.get(r["hitid"], {})
        r["sysname"], r["desc"] = g.get("sysname"), g.get("desc")
    res["cofit_top30"] = cof
    # genome-wide context of the tungstate / molybdate experiments
    ctx = {}
    exps = sorted({r["expname"] for r in fit if any(w in (r["expdesc"] or "").lower() for w in ("tungstate", "molybdate"))})
    for ex in exps:
        allrows = q(f"""SELECT locusid, CAST(fit AS DOUBLE) fit, CAST(t AS DOUBLE) t FROM {DB}.genefitness
WHERE orgid='{ORG}' AND expname='{ex}' ORDER BY locusid""")
        rows = sorted([r for r in allrows if strong(r)], key=lambda r: r["fit"])
        for r in rows:
            g = gene_tab.get(r["locusid"], {})
            r["sysname"], r["desc"] = g.get("sysname"), g.get("desc")
        me = [r for r in fit if r["expname"] == ex][0]
        neg = [r for r in rows if r["fit"] < 0]
        pos = sorted([r for r in rows if r["fit"] > 0], key=lambda r: -r["fit"])
        side = neg if me["fit"] < 0 else pos
        loci = [r["locusid"] for r in side]
        ctx[ex] = {"expdesc": me["expdesc"], "DVU1219_fit": me["fit"], "DVU1219_t": me["t"],
                   "n_genes_measured": len(allrows), "n_strong_neg": len(neg), "n_strong_pos": len(pos),
                   "DVU1219_rank_on_its_side": (1 + loci.index(LOCUS)) if LOCUS in loci else None,
                   "top15_same_side": side[:15]}
    res["metal_experiment_context"] = ctx
    # neighbours
    nb = [f"DVU{i}" for i in range(1210, 1229)]
    inl = ",".join(f"'{x}'" for x in nb)
    genes = [{k: g[k] for k in ("locusid", "sysname", "gene", "desc")} for g in gene_tab.values() if g["sysname"] in nb]
    genes.sort(key=lambda g: g["sysname"])
    ids = ",".join(f"'{g['locusid']}'" for g in genes)
    nfit = q(f"""SELECT locusid, expname, CAST(fit AS DOUBLE) fit, CAST(t AS DOUBLE) t FROM {DB}.genefitness
WHERE orgid='{ORG}' AND locusid IN ({ids}) ORDER BY locusid, expname""")
    me_by_exp = {r["expname"]: r["fit"] for r in fit}
    import statistics
    nsum = []
    for g in genes:
        rows = [r for r in nfit if r["locusid"] == g["locusid"]]
        if not rows:
            nsum.append({**g, "n": 0})
            continue
        xs = [me_by_exp[r["expname"]] for r in rows if r["expname"] in me_by_exp]
        ys = [r["fit"] for r in rows if r["expname"] in me_by_exp]
        corr = statistics.correlation(xs, ys) if len(xs) > 2 else None
        nsum.append({**g, "n": len(rows), "n_strong": sum(strong(r) for r in rows),
                     "min_fit": min(r["fit"] for r in rows), "max_fit": max(r["fit"] for r in rows),
                     "pearson_with_DVU1219": corr})
    res["neighbours"] = nsum
    # orthologues in other FB organisms
    orth = q(f"""SELECT orgid2, locusid2, CAST(ratio AS DOUBLE) ratio FROM {DB}.ortholog
WHERE orgid1='{ORG}' AND locusid1='{LOCUS}' ORDER BY orgid2""")
    for o in orth:
        gi = q(f"""SELECT sysname, "desc" FROM {DB}.gene WHERE orgid='{o['orgid2']}' AND locusid='{o['locusid2']}'""")
        o["sysname"], o["desc"] = (gi[0]["sysname"], gi[0]["desc"]) if gi else (None, None)
        ex2 = {e["expname"]: e["expdesc"] for e in q(f"""SELECT expname, expdesc FROM {DB}.experiment
WHERE orgid='{o['orgid2']}' ORDER BY expname""")}
        rows = q(f"""SELECT expname, CAST(fit AS DOUBLE) fit, CAST(t AS DOUBLE) t FROM {DB}.genefitness
WHERE orgid='{o['orgid2']}' AND locusid='{o['locusid2']}' ORDER BY expname""")
        for r in rows:
            r["expdesc"] = ex2.get(r["expname"])
        rows.sort(key=lambda r: r["fit"])
        o["n_experiments"] = len(rows)
        o["n_strong"] = sum(strong(r) for r in rows)
        o["strongest5_neg"] = rows[:5]
        o["strongest3_pos"] = rows[-3:][::-1]
    res["orthologs"] = orth
    json.dump(res, open(os.path.join(out, "fitness_results.json"), "w"), indent=1, default=str)
    d = res["DVU1219"]
    print(f"DVU1219: {d['n_experiments']} experiments; strong {d['n_strong']} (neg {d['n_strong_neg']}, pos {d['n_strong_pos']}); "
          f"min {d['min_fit']:.2f} max {d['max_fit']:.2f}")
    print("by expgroup:", json.dumps(by_group))
    for k, v in kw.items():
        if v["n_exps"]:
            print(f"  {k}: {v['n_strong']}/{v['n_exps']} strong; fits {v['fits']}")
    print("specific phenotypes:", [(r["expname"], r["expdesc"]) for r in res["specificphenotype"]])
    print("cofit top30:")
    for r in res["cofit_top30"]:
        print(f"  {r['rank']:>3} {r['cofit']:.2f} {r['sysname']} {r['desc']}")
    print("metal experiments:")
    for ex, c in ctx.items():
        print(f"  {ex} {c['expdesc']}: DVU1219 fit {c['DVU1219_fit']:.2f} t {c['DVU1219_t']:.1f}; strong neg {c['n_strong_neg']} pos {c['n_strong_pos']}; rank {c['DVU1219_rank_on_its_side']}")
        print("     top:", "; ".join(f"{r['sysname']}({r['fit']:.1f}) {(r['desc'] or '')[:40]}" for r in c["top15_same_side"][:10]))
    print("neighbours:")
    for g in nsum:
        print("  ", {k: (round(v, 2) if isinstance(v, float) else v) for k, v in g.items()})
    print("orthologs:")
    for o in orth:
        print(f"  {o['orgid2']} {o['sysname']} ratio {o['ratio']:.2f} {o['desc']} n={o['n_experiments']} strong={o['n_strong']}")
        for r in o["strongest5_neg"][:3] + o["strongest3_pos"][:2]:
            print(f"      {r['fit']:.2f} t={r['t']:.1f} {r['expdesc']}")


if __name__ == "__main__":
    main()
