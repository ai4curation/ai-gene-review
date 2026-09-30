"""Synthetic checks for primer orientation, coordinates and 5-prime trimming."""

import unittest

from analyze import primer_hits


class PrimerHitsTest(unittest.TestCase):
    def test_forward_full_length(self):
        self.assertEqual(primer_hits("TTACGTACTT", "ACGTAC", "forward", 4), [
            {"start": 3, "end": 8, "matched_bases": 6, "five_prime_trim": 0},
        ])

    def test_reverse_complement(self):
        self.assertEqual(primer_hits("TTTACGTTAGCCC", "CTAACG", "reverse", 6), [
            {"start": 5, "end": 10, "matched_bases": 6, "five_prime_trim": 0},
        ])

    def test_five_prime_tail_and_multiple_hits(self):
        self.assertEqual(primer_hits("AACCGGTTAACCGGTT", "CCAACC", "forward", 4), [
            {"start": 1, "end": 4, "matched_bases": 4, "five_prime_trim": 2},
            {"start": 9, "end": 12, "matched_bases": 4, "five_prime_trim": 2},
        ])

    def test_reverse_five_prime_tail(self):
        self.assertEqual(primer_hits("TTTACGTTAGCCC", "AACTAACG", "reverse", 6), [
            {"start": 5, "end": 10, "matched_bases": 6, "five_prime_trim": 2},
        ])

    def test_prefers_longest_match(self):
        self.assertEqual(primer_hits("TTACGTACGGGTAC", "ACGTAC", "forward", 4), [
            {"start": 3, "end": 8, "matched_bases": 6, "five_prime_trim": 0},
        ])

    def test_no_match(self):
        self.assertEqual(primer_hits("AAAAAA", "CCCC", "forward", 4), [])

    def test_match_below_minimum_is_rejected(self):
        self.assertEqual(primer_hits("AACCGGTT", "CCAACC", "forward", 5), [])


if __name__ == "__main__":
    unittest.main()
