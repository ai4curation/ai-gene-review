"""KT2440 Fitness Browser summary for the six AsmA-like genes (PP_4704, PP_4572, PP_2893 tamB,
PP_0938 yhdP, PP_4857 yhjG, PP_0287 asmA) from BERDL kescience.fitnessbrowser, plus PP_4704 values in
envelope-stress experiments. Usage: python3 -I fb_asma_paralogs.py OUTDIR"""
import json, os, sys, importlib.util
spec = importlib.util.spec_from_file_location("fb", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fb_fitness.py"))
src = open(spec.origin).read().split("out = sys.argv[1]")[0]
ns = {}
exec(src, ns)
q, DB, ORG = ns["q"], ns["DB"], ns["ORG"]
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
genes = ["PP_4704", "PP_4572", "PP_2893", "PP_0938", "PP_4857", "PP_0287"]
inlist = ",".join("'%s'" % g for g in genes)
fit = q(f"""SELECT g.locusid, g.expname, CAST(g.fit AS DOUBLE) fit, CAST(g.t AS DOUBLE) t, e.expdesc, e.expgroup
FROM {DB}.genefitness g JOIN {DB}.experiment e ON e.orgid=g.orgid AND e.expname=g.expname
WHERE g.orgid='{ORG}' AND g.locusid IN ({inlist})""")
res = {}
for g in genes:
    rows = sorted([r for r in fit if r["locusid"] == g], key=lambda r: r["fit"])
    if not rows:
        res[g] = {"n_experiments": 0, "note": "no fitness values (no usable insertions; possibly essential or not assayed)"}
        continue
    strong = [r for r in rows if r["fit"] <= -1 and r["t"] <= -4]
    res[g] = {"n_experiments": len(rows), "n_fit_le_m1_t_le_m4": len(strong), "min_fit": rows[0]["fit"],
              "max_fit": rows[-1]["fit"], "mean_fit": sum(r["fit"] for r in rows) / len(rows),
              "lowest5": [{k: r[k] for k in ("expdesc", "fit", "t")} for r in rows[:5]],
              "strong_groups": sorted({r["expgroup"] for r in strong})}
kw = ("polymyxin", "sds", "deoxycholate", "bile", "edta", "vancomycin", "lauryl", "triton", "cetyl", "benzalkonium",
      "chlorhexidine", "carbenicillin", "detergent", "colistin", "zwittergent")
res["PP_4704_envelope_stress"] = [{k: r[k] for k in ("expname", "expdesc", "fit", "t")} for r in fit
                                  if r["locusid"] == "PP_4704" and any(w in r["expdesc"].lower() for w in kw)]
json.dump(res, open(os.path.join(out, "asma_paralog_fitness.json"), "w"), indent=1)
print(json.dumps({g: ({k: v for k, v in s.items() if k != "lowest5"} if isinstance(s, dict) else s) for g, s in res.items()}, indent=1))
