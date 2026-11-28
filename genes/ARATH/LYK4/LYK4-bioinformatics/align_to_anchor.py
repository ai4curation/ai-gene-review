# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Align a target protein to an active anchor kinase and map the HRD and DFG aspartates.

Reads both sequences from cached UniProt flat files, makes a global pairwise alignment
(BLOSUM62, gap open -10, extend -0.5), writes it as aligned FASTA, and reports which target
residues face the anchor's catalytic-loop aspartate (the anchor's UniProt ACT_SITE, HRD motif)
and the Mg2+-binding aspartate of the anchor's DFG motif (first DFG within 40 residues after
the HRD). Nothing is hardcoded: positions are read from the files and the alignment.

Usage: uv run align_to_anchor.py ANCHOR_UNIPROT.txt TARGET_UNIPROT.txt OUT_PREFIX
"""
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices


def read_uniprot(path: Path) -> tuple[str, str, int | None]:
    """Return (accession, sequence, first ACT_SITE position) from a UniProt flat file."""
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    seq = "".join(text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0].split())
    m = re.search(r"^FT   ACT_SITE\s+(\d+)", text, re.M)
    return acc, seq, int(m.group(1)) if m else None


def column_map(a_row: str, t_row: str) -> dict[int, int | None]:
    """Map each 1-based anchor position to the 1-based target position facing it (None = gap)."""
    out, ai, ti = {}, 0, 0
    for a, t in zip(a_row, t_row):
        ti += t != "-"
        if a != "-":
            ai += 1
            out[ai] = ti if t != "-" else None
    return out


def main() -> None:
    anchor_file, target_file, prefix = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    a_acc, a_seq, a_hrd = read_uniprot(anchor_file)
    t_acc, t_seq, _ = read_uniprot(target_file)
    if a_hrd is None or a_seq[a_hrd - 3:a_hrd] != "HRD":
        sys.exit(f"anchor ACT_SITE {a_hrd} is not the D of an HRD motif")
    dfg = a_seq.find("DFG", a_hrd, a_hrd + 40)
    if dfg < 0:
        sys.exit("no DFG motif within 40 residues after the anchor HRD")
    a_dfg = dfg + 1

    aligner = Align.PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                                    open_gap_score=-10, extend_gap_score=-0.5)
    aln = aligner.align(a_seq, t_seq)[0]
    a_row, t_row = aln[0], aln[1]
    fasta = prefix.with_suffix(".aln.fasta")
    fasta.write_text(f">{a_acc} anchor\n{a_row}\n>{t_acc} target\n{t_row}\n")

    cmap = column_map(a_row, t_row)
    rows = ["role\tanchor_acc\tanchor_pos\tanchor_res\ttarget_acc\ttarget_pos\ttarget_res\tstatus\ttarget_context"]
    for role, apos in (("catalytic-loop aspartate (HRD)", a_hrd), ("Mg2+-binding aspartate (DFG)", a_dfg)):
        tpos = cmap[apos]
        tres = t_seq[tpos - 1] if tpos else "-"
        status = "RETAINED" if tres == a_seq[apos - 1] else ("LOST" if tpos else "NO_ALIGNED_RESIDUE")
        ctx = t_seq[max(0, tpos - 6):tpos + 3] if tpos else ""
        rows.append(f"{role}\t{a_acc}\t{apos}\t{a_seq[apos - 1]}\t{t_acc}\t{tpos}\t{tres}\t{status}\t{ctx}")
    tsv = prefix.with_suffix(".residues.tsv")
    tsv.write_text("\n".join(rows) + "\n")
    print(f"alignment score {aln.score:.1f}; wrote {fasta} and {tsv}")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
