#!/usr/bin/env python3
"""Classify every annotation to GO:0004321 fatty-acyl-CoA synthase activity.

GO:0004321 is defined by EC 2.3.1.86, the fungal type I fatty acid synthase
"system" (an alpha6beta6 complex of two multifunctional chains). This script
downloads all annotations to the term from QuickGO and the matching UniProtKB
entries, then sorts each annotation into a class by the protein's lineage,
PANTHER family, EC numbers and the annotation source.

Classes (first match wins):

* PTHR43605 acyl-CoA ligases: TreeGrafter rows, or any protein in PTHR43605
  (inherited from the PAINT root IBD on PTN001944787 seeded by RGD Acsm4).
* Fungal FAS, curated: SGD, PomBase and ComplexPortal rows.
* Fungal FAS subunits: any other row on a fungal protein.
* Experimental/ISO rows on other acyl-CoA ligases: non-IEA rows on non-fungal
  proteins, and EnsemblPlants projections.
* Bacterial PKS / PUFA-synthase multidomain proteins: bacterial members of the
  PKS/FAS-like families PTHR43775, PTHR43074, PTHR11712, PTHR10982.
* Other acyl-CoA ligases with EC 2.3.1.86 from submitters: ligase-named
  proteins or members of acyl-CoA ligase families.
* Non-fungal eukaryote FAS-like proteins (uncertain).
* Unrelated proteins with EC 2.3.1.86.
* Not resolved: annotated entries the UniProt query did not return.

Run from the repository root (needs network access):

    uv run python projects/FATTY_ACYL_COA_SYNTHASE_OBSOLETION/audit_go0004321.py

Writes ``usage_summary.yaml`` beside this script. Downloads are cached in
``.cache/go0004321/`` (git-ignored) and reused unless ``--refresh`` is given.
"""

from __future__ import annotations

import argparse
import csv
import io
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
CACHE = Path(".cache/go0004321")
TERM = "GO:0004321"
QUICKGO = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?"
    + urllib.parse.urlencode(
        {
            "goId": TERM,
            "goUsage": "exact",
            "downloadLimit": "100000",
            "selectedFields": "geneProductId,symbol,evidenceCode,goEvidence,reference,"
            "withFrom,taxonId,assignedBy,qualifier",
        }
    )
)
UNIPROT = "https://rest.uniprot.org/uniprotkb/stream?" + urllib.parse.urlencode(
    {
        "query": "go:0004321",
        "fields": "accession,reviewed,protein_name,ec,xref_panther,lineage,organism_name",
        "format": "tsv",
    }
)
PKS_FAS_FAMILIES = {"PTHR43775", "PTHR43074", "PTHR11712", "PTHR10982"}
LIGASE_FAMILIES = {
    "PTHR43767",
    "PTHR43201",
    "PTHR24096",
    "PTHR43107",
    "PTHR22754",
    "PTHR43272",
    "PTHR43859",
}
KINGDOMS = ("Fungi", "Metazoa", "Viridiplantae", "Bacteria", "Archaea")


def fetch(url: str, path: Path, refresh: bool, accept: str) -> str:
    """Download ``url`` to ``path`` unless a cached copy exists."""
    if refresh or not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={"Accept": accept})
        with urllib.request.urlopen(req, timeout=600) as resp:
            path.write_bytes(resp.read())
    return path.read_text()


def kingdom(lineage: str) -> str:
    """Coarse lineage bucket.

    >>> kingdom("cellular organisms (no rank), Eukaryota (domain), Fungi (kingdom)")
    'Fungi'
    >>> kingdom("cellular organisms (no rank), Eukaryota (domain), Sar (clade)")
    'other eukaryote'
    """
    for k in KINGDOMS:
        if k in lineage:
            return k
    return "other eukaryote" if "Eukaryota" in lineage else "unknown"


def family(panther: str) -> str:
    """First PANTHER family (not subfamily) id.

    >>> family("PTHR43605:SF10;PTHR43605;")
    'PTHR43605'
    """
    fams = [p for p in panther.split(";") if p and ":SF" not in p]
    return fams[0] if fams else ""


def classify(row: dict, entry: dict | None) -> str:
    """Assign one QuickGO annotation row to a class."""
    source, evidence = row["ASSIGNED BY"], row["GO EVIDENCE CODE"]
    if source == "TreeGrafter" or (entry and family(entry["PANTHER"]) == "PTHR43605"):
        return "PTHR43605 acyl-CoA ligases (PAINT root IBD seeded by RGD Acsm4)"
    if row["GENE PRODUCT DB"] == "ComplexPortal" or source in ("SGD", "PomBase"):
        return "Fungal FAS, curated (SGD, PomBase, ComplexPortal)"
    if entry is None:
        return "Not resolved (entry not returned by UniProt query)"
    king = kingdom(entry["Taxonomic lineage"])
    fam = family(entry["PANTHER"])
    name = entry["Protein names"].lower()
    if king == "Fungi":
        return "Fungal FAS subunits"
    if evidence != "IEA" or source == "EnsemblPlants":
        return "Experimental/ISO rows on other acyl-CoA ligases"
    if king == "Bacteria" and fam in PKS_FAS_FAMILIES:
        return "Bacterial PKS / PUFA-synthase multidomain proteins"
    if (
        "6.2.1" in entry["EC number"]
        or "ligase" in name
        or "synthetase" in name
        or "coa synth" in name
        or fam in LIGASE_FAMILIES
    ):
        return "Other acyl-CoA ligases with EC 2.3.1.86 from submitters"
    if king == "other eukaryote" and fam in PKS_FAS_FAMILIES | {""}:
        return "Non-fungal eukaryote FAS-like proteins (uncertain)"
    return "Unrelated proteins with EC 2.3.1.86"


def main() -> None:
    """Download, classify and write ``usage_summary.yaml``."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--refresh", action="store_true", help="re-download sources")
    args = parser.parse_args()
    quickgo = fetch(QUICKGO, CACHE / "quickgo.tsv", args.refresh, "text/tsv")
    uniprot = fetch(UNIPROT, CACHE / "uniprot.tsv", args.refresh, "text/plain")
    rows = list(csv.DictReader(io.StringIO(quickgo), delimiter="\t"))
    entries = {
        e["Entry"]: e for e in csv.DictReader(io.StringIO(uniprot), delimiter="\t")
    }

    counts: Counter[str] = Counter()
    sources: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        cls = classify(row, entries.get(row["GENE PRODUCT ID"]))
        counts[cls] += 1
        sources[cls][f"{row['GO EVIDENCE CODE']}/{row['ASSIGNED BY']}"] += 1
    non_iea = sorted(
        {
            (
                r["GO EVIDENCE CODE"],
                r["ASSIGNED BY"],
                r["SYMBOL"],
                r["GENE PRODUCT ID"],
                r["REFERENCE"],
                r["TAXON ID"],
            )
            for r in rows
            if r["GO EVIDENCE CODE"] not in ("IEA", "IBA")
        }
    )
    summary = {
        "term": {"id": TERM, "label": "fatty-acyl-CoA synthase activity"},
        "retrieved": date.fromtimestamp(
            (CACHE / "quickgo.tsv").stat().st_mtime
        ).isoformat(),
        "total_annotations": len(rows),
        "uniprot_entries": len(entries),
        "classes": [
            {"class": c, "annotations": n, "sources": dict(sources[c].most_common())}
            for c, n in counts.most_common()
        ],
        "non_iea_non_iba_annotations": [
            {
                "evidence": e,
                "assigned_by": a,
                "symbol": s,
                "id": i,
                "reference": ref,
                "taxon": t,
            }
            for e, a, s, i, ref, t in non_iea
        ],
    }
    out = HERE / "usage_summary.yaml"
    out.write_text(
        yaml.safe_dump(summary, sort_keys=False, allow_unicode=True, width=100)
    )
    for c, n in counts.most_common():
        print(f"{n:6d}  {c}")
    print(f"{len(rows):6d}  total -> {out}")


if __name__ == "__main__":
    main()
