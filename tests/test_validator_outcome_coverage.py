"""Meta-test: every check must be capable of failing.

The most dangerous defect in a validator is not a wrong answer, it is an assertion that
cannot fail. It is invisible by construction -- the suite is green, the pipeline reports
"0 failures", and nothing distinguishes "verified" from "never actually looked".

This PR produced four such checks in one round: ``check_controls`` took a ``cache`` it
never used while its docstring described resolving sequences; a motif-only site made
``site_ref`` fail unconditionally; ``anchor_sequence_version`` was read by nothing; and
the GO branch binding was never exercised because no recipe ran ``linkml-term-validator``.
All four passed CI.

So the suite asserts a property about itself: run the validator tests with the result
classes instrumented, collect which outcomes each *check kind* actually produced, and
require every kind to have been driven to a rejection by some test.

The first version of this test had the very defect it exists to detect. It sampled
``kind`` inside the patched ``__init__``, but several kinds were assigned in post-loops
*after* construction, so they were invisible to the instrumentation and collapsed into a
single default bucket that one unrelated test satisfied. Four of six residue check kinds
were uncovered while the test reported success. Two consequences are now permanent:

* ``kind`` is set at construction for every result object, never patched on afterwards --
  ``test_kind_is_set_at_construction`` enforces that, because the instrumentation can only
  see what exists when the object is built;
* the non-vacuity proof injects a check whose kind is assigned *after* construction, which
  is the case the original proof missed by injecting a constructor-set kind instead.

Coverage is per *kind*, not per branch. Several kinds cover more than one distinguishable
rejection (``CONTROL_RESIDUE`` spans a wrong declared residue, a positive control lacking
the site, and a negative control having it), so one test can satisfy the bucket for all of
them. That is a deliberate limit: kinds are the granularity at which a check is
identifiable, and finer tracking would need per-branch instrumentation.
"""

from __future__ import annotations

import collections
import re
from pathlib import Path

import pytest

import ai_gene_review.validation.family_gene_crosscheck as fgc
import ai_gene_review.validation.family_residue_validator as frv
import ai_gene_review.validation.gene_residue_claims as grc

#: Outcomes that mean "this check rejected something".
NEGATIVE = {"FAIL", "CONFLICT"}

#: Kinds that legitimately cannot reach FAIL, each with the reason. An allowlist rather
#: than a loophole: adding an entry forces the author to state why the check can only
#: decline to decide, which is the claim a reviewer needs to check. A kind added here
#: without justification is the same defect this module exists to catch.
CANNOT_REJECT = {
    "ANCHOR_MISSING": (
        "a site with neither its own anchor nor a family reference_protein is "
        "incomplete, not contradicted, so this check reports UNRESOLVED by design"
    ),
}

#: The validator test modules whose execution defines coverage.
VALIDATOR_TESTS = [
    "tests/test_family_residue_validator.py",
    "tests/test_gene_residue_claims.py",
    "tests/test_family_gene_crosscheck.py",
]

VALIDATOR_SOURCES = [
    Path("src/ai_gene_review/validation/family_residue_validator.py"),
    Path("src/ai_gene_review/validation/gene_residue_claims.py"),
    Path("src/ai_gene_review/validation/family_gene_crosscheck.py"),
]


@pytest.fixture(scope="module")
def outcomes() -> dict[str, set[str]]:
    """Run the validator suites once, with result classes instrumented.

    Module-scoped so the nested suite runs a single time rather than once per test.
    """
    seen: dict[str, set[str]] = collections.defaultdict(set)
    originals = []

    def instrument(cls, outcome_attr):
        original = cls.__init__
        originals.append((cls, original))

        def patched(self, *args, **kwargs):
            original(self, *args, **kwargs)
            outcome = getattr(self, outcome_attr, None)
            seen[getattr(self, "kind", "?")].add(getattr(outcome, "value", str(outcome)))

        cls.__init__ = patched

    instrument(frv.ResidueCheck, "outcome")
    instrument(grc.ClaimCheck, "outcome")
    instrument(fgc.CrossCheck, "verdict")
    try:
        exit_code = pytest.main(
            ["-q", "--no-header", "-p", "no:cacheprovider", *VALIDATOR_TESTS]
        )
    finally:
        for cls, original in originals:
            cls.__init__ = original
    assert exit_code == 0, "instrumented validator suite must pass"
    return dict(seen)


def test_every_check_kind_can_fail(outcomes):
    """No check may be incapable of rejecting something.

    If this fails, either the check is inert and should be fixed or removed, or it is
    real and needs a test that drives it to a rejection.
    """
    assert outcomes, "instrumentation collected nothing; the harness itself is broken"
    never_fails = sorted(
        k for k, outs in outcomes.items()
        if not (outs & NEGATIVE) and k not in CANNOT_REJECT
    )
    assert not never_fails, (
        "these check kinds were never driven to FAIL/CONFLICT by any test, so nothing "
        f"demonstrates they can reject anything: {never_fails}\n"
        "Either write a test that breaks the data they check, or add the kind to "
        "CANNOT_REJECT with the reason it can only decline to decide.\n"
        "Observed outcomes per kind: "
        + ", ".join(f"{k}={sorted(v)}" for k, v in sorted(outcomes.items()))
    )


def test_every_check_kind_produces_a_non_pass_outcome(outcomes):
    """Even an exempt kind must be able to *not* accept.

    A check whose only possible outcome is PASS is inert whatever its justification, so
    the CANNOT_REJECT allowlist does not excuse a kind from reaching UNRESOLVED at least.
    """
    always_passes = sorted(k for k, outs in outcomes.items() if outs == {"PASS"})
    assert not always_passes, (
        f"these check kinds only ever produced PASS, so they accept unconditionally: "
        f"{always_passes}"
    )


def test_exemptions_are_still_needed(outcomes):
    """An exemption that has become unnecessary must be removed, not left to rot.

    Otherwise the allowlist silently accumulates entries that would now be caught,
    weakening the guard by exactly the checks it no longer needs to excuse.
    """
    stale = sorted(
        k for k, reason in CANNOT_REJECT.items()
        if k in outcomes and (outcomes[k] & NEGATIVE)
    )
    assert not stale, (
        f"these kinds are listed in CANNOT_REJECT but a test now drives them to a "
        f"rejection, so the exemption is obsolete: {stale}"
    )


def test_coverage_spans_every_declared_kind(outcomes):
    """Every kind the validators can emit must be reached by the suite at all.

    A kind that appears in the source but never in a run is unexercised code, which the
    failure test above cannot see -- it only inspects kinds it actually observed.
    """
    # Two construction styles, both discovered rather than listed. Listing them would
    # make this test unable to find a kind nobody had already written into it, which is
    # precisely the hole it exists to close.
    declared: set[str] = set()
    for path in VALIDATOR_SOURCES:
        source = path.read_text()
        # ResidueCheck passes kind as a keyword
        declared |= set(re.findall(r'kind="([A-Z_]+)"', source))
        # ClaimCheck and CrossCheck take kind as the first positional argument
        declared |= set(
            re.findall(r'(?:ClaimCheck|CrossCheck)\(\s*"([A-Z_]+)"', source, re.S)
        )
        # Helpers that build a result on their caller's behalf receive the kind as a
        # literal at the call site, so discover those too -- otherwise a new kind
        # introduced through a pass-through would be invisible here, which is the
        # same blind spot in a different shape.
        declared |= set(
            re.findall(r'_check_position\([^)]*?"([A-Z_]+)"', source, re.S)
        )
    unreached = sorted(declared - set(outcomes))
    assert not unreached, (
        f"these check kinds exist in the validators but no test reaches them: {unreached}"
    )


def test_kind_is_set_at_construction():
    """``kind`` must never be assigned after a result object is built.

    The instrumentation samples ``kind`` inside ``__init__``, so a kind patched on
    afterwards is invisible and silently collapses into the default bucket. That is
    exactly how the first version of this module reported full coverage while four of
    six residue kinds were unexercised.
    """
    offenders = []
    for path in VALIDATOR_SOURCES:
        for lineno, line in enumerate(path.read_text().split("\n"), start=1):
            # `=` but not `==`, so a comparison on .kind is not mistaken for a write
            if re.search(r"\.kind\s*=(?!=)", line) and "self.kind" not in line:
                offenders.append(f"{path.name}:{lineno}: {line.strip()}")
    assert not offenders, (
        "kind is assigned after construction here, which hides the check from coverage "
        "instrumentation; pass kind= to the constructor instead:\n  "
        + "\n  ".join(offenders)
    )


def test_post_stamped_kind_is_invisible_to_instrumentation(monkeypatch):
    """Demonstrates why post-stamping must be banned rather than merely discouraged.

    This is the exact defect the first version of this module shipped with. The original
    non-vacuity proof missed it by injecting a check whose kind was set in the
    constructor -- the one path that already worked.
    """
    seen: dict[str, set[str]] = collections.defaultdict(set)
    original = frv.ResidueCheck.__init__

    def patched(self, *args, **kwargs):
        original(self, *args, **kwargs)
        seen[getattr(self, "kind", "?")].add(self.outcome.value)

    monkeypatch.setattr(frv.ResidueCheck, "__init__", patched)

    inert = frv.ResidueCheck(
        "PANTHER:PTHR00001", "-", "-", 0, [], None, frv.Outcome.PASS,
        "an inert check that can never fail",
    )
    inert.kind = "ALWAYS_PASSES_POST_STAMPED"

    assert inert.kind == "ALWAYS_PASSES_POST_STAMPED"
    assert "ALWAYS_PASSES_POST_STAMPED" not in seen, (
        "a post-stamped kind should be invisible to the instrumentation"
    )
    assert seen == {"RESIDUE": {"PASS"}}, (
        "it collapses into the default bucket, where an unrelated test's PASS hides it"
    )


def test_source_guard_rejects_post_stamping(tmp_path, monkeypatch):
    """The guard must actually fire on a file that assigns kind after construction."""
    offending = tmp_path / "offender.py"
    offending.write_text("results[0].kind = \"SOMETHING\"\n")
    monkeypatch.setattr(
        "tests.test_validator_outcome_coverage.VALIDATOR_SOURCES", [offending]
    )
    with pytest.raises(AssertionError, match="assigned after construction"):
        test_kind_is_set_at_construction()


def test_source_guard_accepts_constructor_assignment(tmp_path, monkeypatch):
    """...and must not fire on the correct pattern, or it would block the fix."""
    clean = tmp_path / "clean.py"
    clean.write_text('ResidueCheck(..., kind="SOMETHING")\nself.kind = kind\n')
    monkeypatch.setattr(
        "tests.test_validator_outcome_coverage.VALIDATOR_SOURCES", [clean]
    )
    test_kind_is_set_at_construction()
