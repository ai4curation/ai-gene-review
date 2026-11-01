"""Check each Wei et al. 2020 example protein/term pair against current GOA.

Reads data/rar_supplement_cases.yaml (from parse_supplement.py) and, for every
(example protein, GO term) pair, records:

- the protein's organism and coarse taxon group (from its UniProt lineage);
  inactive or merged accessions are reported as such;
- whether current GOA (QuickGO API) still annotates the protein to that exact
  term, and with which evidence codes and WITH/FROM sources.

Nothing is judged here. A pair that is gone from GOA was either corrected or
dropped for another reason (e.g. a PAINT re-run, an accession change); a pair
that persists is a candidate for the per-case review in the project page.

Usage:
    uv run python projects/RAR_MISANNOTATION/scripts/check_current_goa.py
"""

import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "projects" / "RAR_MISANNOTATION" / "data"
CASES = DATA / "rar_supplement_cases.yaml"
OUT = DATA / "rar_current_status.yaml"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"

# Ordered so that the most specific matching lineage name wins.
GROUPS = [
    ("Vertebrata", "Vertebrates"),
    ("Metazoa", "Invertebrates"),
    ("Fungi", "Fungi"),
    ("Viridiplantae", "Plants"),
    ("Bacteria", "Bacteria"),
    ("Archaea", "Archaea"),
]


def get_json(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 ** (i + 1))


def uniprot_info(accessions):
    info = {}
    accs = sorted(accessions)
    for i in range(0, len(accs), 100):
        chunk = accs[i:i + 100]
        q = " OR ".join(f"accession:{a}" for a in chunk)
        url = UNIPROT + "?" + urllib.parse.urlencode({
            "query": q, "fields": "accession,organism_name,organism_id,lineage",
            "format": "json", "size": 500})
        for r in get_json(url).get("results", []):
            if "organism" not in r:
                reason = (r.get("inactiveReason") or {}).get("inactiveReasonType", "inactive")
                info[r["primaryAccession"]] = {"status": f"inactive ({reason.lower()})"}
                continue
            lineage = [t["scientificName"] for t in r.get("lineages", [])]
            group = next((g for name, g in GROUPS if name in lineage), "Other")
            info[r["primaryAccession"]] = {
                "organism": r["organism"]["scientificName"],
                "taxon_id": r["organism"]["taxonId"],
                "group": group,
                "status": "active",
            }
    return info


def goa_rows(accessions, go_id):
    rows = []
    page = 1
    while True:
        url = QUICKGO + "?" + urllib.parse.urlencode({
            "geneProductId": ",".join(accessions), "goId": go_id,
            "goUsage": "exact", "limit": 200, "page": page})
        d = get_json(url)
        rows.extend(d.get("results", []))
        if page >= d.get("pageInfo", {}).get("total", 1):
            return rows
        page += 1


def with_from(row):
    out = []
    for wf in row.get("withFrom") or []:
        for x in wf.get("connectedXrefs", []):
            out.append(f"{x['db']}:{x['id']}")
    return out


def main():
    cases = yaml.safe_load(CASES.read_text())["cases"]
    all_accs = {a for c in cases for a in c["example_proteins"]}
    info = uniprot_info(all_accs)
    results = []
    for c in cases:
        accs = c["example_proteins"]
        rows = goa_rows(accs, c["go_id"]) if accs else []
        by_acc = {}
        for r in rows:
            if r.get("qualifier", "").startswith("NOT"):
                continue
            acc = r["geneProductId"].split(":", 1)[1].split("-")[0]
            by_acc.setdefault(acc, []).append({
                "evidence": r["goEvidence"],
                "reference": r["reference"],
                "assigned_by": r["assignedBy"],
                "with_from": with_from(r),
            })
        pairs = []
        for a in accs:
            ui = info.get(a)
            pairs.append({
                "protein": a,
                "organism": ui.get("organism") if ui else None,
                "group": ui.get("group") if ui else None,
                "uniprot_status": ui["status"] if ui else "not_found",
                "current_goa": "present" if a in by_acc else "absent",
                "current_annotations": by_acc.get(a, []),
            })
        results.append({
            "table": c["table"], "release": c["release"], "go_id": c["go_id"],
            "go_label_in_paper": c["go_label_in_paper"],
            "most_frequent_evidence": c["most_frequent_evidence"],
            "pairs": pairs,
        })
    n = sum(len(r["pairs"]) for r in results)
    present = sum(p["current_goa"] == "present" for r in results for p in r["pairs"])
    OUT.write_text(yaml.safe_dump({
        "source": {
            "cases": "projects/RAR_MISANNOTATION/data/rar_supplement_cases.yaml",
            "generated_by": "projects/RAR_MISANNOTATION/scripts/check_current_goa.py",
            "checked_on": date.today().isoformat(),
            "goa_source": QUICKGO,
            "pairs_checked": n,
            "pairs_still_annotated": present,
        },
        "results": results,
    }, sort_keys=False, width=100))
    print(f"{present}/{n} example pairs still annotated -> {OUT}")


if __name__ == "__main__":
    main()
