# GET3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43681
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GET3/GET3-ai-review.yaml](GET3-ai-review.yaml)
- AIGR review HTML: missing - genes/human/GET3/GET3-ai-review.html
- Gene notes: present - [genes/human/GET3/GET3-notes.md](GET3-notes.md)
- GOA TSV: present - [genes/human/GET3/GET3-goa.tsv](GET3-goa.tsv)
- UniProt record: present - [genes/human/GET3/GET3-uniprot.txt](GET3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GET3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GET3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GET3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GET3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/GET3/GET3-deep-research-falcon.md](GET3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: GET3 (ASNA1; also known as TRC40 and arsenite-stimulated ATPase) is the central cytosolic ATPase of the GET/TRC pathway for post-translational targeting of tail-anchored (TA) membrane proteins to the endoplasmic reticulum (ER). It is a homodimeric P-loop NTPase of the ArsA/ArsA-like ATPase family. GET3 selectively recognizes and binds the single C-terminal transmembrane domain (TMD) of newly synthesized TA proteins in the cytosol, receiving them via the BAG6/UBL4A/GET4 pre-targeting and bridging machinery (and from the cochaperone SGTA), and shields the hydrophobic TMD as a soluble carrier/chaperone. ATP binding drives the homodimer into a closed state that captures the substrate; the GET3-TA complex then docks at the ER-membrane receptor-insertase formed by GET1/WRB and CAMLG/GET2, and ATP hydrolysis triggers TA release for insertion into the lipid bilayer, after which GET3 returns to the cytosol for another round. GET3 is thus the targeting factor and TMD chaperone of the pathway, not the membrane insertase itself. It was originally isolated as the human homolog of bacterial ArsA, an arsenite/antimonite-stimulated ATPase, but its physiological role is TA-protein biogenesis. Loss-of-function variants cause an autosomal recessive, rapidly progressive infantile dilated cardiomyopathy. GET3 acts predominantly in the cytoplasm and transiently at the ER membrane.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 15

## PN Consistency Summary

- **Consistency:** Deep research, review YAML, and PN annotation are consistent: GET3/ASNA1/TRC40 is the cytosolic homodimeric ATPase + TMD chaperone (carrier) of the GET/TRC pathway — the targeting factor, NOT the insertase (insertase = WRB/CAML). The review cleanly distinguishes the **ATPase MF (GO:0016887 ATP hydrolysis activity)** and **carrier/chaperone MF (GO:0140597 protein carrier activity)** from the GET1 receptor role, exactly as the task brief requires. Legacy arsenite/nucleolar framing correctly treated as secondary/non-core.
- **PN story / NEW pressure:** PN asserts post-translational ER targeting of TA proteins — already captured: GO:0071816 (involved_in), GO:0016887 + GO:0140597 (core MFs), GO:0043529 (GET complex), GO:0045048 (non-core parent). No NEW GO term warranted. GO:0006620 (post-translational protein targeting to ER membrane) is a defensible, verified-real term that fits GET3's targeting role well — arguably a good *added* BP for GET3, though the GET-pathway role is conventionally captured by GO:0071816 in GOA.
- **Evidence alignment:** High overlap — review's targeting-pathway PMIDs (17382883, 21444755, 23041287, 23610396, 25535373, 31461301, 32910895, 36640319, 37963916) fully evidence the PN targeting claim.
- **Verdict:** Consistent; exemplary review with correct ATPase-vs-chaperone MF split. GO:0006620 is an apt (verified) targeting term for GET3; flag the cross-gene goa_status inconsistency with the GET1 dossier.

## Full Consistency Review

- **UniProt:** O43681 (ASNA1/TRC40) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|GET pathway component` ; **PN-node mapping:** group → GO:0006620 (post-translational protein targeting to ER membrane), scope=ok_for_propagation, **goa_status=new_to_goa**; class → GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Deep research, review YAML, and PN annotation are consistent: GET3/ASNA1/TRC40 is the cytosolic homodimeric ATPase + TMD chaperone (carrier) of the GET/TRC pathway — the targeting factor, NOT the insertase (insertase = WRB/CAML). The review cleanly distinguishes the **ATPase MF (GO:0016887 ATP hydrolysis activity)** and **carrier/chaperone MF (GO:0140597 protein carrier activity)** from the GET1 receptor role, exactly as the task brief requires. Legacy arsenite/nucleolar framing correctly treated as secondary/non-core.
- **PN story / NEW pressure:** PN asserts post-translational ER targeting of TA proteins — already captured: GO:0071816 (involved_in), GO:0016887 + GO:0140597 (core MFs), GO:0043529 (GET complex), GO:0045048 (non-core parent). No NEW GO term warranted. GO:0006620 (post-translational protein targeting to ER membrane) is a defensible, verified-real term that fits GET3's targeting role well — arguably a good *added* BP for GET3, though the GET-pathway role is conventionally captured by GO:0071816 in GOA.
- **Mapping strategy:** GET3 does not change the GET-node mapping. GO:0006620 fits GET3 (the targeting ATPase) more precisely than GET1 (the receptor-insertase). The goa_status `new_to_goa` here vs `more_specific_than_existing_goa` for the identical GET1 mapping is internally inconsistent across the two same-node genes — one needs correction.
- **Evidence alignment:** High overlap — review's targeting-pathway PMIDs (17382883, 21444755, 23041287, 23610396, 25535373, 31461301, 32910895, 36640319, 37963916) fully evidence the PN targeting claim.
- **Verdict:** Consistent; exemplary review with correct ATPase-vs-chaperone MF split. GO:0006620 is an apt (verified) targeting term for GET3; flag the cross-gene goa_status inconsistency with the GET1 dossier.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/GET3/GET3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | GET pathway component
- UniProt: O43681
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
- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport|GET pathway component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
