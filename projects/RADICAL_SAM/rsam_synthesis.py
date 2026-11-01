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
`PENDING`. That deliberately does not consult `status:`, which can go stale: MOCS1
was fully reviewed while still reading `INITIALIZED`, which this script reported
under `data_quality` until Phase 3 corrected it. Status mismatches are still
reported there rather than being allowed to skew the counts.

The Phase 3 reviews -- the radical SAM genes that already existed when the project
started -- are kept OUT of these totals, because Phase 4 reports what this project
reviewed from scratch. They are still judged by the same treatment rule, through the
same code, under `phase3_rule_conformance`; their list lives in
data/phase3_scope.yaml.

Editing any of the 29 gene reviews, or any review named in data/phase3_scope.yaml,
changes these figures, so re-run this script and commit the regenerated
data/synthesis.yaml in the same change; CI fails until you do
(tests/test_radical_sam_synthesis.py).

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
PHASE3_SCOPE = Path(__file__).resolve().parent / "data" / "phase3_scope.yaml"
RULE_EXCEPTIONS = Path(__file__).resolve().parent / "data" / "rule_exceptions.yaml"

SAM_BINDING = "GO:1904047"
FE4S4 = "GO:0051539"

# The rows the project's treatment rule governs, and what the rule expects.
# "refine" => MODIFY to the specific term; "accept_or_new" => ACCEPT, or NEW where the
# term is absent from GOA.
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
    # accept_or_new, not accept: GOA does not always carry the 4Fe-4S row (PSEPK/bioB
    # has GO:0051537 but not GO:0051539), and a cofactor the rule calls core has to be
    # proposable where it is missing. Same reasoning as GO:1904047 below.
    FE4S4: ("4 iron, 4 sulfur cluster binding", "accept_or_new", "KEEP_AS_NON_CORE"),
    SAM_BINDING: ("S-adenosyl-L-methionine binding", "accept_or_new", None),
}
EXPECTED = {"refine": {"MODIFY"}, "accept_or_new": {"ACCEPT", "NEW"}}

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


def sam_actions_of(rows: list) -> list[str]:
    """Actions this review takes on GO:1904047, which is how the rule decides
    whether catalysis is established for the gene."""
    return sorted({(a.get("review") or {}).get("action")
                   for a in rows if (a.get("term") or {}).get("id") == SAM_BINDING} - {None})


def load_rule_exceptions() -> dict[tuple[str, str, str], dict]:
    """Documented exceptions to the treatment rule, keyed by (organism, gene, term).

    The rule table documents one branch its constant cannot express -- keep
    `GO:0046872` where the protein binds a separate mononuclear metal ion -- and the
    project's tests turn a deviation into a CI failure. Without a hatch, honouring
    that branch would mean editing a test, so the hatch lives in curated data
    instead (data/rule_exceptions.yaml), beside the scope file.
    """
    spec = yaml.safe_load(RULE_EXCEPTIONS.read_text()) or {}
    out: dict[tuple[str, str, str], dict] = {}
    for e in spec.get("exceptions") or []:
        org, _, sym = str(e["gene"]).partition("/")
        if not sym:
            sys.exit(f"rule_exceptions: {e['gene']!r} is not organism-qualified")
        actions = e["actions"]
        out[(org, sym, e["term"])] = {
            "actions": set(actions if isinstance(actions, list) else [actions]),
            "reason": e["reason"],
        }
    return out


def rule_check(sym: str, org: str, rows: list, catalysis_established: bool,
               exceptions: dict[tuple[str, str, str], dict] | None = None):
    """Apply the treatment rule to one review's domain-derived generic rows.

    Returns (generic_counts, deviations, branch_uses, exceptions_used). Shared by the
    Phase 4 scope and the Phase 3 scope so both are judged by exactly the same code:
    a rule that is only enforced where it was written is not a rule.

    A row named in *exceptions* with a matching action is recorded as a documented
    exception rather than a deviation. Callers report which entries were used, so an
    entry that matches nothing is visible as stale instead of quietly widening the
    rule.
    """
    exceptions = exceptions or {}
    generic: dict = defaultdict(Counter)
    deviations: list[dict] = []
    branch: list[dict] = []
    used: list[dict] = []
    for a in rows:
        r = a.get("review") or {}
        act = r.get("action")
        tid = (a.get("term") or {}).get("id")
        if not act or tid not in RULE:
            continue
        generic[tid][act] += 1
        label, mode, alt = RULE[tid]
        if act in EXPECTED[mode]:
            continue
        entry = {"gene": sym, "organism": org, "term": tid, "label": label,
                 "action": act, "expected": sorted(EXPECTED[mode])}
        allowed = exceptions.get((org, sym, tid))
        if allowed and act in allowed["actions"]:
            entry["documented_exception"] = allowed["reason"]
            used.append(entry)
        elif alt and act == alt and not catalysis_established:
            entry["note"] = "rule branch: catalysis not established"
            branch.append(entry)
        else:
            deviations.append(entry)
    return generic, deviations, branch, used


def phase3_conformance() -> dict:
    """Check the treatment rule across the pre-existing reviews (Phase 3).

    Organism-qualified entries, because lipA, bioB, moaA, hemN and pqqE each exist
    in several organism directories and `load()`'s first-match lookup would silently
    pick one of them.
    """
    spec = yaml.safe_load(PHASE3_SCOPE.read_text())
    exceptions = load_rule_exceptions()
    deviations: list[dict] = []
    branch: list[dict] = []
    used: list[dict] = []
    entries: list[dict] = []
    for qualified in spec["genes"]:
        org, _, sym = qualified.partition("/")
        path = ROOT / "genes" / org / sym / f"{sym}-ai-review.yaml"
        if not path.exists():
            sys.exit(f"phase3 scope names {qualified}, but {path} does not exist")
        review = yaml.safe_load(path.read_text())
        rows = review.get("existing_annotations") or []
        pending = sum(1 for a in rows
                      if ((a.get("review") or {}).get("action")) == "PENDING")
        sam = sam_actions_of(rows)
        catalysis = bool({"ACCEPT", "NEW"} & set(sam))
        generic, devs, brs, exc = rule_check(sym, org, rows, catalysis, exceptions)
        deviations += devs
        branch += brs
        used += exc
        entries.append({
            "gene": qualified, "uniprot": review.get("id"),
            "declared_status": review.get("status"),
            "n_rows": len(rows), "pending_rows": pending,
            "catalysis_established": catalysis,
            "sam_binding_actions": sam or None,
            "generic_rows": {t: dict(sorted(c.items())) for t, c in sorted(generic.items())},
        })
    return {
        "scope_file": str(PHASE3_SCOPE.relative_to(ROOT)),
        "note": ("pre-existing reviews, outside the Phase 4 totals, judged by the same "
                 "rule_check() as the genes in scope"),
        "genes_checked": len(entries),
        "deviations": deviations,
        "branch_uses": branch,
        "documented_exceptions_used": used,
        "genes": entries,
    }


def build() -> dict:
    fm = frontmatter()
    symbols = fm["genes"]
    orgs = list(fm.get("species") or ["human"])

    exceptions = load_rule_exceptions()
    exceptions_used: list[dict] = []

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
        sam_actions = sam_actions_of(rows)
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

        if reviewed:
            g, devs, brs, exc = rule_check(sym, org, rows, catalysis_established,
                                           exceptions)
            for t, c in g.items():
                generic[t].update(c)
            deviations += devs
            rule_branch += brs
            exceptions_used += exc

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

    p3 = phase3_conformance()

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
        "phase3_rule_conformance": p3,
        "documented_rule_exceptions": {
            "file": str(RULE_EXCEPTIONS.relative_to(ROOT)),
            "declared": [{"gene": f"{o}/{g}", "term": t, "actions": sorted(v["actions"]),
                          "reason": v["reason"]}
                         for (o, g, t), v in sorted(exceptions.items())],
            "used": exceptions_used + p3["documented_exceptions_used"],
            "stale": sorted(
                f"{o}/{g}:{t}" for (o, g, t) in exceptions
                if not any(u["organism"] == o and u["gene"] == g and u["term"] == t
                           for u in exceptions_used + p3["documented_exceptions_used"])
            ),
        },
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
    ex = out["documented_rule_exceptions"]
    print(f"documented rule exceptions: {len(ex['declared'])} declared, "
          f"{len(ex['used'])} used, {len(ex['stale'])} stale")
    for stale in ex["stale"]:
        print(f"  STALE EXCEPTION (matches no row): {stale}")
    p3 = out["phase3_rule_conformance"]
    print(f"phase 3 scope: {p3['genes_checked']} pre-existing reviews, "
          f"DEVIATIONS {len(p3['deviations'])}, branch uses {len(p3['branch_uses'])}")
    for d in p3["deviations"]:
        print(f"  {d['organism']}/{d['gene']:<10} {d['term']} {d['action']} "
              f"(expected {'/'.join(d['expected'])})")
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
