"""Mutation-test the guards in ``analyze_arhgap23.py --self-test``.

A self-test that passes has proved nothing until you know it *can* fail. This script
breaks each guard in a copy of the analysis script, one at a time, and asserts that the
self-test catches the break. It also applies a no-op edit as a negative control, which
must leave the self-test silent -- a self-test that fails on cosmetic changes is a
different kind of useless.

This is committed, not kept in a scratchpad, because an uncommitted check never re-runs
and its claims go stale silently. It caught one real hole when it was written: the
"missing arginine finger" case had been re-implemented inside the self-test instead of
being driven through ``Protein.__init__``, so deleting the real guard left the self-test
passing. The fix was to give ``Protein`` an injectable record and test the real path.

Usage:
    uv run python mutation_test.py
"""

from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SRC = SCRIPT_DIR / "analyze_arhgap23.py"

# (description, exact source text to replace, replacement). Each anchor must match
# exactly once: zero matches would "pass" by changing nothing, two would mutate a row
# nobody intended.
MUTATIONS: list[tuple[str, str, str, str]] = [
    (
        "drop the annotated-site requirement from forward_retained",
        'forward_retained = bool(s_res == "R" and lands_on_site)',
        'forward_retained = bool(s_res == "R")',
        'retained must require the annotated-site condition',
    ),
    (
        "make reciprocal ignore the reverse mapping",
        '"reciprocal": bool(forward_retained and reverse_ok),',
        '"reciprocal": bool(forward_retained),',
        'reciprocity survived a broken reverse mapping',
    ),
    (
        "let an out-of-register interface projection through",
        "if anchor != subject.finger:",
        "if False:",
        'interface projection: expected AnalysisError',
    ),
    (
        "weaken the chain-identity proof to accept anything",
        "if identity < min_identity:",
        "if identity < 0.0:",
        'chain identity proof: expected AnalysisError',
    ),
    (
        "stop refusing a record with no arginine-finger annotation",
        '        if not fingers:\n            raise AnalysisError(\n                f"{self.name} carries no',
        '        if False:\n            raise AnalysisError(\n                f"{self.name} carries no',
        'annotated arginine fingers',
    ),
    (
        "accept an arginine finger annotated outside its own domain",
        "if not (self.domain_start <= self.finger <= self.domain_end):",
        "if False:",
        'finger outside the domain: expected AnalysisError',
    ),
    (
        "compare residue numbers across constructs of different length",
        '    length_matches = muller["construct"]["length"] == len(subject.seq)',
        "    length_matches = True",
        'a length mismatch did not stop the residue comparison',
    ),
    (
        "stop distinguishing the published mutant from the annotated arginine finger",
        '"is_uniprot_annotated_arginine_finger": pos == subject.finger,',
        '"is_uniprot_annotated_arginine_finger": True,',
        'the conclusion of section 5 has silently inverted',
    ),
    (
        "take every matching column instead of the first run in Supplementary Table 2",
        "            if label in cells:\n                break  # the run has ended and a repeat block has begun",
        "            if False:\n                break  # the run has ended and a repeat block has begun",
        'outside the +/- call vocabulary',
    ),
    (
        "stop requiring the in-vitro literature block to be found at all",
        "    for needed in LITERATURE_GROUPS_REQUIRED:\n        if needed not in groups:",
        "    for needed in LITERATURE_GROUPS_REQUIRED:\n        if False:",
        'missing literature block: expected AnalysisError',
    ),
    (
        "compute emptiness for fewer groups than the review's prose asserts",
        '        "empty_by_group": {g: _empty(groups[g]) for g in LITERATURE_GROUPS_REQUIRED},',
        '        "empty_by_group": {"in vitro": _empty(groups["in vitro"])},',
        "narrower than the pattern the review's prose asserts",
    ),
    (
        "render a literature group the presence guard does not require",
        'LITERATURE_GROUPS_REQUIRED = ("integrated", "in vitro", "in vivo", "reference")',
        'LITERATURE_GROUPS_REQUIRED = ("in vitro", "in vivo")',
        'rendered group missing from the guard: expected AnalysisError',
    ),
    (
        "resolve an ambiguous supplementary row by picking the first",
        '            f"expected exactly 1 row for {symbol} in the supplementary sheet, found {len(hits)}"',
        '            "an ambiguity that is no longer reported"',
        'duplicated supplementary row: guard fired with the wrong message',
    ),
]

NEGATIVE_CONTROLS: list[tuple[str, str, str]] = [
    (
        "a docstring reflow that changes no behaviour",
        '"""Map 1-based positions of `seq_from` onto 1-based positions of `seq_to`."""',
        '"""Map 1-based positions of seq_from onto 1-based positions of seq_to."""',
    ),
]


def _write_mutant(target: pathlib.Path, old: str, new: str) -> None:
    text = SRC.read_text()
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"anchor matched {n} times, expected exactly 1: {old!r}")
    target.write_text(text.replace(old, new))


def _run_self_test(target: pathlib.Path) -> tuple[int, str, str]:
    """Return (exit code, full combined output, last line).

    The full output is returned, not just the exit code, because a non-zero exit only
    says that *something* failed. Several mutations here can be caught incidentally - a
    KeyError downstream of the guard they break, for instance - which would let the guard
    that is supposed to catch them rot unnoticed while the harness still reported "caught".
    """
    proc = subprocess.run(
        [sys.executable, str(target), "--self-test"],
        cwd=SCRIPT_DIR,
        capture_output=True,
        text=True,
    )
    combined = (proc.stdout + proc.stderr).strip()
    lines = combined.splitlines()
    return proc.returncode, combined, lines[-1] if lines else ""


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        target = pathlib.Path(tmp) / "analyze_arhgap23.py"
        for entry in MUTATIONS:
            desc, old, new = entry[0], entry[1], entry[2]
            expect = entry[3] if len(entry) > 3 else None
            _write_mutant(target, old, new)
            code, full, last = _run_self_test(target)
            if code == 0:
                failures.append(f"GUARD HOLE: {desc}")
                print(f"*** GUARD HOLE: {desc} -- self-test still passed")
            elif expect is not None and expect not in full:
                # Caught, but by something other than the guard this mutation targets.
                failures.append(f"WRONG GUARD: {desc}")
                print(
                    f"*** WRONG GUARD: {desc}\n"
                    f"      expected the failure to mention: {expect!r}\n"
                    f"      got: {last[:150]}"
                )
            else:
                print(f"ok, caught: {desc}\n      -> {last[:150]}")
        for desc, old, new in NEGATIVE_CONTROLS:
            _write_mutant(target, old, new)
            code, _full, last = _run_self_test(target)
            if code != 0:
                failures.append(f"FALSE POSITIVE: {desc}")
                print(f"*** FALSE POSITIVE: {desc}\n      -> {last[:150]}")
            else:
                print(f"ok, silent: {desc}")
    print()
    if failures:
        print("MUTATION TEST FAILED:")
        for f in failures:
            print(" -", f)
        return 1
    print(
        f"MUTATION TEST PASSED: {len(MUTATIONS)} guards all caught, "
        f"{len(NEGATIVE_CONTROLS)} negative control(s) silent"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
