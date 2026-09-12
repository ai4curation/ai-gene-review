#!/usr/bin/env python3
"""Inspect conserved SET-domain catalytic / SAM-binding motifs across a panel.

Strategy (no hardcoded conclusions):
  1. Run hmmalign of every panel sequence to the Pfam SET HMM (PF00856). This puts
     every protein into the SAME coordinate frame (the HMM match states), so we can
     read off, for each conserved HMM column, which residue each protein contributes.
  2. Identify the HMM match-state columns that correspond to the diagnostic SET-domain
     signatures:
        - the invariant NHS motif "NHSC" (SAM methyl-donor / catalytic pocket),
          Pfam consensus "...NHsc.pn..." near the C-terminus of the domain.
        - the C-terminal catalytic tyrosine in the "...tidY" / "GEELtidY" motif
          (the "Y/F switch" position that discriminates the SET active site).
  3. Report, per protein, the residues aligned to those signature columns so a
     human can judge whether the motif is intact (like an active enzyme) or
     substituted (like a reported pseudo-methyltransferase).

We do NOT decide activity in code; we only extract the residues. Interpretation is
written up separately in RESULTS.md.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from Bio import AlignIO, SeqIO

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
DATA = PROJ / "data"
RESULTS = PROJ / "results"


def run_hmmalign(hmm: Path, seqs: Path, out_sto: Path) -> None:
    """Align sequences to the HMM, producing a Stockholm alignment."""
    cmd = ["hmmalign", "--trim", "--amino", "-o", str(out_sto), str(hmm), str(seqs)]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def load_alignment_with_rf(sto: Path):
    """Load the Stockholm alignment and its reference-annotation (#=GC RF) line.

    The RF line marks HMM match states (non-'.' characters), letting us map
    alignment columns back to HMM consensus positions.
    """
    aln = AlignIO.read(sto, "stockholm")
    rf = None
    for line in sto.read_text().splitlines():
        if line.startswith("#=GC RF"):
            rf = line.split(None, 2)[2]
    if rf is None:
        raise RuntimeError("No #=GC RF line found in Stockholm alignment")
    return aln, rf


def hmm_column_map(rf: str) -> list[int]:
    """Return list mapping each alignment column -> HMM match-state index (1-based),
    or -1 for insert columns."""
    col_to_hmm = []
    hmm_idx = 0
    for ch in rf:
        # In hmmalign RF, match columns are uppercase letters or 'x'; inserts are '.'
        if ch != "." and ch != "-":
            hmm_idx += 1
            col_to_hmm.append(hmm_idx)
        else:
            col_to_hmm.append(-1)
    return col_to_hmm


def residues_at_hmm_cols(aln, col_to_hmm, target_hmm_cols):
    """For each sequence return dict hmm_col -> residue (aligned char)."""
    # Build reverse map: hmm_col -> alignment column index
    hmm_to_aln = {}
    for aln_col, hmm_col in enumerate(col_to_hmm):
        if hmm_col in target_hmm_cols:
            hmm_to_aln[hmm_col] = aln_col
    out = {}
    for rec in aln:
        row = {}
        for hmm_col in target_hmm_cols:
            aln_col = hmm_to_aln.get(hmm_col)
            row[hmm_col] = rec.seq[aln_col] if aln_col is not None else None
        out[rec.id] = row
    return out


def build_match_consensus(aln, col_to_hmm):
    """Derive a per-HMM-column majority-residue consensus from the alignment itself.

    We only consider match-state columns (col_to_hmm != -1). For each, take the most
    common non-gap residue across the panel. Returns (consensus_str, hmm_idx_list).
    """
    from collections import Counter

    # gather match columns in HMM order
    match_cols = [(hmm_col, aln_col) for aln_col, hmm_col in enumerate(col_to_hmm) if hmm_col != -1]
    match_cols.sort()
    consensus_chars = []
    idxs = []
    for hmm_col, aln_col in match_cols:
        col_res = [rec.seq[aln_col].upper() for rec in aln if rec.seq[aln_col] not in "-."]
        if col_res:
            most = Counter(col_res).most_common(1)[0][0]
        else:
            most = "-"
        consensus_chars.append(most)
        idxs.append(hmm_col)
    return "".join(consensus_chars), idxs


def find_consensus_motif_cols(rf: str, col_to_hmm, aln) -> dict[str, list[int]]:
    """Locate HMM columns for the diagnostic motifs by scanning a majority consensus
    built from the panel alignment (the RF line only marks match states, not residues).
    """
    consensus, idxs = build_match_consensus(aln, col_to_hmm)
    print("Match-state majority consensus:", consensus)

    motifs: dict[str, list[int]] = {}

    def locate(substr: str, label: str):
        pos = consensus.find(substr)
        if pos >= 0:
            motifs[label] = idxs[pos: pos + len(substr)]
            print(f"  Located {label} ({substr!r}) at HMM cols {motifs[label]}")
        else:
            print(f"  WARNING: motif {substr!r} ({label}) not found in consensus")

    # NHSC signature (SAM/catalytic pocket). Try NHSC then relax to NHS.
    locate("NHSC", "NHSC_motif")
    if "NHSC_motif" not in motifs:
        locate("NHS", "NHSC_motif")
    # terminal catalytic tyrosine motif. Try IDY then relax.
    locate("IDY", "catalytic_Y")
    if "catalytic_Y" not in motifs:
        locate("DY", "catalytic_Y")
    return motifs


def main() -> int:
    hmm = DATA / "PF00856_SET.hmm"
    seqs = DATA / "reference_sequences.fasta"
    sto = RESULTS / "set_domain_hmmalign.sto"

    run_hmmalign(hmm, seqs, sto)
    aln, rf = load_alignment_with_rf(sto)
    col_to_hmm = hmm_column_map(rf)

    motifs = find_consensus_motif_cols(rf, col_to_hmm, aln)
    if not motifs:
        print("No diagnostic motifs located; aborting motif read-out.")
        return 1

    all_cols = sorted({c for cols in motifs.values() for c in cols})
    residues = residues_at_hmm_cols(aln, col_to_hmm, all_cols)

    # Pretty print a table.
    report_lines = []
    report_lines.append("# SET-domain diagnostic-motif residue read-out")
    report_lines.append("")
    report_lines.append("Residues each protein contributes at conserved Pfam SET (PF00856) HMM match columns.")
    report_lines.append("A gap ('-') means the protein has no residue aligned to that HMM position.")
    report_lines.append("")
    for label, cols in motifs.items():
        report_lines.append(f"## {label} (HMM match columns {cols})")
        report_lines.append("")
        header = f"{'protein':22s} " + " ".join(f"H{c:>3d}" for c in cols)
        report_lines.append(header)
        report_lines.append("-" * len(header))
        for rec in aln:
            row = residues[rec.id]
            cells = " ".join(f"{(row[c] or '-'):>4s}" for c in cols)
            report_lines.append(f"{rec.id:22s} {cells}")
        report_lines.append("")

    out = RESULTS / "motif_readout.txt"
    out.write_text("\n".join(report_lines) + "\n")
    print("\n".join(report_lines))
    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
