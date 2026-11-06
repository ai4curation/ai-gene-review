"""Align PP_2389 (dashboard query and Q88KA1) to characterized YqcI/YcgG (PF08892) members and map AglA
functional residues (PMID:41221789: heme ligand Cys44; heme propionate salt bridges Arg166, Lys196, Arg200;
substrate gate Phe152, Arg179, Phe182). Usage: python fam_align.py QUERY_FASTA OUTDIR"""
import json, os, sys, urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

qfa, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8"}), timeout=60) as r:
        return r.read().decode()


def fasta_seq(txt):
    return "".join(l.strip() for l in txt.splitlines() if l and not l.startswith(">"))


seqs = {"dashboard_NZ_CP026332.1_3351": fasta_seq(open(qfa).read())}
seqs["Q88KA1_PP_2389"] = fasta_seq(get("https://rest.uniprot.org/uniprotkb/Q88KA1.fasta"))
mol = json.loads(get("https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/9ub3"))["9ub3"]
seqs["AglA_PDB_9UB3"] = [m for m in mol if m.get("sequence")][0]["sequence"]
refs = {"AglA_PDB_9UB3": "AglA, S. monomycini, AMPn-Arg N-epsilon hydroxylase (PMID:35616638, PMID:41221789)",
        "D2Z024": "DcsA, S. lavendulae, N-omega-hydroxy-L-arginine synthase (D-cycloserine)",
        "A0ABX8WWF6": "GntA, Sphaerospermopsis torques-reginae, pre-guanitoxin N-hydroxylase",
        "P45944": "YqcI, B. subtilis, uncharacterized", "P94382": "YcgG, B. subtilis, uncharacterized"}
for acc in ["D2Z024", "A0ABX8WWF6", "P45944", "P94382"]:
    seqs[acc] = fasta_seq(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"))
with open(os.path.join(out, "sequences.fasta"), "w") as f:
    for k, v in seqs.items():
        f.write(f">{k}\n{v}\n")

al = Align.PairwiseAligner(mode="local", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                           open_gap_score=-11, extend_gap_score=-1)


def pair(a, b):
    aln = al.align(seqs[a], seqs[b])[0]
    m = {}
    ident = n = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            m[j] = i
            n += 1
            ident += seqs[a][i] == seqs[b][j]
    return aln, m, ident, n


res = {"query_vs_Q88KA1": {}, "pairs": {}, "aglA_residue_map": {}}
_, _, i0, n0 = pair("dashboard_NZ_CP026332.1_3351", "Q88KA1_PP_2389")
res["query_vs_Q88KA1"] = {"identical": i0, "aligned": n0, "pct": round(100 * i0 / n0, 1),
                          "len_query": len(seqs["dashboard_NZ_CP026332.1_3351"]), "len_Q88KA1": len(seqs["Q88KA1_PP_2389"])}
Q = "Q88KA1_PP_2389"
for s in refs:
    aln, m, i, n = pair(Q, s)
    res["pairs"][s] = {"description": refs[s], "identical": i, "aligned": n, "pct_identity": round(100 * i / n, 1),
                       "score": aln.score, "subject_len": len(seqs[s])}
    with open(os.path.join(out, f"aln_PP_2389_vs_{s}.txt"), "w") as f:
        f.write(str(aln))
# AglA numbering: the paper's numbering; check which offset gives C44, F152, R166, R179, F182, K196, R200
A = seqs["AglA_PDB_9UB3"]
key = {44: "C", 152: "F", 166: "R", 179: "R", 182: "F", 196: "K", 200: "R"}
offs = [o for o in range(-20, 21) if all(0 <= p - 1 + o < len(A) and A[p - 1 + o] == aa for p, aa in key.items())]
res["aglA_numbering_offset_into_pdb_seq"] = offs
aln, m, _, _ = pair(Q, "AglA_PDB_9UB3")
o = offs[0] if offs else 0
for p, aa in key.items():
    j = p - 1 + o
    i = m.get(j)
    res["aglA_residue_map"][f"{aa}{p}"] = {"aglA_residue": A[j], "PP_2389_pos": None if i is None else i + 1,
                                            "PP_2389_residue": None if i is None else seqs[Q][i]}
# FPC / CPF motifs in PP_2389
import re
res["PP_2389_motifs"] = {mo: [x.start() + 1 for x in re.finditer(mo, seqs[Q])] for mo in ["FPC", "CPF"]}
res["PP_2389_cys_positions"] = [k + 1 for k, c in enumerate(seqs[Q]) if c == "C"]
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
