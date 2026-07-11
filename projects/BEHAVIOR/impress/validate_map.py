#!/usr/bin/env python3
"""Validate the hand-curated behavioural_assay_go_map.yaml.

These files are bespoke project data (not gene-review docs bound to the LinkML
schema), so this is their dedicated check. Exits non-zero on any failure, so it
can gate CI / a `just` recipe.

Checks (offline):
  - both YAMLs parse;
  - map header has proximity / convergence / default_curation;
  - each assay has a string assay_type, a list `supports_go`, and a `note`;
  - every supports_go entry is {id: GO:nnnnnnn, label: str};
  - assay_type values are unique;
  - the map joins exactly to the ingested canonical assay types
    (every ingested type is mapped; every mapped type is ingested, except
    entries flagged `not_in_impress: true`).

Checks (--online, hits QuickGO):
  - every GO id resolves, is not obsolete, is in the biological_process aspect,
    and its label matches the map verbatim.

Usage:
    uv run python projects/BEHAVIOR/impress/validate_map.py [--online]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
MAP = os.path.join(HERE, "behavioural_assay_go_map.yaml")
INGEST = os.path.join(HERE, "behavioural_assays.yaml")
GO_ID = re.compile(r"^GO:\d{7}$")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--online", action="store_true", help="verify GO ids/labels against QuickGO")
    args = ap.parse_args()
    errors: list[str] = []

    try:
        with open(MAP) as fh:
            m = yaml.safe_load(fh)
    except Exception as e:
        print(f"FAIL: map does not parse: {e}")
        return 1
    try:
        with open(INGEST) as fh:
            ing = yaml.safe_load(fh)
    except Exception as e:
        print(f"FAIL: ingest does not parse: {e}")
        return 1

    for key in ("proximity", "convergence", "default_curation"):
        if key not in m:
            errors.append(f"map missing header key '{key}'")

    seen: set[str] = set()
    entries: list[tuple[str, str, str]] = []  # (assay_type, go_id, label) per occurrence
    for a in m.get("assays") or []:
        at = a.get("assay_type")
        if not isinstance(at, str):
            errors.append(f"assay missing string assay_type: {a!r:.80}")
            continue
        if at in seen:
            errors.append(f"duplicate assay_type: {at}")
        seen.add(at)
        if "note" not in a:
            errors.append(f"{at}: missing note")
        sg = a.get("supports_go")
        if not isinstance(sg, list):
            errors.append(f"{at}: supports_go is not a list")
            continue
        for g in sg:
            if not (isinstance(g, dict) and GO_ID.match(str(g.get("id", ""))) and isinstance(g.get("label"), str)):
                errors.append(f"{at}: malformed supports_go entry {g!r}")
            else:
                entries.append((at, g["id"], g["label"]))

    map_types = seen
    not_impress = {a["assay_type"] for a in m["assays"] if a.get("not_in_impress")}
    ing_types = {a["assay_type"] for a in ing.get("assays") or []}
    missing_from_map = ing_types - map_types
    extra_in_map = (map_types - not_impress) - ing_types
    if missing_from_map:
        errors.append(f"ingested assay types not in map: {sorted(missing_from_map)}")
    if extra_in_map:
        errors.append(f"map assay types not in ingest (and not flagged not_in_impress): {sorted(extra_in_map)}")

    if args.online and not errors:
        import requests
        ids = ",".join(sorted({gid for _, gid, _ in entries}))
        r = requests.get(
            f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}",
            headers={"Accept": "application/json"}, timeout=60)
        r.raise_for_status()
        resolved = {t["id"]: t for t in r.json().get("results", [])}
        for at, gid, label in entries:  # check every occurrence (labels not deduped)
            t = resolved.get(gid)
            if t is None:
                errors.append(f"{at}: {gid} does not resolve in QuickGO")
            elif t.get("isObsolete"):
                errors.append(f"{at}: {gid} obsolete")
            elif t.get("aspect") != "biological_process":
                errors.append(f"{at}: {gid} aspect {t.get('aspect')} (expected biological_process)")
            elif t.get("name") != label:
                errors.append(f"{at}: {gid} label '{label}' != QuickGO '{t.get('name')}'")

    if errors:
        print("INVALID — behavioural_assay_go_map.yaml:")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print(f"VALID — behavioural_assay_go_map.yaml: {len(map_types)} assay types, "
          f"{len(entries)} GO-term refs ({len({e[1] for e in entries})} unique)"
          f"{' (QuickGO-verified)' if args.online else ' (offline checks only)'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
