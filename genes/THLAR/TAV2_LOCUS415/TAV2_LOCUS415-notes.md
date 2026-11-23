# TAV2_LOCUS415: SOT17-like desulfoglucosinolate sulfotransferase

## Identity and inference

UniProtKB A0AAU9RDZ2, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS415; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS415 encodes a predicted SOT17-like sulfotransferase in field pennycress. Its close relationship to Arabidopsis SOT17 supports transfer of sulfate from PAPS to desulfoglucosinolates in the final step of glucosinolate core biosynthesis. Both aliphatic and aromatic desulfoglucosinolate activities are inferred, while quantitative preferences among chain lengths and native tissue expression remain unresolved.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:16367753](https://pubmed.ncbi.nlm.nih.gov/16367753/): The accessible abstract describes Arabidopsis SOT16/17/18 enzyme assays with desulfoglucosinolates and cytoplasmic localization. Target substrate preference and localization are not directly measured.
- [PMID:19077143](https://pubmed.ncbi.nlm.nih.gov/19077143/): The accessible abstract reports Arabidopsis SOT17 chain-length-dependent activity and substrate comparisons. These support desulfoglucosinolate sulfation but not a quantitative pennycress chain-length preference.

## Annotation decisions

- GO:0008146 sulfotransferase activity: MODIFY. The 91.9%-identity reciprocal SOT17 match over 99.4% query coverage, together with the sulfotransferase domain, supports desulfoglucosinolate substrates beyond the family-wide term. Characterized Arabidopsis SOT17 acts on aliphatic and aromatic substrates; list both supported descendants without transferring exact chain-length preferences, kinetic constants or tissue expression.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS415-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.

## 2026-10-26 independent evidence-selection QA

Matched supporting quotations to the actual claim: specific SOT17 reciprocal mapping rather than the neighboring SOT18 search row, positive MAM condensation evidence for the functional claim, and direct homolog localization text where localization is inferred. Only relevant corrections apply to this gene. Annotation actions and all seeded fields are unchanged.
