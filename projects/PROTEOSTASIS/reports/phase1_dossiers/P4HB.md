# PN dossier: P4HB

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/P4HB/P4HB-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: P07237
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: P07237
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032964 collagen biosynthetic process]
        rationale: This PN group contains ER factors dedicated to collagen maturation, processing, and folding. Collagen biosynthetic process captures the shared substrate-specific pathway context.
    - [class] ER proteostasis|Maturation and folding of specific substrates
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
