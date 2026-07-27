"""Two corrections found by self-review, applied across every surface at once.

1. SCOPE THE SEARCH-DERIVED NEGATIVE. Four sites stated "no GAP assay has been
   reported / has ever been run" as a fact about the world. That is a statement
   about the sources consulted, not an existence claim, and the campaign has a
   recorded instance of exactly this promotion (a clade-wide "no coupling assay
   exists" refuted by two papers a narrower query missed). Reworded to attribute
   it: the family's consensus reference reports none, and a recorded query
   returned none.

2. REMOVE A STRUCTURED FIELD THAT ASSERTS A HEDGED CLAIM. core_functions[1] (the
   acrosome function) carried `molecular_function: GO:0000149 SNARE binding`
   while its own `knowledge_gaps[0]` states that whether the acrosomal role uses
   the VAMP7 interaction is undetermined. The slot asserted flatly what the prose
   hedged. The MF is dropped from that core function - it remains recorded as the
   MODIFY replacement term on the VAMP7 row, where it was actually measured.

Every anchor is asserted present before replacement, each replacement is asserted
to have landed, and the script refuses to run twice.

Usage: uv run python patch_selfreview.py [--pr-body PATH]
"""

from __future__ import annotations

import argparse
import pathlib

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
NOTES = HERE.parent / "AGFG1-notes.md"

# (path, old, new) - `old` must appear exactly once.
EDITS: list[tuple[pathlib.Path, str, str]] = [
    # 1a. top-level description
    (
        REVIEW,
        """  genetically required for Arf-dependent actomyosin contractility, but no GAP assay has
  been reported on either human AGFG protein.""",
        """  genetically required for Arf-dependent actomyosin contractility, while the family's
  consensus nomenclature reference reports no GAP measurement for either human AGFG
  protein.""",
    ),
    # 1b. GO:0005096 summary
    (
        REVIEW,
        """      interactome - but no GAP assay has ever been run on either human AGFG protein, and the
      family's own reference supplies a counterexample showing an intact motif does not
      imply activity.""",
        """      interactome - but the family's own reference reports no GAP measurement for either
      human AGFG protein, and it also supplies a counterexample showing that an intact motif
      does not imply activity.""",
    ),
    # 1c. GO:0005096 reason
    (
        REVIEW,
        """      ARF1, ARF3 and ARF6. What is absent: any GAP assay on human AGFG1 or AGFG2, and any
      identified substrate.""",
        """      ARF1, ARF3 and ARF6. What no source consulted here supplies is a GAP measurement on
      human AGFG1 or AGFG2, or an identified substrate: PMID:18809720's AGFG section reports
      neither, and a recorded Europe PMC query returned no such study. That is a statement
      about those sources and that query, not a proof that no assay exists.""",
    ),
    # 1d. notes
    (
        NOTES,
        """* no GAP assay has ever been reported on the human protein, and none on either human
  AGFG paralogue. `PMID:18809720`'s own AGFG section says only""",
        """* no GAP measurement on the human protein is reported by any source consulted here, and
  none for either human AGFG paralogue - a statement about those sources and about a
  recorded Europe PMC query, not an existence claim. `PMID:18809720`'s own AGFG section
  says only""",
    ),
    # 2. drop the MF that asserts a hedged claim, and say why in the description
    (
        REVIEW,
        """    is the same activity as the somatic one seen in a different compartment - selection and
    retention of SNARE-bearing vesicles - which is why the SNARE-binding function is listed
    here rather than a second adaptor activity.
  molecular_function:
    id: GO:0000149
    label: SNARE binding
  directly_involved_in:""",
        """    may be the same activity as the somatic one operating in a different compartment -
    selection and retention of SNARE-bearing vesicles - but that has not been tested, so no
    molecular function is asserted for this core function. The SNARE-binding activity is
    recorded on the VAMP7 row, where it was measured.
  directly_involved_in:""",
    ),
]

PR_EDITS: list[tuple[str, str]] = [
    (
        """GOA and from the affinage record). What is absent: any GAP assay on either human AGFG
protein.""",
        """GOA and from the affinage record). What no source consulted supplies is a GAP measurement
on either human AGFG protein or an identified substrate - a statement about those sources
and about a recorded Europe PMC query, not a proof that no assay exists.""",
    ),
]

DONE_MARKER = "consensus nomenclature reference reports no GAP measurement"


def apply(path: pathlib.Path, pairs: list[tuple[str, str]]) -> int:
    text = path.read_text()
    n = 0
    for old, new in pairs:
        count = text.count(old)
        assert count == 1, f"{path.name}: anchor found {count} times:\n{old}"
        text = text.replace(old, new, 1)
        assert new in text, f"{path.name}: replacement did not land"
        assert text.count(old) == 0, f"{path.name}: anchor survived"
        n += 1
    path.write_text(text)
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pr-body", type=pathlib.Path)
    args = ap.parse_args()

    if DONE_MARKER in REVIEW.read_text():
        print("already patched; nothing to do")
    else:
        by_file: dict[pathlib.Path, list[tuple[str, str]]] = {}
        for path, old, new in EDITS:
            by_file.setdefault(path, []).append((old, new))
        total = 0
        for path, pairs in by_file.items():
            k = apply(path, pairs)
            print(f"{path.name}: {k} edit(s) applied")
            total += k
        assert total == len(EDITS), f"applied {total} of {len(EDITS)} edits"
        # Post-condition on edit 2, checked through the parser rather than by
        # matching an indentation form - a first version of this assertion looked
        # for the 4-space core_functions layout and could therefore never pass
        # once the MF had been removed, which is a check that guards nothing.
        import yaml

        doc = yaml.safe_load(REVIEW.read_text())
        cf_mfs = [
            cf.get("molecular_function", {}).get("id")
            for cf in doc["core_functions"]
        ]
        assert "GO:0000149" not in cf_mfs, (
            f"GO:0000149 is still a core_functions molecular_function: {cf_mfs}"
        )
        repl = [
            t["id"]
            for a in doc["existing_annotations"]
            for t in ((a.get("review") or {}).get("proposed_replacement_terms") or [])
        ]
        assert repl.count("GO:0000149") == 1, (
            f"GO:0000149 should remain exactly one proposed replacement term: {repl}"
        )
        print(f"{total} edits applied across {len(by_file)} file(s)")

    if args.pr_body:
        if DONE_MARKER.split(" reports")[0] in args.pr_body.read_text() or (
            "What no source consulted supplies" in args.pr_body.read_text()
        ):
            print("PR body already patched")
        else:
            k = apply(args.pr_body, PR_EDITS)
            print(f"{args.pr_body.name}: {k} edit(s) applied")


if __name__ == "__main__":
    main()
