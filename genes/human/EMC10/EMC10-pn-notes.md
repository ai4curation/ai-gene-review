# EMC10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5UCC4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC10/EMC10-ai-review.yaml](EMC10-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC10/EMC10-ai-review.html
- Gene notes: present - [genes/human/EMC10/EMC10-notes.md](EMC10-notes.md)
- GOA TSV: present - [genes/human/EMC10/EMC10-goa.tsv](EMC10-goa.tsv)
- UniProt record: present - [genes/human/EMC10/EMC10-uniprot.txt](EMC10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC10/EMC10-deep-research-falcon.md](EMC10-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC10 (ER membrane protein complex subunit 10; also C19orf63, INM02) is a 262 aa single-pass type I ER membrane glycoprotein with a cleavable N-terminal signal peptide, a large lumenal domain (N-glycosylated at Asn-182), a single transmembrane helix, and a short cytoplasmic tail. It is a constitutive lumenal/peripheral subunit of the ER membrane protein complex (EMC), a conserved transmembrane-domain insertase and membrane-protein chaperone that mediates energy-independent insertion of newly synthesized membrane proteins into the ER membrane, including post-translational insertion of tail-anchored proteins and cotranslational insertion and topogenesis of multipass membrane proteins such as G protein-coupled receptors. The membrane insertase activity resides in the EMC3/EMC6 membrane core; EMC10 is a non-catalytic structural subunit whose bulk projects into the ER lumen. An alternatively spliced isoform is secreted (HSS1) and circulates; secreted EMC10 has been characterized as a bone marrow-derived angiogenic growth factor that stimulates endothelial cell migration and outgrowth and promotes tissue repair after myocardial infarction. Biallelic loss-of-function variants in EMC10 cause a neurodevelopmental disorder with dysmorphic facies and variable seizures. EMC10 is broadly expressed, with the membrane form localizing to the ER membrane.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 14

## PN Consistency Summary

- **Consistency:** Deep research, review YAML, and PN annotation agree on the EMC role: EMC10 is a single-pass type I lumenal/peripheral, non-catalytic EMC subunit. The review additionally documents the **secreted isoform 2 (HSS1/INM02)** as an extracellular angiogenic growth factor (PMID:28931551, 20680400, 19570817) and biallelic-LoF NEDD (NEDDFAS) disease — a substantial moonlighting biology entirely outside the PN node's scope. Not a contradiction, but the PN row captures only the membrane-EMC facet.
- **PN story / NEW pressure:** PN asserts only EMC membership + import/insertion, already captured (GO:0072546 part_of; insertion/insertase terms KEEP_AS_NON_CORE). No NEW GO term needed for the PN claim. The secreted-form functions are already annotated (GO:0001938, GO:0010595, GO:0045766, GO:0005576) and correctly KEEP_AS_NON_CORE — they are not a PN/ER-proteostasis story.
- **Evidence alignment:** Core EMC papers overlap (22119785, 29242231, 32439656, 30415835); review adds EMC10-specific secreted-isoform and disease PMIDs absent from the PN row.
- **Verdict:** Consistent for the EMC facet; well-reviewed. Shared group→GO:0044743 mapping diverges from insertion semantics; note EMC10's secreted angiogenic moonlighting is correctly non-core and outside PN scope.

## Full Consistency Review

- **UniProt:** Q5UCC4 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component` ; **PN-node mapping:** type → GO:0072546 (EMC complex); group → GO:0044743 (protein transmembrane import into intracellular organelle); class → GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Deep research, review YAML, and PN annotation agree on the EMC role: EMC10 is a single-pass type I lumenal/peripheral, non-catalytic EMC subunit. The review additionally documents the **secreted isoform 2 (HSS1/INM02)** as an extracellular angiogenic growth factor (PMID:28931551, 20680400, 19570817) and biallelic-LoF NEDD (NEDDFAS) disease — a substantial moonlighting biology entirely outside the PN node's scope. Not a contradiction, but the PN row captures only the membrane-EMC facet.
- **PN story / NEW pressure:** PN asserts only EMC membership + import/insertion, already captured (GO:0072546 part_of; insertion/insertase terms KEEP_AS_NON_CORE). No NEW GO term needed for the PN claim. The secreted-form functions are already annotated (GO:0001938, GO:0010595, GO:0045766, GO:0005576) and correctly KEEP_AS_NON_CORE — they are not a PN/ER-proteostasis story.
- **Mapping strategy:** EMC10 does not change the shared node mapping (EMC complex member → GO:0072546 stands). Same group-level concern as EMC7-9: GO:0044743 (lumenal import) mismatches EMC membrane-protein *insertion*; insertion terms are not subclasses of it. The secreted/angiogenic facet argues against treating this node as capturing all of EMC10's biology, but is out of PN scope.
- **Evidence alignment:** Core EMC papers overlap (22119785, 29242231, 32439656, 30415835); review adds EMC10-specific secreted-isoform and disease PMIDs absent from the PN row.
- **Verdict:** Consistent for the EMC facet; well-reviewed. Shared group→GO:0044743 mapping diverges from insertion semantics; note EMC10's secreted angiogenic moonlighting is correctly non-core and outside PN scope.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC10/EMC10-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q5UCC4
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
