"""Reconcile the ARHGAP11B review's entry count and action tally against the GOA TSV.

Hand-maintained counts drift. This one did: the first hand tally said ACCEPT 12 and wrote
the arithmetic as ``12 + 2 + 4 = 18``, which also came to 18 -- because it had dropped the
NEW row from the sum at the same moment as inflating ACCEPT by one, so two errors cancelled
into a total that looked reconciled. The true tally is ACCEPT 11, MODIFY 2, REMOVE 4, NEW 1.
The wrong figure reached the commit message and the PR body before this script was run.

So the numbers quoted in the notes and the PR body are produced here, not counted by eye.

Checks:
  1. non-NEW entries == GOA TSV rows (missing coverage, or a stub that collapsed rows)
  2. raw ``- term:`` lines == parsed entries, and a strict loader rejects duplicate YAML
     keys -- PyYAML keeps the LAST occurrence of a duplicated key and discards the earlier
     one silently, so data can vanish before any parsed-document check can see it
  3. no annotation left PENDING, and every action is a schema-permitted value
  4. no EXPERIMENTAL annotation was removed or demoted
  5. every REMOVE/MARK on a propagated evidence code carries a propagation_review

Usage:
    uv run python check_review_counts.py
    uv run python check_review_counts.py --self-test
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml


class StrictLoader(yaml.SafeLoader):
    pass


def _no_dupes(loader, node, deep=False):
    out = {}
    for k_node, v_node in node.value:
        k = loader.construct_object(k_node, deep=deep)
        if k in out:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {k!r}", k_node.start_mark
            )
        out[k] = loader.construct_object(v_node, deep=deep)
    return out


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dupes)

def repo_root() -> Path:
    """Derive the root; never assert it.

    A shared script in this campaign once hardcoded one agent's worktree path and then
    reported 56 false failures against another's clean file. Walking up from this file's
    own location is correct from any worktree and from any cwd.
    """
    here = Path(__file__).resolve()
    for cand in here.parents:
        if (cand / "src").is_dir() and (cand / "genes").is_dir():
            return cand
    raise SystemExit("could not locate the repo root (need a dir containing src/ and genes/)")


ROOT = repo_root()
GENE_DIR = ROOT / "genes/human/ARHGAP11B"
REVIEW_PATH = GENE_DIR / "ARHGAP11B-ai-review.yaml"
GOA_PATH = GENE_DIR / "ARHGAP11B-goa.tsv"
SCHEMA_PATH = ROOT / "src/ai_gene_review/schema/gene_review.yaml"


def load(review_text: str | None = None) -> tuple[str, dict, int, set[str]]:
    for p in (REVIEW_PATH, GOA_PATH, SCHEMA_PATH):
        if not p.exists():
            raise SystemExit(f"missing input: {p} (run `just fetch-gene human ARHGAP11B`)")
    raw_text = REVIEW_PATH.read_text() if review_text is None else review_text
    parsed = yaml.load(raw_text, Loader=StrictLoader)
    with GOA_PATH.open() as fh:
        goa_rows = len(list(csv.DictReader(fh, delimiter="\t")))
    schema_doc = yaml.safe_load(SCHEMA_PATH.read_text())
    return raw_text, parsed, goa_rows, set(schema_doc["enums"]["ActionEnum"]["permissible_values"])


EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
# Evidence codes whose annotations are transferred or asserted rather than measured on
# this gene, so a REMOVE/MARK on one owes an explanation of the propagation.
NEEDS_PROP = {"IBA", "ISS", "ISO", "IEA", "TAS", "RCA", "IGC", "NAS"}


def check(review_text: str | None = None, quiet: bool = False) -> list[str]:
    """Return a list of problems. Never raises from inside a check.

    A check that raises aborts every later check, including a self-test baseline, while
    the harness still prints as though it ran. Collect and let the caller decide.
    """
    raw_text, doc, n_goa, permitted = load(review_text)
    anns = doc["existing_annotations"]
    actions = Counter(a["review"]["action"] for a in anns)
    n_new = actions.get("NEW", 0)
    n_from_goa = len(anns) - n_new

    # Anchored to a whole line so nested '- term:' inside proposed_replacement_terms
    # (which is indented) is excluded. Any substring test on a controlled vocabulary
    # needs an anchor.
    raw_terms = len(re.findall(r"^- term:$", raw_text, flags=re.M))

    problems: list[str] = []
    if n_from_goa != n_goa:
        problems.append(
            f"entry/GOA mismatch: {n_goa} GOA rows vs {n_from_goa} non-NEW entries "
            "(missing coverage, or a stub that collapsed rows)"
        )
    if raw_terms != len(anns):
        problems.append(f"raw '- term:' lines {raw_terms} != parsed entries {len(anns)}")
    if sum(actions.values()) != len(anns):
        problems.append("action tally does not sum to the entry count")
    if "PENDING" in actions:
        problems.append(f"{actions['PENDING']} entries still PENDING")
    bad = set(actions) - permitted
    if bad:
        problems.append(f"actions not in ActionEnum: {sorted(bad)}")

    touched_exp = [
        f"{a['term']['id']} {a['evidence_type']} -> {a['review']['action']}"
        for a in anns
        if a["review"]["action"] in {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
        and a.get("evidence_type") in EXPERIMENTAL
    ]
    if touched_exp:
        problems.append(f"experimental annotation removed/demoted: {touched_exp}")

    missing_prop = [
        f"{a['term']['id']} {a['evidence_type']}"
        for a in anns
        if a["review"]["action"] in {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
        and a.get("evidence_type") in NEEDS_PROP
        and not a["review"].get("propagation_review")
    ]
    if missing_prop:
        problems.append(f"REMOVE/MARK without propagation_review: {missing_prop}")

    if not quiet:
        print(f"GOA TSV rows            : {n_goa}")
        print(f"existing_annotations    : {len(anns)}  (raw '- term:' lines {raw_terms})")
        print(f"  of which NEW          : {n_new}")
        print(f"  derived from GOA      : {n_from_goa}")
        print("action tally:")
        for a, n in sorted(actions.items()):
            print(f"  {a:<22} {n}")
        summed = " + ".join(str(n) for _, n in sorted(actions.items()))
        print(f"sum of actions          : {summed} = {sum(actions.values())} "
              f"= {n_goa} GOA + {n_new} NEW")
        print(f"experimental rows removed or demoted        : {len(touched_exp)}")
        print(f"REMOVE/MARK rows lacking propagation_review : {len(missing_prop)}")
    return problems


def self_test() -> int:
    """Break each check on purpose and require it to notice.

    Each mutation asserts its anchor is present BEFORE mutating, so a mutation whose
    target string has drifted is an error rather than a vacuous pass. A passing self-test
    only proves the guards that were written fire; it says nothing about the guard that
    was never written.
    """
    failures: list[str] = []
    base = check(quiet=True)
    if base:
        failures.append(f"baseline is not clean, so no mutation result is meaningful: {base}")

    original = REVIEW_PATH.read_text()

    def mutate(name: str, anchor: str, replacement: str, expect: str, count: int = 1) -> None:
        if anchor not in original:
            failures.append(f"{name}: anchor {anchor!r} not present; mutation would be vacuous")
            return
        broken = original.replace(anchor, replacement, count)
        if broken == original:
            failures.append(f"{name}: mutation was a no-op")
            return
        try:
            got = check(review_text=broken, quiet=True)
        except yaml.YAMLError as exc:
            got = [f"yaml error: {exc}"]
        if not any(expect in g for g in got):
            failures.append(f"{name}: expected a problem containing {expect!r}, got {got}")

    # M1 the entry-count reconciliation must fire when the NEW/GOA split is wrong.
    # Deleting a block is a poor mutation here -- it leaves dangling YAML and the loader
    # raises before the check under test can run, which would prove nothing. Reclassifying
    # the NEW row as ACCEPT is a one-token change that leaves the document valid and makes
    # the non-NEW count 18 against 17 GOA rows.
    mutate("M1 NEW row reclassified", "    action: NEW", "    action: ACCEPT",
           "entry/GOA mismatch")

    # M2 an un-reviewed row must be caught
    mutate("M2 PENDING left behind", "    action: ACCEPT", "    action: PENDING", "still PENDING")

    # M3 an action outside the enum must be caught
    mutate("M3 bogus action", "    action: ACCEPT", "    action: DEFINITELY_NOT_AN_ACTION",
           "not in ActionEnum")

    # M4 removing an experimental annotation must be caught. Anchor on the IDA row for
    # GO:0021987 from PMID:33938018 by flipping its action.
    ida_accept = (
        "  evidence_type: IDA\n  original_reference_id: PMID:33938018\n"
        "  qualifier: involved_in\n  review:\n"
    )
    if ida_accept in original:
        broken = original.replace(ida_accept, ida_accept, 1)
        idx = broken.index(ida_accept) + len(ida_accept)
        tail = broken[idx:]
        if "    action: ACCEPT" in tail:
            tail2 = tail.replace("    action: ACCEPT", "    action: REMOVE", 1)
            got = check(review_text=broken[:idx] + tail2, quiet=True)
            if not any("experimental annotation removed" in g for g in got):
                failures.append(f"M4: removing an IDA row was not flagged; got {got}")
        else:
            failures.append("M4: could not find the ACCEPT action after the anchor")
    else:
        failures.append("M4: anchor for the PMID:33938018 IDA row drifted")

    # M5 a duplicate YAML key must be rejected by the strict loader, not silently absorbed
    dup_anchor = "id: Q3KRB8\ngene_symbol: ARHGAP11B\n"
    mutate("M5 duplicate key", dup_anchor, dup_anchor + "gene_symbol: ARHGAP11B\n",
           "duplicate key")

    for line in failures:
        print("SELF-TEST FAIL:", line)
    if not failures:
        print("SELF-TEST: all 5 mutations were caught")
    return 1 if failures else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    found = check()
    if found:
        print("\nPROBLEMS:")
        for item in found:
            print("  -", item)
        sys.exit(1)
    print("\nall reconciliation checks passed")
