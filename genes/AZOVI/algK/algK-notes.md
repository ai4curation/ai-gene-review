# AZOVI algK: alginate polymerization/export review

## Identity and scope

P94202, 460 aa; X98863/CAA67370.1; ATCC 9046 (PMID9368366). IPR050767 AlgK-specific repeat assignment. PTHR11102:SF160 officially ERAD-ASSOCIATED E3 UBIQUITIN-PROTEIN LIGASE COMPONENT HRD3; the inherited label is not bacterial ERAD function. All records retain species-level NCBITaxon:354; none is silently relabeled as strain DJ.

## Source-specific findings

- [PMID:9368366](https://pubmed.ncbi.nlm.nih.gov/9368366/): Native ATCC 9046 nonpolar algK disruption establishes alginate-production participation. Structural scaffold and outer-membrane lipid anchoring are comparative/domain inferences, not direct results of this mutant assay.

## Annotation decisions

- GO:0009279 (IEA): ACCEPT. Curated location by similarity and a PROSITE-supported lipoprotein anchor support this compartment. This does not transfer an experimental Pseudomonas localization or claim a transmembrane pore formed by AlgK.
- GO:0042121 (IEA): ACCEPT. A native nonpolar mutant loses alginate production. Its specific AlgK repeat architecture and inferred periplasmic lipid anchoring support a structural contribution to the biosynthetic/export machinery, not a glycosyltransferase reaction. Encystment is a downstream outcome rather than a separate core function.

No cached GO-CAM index match for this accession. Original source/evidence/term fields were preserved. No NEW process annotations were proposed. Live QuickGO definitions were checked for reaction specificity; AlgL GO:0045135 is a descendant of both seeded generic lyase terms. Alg8 substrate corrections are lateral, not ontology-ancestry claims. For AlgG, exact polymer epimerase chemistry is represented by a supported proposed term rather than a guessed GO identifier.

## Research provenance

Applied review, annotation-reviewer and core-function-synthesizer guidance. Default Falcon deep research and fetch-gene-pmids ran concurrently. Falcon failed authentication (403); Perplexity-lite fallback failed with insufficient_quota (401). No provider report was fabricated. Fitness retrieval was attempted but no reachable FEBA source or local AZOVI mapping yielded data; no fitness artifact was written. These failures are missing evidence, not negative phenotypes. Logs are /tmp/azovi-poly-algK-deep.log and /tmp/azovi-poly-algK-fitness.log. Manual primary research and curated-record assessments supply the review.

## Verified family selector labels

IPR050767 — Sel1/AlgK (family), not a uniquely AlgK-only functional selector. The target curated AlgK-family statement and locus/function evidence establish AlgK identity. Actual membership is present in the target UniProt cross-references; official InterPro labels/types were checked against the live InterPro API. No PTN evolutionary placement is inferred.
