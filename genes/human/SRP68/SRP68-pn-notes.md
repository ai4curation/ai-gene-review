# SRP68 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UHB9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SRP68/SRP68-ai-review.yaml](SRP68-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SRP68/SRP68-ai-review.html
- Gene notes: present - [genes/human/SRP68/SRP68-notes.md](SRP68-notes.md)
- GOA TSV: present - [genes/human/SRP68/SRP68-goa.tsv](SRP68-goa.tsv)
- UniProt record: present - [genes/human/SRP68/SRP68-uniprot.txt](SRP68-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SRP68.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SRP68.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP68.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP68.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SRP68/SRP68-deep-research-falcon.md](SRP68-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SRP68 is the 68 kDa subunit of the signal recognition particle (SRP), a cytosolic ribonucleoprotein composed of the 7SL (7S) RNA and six proteins (SRP9, SRP14, SRP19, SRP54, SRP68, SRP72). SRP68 and SRP72 form the heterodimeric "S-domain" module of SRP; SRP68 binds the large/S-domain of the 7SL RNA through an N-terminal RNA-binding domain (residues ~52-252) and, via its C-terminus, recruits SRP72. SRP68 is an RNA-binding scaffold subunit, not a GTPase. Its RNA-binding domain is a tetratricopeptide-like module that bends the SRP RNA at a three-way junction and remodels the conserved 5f loop, a rearrangement required for SRP function in cotranslational targeting and for productive engagement of the SRP receptor. Within SRP, the particle binds the signal sequence of nascent secretory and membrane proteins emerging from the translating ribosome and delivers the ribosome-nascent chain complex to the ER-anchored SRP receptor, where translocation through the Sec61 channel proceeds. SRP68 is predominantly cytosolic; pools are also detected in the nucleolus (reflecting SRP assembly trafficking) and at the endoplasmic reticulum. Biallelic germline SRP68 variants cause severe congenital neutropenia (SCN10).
- Existing/core annotation action counts: ACCEPT: 25; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP68 as the 68 kDa S-domain SRP subunit that binds/remodels 7SL RNA (opening the 5f loop) and heterodimerizes with SRP72. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IBA/IEA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614, GO:0008312 7S RNA binding, GO:0005047 SRP binding, GO:0005786 SRP membership). The disease link (SCN10, PMID:32273475) and nucleolar assembly pool are in the review but outside the PN story. Conclusion: **already captured** (no NEW pressure).
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:24700861 SRP68-RBD RNA remodeling; PMID:27899666 SRP68/72 S-domain structures; PMID:16672232 RNA/SRP72 binding domains; PMID:34208095 SRP review) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds 7S RNA binding, SRP binding, ribosome binding). No edits warranted.

## Full Consistency Review

- **UniProt:** Q9UHB9 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Signal recognition particle component` ; **PN-node mapping:** group=mapped scope=ok_for_propagation_to_go→GO:0006614 (SRP-dependent cotranslational protein targeting to membrane); class `Protein transport`=mapped→GO:0015031; branch=no_mapping.
- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP68 as the 68 kDa S-domain SRP subunit that binds/remodels 7SL RNA (opening the 5f loop) and heterodimerizes with SRP72. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IBA/IEA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614, GO:0008312 7S RNA binding, GO:0005047 SRP binding, GO:0005786 SRP membership). The disease link (SCN10, PMID:32273475) and nucleolar assembly pool are in the review but outside the PN story. Conclusion: **already captured** (no NEW pressure).
- **Mapping strategy:** No change needed. GO:0006614 (goa_status already_in_goa_exact) is present and ACCEPTed — exact projection, not broader than the review. The class-level GO:0015031 is a broad class target, not asserted of SRP68. Note the review independently flags GO:0030942 (ER signal-sequence receptor activity, IEA) as over-annotated — that activity belongs to SRPR/SRPRB, not the SRP S-domain scaffold; internal QC unrelated to the PN node.
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:24700861 SRP68-RBD RNA remodeling; PMID:27899666 SRP68/72 S-domain structures; PMID:16672232 RNA/SRP72 binding domains; PMID:34208095 SRP review) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds 7S RNA binding, SRP binding, ribosome binding). No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SRP68/SRP68-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Signal recognition particle component
- UniProt: Q9UHB9
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
