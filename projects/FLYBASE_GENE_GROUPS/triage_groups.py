#!/usr/bin/env python3
"""Apply the curated triage rules to every FlyBase gene group.

Reads ``group_index.yaml`` (from ``build_group_index.py``) and the hand-curated
``triage_rules.yaml`` and writes ``group_triage.yaml``: one record per FlyBase
group with its decision, the module that realizes it (if any) and the reason.

Groups without an explicit rule inherit from their nearest ruled ancestor. A
module decision makes the descendant SUBSUMED into the same module. A group
with several parents takes the first module-bearing inherited decision, else
the first inherited decision. Groups left without any decision are reported as
UNTRIAGED so that gaps in the rules are visible.

The script fails if a rule names an unknown or ambiguous group symbol, or if an
EXISTING_MODULE rule names a module file that does not exist.

Usage (from the repository root)::

    uv run python projects/FLYBASE_GENE_GROUPS/triage_groups.py
"""

from __future__ import annotations

import argparse
import collections
from pathlib import Path

import yaml

HERE = Path(__file__).parent
MODULE_DECISIONS = {"NEW_MODULE", "EXISTING_MODULE"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--index", type=Path, default=HERE / "group_index.yaml")
    ap.add_argument("--rules", type=Path, default=HERE / "triage_rules.yaml")
    ap.add_argument("--modules-dir", type=Path, default=Path("modules"))
    ap.add_argument("-o", "--output", type=Path, default=HERE / "group_triage.yaml")
    args = ap.parse_args()

    index = yaml.safe_load(args.index.read_text())
    groups = {g["id"]: g for g in index["groups"]}
    by_symbol: dict[str, list[str]] = collections.defaultdict(list)
    for g in index["groups"]:
        by_symbol[g["symbol"]].append(g["id"])

    explicit: dict[str, dict] = {}
    errors = []
    for rule in yaml.safe_load(args.rules.read_text()):
        for sym in rule["groups"]:
            ids = by_symbol.get(sym, [])
            if len(ids) != 1:
                errors.append(f"rule symbol {sym!r} matches {len(ids)} groups")
                continue
            if ids[0] in explicit:
                errors.append(f"group {sym} has more than one rule")
            explicit[ids[0]] = {k: v for k, v in rule.items() if k != "groups"}
        if rule["decision"] == "EXISTING_MODULE":
            if not (args.modules_dir / f"{rule['module']}.yaml").exists():
                errors.append(f"existing module {rule['module']} not found")
    if errors:
        raise SystemExit("\n".join(errors))

    memo: dict[str, dict | None] = {}

    def decide(gid: str, seen: frozenset = frozenset()) -> dict | None:
        if gid in memo:
            return memo[gid]
        if gid in explicit:
            memo[gid] = dict(explicit[gid], inherited_from=None)
            return memo[gid]
        inherited = []
        for pid in groups[gid]["parents"]:
            if pid in groups and pid not in seen:
                d = decide(pid, seen | {gid})
                if d is not None:
                    inherited.append((pid, d))
        result = None
        for pid, d in inherited:
            if d["decision"] in MODULE_DECISIONS or d["decision"] == "SUBSUMED":
                result = {"decision": "SUBSUMED", "module": d["module"],
                          "inherited_from": groups[pid]["symbol"]}
                break
        if result is None and inherited:
            pid, d = inherited[0]
            if d["decision"] == "UMBRELLA":
                result = None
            else:
                result = dict(d, inherited_from=groups[pid]["symbol"])
        memo[gid] = result
        return result

    records = []
    for gid in sorted(groups):
        g = groups[gid]
        d = decide(gid) or {"decision": "UNTRIAGED"}
        rec = {
            "id": gid,
            "symbol": g["symbol"],
            "name": g["name"],
            "source": g["sources"][0],
            "n_members": g["n_subtree_members"],
            "decision": d["decision"],
        }
        for key in ("module", "reason_code", "reason", "note", "inherited_from"):
            if d.get(key):
                rec[key] = d[key]
        records.append(rec)

    counts = collections.Counter(r["decision"] for r in records)
    new_modules = sorted({r["module"] for r in records if r["decision"] == "NEW_MODULE"})
    existing = sorted({r["module"] for r in records if r["decision"] == "EXISTING_MODULE"})
    doc = {
        "release": index["release"],
        "n_groups": len(records),
        "decision_counts": dict(sorted(counts.items())),
        "n_new_modules": len(new_modules),
        "n_existing_modules": len(existing),
        "groups": records,
    }
    args.output.write_text(yaml.safe_dump(doc, sort_keys=False, width=100))
    print(f"wrote {args.output}")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    print(f"  new modules: {len(new_modules)}, existing modules: {len(existing)}")
    untriaged = [r for r in records if r["decision"] == "UNTRIAGED"]
    for r in untriaged:
        print(f"  UNTRIAGED {r['symbol']} {r['name']} ({r['n_members']})")


if __name__ == "__main__":
    main()
