# AZOVI algG: alginate polymerization/export review

## Identity and scope

P70805, 525 aa; X87973/CAA61231.1; strain E primary sequence and assayed enzyme (PMID8830682). Specific IPR053409 family/domain and curated AlgG family. No PANTHER cross-reference. Avoid the separate 32-aa O52193 fragment. All records retain species-level NCBITaxon:354; none is silently relabeled as strain DJ.

## Source-specific findings

- [PMID:8830682](https://pubmed.ncbi.nlm.nih.gov/8830682/): Direct recombinant strain E AlgG epimerization assay. Low activity is not inactivity; the protein is different from secreted AlgE1–7. Signal-peptide behavior in heterologous E. coli is not a native localization assay.
- [PMID:16855245](https://pubmed.ncbi.nlm.nih.gov/16855245/): Strain E eexDEF mutants lacking exported AlgE1–7 produce almost pure mannuronan, demonstrating the dominance of extracellular epimerases under those conditions. This is not an AlgG knockout or proof of AlgG catalytic absence.

## Annotation decisions

- GO:0042121 (IEA): ACCEPT. Direct recombinant target epimerization establishes a catalytic contribution to alginate biosynthesis. A minor physiological contribution compared with extracellular AlgE1–7 does not negate activity. The additional polymer-protection/scaffold role is supported by homology rather than an Azotobacter structural-complex assay.
- GO:0042597 (IEA): ACCEPT. Both localization rows express the same supported comparative claim. Curated transfer from Pseudomonas AlgG and the target export sequence support the periplasmic assignment. Failure to process the Azotobacter signal in overexpressing E. coli is not evidence of native cytosolic localization; direct native fractionation is not claimed.
- GO:0042597 (ISS): ACCEPT. Both localization rows express the same supported comparative claim. Curated transfer from Pseudomonas AlgG and the target export sequence support the periplasmic assignment. Failure to process the Azotobacter signal in overexpressing E. coli is not evidence of native cytosolic localization; direct native fractionation is not claimed.

No cached GO-CAM index match for this accession. Original source/evidence/term fields were preserved. No NEW process annotations were proposed. Live QuickGO definitions were checked for reaction specificity; AlgL GO:0045135 is a descendant of both seeded generic lyase terms. Alg8 substrate corrections are lateral, not ontology-ancestry claims. For AlgG, exact polymer epimerase chemistry is represented by a supported proposed term rather than a guessed GO identifier.

## Research provenance

Applied review, annotation-reviewer and core-function-synthesizer guidance. Default Falcon deep research and fetch-gene-pmids ran concurrently. Falcon failed authentication (403); Perplexity-lite fallback failed with insufficient_quota (401). No provider report was fabricated. Fitness retrieval was attempted but no reachable FEBA source or local AZOVI mapping yielded data; no fitness artifact was written. These failures are missing evidence, not negative phenotypes. Logs are /tmp/azovi-poly-algG-deep.log and /tmp/azovi-poly-algG-fitness.log. Manual primary research and curated-record assessments supply the review.

## Verified family selector labels

IPR053409 — Mannuronan C5-epimerase (family). Actual membership is present in the target UniProt cross-references; official InterPro labels/types were checked against the live InterPro API. No PTN evolutionary placement is inferred.

## 2026-10-26 quotation-source QA

Expanded the periplasm quotation to include the verbatim SUBCELLULAR LOCATION prefix, so automated record-section assignment distinguishes the curated location statement from the Periplasm keyword. No annotation action or original machine field changed.


## PR #5552 follow-up, 2026-10-26

GO:0016857 was verified live as catalysis altering chiral centers in a carbohydrate molecule (EC5.1.3.-); polymer-bound mannuronate meets that definition. All three cores now use the valid broad term. Pa PMID:8144447 and Azotobacter PMID:8830682 directly assay recombinant target epimerization and support nonredundant IDA MF proposals; the pre-existing KT2440 ISS proposal remains comparative. All three precise-term proposals use an identical definition and GO parent; this is one ontology request with three supported use cases, not three distinct activities. RHEA:45572 was verified directly and is attached as module reaction evidence. No redundant specific NEW row was added.
