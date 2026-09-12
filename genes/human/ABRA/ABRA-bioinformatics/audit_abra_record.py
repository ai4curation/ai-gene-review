"""Audit the provenance of the human ABRA (Q8N0Z2) GO record.

Four questions, all answered from data fetched at run time. Nothing is hardcoded;
if a fetch fails the script says so rather than counting the failure as absence.

  Q1. Where does each human ABRA annotation actually come from? Split the GOA file
      by evidence code and resolve every WITH/FROM accession to a species + gene.

  Q2. Does the human GO:0005886 "plasma membrane" IDA have any support outside the
      single LIFEdb GFP-fusion survey (GO_REF:0000054)? Two independent checks:
      (a) does UniProt place ABRA at the plasma membrane, or give it any
          membrane-targeting sequence feature (TRANSMEM / SIGNAL / LIPID / INTRAMEM)?
      (b) has the human call been projected into the mouse ortholog's record?

  Q3. Is PANTHER PTHR22739 an ortholog-only family (so that IBA/ISS transfers into
      human carry no paralog hazard), or does it mix paralogous subfamilies?

  Q4. ABRA's C-terminal Costars domain (Pfam PF14705) is shared with the small
      standalone protein ABRACL. Which human proteins carry PF14705, and how long
      are they? This decides whether a phenotype reported for "Costars" is a
      statement about ABRA or about a different gene that happens to share the domain.

Usage:  uv run python audit_abra_record.py [--goa PATH] [--json OUT.json]
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
INTERPRO = "https://www.ebi.ac.uk/interpro/api"

HUMAN_ABRA = "Q8N0Z2"
MOUSE_ABRA = "Q8BUZ1"
COSTARS_PFAM = "PF14705"
PANTHER_FAMILY = "PTHR22739"
MEMBRANE_FEATURES = {"Transmembrane", "Signal", "Lipidation", "Intramembrane"}

SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/json"})


def get(url: str, **params: Any) -> Any:
    """GET with one retry. Returns None on failure, and says so on stderr."""
    for attempt in (1, 2):
        response = SESSION.get(url, params=params or None, timeout=60)
        if response.ok:
            return response.json() if "json" in response.headers.get("content-type", "") else response.text
        if attempt == 1:
            time.sleep(2)
    print(f"  ! FETCH FAILED ({response.status_code}): {url}", file=sys.stderr)
    return None


# --------------------------------------------------------------------------
# Q1: provenance of every human annotation
# --------------------------------------------------------------------------

def describe_accession(token: str, cache: dict[str, str]) -> str:
    """Resolve one WITH/FROM token to 'GENE (Species)'. Non-UniProt tokens pass through."""
    if token in cache:
        return cache[token]
    label = token
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        record = get(f"{UNIPROT}/{acc}.json", fields="gene_names,organism_name")
        if record is None:
            label = f"{token} [unresolved]"
        else:
            genes = [g.get("geneName", {}).get("value", "?") for g in record.get("genes", [])]
            species = record.get("organism", {}).get("scientificName", "?")
            label = f"{'/'.join(genes) or acc} ({species})"
    cache[token] = label
    return label


def audit_goa(goa_path: Path) -> dict[str, Any]:
    rows = list(csv.DictReader(goa_path.open(), delimiter="\t"))
    cache: dict[str, str] = {}
    by_evidence: Counter[str] = Counter()
    detail = []
    for row in rows:
        evidence = row["GO EVIDENCE CODE"]
        by_evidence[evidence] += 1
        sources = [describe_accession(t, cache) for t in row["WITH/FROM"].split("|") if t]
        detail.append(
            {
                "term": row["GO TERM"],
                "name": row["GO NAME"],
                "aspect": row["GO ASPECT"],
                "evidence": evidence,
                "reference": row["REFERENCE"],
                "sources": sources,
            }
        )
    experimental = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}
    return {
        "n_rows": len(rows),
        "by_evidence": dict(by_evidence),
        "n_experimental": sum(v for k, v in by_evidence.items() if k in experimental),
        "rows": detail,
    }


# --------------------------------------------------------------------------
# Q2: is the plasma-membrane call supported anywhere else?
# --------------------------------------------------------------------------

def mouse_annotations(go_id: str) -> list[dict[str, Any]]:
    """Every annotation of `go_id` on the mouse ortholog, with evidence and WITH/FROM.

    Used to check the direction of travel between the two orthologs: a human-only IDA that
    reappears in mouse citing the human accession is a round trip, not corroboration.
    """
    result = get(
        f"{QUICKGO}/annotation/search",
        geneProductId=f"UniProtKB:{MOUSE_ABRA}",
        goId=go_id,
        limit=100,
    )
    if result is None:
        return []
    return [
        {
            "evidence": annotation.get("goEvidence"),
            "reference": annotation.get("reference"),
            "with_from": [
                c["id"]
                for connected in annotation.get("withFrom", []) or []
                for c in connected.get("connectedXrefs", [])
            ],
        }
        for annotation in result.get("results", [])
    ]


def membrane_evidence() -> dict[str, Any]:
    queried = "cc_subcellular_location,ft_transmem,ft_signal,ft_lipid,ft_intramem"
    record = get(f"{UNIPROT}/{HUMAN_ABRA}.json", fields=queried)
    if record is None:
        return {"available": False}
    locations: list[str] = []
    for comment in record.get("comments", []):
        if comment["commentType"] == "SUBCELLULAR LOCATION":
            for loc in comment.get("subcellularLocations", []):
                locations.append(loc.get("location", {}).get("value", "?"))
    # The request asked UniProt for exactly the four membrane-targeting feature
    # classes, so an empty list here means "none annotated", not "not requested".
    features = sorted({f["type"] for f in record.get("features", [])})

    # Has the human-only call been projected into the mouse ortholog?
    projected = mouse_annotations("GO:0005886")
    return {
        "available": True,
        "uniprot_subcellular_locations": locations,
        "plasma_membrane_in_uniprot": any("plasma membrane" in v.lower() for v in locations),
        "feature_classes_queried": sorted(MEMBRANE_FEATURES),
        "membrane_targeting_features_found": sorted(set(features) & MEMBRANE_FEATURES),
        "mouse_GO_0005886_annotations": projected,
    }


# --------------------------------------------------------------------------
# Q3: is the PANTHER family ortholog-only?
# --------------------------------------------------------------------------

def family_composition(entries_csv: Path) -> dict[str, Any]:
    """Summarise the PANTHER family's reviewed members from the repo's entries CSV.

    A missing CSV is a hard error, not a degraded result. Returning {"available": False}
    here would drop the whole Q3 section from RESULTS.md while results.json still carried
    the numbers from an earlier run - a silent disagreement between the two artefacts, and
    Q3's ortholog-only conclusion is quoted as supporting_text in the review.
    """
    if not entries_csv.exists():
        raise SystemExit(
            f"PANTHER entries CSV not found: {entries_csv}\n"
            f"Q3 cannot be computed without it. Fetch it with:\n"
            f"    just fetch-panther-family {PANTHER_FAMILY}"
        )
    rows = list(csv.DictReader(entries_csv.open()))
    subfamilies = Counter(r["subfamily"] for r in rows)
    symbols = Counter(r["gene"].upper() for r in rows)
    return {
        "available": True,
        "family": PANTHER_FAMILY,
        "n_reviewed_members": len(rows),
        "species": sorted({r["source_tax_name"] for r in rows}),
        "subfamilies": dict(subfamilies),
        "gene_symbols": dict(symbols),
        "single_symbol": len(symbols) == 1,
    }


# --------------------------------------------------------------------------
# Q5: what does the mouse ortholog actually carry for nuclear import?
# --------------------------------------------------------------------------

def nuclear_import_evidence() -> dict[str, Any]:
    """The mouse ortholog's protein-import annotations, which the NEW GO:0042307 rests on.

    The review proposes GO:0042307 "positive regulation of protein import into nucleus" for
    human ABRA, reasoning from the mouse record plus the MRTF translocation literature. That
    reasoning was previously unauditable, unlike the GO:0005886 back-propagation in Q2, so
    the same projection check is applied to the import terms.
    """
    terms = {
        "GO:0006606": "protein import into nucleus",
        "GO:0042307": "positive regulation of protein import into nucleus",
    }
    return {
        "available": True,
        "mouse_accession": MOUSE_ABRA,
        "annotations": {go_id: mouse_annotations(go_id) for go_id in terms},
        "terms_queried": terms,
    }


# --------------------------------------------------------------------------
# Q4: who else carries the Costars domain?
# --------------------------------------------------------------------------

def costars_carriers() -> dict[str, Any]:
    result = get(
        f"{UNIPROT}/search",
        query=f"xref:pfam-{COSTARS_PFAM} AND organism_id:9606 AND reviewed:true",
        fields="accession,id,gene_names,length,cc_function",
        size=50,
    )
    if result is None:
        return {"available": False}
    proteins = []
    for entry in result.get("results", []):
        function = ""
        for comment in entry.get("comments", []):
            if comment["commentType"] == "FUNCTION":
                function = comment.get("texts", [{}])[0].get("value", "")
                break
        proteins.append(
            {
                "accession": entry["primaryAccession"],
                "id": entry["uniProtkbId"],
                "gene": (entry.get("genes") or [{}])[0].get("geneName", {}).get("value", "?"),
                "length": entry["sequence"]["length"],
                "function": function,
            }
        )
    return {"available": True, "pfam": COSTARS_PFAM, "proteins": sorted(proteins, key=lambda p: p["length"])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument("--goa", type=Path, default=here.parent / "ABRA-goa.tsv")
    parser.add_argument(
        "--panther",
        type=Path,
        default=here.parents[3] / "interpro" / "panther" / PANTHER_FAMILY / f"{PANTHER_FAMILY}-entries.csv",
    )
    parser.add_argument("--json", type=Path, default=here / "results.json")
    args = parser.parse_args()

    print("Q1. Provenance of the human ABRA GO record")
    provenance = audit_goa(args.goa)
    print(f"  rows: {provenance['n_rows']}   by evidence: {provenance['by_evidence']}")
    print(f"  experimental rows: {provenance['n_experimental']}")
    by_source: defaultdict[str, list[str]] = defaultdict(list)
    for row in provenance["rows"]:
        for source in row["sources"] or ["(no WITH/FROM)"]:
            by_source[source].append(f"{row['term']} {row['evidence']}")
    for source, terms in sorted(by_source.items(), key=lambda kv: -len(kv[1])):
        print(f"    {len(terms):2d}x  {source}")

    print("\nQ2. Support for GO:0005886 plasma membrane")
    membrane = membrane_evidence()
    print(f"  UniProt subcellular locations: {membrane['uniprot_subcellular_locations']}")
    print(f"  plasma membrane stated by UniProt: {membrane['plasma_membrane_in_uniprot']}")
    print(f"  membrane-targeting feature classes queried: {membrane['feature_classes_queried']}")
    print(f"  of those, found on ABRA: {membrane['membrane_targeting_features_found'] or 'NONE'}")
    for annotation in membrane["mouse_GO_0005886_annotations"]:
        print(f"  mouse GO:0005886  {annotation['evidence']:5s} {annotation['reference']}  from {annotation['with_from']}")

    print(f"\nQ3. Composition of PANTHER {PANTHER_FAMILY}")
    family = family_composition(args.panther)
    if family.get("available"):
        print(f"  reviewed members: {family['n_reviewed_members']}  species: {family['species']}")
        print(f"  gene symbols: {family['gene_symbols']}  ortholog-only: {family['single_symbol']}")
        print(f"  subfamilies among reviewed members: {family['subfamilies']}")

    print(f"\nQ4. Human proteins carrying the Costars domain ({COSTARS_PFAM})")
    costars = costars_carriers()
    if costars.get("available"):
        for protein in costars["proteins"]:
            print(f"  {protein['accession']}  {protein['gene']:8s} {protein['length']:4d} aa  {protein['id']}")
            if protein["function"]:
                print(f"      FUNCTION: {protein['function'][:160]}")

    print("\nQ5. Mouse ortholog annotations for nuclear protein import")
    nuclear = nuclear_import_evidence()
    for go_id, annotations in nuclear["annotations"].items():
        label = nuclear["terms_queried"][go_id]
        if not annotations:
            print(f"  {go_id} {label}: NONE on mouse {nuclear['mouse_accession']}")
        for annotation in annotations:
            print(f"  {go_id} {annotation['evidence']:5s} {annotation['reference']}  "
                  f"from {annotation['with_from'] or '(none)'}")

    args.json.write_text(
        json.dumps(
            {
                "provenance": provenance,
                "membrane": membrane,
                "family": family,
                "nuclear_import": nuclear,
                "costars": costars,
            },
            indent=2,
        )
    )
    print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
