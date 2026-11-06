"""Identity of dashboard DOAB01000105.1_3 to Q88MF2 and E. coli TruD (Q57261);
conservation of E. coli TruD catalytic / mutagenised residues in the query."""
import json, sys
from pathlib import Path
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

D = Path(__file__).parent / "data"
def rd(f): return str(next(SeqIO.parse(D / f, "fasta")).seq)
q = rd("dashboard_DOAB01000105.1_3.fasta")
subjects = {"Q88MF2": ("P. putida KT2440 TruD (PP_1619)", rd("Q88MF2.fasta")),
            "Q57261": ("E. coli K-12 TruD", rd("Q57261.fasta"))}
al = PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                     open_gap_score=-11, extend_gap_score=-1, end_gap_score=0)
# E. coli TruD residues with experimental/curated roles (UniProt Q57261 FT lines)
ecoli_sites = {27: "binding (ECO:0000250)", 31: "Glu31 proton acceptor; E31Q loss of activity (PMID:19664587)",
               79: "K79L 20-fold decrease (PMID:19664587)",
               80: "Asp80 nucleophile; D80N/T loss of activity (PMID:12756329, 19664587)",
               129: "binding (ECO:0000305)", 329: "binding (ECO:0000250)"}
out = {"query": "DOAB01000105.1_3", "query_length": len(q), "alignments": {}}
for acc, (lab, s) in subjects.items():
    a = al.align(q, s)[0]
    qmap = {}; ident = alnpos = 0
    for (qs, qe), (ss, se) in zip(*a.aligned):
        for i, j in zip(range(qs, qe), range(ss, se)):
            alnpos += 1; ident += q[i] == s[j]; qmap[j + 1] = i + 1
    rec = {"label": lab, "subject_length": len(s), "identities": ident, "aligned_positions": alnpos,
           "percent_identity_aligned": round(100 * ident / alnpos, 1),
           "query_range": [int(a.aligned[0][0][0]) + 1, int(a.aligned[0][-1][1])],
           "subject_range": [int(a.aligned[1][0][0]) + 1, int(a.aligned[1][-1][1])]}
    if acc == "Q57261":
        sites = {}
        for pos, note in ecoli_sites.items():
            qp = qmap.get(pos)
            sites[str(pos)] = {"ecoli_residue": s[pos - 1], "query_pos": qp,
                               "query_residue": q[qp - 1] if qp else None,
                               "conserved": bool(qp and q[qp - 1] == s[pos - 1]), "note": note}
        rec["ecoli_sites"] = sites
        rec["query_74_92"] = q[73:92]; rec["ecoli_73_91"] = s[72:91]
        print(a)
    out["alignments"][acc] = rec
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "results.json", "w"), indent=2)
print(json.dumps(out, indent=2))
