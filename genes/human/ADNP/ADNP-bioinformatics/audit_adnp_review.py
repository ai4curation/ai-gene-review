#!/usr/bin/env python3
"""Invariant checks over the EMITTED ``ADNP-ai-review.yaml``.

These run over the shipped file, not over the script that generated it: a claim
that is one sentence in a builder is line-wrapped in the dumped YAML, so a
detector reading the generator cannot see what a reviewer greps.

Checks
------
A. **Duplicate YAML keys.**  PyYAML keeps the last occurrence of a repeated
   mapping key and silently discards the earlier one, so data can vanish before
   any quote gate runs.  Loaded here with a loader that raises instead.
B. **Raw-vs-parsed quote count.**  Reconciles ``reference_id:`` occurrences in
   the raw text against a walk of the parsed document, so a quote destroyed by
   parsing shows up as an arithmetic mismatch.
C. **GOA reconciliation.**  Exactly one ``existing_annotations`` entry per
   distinct GOA TSV row, keyed on (GO id, evidence, reference, WITH/FROM) --
   the stable entity, not the prose.  ``fetch-gene`` collapses rows that differ
   only in WITH/FROM, so this is the check that catches under-review.
D. **Every quote verbatim, everywhere.**  ``checkquotes.py`` walks
   ``supported_by`` and ``findings`` only; it does not walk ``provenance`` or
   ``knowledge_gaps[].provenance``.  This walks every ``supporting_text`` in the
   document, whatever its parent key.
E. **Summary opener agrees with action.**  The first sentence is what a human
   reads first and is a stable, greppable position; the reasoning below it is
   what gets reworded.
F. **Propagation review present** on every REMOVE / MARK_AS_OVER_ANNOTATED row
   whose evidence code is not experimental.
G. **The peptide claim matches the computed data.**  The set of GO ids this
   review treats as NAP-peptide-derived must equal
   ``results.json["nap_derived_go_ids"]``, which is computed from QuickGO and
   PubMed.  Selects on GO id, so rewording cannot drift it.
I. **The verdict tally in ``ADNP-notes.md`` equals the computed one.**  Added
   because the first PR body's hand-counted tally was wrong on three of six
   actions.
J. **A withdrawn cross-row claim stays withdrawn**, guarded on stable tokens
   (a PMID, an RGD id, gene symbols) rather than on the conclusion's wording.
   Cannot catch a paraphrase that avoids all of them -- prose still needs human
   re-reading; this closes the cheap half.
H. **core_functions terms are backed by a row.**  Reported in both directions,
   but only the forward direction fails: a core function must trace to an
   ACCEPT/NEW row or to a MODIFY row's replacement term.  The reverse direction
   (an ACCEPT row whose term is absent from ``core_functions``) is *listed, not
   failed*, because accepting a correct general parent while promoting a
   specific child is legitimate curation and a guard that forbade it would be
   worked around rather than obeyed.

Usage::

    uv run python audit_adnp_review.py
    uv run python audit_adnp_review.py --self-test
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterator

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "ADNP-ai-review.yaml"
GOA = GENE_DIR / "ADNP-goa.tsv"
RESULTS = HERE / "results.json"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# Opening words that contradict an action if they start the summary.
FORBIDDEN_OPENERS: dict[str, tuple[str, ...]] = {
    "REMOVE": ("accept", "accepted", "retained", "retain", "kept", "keep", "correct and core"),
    "MARK_AS_OVER_ANNOTATED": ("accept", "accepted", "removed", "remove"),
    "ACCEPT": ("removed", "remove", "over-annotated", "overannotated"),
    "KEEP_AS_NON_CORE": ("removed", "remove", "core and", "accepted and core"),
    "MODIFY": ("accepted", "removed"),
    "NEW": ("accepted", "removed", "retained"),
}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of dropping data."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"duplicate key {key!r}", key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    lambda loader, node: _no_duplicates(loader, node, deep=False),
)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def walk_quotes(node: Any, path: str = "") -> Iterator[tuple[str, str, str]]:
    """Every (path, reference_id, supporting_text) in the document, any parent key."""
    if isinstance(node, dict):
        if "supporting_text" in node and node.get("supporting_text"):
            yield path, node.get("reference_id", ""), node["supporting_text"]
        for key, value in node.items():
            yield from walk_quotes(value, f"{path}.{key}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from walk_quotes(item, f"{path}[{i}]")


def source_text(ref: str) -> str | None:
    if ref.startswith("PMID:"):
        path = REPO / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
    elif ref.startswith("file:"):
        rel = ref.split(":", 1)[1]
        path = REPO / "genes" / rel
        if not path.exists():
            path = REPO / rel
    else:
        return None
    return path.read_text() if path.exists() else ""


# --------------------------------------------------------------------------
def audit(doc: dict, raw: str, goa_rows: list[dict], results: dict) -> list[str]:
    problems: list[str] = []
    annotations = doc.get("existing_annotations") or []
    if not annotations:
        problems.append("A/C: existing_annotations is empty -- refusing to pass vacuously")
        return problems

    # ---- B: raw vs parsed -------------------------------------------------
    raw_count = len(re.findall(r"^\s*(?:-\s*)?reference_id:", raw, flags=re.M))
    parsed_count = sum(1 for _ in walk_quotes(doc))
    parsed_refids = len(
        [1 for _p, _r, _t in walk_quotes(doc)]
    )
    if raw_count != parsed_refids:
        problems.append(
            f"B: raw reference_id occurrences ({raw_count}) != parsed quote entries "
            f"({parsed_refids}); a duplicate key or an alias may be hiding data"
        )
    if parsed_count == 0:
        problems.append("B: no quotes found at all -- the walker is broken or the file is empty")

    # ---- C: GOA reconciliation -------------------------------------------
    goa_keys = {
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"])
        for r in goa_rows
    }
    review_keys: list[tuple] = []
    for ann in annotations:
        if (ann.get("review") or {}).get("action") == "NEW":
            continue
        review_keys.append(
            (
                ann["term"]["id"],
                ann.get("evidence_type", ""),
                ann.get("original_reference_id", ""),
                "|".join(ann.get("supporting_entities") or []),
            )
        )
    missing = goa_keys - set(review_keys)
    extra = set(review_keys) - goa_keys
    dupes = {k for k in review_keys if review_keys.count(k) > 1}
    if missing:
        problems.append(f"C: GOA rows with no review entry: {sorted(missing)}")
    if extra:
        problems.append(f"C: review entries matching no GOA row: {sorted(extra)}")
    if dupes:
        problems.append(f"C: duplicated review entries: {sorted(dupes)}")

    # ---- D: quotes verbatim ----------------------------------------------
    checked = 0
    for path, ref, text in walk_quotes(doc):
        src = source_text(ref)
        if src is None:
            continue
        if not src:
            problems.append(f"D: no cached source for {ref} (at {path})")
            continue
        checked += 1
        if norm(text) not in norm(src):
            problems.append(f"D: quote not verbatim in {ref} at {path}: {text[:80]!r}")
    if checked == 0:
        problems.append("D: zero quotes were actually checked -- refusing to pass vacuously")

    # ---- E: summary opener vs action -------------------------------------
    for i, ann in enumerate(annotations):
        review = ann.get("review") or {}
        action = review.get("action")
        summary = review.get("summary") or ""
        if not action:
            problems.append(f"E: annotation {i} ({ann['term']['id']}) has no action")
            continue
        if not summary:
            problems.append(f"E: annotation {i} ({ann['term']['id']}) has no summary")
            continue
        first = norm(summary.split(".")[0])
        for bad in FORBIDDEN_OPENERS.get(action, ()):
            if first.startswith(bad):
                problems.append(
                    f"E: {ann['term']['id']} action={action} but summary opens {first[:60]!r}"
                )

    # ---- F: propagation_review on non-experimental down-grades -----------
    for ann in annotations:
        review = ann.get("review") or {}
        if review.get("action") in {"REMOVE", "MARK_AS_OVER_ANNOTATED"}:
            if ann.get("evidence_type") not in EXPERIMENTAL:
                if not review.get("propagation_review"):
                    problems.append(
                        f"F: {ann['term']['id']} ({ann.get('evidence_type')}) is "
                        f"{review['action']} without a propagation_review"
                    )

    # ---- G: peptide claim vs computed data -------------------------------
    expected_nap = set(results["nap_derived_go_ids"])
    expected_protein = set(results["protein_derived_go_ids"])
    if not expected_nap:
        problems.append("G: results.json lists no NAP-derived terms -- nothing to check against")
    claimed_nap = set()
    for ann in annotations:
        if ann.get("original_reference_id") != "GO_REF:0000107":
            continue
        if "UniProtKB:Q9JKL8" not in (ann.get("supporting_entities") or []):
            continue
        prop = (ann.get("review") or {}).get("propagation_review") or {}
        if prop.get("root_cause") == "SOURCE_BAD":
            claimed_nap.add(ann["term"]["id"])
    if claimed_nap != expected_nap:
        problems.append(
            "G: rows flagged root_cause=SOURCE_BAD do not match the computed "
            f"NAP-derived set. only-in-YAML={sorted(claimed_nap - expected_nap)} "
            f"only-in-results.json={sorted(expected_nap - claimed_nap)}"
        )
    leaked = claimed_nap & expected_protein
    if leaked:
        problems.append(f"G: protein-derived rows flagged as peptide-derived: {sorted(leaked)}")

    # ---- H: core_functions backed by rows --------------------------------
    backed: set[str] = set()
    accepted_terms: set[str] = set()
    for ann in annotations:
        review = ann.get("review") or {}
        action = review.get("action")
        if action in {"ACCEPT", "NEW"}:
            backed.add(ann["term"]["id"])
            if action == "ACCEPT":
                accepted_terms.add(ann["term"]["id"])
        for repl in review.get("proposed_replacement_terms") or []:
            backed.add(repl["id"])
    core_terms: set[str] = set()
    for cf in doc.get("core_functions") or []:
        for key in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
            if cf.get(key):
                core_terms.add(cf[key]["id"])
        for key in ("directly_involved_in", "locations", "anatomical_locations", "substrates"):
            for term in cf.get(key) or []:
                core_terms.add(term["id"])
    if not core_terms:
        problems.append("H: no core_functions terms found -- refusing to pass vacuously")
    unbacked = core_terms - backed
    if unbacked:
        problems.append(
            f"H: core_functions terms with no ACCEPT/NEW row and no MODIFY target: {sorted(unbacked)}"
        )

    # ---- J: a withdrawn cross-row claim must not come back ----------------
    # An earlier draft argued that GO:0042277 was "inverted" and that RGD's own
    # records made the inversion explicit, citing Tubb3/Tubb4b rows carrying
    # WITH/FROM RGD:71030.  Those rows come from PMID:16893427, the donor for
    # GO:0048487 -- not for GO:0042277, whose only donor is PMID:14706557 and
    # which annotates exactly one entity.  The REMOVE stands on entity identity
    # alone; the tubulin cross-check belongs on the GO:0048487 row, where it is.
    #
    # The guard selects on STABLE tokens (a PMID, an RGD id, two gene symbols) --
    # those survive rewording, unlike the conclusion's phrasing.  Stated
    # limitation: it cannot catch a paraphrase that avoids all of them, e.g.
    # "the companion affinity-chromatography study shows the reverse".  A prose
    # surface still needs human re-reading when a claim is withdrawn; this
    # closes the cheap half, not the whole hole.
    problems.extend(check_withdrawn_cross_row_claim(annotations))

    # ---- I: the verdict tally in the notes must match the computed one -----
    # This exists because the hand-written tally in the first version of the PR
    # body was wrong on three of six actions.  A count stated in prose is a
    # hand-derived number; derive it instead.
    problems.extend(check_verdict_table(annotations))
    return problems


# (GO id of the row, tokens that must not appear in its prose or its quotes)
WITHDRAWN_CROSS_ROW: dict[str, tuple[str, ...]] = {
    "GO:0042277": ("16893427", "RGD:71030", "Tubb3", "Tubb4b", "invert"),
}


def check_withdrawn_cross_row_claim(annotations: list[dict]) -> list[str]:
    problems: list[str] = []
    for go_id, tokens in WITHDRAWN_CROSS_ROW.items():
        rows = [a for a in annotations if a["term"]["id"] == go_id]
        if not rows:
            # Assert presence: a guard defeatable by deleting the thing it
            # guards is worse than no guard.
            problems.append(
                f"J: no {go_id} row found -- the withdrawn-claim guard was not exercised"
            )
            continue
        for row in rows:
            review = row.get("review") or {}
            blob = " ".join(
                [review.get("summary") or "", review.get("reason") or ""]
                + [
                    (sb.get("reference_id") or "") + " " + (sb.get("supporting_text") or "")
                    for sb in review.get("supported_by") or []
                ]
            ).lower()
            hit = [t for t in tokens if t.lower() in blob]
            if hit:
                problems.append(
                    f"J: withdrawn cross-row claim tokens back in the {go_id} row: {hit}. "
                    f"{go_id}'s only donor is PMID:14706557; the tubulin evidence belongs "
                    f"on GO:0048487."
                )
    return problems


VERDICT_BLOCK = re.compile(
    r"<!-- verdict-counts:begin -->(.*?)<!-- verdict-counts:end -->", re.S
)


def computed_verdicts(annotations: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ann in annotations:
        action = (ann.get("review") or {}).get("action")
        if action:
            counts[action] = counts.get(action, 0) + 1
    return counts


def check_verdict_table(annotations: list[dict], notes: Path | None = None) -> list[str]:
    notes = notes or (GENE_DIR / "ADNP-notes.md")
    if not notes.exists():
        return ["I: ADNP-notes.md is missing -- refusing to pass vacuously"]
    match = VERDICT_BLOCK.search(notes.read_text())
    if not match:
        return [
            "I: no <!-- verdict-counts:begin/end --> block in ADNP-notes.md; the tally "
            "must be present so it can be checked against the computed one"
        ]
    stated = {
        m.group(1): int(m.group(2))
        for m in re.finditer(r"^\|\s*`?([A-Z_]+)`?\s*\|\s*(\d+)\s*\|", match.group(1), re.M)
    }
    if not stated:
        return ["I: verdict-counts block parsed to zero rows -- refusing to pass vacuously"]
    computed = computed_verdicts(annotations)
    if stated != computed:
        return [f"I: notes tally {stated} != computed {computed}"]
    return []


def report_only(doc: dict) -> list[str]:
    """The reverse of H: informational, never a failure (see module docstring)."""
    core_terms: set[str] = set()
    for cf in doc.get("core_functions") or []:
        for key in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
            if cf.get(key):
                core_terms.add(cf[key]["id"])
        for key in ("directly_involved_in", "locations"):
            for term in cf.get(key) or []:
                core_terms.add(term["id"])
    out = []
    for ann in doc.get("existing_annotations") or []:
        if (ann.get("review") or {}).get("action") == "ACCEPT":
            if ann["term"]["id"] not in core_terms:
                out.append(f"{ann['term']['id']} {ann['term']['label']}")
    return sorted(set(out))


def load() -> tuple[dict, str, list[dict], dict]:
    raw = REVIEW.read_text()
    doc = yaml.load(raw, Loader=StrictLoader)  # raises on duplicate keys (check A)
    goa_rows = list(csv.DictReader(GOA.open(), delimiter="\t"))
    results = json.loads(RESULTS.read_text())
    return doc, raw, goa_rows, results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    doc, raw, goa_rows, results = load()
    if args.self_test:
        return self_test(doc, raw, goa_rows, results)

    problems = audit(doc, raw, goa_rows, results)
    for line in problems:
        print(f"PROBLEM: {line}", file=sys.stderr)
    if problems:
        return 1
    print(
        f"OK: {len(doc['existing_annotations'])} annotations, "
        f"{len(goa_rows)} GOA rows, {sum(1 for _ in walk_quotes(doc))} quotes, "
        f"{len(results['nap_derived_go_ids'])} peptide-derived terms matched"
    )
    informational = report_only(doc)
    if informational:
        print("\nInformational (not a failure): ACCEPT rows whose term is not a core_functions")
        print("term. Accepting a correct general parent while promoting a specific child is")
        print("legitimate, so this is listed rather than enforced:")
        for line in informational:
            print(f"  - {line}")
    return 0


def self_test(doc: dict, raw: str, goa_rows: list[dict], results: dict) -> int:
    """Break each check in the direction it exists to catch, and confirm the
    happy path passes.  A self-test proves the guards you thought of fire; it
    cannot tell you which guard you failed to write."""
    failures: list[str] = []

    if audit(doc, raw, goa_rows, results):
        failures.append("baseline: the unmodified file does not pass")

    def expect(label: str, mutate, needle: str) -> None:
        d, r, g, s = copy.deepcopy(doc), raw, copy.deepcopy(goa_rows), copy.deepcopy(results)
        changed = mutate(d, g, s)
        if changed is False:
            failures.append(f"{label}: mutation target not present -- the guard was not exercised")
            return
        found = [p for p in audit(d, r, g, s) if p.startswith(needle)]
        if not found:
            failures.append(f"{label}: expected a {needle} problem, got none")

    # A: duplicate keys -- exercised by parsing, tested separately below.
    dup = "id: Q9H2P0\nid: Q9H2P0\n"
    try:
        yaml.load(dup, Loader=StrictLoader)
        failures.append("A: StrictLoader accepted a duplicate key")
    except yaml.constructor.ConstructorError:
        pass
    if yaml.safe_load(dup) != {"id": "Q9H2P0"}:
        failures.append("A: baseline assumption about SafeLoader dedup is wrong")

    def drop_row(d, g, s):
        before = len(d["existing_annotations"])
        d["existing_annotations"] = [
            a for a in d["existing_annotations"]
            if not (a["term"]["id"] == "GO:0044849")
        ]
        return len(d["existing_annotations"]) < before

    expect("C-missing", drop_row, "C:")

    def break_quote(d, g, s):
        for ann in d["existing_annotations"]:
            for sb in (ann.get("review") or {}).get("supported_by") or []:
                sb["supporting_text"] = "this sentence appears in no publication anywhere"
                return True
        return False

    expect("D-supported_by", break_quote, "D:")

    def break_provenance_quote(d, g, s):
        # The blind spot checkquotes.py has: provenance under knowledge_gaps.
        for gap in d.get("knowledge_gaps") or []:
            for prov in gap.get("provenance") or []:
                prov["supporting_text"] = "fabricated provenance quote for the self-test"
                return True
        return False

    expect("D-knowledge_gaps.provenance", break_provenance_quote, "D:")

    def flip_opener(d, g, s):
        for ann in d["existing_annotations"]:
            if (ann.get("review") or {}).get("action") == "REMOVE":
                ann["review"]["summary"] = "Accepted. " + ann["review"]["summary"]
                return True
        return False

    expect("E-opener", flip_opener, "E:")

    def strip_propagation(d, g, s):
        for ann in d["existing_annotations"]:
            review = ann.get("review") or {}
            if review.get("action") == "REMOVE" and review.get("propagation_review"):
                del review["propagation_review"]
                return True
        return False

    expect("F-propagation", strip_propagation, "F:")

    def unflag_peptide_row(d, g, s):
        for ann in d["existing_annotations"]:
            if ann["term"]["id"] == "GO:0050805":
                ann["review"]["propagation_review"]["root_cause"] = "UNRESOLVED"
                return True
        return False

    expect("G-drift", unflag_peptide_row, "G:")

    def misflag_protein_row(d, g, s):
        for ann in d["existing_annotations"]:
            if ann["term"]["id"] == "GO:0030425":
                ann["review"]["propagation_review"] = {
                    "root_cause": "SOURCE_BAD",
                    "source_entities": [{"source_id": "UniProtKB:Q9JKL8"}],
                }
                return True
        return False

    expect("G-leak", misflag_protein_row, "G:")

    def reintroduce_withdrawn(d, g, s):
        for ann in d["existing_annotations"]:
            if ann["term"]["id"] == "GO:0042277":
                ann["review"]["reason"] += (
                    " RGD's own annotations from the companion tubulin paper make the "
                    "inversion explicit: PMID:16893427 gives peptide binding to Tubb3."
                )
                return True
        return False

    expect("J-withdrawn", reintroduce_withdrawn, "J:")

    def delete_guarded_row(d, g, s):
        before = len(d["existing_annotations"])
        d["existing_annotations"] = [
            a for a in d["existing_annotations"] if a["term"]["id"] != "GO:0042277"
        ]
        return len(d["existing_annotations"]) < before

    expect("J-deleted-row", delete_guarded_row, "J:")

    def break_tally(d, g, s):
        # The defect that actually shipped: a hand-written tally disagreeing
        # with the file.  Simulate it by changing an action so the counts move.
        for ann in d["existing_annotations"]:
            if (ann.get("review") or {}).get("action") == "MODIFY":
                ann["review"]["action"] = "ACCEPT"
                return True
        return False

    expect("I-tally", break_tally, "I:")

    def orphan_core_function(d, g, s):
        if not d.get("core_functions"):
            return False
        d["core_functions"][0]["molecular_function"] = {
            "id": "GO:0016787", "label": "hydrolase activity",
        }
        return True

    expect("H-unbacked", orphan_core_function, "H:")

    def empty_annotations(d, g, s):
        d["existing_annotations"] = []
        return True

    expect("vacuous", empty_annotations, "A/C:")

    for failure in failures:
        print(f"SELF-TEST FAIL: {failure}", file=sys.stderr)
    if not failures:
        print("self-test: 14/14 directions OK (baseline + 12 mutations + SafeLoader baseline)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
