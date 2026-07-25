#!/usr/bin/env python3
"""Compare MTHFR-family sequences and retrieve InterPro domain coordinates."""

from __future__ import annotations

import argparse
import csv
import json
import urllib.parse
import urllib.request
from io import StringIO
from itertools import combinations
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.SeqRecord import SeqRecord


USER_AGENT = "ai-gene-review/PP_4638 comparative analysis"


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def parse_local(spec: str) -> SeqRecord:
    accession, raw_path = spec.split("=", 1)
    path = Path(raw_path)
    record = SeqIO.read(path, "swiss")
    record.id = accession
    record.name = accession
    record.description = f"{accession} from {path}"
    return record


def fetch_uniprot(accession: str) -> SeqRecord:
    url = f"https://rest.uniprot.org/uniprotkb/{urllib.parse.quote(accession)}.fasta"
    text = fetch_text(url)
    return next(SeqIO.parse(StringIO(text), "fasta"))


def fetch_ncbi(accession: str) -> SeqRecord:
    query = urllib.parse.urlencode(
        {"db": "protein", "id": accession, "rettype": "fasta", "retmode": "text"}
    )
    text = fetch_text(
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{query}"
    )
    return next(SeqIO.parse(StringIO(text), "fasta"))


def interpro_matches(accession: str, sequence: str) -> list[dict[str, object]]:
    url = (
        "https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/"
        f"{urllib.parse.quote(accession)}/?page_size=200"
    )
    payload = json.loads(fetch_text(url))
    rows: list[dict[str, object]] = []
    for result in payload.get("results", []):
        metadata = result.get("metadata", {})
        for protein in result.get("proteins", []):
            for location in protein.get("entry_protein_locations", []):
                for fragment in location.get("fragments", []):
                    start = int(fragment.get("start"))
                    end = int(fragment.get("end"))
                    segment = sequence[start - 1 : end]
                    rows.append(
                        {
                            "protein": accession,
                            "database": metadata.get("source_database", ""),
                            "entry": metadata.get("accession", ""),
                            "name": metadata.get("name") or "",
                            "start": start,
                            "end": end,
                            "length": len(segment),
                            "cysteine_count": segment.count("C"),
                        }
                    )
    return rows


def alignment_row(
    left: SeqRecord, right: SeqRecord, aligner: PairwiseAligner
) -> dict[str, object]:
    alignment = aligner.align(left.seq, right.seq)[0]
    left_blocks, right_blocks = alignment.aligned
    aligned_residues = 0
    identical_residues = 0
    for (left_start, left_end), (right_start, right_end) in zip(
        left_blocks, right_blocks, strict=True
    ):
        left_segment = left.seq[left_start:left_end]
        right_segment = right.seq[right_start:right_end]
        aligned_residues += len(left_segment)
        identical_residues += sum(a == b for a, b in zip(left_segment, right_segment))

    return {
        "protein_1": left.id,
        "protein_2": right.id,
        "length_1": len(left.seq),
        "length_2": len(right.seq),
        "score": f"{alignment.score:.1f}",
        "aligned_residues": aligned_residues,
        "identity_percent": f"{100 * identical_residues / aligned_residues:.2f}",
        "coverage_1_percent": f"{100 * aligned_residues / len(left.seq):.2f}",
        "coverage_2_percent": f"{100 * aligned_residues / len(right.seq):.2f}",
        "start_1": int(left_blocks[0][0]) + 1,
        "end_1": int(left_blocks[-1][1]),
        "start_2": int(right_blocks[0][0]) + 1,
        "end_2": int(right_blocks[-1][1]),
    }


def write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows produced for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local",
        action="append",
        default=[],
        metavar="ACCESSION=UNIPROT_TXT",
        help="Local UniProt flat file; repeat for each protein.",
    )
    parser.add_argument("--uniprot-reference", action="append", default=[])
    parser.add_argument("--ncbi-reference", action="append", default=[])
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    if len(args.local) < 2:
        parser.error("Provide at least two --local records so the workflow tests a comparator.")

    local_records = [parse_local(spec) for spec in args.local]
    records = [
        *local_records,
        *(fetch_uniprot(accession) for accession in args.uniprot_reference),
        *(fetch_ncbi(accession) for accession in args.ncbi_reference),
    ]
    for record, accession in zip(
        records[len(local_records) :],
        [*args.uniprot_reference, *args.ncbi_reference],
        strict=True,
    ):
        record.id = accession
        record.name = accession

    args.output_dir.mkdir(parents=True, exist_ok=True)
    SeqIO.write(records, args.output_dir / "sequences.fasta", "fasta")

    summary_rows = [
        {
            "protein": record.id,
            "length": len(record.seq),
            "cysteine_count": str(record.seq).count("C"),
            "cysteine_percent": f"{100 * str(record.seq).count('C') / len(record.seq):.2f}",
        }
        for record in records
    ]
    write_tsv(args.output_dir / "sequence_summary.tsv", summary_rows)

    aligner = PairwiseAligner(mode="local")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    alignment_rows = [
        alignment_row(left, right, aligner) for left, right in combinations(records, 2)
    ]
    write_tsv(args.output_dir / "pairwise_alignments.tsv", alignment_rows)

    domain_rows: list[dict[str, object]] = []
    for record in local_records:
        domain_rows.extend(interpro_matches(record.id, str(record.seq)))
    write_tsv(args.output_dir / "interpro_domains.tsv", domain_rows)


if __name__ == "__main__":
    main()
