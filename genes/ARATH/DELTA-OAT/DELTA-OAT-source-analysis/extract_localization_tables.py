# /// script
# dependencies = ["requests", "openpyxl"]
# ///
"""Extract exact target rows from the publisher-deposited PMID 28887381 supplement."""
import hashlib
import io
import json
from pathlib import Path
import zipfile
import openpyxl
import requests

URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5672003/supplementaryFiles"
TARGETS = ["AT5G46180", "AT5G62530", "AT4G08900", "AT4G08870"]
response = requests.get(URL, timeout=120)
response.raise_for_status()
archive = zipfile.ZipFile(io.BytesIO(response.content))
report = {"source_url": URL, "pmid": "28887381", "targets": TARGETS, "tables": []}
for name in sorted(archive.namelist()):
    if not name.endswith(".xlsx"):
        continue
    raw = archive.read(name)
    workbook = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)
    entry = {"file": name, "sha256": hashlib.sha256(raw).hexdigest(), "sheets": []}
    for sheet in workbook:
        # Keep interpretive summary tables, not thousands of individual spectra.
        if "raw" in sheet.title.lower() or "gaussian fitted" in sheet.title.lower():
            continue
        rows = list(sheet.values)
        matches = [{"excel_row": i + 1, "values": list(row)} for i, row in enumerate(rows)
                   if any(target in str(value).upper() for target in TARGETS for value in row)]
        entry["sheets"].append({"sheet": sheet.title, "header_rows": rows[:5], "matches": matches})
    report["tables"].append(entry)
Path(__file__).with_name("localization-table-extraction.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False) + "\n")
