# SRP9 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P49458
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SRP9/SRP9-ai-review.yaml](SRP9-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SRP9/SRP9-ai-review.html
- Gene notes: present - [genes/human/SRP9/SRP9-notes.md](SRP9-notes.md)
- GOA TSV: present - [genes/human/SRP9/SRP9-goa.tsv](SRP9-goa.tsv)
- UniProt record: present - [genes/human/SRP9/SRP9-uniprot.txt](SRP9-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SRP9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SRP9.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SRP9.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SRP9/SRP9-deep-research-falcon.md](SRP9-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SRP9 is the 9 kDa subunit of the signal recognition particle (SRP), the cytosolic ribonucleoprotein that mediates co-translational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER). SRP comprises a single 7SL RNA (~300 nucleotides) and six proteins (SRP9, SRP14, SRP19, SRP54, SRP68, SRP72). SRP9 binds the SRP RNA as an obligate heterodimer with SRP14, and together with the Alu portion of the SRP RNA forms the Alu domain at one end of the particle. This Alu domain is the elongation-arrest module of SRP. When SRP binds a ribosome translating a signal sequence, the SRP9/SRP14 heterodimer reaches into the ribosomal elongation-factor binding site and transiently pauses (arrests) translation elongation, giving SRP time to deliver the ribosome-nascent chain complex to the ER membrane SRP receptor. SRP9 is an RNA-binding protein rather than a GTPase (the GTPases of the pathway are SRP54 and the SRP-receptor subunits). It functions in the cytoplasm/cytosol; SRP9/SRP14 transit the nucleolus during SRP assembly.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP9 as the 9 kDa SRP subunit that, with SRP14, forms the Alu/elongation-arrest domain bound to 7SL RNA. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IBA/IEA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614 ACCEPT; plus the SRP9-specific GO:0045900 negative regulation of translational elongation and GO:0008312 7S RNA binding). Noncanonical Alu-RNA/nuclear roles (PMID:37156570, 37309897, 26585389) are in the review references but outside the PN story and not core. Conclusion: **already captured** (no NEW pressure).
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:34208095 SRP review, elongation arrest; PMID:26585389 Alu-RNP ribosome-stalling structure; file UniProt) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds elongation-arrest GO:0045900 and 7S RNA binding). No edits warranted.

## Full Consistency Review

- **UniProt:** P49458 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Signal recognition particle component` ; **PN-node mapping:** group=mapped scope=ok_for_propagation_to_go→GO:0006614 (SRP-dependent cotranslational protein targeting to membrane); class `Protein transport`=mapped→GO:0015031; branch=no_mapping.
- **Consistency:** Strong and mutually consistent. Deep research, review YAML, and PN annotation all describe SRP9 as the 9 kDa SRP subunit that, with SRP14, forms the Alu/elongation-arrest domain bound to 7SL RNA. The PN "SRP component" label and GO:0006614 mapping match the review's core BP (GO:0006614 IBA/IEA, ACCEPT). No contradictions.
- **PN story / NEW pressure:** PN asserts only the canonical SRP cotranslational-targeting role, already captured (GO:0006614 ACCEPT; plus the SRP9-specific GO:0045900 negative regulation of translational elongation and GO:0008312 7S RNA binding). Noncanonical Alu-RNA/nuclear roles (PMID:37156570, 37309897, 26585389) are in the review references but outside the PN story and not core. Conclusion: **already captured** (no NEW pressure).
- **Mapping strategy:** No change needed. GO:0006614 (goa_status already_in_goa_exact) is present and ACCEPTed — exact projection, not broader than the review. The class-level GO:0015031 is a deliberately broad class target, not asserted of SRP9 specifically. Note the review flags GO:0005785 (SRP receptor complex, TAS PMID:7730321) as over-annotated (SRP vs SRP-receptor confusion) — internal review QC unrelated to the PN node.
- **Evidence alignment:** PN dossier lists no reference titles; alignment via projected-term provenance. Review's core support (PMID:34208095 SRP review, elongation arrest; PMID:26585389 Alu-RNP ribosome-stalling structure; file UniProt) all encode the SRP cotranslational-targeting biology the PN maps to. No divergence.
- **Verdict:** Fully consistent; PN already captured, review more granular (adds elongation-arrest GO:0045900 and 7S RNA binding). No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SRP9/SRP9-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Signal recognition particle component
- UniProt: P49458
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
