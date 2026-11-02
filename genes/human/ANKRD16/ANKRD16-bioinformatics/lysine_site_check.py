"""Check that the serine-accepting lysines mapped in mouse ANKRD16 (K102, K135, K165;
PMID:29769718) are conserved in human ANKRD16.

Fetches canonical sequences from UniProt, aligns them globally (Biopython PairwiseAligner,
BLOSUM62) and reports the human residue aligned to each mouse site. Run with:
    uv run python lysine_site_check.py
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

HUMAN, MOUSE = "Q6P6B7", "A2AS55"
MOUSE_SITES = [102, 135, 165]


def fetch(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        return "".join(r.read().decode().splitlines()[1:])


def main() -> None:
    hu, mo = fetch(HUMAN), fetch(MOUSE)
    al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aln = al.align(mo, hu)[0]
    m2h = {}
    for (ms, me), (hs, he) in zip(*aln.aligned):
        for k in range(me - ms):
            m2h[ms + k + 1] = hs + k + 1
    ident = sum(a == b for a, b in zip(*aln) if a != "-" and b != "-") / len(mo)
    print(f"mouse {MOUSE} len={len(mo)}  human {HUMAN} len={len(hu)}  identity/mouse_len={ident:.2f}")
    for s in MOUSE_SITES:
        h = m2h.get(s)
        print(f"mouse {mo[s-1]}{s} -> human {hu[h-1] + str(h) if h else 'gap'}")


if __name__ == "__main__":
    main()
