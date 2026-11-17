"""Report PseudoCAP shared claims whose members were reviewed inconsistently.

A *shared claim* is one GO term asserted on several proteins by one reference --
a complex, an operon, or a pair of paralogues assayed in the same paper. The
worklist builder (``build_pseudocap_mf_worklist.py``) emits these as
``shared_claims``. One paper asserting one term across several proteins is
normally one judgement, so the reviews of those proteins should reach the same
verdict, or say why they differ.

They drift apart easily, because the members are usually reviewed in different
sittings. Two cases found so far:

- ``liuB``/``liuD`` (PR #6341): the same claim was ``ACCEPT`` on one and
  ``TOO_GENERAL`` on the other, and after the fix one review's prose still
  described the other's superseded verdict.
- ``wbpX``/``wbpY``: ``wbpY`` refined the term citing direct enzymology for both
  enzymes, while ``wbpX`` accepted the generic term saying that very evidence did
  not exist, and never cited the paper.

Divergence is not automatically a defect. ``ccoQ1``/``ccoQ2`` diverge from the
other cbb3 subunits because they are accessory chains absent from the cryo-EM
models, and ``tse6`` diverges from ``tsi6`` because of a recorded
``WRONG_GENE_PRODUCT`` defect. Both are deliberate and argued in the rows. This
script finds candidates to read; it does not decide them.

Groups with an unreviewed member are reported separately: those cannot diverge
yet, but they are where divergence will appear once the member is reviewed.

**Scope: molecular function only.** ``WORKLIST`` below is the MF worklist, which
the builder fills by selecting IMP rows on molecular-function terms, so every
shared claim this script can see is an MF claim. A clean run therefore does not
mean a pair agrees -- only that it agrees about molecular function.

This is a real gap, not a theoretical one. ``wbpX`` and ``wbpY`` also share
``GO:0009103`` lipopolysaccharide biosynthetic process from the same reference
(PMID:9680202), and they were reviewed ``TOO_GENERAL`` and ``MODIFY`` respectively
with no argument for the difference -- drift of exactly the kind this script
exists to find, which it could not see because the term is a biological process.
It was caught by a reviewer reading the diff. Widening the audit means building a
process-aspect worklist (the builder takes ``--all-aspects``) and pointing
``WORKLIST`` at it, or reading shared claims from GOA directly.

Usage::

    uv run python projects/PSEUDOCAP/check_shared_claim_consistency.py
    uv run python projects/PSEUDOCAP/check_shared_claim_consistency.py --quiet
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKLIST = Path(__file__).resolve().parent / "pseudocap_mf_worklist.yaml"
GENES = ROOT / "genes" / "PSEAE"


def actions_for_term(folder: str, term_id: str) -> list[str]:
    """Return the sorted distinct review verdicts on ``term_id`` in a gene review.

    A verdict is the action, plus the replacement term where the action is
    MODIFY: two members that both MODIFY but to *different* terms have not
    reached the same judgement, and comparing bare actions would call them
    consistent. ``wbpL`` and ``wbpY`` are the worked example -- both once read
    MODIFY on ``GO:0016757``, but ``wbpL`` moves to ``GO:0016780``
    phosphotransferase activity, a different reaction class, because it is a
    WecA-type initiating enzyme rather than a glycosyltransferase.

    Three empty-ish results are kept distinct, because they mean different things
    and conflating them would report "no row" for a review that is simply not
    there: ``["(no review file)"]`` when the review does not exist, against
    ``["(no row)"]`` when it exists but says nothing about the term -- the
    latter being worth seeing, since the claim is in GOA for the gene and absent
    from its review. ``["(only a NEW row)"]`` is the third: the review addresses
    the term, but only to propose an annotation GOA lacks, so there is no verdict
    on the shared claim to compare and reporting silence would be wrong.

    ``NEW`` rows are deliberately excluded. A ``NEW`` row proposes an annotation
    GOA does not have, so it is an addition rather than a verdict on the shared
    claim, and counting it would make a member that proposes an extra row look
    as though it disagreed about the existing one. The exclusion only bites when
    a ``NEW`` row sits on the shared term itself; the usual case, as with the
    ``GO:0016758`` rows on ``wbpX`` and ``wbpY``, puts it on a different term
    that no shared claim names.
    """
    path = GENES / folder / f"{folder}-ai-review.yaml"
    if not path.exists():
        return ["(no review file)"]
    with open(path, encoding="utf-8") as handle:
        doc = yaml.safe_load(handle)
    verdicts = set()
    skipped_new = False
    for row in doc.get("existing_annotations") or []:
        if row.get("term", {}).get("id") != term_id:
            continue
        review = row.get("review") or {}
        action = review.get("action")
        if not action:
            continue
        if action == "NEW":
            skipped_new = True
            continue
        replacements = sorted(
            term.get("id", "?")
            for term in review.get("proposed_replacement_terms") or []
            if term.get("id")
        )
        verdicts.add(f"{action}->{'+'.join(replacements)}" if replacements else action)
    if verdicts:
        return sorted(verdicts)
    # Excluding NEW rows created a third empty case, distinct from the other two:
    # the review does discuss this term, but only to propose an annotation GOA
    # lacks. Reporting that as "(no row)" would say the review is silent about a
    # claim it in fact addresses.
    return ["(only a NEW row)"] if skipped_new else ["(no row)"]


def collect() -> dict[str, list[dict[str, Any]]]:
    """Split shared-claim groups into divergent, consistent and incomplete."""
    with open(WORKLIST, encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    reviewed = {entry["symbol"]: entry["review_folder"] for entry in data["genes"]}

    out: dict[str, list[dict[str, Any]]] = {
        "divergent": [],
        "consistent": [],
        "incomplete": [],
    }
    for group in data.get("shared_claims") or []:
        symbols = group["symbols"]
        folders = {s: reviewed.get(s) for s in symbols}
        record = {"term": group["term"], "reference": group["reference"]}

        missing = [s for s, f in folders.items() if not f]
        if missing:
            record["unreviewed"] = missing
            record["reviewed"] = [s for s in symbols if folders[s]]
            out["incomplete"].append(record)
            continue

        # Every folder is non-None here: the missing ones took the branch above.
        actions = {
            s: actions_for_term(str(f), group["term"]) for s, f in folders.items()
        }

        # Two kinds of member cannot be compared on this claim, and neither is a
        # disagreement about it: one whose review file is missing, and one whose
        # only row on the term is a NEW proposal, which rules on nothing. Both
        # join the incomplete cases. Leaving either in the comparison would make
        # a single such member read as divergence, and a group where every member
        # is like that read as agreement on a claim nobody ruled on.
        absent = [
            s
            for s, v in actions.items()
            if v in (["(no review file)"], ["(only a NEW row)"])
        ]
        if absent:
            record["unreviewed"] = absent
            record["reviewed"] = [s for s in symbols if s not in absent]
            out["incomplete"].append(record)
            continue

        record["actions"] = actions
        bucket = (
            "divergent"
            if len({tuple(v) for v in actions.values()}) > 1
            else "consistent"
        )
        out[bucket].append(record)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print only divergent groups and the summary counts",
    )
    args = parser.parse_args()

    groups = collect()

    def show(record: dict[str, Any]) -> str:
        pairs = ", ".join(f"{s}={'/'.join(a)}" for s, a in record["actions"].items())
        return f"  {record['term']:13} {record['reference']:16} {pairs}"

    if groups["divergent"]:
        print("DIVERGENT -- members of one shared claim reviewed differently:")
        for record in groups["divergent"]:
            print(show(record))
        print()
        print("  Read each before changing anything: a divergence can be deliberate")
        print("  (an accessory subunit, a recorded source defect). If it is, the rows")
        print("  should already say so; if they do not, that is the thing to fix.")
    else:
        print("No divergent shared claims.")

    if not args.quiet:
        if groups["incomplete"]:
            print()
            print("INCOMPLETE -- groups with an unreviewed member:")
            for record in groups["incomplete"]:
                print(
                    f"  {record['term']:13} {record['reference']:16} "
                    f"reviewed={record['reviewed']} unreviewed={record['unreviewed']}"
                )
        if groups["consistent"]:
            print()
            print("CONSISTENT:")
            for record in groups["consistent"]:
                print(show(record))

    print()
    print(
        f"summary: {len(groups['divergent'])} divergent, "
        f"{len(groups['consistent'])} consistent, "
        f"{len(groups['incomplete'])} incomplete"
    )
    print(
        "scope: molecular-function shared claims only; process and component claims are not checked"
    )
    # Divergence is a prompt to read, not a build failure: always exit 0.
    return 0


if __name__ == "__main__":
    sys.exit(main())
