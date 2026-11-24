"""A quote that is a paper's title validates against the cached record's title.

Publications cached in the reference validator's own layout (``reference_id`` /
``extractor_version`` frontmatter, body under ``## Content``) carry the title only
in the frontmatter and a ``#`` heading, and the validator searches only the text
under ``## Content``. Records cached in the older layouts keep the title in the
searchable text, so a ``supporting_text`` that is just the title (over a hundred in
the corpus) passes there and fails the moment its record is re-cached in the new
layout, as happened with #6582. These tests pin the fix: the title is one more
searchable text for literature references, on the repo's own validator and on
the reference-validator CLI.
"""

import subprocess
import sys
from pathlib import Path

import pytest
from linkml_reference_validator.models import ReferenceContent
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)

from ai_gene_review.validation.supporting_text import build_supporting_text_validator
from ai_gene_review.validation.title_matching import install_title_matching

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_ID = "PMID:99999901"
TITLE = "Defining the membrane proteome of NK cells."
BODY_SENTENCE = "Natural killer cells express a distinctive set of surface receptors."

# The reference validator's own cache layout: the title is in the frontmatter and
# the display heading, neither of which is searched.
RECORD = f"""---
reference_id: {REFERENCE_ID}
extractor_version: 1
title: "{TITLE}"
authors:
- Example A
journal: Example Journal
year: '2010'
content_type: abstract_only
full_text_attempted: true
---

# {TITLE}
**Authors:** Example A
**Journal:** Example Journal (2010)

## Content

{BODY_SENTENCE} Their membrane proteome was mapped by mass spectrometry.
"""


@pytest.fixture
def publications_dir(tmp_path: Path) -> Path:
    """A publications cache holding one record in the canonical layout."""
    directory = tmp_path / "publications"
    directory.mkdir()
    (directory / "PMID_99999901.md").write_text(RECORD)
    return directory


@pytest.mark.parametrize(
    "quote,expected",
    [
        (TITLE, True),
        (BODY_SENTENCE, True),
        ("Defining the membrane proteome", True),
        ("This sentence is in neither the title nor the abstract.", False),
    ],
)
def test_repo_validator_matches_title_and_body(publications_dir, quote, expected):
    validator, _ = build_supporting_text_validator(publications_dir)
    assert validator is not None
    assert validator.validate(quote, REFERENCE_ID).is_valid is expected


def test_quote_must_fall_within_title_or_body_not_across_both(publications_dir):
    """The title is a separate text: a quote running from it into the body still fails."""
    validator, _ = build_supporting_text_validator(publications_dir)
    spanning = f"{TITLE} {BODY_SENTENCE}"
    assert validator.validate(spanning, REFERENCE_ID).is_valid is False


@pytest.mark.parametrize(
    "reference_id,expected",
    [
        ("PMID:1", ["Body text.", "A Title"]),
        ("DOI:10.1/x", ["Body text.", "A Title"]),
        ("file:human/X/X-notes.md", ["Body text."]),
        ("Reactome:R-HSA-1", ["Body text."]),
    ],
)
def test_title_is_searchable_only_for_literature(reference_id, expected):
    install_title_matching()
    reference = ReferenceContent(
        reference_id=reference_id, content="Body text.", title="A Title"
    )
    assert SupportingTextValidator.searchable_texts(reference) == expected


def test_install_is_idempotent():
    install_title_matching()
    install_title_matching()
    reference = ReferenceContent(
        reference_id="PMID:1", content="Body text.", title="A Title"
    )
    assert SupportingTextValidator.searchable_texts(reference) == [
        "Body text.",
        "A Title",
    ]


def test_untitled_reference_is_unchanged():
    install_title_matching()
    reference = ReferenceContent(reference_id="PMID:1", content="Body text.")
    assert SupportingTextValidator.searchable_texts(reference) == ["Body text."]


@pytest.mark.parametrize(
    "quote,expected_code", [(TITLE, 0), ("Not in this paper at all, anywhere.", 1)]
)
def test_reference_cli_matches_title(publications_dir, quote, expected_code):
    """``scripts/run_reference_validator.sh`` goes through this entry point."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "ai_gene_review.validation.reference_cli",
            "validate",
            "text",
            quote,
            REFERENCE_ID,
            "--cache-dir",
            str(publications_dir),
            "--no-full-text",
        ],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == expected_code, result.stdout + result.stderr
