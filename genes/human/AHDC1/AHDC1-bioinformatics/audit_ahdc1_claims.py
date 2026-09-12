#!/usr/bin/env python3
"""Invariant check for the human AHDC1 review.

Why this exists. One claim in this review was published and then retracted: an
earlier draft said the twelve AHDC1-HTT IntAct records were "one experiment logged
twelve times", inferred from a shared publication accession. Dumping the full
records refuted it -- twelve distinct interaction ACs, decomposing as four HTT bait
constructs times three yeast two-hybrid sub-method labels. A second defect was a
narrative off-by-one: the PR body claimed five NEW rows while the file had four.

Both are the same shape: a number or a phrasing asserted in prose and never
re-derived from the data. So this script derives the numbers and asserts that the
prose agrees, and it refuses to let the retracted phrasings come back.

What it checks
  1. Every data row of AHDC1-goa.tsv is covered by a non-NEW existing_annotation,
     matched on (GO id, evidence code, reference, WITH/FROM). Coverage is asserted
     by PRESENCE, not validated only on match -- a deleted entry must fail.
  2. The action tally sums to the entry count, and the entry count equals
     GOA rows + NEW rows.
  3. Retracted phrasings are absent from the review, the notes and the history
     record -- except inside an explicit retraction context, which is allowed and
     is checked for.
  4. Required claims are present, with the occurrence count they should have.
  5. Duplicate YAML mapping keys are rejected, because PyYAML silently keeps the
     last one and no other gate can see the loss.

Run:        uv run python genes/human/AHDC1/AHDC1-bioinformatics/audit_ahdc1_claims.py
Self-test:  ... --self-test   (mutates copies; every guard must fire)
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[4]
GENE_DIR = REPO / "genes" / "human" / "AHDC1"
REVIEW = GENE_DIR / "AHDC1-ai-review.yaml"
NOTES = GENE_DIR / "AHDC1-notes.md"
GOA = GENE_DIR / "AHDC1-goa.tsv"
HISTORY_DIR = REPO / "history" / "genes" / "human" / "AHDC1"


class DupKeyLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key rather than keeping the last."""


def _no_duplicates(loader, node, deep=False):  # type: ignore[no-untyped-def]
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(
                f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DupKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)

# Phrasings that were asserted and then retracted. If any reappears outside a
# sentence that explicitly marks it as retracted, that is a regression.
RETRACTED = [
    # The IntAct decomposition error (round 2).
    "same single yeast two-hybrid experiment logged twelve times",
    "all twelve IntAct records for the AHDC1-HTT pair carry the same IntAct",
    "this is one screen",
    "NbExp=12 overstates replication twelvefold",
    # The hexanediol condensate-control reading (asserted passes 6-8, withdrawn
    # pass 8). Listed because it is likelier to come back than the IntAct ones:
    # the GO:0003682 row still states the intent immediately before withdrawing it,
    # so an editor trimming that paragraph could easily leave the claim standing.
    "this strengthens the binding call",
    "It strengthens the `GO:0003682` call",
    "survived a condensate-disrupting pre-treatment would",
]
# A retraction context makes a retracted phrasing legitimate to quote.
RETRACTION_MARKERS = (
    "earlier draft",
    "retracted",
    "got it wrong",
    "was WRONG",
    "refuted",
    "withdrawn",
    "superseded",
)
# Characters either side of a match that count as "the same context". Bounded on
# purpose -- see the comment in check_retracted.
RETRACTION_WINDOW = 400

# Claims that must be present, with the number of files they must appear in.
# Keyed by a short name so a failure names the claim, not a regex.
REQUIRED = {
    "htt_decomposition": (
        re.compile(r"(?:four|4)\s+(?:distinct\s+)?HTT\s+(?:bait\s+)?constructs", re.I),
        2,  # review + notes
    ),
    "atxn1_axh_mapping": (re.compile(r"axh", re.I), 2),
    "at_hook_core_is_unique": (
        re.compile(r"occurs?\s+exactly\s+once|sole\s+occurrence|single\s+occurrence", re.I),
        2,
    ),
    "no_interpro2go": (
        re.compile(
            r"empty\s+`?interpro2go`?|carries?\s+(?:no|any)\s+GO\s+term|with\s+empty\s+`?interpro2go",
            re.I,
        ),
        2,
    ),
    # The crux of why GO:0003700 -> GO:0003712 is a lateral correction rather than a
    # retreat to a parent. Deliberately anchored on the term ids so it cannot be
    # satisfied by the unrelated "sibling review" / "sibling subunit" usages.
    "go0003700_is_sibling_not_parent": (
        re.compile(r"sibling\s+(?:of\s+`?GO:0003700|under\s+`?GO:0140110)", re.I),
        2,
    ),
}

# Claims that must be stated on BOTH SIDES of a comparison, scoped to specific
# rows. A whole-file occurrence count cannot express this: two matches anywhere
# would satisfy it even if both sat in the same reason, which is exactly the
# invariant that matters. So these are checked against the parsed
# existing_annotations[].review.reason of the named term, one entry per side.
#
# The tagged-transgene limitation is weighted differently on GO:0003700 (where it
# is load-bearing, because that term claims site specificity) and GO:0003682
# (where it is secondary, because that term claims only association). A reader
# arriving at either row must find the justification there.
PAIRED_CLAIMS = {
    "tagged_transgene_weighting_justified": (
        re.compile(r"weighted\s+(?:differently|less)", re.I),
        ["GO:0003700", "GO:0003682"],
    ),
    # The FILTERING half of the hexanediol argument bears on both rows: it limits
    # what the GO:0003682 peak set shows, and it is a fifth argument against
    # GO:0003700. A first draft stated it only on GO:0003682 while referring to
    # "the ectopic promoter and the authors' own statement", both of which live on
    # the GO:0003700 row -- so a curator reading the MODIFY row would never have
    # learned of it.
    "hexanediol_filtering_on_both_rows": (
        re.compile(r"hexanediol", re.I),
        ["GO:0003700", "GO:0003682"],
    ),
}


def load_review() -> dict:
    return yaml.load(REVIEW.read_text(), Loader=DupKeyLoader)


def goa_rows() -> list[dict]:
    with GOA.open() as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t") if r.get("GENE PRODUCT DB")]
    return rows


def _key_from_goa(r: dict) -> tuple:
    wf = tuple(sorted(t for t in (r["WITH/FROM"] or "").split("|") if t))
    return (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], wf)


def _key_from_entry(e: dict) -> tuple:
    wf = tuple(sorted(e.get("supporting_entities") or []))
    return (
        e["term"]["id"],
        e.get("evidence_type"),
        e.get("original_reference_id"),
        wf,
    )


def check_coverage(problems: list[str]) -> None:
    doc = load_review()
    entries = doc["existing_annotations"]
    new_entries = [e for e in entries if e["review"]["action"] == "NEW"]
    goa_entries = [e for e in entries if e["review"]["action"] != "NEW"]
    rows = goa_rows()

    # (1) presence, not validate-on-match: build the index, then assert each GOA
    # key is IN it. A deleted entry therefore fails instead of being skipped.
    index: dict[tuple, int] = {}
    for e in goa_entries:
        index[_key_from_entry(e)] = index.get(_key_from_entry(e), 0) + 1
    for r in rows:
        k = _key_from_goa(r)
        if k not in index:
            problems.append(f"GOA row not covered by any non-NEW entry: {k}")
    for k, n in index.items():
        want = sum(1 for r in rows if _key_from_goa(r) == k)
        if n != want:
            problems.append(f"entry/GOA multiplicity mismatch for {k}: {n} entries vs {want} rows")

    # (2) arithmetic, derived on both sides
    if len(entries) != len(rows) + len(new_entries):
        problems.append(
            f"entry count {len(entries)} != GOA rows {len(rows)} + NEW rows {len(new_entries)}"
        )
    tally: dict[str, int] = {}
    for e in entries:
        a = e["review"]["action"]
        tally[a] = tally.get(a, 0) + 1
    if sum(tally.values()) != len(entries):
        problems.append(f"action tally {tally} does not sum to {len(entries)} entries")
    if "PENDING" in tally:
        problems.append(f"{tally['PENDING']} entries still have action: PENDING")
    print(f"  GOA rows={len(rows)}  entries={len(entries)}  NEW={len(new_entries)}  {tally}")


def check_retracted(problems: list[str]) -> None:
    targets = [REVIEW, NOTES] + sorted(HISTORY_DIR.glob("*.yaml"))
    for path in targets:
        if not path.exists():
            problems.append(f"expected file missing: {path}")
            continue
        text = path.read_text()
        for phrase in RETRACTED:
            for m in re.finditer(re.escape(phrase), text, re.I):
                # Allow it inside an explicit retraction context. The window must be
                # BOUNDED on both sides: an earlier version reached back to the last
                # blank line, which in a YAML file can be the start of the document,
                # so any retraction marker anywhere above silently excused every
                # later match. The self-test caught that only after an unrelated
                # edit added a marker near the top -- i.e. the guard had been
                # passing by luck. A fixed +/- window is predictable and cannot
                # swallow the file.
                lo = max(0, m.start() - RETRACTION_WINDOW)
                para = text[lo : m.end() + RETRACTION_WINDOW]
                if not any(k.lower() in para.lower() for k in RETRACTION_MARKERS):
                    problems.append(
                        f"{path.name}: retracted phrasing outside a retraction context: {phrase!r}"
                    )
    print(f"  retracted-phrasing scan over {len(targets)} files: "
          f"{len(RETRACTED)} phrasings checked")


def check_required(problems: list[str]) -> None:
    corpus = {REVIEW.name: REVIEW.read_text(), NOTES.name: NOTES.read_text()}
    for name, (pattern, min_files) in REQUIRED.items():
        hits = [fn for fn, txt in corpus.items() if pattern.search(txt)]
        if len(hits) < min_files:
            problems.append(
                f"required claim {name!r} found in {len(hits)} file(s) "
                f"({hits}), expected at least {min_files}"
            )
    # Paired claims: resolve each named term to its row's review.reason and require
    # the pattern in EVERY side. A missing row is an error, not a silent skip --
    # otherwise deleting the row would satisfy the check.
    doc = load_review()
    by_term: dict[str, list[str]] = {}
    for e in doc["existing_annotations"]:
        by_term.setdefault(e["term"]["id"], []).append(e["review"].get("reason") or "")
    for name, (pattern, term_ids) in PAIRED_CLAIMS.items():
        for tid in term_ids:
            reasons = by_term.get(tid)
            if not reasons:
                problems.append(
                    f"paired claim {name!r}: no existing_annotation for {tid}, so the "
                    f"claim cannot be checked on that side"
                )
                continue
            if not any(pattern.search(r) for r in reasons):
                problems.append(
                    f"paired claim {name!r} is absent from the {tid} row's review.reason; "
                    f"the justification must appear on both sides of the comparison"
                )
    print(
        f"  required-claim scan: {len(REQUIRED)} claims, "
        f"{len(PAIRED_CLAIMS)} paired claims over "
        f"{sum(len(v[1]) for v in PAIRED_CLAIMS.values())} rows"
    )


def run() -> list[str]:
    problems: list[str] = []
    try:
        load_review()
    except ValueError as e:
        return [f"DUPLICATE YAML KEY: {e}"]
    # Each check appends; none raises, so one failure cannot abort the rest.
    check_coverage(problems)
    check_retracted(problems)
    check_required(problems)
    return problems


def fired_with(problems: list[str], expected: str) -> bool:
    """Did the INTENDED guard fire, rather than merely some guard?

    ``bool(run())`` only proves a problem appeared. Three of the mutations below go
    through a YAML round-trip, so they share a possible vacuous-pass mode: if the
    round-trip itself perturbed the document, every one of them would "pass" while
    testing nothing. Matching the expected problem text closes that.
    """
    return any(expected.lower() in p.lower() for p in problems)


def self_test() -> int:
    """Break it on purpose. A guard no mutation exercises is reported, not counted."""
    import shutil
    import tempfile

    global REVIEW, NOTES, HISTORY_DIR
    orig_review, orig_notes, orig_hist = REVIEW, NOTES, HISTORY_DIR
    fired: dict[str, bool] = {}
    tmp = Path(tempfile.mkdtemp())
    try:
        shutil.copy(orig_review, tmp / orig_review.name)
        shutil.copy(orig_notes, tmp / orig_notes.name)
        hist_tmp = tmp / "history"
        hist_tmp.mkdir()
        for h in orig_hist.glob("*.yaml"):
            shutil.copy(h, hist_tmp / h.name)
        REVIEW, NOTES, HISTORY_DIR = tmp / orig_review.name, tmp / orig_notes.name, hist_tmp

        base = REVIEW.read_text()

        # guard: a deleted GOA-covering entry must fail coverage
        doc = yaml.safe_load(base)
        removed = None
        for i, e in enumerate(doc["existing_annotations"]):
            if e["review"]["action"] != "NEW":
                removed = doc["existing_annotations"].pop(i)
                break
        assert removed is not None, "self-test could not find a non-NEW entry to delete"
        REVIEW.write_text(yaml.dump(doc, sort_keys=False))
        fired["coverage_on_deleted_entry"] = fired_with(run(), "GOA row not covered")

        # guard: duplicate mapping key
        REVIEW.write_text(base.replace("gene_symbol: AHDC1", "gene_symbol: AHDC1\ngene_symbol: AHDC1", 1))
        assert REVIEW.read_text() != base, "self-test target 'gene_symbol: AHDC1' not present"
        fired["duplicate_key"] = fired_with(run(), "DUPLICATE YAML KEY")

        # guard: a retracted phrasing reintroduced with no retraction context
        REVIEW.write_text(
            base.replace(
                "    reason: >-",
                "    reason: >-\n      This is one screen.",
                1,
            )
        )
        assert "This is one screen." in REVIEW.read_text(), "self-test mutation did not land"
        fired["retracted_phrasing"] = fired_with(
            run(), "retracted phrasing outside a retraction context"
        )

        # guard: a required claim deleted
        REVIEW.write_text(base)
        notes_base = NOTES.read_text()
        NOTES.write_text(re.sub(r"(?i)axh", "XXX", notes_base))
        assert "axh" not in NOTES.read_text().lower(), "self-test mutation did not land"
        fired["required_claim_missing"] = fired_with(
            run(), "required claim 'atxn1_axh_mapping'"
        )
        NOTES.write_text(notes_base)

        # guard: a paired claim removed from ONE side. This is the mutation a
        # whole-file occurrence count could not catch, because the other side still
        # supplies a match. Mutate through the parsed YAML so the edit is scoped to
        # exactly one row's reason, and assert it landed before running the check.
        pat = re.compile(r"weighted\s+(?:differently|less)", re.I)
        doc = yaml.safe_load(base)
        hit = None
        for e in doc["existing_annotations"]:
            if e["term"]["id"] == "GO:0003682" and pat.search(e["review"].get("reason") or ""):
                e["review"]["reason"] = pat.sub("weighted somehow", e["review"]["reason"])
                hit = e
                break
        assert hit is not None, "self-test could not find the GO:0003682 side to thin"
        assert not pat.search(hit["review"]["reason"]), "thinning did not land"
        REVIEW.write_text(yaml.dump(doc, sort_keys=False))
        fired["paired_claim_one_side_removed"] = fired_with(
            run(), "tagged_transgene_weighting_justified' is absent from the GO:0003682"
        )
        REVIEW.write_text(base)

        # guard: the row a paired claim names is deleted entirely -- must fail, not skip
        doc = yaml.safe_load(base)
        before = len(doc["existing_annotations"])
        doc["existing_annotations"] = [
            e for e in doc["existing_annotations"] if e["term"]["id"] != "GO:0003682"
        ]
        assert len(doc["existing_annotations"]) < before, "self-test deletion did not land"
        REVIEW.write_text(yaml.dump(doc, sort_keys=False))
        fired["paired_claim_row_deleted"] = fired_with(
            run(), "no existing_annotation for GO:0003682"
        )
        REVIEW.write_text(base)
    finally:
        REVIEW, NOTES, HISTORY_DIR = orig_review, orig_notes, orig_hist
        shutil.rmtree(tmp, ignore_errors=True)

    print("\nself-test:")
    ok = True
    for k, v in fired.items():
        print(f"  {k}: {'FIRED' if v else 'DID NOT FIRE  <<< guard is broken'}")
        ok = ok and v
    print(
        "  note: a passing self-test proves the guards I thought of fire. It cannot\n"
        "        tell me which guard I failed to write."
    )
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    probs = run()
    if probs:
        print(f"\n{len(probs)} PROBLEM(S):")
        for p in probs:
            print("  x", p)
        raise SystemExit(1)
    print("\n0 problems")
