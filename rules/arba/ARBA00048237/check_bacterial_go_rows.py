"""Trace the bacterial GO:0004321 rows that QuickGO serves to their EC source.

1. Download every GO:0004321 annotation on Bacteria from QuickGO and count rows
   by reference (GO_REF:0000003 is EC2GO, GO_REF:0000117 is ARBA).
2. For each EC2GO row, look the entry up in the current UniProtKB release and
   record whether it still carries EC 2.3.1.86, and on what evidence.
3. For the first entry that no longer carries it, read its UniSave history and
   report which versions carried EC 2.3.1.86 and with what evidence line.

Writes RESULTS-bacterial-rows.md next to this script.

Usage: python check_bacterial_go_rows.py
"""

from __future__ import annotations

import csv
import io
import json
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?" + urllib.parse.urlencode(
    {
        "goId": "GO:0004321",
        "goUsage": "exact",
        "taxonId": "2",
        "taxonUsage": "descendants",
        "selectedFields": "geneProductId,goEvidence,reference,assignedBy,withFrom",
        "downloadLimit": "50000",
    }
)
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"


def fetch(url: str, accept: str = "application/json") -> tuple[bytes, dict]:
    """GET with retries; return body and headers."""
    req = urllib.request.Request(url, headers={"Accept": accept})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read(), dict(r.headers)
        except Exception:  # network: retry with backoff
            if attempt == 3:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("unreachable")


def ec_evidence(entry: dict) -> list[str]:
    """Evidence codes on EC 2.3.1.86 in the entry's names and catalytic activities."""
    found: list[str] = []
    for c in entry.get("comments", []):
        r = c.get("reaction", {})
        if r.get("ecNumber") == "2.3.1.86":
            found += [f"CA {e.get('evidenceCode')} {e.get('source', '')}:{e.get('id', '')}" for e in r.get("evidences", [])] or ["CA curated"]
    desc = entry.get("proteinDescription", {})
    names = list(desc.get("submissionNames") or []) + ([desc["recommendedName"]] if desc.get("recommendedName") else [])
    for n in names:
        for x in n.get("ecNumbers", []):
            if x["value"] == "2.3.1.86":
                found += [f"DE {e.get('evidenceCode')} {e.get('source', '')}" for e in x.get("evidences", [])] or ["DE curated"]
    return found


def main() -> None:
    """Run the three steps and write RESULTS-bacterial-rows.md."""
    body, _ = fetch(QUICKGO, "text/tsv")
    rows = list(csv.DictReader(io.StringIO(body.decode()), delimiter="\t"))
    by_ref = Counter(f"{r['REFERENCE']} / {r['ASSIGNED BY']}" for r in rows)
    accs = sorted({r["GENE PRODUCT ID"] for r in rows if r["REFERENCE"] == "GO_REF:0000003"})

    status: Counter[str] = Counter()
    release = None
    without: list[str] = []
    for i in range(0, len(accs), 100):
        chunk = accs[i : i + 100]
        q = " OR ".join(f"accession:{a}" for a in chunk)
        url = UNIPROT + "?" + urllib.parse.urlencode(
            {"query": q, "format": "json", "size": "100", "fields": "accession,protein_name,ec,cc_catalytic_activity"}
        )
        data, headers = fetch(url)
        release = headers.get("X-UniProt-Release") or headers.get("x-uniprot-release") or release
        got = json.loads(data)["results"]
        status["not in current release"] += len(chunk) - len(got)
        for e in got:
            ev = ec_evidence(e)
            key = "; ".join(sorted(set(ev))) if ev else "no EC 2.3.1.86 in current entry"
            status[key] += 1
            if not ev:
                without.append(e["primaryAccession"])

    history: list[str] = []
    if without:
        acc = without[0]
        versions = json.loads(fetch(f"https://rest.uniprot.org/unisave/{acc}?format=json")[0])["results"][:12]
        for v in versions:
            txt = fetch(
                f"https://rest.uniprot.org/unisave/{acc}?format=txt&versions={v['entryVersion']}", "text/plain"
            )[0].decode()
            hits = [ln.strip() for ln in txt.splitlines() if "EC=2.3.1.86" in ln or "ARBA00048237" in ln]
            history.append(f"- {acc} version {v['entryVersion']} ({v.get('lastReleaseDate', '')}): "
                           + (" / ".join(hits) if hits else "no EC 2.3.1.86"))

    lines = [
        "# Bacterial GO:0004321 rows and their EC source",
        "",
        f"QuickGO retrieved {time.strftime('%Y-%m-%d')}; UniProtKB release {release}. "
        "Produced by `check_bacterial_go_rows.py`.",
        "",
        f"QuickGO serves {len(rows)} GO:0004321 annotations on Bacteria:",
        "",
        *[f"- {k}: {v}" for k, v in by_ref.most_common()],
        "",
        f"The {len(accs)} entries with an EC2GO (GO_REF:0000003) row, in the current UniProtKB release:",
        "",
        *[f"- {k}: {v}" for k, v in status.most_common()],
        "",
        "History of the first entry that no longer carries EC 2.3.1.86:",
        "",
        *history,
    ]
    Path(__file__).with_name("RESULTS-bacterial-rows.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
