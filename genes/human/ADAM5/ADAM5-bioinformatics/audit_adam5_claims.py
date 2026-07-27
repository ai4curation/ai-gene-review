#!/usr/bin/env python3
"""Pin the ADAM5 review's numeric claims to the measurement, and keep a retracted claim dead.

Two distinct jobs, both of which this campaign has repeatedly needed:

**A. Numbers.** `ADAM5-ai-review.yaml`, `ADAM5-notes.md` and `RESULTS.md` all restate figures
that only `results.json` actually establishes -- the 246-residue deletion, the 0.066 M12B
coverage, the 7-gene detector fire set. A figure corrected in one surface and left standing
in its twin is the single most repeated defect of this campaign, so every such number is
checked against `results.json` here rather than by eye.

**B. A retracted claim.** The review originally described the six human ADAM pseudogenes as
one "8p11.22 reproductive ADAM cluster". An HGNC location query refuted it: only ADAM3A and
ADAM5 are at 8p11.22, while ADAM1A/ADAM1B are at 12q24, ADAM3B at 16q12.1 and ADAM6 at
14q32.33 -- four chromosomes, so these are independent pseudogenisation events. That wrong
claim **shipped** in commit 4d92ca329, and `--against-shipped-defect` runs this check against
that exact blob to prove the guard covers the bug it was written for, which is a stronger
statement than any self-test.

**Declared limitation, deliberately not papered over:** part B matches *fixed phrases*. It
cannot catch a paraphrase -- someone re-asserting the cluster claim in different words would
pass. Prose surfaces still need human re-reading when a claim is withdrawn. A guard that says
what it cannot do is worth more than one that reads as coverage it does not have.

Usage::

    uv run python audit_adam5_claims.py
    uv run python audit_adam5_claims.py --self-test
    uv run python audit_adam5_claims.py --against-shipped-defect 4d92ca329
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]

REVIEW = GENE_DIR / "ADAM5-ai-review.yaml"
NOTES = GENE_DIR / "ADAM5-notes.md"
RESULTS_MD = HERE / "RESULTS.md"
RESULTS_JSON = HERE / "results.json"

#: Phrasings of the refuted "one 8p11.22 cluster" claim. Anchored on the stable entity -- the
#: locus string -- not on the conclusion's wording, which is what gets reworded.
RETRACTED_PHRASES = (
    "8p11.22 reproductive ADAM cluster",
    "8p11-8p23 reproductive ADAM cluster",
    "8p11–8p23 reproductive ADAM cluster",
    "closest paralogues in the same cluster",
)

#: Surfaces that must never re-assert the retracted claim.
SCAN_FILES = (REVIEW, NOTES, RESULTS_MD)


def _load_results() -> dict:
    if not RESULTS_JSON.exists():
        raise SystemExit(
            f"missing input: {RESULTS_JSON}\n"
            f"  fix: cd {HERE} && uv run python analyze_adam5.py"
        )
    return json.loads(RESULTS_JSON.read_text())


def check_numbers(res: dict, problems: list) -> int:
    """Every figure the prose asserts, re-derived from results.json."""
    aln = res["alignment_to_macaque"]
    panel, census = res["panel"], res["go_census"]
    fam = res["family_wide"]
    cov = aln["reference_feature_coverage"]
    deletion = aln["internal_reference_deletions"][0]

    expected = {
        "internal deletion length (246 aa)": (deletion["length"], 246),
        "deletion junction (after human 162)": (deletion["subject_junction_after_residue"], 162),
        "human length (412 aa)": (panel["Q6NVV9"]["length"], 412),
        "macaque length (756 aa)": (panel["Q28483"]["length"], 756),
        "M12B coverage (0.066)": (aln["m12b_coverage"], 0.066),
        "signal peptide coverage (0.000)": (cov["Signal:Signal 1-16"]["fraction_covered"], 0.0),
        "transmembrane coverage (0.000)": (cov["Transmembrane:Helical 699-719"]["fraction_covered"], 0.0),
        "disintegrin coverage (0.411)": (cov["Domain:Disintegrin 389-478"]["fraction_covered"], 0.411),
        "human M12B domain absent": (panel["Q6NVV9"]["m12b_domain"], None),
        "human HExxH count (0)": (panel["Q6NVV9"]["zinc_core_HExxH_count"], 0),
        "human GO:0004222 count (0)": (census["Q6NVV9"]["GO:0004222"]["count"], 0),
        "human GO:0008237 count (0)": (census["Q6NVV9"]["GO:0008237"]["count"], 0),
        "human GO:0006508 count (0)": (census["Q6NVV9"]["GO:0006508"]["count"], 0),
        "subject annotation count (3)": (len(res["subject_annotations"]), 3),
        "detector fires (7)": (len(res["detector"]["fires"]), 7),
        "detector clean (5)": (len(res["detector"]["clean"]), 5),
        "analysis reported no problems": (res["problems"], []),
        # Signature ids named in suggested_questions and the notes. Before with_from was
        # added to the projection these two were the only figures in the package not pinned
        # by the artifact -- grepping results.json for either returned nothing.
        "IPR001590 is a GO:0004222 source on mouse Adam5": (
            "InterPro:IPR001590" in census["Q3TTE0"]["GO:0004222"]["with_from"], True),
        "PTN000224844 is a GO:0004222 source on mouse Adam5": (
            "PANTHER:PTN000224844" in census["Q3TTE0"]["GO:0004222"]["with_from"], True),
        "IPR001590 is a GO:0004222 source on ADAM2": (
            "InterPro:IPR001590" in census["Q99965"]["GO:0004222"]["with_from"], True),
        "PTN000224844 is a GO:0004222 source on ADAM2": (
            "PANTHER:PTN000224844" in census["Q99965"]["GO:0004222"]["with_from"], True),
        # Family-wide figures quoted in suggested_questions, the notes and RESULTS.md.
        "reviewed family members measured (331)": (fam["reviewed_members_measured"], 331),
        "family total proteins (29886)": (fam["family_total_proteins"], 29886),
        "fold+zinc annotated (204/204)": (
            (fam["fold_with_zinc_site_annotated_GO_0004222"], fam["fold_with_zinc_site"]), (204, 204)),
        "fold-no-zinc annotated (37/40)": (
            (fam["fold_without_zinc_site_annotated_GO_0004222"], fam["fold_without_zinc_site"]), (37, 40)),
        "panel members reproduced family-wide (10)": (fam.get("panel_members_reproduced"), 10),
        "panel members absent from family (ADAM10, ADAM17)": (
            fam.get("panel_members_absent_from_family"), ["O14672", "P78536"]),
    }
    for label, (observed, want) in expected.items():
        if observed != want:
            problems.append(f"claim/measurement mismatch - {label}: results.json says {observed!r}")

    if not all(a["evidence"] == "ND" for a in res["subject_annotations"]):
        problems.append("subject annotations are no longer all ND; the review's premise has changed")

    fires = sorted(e["accession"] for e in res["detector"]["fires"])
    named = sorted(["Q28483", "Q3TTE0", "Q5BK84", "Q60472", "Q99965", "Q9Y3Q7", "Q9H2U9"])
    if fires != named:
        problems.append(f"detector fire set {fires} differs from the set the review names {named}")
    return len(expected) + 2


def check_retracted(texts: dict[str, str], problems: list) -> int:
    """The refuted cluster claim must not reappear on any surface."""
    for name, text in texts.items():
        for phrase in RETRACTED_PHRASES:
            if phrase in text:
                problems.append(f"RETRACTED claim reappeared in {name}: {phrase!r}")
    return len(texts) * len(RETRACTED_PHRASES)


def check_required(texts: dict[str, str], problems: list) -> int:
    """Claims that must be PRESENT.

    Written because 'unwritten is not the same as passing': without this half, deleting the
    correction would satisfy the retracted-phrase check trivially.
    """
    required = {
        REVIEW.name: ["dispersed across", "ADAM6 (14q32.33)", "331 Swiss-Prot reviewed members",
                      "PTN000224844", "IPR001590"],
        NOTES.name: ["16q12.1", "14q32.33", "not* one contiguous cluster",
                     "331 Swiss-Prot reviewed members", "29,886"],
        RESULTS_MD.name: ["Swiss-Prot reviewed members", "reviewed subset"],
    }
    n = 0
    for name, needles in required.items():
        if name not in texts:
            problems.append(f"required surface missing from scan: {name}")
            continue
        for needle in needles:
            n += 1
            if needle not in texts[name]:
                problems.append(f"required correction missing from {name}: {needle!r}")
    return n


def read_surfaces() -> dict[str, str]:
    out = {}
    for p in SCAN_FILES:
        if not p.exists():
            raise SystemExit(f"missing input: {p}")
        out[p.name] = p.read_text()
    return out


def run(texts: dict[str, str], res: dict | None) -> list[str]:
    """Collect problems. No check raises - a check that kills the harness is worse than none."""
    problems: list[str] = []
    n = check_retracted(texts, problems)
    n += check_required(texts, problems)
    if res is not None:
        n += check_numbers(res, problems)
    print(f"ran {n} assertions over {len(texts)} surfaces", file=sys.stderr)
    return problems


def self_test() -> int:
    failures: list[str] = []
    good = read_surfaces()

    if run(good, _load_results()):
        failures.append("audit reported problems on the current, believed-good tree")

    # Retracted-phrase check must fire, and the mutation must not be a silent no-op.
    bad = dict(good)
    marker = "dispersed across"
    assert marker in bad[REVIEW.name], "self-test anchor drifted; refusing a no-op mutation"
    bad[REVIEW.name] = bad[REVIEW.name].replace(marker, "in the 8p11.22 reproductive ADAM cluster", 1)
    probs: list[str] = []
    check_retracted(bad, probs)
    if not probs:
        failures.append("retracted-phrase check did not fire on a re-inserted claim")

    # Required-claim check must fire when the correction is deleted.
    stripped = dict(good)
    stripped[NOTES.name] = stripped[NOTES.name].replace("14q32.33", "REMOVED")
    probs = []
    check_required(stripped, probs)
    if not probs:
        failures.append("required-claim check did not fire when the correction was deleted")

    # Number check must fire on a perturbed measurement...
    res = _load_results()
    perturbed = json.loads(json.dumps(res))
    perturbed["alignment_to_macaque"]["internal_reference_deletions"][0]["length"] = 999
    probs = []
    check_numbers(perturbed, probs)
    if not probs:
        failures.append("number check did not fire on a perturbed deletion length")

    perturbed2 = json.loads(json.dumps(res))
    perturbed2["family_wide"]["fold_without_zinc_site_annotated_GO_0004222"] = 0
    probs = []
    check_numbers(perturbed2, probs)
    if not probs:
        failures.append("number check did not fire on a perturbed family-wide figure")

    perturbed3 = json.loads(json.dumps(res))
    perturbed3["go_census"]["Q3TTE0"]["GO:0004222"]["with_from"] = []
    probs = []
    check_numbers(perturbed3, probs)
    if not probs:
        failures.append("number check did not fire when the signature ids were removed")

    # ...and must stay silent on the real one (a check can be wrong about success too).
    probs = []
    check_numbers(res, probs)
    if probs:
        failures.append(f"number check fired on the real measurement: {probs}")

    for f in failures:
        print(f"SELF-TEST FAILURE: {f}", file=sys.stderr)
    print(f"self-test: {len(failures)} failure(s)", file=sys.stderr)
    return 1 if failures else 0


def against_shipped_defect(sha: str) -> int:
    """Run the retracted-phrase check against the blob that actually shipped the bug."""
    rel = REVIEW.relative_to(REPO).as_posix()
    blob = subprocess.run(
        ["git", "-C", str(REPO), "show", f"{sha}:{rel}"], capture_output=True, text=True
    )
    if blob.returncode != 0:
        print(f"cannot read {sha}:{rel}: {blob.stderr.strip()}", file=sys.stderr)
        return 2
    problems: list[str] = []
    check_retracted({f"{sha}:{REVIEW.name}": blob.stdout}, problems)
    if problems:
        print(f"guard FIRES on the shipped defect at {sha} (correct):", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 0
    print(
        f"guard did NOT fire on {sha} - it does not cover the bug it was written for",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--against-shipped-defect", metavar="SHA")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.against_shipped_defect:
        return against_shipped_defect(args.against_shipped_defect)
    problems = run(read_surfaces(), _load_results())
    for p in problems:
        print(f"PROBLEM: {p}", file=sys.stderr)
    print(f"{len(problems)} problem(s)", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
