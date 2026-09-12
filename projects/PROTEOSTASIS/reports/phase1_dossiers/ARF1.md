# PN dossier: ARF1

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ARF1/ARF1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | ER-Golgi trafficking | Retrograde transport | COPI coating and uncoating
- UniProt: P84077
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport|COPI coating and uncoating
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030126 COPI vesicle coat]
        rationale: This PN subtype is a COPI coat handling bucket in retrograde ER-Golgi transport. COPI vesicle coat is the appropriate shared cellular-component target.
    - [type] ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum]
        rationale: In `4.3.11`, the earlier retrograde-transport bucket has been folded into ER-Golgi trafficking and now specifically denotes COPI/KDEL-style retrograde trafficking from Golgi back to ER. The correct GO target is therefore retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum rather than ER-to-cytosol retrotranslocation.
    - [group] ER proteostasis|Protein transport|ER-Golgi trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=ER proteostasis|Protein transport
- GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport
- GO:0030126 COPI vesicle coat | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport|COPI coating and uncoating
