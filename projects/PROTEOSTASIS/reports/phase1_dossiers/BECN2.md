# PN dossier: BECN2

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/BECN2/BECN2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Class 3 PI3K complex 1 component
- UniProt: A8MW95
- In branches: ALP
- Notes: Paralog of BECN1 that can also be part of the class III PI3K complex 1. Also required for lysosomal degradation of GPCRs.
- PN references (titles):
    - Beclin 2 Functions in Autophagy, Degradation of G Protein-Coupled Receptors, and Metabolism - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I]
        rationale: This PN type is a curated component class for the direct autophagy- promoting class III PI3K complex 1. Propagation to the matching GO cellular-component term is appropriate, although the source is a component-role category rather than the complex term itself.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component
