# GET1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O00258
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GET1/GET1-ai-review.yaml](GET1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/GET1/GET1-ai-review.html
- Gene notes: present - [genes/human/GET1/GET1-notes.md](GET1-notes.md)
- GOA TSV: present - [genes/human/GET1/GET1-goa.tsv](GET1-goa.tsv)
- UniProt record: present - [genes/human/GET1/GET1-uniprot.txt](GET1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GET1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GET1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GET1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GET1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/GET1/GET1-deep-research-falcon.md](GET1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: GET1 (WRB; also known as congenital heart disease 5 protein/CHD5 and tryptophan-rich basic protein) is a multi-pass endoplasmic reticulum (ER) membrane protein that is the membrane receptor for the cytosolic ATPase GET3/TRC40 in the GET (guided entry of tail-anchored proteins) pathway. This pathway delivers tail-anchored (TA) membrane proteins, which carry a single C-terminal transmembrane domain, to the ER for post-translational insertion. GET1/WRB has three transmembrane helices and a cytosolic coiled-coil domain (residues ~39-97) that docks the TA-loaded GET3/TRC40 homodimer at the membrane. Together with CAMLG/GET2, GET1 forms a heterotetrameric insertase that, with bound GET3, accepts the TA substrate and catalyzes its insertion into the ER lipid bilayer through a hydrophilic groove, mechanistically related to the YidC/Oxa1 insertase superfamily and the ER membrane protein complex (EMC). GET1 and CAMLG are mutually dependent for stable expression and correct topology, and GET1 is required for the proper integration of its partner CAMLG into the ER membrane. The protein is broadly expressed and resides in the ER membrane.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Deep research (notes + falcon), review YAML, and PN annotation are consistent: GET1/WRB is the ER membrane receptor-insertase subunit of the GET pathway, with CAMLG/GET2 forming the heterotetramer that accepts GET3-delivered TA proteins. Distinction "receptor/insertase (GET1) vs ATPase targeting factor (GET3)" is honored. The review correctly MARK_AS_OVER_ANNOTATED the legacy nucleus TAS (PMID:9544840), not reproduced.
- **PN story / NEW pressure:** PN asserts post-translational ER-membrane targeting/insertion of TA proteins — already captured by review's core terms GO:0071816 (TA insertion into ER membrane), GO:0045048 (protein insertion into ER membrane), GO:0043495 (protein-membrane adaptor activity, the PAN-GO MF), GO:0043529 (GET complex). No NEW GO term warranted; already captured.
- **Evidence alignment:** Strong overlap — review's GET-pathway PMIDs (21444755, 23041287, 27226539, 32910895, 36640319, 37963916) fully support the PN targeting/insertion claim.
- **Verdict:** Consistent; well-reviewed. Flag the GO:0006620 goa_status inconsistency between GET1 (`more_specific_than_existing_goa`) and GET3 (`new_to_goa`) dossiers and that GO:0006620 (targeting) fits GET3 better than the receptor-insertase GET1.

## Full Consistency Review

- **UniProt:** O00258 (WRB) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|GET pathway component` ; **PN-node mapping:** group → GO:0006620 (post-translational protein targeting to ER membrane), scope=ok_for_propagation, **goa_status=more_specific_than_existing_goa**; class → GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Deep research (notes + falcon), review YAML, and PN annotation are consistent: GET1/WRB is the ER membrane receptor-insertase subunit of the GET pathway, with CAMLG/GET2 forming the heterotetramer that accepts GET3-delivered TA proteins. Distinction "receptor/insertase (GET1) vs ATPase targeting factor (GET3)" is honored. The review correctly MARK_AS_OVER_ANNOTATED the legacy nucleus TAS (PMID:9544840), not reproduced.
- **PN story / NEW pressure:** PN asserts post-translational ER-membrane targeting/insertion of TA proteins — already captured by review's core terms GO:0071816 (TA insertion into ER membrane), GO:0045048 (protein insertion into ER membrane), GO:0043495 (protein-membrane adaptor activity, the PAN-GO MF), GO:0043529 (GET complex). No NEW GO term warranted; already captured.
- **Mapping strategy:** GET1 does not alter the GET-node mapping. **Discrepancy flag:** GET1 dossier labels GO:0006620 `more_specific_than_existing_goa` whereas the identical GET3 mapping labels it `new_to_goa` — one is wrong (GET1's GOA carries the insertion terms but not GO:0006620 specifically; both genes should share the same goa_status for the same projected term). GO:0006620 is verified-real and a defensible group term, but is a *targeting* (not insertion) term; GET1's role is the membrane receptor-insertase, so GO:0006620 is slightly off-target for GET1 specifically (better fits GET3). Acceptable as a group/pathway-level term, but narrower-fit for GET3 than GET1.
- **Evidence alignment:** Strong overlap — review's GET-pathway PMIDs (21444755, 23041287, 27226539, 32910895, 36640319, 37963916) fully support the PN targeting/insertion claim.
- **Verdict:** Consistent; well-reviewed. Flag the GO:0006620 goa_status inconsistency between GET1 (`more_specific_than_existing_goa`) and GET3 (`new_to_goa`) dossiers and that GO:0006620 (targeting) fits GET3 better than the receptor-insertase GET1.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/GET1/GET1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | GET pathway component
- UniProt: O00258
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

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|GET pathway component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
