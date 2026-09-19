"""Mutation-test the guards in ``analyze_arhgap23.py --self-test``.

A self-test that passes has proved nothing until you know it *can* fail. This script
breaks each guard in a copy of the analysis script, one at a time, and asserts that the
self-test catches the break, **by its own named guard** rather than by whatever happens to
fail first. It also applies no-op edits as negative controls, which must leave the
self-test silent -- a self-test that fails on cosmetic changes is a different kind of
useless.

This is committed, not kept in a scratchpad, because an uncommitted check never re-runs
and its claims go stale silently. It caught one real hole when it was written: the
"missing arginine finger" case had been re-implemented inside the self-test instead of
being driven through ``Protein.__init__``, so deleting the real guard left the self-test
passing. The fix was to give ``Protein`` an injectable record and test the real path.

Usage:
    uv run python mutation_test.py
    uv run python mutation_test.py --self-check   # exercise the protection layer itself
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SRC = SCRIPT_DIR / "analyze_arhgap23.py"

# The mutant is written BESIDE the original, not into a temp directory, and this is
# load-bearing rather than tidiness. ``analyze_arhgap23.py`` derives ``CACHE_DIR`` and
# ``REPO = SCRIPT_DIR.parents[3]`` from its own location, so a mutant living in
# ``/tmp/tmpXXXX`` -- the Linux and CI default -- has only two parents above it and raises
# ``IndexError`` at import. Every entry would then fail for a reason unrelated to its
# mutation: before the expected-message check existed this printed "13 guards all caught"
# off nothing but import errors, and after it every entry reports WRONG GUARD. Beside the
# original, ``SCRIPT_DIR``, ``CACHE_DIR`` and ``REPO`` resolve identically to the real
# script's, and the runs share one warm cache instead of re-downloading UniProt, the
# 1TX4 mmCIF and the Müller workbook each time.
MUTANT = SCRIPT_DIR / ".mutation_test_subject.py"

# Sharing the real SCRIPT_DIR has a cost, and it is not hypothetical: the mutant's output
# paths are the committed ones. ``--self-test`` returns before the artifact writes today,
# but nothing enforces that, and a mutation anchored on the dispatch line would run the
# mutated analysis to completion and overwrite files in place -- and RESULTS.md is the
# source for five ``file:`` supporting_text quotes in the review.
#
# The whole directory is snapshotted rather than a hand-listed pair, for three reasons that
# are all the same reason: a hand-list can drift from the write sites it mirrors; a
# membership test like ``if p.exists()`` opts out silently for a file the mutant CREATES,
# which is how a quote source could appear unreported; and an artifact added later would
# be unprotected by default. Comparing the directory's contents as {name: bytes} makes
# creation, deletion and modification all visible, and it is bytes rather than text so no
# newline or encoding normalisation can enter through the restore itself.
SNAPSHOT_EXCLUDE = {MUTANT.name}

# Throwaway files --self-check creates. Deliberately NOT in SNAPSHOT_EXCLUDE -- the point
# of the creation case is that the snapshot sees them -- but gitignored, and cleared before
# the baseline is taken so a crashed run cannot wedge the mode permanently.
SELF_CHECK_INVENTED = ".self_check_invented.md"
SELF_CHECK_SENTINEL = ".self_check_sentinel.md"

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
        'missing finger annotation: guard fired with the wrong message',
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
    (
        # The shape of an edit this repository actually makes: 14 of these comment labels
        # were rewritten in one commit and their neutrality rested on inspection alone.
        "a comment-label edit inside self_test",
        "    # Case: destroy the arginine the test is looking for.",
        "    # Case (renamed): destroy the arginine the test is looking for.",
    ),
]


def _snapshot() -> dict[str, bytes]:
    """Every regular file directly in SCRIPT_DIR, by name, as bytes.

    Directories are skipped, so ``cache/`` and ``.venv/`` are out of scope, and it is worth
    saying why that is safe rather than merely stating it. ``cache/`` is the one directory
    a mutant demonstrably writes into (``_fetch``), but its entries are sticky -- ``_fetch``
    returns the existing bytes for any non-empty cached file and never rewrites one -- so a
    mutant can only ADD entries, and only for a URL it constructs. No mutation in this file
    anchors on a URL template or a cache key, ``cache/`` is gitignored so an added entry
    leaves the tree clean, and the real run that regenerates RESULTS.md reads that same
    cache. The exposure is therefore latent, not live; a future mutation that does touch a
    URL should extend the snapshot to walk ``cache/`` rather than rely on this paragraph.

    The transient mutant is excluded by name. Everything else -- the analysis, this harness,
    the two checkers, the artifacts, the packaging files -- is covered, which is what makes
    a file the mutant invents as visible as one it overwrites.
    """
    return {
        p.name: p.read_bytes()
        for p in sorted(SCRIPT_DIR.iterdir())
        if p.is_file() and p.name not in SNAPSHOT_EXCLUDE
    }


def _restore(baseline: dict[str, bytes], label: str, failures: list[str]) -> list[str]:
    """Report and undo any creation, deletion or modification under SCRIPT_DIR.

    The report tags each name with what happened to it. Flattening the three into one list
    reads as "these files changed", which is wrong in the case that matters most: a created
    name has since been *deleted* by this function, and a reader cannot tell that from a
    bare filename.
    """
    current = _snapshot()
    created = sorted(set(current) - set(baseline))
    deleted = sorted(set(baseline) - set(current))
    modified = sorted(n for n in set(baseline) & set(current) if baseline[n] != current[n])
    changed = (
        [f"created {n}" for n in created]
        + [f"deleted {n}" for n in deleted]
        + [f"modified {n}" for n in modified]
    )
    if not changed:
        return []
    for name in created:
        (SCRIPT_DIR / name).unlink()
    for name, data in baseline.items():
        path = SCRIPT_DIR / name
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
    failures.append(f"DIRECTORY TOUCHED by {label}: {', '.join(changed)}")
    print(f"*** DIRECTORY TOUCHED by {label}: {', '.join(changed)} -- restored")
    return changed


def _write_mutant(old: str, new: str) -> None:
    text = SRC.read_text()
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"anchor matched {n} times, expected exactly 1: {old!r}")
    MUTANT.write_text(text.replace(old, new))


def _run_self_test() -> tuple[int, str, str]:
    """Return (exit code, full combined output, last line).

    The full output is returned, not just the exit code, because a non-zero exit only
    says that *something* failed. Several mutations here can be caught incidentally - a
    KeyError downstream of the guard they break, for instance - which would let the guard
    that is supposed to catch them rot unnoticed while the harness still reported "caught".
    """
    proc = subprocess.run(
        [sys.executable, str(MUTANT), "--self-test"],
        cwd=SCRIPT_DIR,
        capture_output=True,
        text=True,
    )
    combined = (proc.stdout + proc.stderr).strip()
    lines = combined.splitlines()
    return proc.returncode, combined, lines[-1] if lines else ""


def self_check() -> int:
    """Exercise the protection layer's own failure path.

    In a passing run none of ``_restore``'s reporting or repairing branches execute, so the
    only evidence they work would otherwise be an uncommitted mutant run once by hand -
    which is precisely the "a check that does not re-run goes stale silently" argument this
    file makes about everything else. This mode creates a file, modifies an existing one,
    and requires ``_restore`` to name both with the right verbs and put the directory back
    byte-for-byte.
    """
    invented = SELF_CHECK_INVENTED
    sentinel = SELF_CHECK_SENTINEL
    # Clear any leftover from a crashed earlier run BEFORE the baseline is taken. Without
    # this the leftover enters the baseline, the creation assertion fails, the finally
    # recreates it, and the mode fails identically forever with a message pointing at the
    # wrong thing. Both names are gitignored so a crash cannot dirty the tree either.
    for name in (invented, sentinel):
        (SCRIPT_DIR / name).unlink(missing_ok=True)

    baseline = _snapshot()
    # results.json first: it is cited by nothing, while RESULTS.md is the source for the
    # review's file: quotes. The crash window belongs on the lower-consequence file.
    victim = next(n for n in ("results.json", "RESULTS.md") if n in baseline)
    try:
        # Phase 1 -- creation and modification.
        (SCRIPT_DIR / victim).write_bytes(b"CLOBBERED BY --self-check")
        (SCRIPT_DIR / invented).write_bytes(b"a file the harness invented")
        failures: list[str] = []
        changed = _restore(baseline, "--self-check", failures)

        assert f"modified {victim}" in changed, f"a modified file was not reported: {changed}"
        assert f"created {invented}" in changed, f"a created file was not reported: {changed}"
        assert failures, "a directory change was repaired but not counted as a failure"
        assert not (SCRIPT_DIR / invented).exists(), "the created file was not removed"
        after = _snapshot()
        assert after == baseline, (
            "the directory was not restored byte-for-byte: "
            f"{sorted(set(after) ^ set(baseline)) or 'contents differ'}"
        )

        # Phase 2 -- deletion, and the repair arm that recreates a missing file. Neither
        # runs in phase 1, which left the third verb and one of the two repair branches
        # asserted-but-unchecked. A throwaway sentinel is used rather than a real file so
        # that a crash mid-phase cannot lose anything.
        (SCRIPT_DIR / sentinel).write_bytes(b"sentinel for the deletion case")
        with_sentinel = _snapshot()
        assert sentinel in with_sentinel, "the sentinel is excluded from the snapshot"
        (SCRIPT_DIR / sentinel).unlink()
        failures = []
        changed = _restore(with_sentinel, "--self-check deletion", failures)
        assert f"deleted {sentinel}" in changed, f"a deleted file was not reported: {changed}"
        assert failures, "a deletion was repaired but not counted as a failure"
        assert (SCRIPT_DIR / sentinel).read_bytes() == b"sentinel for the deletion case", (
            "the deleted file was not recreated with its original bytes"
        )
        (SCRIPT_DIR / sentinel).unlink()

        # Negative control: with nothing changed, _restore must be silent and report nothing.
        quiet: list[str] = []
        assert _restore(baseline, "--self-check idle", quiet) == []
        assert not quiet, f"_restore reported a change on an untouched directory: {quiet}"
    finally:
        for name in (invented, sentinel):
            (SCRIPT_DIR / name).unlink(missing_ok=True)
        for name, data in baseline.items():
            path = SCRIPT_DIR / name
            if not path.exists() or path.read_bytes() != data:
                path.write_bytes(data)
    print(
        "self-check OK: creation, modification and deletion are each reported with the "
        "right verb and repaired byte-for-byte, and an untouched directory is silent"
    )
    return 0


def main() -> int:
    if "--self-check" in sys.argv[1:]:
        return self_check()
    failures: list[str] = []
    baseline = _snapshot()
    try:
        # Unpacked directly, not indexed with a length check: an optional fourth element
        # would let a future three-element entry silently revert to deciding on the exit
        # code alone, which is the behaviour this harness exists to stop.
        for desc, old, new, expect in MUTATIONS:
            _write_mutant(old, new)
            code, full, last = _run_self_test()
            # Checked after EVERY run, not once at the end: a single trailing comparison
            # names the file but not the mutation that touched it, and leaves every later
            # entry running against an already-clobbered tree.
            _restore(baseline, desc, failures)
            if code == 0:
                failures.append(f"GUARD HOLE: {desc}")
                print(f"*** GUARD HOLE: {desc} -- self-test still passed")
            elif expect not in full:
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
            _write_mutant(old, new)
            code, _full, last = _run_self_test()
            _restore(baseline, desc, failures)
            if code != 0:
                failures.append(f"FALSE POSITIVE: {desc}")
                print(f"*** FALSE POSITIVE: {desc}\n      -> {last[:150]}")
            else:
                print(f"ok, silent: {desc}")
    finally:
        MUTANT.unlink(missing_ok=True)
        # Belt and braces: the per-run restores above cover the normal path, and this
        # catches a directory change made by an exception that escaped the loop.
        _restore(baseline, "teardown", failures)
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
