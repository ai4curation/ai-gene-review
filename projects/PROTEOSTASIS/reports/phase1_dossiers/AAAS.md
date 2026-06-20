# PN dossier: AAAS

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AAAS/AAAS-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Nuclear proteostasis | Protein transport | Nuclear pore complex
- UniProt: Q9NRG9
- In branches: NU
- PN-node mapping records (path + ancestors):
    - [group] Nuclear proteostasis|Protein transport|Nuclear pore complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005643 nuclear pore]
        rationale: This PN group denotes core components of the nuclear pore complex. The closest current GO target in the local ontology cache is the cellular-component term nuclear pore.
    - [class] Nuclear proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN nuclear Protein transport class covers the machinery and routes that move proteins across the nuclear envelope. GO protein transport is the correct propagation target, although the PN class is specialized to the nuclear compartment.
    - [branch] Nuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Nuclear proteostasis|Protein transport
- GO:0005643 nuclear pore | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Nuclear proteostasis|Protein transport|Nuclear pore complex
