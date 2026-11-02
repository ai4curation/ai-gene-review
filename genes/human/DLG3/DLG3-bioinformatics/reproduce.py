# /// script
# requires-python = ">=3.12"
# dependencies = ["openpyxl==3.1.5", "PyYAML==6.0.2"]
# ///
"""Reproduce PDZ fragmentomics tables from published SD1 and explicit sequence inputs.

This script extracts values; it does not infer affinities from zero, assign GO actions,
or infer that isolated fragments form native full-length complexes.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import tempfile
import urllib.request
import zipfile

import openpyxl
import yaml

SOURCE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9482650/supplementaryFiles"
WORKBOOK_NAME = "41467_2022_33018_MOESM4_ESM.xlsx"
WORKBOOK_SHA256 = "ada912921164f0a79630c6a714b9ff264a7217ad3e646153ef498eb456206795"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def tsv_bytes(columns, rows):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


def read_fasta(path):
    records = {}
    name = None
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            if name in records:
                raise ValueError(f"Repeated FASTA identifier: {name}")
            records[name] = ""
        elif line.strip():
            if name is None:
                raise ValueError("Sequence before FASTA identifier")
            records[name] += line.strip()
    return records


def positions(needle, sequence):
    if not needle or not re.fullmatch("[A-Z]+", needle):
        return []
    return [match.start() + 1 for match in re.finditer(re.escape(needle), sequence)]


def parse(workbook, gene, review_path, fasta_path, provenance_path):
    book_bytes = workbook.read_bytes()
    if digest(book_bytes) != WORKBOOK_SHA256:
        raise ValueError("Workbook bytes differ from the identified published SD1 version")
    sequences = read_fasta(fasta_path)
    with provenance_path.open(newline="") as stream:
        provenance = {row["accession"]: row for row in csv.DictReader(stream, delimiter="\t")}
    for accession, sequence in sequences.items():
        if accession not in provenance or digest(sequence.encode()) != provenance[accession]["sequence_sha256"]:
            raise ValueError(f"Sequence provenance mismatch: {accession}")
    review = yaml.safe_load(review_path.read_text())
    if review["gene_symbol"] != gene:
        raise ValueError("The review and requested domain prefix name different genes")
    wb = openpyxl.load_workbook(io.BytesIO(book_bytes), read_only=True, data_only=True)
    sheet = wb["PDZ-PBM interactome"]
    iterator = sheet.iter_rows(max_col=39, values_only=True)
    raw_header = next(iterator)
    columns = [str(value) if value is not None else f"unnamed_column_{i+1}" for i, value in enumerate(raw_header)]
    measurements = []
    for sheet_row, values in enumerate(iterator, start=2):
        if str(values[0]).startswith(gene + "_"):
            measurements.append({"sheet_row": sheet_row, **dict(zip(columns, values))})
    wb.close()
    crosswalk = []
    source_rows = []
    for index, row in enumerate(review["existing_annotations"]):
        if row["original_reference_id"] != "PMID:36115835":
            continue
        entities = row.get("supporting_entities", [])
        if len(entities) != 1 or not entities[0].startswith("UniProtKB:"):
            raise ValueError(f"Ambiguous source partner at annotation index {index}")
        accession = entities[0].split(":", 1)[1]
        sequence = sequences[accession]
        source_rows.append(index)
        for m in measurements:
            if m["PBM_uniprot"] not in (accession, accession.split("-", 1)[0]):
                continue
            natural_positions = positions(m["natural_10mer"], sequence)
            # Internal amidated ligands explicitly use this linker/cap syntax in SD1.
            # Test their actual peptide core, not the '-INTERNAL-' placeholder.
            internal_match = re.fullmatch(r"Biotin-GSGSGS-([A-Z]+)-CONH2", str(m["peptide"]))
            internal_core = internal_match.group(1) if internal_match else ""
            internal_positions = positions(internal_core, sequence)
            crosswalk.append({
                "source_index": index,
                "supporting_entity": entities[0],
                "sheet_row": m["sheet_row"],
                "PDZ": m["PDZ"],
                "PBM": m["PBM"],
                "PBM_uniprot": m["PBM_uniprot"],
                "natural_10mer": m["natural_10mer"],
                "peptide_10mer": m["peptide_10mer"],
                "peptide": m["peptide"],
                "COMP_neglogKd": m["COMP_neglogKd"],
                "COMP_method": m["COMP_method"],
                "natural_sequence_match": bool(natural_positions),
                "natural_sequence_positions_1based": ",".join(map(str, natural_positions)),
                "internal_core": internal_core,
                "internal_sequence_match": bool(internal_positions),
                "internal_sequence_positions_1based": ",".join(map(str, internal_positions)),
                "selected_sequence_supported_measurement": bool(natural_positions or internal_positions),
            })
    if not measurements or not crosswalk:
        raise ValueError("No domain measurements or source-pair matches")
    measurement_columns = ["sheet_row", *columns]
    crosswalk_columns = list(crosswalk[0])
    summary = {
        "gene": gene,
        "publication": "PMID:36115835",
        "source_url": SOURCE_URL,
        "workbook_member": WORKBOOK_NAME,
        "workbook_sha256": digest(book_bytes),
        "sheet": "PDZ-PBM interactome",
        "identity_fasta_sha256": digest(fasta_path.read_bytes()),
        "identity_provenance_sha256": digest(provenance_path.read_bytes()),
        "raw_gene_measurements": len(measurements),
        "imported_source_rows": len(source_rows),
        "accession_candidate_crosswalk_rows": len(crosswalk),
        "natural_sequence_matched_rows": sum(x["natural_sequence_match"] for x in crosswalk),
        "natural_sequence_unmatched_rows": sum(not x["natural_sequence_match"] for x in crosswalk),
        "additional_internal_sequence_matched_rows": sum(x["internal_sequence_match"] and not x["natural_sequence_match"] for x in crosswalk),
        "selected_sequence_supported_rows": sum(x["selected_sequence_supported_measurement"] for x in crosswalk),
        "domain_counts": {name: sum(m["PDZ"] == name for m in measurements) for name in sorted({m["PDZ"] for m in measurements})},
        "interpretation": "Source-value extraction and sequence mapping only. Zero COMP is not zero affinity or proven noninteraction. Selection is not a positive-binding verdict.",
    }
    return {
        "measurements.tsv": tsv_bytes(measurement_columns, measurements),
        "source-row-crosswalk.tsv": tsv_bytes(crosswalk_columns, crosswalk),
        "run-summary.json": (json.dumps(summary, indent=2, ensure_ascii=False) + "\n").encode(),
    }


def main():
    folder = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gene", default="DLG3")
    parser.add_argument("--review", type=Path, default=folder.parent / "DLG3-ai-review.yaml")
    parser.add_argument("--identities", type=Path, default=folder / "identity-sequences.fasta")
    parser.add_argument("--provenance", type=Path, default=folder / "identity-provenance.tsv")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--workbook", type=Path)
    source.add_argument("--download", action="store_true")
    parser.add_argument("--output", type=Path, default=folder)
    parser.add_argument("--check", action="store_true", help="Compare regenerated bytes with saved tables; do not write")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="pdz-fragmentomics-") as temporary:
        workbook = args.workbook
        if args.download:
            with urllib.request.urlopen(SOURCE_URL, timeout=120) as response:
                archive = response.read()
            with zipfile.ZipFile(io.BytesIO(archive)) as z:
                matches = [n for n in z.namelist() if Path(n).name == WORKBOOK_NAME]
                if len(matches) != 1:
                    raise ValueError("The supplement archive did not have exactly one SD1 workbook")
                workbook = Path(temporary) / WORKBOOK_NAME
                workbook.write_bytes(z.read(matches[0]))
        outputs = parse(workbook, args.gene, args.review, args.identities, args.provenance)
        if args.check:
            for name, data in outputs.items():
                if (args.output / name).read_bytes() != data:
                    raise ValueError(f"Regenerated output differs: {name}")
        else:
            args.output.mkdir(parents=True, exist_ok=True)
            for name, data in outputs.items():
                (args.output / name).write_bytes(data)
        print(json.dumps(json.loads(outputs["run-summary.json"]), indent=2))
        print("CHECK PASS" if args.check else "EXTRACTION COMPLETE")


if __name__ == "__main__":
    main()
