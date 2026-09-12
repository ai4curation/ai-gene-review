#!/usr/bin/env python3
"""Reproduce the LNP1 interaction, identity, and HPA localization audit.

Only Python's standard library is required. Source identifiers and URLs are read
from the supplied JSON config; output location is supplied on the command line.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import platform
import re
import sys
import time
import urllib.request
import zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET


USER_AGENT = "ai-gene-review-LNP1-provenance-audit/1.0"


def fetch(url: str, byte_range: str | None = None) -> tuple[bytes, dict[str, str]]:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if byte_range:
        headers["Range"] = f"bytes={byte_range}"
    request = urllib.request.Request(url, headers=headers)
    error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
                metadata = {
                    "status": str(response.status),
                    "content_type": response.headers.get("Content-Type", ""),
                    "content_range": response.headers.get("Content-Range", ""),
                    "etag": response.headers.get("ETag", ""),
                    "last_modified": response.headers.get("Last-Modified", ""),
                }
                return data, metadata
        except Exception as exc:  # network errors are retried, then surfaced
            error = exc
            if attempt < 2:
                time.sleep(1 + attempt)
    raise RuntimeError(f"failed to fetch {url}: {error}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_text_snapshot(path: Path, data: bytes) -> None:
    """Write a review-friendly text snapshot while hashing original source bytes."""
    path.parent.mkdir(parents=True, exist_ok=True)
    text = data.decode("utf-8-sig", errors="replace")
    normalized_lines: list[str] = []
    for line in text.splitlines():
        content = line.lstrip(" \t")
        indentation = line[:len(line) - len(content)]
        normalized_lines.append(
            (" " * len(indentation.expandtabs(4)) + content).rstrip(" \t")
        )
    normalized = "\n".join(normalized_lines)
    path.write_text(normalized + ("\n" if text else ""), encoding="utf-8")


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(rows)


def record_source(manifest: list[dict[str, object]], name: str, url: str, data: bytes,
                  metadata: dict[str, str], byte_range: str = "") -> None:
    manifest.append({
        "name": name,
        "url": url,
        "byte_range": byte_range,
        "bytes": len(data),
        "sha256": sha256(data),
        **metadata,
    })


def uniprot_accession(identifier: str) -> str:
    return identifier.split(":", 1)[1] if identifier.startswith("uniprotkb:") else identifier


def gene_from_aliases(value: str) -> str:
    match = re.search(r"uniprotkb:([^|()]+)\(gene name\)", value)
    if match:
        return match.group(1)
    match = re.search(r"psi-mi:([^|()]+)\(display_short\)", value)
    return match.group(1) if match else value


def parse_intact(data: bytes, selected_pmids: set[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in csv.reader(io.StringIO(data.decode("utf-8")), delimiter="\t"):
        if len(row) < 15:
            continue
        pmids = {x.split(":", 1)[1] for x in row[8].split("|") if x.startswith("pubmed:")}
        if not pmids.intersection(selected_pmids):
            continue
        rows.append({
            "accession_a": uniprot_accession(row[0]),
            "accession_b": uniprot_accession(row[1]),
            "gene_a": gene_from_aliases(row[4]),
            "gene_b": gene_from_aliases(row[5]),
            "detection_method": row[6],
            "publication_ids": row[8],
            "interaction_type": row[11],
            "interaction_ids": row[13],
            "confidence": row[14],
            "expansion_method": row[15] if len(row) > 15 else "",
            "experimental_role_a": row[18] if len(row) > 18 else "",
            "experimental_role_b": row[19] if len(row) > 19 else "",
            "interaction_annotation": row[27] if len(row) > 27 else "",
            "host_organism": row[28] if len(row) > 28 else "",
            "features_a": row[36] if len(row) > 36 else "",
            "features_b": row[37] if len(row) > 37 else "",
        })
    return rows


class TableParser(HTMLParser):
    def __init__(self, table_id: str):
        super().__init__()
        self.table_id = table_id
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.rows: list[list[str]] = []
        self.row: list[str] = []
        self.cell: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "table" and values.get("id") == self.table_id:
            self.in_table = True
        elif self.in_table and tag == "tr":
            self.in_row = True
            self.row = []
        elif self.in_row and tag == "td":
            self.in_cell = True
            self.cell = []

    def handle_data(self, data: str) -> None:
        if self.in_cell:
            self.cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "td" and self.in_cell:
            text = " ".join(" ".join(self.cell).replace("\xa0", " ").split())
            self.row.append(text)
            self.in_cell = False
        elif tag == "tr" and self.in_row:
            if self.row:
                self.rows.append(self.row)
            self.in_row = False
        elif tag == "table" and self.in_table:
            self.in_table = False


def extract_biogrid(data: bytes, interaction_id: str) -> dict[str, str]:
    text = data.decode("utf-8", errors="replace")
    description = re.search(r'<meta name="description" content="([^"]+)"', text)
    keywords = re.search(r'<meta name="keywords" content="([^"]+)"', text)
    accessions = re.findall(r"uniprot(?:kb)?/([A-Z0-9]+)' title='UniprotKB", text, flags=re.I)
    method = re.search(r"<h3>(Affinity Capture-[^<]+)</h3>", text)
    pmid = re.search(r"Pubmed:\s*(\d+)", text)
    if len(accessions) < 2 or not method or not pmid:
        raise AssertionError(f"could not parse BioGRID interaction {interaction_id}")
    return {
        "interaction_id": interaction_id,
        "description": description.group(1) if description else "",
        "keywords": keywords.group(1) if keywords else "",
        "accession_a": accessions[0],
        "accession_b": accessions[1],
        "method": method.group(1).strip(),
        "pmid": pmid.group(1),
    }


def parse_range_rows(header_data: bytes, range_data: bytes, bait_id: str,
                     target_gene: str, family_genes: set[str]) -> list[dict[str, str]]:
    header = next(csv.reader(io.StringIO(header_data.decode("utf-8", errors="replace")), delimiter="\t"))
    selected: list[dict[str, str]] = []
    text = range_data.decode("utf-8", errors="replace")
    for line in text.splitlines():
        if not line.startswith(f"{bait_id}\t{target_gene}\t"):
            continue
        values = next(csv.reader([line], delimiter="\t"))
        row = dict(zip(header, values))
        if row.get("symbol") in family_genes:
            protein_id = row.get("db_protein_id", "")
            match = re.search(r"(?:sp|tr)\|([^|]+)\|", protein_id)
            row["prey_accession"] = match.group(1) if match else protein_id
            selected.append(row)
    return selected


def selected_zip_lines(archive: bytes, member: str, predicate) -> tuple[list[str], str]:
    with zipfile.ZipFile(io.BytesIO(archive)) as zf:
        raw = zf.read(member).decode("utf-8-sig")
    lines = raw.splitlines()
    return [line for line in lines[1:] if predicate(line.split("\t"))], lines[0]


def column_number(reference: str) -> int:
    letters = re.match(r"[A-Z]+", reference)
    if not letters:
        return 0
    value = 0
    for char in letters.group(0):
        value = value * 26 + ord(char) - 64
    return value - 1


def read_xlsx_sheet(workbook: bytes, sheet_name: str) -> list[list[str]]:
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    rel_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    pkg_rel_ns = "{http://schemas.openxmlformats.org/package/2006/relationships}"
    with zipfile.ZipFile(io.BytesIO(workbook)) as zf:
        book = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall(f"{pkg_rel_ns}Relationship")}
        sheet_path = None
        for sheet in book.findall(f".//{ns}sheet"):
            if sheet.attrib.get("name") == sheet_name:
                target = targets[sheet.attrib[f"{rel_ns}id"]]
                sheet_path = "xl/" + target.lstrip("/") if not target.startswith("xl/") else target
                break
        if not sheet_path:
            raise AssertionError(f"sheet not found: {sheet_name}")
        shared: list[str] = []
        if "xl/sharedStrings.xml" in zf.namelist():
            strings = ET.fromstring(zf.read("xl/sharedStrings.xml"))
            for item in strings.findall(f"{ns}si"):
                shared.append("".join(node.text or "" for node in item.iter(f"{ns}t")))
        sheet = ET.fromstring(zf.read(sheet_path))
        rows: list[list[str]] = []
        for row in sheet.findall(f".//{ns}row"):
            values: list[str] = []
            for cell in row.findall(f"{ns}c"):
                index = column_number(cell.attrib.get("r", "A1"))
                while len(values) <= index:
                    values.append("")
                value_node = cell.find(f"{ns}v")
                value = "" if value_node is None else (value_node.text or "")
                if cell.attrib.get("t") == "s" and value:
                    value = shared[int(value)]
                values[index] = value
            rows.append(values)
        return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--publications-dir", type=Path)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    out = args.output_dir.resolve()
    raw = out / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, object]] = []
    summary: dict[str, object] = {"target": config["target"], "checks": {}}
    sources = config["sources"]

    # Exact UniProt identities, including an explicit LNPK/Q9C0E8 negative control.
    identity_rows: list[dict[str, str]] = []
    for check in config["identity_checks"]:
        accession = check["accession"]
        url = sources["uniprot_template"].format(accession=accession)
        data, meta = fetch(url)
        record_source(manifest, f"uniprot:{accession}", url, data, meta)
        parsed = list(csv.DictReader(io.StringIO(data.decode("utf-8")), delimiter="\t"))
        if len(parsed) != 1:
            raise AssertionError(f"UniProt returned {len(parsed)} rows for {accession}")
        row = parsed[0]
        if row["Entry"] != accession or row["Gene Names (primary)"] != check["expected_gene"]:
            raise AssertionError(f"identity mismatch for {accession}: {row}")
        identity_rows.append(row)
    identity_fields = list(identity_rows[0])
    write_tsv(out / "uniprot_identities.tsv", identity_fields, identity_rows)
    summary["checks"]["identity"] = "A1A4G5=LNP1; Q9C0E8=LNPK; all partner accessions matched configured genes"

    # IntAct: retain raw MITAB 2.7 and a compact evidence-method view.
    intact_url = sources["intact_template"].format(accession=config["target"]["uniprot"])
    intact_data, intact_meta = fetch(intact_url)
    write_text_snapshot(raw / "A1A4G5-intact-mitab27.tsv", intact_data)
    record_source(manifest, "intact:A1A4G5", intact_url, intact_data, intact_meta)
    intact_rows = parse_intact(intact_data, set(config["intact_publications"]))
    intact_fields = list(intact_rows[0])
    write_tsv(out / "intact_selected_interactions.tsv", intact_fields, intact_rows)

    # Official BioPlex no-filter rows. HTTP ranges avoid downloading two ~GB TSVs.
    bioplex_rows: list[dict[str, str]] = []
    expected_gene_by_accession = config["bioplex"]["family_accessions"]
    family_genes = set(expected_gene_by_accession.values())
    for release in config["bioplex"]["releases"]:
        header_data, header_meta = fetch(release["url"], "0-4095")
        range_data, range_meta = fetch(release["url"], release["byte_range"])
        stem = f"bioplex-{release['cell_line']}"
        write_text_snapshot(raw / f"{stem}-header-range.tsv", header_data)
        write_text_snapshot(raw / f"{stem}-LNP1-range.tsv", range_data)
        record_source(manifest, f"{stem}:header", release["url"], header_data, header_meta, "0-4095")
        record_source(manifest, f"{stem}:LNP1", release["url"], range_data, range_meta, release["byte_range"])
        rows = parse_range_rows(header_data, range_data, release["bait_id"], config["target"]["gene"], family_genes)
        observed = [row["prey_accession"] for row in rows]
        if sorted(observed) != sorted(release["expected_accessions"]):
            raise AssertionError(f"BioPlex {release['cell_line']} accessions: {observed}")
        for row in rows:
            row["cell_line"] = release["cell_line"]
            bioplex_rows.append(row)
    bioplex_fields = ["cell_line", "prey_accession"] + [x for x in bioplex_rows[0] if x not in {"cell_line", "prey_accession"}]
    write_tsv(out / "bioplex_LNP1_14-3-3_source_rows.tsv", bioplex_fields, bioplex_rows)
    summary["checks"]["bioplex"] = {
        "publication": "PMID:33961781",
        "exact_prey_accessions": sorted(set(row["prey_accession"] for row in bioplex_rows)),
        "method_from_intact": "MI:0007 anti tag coimmunoprecipitation; MI:0914 association; MI:1060 spoke expansion",
    }

    # PLATO / BioGRID discovery and Western-validation records.
    biogrid_rows: list[dict[str, str]] = []
    for interaction_id in config["plato"]["interactions"]:
        url = sources["biogrid_template"].format(interaction_id=interaction_id)
        data, meta = fetch(url)
        write_text_snapshot(raw / f"biogrid-{interaction_id}.html", data)
        record_source(manifest, f"biogrid:{interaction_id}", url, data, meta)
        biogrid_rows.append(extract_biogrid(data, interaction_id))
    if {x for row in biogrid_rows for x in (row["accession_a"], row["accession_b"])} != set(config["plato"]["expected_accessions"]):
        raise AssertionError("BioGRID PLATO accession mismatch")
    write_tsv(out / "plato_biogrid.tsv", list(biogrid_rows[0]), biogrid_rows)
    summary["checks"]["plato"] = biogrid_rows

    # hu.MAP3 target edges.
    humap_id = config["humap"]["complex_id"]
    humap_url = sources["humap_template"].format(complex_id=humap_id)
    humap_data, humap_meta = fetch(humap_url)
    write_text_snapshot(raw / f"{humap_id}.html", humap_data)
    record_source(manifest, f"humap:{humap_id}", humap_url, humap_data, humap_meta)
    table = TableParser("edges")
    table.feed(humap_data.decode("utf-8", errors="replace"))
    humap_rows = [
        {"protein_1": r[0], "protein_2": r[1], "score": r[2],
         "proteomehd": r[3] if len(r) > 3 else "", "interface_overlap": r[4] if len(r) > 4 else ""}
        for r in table.rows if len(r) >= 3 and config["humap"]["target_gene"] in r[:2]
    ]
    if len(humap_rows) != 7:
        raise AssertionError(f"expected seven LNP1 hu.MAP3 edges, got {len(humap_rows)}")
    write_tsv(out / "humap_LNP1_edges.tsv", list(humap_rows[0]), humap_rows)
    summary["checks"]["humap"] = humap_rows

    # Complex Portal: preserve the predicted flag, ECO code, members and null stoichiometry.
    complex_id = config["complex_portal"]["complex_id"]
    complex_url = sources["complex_portal_template"].format(complex_id=complex_id)
    complex_data, complex_meta = fetch(complex_url)
    write_text_snapshot(raw / f"{complex_id}.json", complex_data)
    record_source(manifest, f"complex-portal:{complex_id}", complex_url, complex_data, complex_meta)
    complex_record = json.loads(complex_data)
    if complex_record.get("predictedComplex") is not True or complex_record.get("evidenceType", {}).get("identifier") != "ECO:0008004":
        raise AssertionError("Complex Portal record is no longer marked machine-learning predicted")
    complex_members = [
        {"identifier": p.get("identifier", ""), "gene": p.get("name", ""),
         "description": p.get("description", ""), "stoichiometry": p.get("stochiometry")}
        for p in complex_record["participants"]
    ]
    write_tsv(out / "complex_portal_members.tsv", list(complex_members[0]), complex_members)
    summary["checks"]["complex_portal"] = {
        "predictedComplex": True,
        "evidence": complex_record["evidenceType"],
        "participant_count": len(complex_members),
    }

    # HuRI ORF mapping and exact LNP1-GPRIN2 edge from the official supplement.
    huri_data, huri_meta = fetch(sources["huri_supplement"])
    record_source(manifest, "huri:supplement", sources["huri_supplement"], huri_data, huri_meta)
    huri = config["huri"]
    table2, table2_header = selected_zip_lines(
        huri_data, huri["table2_member"],
        lambda r: bool(r) and r[0] in {huri["target_orf"], huri["partner_orf"]},
    )
    table9, table9_header = selected_zip_lines(
        huri_data, huri["table9_member"],
        lambda r: len(r) >= 2 and set(r[:2]) == {huri["target_gene_id"], huri["partner_gene_id"]},
    )
    if len(table2) != 2 or len(table9) != 1:
        raise AssertionError(f"HuRI mapping mismatch: table2={table2}, table9={table9}")
    write_text_snapshot(raw / "huri_table2_selected.tsv", (table2_header + "\n" + "\n".join(table2) + "\n").encode())
    write_text_snapshot(raw / "huri_table9_selected.tsv", (table9_header + "\n" + "\n".join(table9) + "\n").encode())
    summary["checks"]["huri"] = {"orf_mappings": table2, "interaction": table9[0]}

    # PMID30021884 exact XL-MS source row from Supplemental Table S2.
    xlms_data, xlms_meta = fetch(sources["xlms_supplement"])
    record_source(manifest, "xlms:supplement", sources["xlms_supplement"], xlms_data, xlms_meta)
    xlms = config["xlms"]
    with zipfile.ZipFile(io.BytesIO(xlms_data)) as outer:
        workbook = outer.read(xlms["workbook_member"])
    rows = read_xlsx_sheet(workbook, xlms["sheet"])
    header = rows[0]
    selected_xlms: list[dict[str, str]] = []
    for values in rows[1:]:
        row = dict(zip(header, values))
        a = row.get("Uniprot IDs A", "")
        b = row.get("Uniprot IDs B", "")
        if config["target"]["uniprot"] in {a, b} and xlms["partner_accession"] in (a + ";" + b).split(";"):
            selected_xlms.append(row)
    if len(selected_xlms) != 1:
        raise AssertionError(f"expected one LNP1-GAPDH XL-MS row, got {len(selected_xlms)}")
    write_tsv(raw / "pmid30021884_LNP1_GAPDH_source_row.tsv", header, selected_xlms)
    summary["checks"]["xlms"] = selected_xlms[0]

    # PMID31819260 exact A1A4G5 phosphosite row from official Supplementary Table S2.
    phosphosite_data, phosphosite_meta = fetch(sources["phosphosite_supplement_bundle"])
    record_source(
        manifest,
        "pmid31819260:supplementary-files",
        sources["phosphosite_supplement_bundle"],
        phosphosite_data,
        phosphosite_meta,
    )
    phosphosite = config["phosphosite"]
    with zipfile.ZipFile(io.BytesIO(phosphosite_data)) as outer:
        workbook = outer.read(phosphosite["workbook_member"])
    rows = read_xlsx_sheet(workbook, phosphosite["sheet"])
    header = rows[0]
    selected_phosphosites = [
        dict(zip(header, values))
        for values in rows[1:]
        if values
        and values[0] == phosphosite["accession"]
        and len(values) > 1
        and values[1] == phosphosite["position"]
    ]
    if len(selected_phosphosites) != 1:
        raise AssertionError(
            f"expected one {phosphosite['accession']} S{phosphosite['position']} row, "
            f"got {len(selected_phosphosites)}"
        )
    phosphosite_fields = [
        "uniprot", "position", "residue", "MQ_siteid", "best_PEP",
        "best_localization_prob", "biological_samples", "spectralcounts",
    ]
    write_tsv(
        raw / "pmid31819260_A1A4G5_S114_source_row.tsv",
        phosphosite_fields,
        selected_phosphosites,
    )
    summary["checks"]["phosphosite"] = {
        key: selected_phosphosites[0][key] for key in phosphosite_fields
    }

    # HPA antibody/cell-line snapshot.
    hpa_url = sources["hpa_template"].format(ensembl=config["target"]["ensembl"])
    hpa_data, hpa_meta = fetch(hpa_url)
    write_text_snapshot(raw / f"HPA-{config['target']['ensembl']}.xml", hpa_data)
    record_source(manifest, "hpa:LNP1", hpa_url, hpa_data, hpa_meta)
    root = ET.fromstring(hpa_data)
    antibody = root.find(f".//antibody[@id='{config['hpa']['antibody']}']")
    if antibody is None:
        raise AssertionError("configured HPA antibody not found")
    hpa_rows: list[dict[str, str]] = []
    for assay in antibody.findall("./cellExpression/subAssay"):
        if assay.attrib.get("subtype") != "human cell lines":
            continue
        reliability = assay.findtext("verification", default="")
        for data in assay.findall("data"):
            cell = data.find("cellLine")
            if cell is None:
                continue
            for location in data.findall("location"):
                hpa_rows.append({
                    "antibody": config["hpa"]["antibody"],
                    "reliability": reliability,
                    "cell_line": cell.text or "",
                    "cellosaurus": cell.attrib.get("cellosaurusID", ""),
                    "location": location.text or "",
                    "hpa_go_id": location.attrib.get("GOId", ""),
                })
    if not hpa_rows:
        raise AssertionError("no HPA cell-line localizations parsed")
    write_tsv(out / "hpa_localization_snapshot.tsv", list(hpa_rows[0]), hpa_rows)
    summary["checks"]["hpa"] = hpa_rows

    # Check that the validator-safe quotations used in RESULTS remain in local caches.
    if args.publications_dir:
        quote_checks = []
        for pmid in config["publications"]:
            path = args.publications_dir / f"PMID_{pmid}.md"
            quote_checks.append({"pmid": pmid, "path": str(path), "exists": path.exists()})
        write_tsv(out / "publication_cache_check.tsv", ["pmid", "path", "exists"], quote_checks)

    summary["generated_utc"] = datetime.now(timezone.utc).isoformat()
    summary["python"] = platform.python_version()
    (out / "audit_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_tsv(out / "source_manifest.tsv", [
        "name", "url", "byte_range", "bytes", "sha256", "status", "content_type",
        "content_range", "etag", "last_modified",
    ], manifest)
    print(json.dumps({"output_dir": str(out), "sources": len(manifest), "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
