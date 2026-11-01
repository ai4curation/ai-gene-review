# aah3 bioinformatics: closeness of the ISS donor

Script: `pairwise_identity.py` (run with `uv run --no-project --with biopython python pairwise_identity.py`).
Local Smith-Waterman alignment, BLOSUM62, gap open -10, extend -0.5; sequences fetched live from UniProt.

| query | subject | identities / aligned pairs | % identity |
|---|---|---|---|
| Q9Y7S9 (S. pombe Aah3) | A2QTS4 (A. niger AgtA) | 208 / 520 | 40.0 |
| O74922 (S. pombe Aah1) | A2QTS4 (A. niger AgtA) | 208 / 496 | 41.9 |
| Q9Y7S9 (S. pombe Aah3) | O74922 (S. pombe Aah1) | 237 / 529 | 44.8 |

Interpretation: Aah3 and Aah1 are each about 40% identical to AgtA over almost their full length,
and about 45% identical to each other. That is close enough for a family-level transfer within the
GPI-anchored GH13 alpha-amylase-like group, but it does not make AgtA a one-to-one ortholog:
UniProt places AgtA (PTHR10357:SF220), Aah3 (SF224) and Aah1 (SF215) in different PANTHER
subfamilies. The transferred activity is a reasonable inference, not a demonstration.
