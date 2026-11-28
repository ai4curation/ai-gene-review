import json, glob, pathlib, re, collections
HERE = pathlib.Path(__file__).parent
T = {t["accession"]: t for t in json.load(open(HERE / "truth.json"))}
norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
def ov(a, b): return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)
for f in sorted(glob.glob(str(HERE / "results" / "claude-*.jsonl"))):
    R = [json.loads(l) for l in open(f)]
    ok = [r for r in R if r.get("ans")]
    print(f"\n== {pathlib.Path(f).stem}: {len(R)} calls, {len(R)-len(ok)} unparsed, cost ${sum(r.get('cost') or 0 for r in R):.2f}")
    for cond in ("real", "shuffled"):
        for st in ("B", "A"):
            x = [r for r in ok if r["condition"] == cond and T[r["accession"]]["set"] == st]
            if not x: continue
            tp_id = tp_nm = npred = ntrue = prot_any = prot_hit = 0; iou = []; tmc = tmt = tmexact = tmn = 0; sp = collections.Counter(); helix_hit = helix_true = helix_pred = 0
            for r in x:
                t = T[r["accession"]]; a = r["ans"]
                pd = [d for d in (a.get("pfam_domains") or []) if isinstance(d, dict)]
                true_acc = {p["accession"] for p in t["pfam"]}; true_nm = {norm(p["short"]) for p in t["pfam"]} | {norm(p["name"]) for p in t["pfam"]}
                npred += len(pd); ntrue += len(true_acc); prot_any += bool(pd); hit = False
                for d in pd:
                    ia = str(d.get("accession") or "").split(".")[0] in true_acc; im = norm(d.get("name")) in true_nm
                    tp_id += ia; tp_nm += (ia or im); hit |= (ia or im)
                    if (ia or im) and isinstance(d.get("start"), int) and isinstance(d.get("end"), int):
                        best = max(((ov((d["start"], d["end"]), (p["start"], p["end"])) / (max(d["end"], p["end"]) - min(d["start"], p["start"]) + 1)) for p in t["pfam"]
                                    if p["accession"] == str(d.get("accession")).split(".")[0] or norm(d.get("name")) in (norm(p["short"]), norm(p["name"]))), default=None)
                        if best is not None: iou.append(best)
                prot_hit += hit
                ph = [h for h in (a.get("transmembrane_helices") or []) if isinstance(h, list) and len(h) == 2 and all(isinstance(v, int) for v in h)]
                tmn += 1; tmexact += len(ph) == len(t["tm"]); tmc += (bool(ph) == bool(t["tm"]))
                helix_true += len(t["tm"]); helix_pred += len(ph); helix_hit += sum(any(ov(h, u) >= 10 for h in ph) for u in t["tm"])
                sp[(bool(a.get("signal_peptide")), t["signal"])] += 1
            print(f"  {cond:8s} set {st} n={len(x)}: Pfam proteins with >=1 correct family {prot_hit}/{len(x)}; predicted domains {npred} (correct by id {tp_id}, by id-or-name {tp_nm}); true families {ntrue}; "
                  f"boundary IoU mean {sum(iou)/len(iou) if iou else float('nan'):.2f} (n={len(iou)})")
            if cond == "real":
                print(f"           TM: membrane yes/no agrees {tmc}/{tmn}, helix count exact {tmexact}/{tmn}, helices recovered {helix_hit}/{helix_true}, predicted {helix_pred}; "
                      f"signal peptide TP {sp[(True,True)]} FN {sp[(False,True)]} FP {sp[(True,False)]} TN {sp[(False,False)]}")
            else:
                print(f"           (shuffled = hallucination check) proteins given any Pfam domain {prot_any}/{len(x)}")
