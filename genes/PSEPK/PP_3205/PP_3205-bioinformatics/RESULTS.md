# PP_3205 FdeI ortholog analysis

## Method

Q88HZ7 and D8J0X3 were fetched from UniProt and aligned globally with
Biopython PairwiseAligner, BLOSUM62, gap-open -10, and gap-extension -0.5.
KEGG mapping and reaction records were fetched through KEGG REST.

## Results

- Q88HZ7 length: 330 aa
- D8J0X3 length: 327 aa
- Aligned residue pairs: 321
- Identical aligned residues: 200
- Pairwise identity over aligned residue pairs: 62.3%
- KEGG target mapping: `ppu:PP_3205	ko:K26185`
- KEGG reaction summaries: `R13078: DEFINITION  5-Hydroxy-5-(4-hydroxyphenyl)-3-oxopentanoate <=> 4-Hydroxy-4-(4-hydroxyphenyl)-butan-2-one + CO2
COMMENT     decarboxylation
            unclear reaction | R13079: DEFINITION  4-Hydroxy-4-(4-hydroxyphenyl)-butan-2-one <=> 4-Hydroxycinnamoylmethane + H2O
COMMENT     unclear reaction`

The high whole-protein similarity and shared fumarylacetoacetate-hydrolase-like
architecture support an FdeI orthology relationship. KEGG marks both reactions
unclear; R13078 is a predicted decarboxylation, whereas R13079 eliminates water.
Neither reaction has been demonstrated for either protein.

## Reproduction

```bash
uv run genes/PSEPK/PP_3205/PP_3205-bioinformatics/analyze_fdei_ortholog.py
```
