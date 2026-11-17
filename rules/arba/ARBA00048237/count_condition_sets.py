"""Count UniProtKB matches for each ARBA00048237 condition set, by lineage.

Each condition set is queried as a conjunction (all signatures plus its taxon),
then split by lineage and by whether the entry is reviewed. Reviewed matches are
listed with their EC numbers and protein names so the in-sample support can be
read directly. Writes counts.json next to this script and prints a summary.

PTHR10982 has a single subfamily, SF21, in the PANTHER release UniProtKB uses,
so ``xref:"panther-PTHR10982:SF21"`` and ``xref:panther-PTHR10982`` return the
same entries; an unknown subfamily id returns none, so the set 2 query does
filter at subfamily level.

Usage: python count_condition_sets.py
"""

from __future__ import annotations

import csv
import io
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://rest.uniprot.org/uniprotkb/search"

SETS: dict[int, list[str]] = {
    1: ["xref:interpro-IPR004568", "xref:interpro-IPR008278", "xref:interpro-IPR016039"],
    2: ["xref:interpro-IPR050830", 'xref:"panther-PTHR10982:SF21"', "taxonomy_id:147545"],
    3: ["xref:interpro-IPR001227", "xref:interpro-IPR002539", "xref:interpro-IPR016452"],
    4: ['xref:"funfam-3.20.20.70:FF:000078"', "taxonomy_id:4890"],
    5: ['xref:"funfam-3.90.470.20:FF:000005"', "taxonomy_id:2759"],
    6: ['xref:"funfam-3.90.25.70:FF:000001"', "taxonomy_id:147545"],
    7: ['xref:"funfam-3.40.366.10:FF:000007"'],
    8: ['xref:"funfam-3.40.50.720:FF:001423"', "taxonomy_id:5042"],
}

LINEAGES = {
    "Fungi": "taxonomy_id:4751",
    "Bacteria": "taxonomy_id:2",
    "Archaea": "taxonomy_id:2157",
    "Eukaryota_not_Fungi": "(taxonomy_id:2759 NOT taxonomy_id:4751)",
}


def get(params: dict[str, str]) -> tuple[dict, dict[str, str]]:
    """GET the search endpoint and return (json, headers)."""
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r), dict(r.headers)
        except Exception as exc:  # network: retry with backoff
            if attempt == 3:
                raise
            print(f"retry {url}: {exc}", file=sys.stderr)
            time.sleep(2**attempt)
    raise RuntimeError("unreachable")


def count(query: str) -> int:
    """Number of UniProtKB entries matching ``query``."""
    _, headers = get({"query": query, "size": "0"})
    return int(headers.get("X-Total-Results") or headers.get("x-total-results") or 0)


def reviewed(query: str) -> list[dict]:
    """Reviewed matches with accession, organism, name and EC numbers."""
    data, _ = get(
        {
            "query": f"({query}) AND reviewed:true",
            "fields": "accession,protein_name,organism_name,ec,lineage",
            "format": "json",
            "size": "50",
        }
    )
    out = []
    for e in data.get("results", []):
        desc = e.get("proteinDescription", {})
        rec = desc.get("recommendedName", {})
        name = rec.get("fullName", {}).get("value", "")
        ecs = [x["value"] for x in rec.get("ecNumbers", [])]
        for c in desc.get("contains", []) or []:
            ecs += [x["value"] for x in c.get("recommendedName", {}).get("ecNumbers", [])]
        lineage = [t.get("scientificName") for t in e.get("lineages", [])]
        out.append(
            {
                "accession": e["primaryAccession"],
                "organism": e.get("organism", {}).get("scientificName", ""),
                "kingdom": lineage[0] if lineage else "",
                "name": name,
                "ec": ecs,
            }
        )
    return out


def main() -> None:
    """Query every set and write counts.json."""
    release = None
    results = {}
    for n, conds in SETS.items():
        q = " AND ".join(conds)
        _, headers = get({"query": q, "size": "0"})
        release = headers.get("X-UniProt-Release") or headers.get("x-uniprot-release") or release
        row = {"query": q, "total": count(q)}
        row["by_lineage"] = {k: count(f"({q}) AND {v}") for k, v in LINEAGES.items()}
        row["with_ec_2.3.1.86"] = count(f"({q}) AND ec:2.3.1.86")
        row["reviewed"] = reviewed(q)
        results[n] = row
        print(f"set {n}: {row['total']} total; {row['by_lineage']}; "
              f"EC 2.3.1.86 now on {row['with_ec_2.3.1.86']}; reviewed {len(row['reviewed'])}")
        for r in row["reviewed"]:
            print(f"    {r['accession']} {r['organism']} | {r['name']} | {r['ec']}")
    union = " OR ".join("(" + " AND ".join(c) + ")" for c in SETS.values())
    union_row = {"total": count(union), "by_lineage": {k: count(f"({union}) AND {v}") for k, v in LINEAGES.items()}}
    print(f"union: {union_row}")
    nf_q = f"({union}) AND {LINEAGES['Eukaryota_not_Fungi']}"
    url = "https://rest.uniprot.org/uniprotkb/stream?" + urllib.parse.urlencode(
        {"query": nf_q, "format": "tsv", "fields": "accession,protein_name,organism_name,lineage,xref_panther,length"}
    )
    with urllib.request.urlopen(url, timeout=120) as r:
        tsv = r.read().decode()
    non_fungal = []
    for rec in csv.DictReader(io.StringIO(tsv), delimiter="\t"):
        lin = [t.split(" (")[0] for t in rec["Taxonomic lineage"].split(", ")]
        rec["lineage"] = " > ".join(lin[2:4])
        non_fungal.append({k: rec[k] for k in ("Entry", "Organism", "lineage", "Protein names", "PANTHER", "Length")})
    out = {"uniprot_release": release, "retrieved": time.strftime("%Y-%m-%d"), "sets": results, "union": union_row, "non_fungal": non_fungal}
    Path(__file__).with_name("counts.json").write_text(json.dumps(out, indent=1) + "\n")
    print("release:", release)
    write_results(out)


def write_results(out: dict) -> None:
    """Write the per-set table to RESULTS-condition-sets.md."""
    lines = [
        "# ARBA00048237 condition-set matches",
        "",
        f"UniProtKB release {out['uniprot_release']}, retrieved {out['retrieved']}, "
        "by `count_condition_sets.py`. Each set is queried as a conjunction.",
        "",
        "| Set | Matches | Fungi | Bacteria | Archaea | Other eukaryotes | Reviewed matches |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for n, row in out["sets"].items():
        b = row["by_lineage"]
        rev = ", ".join(r["accession"] for r in row["reviewed"])
        lines.append(
            f"| {n} | {row['total']} | {b['Fungi']} | {b['Bacteria']} | {b['Archaea']} "
            f"| {b['Eukaryota_not_Fungi']} | {rev} |"
        )
    u = out["union"]
    b = u["by_lineage"]
    lines.append(
        f"| any | {u['total']} | {b['Fungi']} | {b['Bacteria']} | {b['Archaea']} | {b['Eukaryota_not_Fungi']} | |"
    )
    lines += ["", "Reviewed matches and their EC numbers:", ""]
    seen = set()
    for row in out["sets"].values():
        for r in row["reviewed"]:
            if r["accession"] in seen:
                continue
            seen.add(r["accession"])
            lines.append(f"- {r['accession']} {r['organism']}: {r['name']} (EC {', '.join(r['ec'])})")
    lines += ["", "Matches outside Fungi (any set):", "",
              "| Accession | Organism | Lineage | Protein name | PANTHER | Length |", "|---|---|---|---|---|---:|"]
    for r in out.get("non_fungal", []):
        lines.append(f"| {r['Entry']} | {r['Organism']} | {r['lineage']} | {r['Protein names'][:70]} "
                     f"| {r['PANTHER'].split(';')[0]} | {r['Length']} |")
    Path(__file__).with_name("RESULTS-condition-sets.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
