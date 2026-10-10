"""Apply the manual vesicle-row decisions to the gene reviews.

Pass 1 (default): decisions_draft.py over dossiers.yaml, writing decisions.yaml.
Pass 2 (--settled): decisions_settled.py over dossiers_settled.yaml, writing
decisions_settled.yaml.

A decisions module supplies G (one decision per protein), and may supply SUPERSEDED
(genes whose rows a later, separate review has taken over; recorded but not edited), R (per-row
overrides keyed by (gene, row_index), for proteins whose rows need different calls or
row-specific wording) and S (supported_by entries, by reference_id, to drop from a row
because they argued for the action this review overturned).

A row whose decision differs from its pre-review action gets the decision, a reason made
of the reviewer's basis plus a dated provenance note, a summary matching the decision, and
the S drops. A row whose decision equals its pre-review action but which an earlier run of
this script changed is restored to its pre-review action and reason. Re-running is a no-op;
the mechanics (textual edit, parse check) are in ../apply_dispositions.py.

Usage:  python3 projects/OMICS_EVIDENCE/htp/vesicle_review/apply_decisions.py [--settled] [--write]
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
from apply_dispositions import LOADER, VESICLE_TERMS, apply_row_targets  # noqa: E402

NOTE = "(Manual re-review for OMICS_EVIDENCE, 2026-10-10; previous action: {old}.)"
MARKER = "Manual re-review for OMICS_EVIDENCE, 2026-10-10"
SUMMARY = {
    "KEEP_AS_NON_CORE": "Detected in an extracellular-vesicle proteome. The protein is plausible EV content, "
                        "but this is not where it functions.",
    "MARK_AS_OVER_ANNOTATED": "Detected in an extracellular-vesicle proteome, but the detection does not "
                              "establish that this protein is an EV constituent.",
    "ACCEPT": "The protein is an established EV marker incorporated by the EV biogenesis machinery; the "
              "vesicle location is supported.",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--settled", action="store_true", help="second pass: rows already KEEP_AS_NON_CORE")
    args = ap.parse_args()
    if args.settled:
        import decisions_settled as dm
        dossier_file, out_file, source = "dossiers_settled.yaml", "decisions_settled.yaml", "decisions_settled.py"
    else:
        import decisions_draft as dm
        dossier_file, out_file, source = "dossiers.yaml", "decisions.yaml", "decisions_draft.py"
    G, R, S = dm.G, getattr(dm, "R", {}), getattr(dm, "S", {})
    superseded = getattr(dm, "SUPERSEDED", {})
    dossiers = yaml.safe_load(open(os.path.join(HERE, dossier_file)))
    genes = {d["gene"] for d in dossiers}
    assert genes == set(G), f"missing: {genes - set(G)}; extra: {set(G) - genes}"
    rows = {(d["gene"], d["row_index"]) for d in dossiers}
    assert set(R) <= rows and set(S) <= rows, "overrides must name dossier rows"
    records, targets, parsed = [], defaultdict(list), {}
    for d in dossiers:
        key = (d["gene"], d["row_index"])
        action, basis = R.get(key, G[d["gene"]])
        old = d["current_action"]
        changed = action != old
        records.append({"gene": f'{d["organism"]}/{d["gene"]}', "row_index": d["row_index"], "term": d["term"],
                        "reference": d["reference"], "previous_action": old,
                        "decision": action, "changed": changed, "basis": basis})
        if d["gene"] in superseded:
            records[-1]["superseded_by"] = superseded[d["gene"]]
            continue
        path = os.path.join(ROOT, "genes", d["organism"], d["gene"], f'{d["gene"]}-ai-review.yaml')
        if path not in parsed:
            parsed[path] = yaml.load(open(path).read(), Loader=LOADER)["existing_annotations"]
        ann = parsed[path][d["row_index"]]
        assert ann["term"]["id"] in VESICLE_TERMS, (path, d["row_index"])
        rv = ann["review"]
        if changed:
            targets[path].append((d["row_index"], action, f"{basis} {NOTE.format(old=old)}",
                                  SUMMARY[action], set(S.get(key, []))))
        elif MARKER in str(rv.get("reason") or ""):
            # changed by an earlier run, now decided back to the pre-review action
            targets[path].append((d["row_index"], old, d["current_reason"], rv.get("summary"), set()))
    edited, failed = apply_row_targets(targets, args.write)
    moves = Counter((r["previous_action"], r["decision"]) for r in records if r["changed"])
    print(f"{'WROTE' if args.write else 'DRY RUN'}: {sum(1 for r in records if r['changed'])} of "
          f"{len(records)} rows differ from their pre-review action; {edited} files needed edits; "
          f"failed: {len(failed)}")
    for (a, b), n in sorted(moves.items(), key=lambda kv: -kv[1]):
        print(f"  {a:24s} -> {b:24s} {n}")
    print("final decisions:", dict(Counter(r["decision"] for r in records)))
    if args.write:
        with open(os.path.join(HERE, out_file), "w") as fh:
            fh.write(f"# Manual review of HTP-family vesicle-type rows, 2026-10-10. Source: {source}\n")
            yaml.safe_dump(records, fh, sort_keys=False, width=120, allow_unicode=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
