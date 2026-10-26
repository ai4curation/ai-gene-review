# AZOVI alg8: alginate polymerization/export review

## Identity and scope

P94199, 492 aa; Y08819/CAA70053.1; original ATCC 9046 sequence (PMID9358065). PTHR22913:SF12 official name MANNURONAN SYNTHASE; parent PTHR22913 HYALURONAN SYNTHASE. All records retain species-level NCBITaxon:354; none is silently relabeled as strain DJ.

## Source-specific findings

- [PMID:9358065](https://pubmed.ncbi.nlm.nih.gov/9358065/): Native ATCC 9046 gene sequences and mutant loss of alginate establish both polymerase-system components. Alg8 chemistry/topology was inferred, not measured with purified target enzyme.
- [PMID:32989088](https://pubmed.ncbi.nlm.nih.gov/32989088/): Native c-di-GMP regulation is measured in Azotobacter; Alg44 receptor assignment is explicitly presumed from conservation. The AvGReg/MucG control module differs from the Pseudomonas MucR circuit. The introduction mistakenly calls the Alg8 substrate GDP-mannose; the actual activated substrate is GDP-mannuronate.

## Annotation decisions

- GO:0005886 (IEA): ACCEPT. The curated multipass topology supports the bacterial plasma membrane. This agrees with the native polymerization-system role; it is not based solely on the broad PANTHER transfer.
- GO:0030213 (IEA): MODIFY. GO:0030213 requires the glucuronate/GlcNAc disaccharide polymer. Native Alg8 belongs to the alginate locus and its loss eliminates alginate. The target subfamily is MANNURONAN SYNTHASE within a wider family named HYALURONAN SYNTHASE. The PTN002740694 electronic assignment transfers the wrong polymer specificity; this is a lateral correction, not a claim of ontology ancestry or weak donor count.
- GO:0042121 (IEA): ACCEPT. Native mutation establishes the biosynthetic role, while GT2-family identity and the GDP-mannuronate polymerase assignment identify a catalytic step rather than a mere downstream phenotype.
- GO:0050501 (IEA): MODIFY. The live definition of GO:0050501 requires UDP-glucuronate and UDP-GlcNAc, chemically different from GDP-mannuronate extension by Alg8. GO:0047643 captures the supported inferred substrate/reaction. This is a lateral substrate correction to an overextended family-based assignment; purified native enzyme kinetics are not claimed.
- GO:0085029 (IEA): MARK_AS_OVER_ANNOTATED. Alg8 synthesizes an exopolysaccharide constituent. Evidence for its native alginate-synthetic step does not establish the distinct aggregation, arrangement and bonding of an extracellular matrix described by GO:0085029. The electronic PTN002740694 transfer extends from family members with matrix-assembly annotations; a native matrix-assembly role beyond polymer synthesis remains unestablished. This does not deny the structural importance of alginate outside the cell.

No cached GO-CAM index match for this accession. Original source/evidence/term fields were preserved. No NEW process annotations were proposed. Live QuickGO definitions were checked for reaction specificity; AlgL GO:0045135 is a descendant of both seeded generic lyase terms. Alg8 substrate corrections are lateral, not ontology-ancestry claims. For AlgG, exact polymer epimerase chemistry is represented by a supported proposed term rather than a guessed GO identifier.

## Research provenance

Applied review, annotation-reviewer and core-function-synthesizer guidance. Default Falcon deep research and fetch-gene-pmids ran concurrently. Falcon failed authentication (403); Perplexity-lite fallback failed with insufficient_quota (401). No provider report was fabricated. Fitness retrieval was attempted but no reachable FEBA source or local AZOVI mapping yielded data; no fitness artifact was written. These failures are missing evidence, not negative phenotypes. Logs are /tmp/azovi-poly-alg8-deep.log and /tmp/azovi-poly-alg8-fitness.log. Manual primary research and curated-record assessments supply the review.

## Matrix-assembly scope clarification

An active polysaccharide synthase can participate in matrix assembly where that role is demonstrated. For this Azotobacter target, the retrieved native study tests alginate production and predicts the polymerase role, but does not resolve participation in the aggregation, arrangement or organization of a particular extracellular matrix. The PTN002740694 electronic transfer therefore exceeds the target-specific context established here. This is not a categorical exclusion of polymerases from assembly or a denial that alginate supplies extracellular structure; evidence of a native matrix-architecture phenotype could support retention.

## Verified family selector labels

PANTHER:PTHR22913:SF12 — MANNURONAN SYNTHASE (target UniProt membership; official label checked in panther.obo). Actual membership is present in the target UniProt cross-references; official InterPro labels/types were checked against the live InterPro API. No PTN evolutionary placement is inferred.
