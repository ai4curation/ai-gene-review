"""VC_0658 (Q9KU65) motif / topology / identity analysis vs dashboard NZ_JABEED010000006.1_102."""
import json, os, re, sys

uniprot_txt, dash_fasta = sys.argv[1], sys.argv[2]
out = os.environ.get("BERIL_RUN_DIR", ".")

def read_uniprot_seq(p):
    s, on = [], False
    for line in open(p):
        if line.startswith("SQ"): on = True; continue
        if line.startswith("//"): break
        if on: s.append(line.replace(" ", "").strip())
    return "".join(s)

def read_fasta(p):
    return "".join(l.strip() for l in open(p) if not l.startswith(">"))

U = read_uniprot_seq(uniprot_txt); D = read_fasta(dash_fasta)

# Global alignment (Needleman-Wunsch, identity scoring, linear gap)
def nw(a, b, match=2, mis=-1, gap=-2):
    n, m = len(a), len(b)
    S = [[0]*(m+1) for _ in range(n+1)]; T = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): S[i][0] = i*gap; T[i][0] = 1
    for j in range(1, m+1): S[0][j] = j*gap; T[0][j] = 2
    for i in range(1, n+1):
        for j in range(1, m+1):
            d = S[i-1][j-1] + (match if a[i-1] == b[j-1] else mis)
            u = S[i-1][j] + gap; l = S[i][j-1] + gap
            S[i][j], T[i][j] = max((d, 0), (u, 1), (l, 2))
    i, j, A, B = n, m, [], []
    while i > 0 or j > 0:
        t = T[i][j] if i > 0 and j > 0 else (1 if i > 0 else 2)
        if t == 0: A.append(a[i-1]); B.append(b[j-1]); i -= 1; j -= 1
        elif t == 1: A.append(a[i-1]); B.append("-"); i -= 1
        else: A.append("-"); B.append(b[j-1]); j -= 1
    return "".join(reversed(A)), "".join(reversed(B))

A, B = nw(U, D)
ident = sum(1 for x, y in zip(A, B) if x == y and x != "-")
aligned = sum(1 for x, y in zip(A, B) if x != "-" and y != "-")
diffs = []
ui = 0
for x, y in zip(A, B):
    if x != "-": ui += 1
    if x != y: diffs.append({"uniprot_pos": ui, "uniprot": x, "dashboard": y})

# Motifs (positions 1-based on Q9KU65)
def find(pat, s):
    return [{"start": m.start()+1, "end": m.end(), "match": m.group()} for m in re.finditer(pat, s)]

motifs = {
    "GGDEF_A_site_GG[DE]EF": find(r"GG[DE]EF", U),
    "I_site_RxxD_(within_~10aa_upstream_of_GGDEF)": [],
    "EAL_ExLxR": find(r"E[A-Z]L[A-Z]R", U),
    "EAL_DDFGTG_loop6": find(r"DDFG[A-Z]G", U),
    "EAL_conserved_K_in_KxD_(KIDR)": find(r"K[IV]D[RK]", U),
    "EAL_conserved_E_in_EGVE": find(r"E[GC]VE", U),
    "EAL_N_in_INxS": find(r"[IL][NQ][IL][SN]", U),
    "EAL_E_in_ExxE_(ELEITE)": find(r"E[LI]E[IL]TE", U),
}
for g in motifs["GGDEF_A_site_GG[DE]EF"]:
    win = U[max(0, g["start"]-1-12): g["start"]-1]
    for m in re.finditer(r"R..D", win):
        motifs["I_site_RxxD_(within_~10aa_upstream_of_GGDEF)"].append(
            {"start": g["start"]-12+m.start(), "match": m.group()})
    motifs["GGDEF_context_-12..+5"] = U[g["start"]-13: g["end"]+5]

# Kyte-Doolittle hydropathy, window 19, threshold 1.6
kd = dict(A=1.8,R=-4.5,N=-3.5,D=-3.5,C=2.5,Q=-3.5,E=-3.5,G=-0.4,H=-3.2,I=4.5,L=3.8,K=-3.9,M=1.9,F=2.8,P=-1.6,S=-0.8,T=-0.7,W=-0.9,Y=-1.3,V=4.2)
w = 19; vals = [sum(kd[c] for c in U[i:i+w])/w for i in range(len(U)-w+1)]
segs, cur = [], None
for i, v in enumerate(vals):
    if v >= 1.6:
        if cur is None: cur = [i+1, i+w]
        else: cur[1] = i+w
    else:
        if cur: segs.append(cur); cur = None
if cur: segs.append(cur)
tm = [{"start": a, "end": b, "seq": U[a-1:b], "max_kd": round(max(vals[a-1:b-w+1]), 2)} for a, b in segs]

res = {
    "uniprot_Q9KU65_length": len(U), "dashboard_length": len(D),
    "alignment": {"identical": ident, "aligned_columns_no_gap": aligned,
                  "pct_identity_over_aligned": round(100*ident/aligned, 2),
                  "pct_identity_over_dashboard_len": round(100*ident/len(D), 2),
                  "differences": diffs},
    "motifs_on_Q9KU65": motifs,
    "kd_hydrophobic_segments_w19_ge1.6": tm,
}
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
with open(os.path.join(out, "alignment.txt"), "w") as f:
    for k in range(0, len(A), 60):
        f.write(f"Q9KU65 {A[k:k+60]}\nDASH   {B[k:k+60]}\n\n")
print(json.dumps(res, indent=1))
