# SRP19 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P09132
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SRP19/SRP19-ai-review.yaml](SRP19-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SRP19/SRP19-ai-review.html
- Gene notes: present - [genes/human/SRP19/SRP19-notes.md](SRP19-notes.md)
- GOA TSV: present - [genes/human/SRP19/SRP19-goa.tsv](SRP19-goa.tsv)
- UniProt record: present - [genes/human/SRP19/SRP19-uniprot.txt](SRP19-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SRP19.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SRP19.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP19.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP19.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SRP19/SRP19-deep-research-falcon.md](SRP19-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SRP19 is the 19 kDa protein subunit of the signal recognition particle (SRP), the cytosolic ribonucleoprotein that mediates co-translational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER). SRP consists of a single 7SL RNA (~300 nucleotides) and six proteins (SRP9, SRP14, SRP19, SRP54, SRP68, SRP72). SRP19 binds directly to the SRP 7SL RNA and is the key assembly factor of the S domain: it is intrinsically disordered when free and folds upon RNA binding, clamping the apical tetraloops of helices 6 and 8 and thereby remodeling the asymmetric internal loop of helix 8 to create the binding site for the signal-sequence-recognition GTPase SRP54. SRP54 can only bind the SRP RNA after SRP19 has bound (ordered, SRP54-late assembly), so SRP19 is required for incorporation of SRP54 and for productive SRP assembly. SRP19 is an RNA-binding/scaffolding protein, not a GTPase. The mature particle functions in the cytoplasm, but SRP partially assembles in the nucleus/nucleolus, and SRP19 is actively imported into the nucleus by importin 8 and transportin.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 6

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP19 as the 19 kDa SRP subunit that binds 7SL RNA (clamping helices 6/8), gating SRP54 incorporation and S-domain assembly. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IEA, ACCEPT; plus the signal-sequence-recognition child GO:0006617). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614, GO:0006617, GO:0008312 7S RNA binding, GO:0005786 SRP membership). Nuclear/nucleolar assembly localizations (GO:0005730/0005654, kept non-core) and the disease/autoantigen context (PMID:35754847) are in the review but outside the PN story. Conclusion: **already captured** (no NEW pressure).
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:27899666 SRP72/19 RNA-remodeling structures; PMID:12086622 SRP19 helix-6/8 clamp; PMID:10618370 ordered SRP54-late assembly; PMID:34208095 SRP review) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds 7S RNA binding and signal-sequence-recognition child). No edits warranted.

## Full Consistency Review

- **UniProt:** P09132 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Signal recognition particle component` ; **PN-node mapping:** group=mapped scope=ok_for_propagation_to_go→GO:0006614 (SRP-dependent cotranslational protein targeting to membrane); class `Protein transport`=mapped→GO:0015031; branch=no_mapping.
- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP19 as the 19 kDa SRP subunit that binds 7SL RNA (clamping helices 6/8), gating SRP54 incorporation and S-domain assembly. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IEA, ACCEPT; plus the signal-sequence-recognition child GO:0006617). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614, GO:0006617, GO:0008312 7S RNA binding, GO:0005786 SRP membership). Nuclear/nucleolar assembly localizations (GO:0005730/0005654, kept non-core) and the disease/autoantigen context (PMID:35754847) are in the review but outside the PN story. Conclusion: **already captured** (no NEW pressure).
- **Mapping strategy:** No change needed. GO:0006614 (goa_status already_in_goa_exact) is present and ACCEPTed — exact projection, not broader than the review. The class-level GO:0015031 is a broad class target, not asserted of SRP19 specifically.
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:27899666 SRP72/19 RNA-remodeling structures; PMID:12086622 SRP19 helix-6/8 clamp; PMID:10618370 ordered SRP54-late assembly; PMID:34208095 SRP review) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds 7S RNA binding and signal-sequence-recognition child). No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SRP19/SRP19-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Signal recognition particle component
- UniProt: P09132
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
