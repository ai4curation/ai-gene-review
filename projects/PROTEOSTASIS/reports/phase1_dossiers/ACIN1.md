# PN dossier: ACIN1

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/ACIN1/ACIN1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Specific function in autophagosome maturation and lysosome fusion unknown
- UniProt: Q9UKV3
- In branches: ALP
- Notes: Drosophila ACN promotes autophagosome maturation in basal autophagy.
- PN references (titles):
    - Drosophila acinus encodes a novel regulator of endocytic and autophagic trafficking | Development | The Company of Biologists
    - Stress-induced Cdk5 activity enhances cytoprotective basal autophagy in Drosophila melanogaster by phosphorylating acinus at serine437 | eLife (elifesciences.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Specific function in autophagosome maturation and lysosome fusion unknown
        status=no_mapping scope= GO=[]
        rationale: Reviewed as an unknown or residual PN category. The label does not provide a shared GO-mappable biological process, molecular function, or cellular component.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.
