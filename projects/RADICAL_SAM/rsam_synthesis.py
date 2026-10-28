"""Superfamily-level synthesis for the RADICAL_SAM project (Phase 4).

Computes, from the reviews themselves, the facts the project page's Phase 4
summary cites: per-gene core molecular functions, whether each is an existing GO
term or a proposed one, the treatment-rule outcomes on the domain-derived generic
rows, SAM-binding coverage, upstream defects, and the IBA rows whose node
placement was argued.

Nothing is hardcoded: the gene list comes from the project page's frontmatter and
every number is derived from genes/<org>/<gene>/<gene>-ai-review.yaml.

Run from the repository root:
    uv run python projects/RADICAL_SAM/rsam_synthesis.py
Writes projects/RADICAL_SAM/data/synthesis.yaml and prints a short report.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "projects" / "RADICAL_SAM.md"
ORGS = ("human", "ECOLI")

# The rows the project's treatment rule governs.
GENERIC_ROWS = {
    "GO:0003824": "catalytic activity",
    "GO:0051536": "iron-sulfur cluster binding",
    "GO:0051539": "4 iron, 4 sulfur cluster binding",
    "GO:0046872": "metal ion binding",
    "GO:0005506": "iron ion binding",
    "GO:1904047": "S-adenosyl-L-methionine binding",
}
SAM_BINDING = "GO:1904047"


def genes_from_page() -> list[str]:
    """Read the project page frontmatter's `genes:` list."""
    text = PAGE.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"no frontmatter in {PAGE}")
    return yaml.safe_load(m.group(1))["genes"]


def load(symbol: str):
    for org in ORGS:
        p = ROOT / "genes" / org / symbol / f"{symbol}-ai-review.yaml"
        if p.exists():
            return org, p, yaml.safe_load(p.read_text())
    return None, None, None


def core_function_terms(review: dict) -> list[dict]:
    """Molecular functions a review asserts as core, existing or proposed."""
    out = []
    for cf in review.get("core_functions") or []:
        mf = cf.get("molecular_function")
        if mf and mf.get("id"):
            out.append({"kind": "GO", "id": mf["id"], "label": mf.get("label")})
        elif cf.get("proposed_molecular_function"):
            out.append({"kind": "PROPOSED", "name": cf["proposed_molecular_function"]})
    return out


def main() -> int:
    symbols = genes_from_page()
    genes: dict[str, dict] = {}
    missing: list[str] = []

    actions = Counter()
    generic = defaultdict(Counter)        # term -> action -> n
    proposed_terms: list[dict] = []
    defects: list[dict] = []
    argued_ibas: list[dict] = []
    sam_status: dict[str, str] = {}

    for sym in symbols:
        org, path, review = load(sym)
        if review is None:
            missing.append(sym)
            continue

        rows = review.get("existing_annotations") or []
        per_gene_actions = Counter()
        sam_seen = None

        for a in rows:
            r = a.get("review") or {}
            act = r.get("action")
            if act:
                actions[act] += 1
                per_gene_actions[act] += 1
            tid = (a.get("term") or {}).get("id")
            if tid in GENERIC_ROWS and act:
                generic[tid][act] += 1
            if tid == SAM_BINDING and act:
                # NEW means we added it; anything else means GOA already had it.
                sam_seen = "added_as_NEW" if act == "NEW" else f"already_in_GOA ({act})"

            for d in r.get("source_defects") or []:
                defects.append({
                    "gene": sym, "organism": org,
                    "defect_type": d.get("defect_type"),
                    "resource": d.get("resource"),
                    "record": d.get("record"),
                    "requested_change": d.get("requested_change"),
                    "asserted_value": d.get("asserted_value"),
                    "corrected_value": d.get("corrected_value"),
                    "confidence": d.get("confidence"),
                })

            pr = r.get("propagation_review")
            if pr and a.get("evidence_type") == "IBA":
                argued_ibas.append({
                    "gene": sym, "organism": org,
                    "term": tid, "label": (a.get("term") or {}).get("label"),
                    "action": act,
                    "root_cause": pr.get("root_cause"),
                    "failure_modes": pr.get("failure_modes") or [],
                    "sources": [
                        {"id": s.get("source_id") or s.get("source"),
                         "status": s.get("source_status")}
                        for s in (pr.get("source_entities") or [])
                    ],
                })

        for pt in review.get("proposed_new_terms") or []:
            proposed_terms.append({
                "gene": sym, "organism": org,
                "proposed_name": pt.get("proposed_name"),
                "justification_head": (pt.get("justification") or "").split(".")[0][:200] or None,
            })

        cfs = core_function_terms(review)
        genes[sym] = {
            "organism": org,
            "uniprot": review.get("id"),
            "status": review.get("status"),
            "n_rows": len(rows),
            "actions": dict(sorted(per_gene_actions.items())),
            "core_functions": cfs,
            "n_core_proposed": sum(1 for c in cfs if c["kind"] == "PROPOSED"),
            "sam_binding": sam_seen or "absent",
            "pending_rows": sum(
                1 for a in rows if ((a.get("review") or {}).get("action")) == "PENDING"
            ),
        }
        sam_status[sym] = genes[sym]["sam_binding"]

    reviewed = {k: v for k, v in genes.items() if v["status"] == "COMPLETE"}
    unreviewed = {k: v for k, v in genes.items() if v["status"] != "COMPLETE"}

    # Which core activities rest on a term GO does not have.
    genes_with_proposed_core = sorted(
        k for k, v in reviewed.items() if v["n_core_proposed"] > 0
    )
    core_go_ids = Counter()
    for v in reviewed.values():
        for c in v["core_functions"]:
            if c["kind"] == "GO":
                core_go_ids[c["id"]] += 1

    out = {
        "generated_by": "projects/RADICAL_SAM/rsam_synthesis.py",
        "totals": {
            "genes_in_scope": len(symbols),
            "resolved": len(genes),
            "missing_folder": missing,
            "reviewed_complete": len(reviewed),
            "not_complete": {k: v["status"] for k, v in unreviewed.items()},
            "annotation_rows_reviewed": sum(v["n_rows"] for v in reviewed.values()),
        },
        "actions_across_reviewed": dict(sorted(actions.items())),
        "generic_row_treatment": {
            t: {"label": GENERIC_ROWS[t], "actions": dict(sorted(c.items()))}
            for t, c in sorted(generic.items())
        },
        "sam_binding_coverage": dict(sorted(sam_status.items())),
        "core_function_go_terms": dict(core_go_ids.most_common()),
        "genes_whose_core_activity_has_no_go_term": genes_with_proposed_core,
        "proposed_new_terms": proposed_terms,
        "source_defects": defects,
        "ibas_whose_node_placement_was_argued": argued_ibas,
        "genes": genes,
    }

    dest = Path(__file__).resolve().parent / "data" / "synthesis.yaml"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(yaml.safe_dump(out, sort_keys=False, allow_unicode=True))

    t = out["totals"]
    print(f"genes in scope: {t['genes_in_scope']}  resolved: {t['resolved']}  "
          f"complete: {t['reviewed_complete']}")
    if t["missing_folder"]:
        print("  MISSING FOLDERS:", t["missing_folder"])
    if t["not_complete"]:
        print("  not COMPLETE:", t["not_complete"])
    print(f"annotation rows reviewed: {t['annotation_rows_reviewed']}")
    print("actions:", out["actions_across_reviewed"])
    print("\ngeneric rows:")
    for term, info in out["generic_row_treatment"].items():
        print(f"  {term} {info['label']:<34} {info['actions']}")
    print("\nSAM binding:", Counter(sam_status.values()))
    print(f"proposed new terms: {len(proposed_terms)} "
          f"(genes: {[p['gene'] for p in proposed_terms]})")
    print(f"source defects: {len(defects)}")
    print(f"argued IBAs: {len(argued_ibas)}")
    print(f"\nwrote {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
