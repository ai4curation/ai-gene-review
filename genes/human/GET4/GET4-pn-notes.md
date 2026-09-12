# GET4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q7L5D6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GET4/GET4-ai-review.yaml](GET4-ai-review.yaml)
- AIGR review HTML: missing - genes/human/GET4/GET4-ai-review.html
- Gene notes: present - [genes/human/GET4/GET4-notes.md](GET4-notes.md)
- GOA TSV: present - [genes/human/GET4/GET4-goa.tsv](GET4-goa.tsv)
- UniProt record: present - [genes/human/GET4/GET4-uniprot.txt](GET4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GET4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GET4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GET4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GET4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/GET4/GET4-deep-research-falcon.md](GET4-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: GET4 (TRC35; also known as C7orf20 and conserved edge-expressed protein/CEE) is a cytosolic TPR-like all-alpha helical scaffold protein that functions in the pre-targeting/loading stage of the GET/TRC pathway for post-translational insertion of tail-anchored (TA) membrane proteins into the endoplasmic reticulum (ER). It is a constitutive subunit of the heterotrimeric BAG6/BAT3 (Bag6) complex (BAG6 + UBL4A + GET4/TRC35), which captures the transmembrane domains of newly released TA proteins at the ribosome and bridges their handoff from the cochaperone SGTA onto the cytosolic targeting ATPase GET3/TRC40. GET4/TRC35 directly contacts GET3, and the GET3-GET4 interface forms a composite lid over the GET3 substrate-binding chamber that controls TA loading. Beyond TA targeting, the Bag6 complex acts as a holdase in protein quality control, keeping mislocalized and retrotranslocated hydrophobic substrates soluble en route to the proteasome (ERAD and mislocalized-protein degradation); GET4/TRC35 also retains BAG6 in the cytosol by occluding its nuclear localization signal. GET4 acts in the cytoplasm/cytosol. Biallelic GET4 variants destabilize the TRC complex and cause a congenital disorder of glycosylation with impaired TA-protein targeting.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 17

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research (falcon, incorporated into notes), the review YAML, and the PN annotation all describe GET4/TRC35 as the scaffold subunit of the BAG6/BAT3 pre-targeting complex that loads tail-anchored (TA) cargo onto GET3/TRC40 for post-translational ER insertion. The PN "GET pathway component" label and its GO:0006620 mapping match the review's core BP annotation (GO:0006620 IDA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical post-translational ER-targeting role, which the review already captures as core (GO:0006620, GO:0071816 TA-insertion, GO:0140597 carrier activity). The secondary holdase/ERAD/quality-control branch (GO:0031647, GO:0036503, GO:0006511) is in the review but not the PN story. No new GO term needed. Conclusion: **already captured** (no NEW pressure).
- **Evidence alignment:** PN dossier lists no reference titles, so alignment is via projected-term provenance. Review's core support (PMID:20676083 founding Bag6/TRC complex; PMID:25535373 minimal Bag6 module SGTA→TRC40; PMID:34887561 cryo-EM GET4-GET3 lid; PMID:32395830 disease IMP) all encode the same post-translational TA-targeting biology the PN node maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured by the review, which is more granular (adds TA-specific GO:0071816 and the QC branch). No edits warranted.

## Full Consistency Review

- **UniProt:** Q7L5D6 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|GET pathway component` ; **PN-node mapping:** group=mapped scope=ok_for_propagation_to_go→GO:0006620 (post-translational protein targeting to ER membrane); class `Protein transport`=mapped→GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Strong and mutually consistent. Deep research (falcon, incorporated into notes), the review YAML, and the PN annotation all describe GET4/TRC35 as the scaffold subunit of the BAG6/BAT3 pre-targeting complex that loads tail-anchored (TA) cargo onto GET3/TRC40 for post-translational ER insertion. The PN "GET pathway component" label and its GO:0006620 mapping match the review's core BP annotation (GO:0006620 IDA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical post-translational ER-targeting role, which the review already captures as core (GO:0006620, GO:0071816 TA-insertion, GO:0140597 carrier activity). The secondary holdase/ERAD/quality-control branch (GO:0031647, GO:0036503, GO:0006511) is in the review but not the PN story. No new GO term needed. Conclusion: **already captured** (no NEW pressure).
- **Mapping strategy:** No change needed. GO:0006620 (goa_status already_in_goa_exact) is present and ACCEPTed in the review — the projection is exact, not broader (unlike the TOMM20/HSPA8/RAB7A "too broad" precedent). The class-level GO:0015031 is correctly flagged as a broad propagation target for the ER Protein-transport class, not for GET4 specifically.
- **Evidence alignment:** PN dossier lists no reference titles, so alignment is via projected-term provenance. Review's core support (PMID:20676083 founding Bag6/TRC complex; PMID:25535373 minimal Bag6 module SGTA→TRC40; PMID:34887561 cryo-EM GET4-GET3 lid; PMID:32395830 disease IMP) all encode the same post-translational TA-targeting biology the PN node maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured by the review, which is more granular (adds TA-specific GO:0071816 and the QC branch). No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/GET4/GET4-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | GET pathway component
- UniProt: Q7L5D6
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
- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|GET pathway component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
