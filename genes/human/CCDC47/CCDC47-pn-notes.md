# CCDC47 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96A33
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CCDC47/CCDC47-ai-review.yaml](CCDC47-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CCDC47/CCDC47-ai-review.html](CCDC47-ai-review.html)
- Gene notes: present - [genes/human/CCDC47/CCDC47-notes.md](CCDC47-notes.md)
- GOA TSV: present - [genes/human/CCDC47/CCDC47-goa.tsv](CCDC47-goa.tsv)
- UniProt record: present - [genes/human/CCDC47/CCDC47-uniprot.txt](CCDC47-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CCDC47.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CCDC47.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CCDC47.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CCDC47.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CCDC47 (also called calumin) is a widely conserved, single-pass type I endoplasmic reticulum membrane protein with a small cytosolic domain, a single transmembrane helix, and a large luminal domain ending in a disordered, basic, coiled-coil region. It is the scaffold subunit of the PAT (protein associated with the ER translocon) complex, an obligate heterodimer with WDR83OS/Asterix. The PAT complex is one of three accessory subcomplexes (GEL, BOS, PAT) of the ribosome-associated multi-pass translocon (MPT) that assembles around the Sec61 channel during synthesis of multi-pass membrane proteins. Within this assembly CCDC47 occludes the lateral gate of Sec61 and stabilizes Asterix, which directly engages and shields hydrophilic transmembrane segments of nascent multi-pass clients until they fold, thereby promoting the biogenesis of GPCRs, channels, transporters and other polytopic membrane proteins. CCDC47 binds Ca2+ with low affinity and high capacity and contributes to ER calcium storage and signaling, and it has been linked to ER-associated degradation (ERAD) and to maintenance of ER organization during embryogenesis. Biallelic loss-of-function variants cause an autosomal recessive trichohepatoneurodevelopmental syndrome (woolly hair, liver dysfunction, dysmorphic features, hypotonia, developmental delay).
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 9; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Highly consistent. Review, notes, and PN all identify CCDC47 as the scaffold subunit of the PAT intramembrane-chaperone complex (obligate heterodimer with WDR83OS/Asterix) within the ribosome-associated multi-pass translocon (MPT). No contradictions.
- **PN story / NEW pressure:** GO:0160005 "PAT complex" is VERIFIED real (OLS def names CCDC47+Asterix heterodimer) and is NOT in CCDC47's GOA or review — the review used the broader parent GO:0160064 multi-pass translocon complex (IDA, PMID:36261522) and GO:0101031 protein folding chaperone complex. GO:0160005 is strictly more specific and exactly correct. Conclude: defensible ADD (the precise complex term). GO:0044743 / GO:0015031 are broader generalizations (transmembrane import / protein transport) that the review covers more specifically via GO:0160063 multi-pass TM insertion + GO:0045048 — already captured / broader.
- **Evidence alignment:** PN node carries no reference titles; review/GOA anchored on the defining primary literature (PMID:32814900 PAT discovery, PMID:36261522 MPT assembly, PMID:32820719 ribosome-Sec61 translocon). The PAT-complex term itself originates from this same literature, so PN and review are evidence-aligned even without shared citation strings.
- **Verdict:** Consistent; PN adds the precise complex term. **Recommended edits:** [YAML] ADD GO:0160005 PAT complex (part_of, IPI/IDA, PMID:32814900/PMID:36261522) to CCDC47 existing_annotations and core_functions.in_complex — it is the exact, more-specific complex vs the review's GO:0160064. [MAP] keep GO:0044743/GO:0015031 as context-only (broader than review's GO:0160063/GO:0045048).

## Full Consistency Review

- **UniProt:** Q96A33 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (excellent; review independently lands on PAT/MPT biology, notes present)
- **PN placement:** `ER proteostasis|Protein transport|Transmembrane protein import|PAT complex component` ; **PN-node mapping:** type (PAT complex component)→GO:0160005 PAT complex (mapped/ok); group (Transmembrane protein import)→GO:0044743 protein transmembrane import into intracellular organelle (mapped/ok); class (Protein transport)→GO:0015031 protein transport (mapped/ok).
- **Consistency:** Highly consistent. Review, notes, and PN all identify CCDC47 as the scaffold subunit of the PAT intramembrane-chaperone complex (obligate heterodimer with WDR83OS/Asterix) within the ribosome-associated multi-pass translocon (MPT). No contradictions.
- **PN story / NEW pressure:** GO:0160005 "PAT complex" is VERIFIED real (OLS def names CCDC47+Asterix heterodimer) and is NOT in CCDC47's GOA or review — the review used the broader parent GO:0160064 multi-pass translocon complex (IDA, PMID:36261522) and GO:0101031 protein folding chaperone complex. GO:0160005 is strictly more specific and exactly correct. Conclude: defensible ADD (the precise complex term). GO:0044743 / GO:0015031 are broader generalizations (transmembrane import / protein transport) that the review covers more specifically via GO:0160063 multi-pass TM insertion + GO:0045048 — already captured / broader.
- **Mapping strategy:** Node mapping is sound and laddered correctly (specific complex at type, broad process at class). The class/group terms are broader than the review (precedent: TOMM20/HSPA8/RAB7A broader-than-review rejections) — treat GO:0044743/GO:0015031 as context-only, not as gene-level GO assertions superseding the review's specific terms. The type-level GO:0160005 is the value-add.
- **Evidence alignment:** PN node carries no reference titles; review/GOA anchored on the defining primary literature (PMID:32814900 PAT discovery, PMID:36261522 MPT assembly, PMID:32820719 ribosome-Sec61 translocon). The PAT-complex term itself originates from this same literature, so PN and review are evidence-aligned even without shared citation strings.
- **Verdict:** Consistent; PN adds the precise complex term. **Recommended edits:** [YAML] ADD GO:0160005 PAT complex (part_of, IPI/IDA, PMID:32814900/PMID:36261522) to CCDC47 existing_annotations and core_functions.in_complex — it is the exact, more-specific complex vs the review's GO:0160064. [MAP] keep GO:0044743/GO:0015031 as context-only (broader than review's GO:0160063/GO:0045048).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CCDC47/CCDC47-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | PAT complex component
- UniProt: Q96A33
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Protein transport|Transmembrane protein import|PAT complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160005 PAT complex]
        rationale: This PN type denotes PAT-complex components in ER membrane protein insertion. The GO PAT complex term is the direct target.
    - [group] ER proteostasis|Protein transport|Transmembrane protein import
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044743 protein transmembrane import into intracellular organelle]
        rationale: This PN group covers ER transmembrane-protein insertion/import systems such as EMC- and PAT-related pathways. The local GO cache does not expose an ER-specific matching term, so the broader intracellular-organelle transmembrane-import process is the best supported propagation target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0044743 protein transmembrane import into intracellular organelle | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport|Transmembrane protein import
- GO:0160005 PAT complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|Transmembrane protein import|PAT complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
