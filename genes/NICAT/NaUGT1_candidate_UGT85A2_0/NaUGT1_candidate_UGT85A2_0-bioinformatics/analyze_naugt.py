# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython==1.85", "requests==2.32.5"]
# ///
"""Compare the published, assayed tobacco NaGT sequence with the cached NICAT protein.

Reads original supplementary XLSX cells without changing the workbooks. This is
a pairwise sequence comparison, not a gene tree or a reciprocal-best-hit test.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.Seq import Seq
import requests

HERE = Path(__file__).resolve().parent
GENE = HERE.parent.name
BASE = "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-026-72705-0/MediaObjects/"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def cells(path):
    with ZipFile(path) as archive:
        strings = ["".join(t.itertext()) for t in ET.fromstring(
            archive.read("xl/sharedStrings.xml")).findall("s:si", NS)]
        root = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        out = {}
        for cell in root.findall(".//s:c", NS):
            val = cell.find("s:v", NS)
            if val is not None:
                out[cell.attrib["r"]] = strings[int(val.text)] if cell.get("t") == "s" else val.text
        return out


def main():
    sources = []
    tables = {}
    for n in (3, 6):
        name = f"41467_2026_72705_MOESM{n}_ESM.xlsx"
        path = HERE / name
        if not path.exists():
            response = requests.get(BASE + name, timeout=60)
            response.raise_for_status()
            path.write_bytes(response.content)
        tables[n] = cells(path)
        sources.append({"file": name, "url": BASE + name,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    identities = {key: tables[3][key] for key in ("A36", "B36", "C36", "D36", "E36", "F36")}
    construct = {key: tables[6][key] for key in ("A5", "B5", "C5", "D5", "E5", "F5", "H5", "I5", "J5", "K5")}
    if identities["D36"].split("_")[0] != construct["F5"].split("_")[0]:
        raise ValueError("Supplementary accession mapping differs between tables")
    tobacco = str(Seq(construct["J5"]).translate(to_stop=True))
    if not construct["K5"].endswith(tobacco):
        raise ValueError("Published coding sequence does not match the expressed protein suffix")
    tag = construct["K5"][:-len(tobacco)]
    record = (HERE.parent / f"{GENE}-uniprot.txt").read_text()
    accession = re.search(r"^AC\s+(\w+);", record, re.M).group(1)
    if accession != "A0A2H4GSI3":
        raise ValueError(f"Wrong target accession: {accession}")
    target = "".join(re.findall(r"[A-Z]+", record.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//", 1)[0]))
    aligner = PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                              open_gap_score=-10, extend_gap_score=-0.5)
    alignment = aligner.align(target, tobacco)[0]
    a, b = alignment[0], alignment[1]
    matches = sum(x == y and x != "-" for x, y in zip(a, b))
    paired = sum(x != "-" and y != "-" for x, y in zip(a, b))
    result = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(), "primary_reference": "PMID:42151135",
        "sources": sources, "supplementary_data_1_cells": identities,
        "supplementary_data_4_cells": construct, "removed_expression_tag": tag,
        "target_accession": accession, "target_length": len(target), "tobacco_native_length": len(tobacco),
        "alignment_method": "Global BLOSUM62, gap open -10, extension -0.5; terminal gaps included",
        "identical_positions": matches, "paired_positions": paired, "alignment_columns": len(a),
        "identity_over_all_columns": matches / len(a), "identity_over_paired_positions": matches / paired,
        "target_aligned": a, "tobacco_aligned": b,
        "interpretation_limit": "Sequence similarity plus the primary accession mapping supports a homolog comparison; this calculation alone does not establish exclusive orthology or acceptor specificity.",
    }
    (HERE / "results-natcom.json").write_text(json.dumps(result, indent=2) + "\n")
    (HERE / "natcom-pairwise-alignment.txt").write_text(str(alignment))
    print(json.dumps({k: v for k, v in result.items() if k in ["target_length", "tobacco_native_length", "identical_positions", "paired_positions", "alignment_columns", "identity_over_all_columns", "identity_over_paired_positions"]}, indent=2))


if __name__ == "__main__":
    main()
