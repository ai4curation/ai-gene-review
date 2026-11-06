"""VC_1087 (Q9KT18) ortholog check + HD-GYP motif check.
Usage: analyze.py <proteome.fasta> <dashboard.fasta> <outdir>
1. Local SW (BLOSUM62, open -11, extend -1) of the dashboard protein against every
   N16961 proteome entry; rank by score; report identity over the alignment.
2. Pairwise global alignment of dashboard protein vs N16961 REC/HD-GYP proteins and
   an active HD-GYP PDE set; map HD-GYP metal-binding/catalytic positions."""
import json, os, re, sys
from Bio import Align
from Bio.Align import substitution_matrices

def parse_fasta(path):
    seqs, name, buf = {}, None, []
    for l in open(path):
        l = l.rstrip()
        if l.startswith(">"):
            if name: seqs[name] = "".join(buf)
            name, buf = l[1:], []
        else:
            buf.append(l)
    if name: seqs[name] = "".join(buf)
    return seqs

def gn(h):
    m = re.search(r"GN=(\S+)", h); return m.group(1) if m else h.split()[0]

prot = parse_fasta(sys.argv[1]); q = list(parse_fasta(sys.argv[2]).values())[0]
out = sys.argv[3]; os.makedirs(out, exist_ok=True)
B62 = substitution_matrices.load("BLOSUM62")
loc = Align.PairwiseAligner(mode="local", substitution_matrix=B62, open_gap_score=-11, extend_gap_score=-1)
glo = Align.PairwiseAligner(mode="global", substitution_matrix=B62, open_gap_score=-11, extend_gap_score=-1,
                            end_gap_score=0)

def ident(aln):
    a, b = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    return sum(x == y for x, y in pairs), len(pairs), len(a)

scores = sorted(((loc.score(q, s), h) for h, s in prot.items()), reverse=True)
top = []
for sc, h in scores[:10]:
    aln = loc.align(q, prot[h])[0]
    i, n, L = ident(aln)
    top.append({"gene": gn(h), "header": h[:100], "local_score": sc, "identical": i,
                "aligned_pairs": n, "pct_id_aligned": round(100*i/n, 1), "q_cov_pct": round(100*n/len(q), 1)})
res = {"query_len": len(q), "proteome_size": len(prot), "top_local_hits": top,
       "score_gap_top1_vs_top2": top[0]["local_score"] - top[1]["local_score"]}

# position map query->target via global alignment
def posmap(a, t):
    aln = glo.align(a, t)[0]
    m = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for k in range(qe - qs): m[qs + k] = ts + k
    return aln, m

genes = {gn(h): s for h, s in prot.items()}
# HD-GYP motif landmarks located on the query by regex (1-based)
landmarks = {}
for label, pat in [("HD_dyad_region", r"GLMHQIG"), ("GYP_region", r"YDGTGKP"),
                   ("upstream_H_region", r"FPADHAE")]:
    m = re.search(pat, q); landmarks[label] = m.start() + 1 if m else None
res["query_landmarks_1based"] = landmarks
cmp = {}
for g in ["VC_1087", "VC_1348", "VC_A0210", "VC_A0681", "VC_1295", "VC_A0931", "VC_A0895"]:
    s = genes[g]; aln, m = posmap(q, s); i, n, L = ident(aln)
    win = {}
    for label, p in landmarks.items():
        if p is None: continue
        qs = p - 1
        tpos = [m.get(qs + k) for k in range(12)]
        win[label] = {"query": q[qs:qs+12],
                      "target": "".join(s[t] if t is not None else "-" for t in tpos),
                      "target_start_1based": (tpos[0] + 1) if tpos[0] is not None else None}
    cmp[g] = {"len": len(s), "identical": i, "aligned_pairs": n, "pct_id_aligned": round(100*i/n, 1), "motif_windows": win}
res["pairwise_vs_N16961_HDGYP"] = cmp
# differences dashboard vs VC_1087
aln, m = posmap(q, genes["VC_1087"])
diffs = [{"q_pos": k+1, "q": q[k], "VC_1087_pos": v+1, "VC_1087": genes["VC_1087"][v]}
         for k, v in sorted(m.items()) if q[k] != genes["VC_1087"][v]]
res["n_substitutions_vs_VC_1087"] = len(diffs)
res["substitutions_in_REC_1_126"] = sum(1 for d in diffs if d["q_pos"] <= 126)
res["substitutions_in_HDGYP_195_391"] = sum(1 for d in diffs if 195 <= d["q_pos"] <= 391)
res["phosphoaspartate_D60_query"] = q[59]; res["phosphoaspartate_D60_VC1087"] = genes["VC_1087"][59]
res["substitutions_vs_VC_1087"] = diffs
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1, default=int)
open(os.path.join(out, "alignment_vs_VC_1087.txt"), "w").write(str(aln))
print(json.dumps({k: v for k, v in res.items() if k != "substitutions_vs_VC_1087"}, indent=1, default=int))
