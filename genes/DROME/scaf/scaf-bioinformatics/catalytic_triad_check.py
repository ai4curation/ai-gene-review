# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Check retention of the S1 catalytic triad (His57, Asp102, Ser195) in Scarface.

Scaf (Q7K5M0) peptidase S1 domain (UniProt FT DOMAIN 421..644) is aligned
globally (BLOSUM62, gap open -10, extend -0.5) to bovine chymotrypsinogen A
(P00766), whose sequence positions define chymotrypsin numbering.  As a positive
control the active Drosophila CLIP protease Persephone (psh, Q9VWU1) is aligned
the same way.  Sequences are fetched live from UniProt REST; nothing is
hardcoded except the reference positions of the triad and of Gly193.

Run: uv run catalytic_triad_check.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

REF = "P00766"  # bovine chymotrypsinogen A
REF_POS = {"His57": 57, "Asp102": 102, "Gly193": 193, "Ser195": 195}
TARGETS = {
    "Q7K5M0 scaf (Scarface)": ("Q7K5M0", 421, 655),
    "Q9VWU1 psh (Persephone, active control)": ("Q9VWU1", None, None),
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def map_positions(ref: str, tgt: str, offset: int):
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(ref, tgt)[0]
    mapping = {}
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        for i in range(re_ - rs):
            mapping[rs + i + 1] = ts + i + 1
    out = {}
    for name, p in REF_POS.items():
        t = mapping.get(p)
        out[name] = (ref[p - 1], None if t is None else (tgt[t - 1], t + offset))
    return out, aln.score


def main() -> None:
    ref = fetch(REF)
    print(f"Reference {REF} length {len(ref)}")
    for label, (acc, start, end) in TARGETS.items():
        seq = fetch(acc)
        offset = 0
        if start is not None:
            seq = seq[start - 1 : end]
            offset = start - 1
        res, score = map_positions(ref, seq, offset)
        print(f"\n{label}: local alignment score {score:.1f}")
        for name, (rres, hit) in res.items():
            if hit is None:
                print(f"  {name} ({rres}): not aligned")
            else:
                aa, pos = hit
                status = "retained" if aa == rres else "SUBSTITUTED"
                print(f"  {name} ({rres}) -> {aa}{pos} [{status}]")


if __name__ == "__main__":
    main()
