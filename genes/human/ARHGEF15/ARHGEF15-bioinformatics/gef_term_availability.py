"""Can GO still name the GTPase a GEF acts on? Checked on two INDEPENDENT services.

This is load-bearing for the review's knowledge gap, so it is not allowed to rest on a
single endpoint. QuickGO silently resolves merged ids -- requesting an id that was merged
away returns the *successor's* record with `isObsolete: false` -- so "not obsolete" from
QuickGO alone is ambiguous between "current" and "merged into something else". OLS4 is a
different codebase with a different loader and reports `is_obsolete` + `term_replaced_by`
on the requested id itself. The two together disambiguate; either alone does not.

Usage: uv run --no-project python gef_term_availability.py
"""

from __future__ import annotations

import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / "gef_term_availability.json"

GENERAL = "GO:0005085"  # guanyl-nucleotide exchange factor activity

# The substrate-specific GEF molecular-function terms GO used to carry.
SPECIFIC = {
    "GO:0005086": "ARF guanyl-nucleotide exchange factor activity",
    "GO:0005087": "Ran guanyl-nucleotide exchange factor activity",
    "GO:0005088": "Ras guanyl-nucleotide exchange factor activity",
    "GO:0005089": "Rho guanyl-nucleotide exchange factor activity",
    "GO:0008321": "Ral guanyl-nucleotide exchange factor activity",
}

# The biological-process branch was NOT flattened, so the two aspects disagree about
# whether substrate identity is expressible. These are the terms that matter for a GEF
# whose measured substrates are RhoA in one system and RhoA + Cdc42 in another.
BP_TERMS = {
    "GO:0007266": "Rho protein signal transduction",
    "GO:0032488": "Cdc42 protein signal transduction",
    "GO:0035023": "regulation of Rho protein signal transduction",
    "GO:0035025": "positive regulation of Rho protein signal transduction",
    "GO:0032489": "regulation of Cdc42 protein signal transduction",
    "GO:0035020": "regulation of Rac protein signal transduction",
    "GO:0035022": "positive regulation of Rac protein signal transduction",
}


def get(url: str) -> dict:
    req = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": "ai-gene-review"}
    )
    with urllib.request.urlopen(req, timeout=120) as fh:
        return json.load(fh)


def quickgo(term: str) -> dict:
    r = get(f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{term}/complete")["results"][0]
    return {
        "requested": term,
        "id_returned": r.get("id"),
        "name_returned": r.get("name"),
        "isObsolete": r.get("isObsolete"),
        "secondaryIds": r.get("secondaryIds") or [],
        "children": r.get("children") or [],
        "synonym_names": [s.get("name") for s in (r.get("synonyms") or [])],
        # the tell: QuickGO answered about a DIFFERENT id than the one asked for
        "silently_redirected": r.get("id") != term,
    }


def ols4(term: str) -> dict:
    iri = "http://purl.obolibrary.org/obo/" + term.replace(":", "_")
    enc = urllib.parse.quote(urllib.parse.quote(iri, safe=""), safe="")
    try:
        d = get(f"https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/{enc}")
    except urllib.error.HTTPError as e:
        return {"requested": term, "http_status": e.code, "present": False}
    return {
        "requested": term,
        "http_status": 200,
        "present": True,
        "obo_id": d.get("obo_id"),
        "label": d.get("label"),
        "is_obsolete": d.get("is_obsolete"),
        "term_replaced_by": d.get("term_replaced_by"),
    }


def ols4_children(term: str) -> list[dict]:
    iri = "http://purl.obolibrary.org/obo/" + term.replace(":", "_")
    enc = urllib.parse.quote(urllib.parse.quote(iri, safe=""), safe="")
    d = get(f"https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/{enc}/hierarchicalChildren?size=500")
    return [
        {"obo_id": k.get("obo_id"), "label": k.get("label")}
        for k in d.get("_embedded", {}).get("terms", [])
    ]


def main() -> None:
    res: dict = {"general_term": GENERAL, "specific_terms": {}}

    res["general_quickgo"] = quickgo(GENERAL)
    res["general_ols4"] = ols4(GENERAL)
    res["general_ols4_is_a_children"] = ols4_children(GENERAL)

    for term, historical_label in SPECIFIC.items():
        q, o = quickgo(term), ols4(term)
        merged_per_quickgo = q["silently_redirected"] or term in (
            res["general_quickgo"]["secondaryIds"]
        )
        merged_per_ols4 = bool(o.get("is_obsolete")) and (
            (o.get("term_replaced_by") or "").replace("GO_", "GO:") == GENERAL
            or (o.get("term_replaced_by") or "").endswith(GENERAL.replace(":", "_"))
        )
        res["specific_terms"][term] = {
            "historical_label": historical_label,
            "quickgo": q,
            "ols4": o,
            "merged_into_general_per_quickgo": merged_per_quickgo,
            "merged_into_general_per_ols4": merged_per_ols4,
            "two_services_agree": merged_per_quickgo == merged_per_ols4,
        }

    # --- BP branch: same two services, same disambiguation discipline ---
    res["bp_terms"] = {}
    for term, expected in BP_TERMS.items():
        q, o = quickgo(term), ols4(term)
        res["bp_terms"][term] = {
            "expected_label": expected,
            "quickgo_name": q["name_returned"],
            "quickgo_obsolete": q["isObsolete"],
            "quickgo_silently_redirected": q["silently_redirected"],
            "quickgo_children": q["children"],
            "ols4_label": o.get("label"),
            "ols4_is_obsolete": o.get("is_obsolete"),
            "ols4_is_a_children": ols4_children(term),
            "present_and_current_on_both_services": (
                not q["silently_redirected"] and not q["isObsolete"] and not o.get("is_obsolete")
            ),
        }

    def kids(term: str) -> int:
        row = res["bp_terms"][term]
        return max(len(row["ols4_is_a_children"]), len(row["quickgo_children"] or []))

    res["bp_asymmetry"] = {
        "substrate_specific_BP_terms_still_current": [
            t for t, v in res["bp_terms"].items() if v["present_and_current_on_both_services"]
        ],
        "rho_has_signed_regulation_child": kids("GO:0035023") > 0,
        "rac_has_signed_regulation_child": "GO:0035022" in BP_TERMS,
        "cdc42_regulation_children_ols4": len(res["bp_terms"]["GO:0032489"]["ols4_is_a_children"]),
        "cdc42_regulation_children_quickgo": len(
            res["bp_terms"]["GO:0032489"]["quickgo_children"] or []
        ),
    }

    res["summary"] = {
        "n_specific_terms_checked": len(SPECIFIC),
        "n_merged_into_general_on_both_services": sum(
            1
            for v in res["specific_terms"].values()
            if v["merged_into_general_per_quickgo"] and v["merged_into_general_per_ols4"]
        ),
        "n_services_disagree": sum(
            1 for v in res["specific_terms"].values() if not v["two_services_agree"]
        ),
        "general_term_is_a_children_ols4": len(res["general_ols4_is_a_children"]),
        "general_term_children_quickgo": res["general_quickgo"]["children"],
        "substrate_named_only_as_synonym": [
            s
            for s in res["general_quickgo"]["synonym_names"]
            if "guanyl-nucleotide exchange factor activity" in (s or "")
        ],
    }

    OUT.write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")

    s = res["summary"]
    print(f"{GENERAL} {res['general_quickgo']['name_returned']!r}")
    print(f"  OLS4 is_a children: {s['general_term_is_a_children_ols4']}")
    print(f"  QuickGO children (any relation): {s['general_term_children_quickgo']}")
    print(
        f"  merged into it, agreed by BOTH services: "
        f"{s['n_merged_into_general_on_both_services']}/{s['n_specific_terms_checked']}"
        f" (services disagree on {s['n_services_disagree']})"
    )
    for term, v in sorted(res["specific_terms"].items()):
        print(
            f"    {term} {v['historical_label']}: quickgo_merged={v['merged_into_general_per_quickgo']} "
            f"ols4_merged={v['merged_into_general_per_ols4']} "
            f"(quickgo returned {v['quickgo']['id_returned']}, ols4 replaced_by {v['ols4'].get('term_replaced_by')})"
        )
    print(f"  substrate names surviving only as synonyms: {s['substrate_named_only_as_synonym']}")
    print()
    print("biological-process branch (same two services):")
    for term, v in sorted(res["bp_terms"].items()):
        print(
            f"  {term} {v['quickgo_name']!r} current_on_both={v['present_and_current_on_both_services']} "
            f"ols4_is_a_children={len(v['ols4_is_a_children'])}"
        )
    a = res["bp_asymmetry"]
    print(
        f"  substrate-specific BP terms still current: {len(a['substrate_specific_BP_terms_still_current'])}"
        f"/{len(BP_TERMS)}"
    )
    print(
        f"  GO:0032489 (regulation of Cdc42 signal transduction) children: "
        f"ols4={a['cdc42_regulation_children_ols4']} quickgo={a['cdc42_regulation_children_quickgo']}"
    )
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
