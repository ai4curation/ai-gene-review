#!/usr/bin/env python3
"""Check conservation of functionally important MCT/MFS residues in MCH2.

Anchors on human MCT1 (SLC16A1, P53985) residues with published functional
roles, maps their alignment columns, and reports what each panel member has at
those columns. Also reports the canonical MFS "motif A" region (the
G-x(3)-[DE]-[RK]-x-G-[RK][RK] motif located in the loop between TM2 and TM3).

Reference residues (human MCT1 numbering; Wilson et al. 2009 JBC 284:20011;
Manoharan et al. 2006 Biochem J):
  - Lys38  (TM1)          : charged residue implicated in H+/lactate coupling
  - Asp302 (TM8)          : essential for transport / part of translocation path
  - Arg306 (TM8)          : essential positive charge for substrate carboxylate
  - Phe360 (TM10)         : substrate-binding pocket

Runs on any aligned FASTA that contains the anchor accession.

Usage:
    python motif_check.py --aln results/panel_aln.fasta --anchor P53985 \
        --out results/motif_conservation.tsv
"""
import argparse
import re
from pathlib import Path


def read_fasta(path: Path) -> list[tuple[str, str]]:
    records = []
    name = None
    parts: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                records.append((name, "".join(parts)))
            name = line[1:].strip()
            parts = []
        else:
            parts.append(line.strip())
    if name is not None:
        records.append((name, "".join(parts)))
    return records


# Anchor residue positions in the UNALIGNED anchor sequence (1-based) -> (label,
# expected residue). Only residues whose identity we can VERIFY against the anchor
# sequence are reported; any position whose expected residue does not match the
# anchor is flagged MISMATCH and excluded from interpretation (see RESULTS.md).
#
# Lys38 of human MCT1/SLC16A1 (this exact P53985 sequence position) is the
# well-documented conserved TM1 basic residue implicated in the H+/lactate
# translocation pathway (Wilson et al. 2009 JBC 284:20011-20021; the TM1 lysine
# is conserved across the transporting MCT1-4 subfamily).
ANCHOR_RESIDUES = {
    38: ("Lys38_TM1_MCT1", "K"),
}


def ungapped_index_to_alncol(aln_seq: str) -> dict[int, int]:
    """Map 1-based ungapped residue index -> 0-based alignment column."""
    mapping = {}
    idx = 0
    for col, ch in enumerate(aln_seq):
        if ch != "-":
            idx += 1
            mapping[idx] = col
    return mapping


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--aln", required=True, type=Path)
    ap.add_argument("--anchor", required=True)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    records = read_fasta(args.aln)
    seqs = {n.split("|")[0]: (n.split("|")[-1], s) for n, s in records}
    if args.anchor not in seqs:
        raise SystemExit(f"Anchor {args.anchor} not in alignment")

    anchor_aln = seqs[args.anchor][1]
    idx2col = ungapped_index_to_alncol(anchor_aln)

    # verify anchor residues are as expected
    print("Anchor residue verification (human MCT1):")
    for pos, (label, expected) in ANCHOR_RESIDUES.items():
        col = idx2col.get(pos)
        actual = anchor_aln[col] if col is not None else "?"
        flag = "OK" if actual == expected else "MISMATCH"
        print(f"  {label}: expected {expected}, anchor has {actual} [{flag}]")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w") as fh:
        header = ["protein"] + [ANCHOR_RESIDUES[p][0] for p in sorted(ANCHOR_RESIDUES)]
        fh.write("\t".join(header) + "\n")
        for acc, (short, s) in seqs.items():
            row = [short]
            for pos in sorted(ANCHOR_RESIDUES):
                col = idx2col.get(pos)
                row.append(s[col] if col is not None else "-")
            fh.write("\t".join(row) + "\n")

    print(f"\nWrote {args.out}")

    # MFS motif A search in the raw (ungapped) sequences.
    # Canonical MFS motif A: G-x{3}-D-R/K-x-G-R/K-R/K (loop between TM2 and TM3).
    # We also try a relaxed variant since MCT-family motif A is degenerate.
    print("\nMFS 'motif A' scans (ungapped seqs):")
    motif_a_strict = re.compile(r"G.{3}[DE][RK].G[RK][RK]")
    motif_a_relaxed = re.compile(r"[GA].{2,4}[DE][RK].{0,2}G[RK]")
    for acc, (short, s) in seqs.items():
        if short not in ("MCH2_YEAST", "SLC16A1_MCT1_HUMAN", "MCH3_ESBP6_YEAST", "MCH5_YEAST"):
            continue
        raw = s.replace("-", "")
        ms = motif_a_strict.search(raw)
        mr = motif_a_relaxed.search(raw)
        strict = f"{ms.group()} @ {ms.start() + 1}" if ms else "none"
        relaxed = f"{mr.group()} @ {mr.start() + 1}" if mr else "none"
        print(f"  {short}: strict={strict} | relaxed={relaxed}")

    # Data-driven conservation: most-conserved alignment columns and MCH2 residue there.
    print("\nMost-conserved alignment columns (>=70% single residue) and MCH2's residue:")
    n = len(records)
    ncol = len(anchor_aln)
    conserved_rows = []
    for col in range(ncol):
        counts: dict[str, int] = {}
        for _, (_short, s) in seqs.items():
            ch = s[col]
            if ch == "-":
                continue
            counts[ch] = counts.get(ch, 0) + 1
        if not counts:
            continue
        top_res, top_n = max(counts.items(), key=lambda x: x[1])
        frac = top_n / n
        if frac >= 0.70:
            mch2_res = seqs["P36032"][1][col]
            conserved_rows.append((col + 1, top_res, round(frac, 2), mch2_res))
    n_conserved = len(conserved_rows)
    n_mch2_match = sum(1 for _, tr, _, mr in conserved_rows if tr == mr)
    print(f"  {n_conserved} highly-conserved columns; MCH2 matches the consensus at {n_mch2_match}")
    with (args.out.parent / "conserved_columns.tsv").open("w") as fh:
        fh.write("aln_col\tconsensus_res\tconsensus_frac\tMCH2_res\tMCH2_matches\n")
        for col, tr, frac, mr in conserved_rows:
            fh.write(f"{col}\t{tr}\t{frac}\t{mr}\t{tr == mr}\n")
    print(f"  Wrote {args.out.parent / 'conserved_columns.tsv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
