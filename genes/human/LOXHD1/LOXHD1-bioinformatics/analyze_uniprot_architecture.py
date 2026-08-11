#!/usr/bin/env python3
"""Analyze UniProt domain repeats and isoform sequence changes.

The script is intentionally generic: all input and output locations are supplied
on the command line, and no gene-specific coordinates or expected results are
embedded in the implementation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Feature:
    kind: str
    start: int
    end: int
    note: str
    feature_id: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Map UniProt isoform changes onto annotated domains and compare domain sequences."
    )
    parser.add_argument("--uniprot", type=Path, required=True, help="UniProt flat-file input")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output directory")
    parser.add_argument(
        "--repeat-label",
        default="PLAT",
        help="Case-insensitive substring selecting domains for pairwise comparison",
    )
    return parser.parse_args()


def parse_uniprot(path: Path) -> tuple[str, str, dict[str, str], list[Feature], str]:
    text = path.read_text(encoding="utf-8")
    accession_match = re.search(r"^AC\s+([^;]+);", text, re.MULTILINE)
    if not accession_match:
        raise ValueError(f"No primary accession found in {path}")
    accession = accession_match.group(1)

    length_match = re.search(r"^ID\s+\S+\s+.*?\s+(\d+) AA\.", text, re.MULTILINE)
    if not length_match:
        raise ValueError(f"No sequence length found in {path}")
    declared_length = int(length_match.group(1))

    isoforms: dict[str, str] = {}
    current_isoform = ""
    for line in text.splitlines():
        if line.startswith("CC       Name="):
            current_isoform = line.split("Name=", 1)[1].split(";", 1)[0].strip()
        elif current_isoform and line.startswith("CC         IsoId="):
            isoform_id = line.split("IsoId=", 1)[1].split(";", 1)[0].strip()
            isoforms[current_isoform] = isoform_id

    features: list[Feature] = []
    current: dict[str, object] | None = None
    feature_re = re.compile(r"^FT\s+([A-Z_]+)\s+(\d+)(?:\.\.(\d+))?\s*$")
    for line in text.splitlines():
        match = feature_re.match(line)
        if match:
            if current is not None:
                features.append(Feature(**current))
            current = None
            if match.group(1) in {"DOMAIN", "VAR_SEQ"}:
                current = {
                    "kind": match.group(1),
                    "start": int(match.group(2)),
                    "end": int(match.group(3) or match.group(2)),
                    "note": "",
                    "feature_id": "",
                }
        elif current is not None and line.startswith("FT"):
            note_match = re.search(r'/note="(.*)"', line)
            id_match = re.search(r'/id="(.*)"', line)
            if note_match:
                current["note"] = note_match.group(1)
            elif id_match:
                current["feature_id"] = id_match.group(1)
        elif current is not None:
            features.append(Feature(**current))
            current = None
    if current is not None:
        features.append(Feature(**current))

    sequence_lines: list[str] = []
    in_sequence = False
    for line in text.splitlines():
        if line.startswith("SQ   SEQUENCE"):
            in_sequence = True
            continue
        if in_sequence and line == "//":
            break
        if in_sequence:
            sequence_lines.append(re.sub(r"[^A-Z]", "", line))
    sequence = "".join(sequence_lines)
    if len(sequence) != declared_length:
        raise ValueError(
            f"Parsed sequence length {len(sequence)} does not match declared length {declared_length}"
        )
    return accession, str(declared_length), isoforms, features, sequence


def global_identity(first: str, second: str) -> tuple[int, int, float]:
    """Return matches, aligned length, and identity from a global alignment.

    Scoring is match +1, mismatch 0, gap -1. Only two score rows are retained;
    match and alignment-length tie-breakers make the reported identity stable.
    """

    previous = [(-index, 0, index) for index in range(len(second) + 1)]
    for i, aa_first in enumerate(first, start=1):
        current = [(-i, 0, i)]
        for j, aa_second in enumerate(second, start=1):
            diagonal = previous[j - 1]
            candidates = [
                (
                    diagonal[0] + (1 if aa_first == aa_second else 0),
                    diagonal[1] + (1 if aa_first == aa_second else 0),
                    diagonal[2] + 1,
                ),
                (previous[j][0] - 1, previous[j][1], previous[j][2] + 1),
                (current[j - 1][0] - 1, current[j - 1][1], current[j - 1][2] + 1),
            ]
            current.append(max(candidates, key=lambda item: (item[0], item[1], -item[2])))
        previous = current
    _, matches, aligned_length = previous[-1]
    identity = matches / aligned_length if aligned_length else 0.0
    return matches, aligned_length, identity


def affected_isoforms(note: str) -> set[str]:
    return set(re.findall(r"isoform\s+([A-Za-z0-9_-]+)", note, flags=re.IGNORECASE))


def overlap_length(first: Feature, second: Feature) -> int:
    return max(0, min(first.end, second.end) - max(first.start, second.start) + 1)


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    if not args.uniprot.is_file():
        raise FileNotFoundError(args.uniprot)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    accession, declared_length, isoforms, features, sequence = parse_uniprot(args.uniprot)
    domains = [feature for feature in features if feature.kind == "DOMAIN"]
    changes = [feature for feature in features if feature.kind == "VAR_SEQ"]
    selected = [domain for domain in domains if args.repeat_label.lower() in domain.note.lower()]

    architecture_rows = [
        {
            "domain_index": index,
            "start": domain.start,
            "end": domain.end,
            "length": domain.end - domain.start + 1,
            "note": domain.note,
            "selected_repeat": str(domain in selected).lower(),
        }
        for index, domain in enumerate(domains, start=1)
    ]
    write_tsv(
        args.output_dir / "domains.tsv",
        ["domain_index", "start", "end", "length", "note", "selected_repeat"],
        architecture_rows,
    )

    isoform_rows: list[dict[str, object]] = []
    isoform_names = list(isoforms) or ["displayed"]
    for isoform_name in isoform_names:
        isoform_changes = [change for change in changes if isoform_name in affected_isoforms(change.note)]
        for repeat_index, domain in enumerate(selected, start=1):
            overlaps = [(change, overlap_length(domain, change)) for change in isoform_changes]
            overlaps = [(change, overlap) for change, overlap in overlaps if overlap]
            missing_overlap = sum(
                overlap for change, overlap in overlaps if change.note.lower().startswith("missing")
            )
            has_replacement = any("->" in change.note for change, _ in overlaps)
            domain_length = domain.end - domain.start + 1
            if missing_overlap >= domain_length:
                status = "LOST"
            elif missing_overlap > 0:
                status = "PARTIAL"
            elif has_replacement:
                status = "ALTERED"
            else:
                status = "RETAINED"
            isoform_rows.append(
                {
                    "isoform_name": isoform_name,
                    "isoform_id": isoforms.get(isoform_name, ""),
                    "repeat_index": repeat_index,
                    "domain_start": domain.start,
                    "domain_end": domain.end,
                    "status": status,
                    "affected_residues": missing_overlap,
                    "overlapping_changes": "; ".join(
                        f"{change.feature_id}:{change.start}-{change.end}:{change.note}"
                        for change, _ in overlaps
                    ),
                }
            )
    write_tsv(
        args.output_dir / "isoform_repeat_effects.tsv",
        [
            "isoform_name",
            "isoform_id",
            "repeat_index",
            "domain_start",
            "domain_end",
            "status",
            "overlapping_changes",
            "affected_residues",
        ],
        isoform_rows,
    )

    similarity_rows: list[dict[str, object]] = []
    for first_index, first_domain in enumerate(selected, start=1):
        first_sequence = sequence[first_domain.start - 1 : first_domain.end]
        for second_index in range(first_index + 1, len(selected) + 1):
            second_domain = selected[second_index - 1]
            second_sequence = sequence[second_domain.start - 1 : second_domain.end]
            matches, aligned_length, identity = global_identity(first_sequence, second_sequence)
            similarity_rows.append(
                {
                    "repeat_1": first_index,
                    "repeat_2": second_index,
                    "matches": matches,
                    "aligned_length": aligned_length,
                    "identity_fraction": f"{identity:.6f}",
                }
            )
    write_tsv(
        args.output_dir / "repeat_pairwise_identity.tsv",
        ["repeat_1", "repeat_2", "matches", "aligned_length", "identity_fraction"],
        similarity_rows,
    )

    status_counts: dict[str, int] = {}
    for row in isoform_rows:
        key = f"{row['isoform_name']}:{row['status']}"
        status_counts[key] = status_counts.get(key, 0) + 1
    identities = [float(row["identity_fraction"]) for row in similarity_rows]
    summary = {
        "accession": accession,
        "declared_sequence_length": int(declared_length),
        "input_sha256": hashlib.sha256(args.uniprot.read_bytes()).hexdigest(),
        "repeat_label": args.repeat_label,
        "annotated_domain_count": len(domains),
        "selected_repeat_count": len(selected),
        "isoforms": isoforms,
        "isoform_repeat_status_counts": status_counts,
        "pairwise_comparison_count": len(similarity_rows),
        "pairwise_identity_min": min(identities) if identities else None,
        "pairwise_identity_median": (
            sorted(identities)[len(identities) // 2] if identities else None
        ),
        "pairwise_identity_max": max(identities) if identities else None,
        "sequence_changes": [asdict(change) for change in changes],
        "python_version": platform.python_version(),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
