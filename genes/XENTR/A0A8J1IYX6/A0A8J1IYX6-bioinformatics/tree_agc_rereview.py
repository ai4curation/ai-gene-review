"""Neighbour-joining placement of the A0A8J1IYX6 kinase domain among AGC kinases.

For each sequence, the region locally aligned to the target catalytic region
(target residues 105-424) is extracted, the set is aligned with MAFFT
(--auto, must be on PATH), pairwise p-distances over gap-free columns are
computed, and a neighbour-joining tree is built (Biopython), rooted on PKA.
A rough, unbootstrapped placement; read clade membership, not branch lengths.

Run: uv run --no-project --with biopython --with requests python tree_agc_rereview.py [EXCLUDED_ACC ...]
Accessions given as arguments are left out (used to drop the out-of-family
long-branch sequence RSKR, Q96LW2, which PANTHER places in PTHR24355).
"""

import subprocess
import sys
import tempfile

from Bio import AlignIO, Phylo, Align
from Bio.Align import substitution_matrices
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

from compare_agc_rereview import COMPARATORS, TARGET, fetch


def main(excluded: list[str]) -> None:
    target = fetch(TARGET)
    query = target[104:]
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    seqs = {f"{TARGET}_LOC101732819": query}
    for acc, label in COMPARATORS.items():
        if acc in excluded:
            continue
        seq = fetch(acc)
        aln = aligner.align(query, seq)[0]
        start, end = aln.aligned[1][0][0], aln.aligned[1][-1][1]
        name = f"{acc}_{label.split()[0]}"
        if acc in ("A0A6I8SIW5", "A0A8J0S8T2"):
            name = f"{acc}_XENTR_{label.split()[2]}"
        seqs[name] = seq[start:end]
    with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as fh:
        for n, s in seqs.items():
            fh.write(f">{n}\n{s}\n")
        path = fh.name
    out = subprocess.run(["mafft", "--auto", "--quiet", path], capture_output=True, text=True, check=True).stdout
    msa = AlignIO.read(__import__("io").StringIO(out), "fasta")
    names = [r.id for r in msa]
    matrix = []
    for i, ri in enumerate(msa):
        row = []
        for j in range(i + 1):
            rj = msa[j]
            cols = [(a, b) for a, b in zip(str(ri.seq), str(rj.seq)) if a != "-" and b != "-"]
            diff = sum(a != b for a, b in cols)
            row.append(diff / len(cols) if cols else 1.0)
        matrix.append(row)
    tree = DistanceTreeConstructor().nj(DistanceMatrix(names, matrix))
    outgroup = next(c for c in tree.get_terminals() if c.name.startswith("P17612"))
    tree.root_with_outgroup(outgroup)
    Phylo.draw_ascii(tree)
    suffix = "_excl_" + "_".join(excluded) if excluded else ""
    Phylo.write(tree, f"tree_agc_rereview{suffix}.nwk", "newick")
    tgt = next(c for c in tree.get_terminals() if c.name.startswith(TARGET))
    path_nodes = tree.get_path(tgt)
    for node in reversed(path_nodes[:-1]):
        members = sorted(t.name for t in node.get_terminals())
        print(f"\nSmallest clade containing target (size {len(members)}): {members}")
        break


if __name__ == "__main__":
    main(sys.argv[1:])
