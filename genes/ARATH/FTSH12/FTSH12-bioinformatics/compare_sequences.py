#!/usr/bin/env python3
"""Map the A0A1P8ARD2 FTSH12 gene-model product onto the reviewed FTSH12 reference (Q9SAJ3).

Inputs (public database records only; no prediction output is used):
- ../FTSH12-uniprot.txt                UniProt flat file for A0A1P8ARD2 (sequence)
- ../FTSH12-same-gene-reference.json   UniProt REST JSON for reviewed Arabidopsis FTSH12 (Q9SAJ3)

Run from this directory: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not protein expression or activity.
"""

import json
import re
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
FEATURE_TYPES = {
    "Active site",
    "Binding site",
    "Transmembrane",
    "Signal",
    "Transit peptide",
    "Domain",
    "Motif",
}


def parse_uniprot_flat(path: Path) -> tuple[str, str]:
    """Return (accession, sequence) from a UniProt flat file."""
    text = path.read_text()
    acc = re.search(r"^AC   (\w+);", text, re.M).group(1)
    sq = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//")[0]
    return acc, re.sub(r"[^A-Z]", "", sq)


def main() -> None:
    sel_acc, b = parse_uniprot_flat(GENE_DIR / "FTSH12-uniprot.txt")
    reference = json.loads((GENE_DIR / "FTSH12-same-gene-reference.json").read_text())["record"]
    a = reference["sequence"]["value"]

    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]

    pairs: dict[int, int] = {}
    segments = []
    for (x, y), (u, v) in zip(aln.aligned[0], aln.aligned[1]):
        x, y, u, v = map(int, (x, y, u, v))
        segments.append(
            {
                "reference_start": x + 1,
                "reference_end": y,
                "target_start": u + 1,
                "target_end": v,
                "identical": sum(a[x + k] == b[u + k] for k in range(y - x)),
            }
        )
        for k in range(y - x):
            pairs[x + k + 1] = u + k + 1

    # Longest identical prefix: where the two gene models diverge.
    prefix = 0
    while prefix < min(len(a), len(b)) and a[prefix] == b[prefix]:
        prefix += 1

    features = []
    for f in reference.get("features", []):
        if f["type"] not in FEATURE_TYPES:
            continue
        start = f["location"]["start"].get("value")
        end = f["location"]["end"].get("value")
        if not start or not end:
            continue
        mapped = [(p, pairs[p]) for p in range(start, end + 1) if p in pairs]
        features.append(
            {
                "type": f["type"],
                "description": f.get("description", ""),
                "reference_start": start,
                "reference_end": end,
                "mapped_count": len(mapped),
                "length": end - start + 1,
                "identical_count": sum(a[p - 1] == b[q - 1] for p, q in mapped),
                "target_positions": [q for _, q in mapped],
            }
        )

    out = {
        "selected_accession": sel_acc,
        "selected_length": len(b),
        "reference_accession": reference["primaryAccession"],
        "reference_length": len(a),
        "identical_prefix_length": prefix,
        "reference_c_terminus_after_divergence": a[prefix:],
        "selected_c_terminus_after_divergence": b[prefix:],
        "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
        "aligned_segments": segments,
        "reference_features": features,
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
    (HERE / "alignment.txt").write_text(str(aln) + "\n")

    lines = [
        "# FTSH12: A0A1P8ARD2 gene-model product vs reviewed FTSH12 (Q9SAJ3)",
        "",
        f"Selected {sel_acc} has {len(b)} residues; reference {out['reference_accession']} has {len(a)} residues.",
        "",
        f"The two sequences are identical over residues 1–{prefix}. After that the reference continues with "
        f"`{a[prefix:]}` ({len(a) - prefix} aa) whereas {sel_acc} ends with `{b[prefix:]}` ({len(b) - prefix} aa).",
        "",
        out["method"] + ".",
        "",
        "| Reference interval | Selected interval | Identical residues |",
        "|---|---|---|",
    ]
    for s in segments:
        lines.append(f"| {s['reference_start']}–{s['reference_end']} | {s['target_start']}–{s['target_end']} | {s['identical']} |")
    lines += [
        "",
        "Reference feature mapping (sequence coverage does not establish retained function):",
        "",
        "| Reference feature | Interval | Mapped / length | Identical |",
        "|---|---|---|---|",
    ]
    for f in features:
        lines.append(
            f"| {f['type']}: {f['description']} | {f['reference_start']}–{f['reference_end']} | {f['mapped_count']} / {f['length']} | {f['identical_count']} |"
        )
    lines += [
        "",
        "Inputs: `FTSH12-uniprot.txt` (selected sequence) and `FTSH12-same-gene-reference.json` (UniProt Q9SAJ3). "
        "Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.",
        "",
    ]
    (HERE / "RESULTS.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
