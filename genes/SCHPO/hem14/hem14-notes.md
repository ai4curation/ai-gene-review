# hem14 (SPAC1F5.07c) notes

UniProt Q10062, protoporphyrinogen oxidase [UniProt:Q10062].

- Deep research was unavailable for this gene: `just deep-research SCHPO hem14 --provider perplexity` failed (no provider API key; the prompt template is absent from this sparse checkout), so no -deep-research file exists. The review is based on the UniProt record, the PomBase GOA rows, cached publications, and the S. cerevisiae HEM14 review in this repository.
- Function assigned by orthology to S. cerevisiae HEM14 and the PANTHER family (IBA); see the review rows for quotes.
- Location rows from the ORFeome YFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"] are abstract-only here; gene-level calls are in the dataset.
- PAINT places an IRD NOT mitochondrial inner membrane (GO:0005743) at the S. pombe node PTN000077950 of PTHR42923 (interpro/panther/PTHR42923/PTHR42923-paint.tsv), and the ORFeome screen (PMID:16823372) recorded cytosolic and nuclear YFP signal. The mitochondrial location rests only on orthology (UniProt ECO:0000250). The ORFeome screen also reports non-mitochondrial signal for hem15, a near-certain mitochondrial enzyme, so C-terminal tag/overexpression artefacts are plausible. Decision: extramitochondrial HDA rows MARK_AS_OVER_ANNOTATED (the earlier UNDECIDED cytosol row resolved this way); localization flagged as a question/experiment.
