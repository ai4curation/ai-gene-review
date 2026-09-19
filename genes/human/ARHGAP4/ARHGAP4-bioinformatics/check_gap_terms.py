#!/usr/bin/env python3
"""Can GO still express *which* GTPase a GAP acts on?

ARHGAP4's only experimental activity measurement (PMID:12414125, rat protein)
reports stimulation of RAC1, CDC42 and RHOA, and Reactome files it under
``R-HSA-9013144 RAC1 GAPs stimulate RAC1 GTPase activity``.  Recording that
substrate identity needs a substrate-specific GAP term.  This script asks whether
one exists, and whether ``GO:0005096 GTPase activator activity`` has any ``is_a``
children to refine into.

**Why more than one service.**  QuickGO **silently resolves merges**: ask it for a
merged id and it hands back the *surviving* term's record, flagged
``isObsolete: false``.  Read naively that says "the term is alive and well", which
is the opposite of the truth.  Its obsolescence answers therefore cannot be taken
at face value in either direction, and two QuickGO endpoints are one check, not
two.  So every claim here is taken from **independent services**:

1. **OLS4** (EBI)                -- ``is_obsolete``, ``term_replaced_by``, and the
                                    count of *asserted direct* subclasses.
2. **GO API** (geneontology.org) -- an independent resolver; a merged id comes back
                                    as an empty record, and the merged terms'
                                    names show up as *synonyms* of the survivor.
3. **repo cache** ``cache/go/terms.csv`` -- what this repo's own validation sees.
4. **QuickGO**                   -- recorded for its ``secondaryIds`` list and its
                                    child *relation types*, with its merge-masking
                                    behaviour asserted rather than trusted.

**Relation types matter.**  "No children" and "no ``is_a`` children" are different
claims and only the second is true: QuickGO reports exactly one child of
``GO:0005096``, and it is ``capable_of GO:1902773 GTPase activator complex`` --
a complex that is capable of the activity, not a more specific activity.  The
script prints the relation of every child it finds so the distinction cannot be
lost downstream.

Run:    uv run --with requests python check_gap_terms.py
        uv run --with requests python check_gap_terms.py --self-test
Writes: gap_terms.json
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
from pathlib import Path

import requests

OLS4 = "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms"
GO_API = "https://api.geneontology.org/api/ontology/term/{cid}"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{cid}/complete"

SURVIVOR = "GO:0005096"

# The substrate-specific GAP terms a curator would reach for, plus the two
# substrate-specific *binding* terms, since "has input"-style substrate identity
# is sometimes carried on a binding term instead.
CANDIDATES = {
    "GO:0005096": "GTPase activator activity (the survivor)",
    "GO:0005100": "Rho GTPase activator activity",
    "GO:0005099": "Ras GTPase activator activity",
    "GO:0008060": "ARF GTPase activator activity",
    "GO:0005097": "Rab GTPase activator activity",
    "GO:0005098": "Ras GTPase activator activity (alt id)",
    "GO:0046582": "Rap GTPase activator activity",
    "GO:0017048": "Rho GTPase binding",
    "GO:0031267": "small GTPase binding",
}


def iri(cid: str) -> str:
    return "http://purl.obolibrary.org/obo/" + cid.replace(":", "_")


def ols4_term(cid: str) -> dict[str, object] | None:
    r = requests.get(OLS4, params={"iri": iri(cid)}, timeout=90)
    r.raise_for_status()
    terms = r.json().get("_embedded", {}).get("terms", [])
    if not terms:
        return None
    t = terms[0]
    return {
        "label": t.get("label"),
        "is_obsolete": t.get("is_obsolete"),
        "term_replaced_by": (t.get("term_replaced_by") or "").replace(
            "GO_", "GO:"
        )
        or None,
        "has_children": t.get("has_children"),
    }


def ols4_direct_children(cid: str) -> list[dict[str, str]]:
    """OLS4 ``/children`` == asserted *direct subclasses*, i.e. ``is_a`` children.
    This is the number the 'nothing more specific exists' claim rests on."""
    enc = urllib.parse.quote(urllib.parse.quote(iri(cid), safe=""), safe="")
    r = requests.get(f"{OLS4}/{enc}/children", params={"size": 200}, timeout=90)
    if r.status_code == 404:
        return []
    r.raise_for_status()
    d = r.json()
    page = d.get("page", {})
    if page.get("totalPages", 0) > 1:
        raise RuntimeError(f"paginated children for {cid}; widen the page")
    return [
        {"id": c["obo_id"], "label": c["label"], "relation": "is_a"}
        for c in d.get("_embedded", {}).get("terms", [])
    ]


def go_api_term(cid: str) -> dict[str, object]:
    r = requests.get(GO_API.format(cid=urllib.parse.quote(cid)), timeout=90)
    r.raise_for_status()
    d = r.json()
    return {
        "label": d.get("label"),
        "resolves": bool(d.get("label")),
        "synonyms": d.get("synonyms") or [],
    }


def quickgo_term(cid: str) -> dict[str, object]:
    r = requests.get(
        QUICKGO.format(cid=cid), headers={"Accept": "application/json"}, timeout=90
    )
    r.raise_for_status()
    res = (r.json().get("results") or [None])[0]
    if res is None:
        return {"resolves": False}
    return {
        "resolves": True,
        "id_returned": res.get("id"),
        "name": res.get("name"),
        "isObsolete": res.get("isObsolete"),
        "secondaryIds": res.get("secondaryIds") or [],
        "children": [
            {"id": c["id"], "relation": c["relation"]} for c in (res.get("children") or [])
        ],
    }


def repo_cache(cid: str) -> dict[str, object]:
    here = Path(__file__).resolve()
    root = next(p for p in here.parents if (p / "cache" / "go" / "terms.csv").exists())
    path = root / "cache" / "go" / "terms.csv"
    with path.open() as fh:
        for row in csv.DictReader(fh):
            if row["curie"] == cid:
                return {
                    "present": True,
                    "label": row["label"],
                    "label_marked_obsolete": row["label"].startswith("obsolete "),
                }
    return {"present": False, "label": None, "label_marked_obsolete": None}


def run() -> dict[str, object]:
    out: dict[str, object] = {"terms": {}}
    for cid, note in CANDIDATES.items():
        ols = ols4_term(cid)
        qg = quickgo_term(cid)
        out["terms"][cid] = {
            "note": note,
            "ols4": ols,
            "go_api": go_api_term(cid),
            "repo_cache": repo_cache(cid),
            "quickgo": qg,
            # QuickGO handing back a *different* id than requested is the
            # merge-masking behaviour; record it explicitly.
            "quickgo_masked_the_merge": bool(
                qg.get("resolves")
                and qg.get("id_returned") != cid
                and qg.get("isObsolete") is False
            ),
        }

    merged_into_survivor = sorted(
        cid
        for cid, v in out["terms"].items()
        if v["ols4"] and v["ols4"]["is_obsolete"] and v["ols4"]["term_replaced_by"] == SURVIVOR
    )

    is_a_children = ols4_direct_children(SURVIVOR)
    qg_children = out["terms"][SURVIVOR]["quickgo"].get("children", [])
    non_is_a_children = [c for c in qg_children if c["relation"] != "is_a"]

    # Agreement across services is the point: a claim only survives if the
    # independent resolvers say the same thing.
    agreement = {}
    for cid, v in out["terms"].items():
        ols_obs = v["ols4"]["is_obsolete"] if v["ols4"] else None
        go_resolves = v["go_api"]["resolves"]
        agreement[cid] = {
            "ols4_obsolete": ols_obs,
            "go_api_resolves_as_live_term": go_resolves,
            # A live term resolves in the GO API and is not obsolete in OLS4.
            "services_agree": (ols_obs is True and go_resolves is False)
            or (ols_obs is False and go_resolves is True),
        }

    survivor_syns = out["terms"][SURVIVOR]["go_api"]["synonyms"]
    substrate_names_now_synonyms = sorted(
        s
        for s in survivor_syns
        if any(
            tok in s
            for tok in ("Rho ", "Ras ", "Rab ", "ARF ", "Rac ", "Ral ", "Ran ", "Rap ")
        )
    )

    out["conclusion"] = {
        "survivor": SURVIVOR,
        "merged_into_survivor": merged_into_survivor,
        "survivor_is_a_children": is_a_children,
        "survivor_is_a_child_count": len(is_a_children),
        "survivor_non_is_a_children_per_quickgo": non_is_a_children,
        "substrate_specific_names_now_synonyms_of_survivor": substrate_names_now_synonyms,
        "services_agree_on_every_term": all(a["services_agree"] for a in agreement.values()),
        "per_term_agreement": agreement,
        "quickgo_masked_merges_for": sorted(
            cid for cid, v in out["terms"].items() if v["quickgo_masked_the_merge"]
        ),
    }
    return out


def self_test() -> int:
    """Each guard must fire on a document broken on purpose, and the negative
    controls must stay silent."""
    checks: list[tuple[str, str]] = []

    # 1. The merge-masking detector must actually fire on a known merged id.
    qg = quickgo_term("GO:0005100")
    checks.append(
        (
            "QuickGO masks the GO:0005100 merge (returns GO:0005096, not obsolete)",
            "PASS"
            if qg.get("id_returned") == SURVIVOR and qg.get("isObsolete") is False
            else f"FAIL {qg.get('id_returned')} obsolete={qg.get('isObsolete')}",
        )
    )
    # 2. NEGATIVE CONTROL: on a term that was never merged, it must NOT fire.
    qg_live = quickgo_term(SURVIVOR)
    checks.append(
        (
            "negative control: no masking reported for the survivor itself",
            "PASS" if qg_live.get("id_returned") == SURVIVOR else f"FAIL {qg_live}",
        )
    )
    # 3. OLS4 must disagree with QuickGO on that same id -- which is the whole
    #    reason for querying two services.
    ols = ols4_term("GO:0005100")
    checks.append(
        (
            "OLS4 reports GO:0005100 obsolete, replaced_by GO:0005096",
            "PASS"
            if ols and ols["is_obsolete"] and ols["term_replaced_by"] == SURVIVOR
            else f"FAIL {ols}",
        )
    )
    # 4. The GO API must refuse to resolve the merged id (independent third line).
    ga = go_api_term("GO:0005100")
    checks.append(
        (
            "GO API returns an empty record for the merged id",
            "PASS" if not ga["resolves"] else f"FAIL {ga}",
        )
    )
    # 5. NEGATIVE CONTROL: the GO API must resolve the survivor.
    ga_live = go_api_term(SURVIVOR)
    checks.append(
        (
            "negative control: GO API resolves the survivor",
            "PASS" if ga_live["resolves"] else f"FAIL {ga_live}",
        )
    )
    # 6. A term genuinely absent from the repo cache must read absent, and one
    #    present must read present -- so 'absent' is a measurement, not a default.
    checks.append(
        (
            "repo cache distinguishes present from absent",
            "PASS"
            if repo_cache(SURVIVOR)["present"] and not repo_cache("GO:0005100")["present"]
            else "FAIL",
        )
    )
    # 7. The is_a child count must be read from OLS4's asserted children, and a
    #    term known to have is_a children must report them -- otherwise a
    #    zero here would just mean the endpoint is broken.
    parent_children = ols4_direct_children("GO:0030695")  # GTPase regulator activity
    checks.append(
        (
            "is_a child endpoint returns children for a term that has them",
            "PASS" if len(parent_children) >= 3 else f"FAIL {parent_children}",
        )
    )
    # 8. ...and GO:0005096 itself must report zero.
    checks.append(
        (
            "survivor has zero is_a children",
            "PASS" if ols4_direct_children(SURVIVOR) == [] else "FAIL",
        )
    )

    for name, verdict in checks:
        print(
            f"  [{verdict.split()[0]}] {name}"
            + ("" if verdict.startswith("PASS") else f" -- {verdict}")
        )
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
    dest = Path(__file__).with_name("gap_terms.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"{'term':<12} {'OLS4':<34} {'GO API':<10} {'repo cache':<12} QuickGO")
    for cid, v in out["terms"].items():
        o = v["ols4"]
        ols = (
            f"obsolete->{o['term_replaced_by']}"
            if o and o["is_obsolete"]
            else (f"live: {o['label']}" if o else "absent")
        )
        ga = "resolves" if v["go_api"]["resolves"] else "EMPTY"
        rc = "present" if v["repo_cache"]["present"] else "absent"
        qgm = "MASKS MERGE" if v["quickgo_masked_the_merge"] else "-"
        print(f"{cid:<12} {ols:<34} {ga:<10} {rc:<12} {qgm}")

    c = out["conclusion"]
    print()
    print("merged into", SURVIVOR, ":", c["merged_into_survivor"])
    print("services agree on every term:", c["services_agree_on_every_term"])
    print(f"{SURVIVOR} is_a children: {c['survivor_is_a_child_count']} {c['survivor_is_a_children']}")
    print(f"{SURVIVOR} non-is_a children (QuickGO): {c['survivor_non_is_a_children_per_quickgo']}")
    print("substrate-specific names surviving only as synonyms:")
    for s in c["substrate_specific_names_now_synonyms_of_survivor"]:
        print("   ", s)
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
