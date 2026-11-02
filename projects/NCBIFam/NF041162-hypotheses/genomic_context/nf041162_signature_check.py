#!/usr/bin/env python3
"""Signature-level check: do viral SrpI-like capsids reach NCBIFAM NF041162?

Companion to ``nf041162_context.py`` (genomic context). This script makes
section 1 of ``RESULTS.md`` reproducible. It runs live queries and writes
``nf041162_signature_check.yaml``:

  * UniProtKB result counts for the signature queries in the RESULTS table
    (via the REST ``x-total-results`` header);
  * every viral (taxonomy 10239) UniProtKB entry carrying Pfam PF19307
    (SrpI-like), with organism, protein name and NCBIFAM assignments;
  * GO terms InterPro attaches to IPR045641 / IPR049822 (InterPro API);
  * NCBI's own ``go_terms`` for the relevant NCBIFAM models, with the
    ``hmm_PGAP`` release they come from.

UniProt reports every NCBIFAM signature an entry matches (e.g. 84 entries
carry both NF041162 and NF041163), so an empty NF045672 AND NF041162
intersection reflects disjoint model membership, not a best-hit artefact.

Usage:
    python nf041162_signature_check.py --out nf041162_signature_check.yaml
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import yaml

UNIPROT = "https://rest.uniprot.org/uniprotkb"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/interpro"
PGAP_TSV = "https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv"
PGAP_NOTES = "https://ftp.ncbi.nlm.nih.gov/hmm/current/RELEASE_NOTES.txt"
UA = "ai-gene-review-ncbifam/1.0"

COUNT_QUERIES = [
    "xref:ncbifam-NF041162",
    "xref:ncbifam-NF041162 AND taxonomy_id:10239",
    "xref:pfam-PF19307",
    "xref:pfam-PF19307 AND taxonomy_id:10239",
    "xref:pfam-PF04454",
    "xref:pfam-PF04454 AND taxonomy_id:10239",
    "xref:interpro-IPR045641 AND taxonomy_id:10239",
    "xref:ncbifam-NF045672",
    "xref:ncbifam-NF045672 AND xref:ncbifam-NF041162",
    "xref:ncbifam-NF041162 AND xref:ncbifam-NF041163",
    "xref:ncbifam-NF041162 AND xref:pfam-PF00027",
]
VIRAL_PF19307 = "xref:pfam-PF19307 AND taxonomy_id:10239"
INTERPRO_ENTRIES = ["IPR045641", "IPR049822"]
PGAP_MODELS = ["NF041162", "NF041163", "NF045672", "NF016349", "NF040250"]


def fetch(url: str) -> tuple[str, dict]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:  # noqa: S310
        return r.read().decode("utf-8", "replace"), dict(r.headers)


def uniprot_count(query: str) -> int:
    url = f"{UNIPROT}/search?" + urllib.parse.urlencode({"query": query, "size": 0})
    _, headers = fetch(url)
    return int({k.lower(): v for k, v in headers.items()}["x-total-results"])


def viral_entries() -> list[dict]:
    url = f"{UNIPROT}/stream?" + urllib.parse.urlencode({
        "query": VIRAL_PF19307, "format": "tsv",
        "fields": "accession,protein_name,organism_name,xref_ncbifam",
    })
    text, _ = fetch(url)
    rows = [(ln.split("\t") + [""] * 4)[:4] for ln in text.splitlines()[1:] if ln]
    return [
        {"accession": a, "protein_name": p, "organism": o,
         "ncbifam": [x for x in n.split(";") if x]}
        for a, p, o, n in rows
    ]


def interpro_go(entry: str) -> dict:
    url = f"{INTERPRO}/{entry}"
    meta = json.loads(fetch(url)[0])["metadata"]
    return {"endpoint": url, "name": meta["name"]["name"],
            "go_terms": [g["identifier"] for g in (meta.get("go_terms") or [])]}


def pgap_models() -> dict:
    notes, _ = fetch(PGAP_NOTES)
    m = re.search(r"Release number/name:\s*(\S+)", notes)
    rows = [ln.split("\t") for ln in fetch(PGAP_TSV)[0].splitlines()[1:] if ln]
    out = {"release": m.group(1) if m else None, "source": PGAP_TSV, "models": {}}
    for r in rows:
        acc = r[0].split(".")[0]
        if acc in PGAP_MODELS:
            out["models"][r[0]] = {"label": r[2], "family_type": r[6],
                                   "product_name": r[10],
                                   "go_terms": [g for g in r[14].split(",") if g]}
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path("nf041162_signature_check.yaml"))
    a = ap.parse_args()
    viral = viral_entries()
    result = {
        "queried": date.today().isoformat(),
        "uniprot_counts": {q: uniprot_count(q) for q in COUNT_QUERIES},
        "viral_pf19307_entries": viral,
        "viral_pf19307_by_ncbifam": {
            fam: sum(fam in e["ncbifam"] for e in viral)
            for fam in sorted({f for e in viral for f in e["ncbifam"]})
        } | {"none": sum(not e["ncbifam"] for e in viral)},
        "interpro_go": {e: interpro_go(e) for e in INTERPRO_ENTRIES},
        "ncbi_pgap": pgap_models(),
    }
    a.out.write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=True))
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
