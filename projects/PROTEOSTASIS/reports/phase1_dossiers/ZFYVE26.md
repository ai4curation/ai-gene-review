# PN dossier: ZFYVE26

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/ZFYVE26/ZFYVE26-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Modulator of class 3 PI3K complex 2 activity
- UniProt: Q68DK2
- In branches: ALP
- Notes: aka FYVE-CENT, SPG15, and spastizin. Spastizin interacts with the autophagy related Beclin 1-UVRAG-Rubicon multiprotein complex and is required for autophagosome maturation. In cells lacking spastizin or with mutated forms of the protein, spastizin interaction with Beclin 1 is lost although the formation of the Beclin 1-UVRAG-Rubicon complex can still be observed. However, in these cells there is an impairment of autophagosome maturation and an accumulation of immature autophagosomes. Also important in autophagic lysosomal reformation.
- PN references (titles):
    - Defective autophagy in spastizin mutated patients with hereditary spastic paraparesis type 15 | Brain | Oxford Academic (oup.com)
    - JCI - Spastic paraplegia proteins spastizin and spatacsin mediate autophagic lysosome reformation
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Modulator of class 3 PI3K complex 2 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagic lysosome reformation | Specific function in autophagic lysosome reformation unknown
- UniProt: Q68DK2
- In branches: ALP
- Notes: aka FYVE-CENT, SPG15, and spastizin. Spastizin interacts with the autophagy related Beclin 1-UVRAG-Rubicon multiprotein complex and is required for autophagosome maturation. In cells lacking spastizin or with mutated forms of the protein, spastizin interaction with Beclin 1 is lost although the formation of the Beclin 1-UVRAG-Rubicon complex can still be observed. However, in these cells there is an impairment of autophagosome maturation and an accumulation of immature autophagosomes. Also important in autophagic lysosomal reformation.
- PN references (titles):
    - Defective autophagy in spastizin mutated patients with hereditary spastic paraparesis type 15 | Brain | Oxford Academic (oup.com)
    - JCI - Spastic paraplegia proteins spastizin and spatacsin mediate autophagic lysosome reformation
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Specific function in autophagic lysosome reformation unknown
        status=no_mapping scope= GO=[]
        rationale: This PN group explicitly states that the specific role within autophagic lysosome reformation is unknown. That makes GO propagation unsafe until a narrower mechanistic interpretation is available.
    - [class] Autophagy-Lysosome Pathway|Autophagic lysosome reformation
        status=context_only scope=too_broad_to_propagate GO=[GO:0007040 lysosome organization]
        rationale: Autophagic lysosome reformation is the lysosome-regeneration phase that follows autolysosome formation and cargo degradation. As a class, it is better aligned to lysosome organization than to generic autophagy, but the PN members are mechanistically mixed across membrane remodeling, tubulation, product efflux, and unknown late-stage roles, so class-level propagation would still over-annotate.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.
