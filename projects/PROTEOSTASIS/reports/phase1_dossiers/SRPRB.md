# PN dossier: SRPRB

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SRPRB/SRPRB-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | SRP receptor subunit
- UniProt: Q9Y5M8
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|SRP receptor subunit
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006614 SRP-dependent cotranslational protein targeting to membrane]
        rationale: SRP receptor subunits participate in docking the SRP-ribosome complex to the ER membrane during cotranslational targeting. Mapping to the GO SRP-dependent targeting process is appropriate at propagation scope.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006614 SRP-dependent cotranslational protein targeting to membrane | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=ER proteostasis|Protein transport|SRP receptor subunit
