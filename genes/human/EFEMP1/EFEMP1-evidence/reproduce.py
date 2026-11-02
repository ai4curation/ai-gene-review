# /// script
# requires-python = ">=3.9"
# dependencies = ["xlrd==2.0.1"]
# ///
"""Extract literal EFEMP1 evidence records from hash-checked saved sources.

No annotation verdict is calculated. All output is computed from supplied raw
inputs; selection.json specifies the target and imported source/partner joins.
"""
from pathlib import Path
import argparse
import base64
import csv
import hashlib
import io
import json
import re
import xml.etree.ElementTree as ET
import zipfile

HERE = Path(__file__).resolve().parent
J = lambda p: json.loads(p.read_text())


def workbook_rows(path):
    """Read xlsx cell values without rewriting the workbook."""
    ns = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
          "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    with zipfile.ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            for item in ET.fromstring(z.read("xl/sharedStrings.xml")):
                shared.append("".join(t.text or "" for t in item.iter("{"+ns["s"]+"}t")))
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rel = {x.attrib["Id"]: x.attrib["Target"] for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        for sheet in wb.find("s:sheets", ns):
            target = rel[sheet.attrib["{"+ns["r"]+"}id"]]
            member = target.lstrip("/") if target.startswith("/") else "xl/"+target
            rows = []
            for row in ET.fromstring(z.read(member)).findall(".//s:sheetData/s:row", ns):
                cells = {}
                for cell in row:
                    letters = re.match(r"[A-Z]+", cell.attrib["r"]).group()
                    column = 0
                    for letter in letters: column = column*26+ord(letter)-64
                    value = cell.find("s:v", ns)
                    value = value.text if value is not None else None
                    kind = cell.attrib.get("t")
                    if kind == "s" and value is not None: value = shared[int(value)]
                    elif kind == "inlineStr": value = "".join(t.text or "" for t in cell.findall(".//s:t", ns))
                    elif value is not None and kind not in ("str", "e"):
                        try:
                            value = float(value)
                            if value.is_integer(): value = int(value)
                        except ValueError: pass
                    cells[column] = value
                rows.append({"physical_row": int(row.attrib["r"]),
                             "cells": [cells.get(i) for i in range(1, max(cells, default=0)+1)]})
            yield sheet.attrib["name"], rows


def extract(paths, selection):
    accession, symbol = selection["accession"], selection["symbol"]
    records = []
    counts = {}
    for database in ("intact", "mint"):
        lines = paths[database].read_text().splitlines()
        counts[database] = sum(bool(line and not line.startswith("#")) for line in lines)
        for line_number, line in enumerate(lines, 1):
            if not line or line.startswith("#"): continue
            fields = line.split("\t")
            records.append({"database": database, "physical_line": line_number, "fields": fields})
    joins = []
    for item in selection["pairs"]:
        hits = [r for r in records if {"uniprotkb:"+accession, "uniprotkb:"+item["partner"]} <= set(r["fields"][:2])
                and "pubmed:"+item["pmid"] in r["fields"][8].split("|")]
        joins.append({**item, "records": hits})
    xlsx = []
    for name, rows in workbook_rows(paths["colon_liver_table"]):
        hits = [r for r in rows if any(symbol == str(c) or accession in str(c) for c in r["cells"])]
        xlsx.append({"sheet": name, "physical_rows_present": len(rows), "headers": [r for r in rows if r["physical_row"] <= 4], "target_rows": hits})
    import xlrd
    book = xlrd.open_workbook(paths["hcv_table"])
    xls = []
    for sheet in book.sheets():
        hits = [{"physical_row": i+1, "cells": sheet.row_values(i)} for i in range(sheet.nrows)
                if any(symbol == str(c) or accession in str(c) for c in sheet.row_values(i))]
        xls.append({"sheet": sheet.name, "row_count": sheet.nrows,
                    "headers": [{"physical_row":i+1,"cells":sheet.row_values(i)} for i in range(min(4,sheet.nrows))],
                    "target_rows": hits})
    tables = []
    original = ET.fromstring(paths["aorta_original"].read_bytes())
    for table in original.findall(".//table-wrap"):
        target = [row for row in table.findall(".//tr") if selection["aorta_accession_name"] in "".join(row.itertext())]
        if target:
            tables.append({"table_id":table.attrib.get("id"),"label":table.findtext("label"),
                           "headers":[["".join(c.itertext()) for c in r] for r in table.findall(".//thead/tr")],
                           "target_rows":[["".join(c.itertext()) for c in r] for r in target]})
    nodes, parent = {}, {}
    def visit(node, ancestor=None):
        key=node["persistent_id"];nodes[key]=node
        if ancestor:parent[key]=ancestor
        children=node.get("children",{}).get("annotation_node",[])
        if isinstance(children,dict):children=[children]
        for child in children:visit(child,key)
    visit(J(paths["tree"])["search"]["tree_topology"]["annotation_node"])
    def lineage(key):
        result=[key]
        while key in parent:key=parent[key];result.append(key)
        return result
    target_nodes=[(key,n) for key,n in nodes.items() if "UniProtKB="+accession in n.get("node_name", "")]
    msa=J(paths["msa"])["search"]["MSA_list"]["sequence_info"]
    target_sequence=J(paths["target_uniprot"])["sequence"]["value"]
    tree_hits=[]
    for key,node in target_nodes:
        alignment=[r for r in msa if r.get("node_id")==key or r.get("persistent_id")==key or accession in str({k:v for k,v in r.items() if k!='sequence'})]
        tree_hits.append({"node":key,"node_name":node.get("node_name"),"lineage":lineage(key),
                          "alignment_records":[{k:v for k,v in r.items() if k!='sequence'} for r in alignment],
                          "sequence_match":[re.sub(r"[^A-Za-z]", "",r['sequence']).upper()==target_sequence for r in alignment]})
    gaf=[line.split("\t") for line in paths["ibd"].read_text().splitlines() if line and not line.startswith("!")]
    ibds=[r for r in gaf if r[1] in selection["ancestral_nodes"] and r[4] in selection["paint_terms"]]
    return {"target":{"symbol":symbol,"accession":accession},"interaction_input_record_counts":counts,
            "interaction_joins":joins,"colon_liver_workbook":xlsx,"HCV_workbook":xls,"aorta_tables":tables,
            "phylogeny":{"node_count":len(nodes),"MSA_record_count":len(msa),"targets":tree_hits,"literal_ancestral_records":ibds}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-dir",type=Path,help="Directory containing the source-manifest filenames")
    parser.add_argument("--source",action="append",default=[],metavar="ID=PATH",help="Explicit saved-path override; repeat as needed")
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    overrides=dict(value.split("=",1) for value in args.source)
    paths={}
    for source in J(HERE/'source-manifest.json')['sources']:
        key=source['id']
        if key in overrides: path=Path(overrides[key])
        elif args.raw_dir: path=args.raw_dir/source['filename']
        else: parser.error('Supply --raw-dir or --source for '+key)
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=source['sha256']:
            raise ValueError('Source hash mismatch: '+key)
        paths[key]=path
    output=extract(paths,J(HERE/'selection.json'))
    args.output.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'output':str(args.output),'source_count':len(paths),
                      'source_joins':len(output['interaction_joins']),
                      'matched_record_occurrences':sum(len(x['records']) for x in output['interaction_joins'])}))


if __name__=='__main__':main()
