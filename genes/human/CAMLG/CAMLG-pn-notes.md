# CAMLG PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P49069
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CAMLG/CAMLG-ai-review.yaml](CAMLG-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CAMLG/CAMLG-ai-review.html](CAMLG-ai-review.html)
- Gene notes: present - [genes/human/CAMLG/CAMLG-notes.md](CAMLG-notes.md)
- GOA TSV: present - [genes/human/CAMLG/CAMLG-goa.tsv](CAMLG-goa.tsv)
- UniProt record: present - [genes/human/CAMLG/CAMLG-uniprot.txt](CAMLG-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CAMLG.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CAMLG.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CAMLG.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CAMLG.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CAMLG (CAML; calcium-modulating cyclophilin ligand; also GET2) is an integral endoplasmic reticulum membrane protein with a large cytoplasmic N-terminal region and three C-terminal transmembrane helices. Together with WRB (GET1), it constitutes the mammalian ER membrane receptor for the cytosolic ATPase TRC40/GET3, forming the GET (guided entry of tail-anchored proteins) insertase complex. This complex captures newly synthesized tail-anchored membrane proteins from TRC40/GET3 in the cytosol and mediates their post-translational insertion into the ER membrane. CAML is the mammal-specific subunit (not homologous to yeast Get2) and forms a heterotetramer with WRB stabilized by phosphatidylinositol binding; CAML and WRB are mutually dependent for correct membrane integration and stability. CAML was originally identified as a cyclophilin-B-binding protein that elevates intracellular calcium and activates NF-AT signaling in T cells, and it has additional reported roles in B cell survival, EGFR recycling, and stabilization of the E3 ligase RNF122. Biallelic variants cause an autosomal recessive congenital disorder of glycosylation (CDG2Z) characterized by a neurological phenotype and defective membrane trafficking.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 16

## PN Consistency Summary

- **Consistency:** Partial conflict. The GET-pathway row is fully consistent: review, notes and deep research all establish CAMLG/CAML (GET2) as the mammal-specific subunit of the WRB/CAML/TRC40 GET insertase for tail-anchored proteins (PMID:23041287, 27226539, 32910895, 31417168). But PN row 1 classifies CAMLG as a **cyclophilin-type peptidyl-prolyl isomerase** projecting GO:0003755 (PPIase activity). The review, notes and UniProt give NO evidence CAML has PPIase activity — it was named for *binding* cyclophilin B (PMID:7522304), not for being one. PPIase projection to this gene is a misclassification.
- **PN story / NEW pressure:** GET-targeting role (GO:0006620, verified real) is correct and is NOT in current GOA as that exact term — review instead carries the better, more specific GO:0071816 (TA insertion into ER) and GO:0045048. So the GET process is already captured at gene level by a narrower term. GO:0003755 PPIase activity is an over-reach (no enzymatic evidence). Conclusion: GET row already captured (more specifically); PPIase row over-reaches.
- **Evidence alignment:** PN row 1 cites no references; PN row 2 cites none. Review evidence (GET insertase PMIDs) does not overlap any PPIase literature, reinforcing the misclassification.
- **Verdict:** GET-pathway placement sound and already captured by a more specific gene-level term; PPIase classification is a misassignment — CAML binds cyclophilin B but is not a PPIase. **Recommended edits:** [MAP] flag CAMLG as a non-member of the PN "Peptidyl-prolyl isomerases / Cyclophilin type" node, or block GO:0003755 projection onto P49069 (binds cyclophilin, no isomerase activity).

## Full Consistency Review

- **UniProt:** P49069 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE
- **PN placement:** two rows — `ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type` and `ER proteostasis|Protein transport|GET pathway component` ; **PN-node mapping:** GET group → mapped/ok_for_propagation GO:0006620 (post-translational targeting to ER membrane); Protein-transport class → mapped GO:0015031 protein transport; PPIase group/type → mapped GO:0003755 PPIase activity.
- **Consistency:** Partial conflict. The GET-pathway row is fully consistent: review, notes and deep research all establish CAMLG/CAML (GET2) as the mammal-specific subunit of the WRB/CAML/TRC40 GET insertase for tail-anchored proteins (PMID:23041287, 27226539, 32910895, 31417168). But PN row 1 classifies CAMLG as a **cyclophilin-type peptidyl-prolyl isomerase** projecting GO:0003755 (PPIase activity). The review, notes and UniProt give NO evidence CAML has PPIase activity — it was named for *binding* cyclophilin B (PMID:7522304), not for being one. PPIase projection to this gene is a misclassification.
- **PN story / NEW pressure:** GET-targeting role (GO:0006620, verified real) is correct and is NOT in current GOA as that exact term — review instead carries the better, more specific GO:0071816 (TA insertion into ER) and GO:0045048. So the GET process is already captured at gene level by a narrower term. GO:0003755 PPIase activity is an over-reach (no enzymatic evidence). Conclusion: GET row already captured (more specifically); PPIase row over-reaches.
- **Mapping strategy:** GET group mapping (GO:0006620, scope ok) is defensible but broader than the review's GO:0071816; treat as group-level only, do not project onto CAMLG (gene already has the specific term). The PPIase group/type mapping should NOT project onto CAMLG.
- **Evidence alignment:** PN row 1 cites no references; PN row 2 cites none. Review evidence (GET insertase PMIDs) does not overlap any PPIase literature, reinforcing the misclassification.
- **Verdict:** GET-pathway placement sound and already captured by a more specific gene-level term; PPIase classification is a misassignment — CAML binds cyclophilin B but is not a PPIase. **Recommended edits:** [MAP] flag CAMLG as a non-member of the PN "Peptidyl-prolyl isomerases / Cyclophilin type" node, or block GO:0003755 projection onto P49069 (binds cyclophilin, no isomerase activity).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CAMLG/CAMLG-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | Cyclophilin type
- UniProt: P49069
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes ER cyclophilin-family PPIases. The matching GO molecular function is appropriate for propagation.
    - [group] ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the ER peptidyl-prolyl isomerase family. The GO PPIase activity term is the appropriate propagation target for this folding enzyme bucket.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: ER proteostasis | Protein transport | GET pathway component
- UniProt: P49069
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|GET pathway component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane]
        rationale: The PN GET-pathway group covers machinery for post-translational delivery of tail-anchored membrane proteins to the ER. GO does not model the GET pathway directly in the local cache, and the closest supported process term is post-translational targeting to the ER membrane.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (4)
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport|GET pathway component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
