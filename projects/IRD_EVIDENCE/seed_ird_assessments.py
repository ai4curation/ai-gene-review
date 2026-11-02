"""Write pre-filled, not-yet-adjudicated node assessments for contested IRD rows.

For every IRD row that experimental annotations contradict inside its effective block
(``ird_experimental_conflicts.tsv``, from ``analyze_ird.py``), this writes one entry
shaped like a FamilyReview ``node_assessment``. The entry is pre-filled with the node,
blocked term, ``evidence: IRD``, ``negated: true``, the ancestral node in ``seeds``,
node taxon and PAINT snapshot, plus the conflicting experimental annotations and any
experimental NOTs that support the loss. Only the verdict and reason are left for a
reviewer: copy the entry into ``interpro/panther/<FAM>/<FAM>-review.yaml`` and set
``assessment`` (LOSS_SUPPORTED / LOSS_CONTRADICTED / LOSS_TOO_BROAD / LOSS_STALE /
UNRESOLVED) and ``assessment_reason``.

Inputs:  ird_nodes.tsv, ird_clade_members.tsv.gz, ird_experimental_conflicts.tsv
Output:  ird_seed_assessments.yaml  (committed curation worklist)

Usage:
    uv run python projects/IRD_EVIDENCE/seed_ird_assessments.py
"""

from __future__ import annotations

import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

import requests
import yaml

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
NODES = HERE / "ird_nodes.tsv"
MEMBERS = HERE / "ird_clade_members.tsv.gz"
CONFLICTS = HERE / "ird_experimental_conflicts.tsv"
OUT = HERE / "ird_seed_assessments.yaml"
HTP = {"HTP", "HDA", "HMP", "HGI", "HEP"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def taxon_labels(ids: set[str]) -> dict[str, str]:
    """NCBI taxon id -> scientific name, from the UniProt taxonomy API."""
    labels: dict[str, str] = {}
    for tid in sorted(ids):
        r = requests.get(f"https://rest.uniprot.org/taxonomy/{tid}", timeout=60)
        if r.status_code == 200:
            labels[tid] = r.json().get("scientificName", "")
    return labels


def main() -> int:
    ird = {(r["ird_node"], r["go_id"]): r for r in read_tsv(NODES)}
    clade_size: dict[tuple[str, str], int] = defaultdict(int)
    for m in read_tsv(MEMBERS):
        clade_size[(m["ird_node"], m["go_id"])] += 1
    conflicts = [c for c in read_tsv(CONFLICTS) if c["paint_reannotated_below"] == "false"]
    by_row: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for c in conflicts:
        by_row[(c["ird_node"], c["blocked_go_id"])].append(c)

    reviewed = {p.parent.name for p in ROOT.glob("interpro/panther/*/PTHR*-review.yaml")}
    existing: dict[tuple[str, str], str] = {}
    for p in ROOT.glob("interpro/panther/*/PTHR*-review.yaml"):
        for a in (yaml.safe_load(p.read_text()) or {}).get("node_assessments") or []:
            node = str(a.get("node_id", "")).split(":")[-1]
            existing[(node, (a.get("asserted_term") or {}).get("id", ""))] = a.get("assessment", "")
    with_paint = {p.parent.name for p in ROOT.glob("interpro/panther/*/PTHR*-paint.tsv")}
    taxa = {ird[k]["taxon"].split(":")[-1] for k in by_row if ird[k]["taxon"].split(":")[-1]}
    tax_label = taxon_labels(taxa)

    entries = []
    for key, rows in by_row.items():
        r = ird[key]
        lt_proteins = {c["uniprot"] for c in rows if c["evidence"] not in HTP}
        tid = r["taxon"].split(":")[-1]
        assessment = {
            "node_id": f"PANTHER:{r['ird_node']}",
            "asserted_term": {"id": r["go_id"], "label": r["go_label"]},
            "evidence": "IRD",
            "negated": True,
            "seeds": [{"id": f"PANTHER:{r['ancestral_node']}",
                       "label": f"{r['ancestral_node']} (ancestral IBD node; IRD source)"}],
            "paint_snapshot": r["date"],
        }
        if tid:
            assessment["node_taxon"] = {"id": f"NCBITaxon:{tid}", "label": tax_label.get(tid, "")}
        evidence = [
            {
                "protein": f"UniProtKB:{c['uniprot']}",
                "symbol": c["symbol"],
                "organism": c["organism"],
                "annotation": f"{c['qualifier']} {c['exp_go_id']} {c['exp_label']}",
                "evidence": c["evidence"],
                "reference": c["reference"],
                "assigned_by": c["assigned_by"],
            }
            for c in sorted(rows, key=lambda c: (c["evidence"] in HTP, c["organism"], c["symbol"], c["exp_go_id"]))
        ]
        entries.append({
            "family": f"PANTHER:{r['family']}",
            "family_has_review": r["family"] in reviewed,
            "family_has_paint_tsv": r["family"] in with_paint,
            "existing_verdict": existing.get(key),
            "clade_size": clade_size[key],
            "proteins_with_low_throughput_positive": len(lt_proteins),
            "conflicting_experimental_annotations": evidence,
            "node_assessment": assessment,
        })
    entries.sort(key=lambda e: (-e["proteins_with_low_throughput_positive"], e["family"], e["node_assessment"]["node_id"]))
    header = (
        "# Pre-filled IRD node assessments awaiting a verdict. Generated by\n"
        "# seed_ird_assessments.py; regenerate rather than hand-edit. To adjudicate one, copy\n"
        "# its node_assessment into the family review and add assessment + assessment_reason.\n"
    )
    OUT.write_text(header + yaml.safe_dump({"seeds": entries}, sort_keys=False, allow_unicode=True, width=100))
    print(f"wrote {len(entries)} seeded IRD assessments to {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
