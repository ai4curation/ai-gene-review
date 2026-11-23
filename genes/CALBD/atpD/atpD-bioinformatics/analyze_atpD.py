"""B9MS68 (C. bescii AtpD) vs E. coli AtpD (P0ABB4): catalytic-residue map, and
C. bescii c subunit (B9MS73) vs the Na+-binding c subunit of Ilyobacter tartaricus (Q8KRV3).

Run: uv run --with biopython python analyze_atpD.py   (writes results.json, sequences.fasta)
E. coli literature numbering = UniProt P0ABB4 numbering - 1 (mature chain lacks Met1).
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def seq(acc):
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60) as r:
        return "".join(l for l in r.read().decode().splitlines() if not l.startswith(">"))


def align(a, b, mode):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score, al.mode = -11, -1, mode
    aln = al.align(a, b)[0]
    pairs = [(i, j) for (as_, ae), (bs, be) in zip(*aln.aligned) for i, j in zip(range(as_, ae), range(bs, be))]
    return aln, pairs


S = {a: seq(a) for a in ("B9MS68", "P0ABB4", "B9MS73", "Q8KRV3", "P68699")}
cb, ec = S["B9MS68"], S["P0ABB4"]
aln, pr = align(cb, ec, "global")
ec2cb = {j: i for i, j in pr}
ident = sum(cb[i] == ec[j] for i, j in pr)
sites = {"K155 Walker A": 155, "T156 Walker A, Mg2+": 156, "E181 catalytic base": 181,
         "R182 catalytic site": 182, "E185 catalytic site": 185, "D242 Walker B": 242,
         "Y331 adenine stacking": 331, "D380 DELSEED loop start": 380}
site_map = [{"ecoli_beta": k, "ecoli_aa": ec[v], "b9ms68_pos": ec2cb[v] + 1, "b9ms68_aa": cb[ec2cb[v]],
             "conserved": ec[v] == cb[ec2cb[v]]} for k, v in sites.items()]

# Na+ ligands of the I. tartaricus c ring: Gln32, Glu65, Ser66 (and Tyr70)
ref = S["Q8KRV3"]
na = {}
for acc in ("B9MS73", "P68699"):
    _, p = align(ref, S[acc], "global")
    m = dict(p)
    na[acc] = {f"{ref[k-1]}{k}": (S[acc][m[k-1]] + str(m[k-1] + 1)) if k - 1 in m else "gap" for k in (32, 65, 66, 70)}

res = {"b9ms68_length": len(cb), "p0abb4_length": len(ec), "aligned_pairs": len(pr),
       "identical_pairs": ident, "percent_identity": round(100 * ident / len(pr), 1),
       "walker_a_b9ms68_152_159": cb[151:159], "delseed_b9ms68_384_390": cb[383:390],
       "ecoli_site_map": site_map, "c_subunit_na_site_vs_Q8KRV3": na}
json.dump(res, open("results.json", "w"), indent=2)
with open("sequences.fasta", "w") as f:
    for a, s in S.items():
        f.write(f">{a}\n{s}\n")
print(json.dumps(res, indent=2))
