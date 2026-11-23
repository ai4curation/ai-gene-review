# TAV2_LOCUS15930: BCAT3-like aminotransferase

## Identity and inference

UniProtKB A0AAU9SEL1, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS15930; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS15930 encodes a predicted plastidic BCAT3-like aminotransferase in field pennycress. It is inferred to catalyze reversible transamination of branched-chain amino acids and their 2-oxo acids and to participate in the terminal transamination of elongated methionine precursors for glucosinolate biosynthesis. Its pyridoxal-phosphate-dependent catalytic architecture is conserved, but native reaction rates, chain-length preferences and localization remain unmeasured.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:18162591](https://pubmed.ncbi.nlm.nih.gov/18162591/): Arabidopsis BCAT3 assays and mutant profiles support branched-chain and methionine-related transamination; terminal elongated substrates are distinct from unelongated methionine.

## Annotation decisions

- GO:0003824 catalytic activity: MODIFY. The BCAT3-specific reciprocal match and target RuleBase reaction statements support branched-chain amino-acid transamination; Arabidopsis BCAT3 also accepts methionine. Its terminal elongated-methionine reaction is chemically distinct and will be represented separately rather than silently included in GO:0010326.
- GO:0004084 branched-chain-amino-acid:2-oxoglutarate transaminase activity: ACCEPT. Target RuleBase catalytic statements independently support leucine, isoleucine and valine reactions, while the BCAT3-specific match agrees with direct Arabidopsis enzyme assays. The collective term captures the substrate class; no native quantitative ranking or direction of flux is asserted.
- GO:0009081 branched-chain amino acid metabolic process: ACCEPT. The close BCAT3 relationship and conserved catalytic reactions support the existing metabolic assignment. The broad metabolic direction is retained because native pennycress anabolic versus catabolic flux has not been measured; homolog activity also supports a distinct glucosinolate role.
- GO:0009507 chloroplast: ACCEPT. The nearly full-length 88.9%-identity BCAT3 match and specific subfamily placement support the comparative plastid assignment. The source Arabidopsis enzyme is plastid-localized; this is not a target localization experiment.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS15930-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.
