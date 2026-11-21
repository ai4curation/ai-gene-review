"""Extract the supplied DeepTMHMM2 S20 table and join to existing human reviews.

Usage: python projects/DEEPTMHMM2/extract_s20.py ~/Downloads/media-1.xlsx
Only the Python standard library is required. Source text is preserved verbatim.
"""

import argparse
import csv
import hashlib
import json
from pathlib import Path
import posixpath
import re
from xml.etree import ElementTree as ET
from zipfile import ZipFile

NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def read_sheet(path, name):
    with ZipFile(path) as archive:
        strings = [
            "".join(t.text or "" for t in item.findall(".//s:t", NS))
            for item in ET.fromstring(archive.read("xl/sharedStrings.xml"))
        ]
        relationships = {
            item.attrib["Id"]: item.attrib["Target"]
            for item in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        }
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        sheet = next(s for s in workbook.find("s:sheets", NS) if s.attrib["name"] == name)
        target = relationships[sheet.attrib[RID]]
        member = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
        rows = []
        for row in ET.fromstring(archive.read(member)).findall(".//s:row", NS):
            cells = {}
            for cell in row.findall("s:c", NS):
                column = re.match(r"[A-Z]+", cell.attrib["r"])[0]
                value = cell.find("s:v", NS)
                text = value.text if value is not None else ""
                if cell.attrib.get("t") == "s":
                    text = strings[int(text)]
                elif cell.attrib.get("t") == "inlineStr":
                    text = "".join(t.text or "" for t in cell.findall(".//s:t", NS))
                cells[column] = text
            values = [cells.get(c, "") for c in "ABCDE"]
            if any(values):
                rows.append((int(row.attrib["r"]), values))
        assert rows[0][1] == ["ID", "Type", "Evidence", "Segments", "Description"]
        return rows[1:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = Path(__file__).resolve().parent
    accessions = {}
    for review in sorted((root / "genes/human").glob("*/*-ai-review.yaml")):
        match = re.search(r"^id:\s*['\"]?([A-Z0-9]+)['\"]?\s*$", review.read_text(), re.M)
        if match:
            accessions.setdefault(match[1], []).append(review.parent.name)
    records = []
    for row, values in read_sheet(args.workbook, "S20"):
        identifier, kind, evidence, segments, description = values
        accession = identifier.split("|")[1]
        records.append(dict(source_row=row, accession=accession, source_id=identifier,
                            type=kind, author_evidence=evidence, segments=segments,
                            author_description=description,
                            reviewed_genes=";".join(accessions.get(accession, []))))
    for filename, subset in [("s20.tsv", records),
                             ("reviewed-human.tsv", [r for r in records if r["reviewed_genes"]])]:
        with (output / filename).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(records[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(subset)
    metadata = dict(doi="10.64898/2026.08.24.746435", version="v1", sheet="S20",
                    source_filename=args.workbook.name,
                    sha256=hashlib.sha256(args.workbook.read_bytes()).hexdigest(),
                    rows=len(records), matched_rows=sum(bool(r["reviewed_genes"]) for r in records))
    (output / "source.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
