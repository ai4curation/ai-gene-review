#!/usr/bin/env python3
"""Census of ARBA00028538 and of the GO term it asserts.

ARBA00028538 asserts a single consequent: **GO:0046467**, which UniProt still
labels "membrane lipid biosynthetic process". This script checks, entirely from
live public APIs, three things that decide the review:

1. **Is the consequent term still a usable GO term?** (QuickGO ontology service)
2. **Does the rule as served by UniProt today still assert it?** (UniProt ARBA API)
3. **How many annotations does the term actually carry?** (QuickGO annotation search)

It also re-checks the specific protein the GO curator flagged in
geneontology/go-annotation#5835 -- PomBase SPAC31G5.16c = UniProtKB:O14466,
S. pombe Dpm1 -- and reports every ARBA-sourced (GO_REF:0000117) annotation it
currently carries, so the "is this actually fixed?" question in that thread can
be answered from data rather than from memory.

Run:
    uv run python rules/arba/ARBA00028538/scripts/census_arba00028538.py

    # also try to resolve the CATH FunFam ids named by the condition sets
    uv run python rules/arba/ARBA00028538/scripts/census_arba00028538.py --cath

Nothing is hardcoded: the rule, the ontology record and the annotation counts are
all fetched at run time, so if UniProt or GO change upstream the numbers change.
Runs recorded in ARBA00028538-analysis.md were made on 2026-08-29.
"""

from __future__ import annotations

import argparse
import collections
import json
import time
import urllib.error
import urllib.parse
import urllib.request

RULE_ID = "ARBA00028538"
FLAGGED_PROTEIN = "O14466"  # S. pombe dpm1 / SPAC31G5.16c, named in go-annotation#5835

ARBA_API = "https://rest.uniprot.org/arba/{rule_id}"
QUICKGO_TERM = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete"
QUICKGO_ANN = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
CATH_SF = "https://www.cathdb.info/version/v4_3_0/api/rest/superfamily/{sf}"


def get_json(url: str, retries: int = 3, pause: float = 5.0) -> dict:
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:  # rate limits / 404s
            last = exc
            if exc.code not in (429, 500, 502, 503):
                raise
            time.sleep(pause * (attempt + 1))
    raise last  # type: ignore[misc]


# --------------------------------------------------------------------------
# 1. the rule as UniProt serves it today
# --------------------------------------------------------------------------


def fetch_rule() -> dict:
    return get_json(ARBA_API.format(rule_id=RULE_ID))


def rule_go_terms(rule: dict) -> list[tuple[str, str]]:
    out = []
    for ann in rule.get("mainRule", {}).get("annotations", []) or []:
        ref = ann.get("dbReference", {})
        if ref.get("database") == "GO":
            out.append((ref.get("id", ""), ref.get("label", "")))
    return out


def condition_sets(rule: dict) -> list[list[str]]:
    """Flatten each condition set to a list of "type=value" strings."""
    sets = []
    for cs in rule.get("mainRule", {}).get("conditionSets", []) or []:
        conds = []
        for cond in cs.get("conditions", []):
            neg = "NOT " if cond.get("isNegative") else ""
            vals = "|".join(v.get("value", "") for v in cond.get("conditionValues", []))
            conds.append(f"{neg}{cond.get('type')}={vals}")
        sets.append(conds)
    return sets


def condition_kinds(sets: list[list[str]]) -> collections.Counter:
    kinds: collections.Counter = collections.Counter()
    for conds in sets:
        for c in conds:
            kinds[c.split("=", 1)[0]] += 1
    return kinds


def funfam_superfamilies(sets: list[list[str]]) -> list[str]:
    """CATH superfamily ids (the part before ':FF:') named anywhere in the rule."""
    sfs = set()
    for conds in sets:
        for c in conds:
            if c.startswith("FunFam id="):
                for val in c.split("=", 1)[1].split("|"):
                    if ":FF:" in val:
                        sfs.add(val.split(":FF:")[0])
    return sorted(sfs)


# --------------------------------------------------------------------------
# 2. the consequent GO term
# --------------------------------------------------------------------------


def term_record(go_id: str) -> dict:
    payload = get_json(QUICKGO_TERM.format(go_id=go_id))
    results = payload.get("results") or []
    return results[0] if results else {}


def obsoletion_summary(rec: dict) -> dict:
    replacements = [
        f"{r.get('type')} -> {r.get('id')}" for r in (rec.get("replacements") or [])
    ]
    obsoleted_on = [
        h.get("timestamp")
        for h in (rec.get("history") or [])
        if h.get("category") == "OBSOLETION"
    ]
    return {
        "id": rec.get("id"),
        "name": rec.get("name"),
        "isObsolete": rec.get("isObsolete"),
        "comment": rec.get("comment"),
        "replacements": replacements,
        "obsoletion_history_dates": obsoleted_on,
    }


# --------------------------------------------------------------------------
# 3. annotation counts
# --------------------------------------------------------------------------


def annotation_count(go_id: str, **filters: str) -> int:
    params = {"goId": go_id, "goUsage": "exact", "limit": "1", "page": "1"}
    params.update(filters)
    url = f"{QUICKGO_ANN}?{urllib.parse.urlencode(params)}"
    return get_json(url).get("numberOfHits", -1)


def arba_annotations_for(accession: str) -> list[dict]:
    params = {
        "geneProductId": f"UniProtKB:{accession}",
        "limit": "200",
        "page": "1",
    }
    url = f"{QUICKGO_ANN}?{urllib.parse.urlencode(params)}"
    rows = []
    for row in get_json(url).get("results", []):
        xrefs = [
            x["id"]
            for group in (row.get("withFrom") or [])
            for x in group.get("connectedXrefs", [])
        ]
        if any(x.startswith("ARBA") for x in xrefs):
            rows.append(
                {
                    "goId": row["goId"],
                    "reference": row.get("reference"),
                    "evidence": row.get("evidenceCode"),
                    "with": [x for x in xrefs if x.startswith("ARBA")],
                }
            )
    return rows


def go_label(go_id: str) -> str:
    try:
        return term_record(go_id).get("name", "?")
    except Exception:
        return "?"


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--cath",
        action="store_true",
        help="also try to resolve CATH superfamily names (heavily rate-limited)",
    )
    args = ap.parse_args()

    print(f"=== {RULE_ID}: rule as served by UniProt now ===")
    rule = fetch_rule()
    print(f"created  : {rule.get('createdDate')}")
    print(f"modified : {rule.get('modifiedDate')}")
    print(f"stats    : {rule.get('statistics')}")

    sets = condition_sets(rule)
    print(f"condition sets: {len(sets)}")
    print(f"condition kinds: {dict(condition_kinds(sets))}")

    gos = rule_go_terms(rule)
    print(f"consequent GO terms: {gos}")

    print("\n=== consequent term status in GO ===")
    for go_id, uniprot_label in gos:
        rec = term_record(go_id)
        summary = obsoletion_summary(rec)
        print(json.dumps(summary, indent=2))
        print(f"label asserted by the rule : {uniprot_label!r}")
        print(f"label currently in GO      : {summary['name']!r}")
        if summary["isObsolete"]:
            print("*** the rule asserts an OBSOLETE GO term ***")

        print("\n=== annotation counts for the consequent ===")
        print(f"{go_id} exact, any source        : {annotation_count(go_id)}")
        print(
            f"{go_id} exact, GO_REF:0000117    : "
            f"{annotation_count(go_id, reference='GO_REF:0000117')}"
        )
        for repl in rec.get("replacements") or []:
            rid = repl.get("id")
            print(
                f"{rid} ({go_label(rid)}) exact, GO_REF:0000117: "
                f"{annotation_count(rid, reference='GO_REF:0000117')}"
            )

    print(f"\n=== protein flagged in go-annotation#5835: {FLAGGED_PROTEIN} ===")
    rows = arba_annotations_for(FLAGGED_PROTEIN)
    if not rows:
        print("no ARBA-sourced annotations found")
    for row in rows:
        print(
            f"{row['goId']} ({go_label(row['goId'])})  {row['evidence']}  "
            f"{row['reference']}  with={row['with']}"
        )
    print(
        f"ARBA-sourced rows mentioning {RULE_ID}: "
        f"{sum(1 for r in rows if RULE_ID in r['with'])}"
    )

    if args.cath:
        print("\n=== CATH superfamilies named by the rule ===")
        for sf in funfam_superfamilies(sets):
            try:
                data = get_json(CATH_SF.format(sf=sf) + "?content-type=application/json")
                print(f"{sf}\t{data.get('data', {}).get('classification_name')}")
            except Exception as exc:  # rate limiting is common here
                print(f"{sf}\tUNRESOLVED ({exc})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
