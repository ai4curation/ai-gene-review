# PP_3206 FdeJ ortholog analysis

## Method

UniProt FASTA records for Q88HZ6 (P. putida KT2440 PP_3206) and D8J0X4
(Herbaspirillum seropedicae Hsero_1012, the proposed FdeJ counterpart) were
fetched on demand and aligned globally with Biopython PairwiseAligner, BLOSUM62,
gap-open -10, and gap-extension -0.5. Identity is calculated over columns
containing a residue from both proteins.

## Results

- Q88HZ6 length: 328 aa
- D8J0X4 length: 320 aa
- Aligned residue pairs: 311
- Identical aligned residues: 159
- Pairwise identity over aligned residue pairs: 51.1%

The whole-protein similarity and shared epimerase/dehydratase architecture
support an orthology relationship. Neither protein has direct biochemical
evidence for KEGG reaction R13076, so the alignment does not establish the
substrate or carbon-carbon hydrolase chemistry.

## Reproduction

```bash
uv run genes/PSEPK/PP_3206/PP_3206-bioinformatics/analyze_fdej_ortholog.py
```
