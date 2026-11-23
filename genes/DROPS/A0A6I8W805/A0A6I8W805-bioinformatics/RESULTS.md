# A0A6I8W805 (LOC117183218 isoform X1): mapping onto Herc4

Script: `map_to_herc4.py` (run with `uv run map_to_herc4.py`); raw output in
`map_to_herc4-output.txt`. Data: UniProt REST and AlphaFold DB API, queried 2026-10-21.
Isoform relationships for the gene are in
`genes/DROPS/A0A6I8W8A2/A0A6I8W8A2-bioinformatics/RESULTS.md`.

## Domain architecture

A0A6I8W805 (282 aa, PANTHER PTHR22872, no subfamily) has three RCC1 repeats
(50-144, 145-200, 201-255) and no HECT domain.

## Alignment to relatives

| Comparator | PANTHER | RCC1 repeats | HECT | Identity | X1 range | Comparator range |
|---|---|---|---|---|---|---|
| D. pseudoobscura Herc4 (A0A6I8W510, 1052 aa) | PTHR45622:SF76 | 7 | 726-1052 | 165/218 (76%) | 50-270 | 1-227 |
| D. melanogaster Herc4 (Q9W0H2, 1058 aa) | PTHR45622:SF76 | 7 | 732-1058 | 136/216 (63%) | 52-270 | 7-231 |
| D. pseudoobscura LOC6903915 (A0A6I8W7D9, 332 aa) | PTHR22872 | 6 | none | 202/221 (91%) | 50-270 | 1-221 |

X1 residues 50-270 match the first ~227 residues of Herc4, which span roughly the
first four of Herc4's seven RCC1 repeats (Herc4 repeats 1-54, 55-104, 105-157,
158-212, and the start of 213-264). X1 residues 1-49 do not align to Herc4. X1
therefore carries only about half of a seven-bladed RCC1-like propeller.

AlphaFold DB mean pLDDT for A0A6I8W805 is 58.8 (low confidence), consistent with
a partial propeller that does not fold as a complete domain on its own. This is
a prediction, not an experimental structure.

## Interpretation

- The gene is best explained as a partial duplicate of the N-terminal half of the
  Herc4 RCC1-like domain (higher identity to D. pseudoobscura Herc4 than to
  D. melanogaster Herc4; closest relative is the RCC1-only paralog LOC6903915).
  This is a pairwise-identity inference, not a phylogenetic tree.
- Herc4 is in PANTHER PTHR45622:SF76; this gene is in PTHR22872 with no
  subfamily. The HECT-dependent E3 ligase activity of Herc4 cannot be
  transferred.
- Jiang et al. 2019 (PMID:30925584) showed that the Herc4 RCC1-like domain alone
  can bind Smoothened by co-IP. Whether a half-propeller fragment like X1 retains
  any such binding is untested.
