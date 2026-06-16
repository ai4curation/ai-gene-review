# PN dossier: ATG14

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/ATG14/ATG14-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Class 3 PI3K complex 1 component
- UniProt: Q6ZNE5
- In branches: ALP
- Notes: Member of class III PI3K complex 1 that produces PI(3)P at the site of phagophore nucleation. Targets the complex to the ER membrane. Also homooligomerizes and binds to STX17 in the STX17-SNAP29-VAMP8 SNARE complex to regulate autophagosome-lysosome fusion.
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Full article: Autophagy pathway: Cellular and molecular mechanisms (tandfonline.com)
    - ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes | Nature
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Autophagosome-lysosome docking | Lysosome-autophagosome SNARE complex regulator
- UniProt: Q6ZNE5
- In branches: ALP
- Notes: Member of class III PI3K complex 1 that produces PI(3)P at the site of phagophore nucleation. Targets the complex to the ER membrane. Also homooligomerizes and binds to STX17 in the STX17-SNAP29-VAMP8 SNARE complex to regulate autophagosome-lysosome fusion.
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Full article: Autophagy pathway: Cellular and molecular mechanisms (tandfonline.com)
    - ATG14 promotes membrane tethering and fusion of autophagosomes to endolysosomes | Nature
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking|Lysosome-autophagosome SNARE complex regulator
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups regulators placed around the lysosome-autophagosome SNARE complex, but the current member set mixes broad trafficking, ubiquitin, and autophagy-fusion factors rather than one clean shared GO term for SNARE-complex regulation.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking
        status=context_only scope=too_broad_to_propagate GO=[GO:0061909 autophagosome-lysosome fusion]
        rationale: Reviewed as an autophagosome-lysosome docking context. The subtree mixes component buckets and modulators, so generic fusion propagation should come only from narrower reviewed mechanism leaves.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component
