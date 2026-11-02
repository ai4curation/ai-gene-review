"""Resolve INNATE_IMMUNITY candidate genes to UniProt accessions.

Reads ``candidates.tsv`` (species code, NCBI taxon, gene symbol, display
label, optional pinned accession, family, module), queries the UniProt REST API for each symbol by exact gene name in
that taxon, and writes ``candidates-resolved.tsv``. Reviewed (Swiss-Prot)
entries are preferred; if none exists the unreviewed hits are reported with
their count so ambiguous matches are visible rather than silently picked.
Rows with a pinned ``accession`` (used where UniProt has no gene name, e.g.
Nematostella and horseshoe crab entries) are fetched by accession instead and
checked against the stated taxon. It also records whether a gene review folder already exists under genes/.

Nothing is hardcoded: a symbol UniProt does not know is written as
``NOT_FOUND`` and must be fixed in candidates.tsv, not filled in by hand.

Usage (from the repository root):
    uv run python projects/INNATE_IMMUNITY/scripts/resolve_candidates.py
"""

import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
REPO = HERE.parents[1]
API = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = "accession,reviewed,gene_primary,protein_name,length,annotation_score"


def query(symbol: str, taxon: str, accession: str = "") -> list[dict]:
    if accession:
        q = f"accession:{accession} AND organism_id:{taxon}"
    else:
        q = f'gene_exact:"{symbol}" AND organism_id:{taxon}'
    url = (
        API
        + "?"
        + urllib.parse.urlencode(
            {"query": q, "fields": FIELDS, "format": "json", "size": 25}
        )
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)["results"]
        except OSError:
            time.sleep(2**attempt)
    raise RuntimeError(f"UniProt query failed: {symbol} {taxon}")


def primary_gene(entry: dict) -> str:
    genes = entry.get("genes") or [{}]
    return genes[0].get("geneName", {}).get("value", "")


def protein_name(entry: dict) -> str:
    desc = entry.get("proteinDescription", {})
    rec = desc.get("recommendedName") or (desc.get("submissionNames") or [{}])[0]
    return rec.get("fullName", {}).get("value", "")


def main() -> None:
    rows = list(csv.DictReader(open(HERE / "candidates.tsv"), delimiter="\t"))
    out = []
    for row in rows:
        hits = query(row["symbol"], row["taxon"], row.get("accession", ""))
        # gene_exact also matches synonyms (e.g. Tlr11 hits the TLR12 entry), so
        # keep only entries whose primary gene name is the symbol when any exist.
        primary = [
            h
            for h in hits
            if row.get("accession") or primary_gene(h).lower() == row["symbol"].lower()
        ]
        pool = primary or hits
        reviewed = [h for h in pool if h["entryType"].startswith("UniProtKB reviewed")]
        pool = reviewed or pool
        pool.sort(key=lambda h: -h.get("annotationScore", 0))
        best = pool[0] if pool else None
        folder = REPO / "genes" / row["species"] / row["symbol"]
        out.append(
            {
                **{k: v for k, v in row.items() if k != "accession"},
                "accession": best["primaryAccession"] if best else "NOT_FOUND",
                "status": ("reviewed" if reviewed else "unreviewed") if best else "",
                "n_hits": len(pool),
                "primary_name_match": "yes" if primary else "no",
                "protein_name": protein_name(best) if best else "",
                "review_exists": "yes"
                if (folder / f"{row['symbol']}-ai-review.yaml").exists()
                else "no",
            }
        )
        time.sleep(0.1)
    with open(HERE / "candidates-resolved.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t")
        w.writeheader()
        w.writerows(out)
    found = sum(r["accession"] != "NOT_FOUND" for r in out)
    print(
        f"{found}/{len(out)} resolved; {sum(r['review_exists'] == 'yes' for r in out)} already reviewed"
    )


if __name__ == "__main__":
    main()
