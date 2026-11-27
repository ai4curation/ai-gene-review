# A0A6I8W8A2 (LOC117183218) identity and relative analysis

Script: `compare_sequences.py` (run with `uv run compare_sequences.py`); raw output in `results-output.txt`.
Data source: UniProt REST (live query, 2026-10-21).

## Products of LOC117183218

| Accession | Length | RefSeq isoform | PANTHER |
|---|---|---|---|
| A0A6I8W805 | 282 | X1 | PTHR22872 (no subfamily) |
| A0A6I8W807 | 233 | X2 | PTHR22870:SF408 |
| A0A6I8W8A2 | 169 | X3 (benchmark) | PTHR22872 (no subfamily) |
| A0A6I8W815 | 144 | X4 | PTHR22872 (no subfamily) |

A0A6I8W8A2 residues 6-169 are identical to A0A6I8W805 (X1) residues 119-282;
only the first five residues differ (MSPLI vs HVCRL), consistent with an
alternative first exon. X3 therefore lacks the first 118 residues of X1,
including part of the first RCC1 repeat, and carries two of the three RCC1
repeats annotated on X1. No product of the gene has a HECT domain (the longest
is 282 aa; a HECT domain alone is ~350 aa).

The four isoforms of one gene are split across two PANTHER families
(PTHR22872 for X1/X3/X4, PTHR22870:SF408 for X2) although they share the same
RCC1 repeats, so the PANTHER placement of this short RLD-only sequence is not
robust.

## Closest relatives (local alignment of X1)

- LOC6903915 (A0A6I8W7D9, 332 aa; D. pseudoobscura chromosome X): 91% identity
  over 221 aligned residues; also RCC1-only, PTHR22872.
- D. pseudoobscura Herc4 (A0A6I8W510 and isoforms, ~1050 aa, HECT-containing):
  76-79% identity over ~210-218 residues of its N-terminal RCC1-like domain;
  PTHR45622:SF76.
- D. melanogaster Herc4 (Q9W0H2/M9PE57, FBgn0035207, HECT-containing):
  63-64% identity over ~215 residues; PTHR45622:SF76.
- D. melanogaster HERC2 (Q9VR91): 38% over 138 residues only.

D. melanogaster has no short RCC1-only counterpart among its IPR000408
proteins, and NCBI Gene reports no orthologs for LOC117183218 (gene 117183218).
Higher identity to D. pseudoobscura Herc4 than to D. melanogaster Herc4
indicates that LOC117183218 (and LOC6903915) arose by partial duplication of
the Herc4 RCC1-like-domain region within the obscura lineage. This is an
inference from pairwise identities, not a phylogenetic tree.

Caveat: the HECT column in `results-output.txt` reflects UniProt FT DOMAIN
lines only; some Herc4 isoform records (e.g. B5DRA3) lack the feature line
even though they are the same ~1050-aa protein.
