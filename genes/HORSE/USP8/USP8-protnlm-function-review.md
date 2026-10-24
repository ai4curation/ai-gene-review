# USP8: ProtNLM function-description review

**Finding: Supported conserved deubiquitinase function.**

Target: [A0A9L0T7K6](https://www.uniprot.org/uniprotkb/A0A9L0T7K6/entry), Equus caballus. The exact source is the frozen [ProtNLM API](https://rest.uniprot.org/uniprotkb/A0A9L0T7K6?annotation=protnlm) response dated 2026-09-08, retained in `projects/PROTNLM_EVALUATION/mammal-benchmark/predictions.jsonl.gz`.

## Original prediction

> Deubiquitinating enzyme that removes conjugated ubiquitin from specific proteins to regulate different cellular processes

## Atomic claims

### Removes conjugated ubiquitin from proteins

**Supported.** Recombinant and immunoprecipitated human UBPY/USP8 cleave linear and isopeptide-linked ubiquitin chains (PMID:9628861). The selected horse protein retains the USP8 catalytic architecture with 91.82% paired sequence identity across 99.46% of the human reference.

### Regulates different cellular processes through selected substrates

**Supported at this broad level.** Human studies connect USP8 to endosomal sorting, EGFR trafficking and substrate stability. This broad wording does not assert a particular horse-specific substrate or disease phenotype.

## Evidence and limits

Existing horse GOA already includes cysteine-type deubiquitinase activity and protein deubiquitination. Deubiquitination can participate in ubiquitin-dependent catabolism by controlling cargo sorting; a deubiquitinase label alone does not refute the accompanying catabolic-process GO prediction. Training membership is unknown.

The reproducible [paired sequence comparison](USP8-bioinformatics/RESULTS.md) records residue-level findings and sequence hashes. The [human UniProt source](../../human/USP8/USP8-uniprot.txt) distinguishes experimental supporting papers from inferred statements. ARBA assertions and generated review prose are not used as validating evidence.
