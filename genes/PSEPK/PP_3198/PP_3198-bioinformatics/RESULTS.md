# PP_3198 FdeD ortholog analysis

## Method

UniProt FASTA records for Q88I04 (P. putida KT2440 PP_3198) and D8J0W8
(Herbaspirillum seropedicae Hsero_1006, the proposed FdeD counterpart) were
fetched on demand and aligned globally with Biopython PairwiseAligner, BLOSUM62,
gap-open -10, and gap-extension -0.5. Identity is calculated over columns
containing a residue from both proteins.

## Results

- Q88I04 length: 112 aa
- D8J0W8 length: 112 aa
- Aligned residue pairs: 103
- Identical aligned residues: 47
- Pairwise identity over aligned residue pairs: 45.6%
- KEGG target mapping: `ppu:PP_3198 -> ko:K26179`
- KEGG R13074 summary: `DEFINITION  Naringenin <=> 5,7,8-Trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one
COMMENT     hydroxylation`

Both proteins are compact Rieske [2Fe-2S]-domain proteins. The similarity and
conserved cysteine/histidine-rich region support orthology, but neither sequence
comparison nor the Herbaspirillum pathway paper establishes which enzyme accepts
electrons from FdeD or whether FdeD is required for KEGG reaction R13074.

## Reproduction

```bash
uv run genes/PSEPK/PP_3198/PP_3198-bioinformatics/analyze_fded_ortholog.py
```
