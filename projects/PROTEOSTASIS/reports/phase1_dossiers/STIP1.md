# PN dossier: STIP1

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/STIP1/STIP1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR and STI/HOP domain containing
- UniProt: P31948
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and STI/HOP domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family/domain/subtype label. It classifies PN members but is not itself a GO annotation target; any functional assertion should come from a parent role mapping or gene-specific review.
    - [type] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031072 heat shock protein binding]
        rationale: This PN type groups joint HSP70/HSP90 cochaperones. The shared mechanistic assertion is binding heat-shock-protein chaperones, while narrower domain labels remain non-mapping unless they carry an independent activity.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Microautophagy | Endosomal microautophagy
- UniProt: P31948
- In branches: CY, ALP
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Microautophagy|Endosomal microautophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061738 late endosomal microautophagy]
        rationale: This PN group contains HSPA8/co-chaperone machinery for endosomal microautophagy. The matching GO process is late endosomal microautophagy.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Effectors of chaperone-mediated autophagy | Substrate selection
- UniProt: P31948
- In branches: CY, ALP
- Notes: An HSP90 cochaperone. Works with HSPA8 in autophagy substrate selection. Also a component of the complex at the lysosomal membrane that facilitates the unfolding of substrates.
- PN references (titles):
    - The coming of age of chaperone-mediated autophagy | Nature Reviews Molecular Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy|Substrate selection
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy]
        rationale: This leaf denotes substrate-selection machinery for CMA. The GO protein-targeting term preserves the mechanistic role without relying on broad class-level CMA propagation.
    - [group] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: This group covers direct CMA machinery and substrate-selection effectors, unlike the broader CMA class that also includes regulators. Propagation to chaperone-mediated autophagy is appropriate at this narrower level.
    - [class] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: The class label matches the GO CMA process, but the subtree includes both effectors and positive or negative modulators. The relation is retained as context so modulators are not projected as direct CMA participants unless a narrower node supports it.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0061738 late endosomal microautophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Microautophagy|Endosomal microautophagy
- GO:0061684 chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy
- GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy|Substrate selection
