"""Summarise results/EFFORT/*.jsonl. Usage: analyze.py CLONE EFFORT (CLONE as for run.py; used to compare with the authors' stored outputs)."""
import json, sys, gzip, collections, random, glob, os, pathlib
S = sys.argv[1]
for f in sorted(glob.glob(str(pathlib.Path(__file__).parent / "results" / sys.argv[2] / "claude-*.jsonl"))):
    model = os.path.basename(f)[:-6]
    R = [json.loads(l) for l in open(f)]
    err = [r for r in R if "error" in r or r.get("is_error")]
    R = [r for r in R if r not in err]
    print(f"\n== {model}: {len(R)} answered, {len(err)} errors; served={collections.Counter(tuple(r['served']) for r in R).most_common(3)}; cost=${sum(r['cost'] or 0 for r in R):.2f}")
    acc = {}
    for c in ("real", "shuffled", "reversed"):
        x = [r for r in R if r["condition"] == c]
        if not x: continue
        v = [r for r in x if r["valid"]]
        acc[c] = sum(r["first_correct"] for r in x) / len(x)
        print(f"  {c:9s} n={len(x)} invalid={len(x)-len(v)} first-residue={100*acc[c]:.1f}%  exact10={sum(r['exact10'] for r in x)}  thinking>0 in {sum(1 for r in x if r['thinking'])}")
    # per-family gap + bootstrap over families
    fam = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in R: fam[r["pfam"]][r["condition"]].append(r["first_correct"])
    for other in ("shuffled", "reversed"):
        g = [sum(d["real"])/len(d["real"]) - sum(d[other])/len(d[other]) for d in fam.values() if d["real"] and d[other]]
        if not g: continue
        rng = random.Random(0); bs = sorted(sum(rng.choices(g, k=len(g)))/len(g) for _ in range(10000))
        print(f"  gap real-{other}: {100*sum(g)/len(g):+.1f} pts (95% CI {100*bs[250]:+.1f} to {100*bs[9750]:+.1f}), {len(g)} families")
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in R: by[r["size_bin"]][r["condition"]].append(r["first_correct"])
    print("  by family size (real/shuf/rev %):", {b: tuple(round(100*sum(v)/len(v)) for v in (d["real"], d["shuffled"], d["reversed"]) if v) for b, d in sorted(by.items(), key=lambda kv: int(kv[0].split('-')[0].strip('>')))})
    # agreement with the authors' stored outputs on the identical questions
    p = f"{S}/results/outputs/confirm/{model}.jsonl.gz"
    if os.path.exists(p):
        st = {}
        for l in gzip.open(p, "rt"):
            d = json.loads(l); st[(d["accession"], d["condition"], d["cut"])] = d
        for c in ("real", "shuffled"):
            x = [(r, st[(r["accession"], c, r["cut"])]) for r in R if r["condition"] == c and (r["accession"], c, r["cut"]) in st]
            print(f"  authors' stored run, same {len(x)} {c} questions: {100*sum(b['first_correct'] for a,b in x)/len(x):.1f}%; same first letter as mine in {100*sum(a['pred'][:1]==b['pred'][:1] for a,b in x)/len(x):.0f}%")
