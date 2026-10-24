"""Tests for the shared supporting-text validator's configuration loading.

The repo-local `findings` validation path builds its validator via
``build_supporting_text_validator``. That builder must load the same
``conf/reference_validator_config.yaml`` the CLI passes to the external
reference validator, otherwise the two paths disagree: in particular the
config's ``literal_bracket_patterns`` keep bracketed chemical notation such as
``[4Fe-4S]`` or ``[Na(+)]`` from being stripped as citation markers. Without
that config, a faithful quotation of such notation fails on the findings path
while passing on the ``supported_by`` path.

Note: ``build_supporting_text_validator`` is ``@lru_cache``d on
``publications_dir``, so the repo config is read once per process. A test that
needs a differently-configured validator must call
``build_supporting_text_validator.cache_clear()`` first.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.supporting_text import (
    build_supporting_text_validator,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "reference_id,quote",
    [
        # Verbatim substrings of the cached publications, each containing
        # bracketed chemical notation that must survive validation. The two
        # cases exercise different bracket shapes: an iron-sulfur cluster and
        # a bracketed ion with nested parentheses.
        (
            "PMID:34154323",
            "require at least one [4Fe-4S](Cys)3 cluster for activity",
        ),
        (
            "PMID:17255103",
            "increased [Na(+)](i) with addition of monocarboxylates",
        ),
    ],
)
def test_findings_validator_preserves_chemical_brackets(reference_id, quote):
    """A quote with bracketed chemical notation validates on the findings path.

    Regression test: ``build_supporting_text_validator`` must apply the repo's
    ``literal_bracket_patterns`` so ``[4Fe-4S]`` / ``[Na(+)]`` are treated as
    literal text rather than stripped citation markers.
    """
    validator, _ = build_supporting_text_validator()
    if validator is None:
        pytest.skip("linkml_reference_validator is not installed")
    result = validator.validate(quote, reference_id)
    assert result.is_valid, (
        f"Quote with chemical brackets should validate, but got: "
        f"{getattr(result, 'message', '')!r}"
    )


def test_findings_validator_still_rejects_non_verbatim_quote():
    """The config change must not make the validator permissive in general.

    Negative control: a quote that is not present in the cited publication must
    still be rejected, so the fix only widens acceptance for bracket literals.
    """
    validator, _ = build_supporting_text_validator()
    if validator is None:
        pytest.skip("linkml_reference_validator is not installed")
    bogus = "this exact sentence is deliberately not present in the paper zzqq"
    result = validator.validate(bogus, "PMID:34154323")
    assert not result.is_valid, "A non-verbatim quote must not validate"


def test_findings_validator_loads_repo_bracket_patterns():
    """The built validator carries exactly the repo config's bracket patterns."""
    validator, _ = build_supporting_text_validator()
    if validator is None:
        pytest.skip("linkml_reference_validator is not installed")
    config = getattr(validator, "config", None)
    assert config is not None
    expected = yaml.safe_load(
        (PROJECT_ROOT / "conf" / "reference_validator_config.yaml").read_text()
    )["literal_bracket_patterns"]
    assert list(getattr(config, "literal_bracket_patterns", None) or []) == list(
        expected
    ), "Built validator should carry the repo config's literal_bracket_patterns"
