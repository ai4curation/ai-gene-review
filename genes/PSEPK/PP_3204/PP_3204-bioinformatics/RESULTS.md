# PP_3204 FdeH ortholog analysis

## Method

Q88HZ8 and D8J0X2 were fetched from UniProt and aligned globally with
Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension -0.5.
KEGG mapping and reaction records were fetched through KEGG REST.

## Results

- Q88HZ8 length: 195 aa
- D8J0X2 length: 196 aa
- Aligned residue pairs: 184
- Identical aligned residues: 106
- Pairwise identity over aligned residue pairs: 57.6%
- KEGG target mapping: `ppu:PP_3204	ko:K26182`
- KEGG R13075 summary: `DEFINITION  5,7,8-Trihydroxy-2-(4-hydroxyphenyl)-2,3-dihydro-4H-chromen-4-one <=> (2E,4E)-2,4-Dihydroxy-4-[6-(4-hydroxyphenyl)-2,4-dioxodihydro-2H-pyran-3(4H)-ylidene]but-2-enoate
COMMENT     dioxygenation
ORTHOLOGY   K26181  naringenin degradation protein FdeC
            K26182  naringenin degradation protein FdeH`

The whole-protein similarity and cupin architecture support an FdeH orthology
relationship. R13075 is explicitly marked unclear and is assigned to both FdeC
and FdeH; these records do not establish an independent molecular function for
FdeH.

## Reproduction

```bash
uv run genes/PSEPK/PP_3204/PP_3204-bioinformatics/analyze_fdeh_ortholog.py
```
