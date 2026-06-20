# PN dossier: CLCN7

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CLCN7/CLCN7-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Lysosomal catabolism | Regulation of lysosomal environment | Lysosomal acidification | Miscellaneous function - lysosomal acidification
- UniProt: P51798
- In branches: ALP
- Notes: CLCN7 is a antiporter that transports 2 chloride ions into the lysosome in exchange for pumping one proton out. It helps to maintain ion homoeostasis in the lysosome during acidification.
- PN references (titles):
    - The Cl-/H+ antiporter ClC-7 is the primary chloride permeation pathway in lysosomes | Nature
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification|Miscellaneous function - lysosomal acidification
        status=no_mapping scope= GO=[]
        rationale: Reviewed as an unknown or residual PN category. The label does not provide a shared GO-mappable biological process, molecular function, or cellular component.
    - [type] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0007042 lysosomal lumen acidification]
        rationale: This PN group directly names the lysosomal acidification mechanism. Propagation to the GO lysosomal lumen acidification term is an exact mechanistic match.
    - [group] Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Lysosomal catabolism
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad lysosomal-degradation container. The subtree includes carbohydrate, lipid, protein, nuclease, phosphatase, sulfatase, and environment-regulation roles, so mapping should occur at the enzyme or process subtype level.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0007042 lysosomal lumen acidification | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Lysosomal catabolism|Regulation of lysosomal environment|Lysosomal acidification
