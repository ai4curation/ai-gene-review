# PN dossier: ERO1B

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/ERO1B/ERO1B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases | Protein disulfide isomerase reoxidation
- UniProt: Q86YB8
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Folding enzyme|Protein disulfide isomerases|Protein disulfide isomerase reoxidation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016971 flavin-dependent sulfhydryl oxidase activity]
        rationale: Corrected after gene-level review (proteostasis batch 5). This PN type is the ERO1 "PDI reoxidation" step, whose members (ERO1A/ERO1L, ERO1B/ERO1LB) are FAD-dependent sulfhydryl OXIDASES that reoxidize PDI to regenerate its active site — they do not themselves catalyze protein disulfide isomerization. The previous target GO:0003756 (protein disulfide isomerase activity) was incorrect for this node and would mislabel the oxidases as isomerases (both ERO1A and ERO1B reviews mark the protein-disulfide reductase/isomerase terms as over-annotations). The correct shared molecular function is GO:0016971 flavin-dependent sulfhydryl oxidase activity, which both genes carry with experimental (EXP) evidence in GOA.
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases|Protein disulfide isomerase reoxidation
