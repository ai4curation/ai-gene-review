# PN dossier: CAMLG

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CAMLG/CAMLG-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | Cyclophilin type
- UniProt: P49069
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes ER cyclophilin-family PPIases. The matching GO molecular function is appropriate for propagation.
    - [group] ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the ER peptidyl-prolyl isomerase family. The GO PPIase activity term is the appropriate propagation target for this folding enzyme bucket.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: ER proteostasis | Protein transport | GET pathway component
- UniProt: P49069
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|GET pathway component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane]
        rationale: The PN GET-pathway group covers machinery for post-translational delivery of tail-anchored membrane proteins to the ER. GO does not model the GET pathway directly in the local cache, and the closest supported process term is post-translational targeting to the ER membrane.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (4)
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport|GET pathway component
