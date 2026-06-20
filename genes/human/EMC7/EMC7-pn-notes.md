# EMC7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NPA0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC7/EMC7-ai-review.yaml](EMC7-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC7/EMC7-ai-review.html
- Gene notes: present - [genes/human/EMC7/EMC7-notes.md](EMC7-notes.md)
- GOA TSV: present - [genes/human/EMC7/EMC7-goa.tsv](EMC7-goa.tsv)
- UniProt record: present - [genes/human/EMC7/EMC7-uniprot.txt](EMC7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC7/EMC7-deep-research-falcon.md](EMC7-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC7 (ER membrane protein complex subunit 7) is a 242 aa single-pass type I ER membrane protein and a constitutive subunit of the ER membrane protein complex (EMC), a conserved transmembrane-domain insertase and membrane-protein chaperone of the endoplasmic reticulum. After cleavage of its N-terminal signal peptide, EMC7 presents a large lumenal beta-sandwich domain followed by a single transmembrane helix and a short, partly disordered cytoplasmic tail. EMC7 is a peripheral, non-catalytic architectural subunit; the catalytic insertase machinery (the membrane-embedded hydrophilic vestibule) is formed by EMC3 and EMC6. As part of the EMC, EMC7 contributes to the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or contain destabilizing residues, including post-translational insertion of tail-anchored proteins and cotranslational insertion and topogenesis of multipass membrane proteins. EMC7 localizes to the ER membrane and is broadly expressed.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Deep research (notes + falcon), review YAML, PN annotation, and the type-level mapping are mutually consistent. EMC7 is a single-pass type I, non-catalytic architectural EMC subunit (lumenal beta-sandwich; catalytic vestibule = EMC3/EMC6). No contradictions. The review additionally documents EMC7-specific roles (Rab7/syntaxin-18 ER–endosome tethering, PMID:32111841; VDAC1 interface, PMID:38517390; SQS-client selectivity filter, PMID:37199759) absent from the dossier, but these elaborate rather than conflict.
- **PN story / NEW pressure:** PN asserts only EMC membership + ER membrane-protein import/insertion, all already captured (GO:0072546 part_of; GO:0045050, GO:0071816, GO:0032977 contributes_to). No NEW GO term needed. The carbohydrate-binding IEA (GO:0030246) is correctly MARK_AS_OVER_ANNOTATED. EMC7's tethering/VDAC moonlighting is not pushed as a PN role.
- **Evidence alignment:** Strong overlap — both cite the EMC insertase/structure literature; the review's PMIDs (22119785, 29242231, 32439656, 30415835, etc.) fully cover the PN process claim.
- **Verdict:** Consistent; well-reviewed. Sole concern is the group-level GO:0044743 import mapping (shared across EMC7-10), which mismatches EMC "insertion" semantics.

## Full Consistency Review

- **UniProt:** Q9NPA0 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component` ; **PN-node mapping:** type=mapped/ok_for_propagation → GO:0072546 (EMC complex); group → GO:0044743 (protein transmembrane import into intracellular organelle); class → GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Deep research (notes + falcon), review YAML, PN annotation, and the type-level mapping are mutually consistent. EMC7 is a single-pass type I, non-catalytic architectural EMC subunit (lumenal beta-sandwich; catalytic vestibule = EMC3/EMC6). No contradictions. The review additionally documents EMC7-specific roles (Rab7/syntaxin-18 ER–endosome tethering, PMID:32111841; VDAC1 interface, PMID:38517390; SQS-client selectivity filter, PMID:37199759) absent from the dossier, but these elaborate rather than conflict.
- **PN story / NEW pressure:** PN asserts only EMC membership + ER membrane-protein import/insertion, all already captured (GO:0072546 part_of; GO:0045050, GO:0071816, GO:0032977 contributes_to). No NEW GO term needed. The carbohydrate-binding IEA (GO:0030246) is correctly MARK_AS_OVER_ANNOTATED. EMC7's tethering/VDAC moonlighting is not pushed as a PN role.
- **Mapping strategy:** EMC7 does not change the shared EMC-node mapping. Type→GO:0072546 is exact and correct. The **group→GO:0044743 is semantically off**: GO:0044743 (def. "directed movement of proteins into an intracellular organelle, across a membrane") is lumenal import (TOM/TIM-type), whereas the EMC performs membrane-protein *insertion*; GO:0071816/GO:0045050 (via GO:0090150 establishment of protein localization to membrane) are NOT subclasses of GO:0044743. GO:0044743 over-reaches/diverges.
- **Evidence alignment:** Strong overlap — both cite the EMC insertase/structure literature; the review's PMIDs (22119785, 29242231, 32439656, 30415835, etc.) fully cover the PN process claim.
- **Verdict:** Consistent; well-reviewed. Sole concern is the group-level GO:0044743 import mapping (shared across EMC7-10), which mismatches EMC "insertion" semantics.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC7/EMC7-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q9NPA0
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072546 EMC complex]
        rationale: This PN type denotes ER membrane protein complex components. The GO EMC complex cellular-component term is the direct target.
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
- GO:0072546 EMC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
