#!/usr/bin/env python3
"""Compare protein sequences declared in a manifest.

The script reads UniProt flat files from the repository or fetches explicit
UniProt accessions, reports database cross-references and requested motifs,
and computes global pairwise sequence identities. Biological interpretation
belongs in RESULTS.md, not in this program.
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.request import urlopen

from Bio import Align


@dataclass(frozen=True)
class ProteinRecord:
    label: str
    expected_role: str
    source: str
    accession: str
    sequence: str
    interpro_ids: tuple[str, ...]
    panther_ids: tuple[str, ...]
    kegg_ids: tuple[str, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument(
        "--motif",
        action="append",
        default=[],
        metavar="NAME=REGEX",
        help="Named regular expression to locate; may be supplied repeatedly.",
    )
    parser.add_argument("--features-output", type=Path, required=True)
    parser.add_argument("--pairwise-output", type=Path, required=True)
    parser.add_argument("--kegg-output", type=Path, required=True)
    return parser.parse_args()


def parse_motifs(values: list[str]) -> dict[str, re.Pattern[str]]:
    motifs: dict[str, re.Pattern[str]] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"motif must use NAME=REGEX syntax: {value}")
        name, pattern = value.split("=", 1)
        if not name or name in motifs:
            raise ValueError(f"motif name must be non-empty and unique: {name}")
        motifs[name] = re.compile(pattern)
    return motifs


def parse_uniprot_flatfile(text: str, label: str, expected_role: str, source: str) -> ProteinRecord:
    accession = ""
    sequence_lines: list[str] = []
    interpro_ids: list[str] = []
    panther_ids: list[str] = []
    kegg_ids: list[str] = []
    in_sequence = False

    for line in text.splitlines():
        if line.startswith("AC   ") and not accession:
            accession = line[5:].split(";", 1)[0].strip()
        elif line.startswith("DR   InterPro;"):
            interpro_ids.append(line.split(";", 2)[1].strip())
        elif line.startswith("DR   PANTHER;"):
            panther_ids.append(line.split(";", 2)[1].strip())
        elif line.startswith("DR   KEGG;"):
            kegg_ids.append(line.split(";", 2)[1].strip())
        elif line.startswith("SQ   SEQUENCE"):
            in_sequence = True
        elif line == "//":
            in_sequence = False
        elif in_sequence:
            sequence_lines.append(re.sub(r"[^A-Z]", "", line))

    sequence = "".join(sequence_lines)
    if not accession or not sequence:
        raise ValueError(f"could not parse accession and sequence from {source}")
    return ProteinRecord(
        label=label,
        expected_role=expected_role,
        source=source,
        accession=accession,
        sequence=sequence,
        interpro_ids=tuple(sorted(set(interpro_ids))),
        panther_ids=tuple(sorted(set(panther_ids))),
        kegg_ids=tuple(sorted(set(kegg_ids))),
    )


def load_records(manifest: Path, repo_root: Path) -> list[ProteinRecord]:
    records: list[ProteinRecord] = []
    with manifest.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        required = {"label", "source_type", "source", "expected_role"}
        if set(reader.fieldnames or []) != required:
            raise ValueError(f"manifest columns must be exactly {sorted(required)}")
        for row in reader:
            source_type = row["source_type"]
            source = row["source"]
            if source_type == "local_uniprot_flatfile":
                text = (repo_root / source).read_text(encoding="utf-8")
            elif source_type == "uniprot_accession":
                url = f"https://rest.uniprot.org/uniprotkb/{source}.txt"
                with urlopen(url, timeout=60) as response:
                    text = response.read().decode("utf-8")
            else:
                raise ValueError(f"unsupported source_type: {source_type}")
            records.append(
                parse_uniprot_flatfile(
                    text,
                    label=row["label"],
                    expected_role=row["expected_role"],
                    source=source,
                )
            )
    if len(records) < 2:
        raise ValueError("manifest must contain at least two proteins")
    return records


def motif_positions(sequence: str, pattern: re.Pattern[str]) -> str:
    return ";".join(str(match.start() + 1) for match in pattern.finditer(sequence))


def write_features(
    records: list[ProteinRecord],
    motifs: dict[str, re.Pattern[str]],
    output: Path,
) -> None:
    fields = [
        "label",
        "accession",
        "expected_role",
        "source",
        "length",
        "interpro_ids",
        "panther_ids",
        "kegg_ids",
        *[f"motif_{name}_start_positions" for name in motifs],
    ]
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for record in records:
            row = {
                "label": record.label,
                "accession": record.accession,
                "expected_role": record.expected_role,
                "source": record.source,
                "length": len(record.sequence),
                "interpro_ids": ";".join(record.interpro_ids),
                "panther_ids": ";".join(record.panther_ids),
                "kegg_ids": ";".join(record.kegg_ids),
            }
            for name, pattern in motifs.items():
                row[f"motif_{name}_start_positions"] = motif_positions(
                    record.sequence, pattern
                )
            writer.writerow(row)


def write_pairwise(records: list[ProteinRecord], output: Path) -> None:
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1.0
    aligner.mismatch_score = 0.0
    aligner.open_gap_score = -1.0
    aligner.extend_gap_score = -0.1

    fields = [
        "query_label",
        "query_accession",
        "target_label",
        "target_accession",
        "matches",
        "aligned_residues",
        "global_identity_percent",
        "alignment_score",
    ]
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for index, query in enumerate(records):
            for target in records[index + 1 :]:
                alignment = aligner.align(query.sequence, target.sequence)[0]
                query_aligned = str(alignment[0])
                target_aligned = str(alignment[1])
                residue_pairs = [
                    (left, right)
                    for left, right in zip(query_aligned, target_aligned)
                    if left != "-" and right != "-"
                ]
                matches = sum(left == right for left, right in residue_pairs)
                aligned_residues = len(residue_pairs)
                writer.writerow(
                    {
                        "query_label": query.label,
                        "query_accession": query.accession,
                        "target_label": target.label,
                        "target_accession": target.accession,
                        "matches": matches,
                        "aligned_residues": aligned_residues,
                        "global_identity_percent": f"{100 * matches / aligned_residues:.2f}",
                        "alignment_score": f"{alignment.score:.2f}",
                    }
                )


def write_kegg_orthology(records: list[ProteinRecord], output: Path) -> None:
    fields = ["label", "accession", "kegg_gene", "kegg_orthology"]
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for record in records:
            for kegg_id in record.kegg_ids:
                url = f"https://rest.kegg.jp/link/ko/{kegg_id}"
                with urlopen(url, timeout=60) as response:
                    links = response.read().decode("utf-8").splitlines()
                for link in links:
                    gene_id, orthology_id = link.split("\t", 1)
                    writer.writerow(
                        {
                            "label": record.label,
                            "accession": record.accession,
                            "kegg_gene": gene_id,
                            "kegg_orthology": orthology_id,
                        }
                    )


def main() -> None:
    args = parse_args()
    motifs = parse_motifs(args.motif)
    records = load_records(args.manifest, args.repo_root.resolve())
    write_features(records, motifs, args.features_output)
    write_pairwise(records, args.pairwise_output)
    write_kegg_orthology(records, args.kegg_output)


if __name__ == "__main__":
    main()
