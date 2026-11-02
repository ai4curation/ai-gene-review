"""Reproduce target-level inspection of all seven McBride 2017 supplement tables.

Run with the repository environment. Downloads publisher-deposited files through
Europe PMC; raw workbooks remain generated cache. No GOA files are used.
"""
from pathlib import Path
import hashlib
import io
import json
import zipfile
import requests
import openpyxl

URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5672003/supplementaryFiles"
CACHE = Path(".cache/module-audit-logs/ABCB19-28887381")
TARGETS = {"AT3G28860": "ABCB19", "AT1G70940": "PIN3", "AT2G36910": "ABCB1", "AT2G47000": "ABCB4"}

def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    if len(list(CACHE.glob("*.xlsx"))) != 7:
        response = requests.get(URL, timeout=180)
        response.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
            for name in archive.namelist():
                if name.endswith(".xlsx"):
                    (CACHE / Path(name).name).write_bytes(archive.read(name))
    files, hits, summary = [], [], []
    for path in sorted(CACHE.glob("*.xlsx")):
        files.append({"file": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        book = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for sheet in book:
            for index, row in enumerate(sheet.iter_rows(values_only=True), 1):
                text = " ".join(str(value) for value in row if value is not None)
                genes = [gene for locus, gene in TARGETS.items() if locus.lower() in text.lower()]
                if not genes:
                    continue
                hits.append({"file": path.name, "sheet": sheet.title, "row": index, "genes": genes})
                if sheet.title == "Mapp":
                    summary.append({"file": path.name, "sheet": sheet.title, "row": index,
                                    "group": row[2], "true_membrane": row[5],
                                    "dual_localized": row[6], "SUBAcon": row[9]})
        book.close()
    result = {"source_url": URL, "files": files, "summary_rows": summary, "all_target_hits": hits}
    destination = Path(__file__).with_name("28887381-target-evidence.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(destination)

if __name__ == "__main__":
    main()
