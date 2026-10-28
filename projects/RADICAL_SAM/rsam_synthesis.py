"""Superfamily-level synthesis for the RADICAL_SAM project (Phase 4).

Computes, from the reviews themselves, the facts the project page's Synthesis
section cites: per-gene core molecular functions, whether each is an existing GO
term or a proposed one, the treatment-rule outcomes on the domain-derived generic
rows (including deviations from the rule), SAM-binding coverage, upstream
defects, and the IBA rows whose node placement was argued.

No *result* is hardcoded: the gene list and the organism directories come from the
project page's frontmatter, and every count is derived from
genes/<org>/<gene>/<gene>-ai-review.yaml. The project's own editorial choices are
encoded here deliberately and are the only constants: RULE (the treatment rule) and
the asserted values that count as PflB-substrate pushes.

A gene counts as REVIEWED when it has annotation rows and none of them is still
`PENDING`. That deliberately does not consult `status:`, which can go stale
(MOCS1 is fully reviewed but still reads `INITIALIZED`); status mismatches are
reported separately under `data_quality`.

Editing any of the 29 gene reviews changes these figures, so re-run this script
and commit the regenerated data/synthesis.yaml in the same change; CI fails until
you do (tests/test_radical_sam_synthesis.py).

Run from the repository root:
    uv run python projects/RADICAL_SAM/rsam_synthesis.py
    uv run python projects/RADICAL_SAM/rsam_synthesis.py --check   # CI: fail if stale

Writes projects/RADICAL_SAM/data/synthesis.yaml and prints a short report.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "projects" / "RADICAL_SAM.md"
DEST = Path(__file__).resolve().parent / "data" / "synthesis.yaml"

SAM_BINDING = "GO:1904047"
FE4S4 = "GO:0051539"

# The rows the project's treatment rule governs, and what the rule expects.
# "refine" => MODIFY to the specific term; "accept" => ACCEPT.
# `no_catalysis_alt` is the action the rule's second branch permits for a member
# whose catalysis is not established. It is set only on the two rows the rule names
# that branch for: GO:0003824 (no reaction known, so it cannot be refined to one) and
# GO:0051539 (the cluster is present but not shown to be catalytic). The other four
# rows have no such branch -- refining `iron-sulfur cluster binding` to the 4Fe-4S
# term, or accepting a SAM-binding row, does not depend on catalysis being proven --
# so their alt is None and any non-primary action there is a deviation.
RULE = {
    "GO:0003824": ("catalytic activity", "refine", "KEEP_AS_NON_CORE"),
    "GO:0051536": ("iron-sulfur cluster binding", "refine", None),
    "GO:0046872": ("metal ion binding", "refine", None),
    "GO:0005506": ("iron ion binding", "refine", None),
    FE4S4: ("4 iron, 4 sulfur cluster binding", "accept", "KEEP_AS_NON_CORE"),
    SAM_BINDING: ("S-adenosyl-L-methionine binding", "accept_or_new", None),
}
EXPECTED = {"refine": {"MODIFY"}, "accept": {"ACCEPT"}, "accept_or_new": {"ACCEPT", "NEW"}}

# Evidence codes that mean the row was propagated to this gene rather than asserted
# about it: electronic signature/EC mappings, PAINT phylogenetic inference, and
# homology transfer. Used to classify REMOVE rows by how they arose.
PROPAGATED_EVIDENCE = {"IEA", "IBA", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA"}


def frontmatter() -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", PAGE.read_text(), re.S)
    if not m:
        sys.exit(f"no frontmatter in {PAGE}")
    return yaml.safe_load(m.group(1))


def load(symbol: str, orgs: list[str]):
    for org in orgs:
        p = ROOT / "genes" / org / symbol / f"{symbol}-ai-review.yaml"
        if p.exists():
            return org, yaml.safe_load(p.read_text())
    return None, None


def core_function_terms(review: dict) -> list[dict]:
    """Molecular functions a review asserts as core, existing or proposed.

    Covers `contributes_to_molecular_function` as well, so a subunit that
    contributes to a complex activity is not dropped from both buckets.
    """
    out = []
    for cf in review.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            mf = cf.get(slot)
            if mf and mf.get("id"):
                out.append({"kind": "GO", "id": mf["id"], "label": mf.get("label"),
                            "slot": slot})
        if cf.get("proposed_molecular_function"):
            out.append({"kind": "PROPOSED", "name": cf["proposed_molecular_function"]})
    return out


def build() -> dict:
    fm = frontmatter()
    symbols = fm["genes"]
    orgs = list(fm.get("species") or ["human"])

    genes: dict[str, dict] = {}
    missing: list[str] = []
    status_mismatch: list[dict] = []

    actions = Counter()                   # reviewed genes only
    generic = defaultdict(Counter)        # term -> action -> n (reviewed genes only)
    deviations: list[dict] = []
    rule_branch: list[dict] = []
    proposed_terms: list[dict] = []
    defects: list[dict] = []
    argued_ibas: list[dict] = []

    for sym in symbols:
        org, review = load(sym, orgs)
        if review is None:
            missing.append(sym)
            continue

        rows = review.get("existing_annotations") or []
        pending = sum(1 for a in rows if ((a.get("review") or {}).get("action")) == "PENDING")
        reviewed = bool(rows) and pending == 0
        sam_actions = sorted({
            (a.get("review") or {}).get("action")
            for a in rows if (a.get("term") or {}).get("id") == SAM_BINDING
        } - {None})
        # Only an affirmative SAM row counts: a REMOVE or UNDECIDED on GO:1904047
        # would otherwise read as "catalysis established" and silently flip a gene
        # into the wrong branch of the treatment rule.
        catalysis_established = bool({"ACCEPT", "NEW"} & set(sam_actions))

        per_gene = Counter()
        for a in rows:
            r = a.get("review") or {}
            act = r.get("action")
            tid = (a.get("term") or {}).get("id")
            if act:
                per_gene[act] += 1
                if reviewed:
                    actions[act] += 1
                    if tid in RULE:
                        generic[tid][act] += 1
                        _, mode, alt = RULE[tid]
                        if act not in EXPECTED[mode]:
                            entry = {"gene": sym, "organism": org, "term": tid,
                                     "label": RULE[tid][0], "action": act,
                                     "expected": sorted(EXPECTED[mode])}
                            if alt and act == alt and not catalysis_established:
                                entry["note"] = "rule branch: catalysis not established"
                                rule_branch.append(entry)
                            else:
                                deviations.append(entry)

            for d in r.get("source_defects") or []:
                defects.append({
                    "gene": sym, "organism": org,
                    "defect_type": d.get("defect_type"), "resource": d.get("resource"),
                    "record": d.get("record"), "requested_change": d.get("requested_change"),
                    "asserted_value": d.get("asserted_value"),
                    "corrected_value": d.get("corrected_value"),
                    "confidence": d.get("confidence"),
                })

            pr = r.get("propagation_review")
            if pr and a.get("evidence_type") == "IBA":
                argued_ibas.append({
                    "gene": sym, "organism": org, "term": tid,
                    "label": (a.get("term") or {}).get("label"), "action": act,
                    "root_cause": pr.get("root_cause"),
                    "failure_modes": pr.get("failure_modes") or [],
                    "sources": [{"id": s.get("source_id"), "status": s.get("source_status")}
                                for s in (pr.get("source_entities") or [])],
                })

        for pt in review.get("proposed_new_terms") or []:
            proposed_terms.append({"gene": sym, "organism": org,
                                   "proposed_name": pt.get("proposed_name")})

        cfs = core_function_terms(review)
        declared = review.get("status")
        if reviewed and declared != "COMPLETE":
            status_mismatch.append({"gene": sym, "declared": declared,
                                    "rows": len(rows), "pending": 0})
        genes[sym] = {
            "organism": org, "uniprot": review.get("id"), "declared_status": declared,
            "reviewed": reviewed, "n_rows": len(rows), "pending_rows": pending,
            "actions": dict(sorted(per_gene.items())),
            "core_functions": cfs,
            "n_core_proposed": sum(1 for c in cfs if c["kind"] == "PROPOSED"),
            "sam_binding_actions": sam_actions or None,
            "catalysis_established": catalysis_established,
            "_remove_terms": [
                ((a.get("term") or {}).get("id"), a.get("evidence_type")) for a in rows
                if ((a.get("review") or {}).get("action")) == "REMOVE"
            ],
        }

    rev = {k: v for k, v in genes.items() if v["reviewed"]}
    unrev = {k: v for k, v in genes.items() if not v["reviewed"]}

    core_go = Counter()
    for v in rev.values():
        for c in v["core_functions"]:
            if c["kind"] == "GO":
                core_go[c["id"]] += 1

    # Partition only over REVIEWED genes: an unreviewed gene has no SAM row because
    # nobody has reviewed it yet, which says nothing about whether its catalysis is
    # established. lipA is lipoyl synthase and would otherwise land in the wrong bucket.
    sam_new = sorted(k for k, v in rev.items() if v["sam_binding_actions"] == ["NEW"])
    sam_in_goa = sorted(k for k, v in rev.items()
                        if v["sam_binding_actions"] and "ACCEPT" in v["sam_binding_actions"])
    sam_absent = sorted(k for k, v in rev.items() if not v["sam_binding_actions"])
    sam_not_reviewed = sorted(k for k, v in genes.items() if not v["reviewed"])

    # What the REMOVE rows actually are, so the page need not assert it.
    # Classified by HOW THE ROW AROSE (its evidence code), not by which term it
    # carries: a term-keyed bucket silently files an experimental row as a mapping
    # error, which is a different claim about a different kind of mistake.
    removes = Counter()
    removes_by_evidence = Counter()
    for sym, v in rev.items():
        for t, ev in v["_remove_terms"]:
            if t == "GO:0005515":
                removes["uninformative_protein_binding"] += 1
            elif ev in PROPAGATED_EVIDENCE:
                removes["propagated_mapping_or_inference"] += 1
                removes_by_evidence[ev] += 1
            else:
                # An asserted row (experimental, or an author/curator statement)
                # withdrawn on the biology rather than on how it propagated.
                removes["asserted_row_rejected_on_biology"] += 1
                removes_by_evidence[ev] += 1

    interpro = [d for d in defects if str(d["record"]).startswith("InterPro")]
    # Defects whose asserted value pushes PflB/formate-C-acetyltransferase
    # specificity onto a protein whose partner GRE is not PflB.
    substrate_push = [d for d in defects
                      if d["asserted_value"] in {"RHEA:19225", "EC:1.97.1.4", "GO:0043365"}]

    return {
        "generated_by": "projects/RADICAL_SAM/rsam_synthesis.py",
        "definitions": {
            "reviewed": "gene has annotation rows and none is PENDING (ignores stale status:)",
            "catalysis_established": f"gene carries a {SAM_BINDING} row, per the project's treatment rule",
        },
        "totals": {
            "genes_in_scope": len(symbols),
            "resolved": len(genes),
            "missing_folder": missing,
            "reviewed": len(rev),
            "not_reviewed": {k: {"declared_status": v["declared_status"],
                                 "pending_rows": v["pending_rows"]} for k, v in unrev.items()},
            "annotation_rows_in_reviewed_genes": sum(v["n_rows"] for v in rev.values()),
        },
        "data_quality": {"reviewed_but_status_not_COMPLETE": status_mismatch},
        "actions_in_reviewed_genes": dict(sorted(actions.items())),
        "generic_row_treatment": {
            t: {"label": RULE[t][0], "actions": dict(sorted(c.items()))}
            for t, c in sorted(generic.items())
        },
        "treatment_rule_deviations": deviations,
        "treatment_rule_branch_uses": rule_branch,
        "sam_binding": {
            "scope": "reviewed genes only",
            "new_rows_absent_from_goa": sam_new,
            "already_in_goa": sam_in_goa,
            "absent_catalysis_not_established": sam_absent,
            "not_reviewed_so_not_classified": sam_not_reviewed,
        },
        "core_function_go_terms": dict(core_go.most_common()),
        "genes_whose_core_activity_has_no_go_term": sorted(
            k for k, v in rev.items() if v["n_core_proposed"] > 0),
        "genes_with_no_core_function": sorted(k for k, v in rev.items() if not v["core_functions"]),
        "proposed_new_terms": proposed_terms,
        "source_defects": defects,
        "remove_breakdown": dict(removes),
        "remove_non_protein_binding_by_evidence": dict(sorted(removes_by_evidence.items())),
        "source_defect_summary": {
            "total": len(defects),
            "by_resource": dict(sorted(Counter(d["resource"] for d in defects).items())),
            "interpro_defects": len(interpro),
            "distinct_interpro_entries": sorted({d["record"] for d in interpro}),
            "pflb_substrate_pushes": [f"{d['gene']}:{d['asserted_value']}" for d in substrate_push],
        },
        "ibas_whose_node_placement_was_argued": argued_ibas,
        "iba_root_causes": dict(sorted(Counter(
            i["root_cause"] for i in argued_ibas).items())),
        "genes": {k: {kk: vv for kk, vv in v.items() if not kk.startswith("_")}
                  for k, v in genes.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if data/synthesis.yaml is stale")
    args = ap.parse_args()

    out = build()
    text = yaml.safe_dump(out, sort_keys=False, allow_unicode=True)

    if args.check:
        if not DEST.exists():
            print(f"MISSING {DEST.relative_to(ROOT)} — run without --check", file=sys.stderr)
            return 1
        if DEST.read_text() != text:
            print(f"STALE {DEST.relative_to(ROOT)} — re-run without --check", file=sys.stderr)
            return 1
        print(f"{DEST.relative_to(ROOT)} is up to date")
        return 0

    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(text)

    t = out["totals"]
    print(f"in scope {t['genes_in_scope']}  resolved {t['resolved']}  reviewed {t['reviewed']}  "
          f"rows in reviewed genes {t['annotation_rows_in_reviewed_genes']}")
    if t["missing_folder"]:
        print("  MISSING FOLDERS:", t["missing_folder"])
    if t["not_reviewed"]:
        print("  not reviewed:", t["not_reviewed"])
    for m in out["data_quality"]["reviewed_but_status_not_COMPLETE"]:
        print(f"  DATA QUALITY: {m['gene']} reviewed but status={m['declared']}")
    a = out["actions_in_reviewed_genes"]
    print("actions:", a, "sum:", sum(a.values()))
    print("\ngeneric rows:")
    for term, info in out["generic_row_treatment"].items():
        print(f"  {term} {info['label']:<34} {info['actions']}")
    print(f"\ntreatment-rule DEVIATIONS: {len(out['treatment_rule_deviations'])}")
    for d in out["treatment_rule_deviations"]:
        print(f"  {d['gene']:<8} {d['term']} {d['action']} (expected {'/'.join(d['expected'])})")
    print(f"rule-branch uses (catalysis not established): {len(out['treatment_rule_branch_uses'])}")
    s = out["sam_binding"]
    print(f"\nSAM: NEW {len(s['new_rows_absent_from_goa'])}  "
          f"in GOA {len(s['already_in_goa'])} {s['already_in_goa']}  "
          f"absent {len(s['absent_catalysis_not_established'])}")
    print("IBA root causes:", out["iba_root_causes"],
          "total:", sum(out["iba_root_causes"].values()))
    sd = out["source_defect_summary"]
    print(f"defects {sd['total']} by resource {sd['by_resource']}; "
          f"InterPro {sd['interpro_defects']} on {len(sd['distinct_interpro_entries'])} entries; "
          f"PflB substrate pushes {len(sd['pflb_substrate_pushes'])}")
    print(f"\nwrote {DEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
