"""Apply the manual membrane-row decisions (decisions_draft.py) to the gene reviews.

Rows whose decided action equals the pre-review action are left untouched. For a changed
row, the action line is replaced, the reason is rewritten to the reviewer's basis plus a
dated provenance note naming the previous action, and the summary is replaced with one
matching the decision. Re-running is a no-op; each edited file is re-parsed and compared
with the original parse (apply_row_targets in ../apply_dispositions.py).

Also writes decisions.yaml: one record per dossier row (decided action, previous action,
changed flag, basis), which is the reviewable output of this pass.

Usage:  python3 projects/OMICS_EVIDENCE/htp/membrane_review/apply_decisions.py [--write]
"""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter, defaultdict

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from apply_dispositions import LOADER, MEMBRANE, apply_row_targets  # noqa: E402
from decisions_draft import D  # noqa: E402

NOTE = "(Manual re-review for OMICS_EVIDENCE, 2026-10-10; previous action: {old}.)"
SUMMARY = {
    "KEEP_AS_NON_CORE": "Membrane association is documented for this protein, so the generic membrane "
                        "term is true, but it is not the protein's core location.",
    "MARK_AS_OVER_ANNOTATED": "Recovered in a membrane-fraction proteome without protein-specific evidence "
                              "that it associates with membranes.",
    "REMOVE": "No credible membrane association for this protein; the generic membrane term is not supported.",
    "ACCEPT": "Membrane association is central to this protein's activity.",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    dossiers = yaml.safe_load(open(os.path.join(HERE, "dossiers.yaml")))
    assert len(D) == len(dossiers) and set(D) == set(range(len(dossiers))), "decision for every dossier"
    records, targets = [], defaultdict(list)
    for i, d in enumerate(dossiers):
        action, basis = D[i]
        changed = action != d["current_action"]
        records.append({"gene": f'{d["organism"]}/{d["gene"]}', "row_index": d["row_index"],
                        "reference": d["reference"], "previous_action": d["current_action"],
                        "decision": action, "changed": changed, "basis": basis})
        if changed:
            path = os.path.join(ROOT, "genes", d["organism"], d["gene"], f'{d["gene"]}-ai-review.yaml')
            targets[path].append((d["row_index"], action, f"{basis} {NOTE.format(old=d['current_action'])}",
                                  SUMMARY[action], set()))
    for path, rows in targets.items():
        doc = yaml.load(open(path).read(), Loader=LOADER)
        for idx, *_ in rows:
            assert doc["existing_annotations"][idx]["term"]["id"] == MEMBRANE, (path, idx)
    edited, failed = apply_row_targets(targets, args.write)
    moves = Counter((r["previous_action"], r["decision"]) for r in records if r["changed"])
    print(f"{'WROTE' if args.write else 'DRY RUN'}: {sum(1 for r in records if r['changed'])} of "
          f"{len(records)} rows differ from their pre-review action; {edited} files needed edits; "
          f"failed: {len(failed)}")
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
