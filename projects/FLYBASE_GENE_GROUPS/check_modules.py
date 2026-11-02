#!/usr/bin/env python3
"""Check generated FlyBase-group modules against the triage.

For every module that the triage marks NEW_MODULE, report:

* whether ``modules/<module>.yaml`` exists;
* whether the root decomposes into at least two parts or variants;
* FlyBase member genes (of the realized groups and their subsumed subgroups,
  excluding regulator sets) that do not appear in the module, matched by
  UniProtKB accession or FlyBase gene id. A gene is accepted as deliberately
  left out if its symbol is mentioned in the spec's ``notes``.

Writes ``module_coverage.yaml`` and exits non-zero if a module is missing or
fails the decomposition rule.

Usage (from the repository root)::

    uv run python projects/FLYBASE_GENE_GROUPS/check_modules.py
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

HERE = Path(__file__).parent


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("-o", "--output", type=Path, default=HERE / "module_coverage.yaml")
    args = ap.parse_args()
    index = yaml.safe_load((HERE / "group_index.yaml").read_text())
    triage = yaml.safe_load((HERE / "group_triage.yaml").read_text())
    groups = {g["id"]: g for g in index["groups"]}
    genes = index["genes"]
    decision = {r["id"]: r for r in triage["groups"]}

    def members(gid: str) -> set[str]:
        if decision[gid]["decision"] == "REGULATOR_SET":
            return set()
        out = set(groups[gid]["direct_members"])
        for c in groups[gid]["children"]:
            if decision[c].get("module") == decision[gid].get("module"):
                out |= members(c)
        return out

    modules: dict[str, set[str]] = {}
    for r in triage["groups"]:
        if r["decision"] == "NEW_MODULE":
            modules.setdefault(r["module"], set()).update(members(r["id"]))

    report, bad = [], 0
    for mod in sorted(modules):
        path = Path("modules") / f"{mod}.yaml"
        rec = {"module": mod, "n_flybase_members": len(modules[mod])}
        if not path.exists():
            rec["status"] = "MISSING"
            bad += 1
            report.append(rec)
            continue
        text = path.read_text()
        doc = yaml.safe_load(text)
        root = doc["module"]
        n_parts = len(root.get("parts") or [])
        n_vars = sum(len(v.get("variants") or []) for v in root.get("variant_sets") or [])
        spec_path = HERE / "module_specs" / f"{mod}.yaml"
        spec_notes = ""
        if spec_path.exists():
            spec_notes = str((yaml.safe_load(spec_path.read_text()) or {}).get("notes", ""))
        ids = set(re.findall(r"UniProtKB:(\w+)", text)) | set(re.findall(r"FB:(FBgn\d+)", text))
        missing, excluded = [], []
        for fbgn in sorted(modules[mod]):
            g = genes[fbgn]
            if g["uniprot"] in ids or fbgn in ids:
                continue
            if re.search(rf"(?<![\w-]){re.escape(g['symbol'])}(?![\w-])", spec_notes):
                excluded.append(g["symbol"])
            else:
                missing.append(g["symbol"])
        rec.update({"n_parts": n_parts, "n_variants": n_vars,
                    "n_uniprot_participants": len(set(re.findall(r"UniProtKB:(\w+)", text)))})
        if excluded:
            rec["excluded_with_note"] = excluded
        if missing:
            rec["missing_members"] = missing
        ok = n_parts >= 2 or n_vars >= 2
        rec["status"] = "OK" if ok and not missing else ("FAIL_DECOMPOSITION" if not ok else "INCOMPLETE")
        if not ok:
            bad += 1
        report.append(rec)
    statuses = {}
    for r in report:
        statuses[r["status"]] = statuses.get(r["status"], 0) + 1
    args.output.write_text(yaml.safe_dump({"summary": statuses, "modules": report},
                                          sort_keys=False, width=100))
    print(statuses)
    for r in report:
        if r["status"] != "OK":
            print(r["module"], r["status"], r.get("missing_members", ""))
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
