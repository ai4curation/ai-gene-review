# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Align NCU08595 (Q7SCN3) with characterized Rpf2 orthologs and report the
residues aligned to experimentally implicated 5S rRNA-binding positions.

Positions checked (from the literature, in the reference protein's numbering):
- S. cerevisiae Rpf2 (P36160) R236, implicated in 5S rRNA binding (PMID:25855814)
- the A. nidulans Rpf2 KKR loop 95-97 (PMID:26117542); A. nidulans Rpf2 is not
  fetched here, so the KKR motif is located by searching each sequence directly.
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q7SCN3": "N. crassa NCU08595", "G0SF80": "C. thermophilum Rpf2",
        "P36160": "S. cerevisiae Rpf2", "Q9H7B2": "H. sapiens RPF2"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligned_pos(aln, q_pos: int) -> tuple[int | None, str | None]:
    """Map 1-based position in target (seq B) to query (seq A)."""
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        if b0 < q_pos <= b1:
            return a0 + (q_pos - b0), None
    return None, None


seqs = {a: fetch(a) for a in ACCS}
aligner = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
target = seqs["Q7SCN3"]
print(f"Q7SCN3 length {len(target)}")
for acc, name in ACCS.items():
    s = seqs[acc]
    kkr = [m.start() + 1 for m in re.finditer("KKR", s)]
    print(f"{acc} ({name}) length {len(s)}; KKR motif starts at {kkr}")
for acc in ["G0SF80", "P36160", "Q9H7B2"]:
    aln = aligner.align(target, seqs[acc])[0]
    ident = sum(1 for (a0, a1), (b0, b1) in zip(*aln.aligned)
                for i in range(a1 - a0) if target[a0 + i] == seqs[acc][b0 + i])
    print(f"Q7SCN3 vs {acc}: identical aligned residues {ident}; identity over shorter seq "
          f"{ident / min(len(target), len(seqs[acc])):.2f}")
    if acc == "P36160":
        p, _ = aligned_pos(aln, 236)
        print(f"  S. cerevisiae R236 ({seqs[acc][235]}) aligns to Q7SCN3 position {p}: "
              f"{target[p - 1] if p else 'gap'}")
