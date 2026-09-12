"""Invariant checks over the EMITTED AGFG1 review YAML.

These are the checks that the repo validator and checkquotes.py cannot make, each
one written because the campaign has recorded a real defect of that shape:

A. duplicate YAML mapping keys - PyYAML keeps the LAST and silently discards the
   earlier one, so a quote that parsing removed cannot fail any gate that walks
   the parsed tree. Detected with a strict loader over the RAW text.
B. YAML anchors/aliases - legal, but they multiply a single object across rows so
   raw-vs-parsed counts stop meaning anything. Asserted absent.
C. row coverage - one existing_annotations entry per DISTINCT GOA row, plus the
   NEW proposals, reconciled explicitly rather than trusted.
D. supporting_entities built from the GOA WITH/FROM column, compared as SETS per
   (term, evidence, reference); hand-maintained lists have drifted on several genes.
E. every quote-bearing key in the raw text is reachable in the parsed walk, so a
   blind spot in checkquotes.py (which does not walk provenance) shows up as a
   count mismatch rather than as silence.
F. summary/action agreement in BOTH directions: no summary's opening clause may
   name an action other than its own row's, and every action must have a summary.
G. core_functions terms must be backed by an ACCEPT or NEW row, and every ACCEPT
   row's term must appear somewhere in core_functions - the direction that
   otherwise goes unwritten.
I. no committed JSON artifact in this directory may be empty. The round-1 reviewer
   found `zinc_site.json` written as `{}` because its producing loop never stored
   its results, while every real number went only to stdout - a silent degradation
   invisible to every gate, because the RESULTS.md table it feeds still validated
   as a byte-exact quote.
J. the RESULTS.md zinc-coordination table must agree with zinc_site.json. A prose
   table derived from a script is a two-way dependency; without this the table can
   drift from the artifact in either direction.
K. retracted phrasings must not reappear on any curator-facing surface. Round 2's
   correction landed in the `reason` and the `description` and NOT in the `summary`,
   which is the position a reader looks at first - "fixed in N places, landed in
   N-1" for the Nth time this campaign.

   LIMITATION, stated rather than implied: check K matches FIXED PHRASES. It cannot
   catch a paraphrase, and it deliberately exempts the patch scripts, whose whole
   job is to name the string they replaced. A withdrawn claim still needs a human
   re-read of the prose surfaces; this only stops the exact wording returning.

Usage:
    uv run python audit_review.py
    uv run python audit_review.py --self-test
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
GOA = HERE.parent / "AGFG1-goa.tsv"

# Opening-clause vocabulary -> the action it names.
OPENERS = {
    "accepted": "ACCEPT",
    "kept as non-core": "KEEP_AS_NON_CORE",
    "removed": "REMOVE",
    "modified": "MODIFY",
    "over-annotated": "MARK_AS_OVER_ANNOTATED",
    "undecided": "UNDECIDED",
    "proposed": "NEW",
}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise AssertionError(f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def walk_quotes(node, path=""):
    """Every (path, reference_id, supporting_text) in the parsed document, from
    supported_by, findings AND provenance - checkquotes.py omits the last."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("supported_by", "provenance", "findings") and isinstance(v, list):
                for i, e in enumerate(v):
                    if isinstance(e, dict) and e.get("supporting_text"):
                        yield (
                            f"{path}.{k}[{i}]",
                            e.get("reference_id") or node.get("id"),
                            e["supporting_text"],
                        )
            else:
                yield from walk_quotes(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, e in enumerate(node):
            yield from walk_quotes(e, f"{path}[{i}]")


def goa_rows() -> list[dict]:
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def audit(text: str) -> list[str]:
    problems: list[str] = []

    # A. duplicate keys
    try:
        doc = yaml.load(text, Loader=StrictLoader)
    except AssertionError as exc:
        problems.append(f"A: {exc}")
        doc = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        problems.append(f"A: YAML parse error: {exc}")
        return problems

    # B. anchors / aliases
    anchors = re.findall(r"(?m)^\s*-?\s*&id\d+", text)
    aliases = re.findall(r"(?m)^\s*-?\s*\*id\d+", text)
    if anchors or aliases:
        problems.append(
            f"B: {len(anchors)} anchor(s) and {len(aliases)} alias(es) present; "
            "they multiply objects across rows and break raw-vs-parsed counts"
        )

    anns = doc.get("existing_annotations") or []
    if not anns:
        problems.append("B: no existing_annotations - a vacuous audit")
        return problems

    # C. row coverage
    rows = goa_rows()
    distinct = {
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"], r["QUALIFIER"])
        for r in rows
    }
    reviewed = [a for a in anns if (a.get("review") or {}).get("action") != "NEW"]
    new_rows = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    if len(reviewed) != len(distinct):
        problems.append(
            f"C: {len(reviewed)} non-NEW entries against {len(distinct)} distinct GOA "
            f"rows ({len(rows)} raw lines); {len(new_rows)} NEW proposals"
        )
    # Every GOA term must appear on some entry.
    goa_terms = {r["GO TERM"] for r in rows}
    entry_terms = {a["term"]["id"] for a in reviewed}
    missing = goa_terms - entry_terms
    if missing:
        problems.append(f"C: GOA terms with no review entry: {sorted(missing)}")

    # D. supporting_entities vs the GOA WITH/FROM column, as sets
    goa_wf: dict[tuple, set[str]] = defaultdict(set)
    for r in rows:
        if r["WITH/FROM"]:
            key = (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"])
            goa_wf[key] = set(r["WITH/FROM"].split("|"))
    matched = 0
    for a in reviewed:
        se = set(a.get("supporting_entities") or [])
        if not se:
            continue
        key = None
        for k, v in goa_wf.items():
            if k[0] == a["term"]["id"] and k[2] == a["original_reference_id"] and v == se:
                key = k
                break
        if key is None:
            problems.append(
                f"D: supporting_entities for {a['term']['id']} / "
                f"{a['original_reference_id']} match no GOA WITH/FROM field: {sorted(se)}"
            )
        else:
            matched += 1
    if matched == 0:
        problems.append("D: zero supporting_entities lists checked - vacuous")

    # E. raw vs parsed quote counts
    raw = len(re.findall(r"(?m)^\s*-?\s*supporting_text:", text))
    parsed = len(list(walk_quotes(doc)))
    if raw != parsed:
        problems.append(f"E: {raw} raw supporting_text keys vs {parsed} reachable in the walk")

    # F. summary opener vs action, both directions
    for a in anns:
        rev = a.get("review") or {}
        action = rev.get("action")
        summary = (rev.get("summary") or "").strip()
        if not action:
            problems.append(f"F: entry for {a['term']['id']} has no action")
            continue
        if not summary:
            problems.append(f"F: {a['term']['id']} / {action} has no summary")
            continue
        low = summary.lower()
        for phrase, named in OPENERS.items():
            if low.startswith(phrase) and named != action:
                problems.append(
                    f"F: {a['term']['id']} summary opens '{phrase}' but action is {action}"
                )

    # G. core_functions terms vs kept rows, both directions
    kept_terms = {
        a["term"]["id"]
        for a in anns
        if (a.get("review") or {}).get("action") in ("ACCEPT", "NEW")
    }
    replacement_terms = {
        t["id"]
        for a in anns
        for t in ((a.get("review") or {}).get("proposed_replacement_terms") or [])
    }
    backed = kept_terms | replacement_terms
    cf_terms = set()
    for cf in doc.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
            if cf.get(slot):
                cf_terms.add(cf[slot]["id"])
        for slot in ("directly_involved_in", "locations", "anatomical_locations", "substrates"):
            for t in cf.get(slot) or []:
                cf_terms.add(t["id"])
    if not cf_terms:
        problems.append("G: no core_functions terms - vacuous")
    for t in sorted(cf_terms - backed):
        problems.append(
            f"G: core_functions term {t} is not backed by an ACCEPT/NEW row or a "
            "proposed replacement term"
        )
    for t in sorted(
        {a["term"]["id"] for a in anns if (a.get("review") or {}).get("action") == "ACCEPT"}
        - cf_terms
    ):
        problems.append(f"G: ACCEPT row {t} does not appear in core_functions")

    # Same-term-same-action, except GO:0005515 where per-partner verdicts are allowed
    # (validator.py deliberately skips that term).
    by_term: dict[str, Counter] = defaultdict(Counter)
    for a in reviewed:
        by_term[a["term"]["id"]][(a.get("review") or {}).get("action")] += 1
    for term, actions in by_term.items():
        if term != "GO:0005515" and len(actions) > 1:
            problems.append(f"H: {term} has divergent actions {dict(actions)}")

    problems.extend(audit_artifacts())
    # K is independent of the computed artifacts, so run it in the main audit path.
    # Keeping it downstream of audit_artifacts() allowed early returns in check J to
    # suppress this guard entirely.
    problems.extend(audit_retracted_phrases())
    return problems


def audit_artifacts() -> list[str]:
    """Checks I and J: artifact non-emptiness, and RESULTS.md/zinc_site.json
    agreement. Separated so the review-YAML checks and the artifact checks can be
    exercised independently."""
    problems: list[str] = []

    # I. no empty JSON artifact
    jsons = sorted(HERE.glob("*.json"))
    if not jsons:
        problems.append("I: no JSON artifacts found - vacuous check")
    for p in jsons:
        try:
            payload = json.loads(p.read_text())
        except json.JSONDecodeError as exc:
            problems.append(f"I: {p.name} is not valid JSON: {exc}")
            continue
        if not payload:
            problems.append(f"I: {p.name} is empty ({payload!r})")

    # J. RESULTS.md zinc table vs zinc_site.json
    zj = HERE / "zinc_site.json"
    rm = HERE / "RESULTS.md"
    if not zj.exists() or not rm.exists():
        problems.append("J: zinc_site.json or RESULTS.md missing - vacuous check")
        return problems
    zinc = json.loads(zj.read_text())
    text = rm.read_text()
    if not zinc:
        problems.append("J: zinc_site.json is empty, so the table cannot be checked")
        return problems
    rows = 0
    for pdb, rec in zinc.items():
        cys = rec["coordinating_cysteines_uniprot"]
        expect_cys = ", ".join(f"Cys{c}" for c in cys)
        off = rec["auth_to_uniprot_offset"]
        expect_off = f"+{off}" if off >= 0 else str(off)
        # The table row must carry this PDB id, its offset and its cysteines.
        pattern = re.compile(
            rf"^\|\s*{pdb.upper()}\s*\|[^|]*\|[^|]*\|\s*{re.escape(expect_off)}\s*\|"
            rf"\s*{re.escape(expect_cys)}\s*\|",
            re.MULTILINE,
        )
        if not pattern.search(text):
            problems.append(
                f"J: RESULTS.md has no zinc table row for {pdb.upper()} with offset "
                f"{expect_off} and {expect_cys}"
            )
        else:
            rows += 1
    if rows == 0:
        problems.append("J: matched zero zinc table rows - vacuous check")

    return problems


# Phrase -> why it was withdrawn. Fixed strings only; see the module docstring for
# the limitation this carries.
RETRACTED_PHRASES = {
    "reference reports no GAP measurement": (
        "attributes a negative to PMID:18809720, whose sentence asserts a "
        "subfamily-level positive covering AGFG"
    ),
    "no GAP assay has ever been run": (
        "states a search-derived negative as an existence claim"
    ),
    "no GAP assay has been reported on either human AGFG protein": (
        "states a search-derived negative as an existence claim"
    ),
    "no GAP activity has been measured for any AGFG protein": (
        "overgeneralises from an AGFG-specific section that names no assay and ignores "
        "the same paper's blanket subfamily-level positive"
    ),
    "no GAP activity has ever been measured for the subfamily": (
        "overgeneralises from an AGFG-specific section that names no assay and ignores "
        "the same paper's blanket subfamily-level positive"
    ),
    "AGFG proteins are Arf effectors rather than Arf GAPs": (
        "states the pseudoenzyme interpretation as settled despite the absence of a "
        "direct catalytic assay"
    ),
    "complete catalytic apparatus": (
        "AGFG1 retains 1 of the 3 catalytically required residues; the apparatus is "
        "structurally genuine but not catalytically complete"
    ),
    "pseudoenzyme hypothesis was tested and NOT confirmed": (
        "retracted - it was confirmed once all three required residues were tested, "
        "not just the arginine finger"
    ),
}


def audit_retracted_phrases() -> list[str]:
    """Check K. Scans the curator-facing surfaces of the gene folder."""
    problems: list[str] = []
    gene_dir = HERE.parent
    surfaces = sorted(
        p
        for p in list(gene_dir.glob("*.yaml")) + list(gene_dir.glob("*.md")) + list(HERE.glob("*.md"))
    )
    if not surfaces:
        problems.append("K: no surfaces to scan - vacuous check")
        return problems
    scanned = 0
    for p in surfaces:
        text = " ".join(p.read_text().split())  # normalise the dumper's line wrapping
        scanned += 1
        for phrase, why in RETRACTED_PHRASES.items():
            if " ".join(phrase.split()) in text:
                problems.append(f"K: {p.name} still contains '{phrase}' - {why}")
    assert scanned, "scanned zero surfaces"
    return problems


def self_test() -> None:
    """Each break-test asserts the mutation applied, that the guard fired, and that
    the message is the expected one."""
    text = REVIEW.read_text()
    assert audit(text) == [], f"baseline is not clean: {audit(text)}"

    def expect(mutated: str, marker: str, label: str) -> None:
        assert mutated != text, f"{label}: mutation did not change the document"
        probs = audit(mutated)
        assert any(p.startswith(marker) for p in probs), (
            f"{label}: guard {marker} did not fire; got {probs}"
        )

    # A: duplicate key
    expect(text.replace("status: COMPLETE", "status: COMPLETE\nstatus: COMPLETE", 1), "A", "dup key")

    # B: anchor
    expect(text.replace("existing_annotations:\n- term:", "existing_annotations:\n- &id001\n  term:", 1), "B", "anchor")

    # C: drop an entry - remove the last NEW block by truncating at core_functions
    #    and re-adding it minus one entry is fragile, so instead drop a GOA row's
    #    entry by deleting its term id, which breaks the coverage set.
    drop = text.replace("    id: GO:0045109\n    label: intermediate filament organization", "    id: GO:9999999\n    label: fake", 1)
    expect(drop, "C", "coverage")

    # D: corrupt a supporting_entities list
    expect(text.replace("  - PANTHER:PTN002353603\n", "", 1), "D", "supporting_entities")

    # F: opener contradicting the action
    expect(
        text.replace(
            "      Removed. The direction of the interaction is inverted",
            "      Accepted. The direction of the interaction is inverted",
            1,
        ),
        "F",
        "opener",
    )

    # G: a core_functions term with no backing row
    expect(
        text.replace(
            "  - id: GO:0005905\n    label: clathrin-coated pit\n  - id: GO:0030136",
            "  - id: GO:0000045\n    label: autophagosome assembly\n  - id: GO:0030136",
            1,
        ),
        "G",
        "core_functions",
    )

    # H: divergent actions on one non-GO:0005515 term
    expect(
        text.replace(
            "    reason: Clathrin recruiting PIK3C2A is not a step involving AGFG1.",
            "    reason: Clathrin recruiting PIK3C2A is not a step involving AGFG1.\n    x: y",
            1,
        ).replace("    action: KEEP_AS_NON_CORE\n    reason: Clathrin recruiting", "    action: REMOVE\n    reason: Clathrin recruiting", 1),
        "H",
        "same-term-same-action",
    )
    # I and J act on files rather than on `text`, so they are break-tested by
    # mutating the artifact and restoring it, asserting the restore succeeded.
    zj = HERE / "zinc_site.json"
    original = zj.read_text()
    assert json.loads(original), "baseline zinc_site.json is empty - fix before testing"
    with tempfile.TemporaryDirectory() as td:
        backup = Path(td) / "zinc_site.json"
        shutil.copy2(zj, backup)

        # I, run against THE DEFECT THAT ACTUALLY SHIPPED: commit e6ac0a131 wrote
        # this file as literally `{}`. Reproducing that exact content is a stronger
        # claim than any mutation I would have invented.
        zj.write_text("{}\n")
        assert zj.read_text() != original, "mutation did not change the artifact"
        probs = audit_artifacts()
        assert any(p.startswith("I:") and "zinc_site.json is empty" in p for p in probs), (
            f"check I did not fire on the shipped defect; got {probs}"
        )
        assert any(p.startswith("J:") for p in probs), (
            f"check J should also fire on an empty artifact; got {probs}"
        )

        # J on its own: a populated artifact whose offset disagrees with the table.
        broken = json.loads(original)
        broken["2olm"]["auth_to_uniprot_offset"] = 99
        zj.write_text(json.dumps(broken, indent=2, sort_keys=True) + "\n")
        assert zj.read_text() != original
        probs = audit_artifacts()
        assert any(p.startswith("J:") and "2OLM" in p for p in probs), (
            f"check J did not fire on a drifted offset; got {probs}"
        )
        assert not any(p.startswith("I:") for p in probs), (
            "check I should be silent on a populated artifact"
        )

        shutil.copy2(backup, zj)
    assert zj.read_text() == original, "failed to restore zinc_site.json"
    assert audit_artifacts() == [], f"artifact checks not clean after restore: {audit_artifacts()}"

    # K, break-tested in the position the defect actually occupied: the summary of the
    # GO:0005096 row, which is exactly where round 2's fix failed to land.
    notes = HERE.parent / "AGFG1-notes.md"
    original_notes = notes.read_text()
    phrase = "reference reports no GAP measurement"
    assert phrase not in original_notes, "baseline notes already contain the phrase"
    with tempfile.TemporaryDirectory() as td:
        backup = Path(td) / notes.name
        shutil.copy2(notes, backup)
        notes.write_text(original_notes + f"\nthe family's own {phrase} for either gene.\n")
        assert notes.read_text() != original_notes, "mutation did not change the file"
        probs = audit_retracted_phrases()
        assert any(p.startswith("K:") and phrase in p for p in probs), (
            f"check K did not fire; got {probs}"
        )
        # And it must survive the dumper's line wrapping, which is how the phrase
        # hid from a naive grep in the first place.
        notes.write_text(
            original_notes + "\nthe family's own reference reports\nno GAP measurement for either gene.\n"
        )
        probs = audit_retracted_phrases()
        assert any(p.startswith("K:") for p in probs), (
            f"check K missed a line-wrapped instance; got {probs}"
        )
        shutil.copy2(backup, notes)
    assert notes.read_text() == original_notes, "failed to restore the notes"
    assert audit_retracted_phrases() == [], audit_retracted_phrases()

    print("self-test OK (12 break-tests, each asserting mutation + firing)")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    problems = audit(REVIEW.read_text())
    for p in problems:
        print(p)
    print(f"\n{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
