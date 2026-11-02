#!/usr/bin/env python3
"""Replay selected primary-data records from exact saved inputs; no network calls.

Python 3.9+, standard library only. Worksheet coordinates are one-based. The
XLSX reader preserves cached literal values and never evaluates formulae.
"""
import argparse
from collections import Counter
import hashlib
import io
import json
from pathlib import Path
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile

import graph_csv

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def column_index(address):
    letters = re.match(r"[A-Z]+", address)
    if not letters:
        raise ValueError("Invalid XLSX cell address: " + address)
    value = 0
    for c in letters.group():
        value = value * 26 + ord(c) - ord("A") + 1
    return value - 1


def read_workbook(data):
    """Read relevant plain literal sheets without guessing biological meanings."""
    sheets = {}
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        strings = []
        if "xl/sharedStrings.xml" in z.namelist():
            strings = ["".join(t.text or "" for t in s.findall(".//m:t", NS))
                       for s in ET.fromstring(z.read("xl/sharedStrings.xml"))]
        rels = {r.attrib["Id"]: r.attrib["Target"] for r in
                ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        for sheet in workbook.findall("m:sheets/m:sheet", NS):
            target = rels[sheet.attrib["{" + REL + "}id"]]
            path = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
            root = ET.fromstring(z.read(path))
            dim = root.find("m:dimension", NS)
            maximum_column = column_index(dim.attrib["ref"].split(":")[-1]) + 1 if dim is not None else 0
            rows = {}
            formula_cells = []
            for row in root.findall("m:sheetData/m:row", NS):
                values = {}
                for cell in row.findall("m:c", NS):
                    address = cell.attrib["r"]
                    col = column_index(address)
                    maximum_column = max(maximum_column, col + 1)
                    kind = cell.attrib.get("t", "n")
                    v = cell.find("m:v", NS)
                    raw = None if v is None else v.text
                    if kind == "inlineStr":
                        inline = cell.find("m:is", NS)
                        value = None if inline is None else "".join(t.text or "" for t in inline.findall(".//m:t", NS))
                    elif raw is None:
                        value = None
                    elif kind == "s":
                        value = strings[int(raw)]
                    elif kind == "b":
                        value = bool(int(raw))
                    elif kind in {"str", "e"}:
                        value = raw
                    elif kind == "n":
                        value = float(raw) if any(x in raw.lower() for x in [".", "e"]) else int(raw)
                    else:
                        raise ValueError("Unsupported XLSX literal type: " + kind)
                    formula = cell.find("m:f", NS)
                    if formula is not None:
                        formula_cells.append({"cell": address, "formula": formula.text, "cached_value": value})
                    values[col] = value
                rows[int(row.attrib["r"])] = values
            cells = {number: [values.get(col) for col in range(maximum_column)] for number, values in rows.items()}
            sheets[sheet.attrib["name"]] = {
                "rows": cells, "maximum_column": maximum_column,
                "worksheet_dimension": None if dim is None else dim.attrib["ref"],
                "formula_cells": formula_cells,
            }
    return sheets


def member_bytes(path, record):
    with zipfile.ZipFile(path) as z:
        content = z.read(record["member"])
    if hashlib.sha256(content).hexdigest() != record["member_sha256"] or len(content) != record["member_bytes"]:
        raise ValueError("Workbook member differs from authenticated source")
    return content


def cell_rows(rows, predicate):
    return [{"worksheet_row": n, "cells": values} for n, values in rows.items() if predicate(n, values)]


def extract_table_359(data, target):
    workbook = read_workbook(data)
    sheet = workbook["data"]
    rows = sheet["rows"]
    header = rows[3]
    assert header[2] == "Uniprot(accession)" and header[10] == "Uniprot(accession)"
    selected = cell_rows(rows, lambda n, v: n > 3 and target in (v[2], v[10]))
    data_rows = [v for n, v in rows.items() if n > 3 and any(x is not None for x in v)]
    return {
        "sheet": "data", "worksheet_dimension": sheet["worksheet_dimension"],
        "column_count": sheet["maximum_column"],
        "headers": [{"worksheet_row": n, "cells": rows[n]} for n in range(1, 4)],
        "nonempty_data_row_count": len(data_rows),
        "incident_count": len(selected), "selected_count": len(selected),
        "participant_label_counts": dict(Counter(v["cells"][7] if v["cells"][2] == target else v["cells"][15] for v in selected)),
        "score_counts": dict(Counter(str(v["cells"][16]) for v in selected)),
        "selected_rows": selected,
        "formula_cells": sheet["formula_cells"],
        "coordinate_scope": "Binding-site columns reproduced literally; no conversion from nucleotide to amino-acid coordinates or complete-insert claim.",
    }


def extract_table_369(data, target, partners):
    workbook = read_workbook(data)
    output = {}
    def tokens(value):
        return {x.strip() for x in str(value or "").split(",")}
    for name, sheet in workbook.items():
        if name == "Overview":
            # Workbook-level explanatory sheet; no target measurement table.
            continue
        rows = sheet["rows"]
        if name == "Datasets_Summary":
            incident = lambda v: str(v[1] or "").split("_")[0] == target
            chosen = lambda v: False
        elif name == "Interactor_Lists":
            incident = lambda v: target in (v[1], v[2])
            chosen = lambda v: (v[1] == target and v[2] in partners) or (v[2] == target and v[1] in partners)
        elif name == "Interactor_Frequency":
            incident = lambda v: target in tokens(v[2])
            chosen = lambda v: v[0] in partners
        elif name == "Interaction_Annotations":
            incident = lambda v: target in (v[0], v[1])
            chosen = lambda v: (v[0] == target and v[1] in partners) or (v[1] == target and v[0] in partners)
        else:
            raise ValueError("Unexpected mmc4 sheet: " + name)
        target_rows = cell_rows(rows, lambda n, v: n > 1 and incident(v))
        selected = [r for r in target_rows if chosen(r["cells"])]
        output[name] = {
            "headers": rows[1], "worksheet_dimension": sheet["worksheet_dimension"],
            "column_count": sheet["maximum_column"],
            "nonempty_data_row_count": sum(n > 1 and any(x is not None for x in v) for n, v in rows.items()),
            "target_count": len(target_rows), "selected_count": len(selected),
            "target_rows": target_rows, "selected_rows": selected,
            "formula_cells": sheet["formula_cells"],
        }
    return output


def verified_paths(mapping, manifest):
    if set(mapping) != set(manifest["inputs"]):
        raise ValueError("Input mapping must name every manifest input exactly once")
    paths = {}
    for key, record in manifest["inputs"].items():
        path = Path(mapping[key])
        if graph_csv.digest(path) != record["sha256"] or path.stat().st_size != record["bytes"]:
            raise ValueError(key + ": input hash/size mismatch; refusing a changed snapshot")
        paths[key] = path
    return paths


def compute(mapping, manifest, selection):
    paths = verified_paths(mapping, manifest)
    target = selection["target_gene_symbol"]
    return {
        "selection": selection,
        "input_sha256": {k: v["sha256"] for k, v in manifest["inputs"].items()},
        "apms": graph_csv.extract_graph(paths["apms"], target, set(selection["apms_partner_symbols"])),
        "opencell": graph_csv.extract_csv(paths["opencell"], target, set(selection["opencell_partner_symbols"])),
        "table_35914814": extract_table_359(member_bytes(paths["table_35914814"], manifest["inputs"]["table_35914814"]), selection["target_accession"]),
        "table_36950384": extract_table_369(member_bytes(paths["table_36950384"], manifest["inputs"]["table_36950384"]), target, set(selection["table_36950384_partner_symbols"])),
    }


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--inputs-map", type=Path, help="JSON mapping source keys to local saved paths; relative paths resolve beside the map")
    group.add_argument("--inputs-dir", type=Path, help="Directory containing manifest filenames")
    parser.add_argument("--manifest", type=Path, default=here / "source-manifest.json")
    parser.add_argument("--selection", type=Path, default=here / "selection.json")
    parser.add_argument("--output", type=Path, default=here / "RESULTS.json")
    parser.add_argument("--check", action="store_true", help="Recompute and compare exact saved output without writing")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    selection = json.loads(args.selection.read_text())
    if args.inputs_map:
        raw = json.loads(args.inputs_map.read_text())
        mapping = {k: str(args.inputs_map.resolve().parent / v) for k, v in raw.items()}
    else:
        mapping = {k: str(args.inputs_dir / v["filename"]) for k, v in manifest["inputs"].items()}
    result = compute(mapping, manifest, selection)
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if args.output.read_text() != encoded:
            raise SystemExit("FAIL: saved result differs from raw-derived output")
    else:
        args.output.write_text(encoded)
    print(json.dumps({"status": "PASS" if args.check else "WRITTEN", "target": selection["target_gene_symbol"],
                      "apms": [result["apms"]["incident_count"], result["apms"]["selected_count"]],
                      "opencell": [result["opencell"]["incident_count"], result["opencell"]["selected_count"]],
                      "table_35914814": result["table_35914814"]["selected_count"],
                      "table_36950384": {k: [v["target_count"], v["selected_count"]] for k, v in result["table_36950384"].items()}}))


if __name__ == "__main__":
    main()
