# PN dossier: CSNK1D

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CSNK1D/CSNK1D-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Regulation of autophagophore membrane composition | ER membrane input | COPII vesicle component regulator
- UniProt: P48730
- In branches: ALP
- Notes: RAB1 effector that is directed to autophagosomes by RAB1, then phosphorylates the COPII coat to promote autophagy. Important for autophagosome closure.
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Ypt1/Rab1 regulates Hrr25/CK1δ kinase activity in ER–Golgi traffic and macroautophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - Frontiers | Casein Kinase 1 Family Member CK1δ/Hrr25 Is Required for Autophagosome Completion | Cell and Developmental Biology (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input|COPII vesicle component regulator
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups upstream regulators of COPII contribution to autophagophore membrane input. The two-member set does not support one crisp shared GO term beyond broad vesicle-coating or kinase context.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Specific function in sealing of autophagophore membrane unknown
- UniProt: P48730
- In branches: ALP
- Notes: RAB1 effector that is directed to autophagosomes by RAB1, then phosphorylates the COPII coat to promote autophagy. Important for autophagosome closure.
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Ypt1/Rab1 regulates Hrr25/CK1δ kinase activity in ER–Golgi traffic and macroautophagy | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - Frontiers | Casein Kinase 1 Family Member CK1δ/Hrr25 Is Required for Autophagosome Completion | Cell and Developmental Biology (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|Specific function in sealing of autophagophore membrane unknown
        status=no_mapping scope= GO=[]
        rationale: This PN leaf is explicitly an unknown-function residual bucket and does not support a defensible shared GO mapping.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
