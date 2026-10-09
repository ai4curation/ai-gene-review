# unc79 (CG5237, dunc79) review notes

Expected accession Q9VDY5 (isoform C, TrEMBL). `just fetch-gene DROME unc79` first resolved to E1JIP9 (isoform B), which carries the same 4 GOA rows; the review was refetched by accession (`just fetch-gene DROME Q9VDY5 --alias unc79`) to match the module.

## Literature journal

- unc79 mutants phenocopy na in anesthesia [PMID:17350263 "in Drosophila, mutations that inactivate the unc-79 ortholog produce an na phenotype"]
  and UNC-79 family proteins control NA levels [PMID:17350263 "biochemical studies show that proteins of the UNC-79 family control NA protein levels by a posttranscriptional mechanism"].
- Complex [PMID:24223770 "Immunoprecipitation experiments also confirm that UNC79 and UNC80 form a complex with NA in the Drosophila brain."]
- Circadian [PMID:24223770 "These mutants display severe defects in circadian locomotor rhythmicity that are indistinguishable from na mutant phenotypes."]

## Curation decisions

- ND root MF -> sodium channel activity (contributes_to), consistent with unc80.
- Complex -> sodium channel complex (consistent across NA complex).
