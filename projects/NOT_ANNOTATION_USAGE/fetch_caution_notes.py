"""Fetch UniProt CAUTION comments for every protein carrying a NOT annotation.

Reads the accessions in ``not_annotations.tsv`` and queries the UniProt REST
API in batches, writing one row per accession to ``not_accessions_caution.tsv``
(accession, reviewed status, gene, CAUTION text joined with " || ", or empty).

Usage:
    uv run python projects/NOT_ANNOTATION_USAGE/fetch_caution_notes.py
"""

from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

import requests

HERE = Path(__file__).parent
NOTS = HERE / "not_annotations.tsv"
OUT = HERE / "not_accessions_caution.tsv"
URL = "https://rest.uniprot.org/uniprotkb/search"
BATCH = 100


def query(batch: list[str]) -> list[dict]:
    q = " OR ".join(f"accession:{a}" for a in batch)
    for attempt in range(6):
        r = requests.get(
            URL,
            params={"query": q, "fields": "accession,reviewed,gene_primary,cc_caution",
                    "format": "json", "size": 500},
            timeout=120,
        )
        if r.status_code == 200:
            return r.json().get("results", [])
        time.sleep(10 * (attempt + 1))
    r.raise_for_status()
    return []


def caution_text(entry: dict) -> str:
    texts = []
    for c in entry.get("comments", []):
        if c.get("commentType") == "CAUTION":
            for t in c.get("texts", []):
                texts.append(t.get("value", "").strip())
    return " || ".join(texts)


def main() -> int:
    with NOTS.open() as fh:
        accs = sorted({r["GENE PRODUCT ID"] for r in csv.DictReader(fh, delimiter="\t", lineterminator="\n")
                       if r["GENE PRODUCT DB"] == "UniProtKB"})
    base = {a.split("-")[0] for a in accs}
    todo = sorted(base)
    found: dict[str, dict] = {}
    for i in range(0, len(todo), BATCH):
        for e in query(todo[i:i + BATCH]):
            found[e["primaryAccession"]] = e
        print(f"{min(i + BATCH, len(todo))}/{len(todo)}", file=sys.stderr)
    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["accession", "reviewed", "gene", "caution"])
        for a in todo:
            e = found.get(a)
            if e is None:
                w.writerow([a, "not_found", "", ""])
                continue
            reviewed = "reviewed" if "Swiss-Prot" in e.get("entryType", "") else "unreviewed"
            genes = e.get("genes") or [{}]
            gene = (genes[0].get("geneName") or {}).get("value", "")
            w.writerow([a, reviewed, gene, caution_text(e)])
    print(f"wrote {len(todo)} accessions to {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
