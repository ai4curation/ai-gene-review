"""Pairwise identities between KT2440 PEA-transferase paralogs (PP_0024, PP_4592, PP_2579) and
characterized/annotated family members (EptA, EptB, EptC/CptA, OpgE, MCR-1, PAO1 PA1972/PA3310/PA4517,
P. syringae EptA, Neisseria LptA). Global alignment (Biopython PairwiseAligner, BLOSUM62, open -10, extend -0.5).
Identity = identical positions / aligned (non-gap) columns, and / query length.
Also: catalytic nucleophile check (Thr of EptA_Nm T280 equivalent) by alignment to NMB1638.
Usage: python fb pea_paralogs.py OUTDIR"""
import json, os, sys, urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

ACC = {"PP_0024": "Q88RV5", "PP_4592": "Q88E74", "PP_2579_CptA": "Q88JS0",
       "Pae_PA1972_EptA": "Q9I2D3", "Pae_PA3310": "Q9HYT4", "Pae_PA4517_CptA": "Q9HVQ5",
       "Psy_B728a_Psyr_1562_EptA": "Q4ZW62", "Psy_1448A_PSPPH_1546": "Q48LC7",
       "Eco_EptA": "P30845", "Eco_EptB": "P37661", "Eco_EptC_CptA": "P0CB39", "Eco_OpgE": "P75785", "Eco_YhbX": "P42640",
       "MCR-1": "A0A0R6L508", "Nme_NMB1638_LptA": "Q7DD94"}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
seqs = {}
for k, a in ACC.items():
    t = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{a}.fasta", timeout=60).read().decode()
    seqs[k] = "".join(t.split("\n")[1:])
with open(os.path.join(out, "seqs.fasta"), "w") as f:
    for k, s in seqs.items():
        f.write(f">{k} {ACC[k]}\n{s}\n")
al = Align.PairwiseAligner(); al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10; al.extend_gap_score = -0.5; al.mode = "global"
al.end_gap_score = 0  # free end gaps


def ident(a, b):
    aln = al.align(seqs[a], seqs[b])[0]
    idn = alnd = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            alnd += 1; idn += seqs[a][i] == seqs[b][j]
    return aln, {"identical": idn, "aligned": alnd, "pct_aligned": round(100 * idn / alnd, 1),
                 "pct_of_shorter": round(100 * idn / min(len(seqs[a]), len(seqs[b])), 1)}


res = {"accessions": ACC, "lengths": {k: len(v) for k, v in seqs.items()}, "pairs": {}}
queries = ["PP_0024", "PP_4592", "PP_2579_CptA"]
for q in queries:
    for t in ACC:
        if t != q:
            res["pairs"][f"{q}|{t}"] = ident(q, t)[1]
for a, b in [("Pae_PA1972_EptA", "Pae_PA3310"), ("Pae_PA1972_EptA", "Psy_B728a_Psyr_1562_EptA"), ("Pae_PA3310", "Psy_B728a_Psyr_1562_EptA")]:
    res["pairs"][f"{a}|{b}"] = ident(a, b)[1]
# best hits
res["best_hit_summary"] = {}
for q in queries:
    hits = sorted(((v["pct_aligned"], k.split("|")[1]) for k, v in res["pairs"].items() if k.startswith(q + "|")), reverse=True)
    res["best_hit_summary"][q] = hits[:6]
# PAO1 EptA paralogs: which KT2440 protein is closest to each (reciprocal check)
res["pao1_to_kt2440"] = {p: {q: res["pairs"][f"{q}|{p}"]["pct_aligned"] for q in queries} for p in ["Pae_PA1972_EptA", "Pae_PA3310", "Pae_PA4517_CptA"]}
# catalytic Thr: NMB1638 (Neisseria EptA, PDB 5FGN) nucleophile T280 and Zn ligands E240, D452, H453, H465 (Wanty et al. 2013)
aln = al.align(seqs["Nme_NMB1638_LptA"], seqs["PP_0024"])[0]
m = {}
for (s1, e1), (s2, e2) in zip(*aln.aligned):
    for i, j in zip(range(s1, e1), range(s2, e2)):
        m[i + 1] = j + 1
res["NmLptA_sites_in_PP_0024"] = {f"{seqs['Nme_NMB1638_LptA'][p-1]}{p}": (f"{seqs['PP_0024'][m[p]-1]}{m[p]}" if p in m else None) for p in [240, 280, 452, 453, 465]}
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps({k: res[k] for k in ("best_hit_summary", "pao1_to_kt2440", "NmLptA_sites_in_PP_0024")}, indent=1))
