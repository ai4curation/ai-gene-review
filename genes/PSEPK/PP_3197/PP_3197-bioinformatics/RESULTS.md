# PP_3197 FdeC ortholog analysis

## Method

UniProt FASTA records for Q88I05 (P. putida KT2440 PP_3197) and D8J0W7
(Herbaspirillum seropedicae Hsero_1005/FdeC) were fetched on demand and aligned
globally with Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension
-0.5. Identity is calculated over columns containing a residue from both
proteins.

## Results

- Q88I05 length: 313 aa
- D8J0W7 length: 308 aa
- Aligned residue pairs: 305
- Identical aligned residues: 212
- Pairwise identity over aligned residue pairs: 69.5%
- Reported C-terminal motif `GCEHFTFHMG`: present at Q88I05 residues 214-223 and D8J0W7 residues 207-216

The high whole-protein identity and identical motif support an ISS relationship
between PP_3197 and the experimentally characterized Hsero_1005 FdeC. They do
not constitute direct evidence that PP_3197 uses the same substrate, metal, or
reaction conditions in KT2440.

## Reproduction

```bash
uv run genes/PSEPK/PP_3197/PP_3197-bioinformatics/analyze_fdec_ortholog.py
```
