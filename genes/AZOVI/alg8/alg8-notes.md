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


## PR #5552 follow-up, 2026-10-26

Hyaluronan-specific propagation is treated consistently as REMOVE across the three Alg8 reviews; supported alginate roles remain independently represented. Live UniProt PANTHER cross-references show that SF12 itself contains S. pyogenes HasA P0C0H0 (hyaluronan chemistry; PMID:8276791) and NodC P04340/P26024, in addition to the three Alg8 proteins. The SF12 label MANNURONAN SYNTHASE is therefore not a substrate-specific selector. GO:0085029 was checked live: matrix aggregation/arrangement/bonding, with no animal restriction. Retained the evidence gradient: Pa target-specific architecture, KT2440 related-strain inference, Azotobacter over-annotation without a comparable matrix-architecture result. Substituting a biofilm term would change the biological claim rather than simply refine it.


## PR #5552 second follow-up: independent MF gap adjudication, 2026-10-26

Read the full follow-up review on cb083d926: https://github.com/ai4curation/ai-gene-review/pull/5552#issuecomment-6407216104. Added one NEW ISS GO:0047643 proposal after examining the evidence and redundancy, not to suppress a validator warning or copy a sibling's annotation. The five original row payloads and decisions remain unchanged. No NEW biological process is added.

**Positive evidence:** PMID:9358065 identifies the native ATCC 9046 alg8 sequence, conserved alginate-locus context and homology to corresponding P. aeruginosa genes; alg8 mutants lose alginate. This necessity result alone cannot establish catalysis. The P. aeruginosa Alg8 ortholog Q52463 has independent polymerization evidence: PMID:16391057 reports radiolabeled GDP-mannuronate incorporation in envelope fractions and alg8 knockout/complementation, while PMID:18524915 reports mutational requirements of predicted GT active-site residues. These support the catalytic assignment within the assembly. Target curated CC:FUNCTION is explicitly tentative and CC:SIMILARITY supplies GT2 membership; neither generic GT2 nor SF12 membership supplies substrate specificity on its own. Thus the proposal is ISS with Q52463 as the identified sequence source, not IDA for purified Azotobacter Alg8.

**Redundancy test:** original rows are membrane location, alginate biosynthesis, extracellular matrix assembly, and two rejected hyaluronan claims. There is no accepted broad transferase/glycosyltransferase MF, no MF replacement and no other NEW MF. Live QuickGO ancestors of GO:0047643 are GO:0016757, GO:0016758, GO:0003824, GO:0016740 and GO:0003674. The original GO:0050501 is not among them, and GO:0047643 is absent from that term's ancestors: these are chemically different sibling activities, not redundant ancestor/descendant claims. A core summary is synthesis, not an existing curatable annotation row. No P94199 match was found in the cached GO-CAM index.

**Original EC identity and nomenclature:** the unchanged target UniProt record carries only DE EC=2.4.-.-, not a specific hyaluronan EC. The erroneous original GO:0050501 assertion is a TreeGrafter transfer, and its live GO definition cites EC 2.4.1.212 (UDP-glucuronate/UDP-GlcNAc hyaluronan synthesis). The proposed GO:0047643 cites EC 2.4.1.33. The official IUBMB entry calls 2.4.1.33 mannuronan synthase and describes GDP-alpha-D-mannuronate extension of the beta-(1,4)-mannuronan precursor; it lists alginate synthase as an incorrect historical enzyme name. GO retains the label alginate synthase activity, so no machine term label is rewritten. This is not GDP-mannose polymerization or synthesis of an already epimerized mixed M/G chain. Sources checked: https://www.ebi.ac.uk/QuickGO/term/GO:0047643 ; https://www.ebi.ac.uk/QuickGO/term/GO:0050501 ; https://www.enzyme-database.org/query.php?ec=2.4.1.33 .

The prior caution against manufacturing rows solely to clear warnings remains appropriate, but the independent catalytic evidence and absence of overlapping MF coverage warrant this narrowly scoped proposal. The PR remains draft pending #5546; no AlgX or module edits are made here.
