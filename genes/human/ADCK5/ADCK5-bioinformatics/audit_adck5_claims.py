#!/usr/bin/env python3
"""Guard: the prose surfaces must not drift from the computed results.

Three prose surfaces restate numbers that `ubib_motif_analysis.py` and
`family_annotation_census.py` compute:

  * `ADCK5-bioinformatics/RESULTS.md`
  * `ADCK5-notes.md`
  * `ADCK5-ai-review.yaml`

Nothing generates those files, so a corrected number can land in one and not the others -
the "fixed in N places, landed in N-1" failure. This script re-reads the JSON outputs and
asserts every restated value against them, and asserts that phrasings this review explicitly
withdrew do not reappear.

Design constraints learned from earlier genes in this campaign:

  * Count **surfaces** (files containing a claim), never summed occurrences: a lint that
    sums passes when one file contains N copies and the other N-1 files contain none.
  * Assert the target is **present** before judging it. A check that `continue`s when it
    cannot find its subject passes silently if the subject is deleted.
  * Collect problems and return them; never `raise` from inside a check, or the first
    failure aborts every later check *and the self-test baseline* while the harness still
    prints as though it ran.

Run `--self-test` to break-test the guards. Every check is exercised in the direction it
exists to catch AND in the happy direction, because a check can be wrong about success as
easily as about failure.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent

RESULTS_MD = HERE / "RESULTS.md"
NOTES_MD = GENE_DIR / "ADCK5-notes.md"
REVIEW_YAML = GENE_DIR / "ADCK5-ai-review.yaml"
MOTIF_JSON = HERE / "results.json"
CENSUS_JSON = HERE / "family_census.json"

PROSE_SURFACES = [RESULTS_MD, NOTES_MD, REVIEW_YAML]

# Phrasings this review considered and withdrew after measuring. If one reappears, some
# surface has been reverted to a claim the data refused.
WITHDRAWN_PHRASES = [
    # The first draft of RESULTS.md said all 25 coIP partners were mitochondrial; measuring
    # each partner's UniProt subcellular location gave 17 of 25.
    "25 mitochondrial proteins",
    # ADCK5 has no protein-kinase GO annotation at all, so no such row can be "removed".
    "remove the protein kinase activity annotation",
    # The mirror error the brief warns about: the family demonstrably CAN phosphorylate a
    # protein (COQ8B -> COQ3), so a blanket denial is wrong.
    "UbiB proteins cannot phosphorylate proteins",
    "ADCK5 is a pseudokinase",
]

# Claims that must appear on at least `min_surfaces` of the prose surfaces.
REQUIRED_CLAIMS = [
    ("K147", 2),  # KxGQ lysine
    ("A209", 2),  # A-rich loop alanine
    ("D382", 2),  # DFG aspartate (cited in the suggested kinase-dead control)
    ("17 of 25", 2),
]


def load_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(
            f"FATAL: {path.name} is missing. Run the analysis scripts first:\n"
            f"  python3 {HERE / 'ubib_motif_analysis.py'}\n"
            f"  python3 {HERE / 'family_annotation_census.py'}"
        )
    return json.loads(path.read_text())


# Residue tokens that legitimately belong to OTHER proteins' numbering and so must not be
# read as drifted ADCK5 calls. Every entry is a residue this review cites from a named
# reference protein; the set is asserted DISJOINT from the computed ADCK5 tokens, because an
# allowlist that overlapped them could mask exactly the drift this guard exists to catch.
FOREIGN_RESIDUE_TOKENS = {
    "K276",  # COQ8A KxGQ lysine
    "A339",  # COQ8A A-rich loop alanine
    "D488",  # COQ8A catalytic base
    "D507",  # COQ8A DFG aspartate
    "K134",  # yeast Coq8p KxGQ lysine
    "A197",  # yeast Coq8p A-rich loop alanine
    "D365",  # yeast Coq8p active-site aspartate
    "G53",   # PKA Calpha G-rich loop, UniProt numbering
    "K73",   # PKA Calpha beta3 lysine
    "E92",   # PKA Calpha alphaC glutamate
    "D167",  # PKA Calpha catalytic aspartate
    "N172",  # PKA Calpha catalytic-loop asparagine
    "D185",  # PKA Calpha DFG aspartate
    "S181",  # SOX9 phosphosite
}

RESIDUE_TOKEN_RE = re.compile(r"\b([A-Z]\d{2,3})\b")


def check_residue_calls(motif: dict, texts: dict[str, str]) -> list[str]:
    """Residue tokens in the prose must be either a computed ADCK5 call or a declared
    foreign-numbering citation - nothing else.

    An earlier version of this check compared every computed residue against every
    same-letter token and so reported a conflict between K147 and K228, which are BOTH
    correct: it failed on perfect agreement. The lesson (and the campaign's) is that the
    happy path is the one most likely to go untested.
    """
    problems: list[str] = []

    computed = {
        f"{c['subject_residue']}{c['subject_position']}"
        for c in motif["columns"]
        if c.get("subject_position") is not None
    }
    if not computed:
        problems.append(
            "residue guard is vacuous: results.json yielded ZERO positioned subject "
            "residues, so nothing was actually checked"
        )
        return problems

    overlap = computed & FOREIGN_RESIDUE_TOKENS
    if overlap:
        problems.append(
            f"allowlist overlaps computed residues {sorted(overlap)} - the allowlist could "
            f"mask a drift in exactly those positions"
        )

    # Presence: assert each computed residue is actually stated somewhere. A guard that only
    # validates tokens it happens to find passes silently when the claim is deleted.
    for tok in sorted(computed):
        if not any(tok in t for t in texts.values()):
            problems.append(f"computed residue {tok} is not stated on any prose surface")

    # Absence of anything else: a drifted position becomes an unrecognised token.
    allowed = computed | FOREIGN_RESIDUE_TOKENS
    for name, text in texts.items():
        for m in RESIDUE_TOKEN_RE.finditer(text):
            tok = m.group(1)
            if tok not in allowed:
                problems.append(
                    f"{name}: unrecognised residue token {tok!r} - not a computed ADCK5 "
                    f"residue {sorted(computed)} nor a declared foreign citation"
                )
    return problems


def check_census_numbers(census: dict, texts: dict[str, str]) -> list[str]:
    problems: list[str] = []
    c = census["census"]

    # ADCK5 must be the ONLY human UbiB gene with zero IBA, and the prose says so.
    zero_iba = sorted(g for g, v in c.items() if v["n_iba"] == 0)
    if zero_iba != ["ADCK5"]:
        problems.append(
            f"census: genes with zero IBA are {zero_iba}, but the prose claims ADCK5 is "
            f"the only one"
        )

    # EC split: the assayed pair downgraded, the unassayed pair not.
    for gene, expected in [
        ("COQ8A", "2.7.-.-"),
        ("COQ8B", "2.7.-.-"),
        ("ADCK5", "2.7.11.-"),
        ("ADCK2", "2.7.11.-"),
    ]:
        got = c[gene]["ec_numbers"]
        if got != [expected]:
            problems.append(f"census: {gene} EC is {got}, prose asserts {expected}")

    # The NOT| rows that make the family argument.
    for gene in ("COQ8A", "COQ8B"):
        if len(c[gene]["negated_annotations"]) != 2:
            problems.append(
                f"census: {gene} has {len(c[gene]['negated_annotations'])} NOT| rows, "
                f"prose asserts 2"
            )

    # ADCK5 must still carry the Ser/Thr kinase keyword - the whole UniProt-correction
    # recommendation is void if UniProt has already fixed it.
    if not c["ADCK5"]["has_ser_thr_kinase_keyword"]:
        problems.append(
            "census: ADCK5 no longer has the Ser/Thr-kinase keyword - the UniProt "
            "correction request in suggested_questions is now stale and must be revised"
        )
    return problems


def check_withdrawn(texts: dict[str, str]) -> list[str]:
    problems = []
    for name, text in texts.items():
        # Normalise quotation marks so a phrase cannot evade the matcher by being quoted
        # (a quote-splitting bypass was found on ACTA1).
        flat = re.sub(r"[\"'`]", "", text.lower())
        flat = re.sub(r"\s+", " ", flat)
        for phrase in WITHDRAWN_PHRASES:
            if re.sub(r"\s+", " ", phrase.lower()) in flat:
                problems.append(f"{name}: withdrawn phrasing reappeared: {phrase!r}")
    return problems


def check_required_claims(texts: dict[str, str]) -> list[str]:
    """Count SURFACES containing each claim, not total occurrences."""
    problems = []
    for claim, min_surfaces in REQUIRED_CLAIMS:
        surfaces = [n for n, t in texts.items() if claim in t]
        if len(surfaces) < min_surfaces:
            problems.append(
                f"required claim {claim!r} appears on {len(surfaces)} surface(s) "
                f"({surfaces}), expected at least {min_surfaces}"
            )
    return problems


def run_checks(texts: dict[str, str], motif: dict, census: dict) -> list[str]:
    problems: list[str] = []
    problems += check_residue_calls(motif, texts)
    problems += check_census_numbers(census, texts)
    problems += check_withdrawn(texts)
    problems += check_required_claims(texts)
    return problems


def read_surfaces() -> dict[str, str]:
    texts = {}
    for p in PROSE_SURFACES:
        if not p.exists():
            raise SystemExit(f"FATAL: prose surface missing: {p}")
        texts[p.name] = p.read_text()
    return texts


def self_test() -> int:
    motif = load_json(MOTIF_JSON)
    census = load_json(CENSUS_JSON)
    good = read_surfaces()

    failures: list[str] = []

    def expect_clean(desc: str, texts, motif=motif, census=census):
        probs = run_checks(texts, motif, census)
        if probs:
            failures.append(f"{desc}: expected clean, got {probs}")
            print(f"  FAIL (flagged good input): {desc} -> {probs}")
        else:
            print(f"  PASS (accepted good input): {desc}")

    def expect_flag(desc: str, texts, motif=motif, census=census):
        probs = run_checks(texts, motif, census)
        if probs:
            print(f"  PASS (caught): {desc}")
        else:
            failures.append(f"{desc}: expected a problem, got none")
            print(f"  FAIL (missed): {desc}")

    # happy direction first - a guard can be wrong about success as easily as failure
    expect_clean("unmodified surfaces", good)

    # 1. residue drift
    target = "A209"
    assert any(target in t for t in good.values()), "mutation target absent; guard vacuous"
    drifted = {k: v.replace(target, "A210") for k, v in good.items()}
    expect_flag("a residue position drifted (A209 -> A210)", drifted)

    # 2. withdrawn phrasing, plain and quote-split
    expect_flag(
        "withdrawn phrasing reappears",
        {**good, "RESULTS.md": good["RESULTS.md"] + "\n25 mitochondrial proteins\n"},
    )
    expect_flag(
        "withdrawn phrasing reappears with quotes inserted (bypass attempt)",
        {**good, "RESULTS.md": good["RESULTS.md"] + '\n25 "mitochondrial" proteins\n'},
    )

    # 3. required claim deleted from all but one surface (surface counting, not summing)
    stripped = dict(good)
    for k in list(stripped):
        if k != "RESULTS.md":
            stripped[k] = stripped[k].replace("17 of 25", "")
    # and pile extra copies into the remaining surface: a summing lint would pass here
    stripped["RESULTS.md"] = stripped["RESULTS.md"] + "\n17 of 25\n" * 5
    expect_flag("claim present 6x on ONE surface but deleted from the others", stripped)

    # 4. census drift
    bad_census = json.loads(json.dumps(census))
    bad_census["census"]["ADCK5"]["n_iba"] = 3
    expect_flag("ADCK5 gained IBA annotations", good, census=bad_census)

    bad_census2 = json.loads(json.dumps(census))
    bad_census2["census"]["ADCK5"]["has_ser_thr_kinase_keyword"] = False
    expect_flag("UniProt dropped the keyword (correction request now stale)", good, census=bad_census2)

    bad_census3 = json.loads(json.dumps(census))
    bad_census3["census"]["COQ8A"]["negated_annotations"] = []
    expect_flag("COQ8A lost its NOT| rows", good, census=bad_census3)

    # 5. the residue guard must not silently pass when it has nothing to check
    empty_motif = {"columns": []}
    expect_flag("results.json has no positioned residues (guard must not pass vacuously)",
                good, motif=empty_motif)

    print()
    if failures:
        for f in failures:
            print("SELF-TEST FAILURE:", f)
        return 1
    print("self-test: all guards behaved correctly in both directions")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    motif = load_json(MOTIF_JSON)
    census = load_json(CENSUS_JSON)
    texts = read_surfaces()
    problems = run_checks(texts, motif, census)
    print(f"audited {len(texts)} prose surfaces against 2 computed JSON outputs")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("no drift detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
