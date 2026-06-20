# PN dossier: SPNS1

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/SPNS1/SPNS1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Efflux of autophagy products
- UniProt: Q9H2V7
- In branches: ALP
- Notes: Lysosome efflux permease that is essential for mTOR reactivation and ALR after prolonged starvation.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Spinster is required for autophagic lysosome reformation and mTOR reactivation following starvation | PNAS
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Efflux of autophagy products
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0007041 lysosomal transport]
        rationale: This PN leaf denotes export of degradation products from the autolysosome during late-stage autophagic lysosome reformation. The closest current GO process term is lysosomal transport, because the key shared semantics are transport across the lysosomal/autolysosomal membrane rather than a specific cargo chemistry.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0007041 lysosomal transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Efflux of autophagy products
