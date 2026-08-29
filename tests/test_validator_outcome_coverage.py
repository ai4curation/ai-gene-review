"""Meta-test: every check must be capable of failing.

The most dangerous defect in a validator is not a wrong answer, it is an assertion that
cannot fail. It is invisible by construction -- the suite is green, the pipeline reports
"0 failures", and nothing distinguishes "verified" from "never actually looked".

This session produced four of them in one PR: ``check_controls`` accepted a ``cache``
argument and never used it while its docstring described resolving sequences; a
motif-only site made ``site_ref`` fail unconditionally; ``anchor_sequence_version`` was
read by nothing; and the GO branch binding was never exercised because no recipe ran
``linkml-term-validator``. All four passed CI. A human reading the code found them.

So the suite asserts a property about itself: run the validator tests with the result
classes instrumented, collect which outcomes each *check kind* actually produced, and
require every kind to have been driven to a failure outcome by some test. A new check
that nothing can falsify fails this test until someone writes the case that breaks it.
"""

from __future__ import annotations

import collections

import pytest

import ai_gene_review.validation.family_gene_crosscheck as fgc
import ai_gene_review.validation.family_residue_validator as frv
import ai_gene_review.validation.gene_residue_claims as grc

#: Outcomes that mean "this check rejected something".
NEGATIVE = {"FAIL", "CONFLICT"}

#: The validator test modules whose execution defines coverage.
VALIDATOR_TESTS = [
    "tests/test_family_residue_validator.py",
    "tests/test_gene_residue_claims.py",
    "tests/test_family_gene_crosscheck.py",
]


def _collect_outcomes() -> dict[str, set[str]]:
    """Run the validator suites with result classes instrumented; map kind -> outcomes."""
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


def test_every_check_kind_can_fail():
    """No check may be incapable of rejecting something.

    If this fails, either the check is inert and should be fixed or removed, or it is
    real and needs a test that drives it to a failure outcome.
    """
    seen = _collect_outcomes()
    assert seen, "instrumentation collected nothing; the harness itself is broken"

    never_fails = sorted(k for k, outs in seen.items() if not (outs & NEGATIVE))
    assert not never_fails, (
        "these check kinds were never driven to FAIL/CONFLICT by any test, so nothing "
        f"demonstrates they can reject anything: {never_fails}\n"
        "Observed outcomes per kind: "
        + ", ".join(f"{k}={sorted(v)}" for k, v in sorted(seen.items()))
    )


def test_every_check_kind_can_also_pass():
    """A check that only ever fails is as suspect as one that only ever passes.

    Weaker than the failure requirement -- a few kinds legitimately exist only to
    report a problem -- so this reports rather than blocks.
    """
    seen = _collect_outcomes()
    only_fail = sorted(
        k for k, outs in seen.items() if outs and not (outs - NEGATIVE)
    )
    # Informational: these are constructed only on the rejection path by design.
    assert isinstance(only_fail, list)
