# PN dossier: STUB1

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/STUB1/STUB1-ai-review.yaml
- PN workbook rows: 5

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR domain and Ub ligase
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR domain and Ub ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN subtype explicitly denotes TPR-containing ubiquitin ligases in the HSP70/HSP90 co-chaperone branch. The shared catalytic assertion is ubiquitin protein ligase activity.
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Chaperone assisted selective autophagy | CASA complex component
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Notes: HSP90 cochaperone. Participates in chaperone-assisted selective autophagy by forming the CASA complex (HSPA8, BAG3, HSPB8, and STUB1) that delivers ubiquitinated substrates to the to the autophagosome
- PN references (titles):
    - Full article: The chaperone-assisted selective autophagy complex dynamics and dysfunctions (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: The PN CASA subtype covers BAG3-HSPB8-HSP70-system machinery that directs damaged or aggregation-prone substrates into selective autophagic clearance. GO lacks a dedicated CASA term in the current cache, and this subtype includes chaperones and cofactors beyond pure cargo adaptors, so aggrephagy is the closest available process target.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Effectors of chaperone-mediated autophagy | Substrate selection
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Notes: An HSP90 cochaperone. Works with HSPA8 in autophagy substrate selection.
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

## PN row 4: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING variant | UBOX | TPR
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Signature domains: IPR003613
- Auxiliary domains: IPR019734
- PN references (titles):
    - 12646216 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|UBOX|TPR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|UBOX
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 5: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic UBOX complex | STUB1/CHIC2 complex | catalytic / UBOX / TPR
- UniProt: Q9UNE7
- In branches: CY, ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR003613, IPR019734
- PN references (titles):
    - 40796662
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex|catalytic / UBOX / TPR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex|STUB1/CHIC2 complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (7)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR domain and Ub ligase
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
- GO:0061684 chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy
- GO:0061740 protein targeting to lysosome involved in chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Effectors of chaperone-mediated autophagy|Substrate selection
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic UBOX complex
