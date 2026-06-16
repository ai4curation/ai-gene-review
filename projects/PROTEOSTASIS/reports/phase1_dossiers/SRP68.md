# PN dossier: SRP68

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
