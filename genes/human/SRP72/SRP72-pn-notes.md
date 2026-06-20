# SRP72 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O76094
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SRP72/SRP72-ai-review.yaml](SRP72-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SRP72/SRP72-ai-review.html
- Gene notes: present - [genes/human/SRP72/SRP72-notes.md](SRP72-notes.md)
- GOA TSV: present - [genes/human/SRP72/SRP72-goa.tsv](SRP72-goa.tsv)
- UniProt record: present - [genes/human/SRP72/SRP72-uniprot.txt](SRP72-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SRP72.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SRP72.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP72.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP72.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SRP72/SRP72-deep-research-falcon.md](SRP72-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SRP72 is the largest protein subunit of the mammalian signal recognition particle (SRP), a cytosolic ribonucleoprotein composed of a 300-nucleotide 7SL RNA and six proteins (SRP9, SRP14, SRP19, SRP54, SRP68 and SRP72). SRP72 forms a stable heterodimer with SRP68 and, together, they bind a regulatory region of the 7SL RNA to constitute part of the SRP S-domain. SRP72 is an RNA-binding scaffolding subunit rather than a GTPase: its N-terminal tetratricopeptide-repeat (TPR) region binds an extended linear motif of SRP68, while its C-terminal RNA-binding region threads along the 5e/5f loops of the 7SL RNA, remodeling the RNA into a state competent for SRP54 binding and modulating ribosome contacts. Through these interactions SRP72 contributes to assembly and architecture of SRP and to its core biological role, the co-translational targeting of secretory and membrane proteins to the endoplasmic reticulum: SRP recognizes the signal sequence of nascent chains emerging from the ribosome and delivers the ribosome-nascent chain complex to the membrane-anchored SRP receptor, where translocation into the ER ensues. SRP72 is broadly expressed, acts in the cytosol and at the ER membrane, and heterozygous mutations in the gene cause autosomal-dominant bone marrow failure (aplastic anemia/myelodysplasia, BMFS1).
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 7

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP72 as the largest SRP subunit, an RNA-binding scaffold that heterodimerizes with SRP68 (N-terminal TPR), threads along the 7SL 5e/5f loops, and contributes to ribosome contacts. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IBA/IEA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614, GO:0008312 7S RNA binding, GO:0005047 SRP binding, GO:0043022 ribosome binding, GO:0005786 SRP membership). The BMFS1 disease link (PMID:22541560) and nucleolar/Cajal-body assembly pool (PMID:38858088) are in the review but outside the PN story. Conclusion: **already captured** (no NEW pressure).
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:27899666 definitive SRP72 structures; PMID:28369529 apo/SRP68-72 structures; PMID:17254600 RNA-remodeling assembly; PMID:16672232 SRP68-binding TPR; PMID:34208095 SRP review) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds 7S RNA binding, SRP binding, ribosome binding, TPR domain binding). No edits warranted.

## Full Consistency Review

- **UniProt:** O76094 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Signal recognition particle component` ; **PN-node mapping:** group=mapped scope=ok_for_propagation_to_go→GO:0006614 (SRP-dependent cotranslational protein targeting to membrane); class `Protein transport`=mapped→GO:0015031; branch=no_mapping.
- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP72 as the largest SRP subunit, an RNA-binding scaffold that heterodimerizes with SRP68 (N-terminal TPR), threads along the 7SL 5e/5f loops, and contributes to ribosome contacts. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IBA/IEA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614, GO:0008312 7S RNA binding, GO:0005047 SRP binding, GO:0043022 ribosome binding, GO:0005786 SRP membership). The BMFS1 disease link (PMID:22541560) and nucleolar/Cajal-body assembly pool (PMID:38858088) are in the review but outside the PN story. Conclusion: **already captured** (no NEW pressure).
- **Mapping strategy:** No change needed. GO:0006614 (goa_status already_in_goa_exact) is present and ACCEPTed — exact projection, not broader than the review. The class-level GO:0015031 is a broad class target, not asserted of SRP72.
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:27899666 definitive SRP72 structures; PMID:28369529 apo/SRP68-72 structures; PMID:17254600 RNA-remodeling assembly; PMID:16672232 SRP68-binding TPR; PMID:34208095 SRP review) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds 7S RNA binding, SRP binding, ribosome binding, TPR domain binding). No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SRP72/SRP72-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Signal recognition particle component
- UniProt: O76094
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|Signal recognition particle component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006614 SRP-dependent cotranslational protein targeting to membrane]
        rationale: This PN group captures core signal-recognition-particle machinery used to direct translating ribosome-nascent chain complexes to the ER membrane. The group is machinery-centric rather than process-equivalent, so it propagates to the GO targeting process.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006614 SRP-dependent cotranslational protein targeting to membrane | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|Signal recognition particle component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
