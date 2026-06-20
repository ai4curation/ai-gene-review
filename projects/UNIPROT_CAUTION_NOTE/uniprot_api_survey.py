#!/usr/bin/env python3
"""Survey UniProtKB CAUTION comments database-wide via the REST API.

Unlike `extract_caution_notes.py` (which reads the genes we have already
fetched), this script queries the live UniProt REST API so we can see the
*global* distribution of CAUTION comments without running `fetch-gene` on
anything. It downloads, for every reviewed (Swiss-Prot) entry that carries a
`cc_caution` comment, the accession / gene / organism / protein name / caution
text, then aggregates locally.

The `cc_caution` query field matches the free-text CAUTION comment ONLY; it is
distinct from `cc_sequence_caution` (erroneous initiation / frameshift), which
we deliberately ignore.

Usage:
    python uniprot_api_survey.py                 # all reviewed entries
    python uniprot_api_survey.py --organism 9606 # restrict to a taxon id
    python uniprot_api_survey.py --no-download    # re-analyze cached TSV only

Outputs (regenerated, not hand-edited):
    caution_uniprot_reviewed.tsv  - raw per-entry download (one row per entry)
    api_survey.md                 - aggregated distribution report

Never hardcodes results. Categorization mirrors extract_caution_notes.py.
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

BASE = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = "accession,gene_primary,organism_name,organism_id,protein_name,cc_caution"
PMID_RE = re.compile(r"(?:PubMed|PMID):(\d+)", re.IGNORECASE)
OUT_DIR = Path(__file__).resolve().parent


def categorize(text: str) -> str:
    """Same taxonomy as extract_caution_notes.py, applied per individual note."""
    t = text.lower()
    if "whole genome shotgun" in t or " wgs " in t:
        return "wgs-preliminary"
    if "lacks conserved residue" in t:
        return "lacks-conserved-residue"
    if "retract" in t:
        return "retracted-reference"
    if (("lacks" in t and any(w in t for w in ("active site", "catalytic", "conserved",
                                               "heme-binding", "phospho-accepting",
                                               "essential", "required")))
            or ("although" in t and "lacks" in t)
            or "probably not" in t or "may not be functional" in t):
        return "degenerate-domain"
    if ("was initially" in t or "was originally" in t or "was reported" in t
            or "originally thought" in t or "initially believed" in t or "previously" in t):
        return "reclassified-function"
    if "artifact" in t or "artefact" in t:
        return "possible-artifact"
    if any(w in t for w in ("controvers", "uncertain", "in contrast", "however",
                            "may not", "could be", "disput", "remains to be",
                            "not clear", "unclear", "questioned")):
        return "contested-function"
    return "other"


def split_notes(field: str) -> list[str]:
    """A cc_caution TSV cell may concatenate several 'CAUTION: ...' comments."""
    field = field.strip()
    if not field:
        return []
    parts = re.split(r"(?:^|\s)CAUTION:\s*", field)
    return [p.strip() for p in parts if p.strip()]


def fetch_all(query: str, size: int = 500) -> list[list[str]]:
    """Cursor-paginate the search API, returning data rows (no header)."""
    params = {"query": query, "format": "tsv", "fields": FIELDS, "size": str(size)}
    url = BASE + "?" + urllib.parse.urlencode(params)
    rows: list[list[str]] = []
    header_seen = False
    page = 0
    while url:
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={"Accept": "text/plain"})
                with urllib.request.urlopen(req, timeout=120) as resp:
                    body = resp.read().decode("utf-8", "replace")
                    link = resp.headers.get("Link", "")
                break
            except Exception as e:  # network hiccup -> exponential backoff
                if attempt == 4:
                    raise
                wait = 2 ** (attempt + 1)
                print(f"  retry {attempt+1} after {wait}s ({e})", file=sys.stderr)
                time.sleep(wait)
        lines = body.splitlines()
        if lines and lines[0].startswith("Entry"):
            lines = lines[1:]
            header_seen = True
        for ln in lines:
            rows.append(ln.split("\t"))
        page += 1
        print(f"  page {page}: +{len(lines)} rows (total {len(rows)})", file=sys.stderr)
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
    if not header_seen:
        print("  WARNING: no header row seen; API response format may have changed",
              file=sys.stderr)
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--organism", help="restrict to an NCBI taxon id (e.g. 9606)")
    ap.add_argument("--reviewed", default="true", choices=["true", "false"])
    ap.add_argument("--no-download", action="store_true",
                    help="skip API; re-analyze cached TSV")
    args = ap.parse_args()

    tsv_path = OUT_DIR / "caution_uniprot_reviewed.tsv"

    if not args.no_download:
        query = f"cc_caution:* AND reviewed:{args.reviewed}"
        if args.organism:
            query += f" AND organism_id:{args.organism}"
        print(f"querying: {query}", file=sys.stderr)
        rows = fetch_all(query)
        with tsv_path.open("w", encoding="utf-8") as fh:
            fh.write("accession\tgene\torganism\torganism_id\tprotein_name\tcaution\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")
        print(f"wrote {tsv_path} ({len(rows)} entries)", file=sys.stderr)

    # ---- analyze ----
    entries = 0
    notes_total = 0
    cat_counter: Counter[str] = Counter()
    org_counter: Counter[str] = Counter()
    org_cat: dict[str, Counter[str]] = {}
    retracted_entries: list[tuple[str, str, str]] = []  # (acc, gene, organism)

    with tsv_path.open(encoding="utf-8") as fh:
        header = fh.readline()
        for line in fh:
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 6:
                continue
            acc, gene, organism, org_id, pname, caution = cols[:6]
            entries += 1
            org_counter[organism] += 1
            for note in split_notes(caution):
                notes_total += 1
                cat = categorize(note)
                cat_counter[cat] += 1
                org_cat.setdefault(organism, Counter())[cat] += 1
                if cat == "retracted-reference":
                    retracted_entries.append((acc, gene or "?", organism))

    n_relevant = sum(c for k, c in cat_counter.items()
                     if k not in ("wgs-preliminary", "lacks-conserved-residue", "other"))

    md = OUT_DIR / "api_survey.md"
    with md.open("w", encoding="utf-8") as fh:
        fh.write("---\ntitle: \"UniProt CAUTION Notes — Database-Wide API Survey\"\n---\n\n")
        fh.write("# UniProt CAUTION Notes — Database-Wide API Survey\n\n")
        fh.write("Auto-generated by `uniprot_api_survey.py` (live UniProt REST API). "
                 "Do not edit by hand.\n\n")
        fh.write(f"- Reviewed (Swiss-Prot) entries with a CAUTION comment: **{entries}**\n")
        fh.write(f"- Individual CAUTION notes parsed: **{notes_total}**\n")
        fh.write(f"- High-signal notes (excl. boilerplate + 'other'): **{n_relevant}**\n\n")

        fh.write("## Notes by category\n\n")
        fh.write("| Category | Notes |\n|---|--:|\n")
        for cat, n in cat_counter.most_common():
            fh.write(f"| {cat} | {n} |\n")
        fh.write("\n")

        fh.write("## Top 25 organisms by entries with CAUTION notes\n\n")
        fh.write("| Organism | Entries |\n|---|--:|\n")
        for org, n in org_counter.most_common(25):
            fh.write(f"| {org} | {n} |\n")
        fh.write("\n")

        fh.write(f"## Retracted-reference entries ({len(retracted_entries)})\n\n")
        fh.write("| Accession | Gene | Organism |\n|---|---|---|\n")
        for acc, gene, organism in sorted(retracted_entries):
            fh.write(f"| {acc} | {gene} | {organism} |\n")
        fh.write("\n")

    print(f"entries={entries} notes={notes_total} high_signal={n_relevant} "
          f"retracted={len(retracted_entries)}")
    print(f"wrote {md}")


if __name__ == "__main__":
    main()
