# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare N. crassa NCU02539 (Q7SHS5) with characterised Mcm4 orthologs and
check conserved MCM motor motifs.

Fetches sequences live from UniProt REST, aligns each ortholog globally to the
target (BLOSUM62), and reports identity, length and target residues at motif
positions that are conserved in all Mcm2-7 subunits (zinc-finger cysteines,
Walker A, Walker B, sensor/arginine-finger region SRF). Motif positions are
located by regular-expression search in each sequence, not hard-coded.

Run: uv run --script compare_mcm4_rereview.py
"""

import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q7SHS5"
OTHERS = {
    "P30665": "S. cerevisiae MCM4/CDC54",
    "P29458": "S. pombe cdc21 (Mcm4)",
    "P33991": "H. sapiens MCM4",
}

MOTIFS = {
    # Walker A of MCM AAA+ domain (GDPG/GDPS-x-x-K-S); Mcm4 subunits carry GDPS
    "Walker_A": r"G[DN]P[GS].[AST]KS",
    # Walker B: hydrophobic stretch followed by DE(F/M)(D/N)K
    "Walker_B": r"[ILV][ACILMV][ACILMV][ACILMV]DE[FLM][DN]K",
    # Arginine finger region conserved in MCM: SRFD
    "SRF_arginine_finger": r"SRF[DE]",
    # N-terminal zinc finger C4 type: C-x2-C-x(n)-C-x2-C (n 10-40)
    "zinc_finger_C4": r"C..C.{10,40}C..C",
    # any CxxC pair, to see whether a degenerate zinc-binding site remains
    "CxxC": r"C..C",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def motif_hits(seq: str) -> dict[str, list[tuple[int, str]]]:
    return {
        name: [(m.start() + 1, m.group()) for m in re.finditer(pat, seq)]
        for name, pat in MOTIFS.items()
    }


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"

    tseq = fetch(TARGET)
    print("# UniProt PRU01410 Walker A/B coordinates 662-669 / 726-729 contain:")
    print(f"  662-669 {tseq[661:669]}  726-729 {tseq[725:729]}")
    print(f"# Target {TARGET} length {len(tseq)}")
    for name, hits in motif_hits(tseq).items():
        print(f"  {name}: {hits}")
    for acc, label in OTHERS.items():
        oseq = fetch(acc)
        aln = aligner.align(tseq, oseq)[0]
        ident = aligned = 0
        for (ts, te), (os_, oe) in zip(*aln.aligned):
            for i, j in zip(range(ts, te), range(os_, oe)):
                aligned += 1
                ident += tseq[i] == oseq[j]
        print(f"\n# {acc} {label} length {len(oseq)}")
        print(
            f"  aligned positions {aligned}; identity {ident / aligned:.3f} "
            f"over aligned; coverage of ortholog {aligned / len(oseq):.3f}"
        )
        for mname, hits in motif_hits(oseq).items():
            print(f"  {mname}: {hits}")


if __name__ == "__main__":
    main()
