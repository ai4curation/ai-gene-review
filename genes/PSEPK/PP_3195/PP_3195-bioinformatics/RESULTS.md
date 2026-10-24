# PP_3195 FdeB ortholog analysis

## Method

UniProt FASTA records for Q88I07 (P. putida KT2440 PP_3195) and D8J0W6
(Herbaspirillum seropedicae Hsero_1004, the proposed FdeB counterpart) were
fetched on demand and aligned globally with Biopython PairwiseAligner, BLOSUM62,
gap-open -10, and gap-extension -0.5. Identity is calculated over columns
containing a residue from both proteins.

## Results

- Q88I07 length: 420 aa
- D8J0W6 length: 386 aa
- Aligned residue pairs: 385
- Identical aligned residues: 314
- Pairwise identity over aligned residue pairs: 81.6%
- Target nucleophile-motif candidate `GVSLG`: present at Q88I07 residues 266-270 and D8J0W6 residues 231-235

The whole-protein similarity and shared alpha/beta-hydrolase architecture
support an orthology relationship. Neither protein has direct biochemical
evidence for KEGG reaction R13077, so the alignment does not establish the
flavonoid-derived lactone substrate.

## Reproduction

```bash
uv run genes/PSEPK/PP_3195/PP_3195-bioinformatics/analyze_fdeb_ortholog.py
```
