# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Map the human/yeast SmG snRNA-contact triad onto Neurospora NCU09880 (Q7S234).

Residues (PMID:27417296): human SmG Arg25, Phe37, Asn39, Arg63
correspond to yeast SmG Arg23, Phe35, Asn37, Arg64.
Sequences are fetched live from UniProt; nothing is hardcoded except accessions/positions.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACC = {"neurospora": "Q7S234", "yeast": "P40204", "human": "P62308"}
YEAST_POS = {"Arg23": 23, "Phe35": 35, "Asn37": 37, "Arg64": 64}
HUMAN_POS = {"Arg25": 25, "Phe37": 37, "Asn39": 39, "Arg63": 63}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def mapping(ref: str, tgt: str) -> dict[int, int | None]:
    al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aln = al.align(ref, tgt)[0]
    m: dict[int, int | None] = {}
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(re_ - rs):
            m[rs + i + 1] = ts + i + 1
    return m


seqs = {k: fetch(v) for k, v in ACC.items()}
for k, s in seqs.items():
    print(f"{k}\t{ACC[k]}\tlength={len(s)}")
for ref, pos in (("yeast", YEAST_POS), ("human", HUMAN_POS)):
    m = mapping(seqs[ref], seqs["neurospora"])
    for name, p in pos.items():
        t = m.get(p)
        res = seqs["neurospora"][t - 1] if t else "-"
        print(f"{ref} {name} (observed {seqs[ref][p-1]}) -> Q7S234 pos {t}: {res}")
