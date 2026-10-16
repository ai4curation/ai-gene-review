#!/usr/bin/env python3
"""Can GO say which GTPase a Rho-family GEF acts on?  Checked on three services.

ARHGEF16/Ephexin-4 exchanges nucleotide on RhoG and, in cells, on nothing else --
not Rac1, not Cdc42, not RhoA (PMID:20679435).  That specificity is the single
fact that separates it from its four ephexin siblings, all of which are RhoA GEFs.
The review therefore rests on a claim about the ontology: that GO has no term in
which to write it, so substrate identity has to live in ``has input`` extensions
and ``core_functions[].substrates``.

A "GO cannot express this" claim is load-bearing, and GO services disagree with
each other about obsolescence and childlessness, so this script asks **three
independent services** -- the GO API (api.geneontology.org), OLS4
(ebi.ac.uk/ols4) and QuickGO (ebi.ac.uk/QuickGO) -- and requires them to agree
before the claim is reported as established.  Two endpoints of one service is one
check, so each service is queried once through its own API.

Two questions:

**Q1 -- are the substrate-specific terms gone?**  For each candidate
(``GO:0005089`` Rho GEF activity, ``GO:0030676`` Rac GEF activity, ``GO:0017048``
Rho GTPase binding, ``GO:0032860`` activation of Rho GTPase activity ...) the GO
API is asked whether the id appears among the ``alternativeIds`` of the general
parent, and OLS4 is asked whether the id is obsolete and what replaced it.
QuickGO is asked too, and its answer is recorded but **not** trusted on its own:
it silently resolves merges, returning the replacement term's record with
``isObsolete: false``.  That behaviour is asserted here as a fact about QuickGO,
because an agent that reads it at face value concludes the term is alive.

**Q2 -- do the general parents still have is_a children?**  If a specific term
survived somewhere, it would show up as an ``is_a`` child.  The GO API
``/subgraph`` descendants and OLS4 ``hierarchicalChildren`` are both consulted.
QuickGO's ``/children`` is consulted too and its relation types are printed,
because its non-``is_a`` children (``capable_of``, ``negatively_regulates``) have
previously been miscounted as evidence that a term still has children.

Run:    uv run --with requests python gef_term_structure.py
        uv run --with requests python gef_term_structure.py --self-test
Writes: gef_term_structure.json
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from pathlib import Path

import requests

GO_API = "https://api.geneontology.org/api/ontology/term/{go}"
GO_API_SUBGRAPH = "https://api.geneontology.org/api/ontology/term/{go}/subgraph"
OLS4_TERM = "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms"
OLS4_CHILDREN = (
    "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/{iri}/hierarchicalChildren"
)
QUICKGO_TERM = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go}"
QUICKGO_CHILDREN = (
    "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go}/children"
)

TIMEOUT = 90

# specific term -> the general parent it is claimed to have been merged into.
MERGED: dict[str, dict[str, str]] = {
    "GO:0005089": {"was": "Rho guanyl-nucleotide exchange factor activity", "into": "GO:0005085"},
    "GO:0030676": {"was": "Rac guanyl-nucleotide exchange factor activity", "into": "GO:0005085"},
    "GO:0005088": {"was": "Ras guanyl-nucleotide exchange factor activity", "into": "GO:0005085"},
    "GO:0017048": {"was": "Rho GTPase binding", "into": "GO:0031267"},
    "GO:0032860": {"was": "activation of Rho GTPase activity", "into": "GO:0090630"},
    "GO:0032861": {"was": "activation of Rac GTPase activity", "into": "GO:0090630"},
    "GO:0005100": {"was": "Rho GTPase activator activity", "into": "GO:0005096"},
}

# The general parents whose is_a childlessness is asserted.
PARENTS = ["GO:0005085", "GO:0031267", "GO:0090630", "GO:0005096"]

# NEGATIVE CONTROL.  A term that is emphatically NOT merged and NOT childless.
# If the merge detector fires on this, it is detecting something other than a
# merge; if the childlessness detector fires on it, the child queries are broken.
LIVE_CONTROL = "GO:0003674"  # molecular_function, the MF root

# The two definitions the review turns on: GO:0005096 is hydrolysis-based (a GAP)
# while GO:0090630, whose name reads like it, is exchange-based (a GEF).
DEFINITION_PROBES = {
    "GO:0005096": {"must_contain": "hydrolysis", "reading": "GAP: increases GTP hydrolysis"},
    "GO:0090630": {"must_contain": "GDP by GTP", "reading": "GEF: GDP-to-GTP replacement"},
    "GO:0005085": {"must_contain": "exchange of GDP to GTP", "reading": "GEF"},
}


def go_api_term(go: str) -> dict:
    r = requests.get(GO_API.format(go=go), timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def go_api_descendants(go: str) -> list[dict]:
    r = requests.get(GO_API_SUBGRAPH.format(go=go), timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("descendents") or []


def ols4_term(go: str) -> dict | None:
    r = requests.get(OLS4_TERM, params={"obo_id": go}, timeout=TIMEOUT)
    r.raise_for_status()
    terms = r.json().get("_embedded", {}).get("terms", [])
    return terms[0] if terms else None


def ols4_children(go: str) -> dict:
    iri = urllib.parse.quote(
        urllib.parse.quote(f"http://purl.obolibrary.org/obo/{go.replace(':', '_')}", safe=""),
        safe="",
    )
    r = requests.get(OLS4_CHILDREN.format(iri=iri), params={"size": 200}, timeout=TIMEOUT)
    r.raise_for_status()
    d = r.json()
    return {
        "total": d.get("page", {}).get("totalElements"),
        "labels": [t.get("label") for t in d.get("_embedded", {}).get("terms", [])],
    }


def quickgo_term(go: str) -> dict | None:
    r = requests.get(
        QUICKGO_TERM.format(go=go), headers={"Accept": "application/json"}, timeout=TIMEOUT
    )
    if r.status_code == 404:
        return None
    r.raise_for_status()
    res = r.json().get("results") or []
    return res[0] if res else None


def quickgo_children(go: str) -> list[dict]:
    r = requests.get(
        QUICKGO_CHILDREN.format(go=go), headers={"Accept": "application/json"}, timeout=TIMEOUT
    )
    r.raise_for_status()
    res = r.json().get("results") or []
    return (res[0].get("children") or []) if res else []


def probe_merge(specific: str, parent: str) -> dict[str, object]:
    """Three independent readings of 'is this specific term still usable?'."""
    parent_rec = go_api_term(parent)
    go_api_says_merged = specific in (parent_rec.get("alternativeIds") or [])

    o = ols4_term(specific)
    ols4_says_obsolete = bool(o and o.get("is_obsolete"))
    ols4_replaced_by = (o or {}).get("term_replaced_by")

    q = quickgo_term(specific)
    quickgo_returned_id = (q or {}).get("id")
    quickgo_says_obsolete = (q or {}).get("isObsolete")
    # QuickGO's documented-here failure mode: asked for a merged id it hands back
    # the *replacement's* record, non-obsolete, with a different id than asked for.
    quickgo_silently_resolved = bool(q and quickgo_returned_id != specific)

    return {
        "specific": specific,
        "parent": parent,
        "go_api_lists_as_alternative_id_of_parent": go_api_says_merged,
        "ols4_is_obsolete": ols4_says_obsolete,
        "ols4_term_replaced_by": ols4_replaced_by,
        "quickgo_returned_id": quickgo_returned_id,
        "quickgo_is_obsolete": quickgo_says_obsolete,
        "quickgo_silently_resolved_the_merge": quickgo_silently_resolved,
        # Established only when the two services that answer honestly agree.
        "merged_confirmed_by_two_services": bool(
            go_api_says_merged
            and ols4_says_obsolete
            and (ols4_replaced_by or "").replace("_", ":") == parent
        ),
    }


def probe_children(parent: str) -> dict[str, object]:
    desc = go_api_descendants(parent)
    ols = ols4_children(parent)
    qg = quickgo_children(parent)
    qg_is_a = [c for c in qg if c.get("relation") == "is_a"]
    return {
        "term": parent,
        "go_api_n_descendants": len(desc),
        "ols4_n_hierarchical_children": ols["total"],
        "quickgo_n_children_any_relation": len(qg),
        "quickgo_child_relations": sorted({c.get("relation") for c in qg}),
        "quickgo_n_is_a_children": len(qg_is_a),
        "no_is_a_children_confirmed_by_two_services": bool(
            len(desc) == 0 and ols["total"] == 0
        ),
    }


def probe_definitions() -> dict[str, dict[str, object]]:
    out = {}
    for go, spec in DEFINITION_PROBES.items():
        rec = go_api_term(go)
        definition = rec.get("definition") or ""
        o = ols4_term(go)
        # OLS4's `description` is a LIST that mixes the definition with any
        # editor comments, and the comment is not reliably last -- for
        # GO:0005096 the Sar-nomenclature note comes first.  Joining rather than
        # indexing is the difference between reading the definition and reading
        # a footnote.
        ols_def = " ".join((o or {}).get("description") or [])
        out[go] = {
            "label": rec.get("label"),
            "go_api_definition": definition,
            "ols4_definition": ols_def,
            "reading": spec["reading"],
            "go_api_matches_reading": spec["must_contain"].lower() in definition.lower(),
            "ols4_matches_reading": spec["must_contain"].lower() in ols_def.lower(),
        }
    return out


def run() -> dict[str, object]:
    merges = {s: probe_merge(s, m["into"]) | {"former_label": m["was"]} for s, m in MERGED.items()}
    children = {p: probe_children(p) for p in PARENTS}
    control_merge = probe_merge(LIVE_CONTROL, "GO:0005085")
    control_children = probe_children(LIVE_CONTROL)
    defs = probe_definitions()

    failures: list[str] = []
    if control_merge["merged_confirmed_by_two_services"]:
        failures.append(f"negative control {LIVE_CONTROL} reported as merged")
    if control_children["no_is_a_children_confirmed_by_two_services"]:
        failures.append(f"negative control {LIVE_CONTROL} reported as childless")
    for go, d in defs.items():
        if not (d["go_api_matches_reading"] and d["ols4_matches_reading"]):
            failures.append(f"{go} definition no longer matches '{d['reading']}'")
    if failures:
        raise RuntimeError("control failure:\n  " + "\n  ".join(failures))

    return {
        "question": "does GO retain any term for the GTPase a Rho-family GEF acts on?",
        "merged_terms": merges,
        "general_parents": children,
        "definitions": defs,
        "negative_controls": {
            "term": LIVE_CONTROL,
            "merge_probe": control_merge,
            "children_probe": control_children,
        },
        "verdict": {
            "all_specific_terms_merged": all(
                d["merged_confirmed_by_two_services"] for d in merges.values()
            ),
            "all_parents_have_no_is_a_children": all(
                d["no_is_a_children_confirmed_by_two_services"] for d in children.values()
            ),
            "quickgo_silently_resolved": sorted(
                s for s, d in merges.items() if d["quickgo_silently_resolved_the_merge"]
            ),
            "quickgo_reported_non_is_a_children": {
                p: d["quickgo_child_relations"]
                for p, d in children.items()
                if d["quickgo_n_children_any_relation"] > d["quickgo_n_is_a_children"]
            },
        },
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []

    # 1. The merge detector must NOT fire on a live, unmerged term.
    c = probe_merge(LIVE_CONTROL, "GO:0005085")
    checks.append(
        (
            "negative control: MF root is not reported merged",
            "PASS" if not c["merged_confirmed_by_two_services"] else f"FAIL {c}",
        )
    )

    # 2. The childlessness detector must NOT fire on a term with thousands of children.
    cc = probe_children(LIVE_CONTROL)
    checks.append(
        (
            "negative control: MF root is not reported childless",
            "PASS" if not cc["no_is_a_children_confirmed_by_two_services"] else f"FAIL {cc}",
        )
    )

    # 3. The merge detector MUST fire on a term we independently know is merged.
    p = probe_merge("GO:0005089", "GO:0005085")
    checks.append(
        (
            "positive control: GO:0005089 detected as merged into GO:0005085",
            "PASS" if p["merged_confirmed_by_two_services"] else f"FAIL {p}",
        )
    )

    # 4. Pointing a merged term at the WRONG parent must not confirm.  Otherwise
    #    the probe is detecting 'obsolete' and ignoring where it went.
    w = probe_merge("GO:0005089", "GO:0031267")
    checks.append(
        (
            "wrong parent does not confirm the merge",
            "PASS" if not w["merged_confirmed_by_two_services"] else f"FAIL {w}",
        )
    )

    # 5. Breaking a definition expectation must abort the whole run.
    saved = DEFINITION_PROBES["GO:0005096"]["must_contain"]
    DEFINITION_PROBES["GO:0005096"]["must_contain"] = "exchange of GDP to GTP"
    try:
        run()
        checks.append(("definition drift aborts the run", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(
            (
                "definition drift aborts the run",
                "PASS" if "definition no longer matches" in str(e) else f"FAIL {e}",
            )
        )
    finally:
        DEFINITION_PROBES["GO:0005096"]["must_contain"] = saved

    # 6. NEGATIVE CONTROL for check 5: with the real expectation restored the run
    #    must complete silently.
    try:
        run()
        checks.append(("restored expectations run clean", "PASS"))
    except RuntimeError as e:
        checks.append(("restored expectations run clean", f"FAIL {e}"))

    for name, verdict in checks:
        mark = verdict.split()[0]
        print(f"  [{mark}] {name}" + ("" if mark == "PASS" else f" -- {verdict}"))
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("gef_term_structure.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"{'specific term':<13} {'former label':<44} {'->':<3} {'parent':<11} {'GO API':>7} {'OLS4':>6} {'QuickGO id':>12}")
    for s, d in out["merged_terms"].items():
        print(
            f"{s:<13} {d['former_label'][:43]:<44} {'->':<3} {d['parent']:<11} "
            f"{str(d['go_api_lists_as_alternative_id_of_parent']):>7} "
            f"{str(d['ols4_is_obsolete']):>6} {str(d['quickgo_returned_id']):>12}"
        )
    print()
    print(f"{'general parent':<13} {'GO API desc':>12} {'OLS4 children':>14} {'QuickGO any':>12} {'QuickGO is_a':>13}  relations")
    for p, d in out["general_parents"].items():
        print(
            f"{p:<13} {d['go_api_n_descendants']:>12} {str(d['ols4_n_hierarchical_children']):>14} "
            f"{d['quickgo_n_children_any_relation']:>12} {d['quickgo_n_is_a_children']:>13}  "
            f"{','.join(r for r in d['quickgo_child_relations'] if r) or '-'}"
        )
    print()
    for go, d in out["definitions"].items():
        print(f"{go} {d['label']}: {d['reading']}")
    v = out["verdict"]
    print()
    print("  every substrate-specific term merged (2 services agree):", v["all_specific_terms_merged"])
    print("  every general parent has no is_a children (2 services agree):", v["all_parents_have_no_is_a_children"])
    print("  QuickGO silently resolved:", v["quickgo_silently_resolved"] or "none")
    print("  QuickGO non-is_a children:", v["quickgo_reported_non_is_a_children"] or "none")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
