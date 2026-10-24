#!/usr/bin/env python3
"""Ask whether GO can express ARHGAP21's contested GAP substrate specificity.

ARHGAP21's literature reports Cdc42 (Dubois 2005), RhoA+Cdc42 (Sousa 2005),
RhoA (Anthony 2011), and RhoA+RhoC (Lazarini 2013).  The obvious curation move
would be to replace the generic `GO:0005096 GTPase activator activity` with a
substrate-specific child.  This script tests whether such a child exists.

It answers two questions that a keyword search cannot:

1. **Do the historical substrate-specific GAP terms still resolve?**  OLS
   reports a MERGED id and an ABSENT id identically, so `secondaryIds` from
   QuickGO's `/complete` endpoint is the only way to tell them apart.
2. **Does `GO:0005096` have substrate-specific children today?**  Children are
   enumerable; text queries are not.  A failed search is not evidence of
   absence.

Run:  uv run --with requests python check_gap_terms.py
Writes: gap_terms.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

BASE = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms"

GENERIC = "GO:0005096"

# Historical substrate-specific GAP terms, plus the GTPase-binding terms the
# campaign has already seen merged.  Each is asked individually: a batch query
# silently collapses several requested ids onto one result row, which reads as
# "only one exists" when in fact several merged into it.
CANDIDATES = [
    "GO:0005096",  # GTPase activator activity (the generic term in GOA)
    "GO:0005099",  # Ras GTPase activator activity
    "GO:0005100",  # Rho GTPase activator activity
    "GO:0008060",  # ARF GTPase activator activity
    "GO:0005097",  # Rab GTPase activator activity
    "GO:0017137",  # Rab GTPase binding
    "GO:0017048",  # Rho GTPase binding
    "GO:0031267",  # small GTPase binding
    "GO:0071889",  # 14-3-3 protein binding
    "GO:0030165",  # PDZ domain binding
]


def complete(go_id: str) -> dict[str, object]:
    resp = requests.get(f"{BASE}/{go_id}/complete", timeout=60)
    if resp.status_code != 200:
        return {"requested": go_id, "http_status": resp.status_code, "resolved": None}
    results = resp.json().get("results") or []
    if not results:
        return {"requested": go_id, "http_status": 200, "resolved": None}
    r = results[0]
    return {
        "requested": go_id,
        "http_status": 200,
        "resolved": r["id"],
        "name": r.get("name"),
        "is_obsolete": r.get("isObsolete"),
        "secondary_ids": r.get("secondaryIds"),
        "definition": (r.get("definition") or {}).get("text"),
        # MERGED: the id you asked for is not the id you got back.
        "merged_into": r["id"] if r["id"] != go_id else None,
    }


def children(go_id: str) -> list[dict[str, str]]:
    resp = requests.get(f"{BASE}/{go_id}/children", timeout=60)
    resp.raise_for_status()
    results = resp.json().get("results") or []
    out: list[dict[str, str]] = []
    for r in results:
        for c in r.get("children") or []:
            out.append({"id": c["id"], "name": c["name"], "relation": c["relation"]})
    return out


def main() -> int:
    resolved = {go_id: complete(go_id) for go_id in CANDIDATES}

    # Assert presence: a guard that only validates the entries it happens to
    # find passes silently when an entry is dropped.
    missing = set(CANDIDATES) - set(resolved)
    assert not missing, f"candidate terms dropped: {sorted(missing)}"

    kids = children(GENERIC)
    is_a_kids = [c for c in kids if c["relation"] == "is_a"]

    merged = {
        k: v["merged_into"] for k, v in resolved.items() if v.get("merged_into")
    }
    unresolvable = [k for k, v in resolved.items() if v.get("resolved") is None]

    out = {
        "generic_term": GENERIC,
        "generic_children_all_relations": kids,
        "generic_is_a_children": is_a_kids,
        "n_is_a_children": len(is_a_kids),
        "resolved": resolved,
        "merged_ids": merged,
        "unresolvable_ids": unresolvable,
    }

    dest = Path(__file__).with_name("gap_terms.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    for go_id in CANDIDATES:
        v = resolved[go_id]
        tag = "UNRESOLVABLE"
        if v.get("resolved"):
            tag = f"-> {v['resolved']} {v['name']}"
            if v.get("merged_into"):
                tag = "MERGED " + tag
            if v.get("is_obsolete"):
                tag = "OBSOLETE " + tag
        print(f"{go_id:<12} {tag}")
    print()
    print(f"{GENERIC} is_a children: {len(is_a_kids)}")
    for c in is_a_kids:
        print("   ", c["id"], c["name"])
    print(f"{GENERIC} children (all relations): {len(kids)}")
    for c in kids:
        print("   ", c["id"], c["name"], f"({c['relation']})")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
