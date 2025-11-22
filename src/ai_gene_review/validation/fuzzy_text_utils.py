"""Efficient fuzzy text matching utilities for large documents.

This module provides optimized fuzzy text matching using RapidFuzz,
designed for finding approximate matches of supporting text within
large publication documents (10K-100K+ words).

Key features:
- Fast partial matching using RapidFuzz (40% faster than difflib)
- Returns both similarity scores and match locations
- Handles large documents efficiently with smart optimizations
- Falls back gracefully when matches aren't found
"""

from typing import Optional, List, Tuple
from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein
import re


def normalize_whitespace(text: str) -> str:
    """Normalize whitespace and lowercase for matching.

    Args:
        text: Text to normalize

    Returns:
        Normalized text with whitespace collapsed and lowercased

    Examples:
        >>> normalize_whitespace("Text  with\\nmultiple   spaces")
        'text with multiple spaces'
        >>> normalize_whitespace("  Leading and trailing  ")
        'leading and trailing'
    """
    return re.sub(r'\s+', ' ', text).strip().lower()


def split_into_sentences(text: str, min_length: int = 20) -> List[str]:
    """Split text into sentences for matching.

    Args:
        text: Text to split
        min_length: Minimum sentence length to include

    Returns:
        List of sentences longer than min_length

    Examples:
        >>> sentences = split_into_sentences("This is the first longer sentence. This is the second longer sentence!")
        >>> len(sentences)
        2
        >>> sentences = split_into_sentences("Short. This is a sentence that is longer than twenty characters.")
        >>> len(sentences)
        1
    """
    # Normalize newlines to spaces but preserve paragraph breaks
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"\s+", " ", text)

    # Split on sentence-ending punctuation
    sentences = re.split(r"[.!?]\s+", text)

    # Filter and clean
    return [s.strip() for s in sentences if s.strip() and len(s.strip()) >= min_length]


def find_fuzzy_match_in_text(
    query: str,
    text: str,
    threshold: float = 85.0,
    max_chars: int = 500_000,
) -> Tuple[bool, float, Optional[str]]:
    """Find fuzzy match of query text in a large document using RapidFuzz.

    This function uses a multi-stage approach for efficiency:
    1. Try exact substring match (fastest)
    2. Try sentence-by-sentence partial matching (fast for most cases)
    3. For very small queries (<5 words), fail fast

    Args:
        query: Text to search for (supporting_text from annotation)
        text: Large document to search within (publication content)
        threshold: Minimum similarity score (0-100) to consider a match
        max_chars: Maximum text size to process (safety limit)

    Returns:
        Tuple of (found, similarity_score, best_match_text) where:
        - found: True if similarity >= threshold
        - similarity_score: Float 0-100 indicating match quality
        - best_match_text: The best matching text segment or None

    Examples:
        >>> text = "The JAK1 protein is a tyrosine kinase. It phosphorylates STAT proteins."
        >>> found, score, match = find_fuzzy_match_in_text(
        ...     "JAK1 protein is a tyrosine kinase",
        ...     text
        ... )
        >>> found
        True
        >>> score >= 90
        True

        >>> # Test with minor variation - this won't match due to <5 word threshold
        >>> found, score, match = find_fuzzy_match_in_text(
        ...     "JAK1 is tyrosine kinase",
        ...     text
        ... )
        >>> found  # Only 4 words, requires exact match
        False

        >>> # Test with non-matching text
        >>> found, score, match = find_fuzzy_match_in_text(
        ...     "completely different text here",
        ...     text
        ... )
        >>> found
        False
    """
    # Safety check: skip if text is too large
    if len(text) > max_chars:
        return (False, 0.0, None)

    # Normalize both texts
    query_norm = normalize_whitespace(query)
    text_norm = normalize_whitespace(text)

    # Stage 1: Try exact substring match (fastest - O(n))
    if query_norm in text_norm:
        return (True, 100.0, query)

    # Stage 2: Quick check - if query is very short, require exact match
    query_words = query_norm.split()
    if len(query_words) < 5:
        return (False, 0.0, None)

    # Stage 3: Sentence-by-sentence matching using RapidFuzz
    # This is much faster than sliding window for large documents
    sentences = split_into_sentences(text)

    best_score = 0.0
    best_match = None

    for sentence in sentences:
        # Use partial_ratio which finds best matching substring
        # This is optimized in RapidFuzz and much faster than our sliding window
        score = fuzz.partial_ratio(query_norm, normalize_whitespace(sentence))

        if score > best_score:
            best_score = score
            best_match = sentence

        # Early exit if we find an excellent match
        if score >= 95:
            return (True, score, sentence)

    # Return result based on threshold
    is_match = best_score >= threshold
    return (is_match, best_score, best_match if is_match else None)


def find_fuzzy_match_with_context(
    query: str,
    text: str,
    threshold: float = 85.0,
    context_words: int = 10,
) -> Tuple[bool, float, Optional[str], Optional[int], Optional[int]]:
    """Find fuzzy match and return the location with surrounding context.

    This is useful for showing users where the match was found in the source.
    Uses RapidFuzz's partial_ratio_alignment to get match positions.

    Args:
        query: Text to search for
        text: Document to search within
        threshold: Minimum similarity score (0-100)
        context_words: Number of words of context to include on each side

    Returns:
        Tuple of (found, score, match_with_context, start_pos, end_pos)

    Examples:
        >>> text = "The JAK1 protein is a tyrosine kinase that activates STAT proteins."
        >>> found, score, context, start, end = find_fuzzy_match_with_context(
        ...     "tyrosine kinase",
        ...     text,
        ...     threshold=80
        ... )
        >>> found
        True
        >>> "tyrosine kinase" in context.lower()
        True
    """
    # Normalize texts
    query_norm = normalize_whitespace(query)
    text_norm = normalize_whitespace(text)

    # Quick exact match check
    if query_norm in text_norm:
        start = text_norm.index(query_norm)
        end = start + len(query_norm)
        return (True, 100.0, query, start, end)

    # Use RapidFuzz for fuzzy matching
    best_score = 0.0
    best_sentence = None
    best_start = None
    best_end = None

    sentences = split_into_sentences(text)
    current_pos = 0

    for sentence in sentences:
        sentence_norm = normalize_whitespace(sentence)
        score = fuzz.partial_ratio(query_norm, sentence_norm)

        if score > best_score:
            best_score = score
            best_sentence = sentence
            # Find approximate position in original text
            best_start = text.lower().find(sentence.lower()[:30])
            if best_start >= 0:
                best_end = best_start + len(sentence)

        if score >= 95:
            break

    if best_score >= threshold and best_sentence:
        return (True, best_score, best_sentence, best_start, best_end)

    return (False, best_score, None, None, None)


def calculate_text_similarity(text1: str, text2: str) -> float:
    """Calculate similarity between two text strings using RapidFuzz.

    Uses token_sort_ratio which handles word order differences well.

    Args:
        text1: First text
        text2: Second text

    Returns:
        Similarity score from 0-100

    Examples:
        >>> calculate_text_similarity("the cat sat", "sat the cat")
        100.0
        >>> score = calculate_text_similarity("hello world", "goodbye world")
        >>> 30 < score < 70
        True
    """
    text1_norm = normalize_whitespace(text1)
    text2_norm = normalize_whitespace(text2)

    # token_sort_ratio handles word reordering
    return fuzz.token_sort_ratio(text1_norm, text2_norm)
