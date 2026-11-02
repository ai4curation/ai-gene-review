"""Compare P. putida KT2440 and P. aeruginosa PAO1 ParA and ParB.

Reads the cached UniProt flat files in the gene folders, aligns each
P. putida protein with its P. aeruginosa ortholog (global, BLOSUM62),
reports identity, and locates the conserved motifs that define the two
activities: the deviant Walker A box of ParA (KGGxGK[ST]) and the
CTP-binding box of ParB (GERRxRA).

Run from the repository root:

    uv run python genes/PSEPK/parA/parA-bioinformatics/compare_orthologs.py
"""

import re
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
MOTIFS = {
    "parA": ("deviant Walker A (KGGxGK[ST])", r"KGG.GK[ST]"),
    "parB": ("ParB CTP-binding box II (GERRxRA)", r"GERR.RA"),
}


def uniprot_sequence(path: Path) -> str:
    text = path.read_text()
    block = text.split("\nSQ ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return re.sub(r"[^A-Z]", "", block)


def main() -> None:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    print("| protein | P. putida length | P. aeruginosa length | identical positions | identity | motif | P. putida position | P. aeruginosa position |")
    print("|---|---:|---:|---:|---:|---|---|---|")
    for gene, (motif_name, motif) in MOTIFS.items():
        pp = uniprot_sequence(ROOT / f"genes/PSEPK/{gene}/{gene}-uniprot.txt")
        pa = uniprot_sequence(ROOT / f"genes/PSEAE/{gene}/{gene}-uniprot.txt")
        aln = aligner.align(pp, pa)[0]
        identical = sum(1 for a, b in zip(aln[0], aln[1]) if a == b and a != "-")
        shorter = min(len(pp), len(pa))

        def hits(seq: str) -> str:
            found = [f"{m.group()} {m.start() + 1}-{m.end()}" for m in re.finditer(motif, seq)]
            return ", ".join(found) or "absent"

        print(
            f"| {gene} | {len(pp)} | {len(pa)} | {identical}/{shorter} | "
            f"{100 * identical / shorter:.1f}% | {motif_name} | {hits(pp)} | {hits(pa)} |"
        )


if __name__ == "__main__":
    main()
