#!/usr/bin/env python3
"""Extract SET-domain catalytic / SAM-binding motif residues via a full MAFFT MSA.

Approach (no hardcoded conclusions):
  1. MAFFT-align the full panel (SET6 + yeast SET1-5 + human SMYD1/2/3 + SETD6).
  2. Anchor on two diagnostic, well-conserved SET-domain signatures that carry the
     catalytic machinery:
        (a) the "NHSC"/"(F/Y)xxNHSCxPN" motif  -- the SAM-binding + catalytic pocket;
            the invariant Asn-His of this motif and the following Cys line the
            AdoMet/target-lysine channel. Loss here is the classic hallmark of a
            pseudo-methyltransferase.
        (b) the C-terminal "(NR)DI...EE...tidY" motif carrying the catalytic tyrosine
            (the post-SET / Y-switch tyrosine).
  3. For each protein, find its residue positions aligned to the SET6 motif columns and
     print them side by side.

Interpretation is written up in RESULTS.md, not here.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from Bio import AlignIO

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
DATA = PROJ / "data"
RESULTS = PROJ / "results"

# The SET6 (Q12529) motif substrings we anchor on, with the 0-based index (within the
# substring) of the residue(s) of special interest. These are taken from the SET6
# primary sequence directly (not from any conclusion), and used only to *find* the
# aligned columns; every protein's residue is then read from the MSA.
SET6_ANCHORS = {
    # NHSC motif: in SET6 the region is ...SYFNHSCNPNI...
    "NHSC_pocket": {"motif": "FNHSCNPN", "highlight": [1, 2, 3]},  # N,H,S(,C)
    # catalytic-Y motif: in SET6 the region is ...MNRDIKKDEQICIDY
    "catalytic_Y": {"motif": "NRDIKKDEQICIDY", "highlight": [13]},  # terminal Y
}


def run_mafft(seqs: Path, out: Path) -> None:
    cmd = ["mafft", "--maxiterate", "1000", "--localpair", str(seqs)]
    print("Running:", " ".join(cmd))
    with out.open("w") as fh:
        subprocess.run(cmd, check=True, stdout=fh, stderr=subprocess.DEVNULL)


def seq_index_to_aln_col(aln_seq: str) -> list[int]:
    """Map ungapped residue index -> alignment column for one aligned sequence."""
    mapping = []
    for col, ch in enumerate(aln_seq):
        if ch not in "-.":
            mapping.append(col)
    return mapping


def main() -> int:
    seqs = DATA / "reference_sequences.fasta"
    aln_path = RESULTS / "panel_mafft.aln.fasta"
    run_mafft(seqs, aln_path)

    aln = AlignIO.read(aln_path, "fasta")
    by_id = {rec.id: str(rec.seq) for rec in aln}

    set6_id = [i for i in by_id if i.startswith("Q12529")][0]
    set6_aln = by_id[set6_id]
    set6_ungapped = set6_aln.replace("-", "").replace(".", "")
    set6_map = seq_index_to_aln_col(set6_aln)

    report = ["# SET-domain motif read-out from MAFFT MSA", ""]
    report.append(f"Anchor protein: {set6_id}")
    report.append("Each block: the SET6 motif, then the residues every panel protein aligns")
    report.append("to those exact SET6 columns. '*' marks the catalytically critical position(s).")
    report.append("")

    for label, spec in SET6_ANCHORS.items():
        motif = spec["motif"]
        highlight = set(spec["highlight"])
        pos = set6_ungapped.find(motif)
        report.append(f"## {label}: SET6 motif '{motif}' at SET6 residues "
                      f"{pos + 1}-{pos + len(motif)}")
        if pos < 0:
            report.append("  ERROR: anchor motif not found in SET6 sequence!")
            report.append("")
            continue
        # alignment columns for each residue of the motif
        motif_cols = [set6_map[pos + k] for k in range(len(motif))]

        # header
        colhead = "".join("*" if k in highlight else " " for k in range(len(motif)))
        report.append(f"  {'':24s} {colhead}")
        report.append(f"  {set6_id:24s} {motif}   <- anchor")
        for rec_id, aln_seq in by_id.items():
            if rec_id == set6_id:
                continue
            chars = "".join(aln_seq[c] for c in motif_cols)
            report.append(f"  {rec_id:24s} {chars}")
        report.append("")

    text = "\n".join(report) + "\n"
    out = RESULTS / "motif_readout_mafft.txt"
    out.write_text(text)
    print(text)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
