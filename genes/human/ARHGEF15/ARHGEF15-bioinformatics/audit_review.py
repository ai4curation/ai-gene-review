"""Check the numbers the review's PROSE asserts against the document's own structure.

Written because the first draft of this review's PR body said "14 ACCEPT, 9
KEEP_AS_NON_CORE" when the document contains 12 and 11, and "six bare screen-hit rows"
when there are seven across five distinct partners. Nothing in the repo compares a
sentence to the thing it describes, so the mismatch was invisible to `just validate`.

Every expectation below is a claim made somewhere in the committed prose (the review's own
`reason`/`summary`/`suggested_questions` text, the notes, or RESULTS.md). If the document
changes and a sentence goes stale, this fails.

Usage:
    uv run --no-project --with pyyaml python audit_review.py
    uv run --no-project --with pyyaml python audit_review.py --self-test
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ARHGEF15-ai-review.yaml"
NOTES = GENE_DIR / "ARHGEF15-notes.md"
RESULTS = HERE / "RESULTS.md"

NEURONAL_TERMS = {
    "GO:0030425",  # dendrite
    "GO:0098794",  # postsynapse
    "GO:0098978",  # glutamatergic synapse
    "GO:0150052",  # regulation of postsynapse assembly
    "GO:2000297",  # negative regulation of synapse maturation
}


def facts(doc: dict) -> dict:
    anns = doc["existing_annotations"]
    actions = collections.Counter(a["review"]["action"] for a in anns)
    pb = [a for a in anns if a["term"]["id"] == "GO:0005515"]
    # Policy (.claude/skills/annotation-reviewer/SKILL.md:187-199): a bare GO:0005515 row goes
    # to MODIFY when the paper supports a better MF term and otherwise to REMOVE.
    # MARK_AS_OVER_ANNOTATED is forbidden for this term, so it is counted in order to assert
    # that it is zero rather than left unmeasured.
    removed = [a for a in pb if a["review"]["action"] == "REMOVE"]
    forbidden = [a for a in pb if a["review"]["action"] == "MARK_AS_OVER_ANNOTATED"]
    partners = {e for a in removed for e in (a.get("supporting_entities") or [])}
    neuronal = [a for a in anns if a["term"]["id"] in NEURONAL_TERMS]
    mf = [a for a in anns if a["term"]["id"] == "GO:0005085"]
    ext = [
        a
        for a in anns
        if any(e.get("predicate") == "RO:0002233" for e in (a.get("extensions") or []))
    ]
    return {
        "n_rows": len(anns),
        "actions": dict(actions),
        "n_protein_binding_rows": len(pb),
        "n_removed_screen_rows": len(removed),
        "n_protein_binding_marked_over_annotated": len(forbidden),
        "n_distinct_screen_partners": len(partners),
        "n_neuronal_rows": len(neuronal),
        "n_neuronal_non_core": sum(
            1 for a in neuronal if a["review"]["action"] == "KEEP_AS_NON_CORE"
        ),
        "n_mf_rows": len(mf),
        "n_has_input_extensions": len(ext),
        "n_references": len(doc["references"]),
        "n_core_functions": len(doc["core_functions"]),
        "n_knowledge_gaps": sum(
            len(cf.get("knowledge_gaps") or []) for cf in doc["core_functions"]
        )
        + len(doc.get("knowledge_gaps") or []),
        "n_suggested_questions": len(doc.get("suggested_questions") or []),
        "n_suggested_experiments": len(doc.get("suggested_experiments") or []),
        "n_remove": actions.get("REMOVE", 0),
    }


# (name, predicate over facts, the prose claim it enforces)
EXPECTATIONS = [
    ("all 31 GOA rows reviewed", lambda f: f["n_rows"] == 31, "31 GOA rows"),
    ("no row left PENDING", lambda f: "PENDING" not in f["actions"], "all adjudicated"),
    (
        "every REMOVE is a bare GO:0005515 row, and there are seven",
        lambda f: f["n_remove"] == 7 and f["n_removed_screen_rows"] == 7,
        "7 REMOVE, all of them bare protein-binding screen rows",
    ),
    (
        "no GO:0005515 row uses MARK_AS_OVER_ANNOTATED",
        lambda f: f["n_protein_binding_marked_over_annotated"] == 0,
        "SKILL.md:187-199 forbids that action for this term",
    ),
    (
        "those seven rows cover five distinct partners",
        lambda f: f["n_distinct_screen_partners"] == 5,
        "five distinct partners: PIN1, LASP1, CEP55, PRKG1, GORASP2",
    ),
    (
        "eight protein-binding rows: seven REMOVE plus the EPHA4 MODIFY",
        lambda f: f["n_protein_binding_rows"] == 8
        and f["n_protein_binding_rows"] - f["n_removed_screen_rows"] == 1
        and f["actions"].get("MODIFY") == 1,
        "EPHA4 is the eighth of eight, and the one interaction with a mechanism",
    ),
    (
        "seven neuronal/dendritic rows, all non-core",
        lambda f: f["n_neuronal_rows"] == 7 and f["n_neuronal_non_core"] == 7,
        "seven neuronal/dendritic rows kept as non-core",
    ),
    (
        "seven GO:0005085 rows",
        lambda f: f["n_mf_rows"] == 7,
        "the weakest of the seven rows for this term",
    ),
    (
        "five rows carry the substrate as a has_input extension",
        lambda f: f["n_has_input_extensions"] == 5,
        "substrate carried in RO:0002233 has_input extensions",
    ),
    ("two core functions", lambda f: f["n_core_functions"] == 2, "two core_functions"),
    (
        "two knowledge gaps",
        lambda f: f["n_knowledge_gaps"] == 2,
        "history record: 'two core_functions and two knowledge gaps'",
    ),
    (
        "four suggested questions and three suggested experiments",
        lambda f: f["n_suggested_questions"] == 4 and f["n_suggested_experiments"] == 3,
        "the question and experiment lists the PR body describes",
    ),
]


def prose_number_checks(f: dict) -> list[str]:
    """Cross-check the specific figures that appear as words/digits in committed prose."""
    problems = []
    review_text = REVIEW.read_text()
    notes_text = NOTES.read_text() if NOTES.exists() else ""
    # Phrase regexes must run against whitespace-normalised text: the review is a wrapped
    # YAML document, so any multi-word phrase can be split across a line break. A regex that
    # never matches also never fires, which is a check that cannot report what it is named
    # for -- caught here by the mutation test below, not by reasoning about it.
    review_flat = re.sub(r"\s+", " ", review_text)
    notes_flat = re.sub(r"\s+", " ", notes_text)

    words = {5: "Five", 6: "Six", 7: "Seven", 8: "Eight"}

    # "Seven bare protein-binding rows in this record" in suggested_questions.
    m = re.search(r"(\w+) bare protein-binding rows in this record", review_flat)
    if m:
        want = words.get(f["n_removed_screen_rows"])
        if m.group(1).capitalize() != want:
            problems.append(
                f"review suggested_questions says {m.group(1)!r} bare protein-binding rows, "
                f"document removes {f['n_removed_screen_rows']} ({want!r})"
            )

    # The review describes the Mueller read-control outcome in prose; compare it to the
    # recorded result. The first draft said "six textbook-specificity read-controls" were
    # recovered when only five are -- and the sixth failing is the whole point of keeping it.
    muller = HERE / "muller2020_specificity.json"
    if muller.exists():
        ok = json.loads(muller.read_text())["read_controls_ok"]
        n_recovered = sum(1 for v in ok.values() if v)
        n_total = len(ok)
        m = re.search(r"(\w+) textbook-specificity read-controls", review_flat)
        if m and m.group(1) != words.get(n_total, "?").lower():
            problems.append(
                f"review says {m.group(1)!r} read-controls; the recorded run has {n_total}"
            )
        m = re.search(r"of which (\w+) recover their expected GTPase", review_flat)
        if m and m.group(1) != words.get(n_recovered, "?").lower():
            problems.append(
                f"review says {m.group(1)!r} read-controls recover; the recorded run has "
                f"{n_recovered} of {n_total}"
            )
        failing = [g for g, v in ok.items() if not v]
        if len(failing) == 1 and failing[0] not in review_flat:
            problems.append(
                f"the one failing read-control ({failing[0]}) is not named in the review; "
                f"its failure is what licenses reading a minus as 'not detected'"
            )

    # The five partner names must all still appear, since REMOVE discards the rows from GOA.
    for partner in ("PIN1", "LASP1", "CEP55", "PRKG1", "GORASP2"):
        if review_flat.count(partner) < 2:
            problems.append(
                f"partner {partner} of a removed GO:0005515 row appears < 2 times in the "
                f"review; removals must not lose the partner identity"
            )

    # "Seven of the thirty-one GOA rows are neuronal or dendritic"
    m = re.search(r"(\w+) of the thirty-one GOA rows are neuronal or dendritic", review_flat)
    if m and m.group(1) != {7: "Seven", 6: "Six"}.get(f["n_neuronal_rows"], "?"):
        problems.append(
            f"review says {m.group(1)!r} neuronal/dendritic rows, document has {f['n_neuronal_rows']}"
        )

    # notes: "Existing GO record (31 GOA rows)"
    m = re.search(r"Existing GO record \((\d+) GOA rows\)", notes_flat)
    if m and int(m.group(1)) != f["n_rows"]:
        problems.append(f"notes says {m.group(1)} GOA rows, document has {f['n_rows']}")

    return problems


def run() -> tuple[dict, list[str]]:
    doc = yaml.safe_load(REVIEW.read_text())
    f = facts(doc)
    problems = [
        f"FAILED expectation {name!r} (enforces prose claim: {claim})"
        for name, pred, claim in EXPECTATIONS
        if not pred(f)
    ]
    problems.extend(prose_number_checks(f))
    return f, problems


def self_test() -> int:
    failures = []

    def expect(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
        if not ok:
            failures.append(name)

    f, problems = run()
    expect("the real document satisfies every expectation", not problems, "; ".join(problems))
    expect("expectations are non-trivial (>=10 of them)", len(EXPECTATIONS) >= 10, str(len(EXPECTATIONS)))

    print("mutation tests (each predicate must be able to fail):")
    # Perturb the facts and confirm each expectation flips. A predicate that survives
    # every perturbation of its own input is not measuring anything.
    # The sweep must offer each predicate a perturbation capable of tripping it. An
    # `actions` dict has several independent ways to be wrong, so try them all rather than
    # one: with only {"ACCEPT": 1} the "no row left PENDING" predicate never saw a PENDING
    # row and was reported unfalsifiable when it is not.
    action_variants = [
        {"ACCEPT": 1},
        dict(f["actions"], PENDING=1),
        dict(f["actions"], REMOVE=3),
        {k: v for k, v in f["actions"].items() if k != "MODIFY"},
    ]
    unfalsifiable = []
    for name, pred, _claim in EXPECTATIONS:
        candidates = [dict(f, actions=a) for a in action_variants]
        candidates += [
            dict(f, **{k: f[k] + 1}) for k in f if isinstance(f[k], int) and k != "n_remove"
        ]
        candidates.append(dict(f, n_remove=f["n_remove"] + 1))
        if not any(not pred(m) for m in candidates):
            unfalsifiable.append(name)
    expect("every expectation flips under some perturbation of the facts",
           not unfalsifiable, str(unfalsifiable))

    # The prose cross-check must fire on wrong prose, not merely pass on right prose.
    bad = prose_number_checks(dict(f, n_removed_screen_rows=6, n_neuronal_rows=6))
    expect("prose cross-check reports a mismatch when the counts disagree",
           len(bad) >= 1, str(bad))
    good = prose_number_checks(f)
    expect("prose cross-check is silent when they agree", good == [], str(good))

    # The read-control branch needs its own mutation: the branch above only exercises the
    # row counts. Temporarily rewrite the recorded run so every control recovers, and confirm
    # the review's "of which five recover" sentence is then reported as disagreeing.
    muller = HERE / "muller2020_specificity.json"
    if muller.exists():
        original = muller.read_text()
        try:
            doc = json.loads(original)
            doc["read_controls_ok"] = {k: True for k in doc["read_controls_ok"]}
            muller.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n")
            mutated = prose_number_checks(f)
            expect(
                "read-control cross-check fires when the recorded run stops matching the prose",
                any("read-controls recover" in p for p in mutated),
                str(mutated),
            )
        finally:
            muller.write_text(original)
        expect(
            "the recorded run was restored byte-for-byte",
            muller.read_text() == original,
        )

    print()
    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    f, problems = run()
    for k, v in f.items():
        print(f"  {k}: {v}")
    print()
    for p in problems:
        print(f"  {p}")
    print(f"problems={len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
