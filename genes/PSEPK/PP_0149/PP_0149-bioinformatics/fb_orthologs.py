"""PP_0149 Fitness Browser orthologs (kescience.fitnessbrowser.ortholog, via BERDL REST): per-ortholog
phenotype summary, quaternary-ammonium (QAC) experiment context (how many genes are strongly
sick, the ortholog's rank), specificphenotype calls, cofitness partners and conserved cofitness;
also the orthologs of the operon partner PP_0150.
Usage: python3 -I fb_orthologs.py OUTDIR"""
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
        out += d["result"]
        if not d.get("pagination", {}).get("has_more"):
            return out
        off += 1000


QAC = "(lower(e.expdesc) LIKE '%benz%onium%' OR lower(e.expdesc) LIKE '%cetyl%' OR lower(e.expdesc) LIKE '%cetrimonium%' OR lower(e.expdesc) LIKE '%ammonium bromide%')"
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
orth = q(f"SELECT orgid2, locusid2, CAST(ratio AS DOUBLE) ratio FROM {DB}.ortholog WHERE orgid1='Putida' AND locusid1='PP_0149'")
orth150 = q(f"SELECT orgid2, locusid2, CAST(ratio AS DOUBLE) ratio FROM {DB}.ortholog WHERE orgid1='Putida' AND locusid1='PP_0150'")
p150 = {o["orgid2"]: o["locusid2"] for o in orth150}
res = {"orthologs_PP_0149": orth, "orthologs_PP_0150": orth150, "per_ortholog": {}}
for o in orth:
    org, loc = o["orgid2"], o["locusid2"]
    if org == "SyringaeB728a_mexBdelta":
        pass
    d = {"locus": loc, "bsr_ratio": o["ratio"], "PP_0150_ortholog": p150.get(org)}
    d["gene"] = q(f"SELECT locusid, begin, `end`, strand, `desc` FROM {DB}.gene WHERE orgid='{org}' AND locusid='{loc}'")
    fit = q(f"""SELECT g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup FROM {DB}.genefitness g
JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname WHERE g.orgid='{org}' AND g.locusid='{loc}'""")
    fit.sort(key=lambda r: r["fit"])
    d["n_experiments"] = len(fit)
    d["strong_neg"] = [r for r in fit if r["fit"] <= -1 and r["t"] <= -4]
    d["strong_pos"] = [r for r in fit if r["fit"] >= 1 and r["t"] >= 4]
    d["specificphenotype"] = q(f"""SELECT s.expname, e.expdesc FROM {DB}.specificphenotype s JOIN {DB}.experiment e
ON e.orgid=s.orgid AND e.expname=s.expname WHERE s.orgid='{org}' AND s.locusid='{loc}'""")
    qexps = q(f"SELECT e.expname, e.expdesc FROM {DB}.experiment e WHERE e.orgid='{org}' AND {QAC}")
    qctx = []
    for e in qexps:
        ex = e["expname"]
        rows = q(f"""SELECT g.locusid, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, ge.`desc` FROM {DB}.genefitness g
JOIN {DB}.gene ge ON ge.orgid=g.orgid AND ge.locusid=g.locusid
WHERE g.orgid='{org}' AND g.expname='{ex}' AND CAST(g.fit AS DOUBLE) <= -1 AND CAST(g.t AS DOUBLE) <= -4 ORDER BY CAST(g.fit AS DOUBLE)""")
        loci = [r["locusid"] for r in rows]
        mine = [r for r in fit if r["expname"] == ex]
        partner = p150.get(org)
        pf = q(f"SELECT CAST(fit AS DOUBLE) fit, CAST(t AS DOUBLE) t FROM {DB}.genefitness WHERE orgid='{org}' AND expname='{ex}' AND locusid='{partner}'") if partner else []
        n = q(f"SELECT count(*) n FROM {DB}.genefitness WHERE orgid='{org}' AND expname='{ex}'")[0]["n"]
        qctx.append({"expname": ex, "expdesc": e["expdesc"], "n_genes": n, "n_strong_neg": len(rows),
                     "ortholog_fit": mine, "ortholog_rank_among_strong": (1 + loci.index(loc)) if loc in loci else None,
                     "PP_0150_ortholog_fit": pf, "top15": rows[:15]})
    d["qac_experiments"] = qctx
    d["cofit_top15"] = q(f"""SELECT c.hitid, CAST(c.rank AS INT) rank, CAST(c.cofit AS DOUBLE) cofit, g.`desc` FROM {DB}.cofit c
JOIN {DB}.gene g ON g.orgid=c.orgid AND g.locusid=c.hitid WHERE c.orgid='{org}' AND c.locusid='{loc}' ORDER BY CAST(c.rank AS INT) LIMIT 15""")
    res["per_ortholog"][org] = d
res["conservedcofit"] = q(f"SELECT * FROM {DB}.conservedcofit WHERE (orgid='Putida' AND locusid='PP_0149') OR (orgid='pseudo5_N2C3_1' AND locusid='AO356_10905') LIMIT 50")
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
for org, d in res["per_ortholog"].items():
    print("##", org, d["locus"], "PP_0150 orth:", d["PP_0150_ortholog"], "n_exp", d["n_experiments"],
          "strong_neg", [(r["expdesc"], round(r["fit"], 2), round(r["t"], 1)) for r in d["strong_neg"]],
          "strong_pos", len(d["strong_pos"]), "specific", [s["expdesc"] for s in d["specificphenotype"]])
    for c in d["qac_experiments"]:
        print("   QAC", c["expname"], c["expdesc"], "n_strong", c["n_strong_neg"], "/", c["n_genes"], "orth", [(round(r["fit"], 2), round(r["t"], 1)) for r in c["ortholog_fit"]],
              "rank", c["ortholog_rank_among_strong"], "PP0150orth", c["PP_0150_ortholog_fit"])
    print("   cofit", [(c["hitid"], round(c["cofit"], 2), c["desc"]) for c in d["cofit_top15"][:8]])
print("conservedcofit", res["conservedcofit"][:10])
