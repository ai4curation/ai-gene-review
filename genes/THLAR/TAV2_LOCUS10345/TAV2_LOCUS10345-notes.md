# TAV2_LOCUS10345: BCAT4-like methionine aminotransferase

## Identity and inference

UniProtKB A0AAU9S298, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS10345; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS10345 encodes a predicted BCAT4-like, pyridoxal-phosphate-dependent aminotransferase in field pennycress. Its close relationship to Arabidopsis BCAT4 supports a role in converting methionine to the corresponding 2-oxo acid at the entry to glucosinolate side-chain elongation. Branched-chain amino-acid transamination is a secondary inferred biochemical capacity. Native substrate preferences and cellular localization have not been measured for this protein.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:17056707](https://pubmed.ncbi.nlm.nih.gov/17056707/): Arabidopsis recombinant BCAT4 and knockout analyses establish methionine-chain-elongation specialization and cytosolic localization. These are homolog data, not pennycress target assays.
- [PMID:18162591](https://pubmed.ncbi.nlm.nih.gov/18162591/): Arabidopsis BCAT3 assays and mutant profiles support branched-chain and methionine-related transamination; terminal elongated substrates are distinct from unelongated methionine.

## Annotation decisions

- GO:0003824 catalytic activity: MODIFY. The reciprocal BCAT4 match (82.7% identity over 99.4% query coverage), BCAT4 subfamily membership and Arabidopsis biochemical evidence support specific catalytic descendants. List both the primary methionine activity and secondary branched-chain activity; no native target kinetics are claimed.
- GO:0004084 branched-chain-amino-acid:2-oxoglutarate transaminase activity: KEEP_AS_NON_CORE. BCAT-family architecture supports this chemistry, and Arabidopsis BCAT4 can turn over branched-chain substrates. The closest homolog is specialized primarily toward methionine-derived glucosinolate precursors, so this precise but peripheral activity is retained as non-core.
- GO:0009081 branched-chain amino acid metabolic process: MARK_AS_OVER_ANNOTATED. The InterPro family mapping conflates enzyme ancestry and residual substrate turnover with physiological pathway use. Arabidopsis BCAT4 is recruited to methionine chain elongation; the target-specific reciprocal match supports that specialization. Branched-chain catalytic capacity alone does not establish a native pennycress metabolic role in this process.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS10345-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.
