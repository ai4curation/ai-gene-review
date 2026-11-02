# AZOVI alg44: alginate polymerization/export review

## Identity and scope

P94200, 389 aa; Y08819/CAA70054.1; original ATCC 9046 sequence (PMID9358065). Alg44 family/PilZ domain; PTHR30386:SF19 has official label MULTIDRUG EXPORT PROTEIN EMRA-RELATED and is not evidence of drug transport. All records retain species-level NCBITaxon:354; none is silently relabeled as strain DJ.

## Source-specific findings

- [PMID:9358065](https://pubmed.ncbi.nlm.nih.gov/9358065/): Native ATCC 9046 gene sequences and mutant loss of alginate establish both polymerase-system components. Alg8 chemistry/topology was inferred, not measured with purified target enzyme.
- [PMID:32989088](https://pubmed.ncbi.nlm.nih.gov/32989088/): Native c-di-GMP regulation is measured in Azotobacter; Alg44 receptor assignment is explicitly presumed from conservation. The AvGReg/MucG control module differs from the Pseudomonas MucR circuit. The introduction mistakenly calls the Alg8 substrate GDP-mannose; the actual activated substrate is GDP-mannuronate.

## Annotation decisions

- GO:0035438 (IEA): ACCEPT. Specific Alg44-family membership and the target PilZ domain support this ligand-binding inference. Native c-di-GMP perturbations independently connect the messenger to alginate production, but PMID32989088 explicitly labels the receptor identity as presumed from conservation. Do not present that study as a purified Azotobacter Alg44 binding assay.
- GO:0042121 (IEA): ACCEPT. The native alg44 mutant loses alginate production. The specific copolymerase family and ligand-binding domain support direct participation in the polymerization machinery rather than an indirect developmental effect.
- GO:0042597 (IEA): ACCEPT. The curated target compartment is inferred by similarity. It describes exposure of a domain in a membrane-spanning copolymerase and does not mean that the entire protein, including the c-di-GMP-binding PilZ domain, is a soluble periplasmic protein. Detailed topology is not a native target experiment.

No cached GO-CAM index match for this accession. Original source/evidence/term fields were preserved. No NEW process annotations were proposed. Live QuickGO definitions were checked for reaction specificity; AlgL GO:0045135 is a descendant of both seeded generic lyase terms. Alg8 substrate corrections are lateral, not ontology-ancestry claims. For AlgG, exact polymer epimerase chemistry is represented by a supported proposed term rather than a guessed GO identifier.

## Research provenance

Applied review, annotation-reviewer and core-function-synthesizer guidance. Default Falcon deep research and fetch-gene-pmids ran concurrently. Falcon failed authentication (403); Perplexity-lite fallback failed with insufficient_quota (401). No provider report was fabricated. Fitness retrieval was attempted but no reachable FEBA source or local AZOVI mapping yielded data; no fitness artifact was written. These failures are missing evidence, not negative phenotypes. Logs are /tmp/azovi-poly-alg44-deep.log and /tmp/azovi-poly-alg44-fitness.log. Manual primary research and curated-record assessments supply the review.

## Verified family selector labels

IPR058834 — ALG44, beta-barrel domain; IPR058835 — ALG44, barrel-sandwich hybrid domain; IPR058833 — ALG44, helical loop domain; IPR009875 — PilZ domain. All are domains. Actual membership is present in the target UniProt cross-references; official InterPro labels/types were checked against the live InterPro API. No PTN evolutionary placement is inferred.

## 2026-10-26 quotation-source QA

Expanded the periplasm quotation to include the verbatim SUBCELLULAR LOCATION prefix, so automated record-section assignment distinguishes the curated location statement from the Periplasm keyword. No annotation action or original machine field changed.


## PR #5552 follow-up, 2026-10-26

Retained the deliberate absence of a separate contributes_to GO:0047643 proposal. Native alg44 loss establishes alginate-production necessity; family/PilZ conservation supports a copolymerase model, but direct native complex activity attribution is absent. The reason now states this boundary rather than leaving an apparent unexplained cross-species asymmetry.
