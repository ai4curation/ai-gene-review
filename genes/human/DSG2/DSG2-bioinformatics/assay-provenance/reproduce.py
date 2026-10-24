# /// script
# requires-python = ">=3.11"
# dependencies = ["openpyxl==3.1.5", "xlrd==2.0.2"]
# ///
"""Calculate reference identities and target table projections from pinned inputs."""
import argparse
import base64
import csv
import hashlib
import json
from pathlib import Path

import openpyxl
import xlrd


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sequence_identity(path):
    record = json.loads(path.read_text())
    sequence = record["sequence"]["value"]
    taxon = record["organism"]["taxonId"]
    rogid = base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip("=") + str(taxon)
    return {"accession": record["primaryAccession"], "length": len(sequence), "taxon": taxon, "rogid": rogid}


def interactions(path, target, partner, publication, identities):
    """MITAB 2.7 positions are fixed by the public format, not by target row."""
    matches = []
    with path.open(newline="") as stream:
        for line_number, row in enumerate(csv.reader(stream, delimiter="\t"), 1):
            if not row or row[0].startswith("#"):
                continue
            if len(row) < 38:
                raise ValueError(f"Incomplete MITAB row {line_number}")
            participants = [row[0], row[1]]
            if set(participants) != {"uniprotkb:" + target, "uniprotkb:" + partner}:
                continue
            if "pubmed:" + publication not in row[8].split("|"):
                continue
            checks = []
            for side in range(2):
                accession = participants[side].split(":", 1)[1]
                check = dict(identities[accession])
                check["literal_rogid"] = row[32 + side]
                check["matches_literal_rogid"] = "rogid:" + check["rogid"] in row[32 + side].split("|")
                checks.append(check)
            matches.append({"line": line_number, "participants": participants,
                            "method": row[6], "publication": row[8],
                            "interaction_type": row[11], "stable_ids": row[13],
                            "expansion": row[15], "host": row[28],
                            "features": row[36:38], "reference_sequences": checks})
    return matches


def network_rows(path, target, partner):
    """Find a header by field names, then preserve the matching table values."""
    matches = []
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for sheet in workbook:
        header = None
        for row_number, values in enumerate(sheet.iter_rows(values_only=True), 1):
            if "Uniprot_1" in values and "Uniprot_2" in values:
                header = values
                continue
            if header is None:
                continue
            record = {str(key): value for key, value in zip(header, values) if key is not None}
            if {record.get("Uniprot_1"), record.get("Uniprot_2")} == {target, partner}:
                matches.append({"sheet": sheet.title, "row": row_number, "record": record})
    workbook.close()
    return matches


def parotid_rows(path, gene):
    """Retain measured/identity fields; exclude background function/GO columns."""
    measured = {"LocusID", "Description", "Sequence Count", "SpectrumCount", "Sequence Coverage",
                "Length", "MW", "pI", "Predicted Transmembrane Helices", "Gene"}
    matches = []
    workbook = xlrd.open_workbook(str(path))
    for sheet in workbook.sheets():
        header = None
        for index in range(sheet.nrows):
            values = sheet.row_values(index)
            if "Gene" in values and "Sequence Count" in values:
                header = values
                continue
            if header is None:
                continue
            record = {key: value for key, value in zip(header, values) if key in measured}
            if str(record.get("Gene", "")).strip() == gene:
                matches.append({"sheet": sheet.name, "row": index + 1, "record": record})
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("input-manifest.json"))
    locations = parser.add_mutually_exclusive_group(required=True)
    locations.add_argument("--input-dir", type=Path)
    locations.add_argument("--input-map", type=Path)
    parser.add_argument("--gene", help="Override the proteomic gene query for a control")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    saved = json.loads(args.input_map.read_text()) if args.input_map else {}
    paths, pins = {}, {}
    for source in manifest["sources"]:
        path = Path(saved[source["key"]]) if args.input_map else args.input_dir / source["filename"]
        actual = digest(path)
        if actual != source["sha256"]:
            raise ValueError(f"Input changed: {source['key']} ({actual})")
        paths[source["key"]] = path
        pins[source["key"]] = actual
    identities = {item["accession"]: item for item in
                  [sequence_identity(paths["target"]), sequence_identity(paths["partner"]) ]}
    target, partner = manifest["target"], manifest["partner"]
    if set(identities) != {target, partner}:
        raise ValueError("Official source identities do not match requested accessions")
    gene = args.gene or manifest["gene"]
    result = {"queries": {"target": target, "partner": partner, "proteomic_gene": gene,
                          "interaction_publication": manifest["interaction_publication"]},
              "input_sha256": pins,
              "reference_sequences": list(identities.values()),
              "interactions": interactions(paths["intact"], target, partner,
                                           manifest["interaction_publication"], identities),
              "network": network_rows(paths["network"], target, partner),
              "parotid": parotid_rows(paths["parotid"], gene)}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: len(result[key]) for key in ["interactions", "network", "parotid"]}))


if __name__ == "__main__":
    main()
