"""Check whether the C-terminal GTP cyclohydrolase II-fold domains of KT2440
ribAB-I (Q88QH7, PP_0516) and ribAB-II (Q88GB1, PP_3813) retain the catalytic
residues of the monofunctional KT2440 GTP cyclohydrolase II RibA (Q88QH1, PP_0522).

Reference residues are read from the RibA UniProt flat file (HAMAP MF_00179
ACT_SITE and zinc BINDING features). Each query C-terminal region (from the
InterPro/Pfam GTP_cyclohydro2 DOMAIN feature start to the C-terminus) is aligned
globally-local to the RibA sequence with BLOSUM62, and the aligned residue at
each reference position is reported. Sequences come from the cached UniProt
files; nothing is hardcoded except file paths.

Run from the repository root:
    uv run python genes/PSEPK/ribAB-I/ribAB-I-bioinformatics/check_gtpchii_residues.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
REF = ROOT / "genes/PSEPK/ribA/ribA-uniprot.txt"
QUERIES = {
    "ribAB-I (Q88QH7)": ROOT / "genes/PSEPK/ribAB-I/ribAB-I-uniprot.txt",
    "ribAB-II (Q88GB1)": ROOT / "genes/PSEPK/ribAB-II/ribAB-II-uniprot.txt",
}


def read_sequence(path: Path) -> str:
    """Return the protein sequence from a UniProt flat file."""
    text = path.read_text()
    block = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", block)


def read_features(path: Path) -> list[tuple[str, int, str]]:
    """Return (type, position, note/ligand) for single-residue ACT_SITE and zinc BINDING features."""
    feats: list[tuple[str, int, str]] = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   (ACT_SITE|BINDING)\s+(\d+)\s*$", line)
        if not m:
            continue
        qual = " ".join(lines[i + 1 : i + 3])
        if m.group(1) == "BINDING" and "Zn(2+)" not in qual:
            continue
        label = re.search(r'/(?:note|ligand)="([^"]+)"', qual)
        feats.append((m.group(1), int(m.group(2)), label.group(1) if label else ""))
    return feats


def domain_start(path: Path) -> int:
    """Return the start of the first DOMAIN feature (the GTP_cyclohydro2 C-terminal domain)."""
    m = re.search(r"FT   DOMAIN\s+(\d+)\.\.(\d+)", path.read_text())
    if not m:
        raise SystemExit(f"no DOMAIN feature in {path}")
    return int(m.group(1))


def main() -> None:
    ref_seq = read_sequence(REF)
    feats = read_features(REF)
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "local"
    results: dict[str, dict] = {}
    for name, path in QUERIES.items():
        seq = read_sequence(path)
        start = domain_start(path)
        region = seq[start - 1 :]
        aln = aligner.align(ref_seq, region)[0]
        mapping: dict[int, int] = {}
        for (rs, re_), (qs, qe) in zip(*aln.aligned):
            for k in range(re_ - rs):
                mapping[int(rs + k + 1)] = int(qs + k + start)
        ident = sum(
            1
            for (rs, re_), (qs, qe) in zip(*aln.aligned)
            for k in range(re_ - rs)
            if ref_seq[rs + k] == region[qs + k]
        )
        aligned_len = sum(re_ - rs for (rs, re_), _ in zip(*aln.aligned))
        rows = []
        for ftype, pos, label in feats:
            qpos = mapping.get(pos)
            rows.append(
                {
                    "feature": ftype,
                    "ribA_residue": f"{ref_seq[pos - 1]}{pos}",
                    "label": label,
                    "query_residue": f"{seq[qpos - 1]}{qpos}" if qpos else None,
                    "conserved": bool(qpos) and seq[qpos - 1] == ref_seq[pos - 1],
                }
            )
        results[name] = {
            "query_length": len(seq),
            "gtpchii_domain_start": start,
            "local_alignment_score": float(aln.score),
            "aligned_ribA_span": [int(aln.aligned[0][0][0]) + 1, int(aln.aligned[0][-1][1])],
            "aligned_positions": int(aligned_len),
            "identical_positions": ident,
            "cysteines_in_gtpchii_region": [i + start for i, c in enumerate(region) if c == "C"],
            "residues": rows,
        }
    json.dump(results, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
