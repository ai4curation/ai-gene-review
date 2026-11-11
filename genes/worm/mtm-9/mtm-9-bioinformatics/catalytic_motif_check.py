"""Check the myotubularin catalytic loop (H-C-x-x-G-x-x-R) of C. elegans MTM-9.

Compares MTM-9 (Q965W9, read from the local UniProt flat file) with active
myotubularins fetched from UniProt REST: human MTMR6 (Q9Y217), C. elegans
MTM-6 (Q22712 is NOT assumed; the accession is resolved by gene name query),
and inactive human MTMR9 (Q96QG7). The loop is located by pairwise global
alignment (Biopython PairwiseAligner, BLOSUM62) against MTMR6, whose active
cysteine is found by regex on the canonical HCSDGWDR motif.

Usage: uv run python catalytic_motif_check.py
"""

import re
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent


def local_seq(path: Path) -> str:
    text = path.read_text()
    sq = text.split("\nSQ ")[1].split("\n", 1)[1]
    return "".join(sq.replace("//", "").split())


def fetch(query: str) -> tuple[str, str]:
    url = (
        "https://rest.uniprot.org/uniprotkb/search?format=fasta&size=1&query="
        + urllib.parse.quote(query)
    )
    fasta = urllib.request.urlopen(url).read().decode()
    header, *lines = fasta.strip().split("\n")
    return header, "".join(lines)


def project(aln, pos0: int) -> int | None:
    """Map 0-based target position to 0-based query position via alignment."""
    for (t0, t1), (q0, q1) in zip(*aln.aligned):
        if t0 <= pos0 < t1:
            return q0 + (pos0 - t0)
    return None


def main() -> None:
    mtm9 = local_seq(HERE.parent / "mtm-9-uniprot.txt")
    ref_h, mtmr6 = fetch("accession:Q9Y217")
    mtm6_h, mtm6 = fetch("gene_exact:mtm-6 AND organism_id:6239 AND reviewed:true")
    mtmr9_h, mtmr9 = fetch("accession:Q96QG7")
    m = re.search("HC[A-Z]{2}G[A-Z]{2}R", mtmr6)
    assert m, "active motif not found in MTMR6 positive control"
    cys0 = m.start() + 1
    print(f"Reference {ref_h.split()[0]}: motif {m.group()} active Cys{cys0 + 1}")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    for name, seq in [
        (mtm6_h.split()[0] + " (worm MTM-6, active control)", mtm6),
        (mtmr9_h.split()[0] + " (human MTMR9, inactive control)", mtmr9),
        ("Q965W9 MTM-9", mtm9),
    ]:
        aln = aligner.align(mtmr6, seq)[0]
        p = project(aln, cys0)
        if p is None:
            print(f"{name}: active-Cys column falls in a gap")
            continue
        loop = seq[p - 1 : p + 7]
        print(
            f"{name}: residue at active-Cys column = {seq[p]}{p + 1}; "
            f"loop (H..R window) = {loop}; "
            f"matches HCxxGxxR: {bool(re.fullmatch('HC..G..R', loop))}"
        )


if __name__ == "__main__":
    import urllib.parse  # noqa: F401

    main()
