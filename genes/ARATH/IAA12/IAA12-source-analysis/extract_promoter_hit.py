"""Reproduce the primary IAA12 promoter hit; no GO annotation is used as evidence."""

from pathlib import Path
import hashlib
import io
import json
import zipfile

import openpyxl
import requests

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
URL = "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature14099/MediaObjects/41586_2015_BFnature14099_MOESM86_ESM.zip"


def main():
    response = requests.get(URL, timeout=60)
    response.raise_for_status()
    raw = response.content
    cache = ROOT / ".cache/module-audit-logs/auxin-iaa12-supplements"
    cache.mkdir(parents=True, exist_ok=True)
    (cache / "nature14099-supplements.zip").write_bytes(raw)
    archive = zipfile.ZipFile(io.BytesIO(raw))
    hits = []
    for name in archive.namelist():
        if not name.endswith(".xlsx"):
            continue
        data = archive.read(name)
        workbook = openpyxl.load_workbook(
            io.BytesIO(data), read_only=True, data_only=True
        )
        for sheet in workbook:
            for number, row in enumerate(sheet.values, 1):
                if any("AT1G04550" in str(cell).upper() for cell in row):
                    hits.append(
                        {
                            "file": name,
                            "sheet": sheet.title,
                            "row": number,
                            "values": list(row),
                            "sha256": hashlib.sha256(data).hexdigest(),
                        }
                    )
    assert any(
        hit["values"][:4] == ["AT1G04550", "AT5G12870", "ppp, x", 1] for hit in hits
    )
    result = {
        "source": "PMID:25533953",
        "publisher_supplement_url": URL,
        "archive_sha256": hashlib.sha256(raw).hexdigest(),
        "matches": hits,
    }
    (OUT / "promoter-hit.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
