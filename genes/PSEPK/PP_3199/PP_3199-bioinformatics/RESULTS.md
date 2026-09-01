# PP_3199 FdeE ortholog analysis

## Method

UniProt FASTA records for Q88I03 (P. putida KT2440 PP_3199) and D8J0W9
(Herbaspirillum seropedicae Hsero_1007/FdeE) were fetched on demand and aligned
globally with Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension
-0.5. Identity is calculated over columns containing a residue from both
proteins.

## Results

- Q88I03 length: 374 aa
- D8J0W9 length: 376 aa
- Aligned residue pairs: 374
- Identical aligned residues: 151
- Pairwise identity over aligned residue pairs: 40.4%
- `GGGIGG`: not found identically in both sequences
- `GADG`: present at Q88I03 residues 157-160 and D8J0W9 residues 158-161
- `GDAAH`: not found identically in both sequences

The whole-protein similarity, shared monooxygenase architecture, and conserved
flavonoid-degradation locus support an ISS relationship between PP_3199 and the
experimentally characterized Hsero_1007 FdeE. They do not constitute direct
evidence that PP_3199 has identical substrate range, regioselectivity, or
cofactor preference in KT2440.

## Reproduction

```bash
uv run genes/PSEPK/PP_3199/PP_3199-bioinformatics/analyze_fdee_ortholog.py
```
