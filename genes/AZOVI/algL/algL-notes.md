# AZOVI algL: alginate polymerization/export review

## Identity and scope

O52195, 374 aa; ATCC 9046 AF027499/AAC04567.1 plus strain E AF037600/AAC32313.1. PMID9683471 assays the strain E sequence; PMID12664154 tests an ATCC 9046 nonpolar mutant. PL5 family, HAMAP MF_00557, IPR022859; no PANTHER cross-reference. All records retain species-level NCBITaxon:354; none is silently relabeled as strain DJ.

## Source-specific findings

- [PMID:9683471](https://pubmed.ncbi.nlm.nih.gov/9683471/): Direct recombinant strain E AlgL enzymology, signal processing and cleavage specificity. The native gene is represented with ATCC 9046 and strain E sequence provenance in the target record.
- [PMID:12664154](https://pubmed.ncbi.nlm.nih.gov/12664154/): Native nonpolar ATCC 9046 algL mutant remains an alginate producer and produces higher-molecular-weight polymer. Supports molecular-weight control and cautions against transferring absolute essentiality from other species.

## Annotation decisions

- GO:0016829 (IEA): MODIFY. The broad activity is correct but direct target cleavage specificity supports GO:0045135, which is already present twice. Live QuickGO confirms that this term is a descendant of both broad lyase terms. This judges reaction specificity consistently across electronic and experimental evidence.
- GO:0016837 (IEA): MODIFY. The broad activity is correct but direct target cleavage specificity supports GO:0045135, which is already present twice. Live QuickGO confirms that this term is a descendant of both broad lyase terms. This judges reaction specificity consistently across electronic and experimental evidence.
- GO:0042122 (IEA): ACCEPT. Direct target cleavage and the native higher-molecular-weight mutant phenotype support alginate catabolism. Breakdown during production is still catabolism; this does not imply growth on alginate as a carbon source or universal essentiality for export.
- GO:0042597 (IEA): ACCEPT. The curated HAMAP location and N-terminal export signal support periplasmic localization. The primary study observes signal cleavage during heterologous production, which is consistent with export but is not native compartment fractionation.
- GO:0045135 (EXP): ACCEPT. Recombinant strain E AlgL directly cleaves M-M and M-G but not G-M or G-G bonds. Both evidence rows represent this supported reaction; no row is discarded as redundant. Activity on acetylated substrate is qualified by acetylation extent, and other Azotobacter lyases are not conflated with AlgL.
- GO:0045135 (IEA): ACCEPT. Recombinant strain E AlgL directly cleaves M-M and M-G but not G-M or G-G bonds. Both evidence rows represent this supported reaction; no row is discarded as redundant. Activity on acetylated substrate is qualified by acetylation extent, and other Azotobacter lyases are not conflated with AlgL.

No cached GO-CAM index match for this accession. Original source/evidence/term fields were preserved. No NEW process annotations were proposed. Live QuickGO definitions were checked for reaction specificity; AlgL GO:0045135 is a descendant of both seeded generic lyase terms. Alg8 substrate corrections are lateral, not ontology-ancestry claims. For AlgG, exact polymer epimerase chemistry is represented by a supported proposed term rather than a guessed GO identifier.

## Research provenance

Applied review, annotation-reviewer and core-function-synthesizer guidance. Default Falcon deep research and fetch-gene-pmids ran concurrently. Falcon failed authentication (403); Perplexity-lite fallback failed with insufficient_quota (401). No provider report was fabricated. Fitness retrieval was attempted but no reachable FEBA source or local AZOVI mapping yielded data; no fitness artifact was written. These failures are missing evidence, not negative phenotypes. Logs are /tmp/azovi-poly-algL-deep.log and /tmp/azovi-poly-algL-fitness.log. Manual primary research and curated-record assessments supply the review.

## Verified family selector labels

IPR022859 — Alginate lyase (family). Actual membership is present in the target UniProt cross-references; official InterPro labels/types were checked against the live InterPro API. No PTN evolutionary placement is inferred.

## 2026-10-26 quotation-source QA

Expanded the periplasm quotation to include the verbatim SUBCELLULAR LOCATION prefix, so automated record-section assignment distinguishes the curated location statement from the Periplasm keyword. No annotation action or original machine field changed.
