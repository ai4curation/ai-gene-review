# PN dossier: MMGT1

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/MMGT1/MMGT1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q8N4V1
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
- GO:0044743 protein transmembrane import into intracellular organelle | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|Transmembrane protein import
- GO:0072546 EMC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component
