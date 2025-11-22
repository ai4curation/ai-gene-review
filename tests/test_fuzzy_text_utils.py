"""Tests for optimized fuzzy text matching utilities."""

import pytest
from ai_gene_review.validation.fuzzy_text_utils import (
    find_fuzzy_match_in_text,
    find_fuzzy_match_with_context,
    normalize_whitespace,
    calculate_text_similarity,
    split_into_sentences,
)


class TestNormalizeWhitespace:
    """Tests for text normalization."""

    def test_basic_normalization(self):
        text = "Text  with\nmultiple   spaces"
        assert normalize_whitespace(text) == "text with multiple spaces"

    def test_leading_trailing_whitespace(self):
        text = "  Leading and trailing  "
        assert normalize_whitespace(text) == "leading and trailing"

    def test_mixed_case(self):
        text = "MixedCase TEXT"
        assert normalize_whitespace(text) == "mixedcase text"


class TestSplitIntoSentences:
    """Tests for sentence splitting."""

    def test_basic_split(self):
        text = "This is the first longer sentence. This is the second longer sentence!"
        sentences = split_into_sentences(text)
        assert len(sentences) == 2

    def test_filters_short_sentences(self):
        text = "Short. This is a sentence that is longer than twenty characters."
        sentences = split_into_sentences(text)
        assert len(sentences) == 1
        assert "longer than twenty" in sentences[0]


class TestFindFuzzyMatch:
    """Tests for fuzzy matching in large documents."""

    @pytest.fixture
    def sample_text(self):
        return "The JAK1 protein is a tyrosine kinase. It phosphorylates STAT proteins."

    def test_exact_match(self, sample_text):
        found, score, match = find_fuzzy_match_in_text(
            "JAK1 protein is a tyrosine kinase", sample_text
        )
        assert found is True
        assert score >= 90

    def test_short_query_requires_exact_match(self, sample_text):
        # Less than 5 words requires exact match
        found, score, match = find_fuzzy_match_in_text(
            "JAK1 is kinase", sample_text  # Only 3 words
        )
        assert found is False

    def test_no_match(self, sample_text):
        found, score, match = find_fuzzy_match_in_text(
            "completely different text here", sample_text
        )
        assert found is False

    def test_performance_on_large_text(self):
        """Ensure fuzzy matching is fast even on very large documents."""
        import time

        # Create a large document (simulate 10K words)
        large_text = " ".join(["word"] * 10000)
        query = "This query text should not be found anywhere in the document at all"

        start = time.time()
        found, score, match = find_fuzzy_match_in_text(query, large_text)
        elapsed = time.time() - start

        # Should complete in under 100ms even on large documents
        assert elapsed < 0.1
        assert found is False


class TestFindFuzzyMatchWithContext:
    """Tests for fuzzy matching with context."""

    def test_finds_match_with_context(self):
        text = "The JAK1 protein is a tyrosine kinase that activates STAT proteins."
        found, score, context, start, end = find_fuzzy_match_with_context(
            "tyrosine kinase", text, threshold=80
        )

        assert found is True
        assert "tyrosine kinase" in context.lower()
        assert start is not None
        assert end is not None


class TestCalculateTextSimilarity:
    """Tests for text similarity calculation."""

    def test_identical_text(self):
        score = calculate_text_similarity("hello world", "hello world")
        assert score == 100.0

    def test_word_reordering(self):
        # token_sort_ratio handles word reordering
        score = calculate_text_similarity("the cat sat", "sat the cat")
        assert score == 100.0

    def test_different_text(self):
        score = calculate_text_similarity("hello world", "goodbye universe")
        assert 0 < score < 50


@pytest.mark.integration
class TestRealWorldScenarios:
    """Integration tests with real-world scenarios."""

    def test_publication_sized_document(self):
        """Test with a document similar in size to actual publications."""
        # Create a ~1000 word document
        document = """
        The protein HglS is a 2-oxoadipate dioxygenase that plays a crucial role
        in lysine catabolism. It catalyzes the conversion of 2-oxoadipate to
        D-2-hydroxyglutarate through an iron-dependent mechanism.
        """ * 200  # Repeat to make it larger

        query = "HglS is a 2-oxoadipate dioxygenase that plays a crucial role"

        found, score, match = find_fuzzy_match_in_text(query, document)

        assert found is True
        assert score >= 90

    def test_no_false_positives_on_dissimilar_text(self):
        """Ensure we don't get false positives with default threshold."""
        document = "This is completely unrelated text about molecular biology."
        query = "quantum physics and particle accelerators in modern science"

        found, score, match = find_fuzzy_match_in_text(query, document)

        assert found is False
