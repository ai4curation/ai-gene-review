"""Score predicted secondary structure and contacts against the deposited PDB structures in truth.json."""
import glob, json, math, pathlib, statistics
HERE = pathlib.Path(__file__).parent
T = {t["pdb"]: t for t in json.loads((HERE / "truth.json").read_text())}
def ss(n, helices, strands):
    s = ["C"] * (n + 1)
    for code, segs in (("H", helices), ("E", strands)):
        for seg in segs or []:
            if isinstance(seg, list) and len(seg) == 2 and all(isinstance(v, int) for v in seg):
                for i in range(max(1, seg[0]), min(n, seg[1]) + 1): s[i] = code
    return s
def dist(a, b): return math.dist(a, b)
for f in sorted(glob.glob(str(HERE / "results" / "*.jsonl"))):
    R = [json.loads(l) for l in open(f)]; ok = [r for r in R if r.get("ans")]
    print(f"\n== {pathlib.Path(f).stem}: {len(R)} calls, {len(R)-len(ok)} unparsed, cost ${sum(r.get('cost') or 0 for r in R):.2f}")
    for stratum in ("novel", "known"):
        q3 = []; base = []; prec = []; bg = []; top5 = []; rec = 0; n = 0
        for r in ok:
            t = T[r["pdb"]]
            if t["stratum"] != stratum: continue
            a = r["ans"]; L = len(t["sequence"]); ca = {int(k): v for k, v in t["ca"].items()}; n += 1; rec += bool(a.get("recognised"))
            true, pred = ss(L, t["helices"], t["strands"]), ss(L, a.get("helices"), a.get("strands"))
            obs = sorted(ca)   # score only residues resolved in the crystal structure
            q3.append(sum(true[i] == pred[i] for i in obs) / len(obs))
            base.append(max(sum(true[i] == c for i in obs) for c in "HEC") / len(obs))   # best constant prediction
            pairs = [p for p in (a.get("contacts") or []) if isinstance(p, list) and len(p) == 2 and all(isinstance(v, int) for v in p)
                     and abs(p[0] - p[1]) >= 24 and p[0] in ca and p[1] in ca]
            if pairs:
                hit = [dist(ca[i], ca[j]) < 8 for i, j in pairs]; prec.append(sum(hit) / len(hit)); top5.append(sum(hit[:5]) / len(hit[:5]))
            lr = [(i, j) for i in obs for j in obs if j - i >= 24]
            bg.append(sum(dist(ca[i], ca[j]) < 8 for i, j in lr) / len(lr))
        if not n: continue
        m = lambda x: statistics.mean(x) if x else float("nan")
        print(f"  {stratum:5s} n={n}: Q3 {100*m(q3):.1f}% (best constant-state baseline {100*m(base):.1f}%); long-range contact precision {100*m(prec):.1f}% "
              f"(top-5 {100*m(top5):.1f}%, n={len(prec)}; chance {100*m(bg):.1f}%); says it recognises the protein {rec}/{n}")
