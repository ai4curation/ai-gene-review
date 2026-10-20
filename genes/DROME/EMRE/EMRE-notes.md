# EMRE (CG17680) review notes

UniProt Q7JX57 (Essential MCU regulator, mitochondrial); PANTHER PTHR33904.

## Literature journal

- EMRE null mutants lack fast uptake [PMID:31042479 "As with MCU1, analysis of these EMRE mutants revealed that they all exhibit no fast mitochondrial Ca2+ uptake"].
- Fly MCU requires EMRE [PMID:27099988 "metazoan MCU homologues from C. elegans and D. melanogaster require EMRE to transport Ca2+"].
- MCU:EMRE overexpression toxicity suppressed by MICU1 [PMID:31042479 "Co-expression of either MICU1-A or MICU1-B with MCU and EMRE prevented the MCU:EMRE phenotype (Figure 5B)."]
- Innate immunity rows come from a genome-wide RNAi survival screen (PMID:19520911); CG17680 is not named in the cached text.

## Curation decisions

- contributes_to calcium channel activity ACCEPTED as core (non-pore essential subunit).
- Uniporter module conventions as in MCU-notes.md.
- Positive regulation of innate immune response marked over-annotated; defense response to Gram-negative bacterium kept as non-core.

## Deep research

`EMRE-deep-research-falcon.md` (falcon) arrived after the review was first committed. It agrees with the review: EMRE is an essential non-pore accessory subunit of the uniporter, required for fast MCU-dependent calcium uptake (EMRE knockdown in larval muscle is not bypassed by raising MCU; three CRISPR alleles lack fast uptake). It does not discuss the innate-immunity screen rows. No annotation decision changed.
