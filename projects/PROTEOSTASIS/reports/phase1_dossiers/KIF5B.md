# PN dossier: KIF5B

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/KIF5B/KIF5B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Localization of the lysosome
- UniProt: P33176
- In branches: ALP
- Notes: A kinesin. Regulates lysosome positioning in the cell, so involved in autophagosome-lysosome fusion. Knockdown leads to autophagosome accumulation near the Golgi and peripheral accumulation of lysosomes. Also drives the formation of tubules from autolysosomes during ALR by binding to PI(4,5)P2 enriched microdomains.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Depletion of Kinesin 5B Affects Lysosomal Distribution and Stability and Induces Peri-Nuclear Accumulation of Autophagosomes in Cancer Cells (plos.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the lysosome
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032418 lysosome localization]
        rationale: This group is explicitly about lysosome positioning in late autophagy. Lysosome localization is the correct propagation target rather than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Lysosomal tubulation
- UniProt: P33176
- In branches: ALP
- Notes: A kinesin. Regulates lysosome positioning in the cell, so involved in autophagosome-lysosome fusion. Knockdown leads to autophagosome accumulation near the Golgi and peripheral accumulation of lysosomes. Also drives the formation of tubules from autolysosomes during ALR by binding to PI(4,5)P2 enriched microdomains.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Depletion of Kinesin 5B Affects Lysosomal Distribution and Stability and Induces Peri-Nuclear Accumulation of Autophagosomes in Cancer Cells (plos.org)
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Lysosomal tubulation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: This PN group specifically captures the tubulation and membrane-remodeling step that regenerates lysosomes from autolysosomes. That aligns better to lysosome organization than to generic autophagy, but the current member set mixes factors annotated in GO to lysosome localization and phagosome/lysosome fusion rather than a clean shared lysosome-organization process role, so propagation would overstate the evidence.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0032418 lysosome localization | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the lysosome
