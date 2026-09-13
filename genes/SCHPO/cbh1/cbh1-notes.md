# cbh1 notes

Identity: cbh1, UniProt O14423; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `cbh1-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

LSP: Purified fission-yeast Cbh1 directly binds centromeric K-type repeat DNA and was characterized by DNA-binding and footprinting assays. Its in vivo centromeric-chromatin association was independently examined. These are direct target observations supporting nucleic acid binding without relying on automated keyword transfer. The target already has the more precise experimental centromeric DNA-binding annotation GO:0019237, so the broad prediction is correct but less precise.

[PMID:9237993 "Cbh protein specifically interacts in vitro with the K-type repeat DNA, which is essential for centromere function."]

[PMID:10733588 "In vivo, epitope-tagged Cbhp associated with centromeric K repeat chromatin, as well as with noncentromeric regions."]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. 

CENP-B family retrotransposon surveillance is supported by [PMID:18094683 "CENP-B homologues of S. pombe localize at and recruit histone deacetylases to silence Tf2 retrotransposons."]. The publisher preview identifies Figure 1 as genome-wide maps of Abp1 and Cbh1, confirming that Cbh1 is among the assayed family members. The broader description records this family role, without transferring every Abp1-specific recruitment mechanism to Cbh1. Later papers PMID:22907751 and PMID:26354768 were checked as additional leads; their cached abstracts emphasize Abp1, so detailed Cbh1-specific numerical effects in the generated report are not treated as independently verified.

QuickGO GO:0007059 was checked for the chromosome segregation process proposed in place of the biological-process ND root; the direct double-mutant evidence is [PMID:10733588 "The synergism between the two null mutations suggests that these proteins perform redundant functions in S. pombe chromosome segregation."].
