"""Apply the manual membrane-row decisions (decisions_draft.py) to the gene reviews.

Rows whose decided action equals the current action are left untouched. For a changed
row, the action line is replaced and the reason is rewritten to the reviewer's basis plus a
dated provenance note naming the previous action; each edited file is re-parsed and
compared with the original parse, as in ../apply_dispositions.py.

Also writes decisions.yaml: one record per dossier row (decided action, previous action,
changed flag, basis), which is the reviewable output of this pass.

Usage:  python3 projects/OMICS_EVIDENCE/htp/membrane_review/apply_decisions.py [--write]
"""

from __future__ import annotations

import argparse
import copy
import os
import sys
from collections import Counter, defaultdict

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from apply_dispositions import LOADER, MEMBRANE, edit_file  # noqa: E402
from decisions_draft import D  # noqa: E402

NOTE = "(Manual re-review for OMICS_EVIDENCE, 2026-10-10; previous action: {old}.)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    dossiers = yaml.safe_load(open(os.path.join(HERE, "dossiers.yaml")))
    assert len(D) == len(dossiers) and set(D) == set(range(len(dossiers))), "decision for every dossier"
    records, per_file = [], defaultdict(list)
    for i, d in enumerate(dossiers):
        action, basis = D[i]
        changed = action != d["current_action"]
        records.append({"gene": f'{d["organism"]}/{d["gene"]}', "row_index": d["row_index"],
                        "reference": d["reference"], "previous_action": d["current_action"],
                        "decision": action, "changed": changed, "basis": basis})
        if changed:
            path = os.path.join(ROOT, "genes", d["organism"], d["gene"], f'{d["gene"]}-ai-review.yaml')
            per_file[path].append((d["row_index"], action, f"{basis} {NOTE.format(old=d['current_action'])}"))
    failed = []
    for path, changes in per_file.items():
        doc = yaml.load(open(path).read(), Loader=LOADER)
        for idx, _, _ in changes:
            assert doc["existing_annotations"][idx]["term"]["id"] == MEMBRANE, (path, idx)
        new_text = edit_file(path, changes)
        expect = copy.deepcopy(doc)
        for idx, act, rea in changes:
            expect["existing_annotations"][idx]["review"]["action"] = act
            expect["existing_annotations"][idx]["review"]["reason"] = rea
        if yaml.load(new_text, Loader=LOADER) != expect:
            failed.append(path)
            continue
        if args.write:
            open(path, "w").write(new_text)
    moves = Counter((r["previous_action"], r["decision"]) for r in records if r["changed"])
    print(f"{'WROTE' if args.write else 'DRY RUN'}: {sum(1 for r in records if r['changed'])} of "
          f"{len(records)} rows changed in {len(per_file) - len(failed)} files; failed: {len(failed)}")
    for (a, b), n in sorted(moves.items(), key=lambda kv: -kv[1]):
        print(f"  {a:24s} -> {b:24s} {n}")
    print("final decisions:", dict(Counter(r["decision"] for r in records)))
    if args.write:
        with open(os.path.join(HERE, "decisions.yaml"), "w") as fh:
            fh.write("# Manual review of HTP-family `membrane` rows, 2026-10-10. Source: decisions_draft.py\n")
            yaml.safe_dump(records, fh, sort_keys=False, width=120, allow_unicode=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
