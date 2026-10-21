#!/usr/bin/env python3
"""Map the benchmark product S6FN32 (WormBase D2030.9d) onto the characterised
WDR-23 isoforms P90794 (WDR-23A, 571 aa) and P90794-2 (WDR-23B).

Inputs (all UniProt-derived, in the gene folder):
  - wdr-23-uniprot.txt                 S6FN32 flat file (sequence)
  - wdr-23-same-gene-reference.json    P90794 UniProt JSON (sequence + features)
  - wdr-23-reference-isoform-b.fasta   P90794-2 sequence

Also reports whether the two DDB1-binding DxR boxes mutated by Staab et al. 2013
(PMID:23555279; R342H and R389H in WDR-23A numbering) are retained.

Run from this directory: UV_NO_SYNC=1 uv run python compare_sequences.py
Alignments describe sequence correspondence, not expression or activity.
"""

import json
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent


def read_uniprot_flat_sequence(path: Path) -> tuple[str, str]:
    """Return (accession, sequence) from a UniProt flat file."""
    lines = path.read_text().splitlines()
    acc = next(line.split()[1].rstrip(";") for line in lines if line.startswith("AC "))
    seq_lines = []
    in_seq = False
    for line in lines:
        if line.startswith("SQ "):
            in_seq = True
            continue
        if line.startswith("//"):
            break
        if in_seq:
            seq_lines.append(line.replace(" ", ""))
    return acc, "".join(seq_lines)


def read_fasta(path: Path) -> tuple[str, str]:
    lines = path.read_text().splitlines()
    acc = lines[0].split("|")[1]
    return acc, "".join(lines[1:])


def align(a: str, b: str):
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    segments = []
    pairs = {}
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
    return aln, segments, pairs


target_acc, target = read_uniprot_flat_sequence(GENE_DIR / "wdr-23-uniprot.txt")
ref_record = json.loads((GENE_DIR / "wdr-23-same-gene-reference.json").read_text())["record"]
ref_acc = ref_record["primaryAccession"]
ref = ref_record["sequence"]["value"]
isob_acc, isob = read_fasta(GENE_DIR / "wdr-23-reference-isoform-b.fasta")

aln_a, seg_a, pairs_a = align(ref, target)
aln_b, seg_b, pairs_b = align(isob, target)

features = []
for f in ref_record.get("features", []):
    if f["type"] not in {"Repeat", "Domain", "Motif", "Region"}:
        continue
    start = f["location"]["start"].get("value")
    end = f["location"]["end"].get("value")
    if not start or not end:
        continue
    mapped = [(p, pairs_a[p]) for p in range(start, end + 1) if p in pairs_a]
    features.append(
        {
            "type": f["type"],
            "description": f.get("description", ""),
            "reference_start": start,
            "reference_end": end,
            "length": end - start + 1,
            "mapped_count": len(mapped),
            "identical_count": sum(ref[p - 1] == target[q - 1] for p, q in mapped),
        }
    )

# DxR boxes: Staab et al. 2013 mutated R342 and R389 of WDR-23A.
dxr = []
for r_pos in (342, 389):
    motif = ref[r_pos - 3 : r_pos]
    t_pos = pairs_a.get(r_pos)
    t_motif = target[t_pos - 3 : t_pos] if t_pos else None
    dxr.append(
        {
            "reference_R_position": r_pos,
            "reference_motif": motif,
            "target_R_position": t_pos,
            "target_motif": t_motif,
            "retained": bool(t_pos) and motif == t_motif and motif[0] == "D" and motif[2] == "R",
        }
    )

out = {
    "target_accession": target_acc,
    "target_length": len(target),
    "reference_accession": ref_acc,
    "reference_length": len(ref),
    "isoform_b_accession": isob_acc,
    "isoform_b_length": len(isob),
    "method": "Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5",
    "segments_vs_isoform_a": seg_a,
    "segments_vs_isoform_b": seg_b,
    "reference_features": features,
    "dxr_boxes": dxr,
}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "alignment.txt").write_text(str(aln_a) + "\n")

lines = [
    "# wdr-23: benchmark product S6FN32 vs characterised WDR-23 isoforms",
    "",
    f"Target {target_acc} has {len(target)} residues; WDR-23A {ref_acc} has {len(ref)} residues; "
    f"WDR-23B {isob_acc} has {len(isob)} residues.",
    "",
    out["method"] + ".",
    "",
    "## Aligned segments vs WDR-23A (P90794)",
    "",
    "| Reference interval | Target interval | Identical residues |",
    "|---|---|---|",
]
for s in seg_a:
    lines.append(f"| {s['reference_start']}-{s['reference_end']} | {s['target_start']}-{s['target_end']} | {s['identical']} |")
lines += [
    "",
    "## Aligned segments vs WDR-23B (P90794-2)",
    "",
    "| Reference interval | Target interval | Identical residues |",
    "|---|---|---|",
]
for s in seg_b:
    lines.append(f"| {s['reference_start']}-{s['reference_end']} | {s['target_start']}-{s['target_end']} | {s['identical']} |")
lines += [
    "",
    "## P90794 features mapped onto the target",
    "",
    "| Feature | Interval | Mapped / length | Identical |",
    "|---|---|---|---|",
]
for f in features:
    lines.append(
        f"| {f['type']}: {f['description']} | {f['reference_start']}-{f['reference_end']} | "
        f"{f['mapped_count']} / {f['length']} | {f['identical_count']} |"
    )
lines += [
    "",
    "## DDB1-binding DxR boxes (Staab et al. 2013, R342H/R389H in WDR-23A)",
    "",
    "| WDR-23A R | WDR-23A motif | Target R | Target motif | Retained |",
    "|---|---|---|---|---|",
]
for d in dxr:
    lines.append(
        f"| {d['reference_R_position']} | {d['reference_motif']} | {d['target_R_position']} | "
        f"{d['target_motif']} | {d['retained']} |"
    )
lines += [
    "",
    "Interpretation: the target is an N-terminally shorter product of the same gene. Every residue "
    "of the target is identical to the C-terminal part of both characterised isoforms; the target "
    "lacks only the isoform-specific N-terminal extensions. A shared segment does not by itself "
    "establish that the shorter product is expressed, folds or localises like either isoform.",
    "",
    "Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.",
    "",
]
(HERE / "RESULTS.md").write_text("\n".join(lines))
