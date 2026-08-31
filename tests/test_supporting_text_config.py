"""Tests for the shared supporting-text validator's configuration loading.

The repo-local `findings` validation path builds its validator via
``build_supporting_text_validator``. That builder must load the same
``conf/reference_validator_config.yaml`` the CLI passes to the external
reference validator, otherwise the two paths disagree: in particular the
config's ``literal_bracket_patterns`` keep bracketed chemical notation such as
``[4Fe-4S]`` or ``[Na(+)]`` from being stripped as citation markers. Without
that config, a faithful quotation of such notation fails on the findings path
while passing on the ``supported_by`` path.
"""

import pytest

from ai_gene_review.validation.supporting_text import (
    build_supporting_text_validator,
)


@pytest.mark.parametrize(
    "reference_id,quote",
    [
        # Verbatim substrings of the cached publications, both containing
        # bracketed chemical notation that must survive validation.
        (
            "PMID:34154323",
            "require at least one [4Fe-4S](Cys)3 cluster for activity",
        ),
    ],
)
def test_findings_validator_preserves_chemical_brackets(reference_id, quote):
    """A quote with bracketed chemical notation validates on the findings path.

    Regression test: ``build_supporting_text_validator`` must apply the repo's
    ``literal_bracket_patterns`` so ``[4Fe-4S]`` is treated as literal text
    rather than a stripped citation marker.
    """
    validator, _ = build_supporting_text_validator()
    if validator is None:
        pytest.skip("linkml_reference_validator is not installed")
    result = validator.validate(quote, reference_id)
    assert result.is_valid, (
        f"Quote with chemical brackets should validate, but got: "
        f"{getattr(result, 'message', '')!r}"
    )


def test_findings_validator_config_matches_repo_bracket_patterns():
    """The built validator carries the repo config's literal_bracket_patterns."""
    validator, _ = build_supporting_text_validator()
    if validator is None:
        pytest.skip("linkml_reference_validator is not installed")
    config = getattr(validator, "config", None)
    assert config is not None
    patterns = getattr(config, "literal_bracket_patterns", None) or []
    # The repo config declares two patterns; the exact first one preserves
    # brackets whose contents include non-alpha characters ([2Fe-2S], [Ca2+]).
    assert any("a-zA-Z" in p for p in patterns), (
        f"Expected repo literal_bracket_patterns to be loaded, got {patterns!r}"
    )
