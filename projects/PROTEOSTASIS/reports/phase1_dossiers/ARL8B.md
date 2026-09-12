# PN dossier: ARL8B

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ARL8B/ARL8B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Localization of the autophagosome | Movement of autophagosomes along microtubules | HOPS-BORC complex bridging
- UniProt: Q9NVJ2
- In branches: ALP
- Notes: Small GTPase that regulates lysosome positioning and bridges the HOPS and BORC complexes for autophagosome-lysosome fusion. Also serves as a link to the dynein-dynactin system for vesicles.
- PN references (titles):
    - Arf-like GTPase Arl8: Moving from the periphery to the center of lysosomal biology (tandfonline.com)
    - Full article: BORC coordinates encounter and fusion of lysosomes with autophagosomes (tandfonline.com)
    - RUFY3 and RUFY4 are ARL8 effectors that promote coupling of endolysosomes to dynein-dynactin | Nature Communications
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules|HOPS-BORC complex bridging
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061906 autophagosome localization]
        rationale: This PN subtype denotes the bridging machinery that links HOPS/BORC-like late-endolysosomal transport systems to autophagosome positioning on microtubules. The best current GO target is autophagosome localization.
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061906 autophagosome localization]
        rationale: This leaf describes a mechanism for positioning autophagosomes. The safe shared GO target is autophagosome localization, not the downstream fusion process.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061906 autophagosome localization]
        rationale: This group is explicitly about positioning/autophagosome localization in late autophagy. Autophagosome localization is the correct propagation target rather than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Autophagosome-lysosome docking | HOPS-BORC interaction mediator
- UniProt: Q9NVJ2
- In branches: ALP
- Notes: Small GTPase that regulates lysosome positioning and bridges the HOPS and BORC complexes for autophagosome-lysosome fusion. Also serves as a link to the dynein-dynactin system for vesicles.
- PN references (titles):
    - Arf-like GTPase Arl8: Moving from the periphery to the center of lysosomal biology (tandfonline.com)
    - Full article: BORC coordinates encounter and fusion of lysosomes with autophagosomes (tandfonline.com)
    - RUFY3 and RUFY4 are ARL8 effectors that promote coupling of endolysosomes to dynein-dynactin | Nature Communications
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking|HOPS-BORC interaction mediator
        status=context_only scope=too_broad_to_propagate GO=[GO:0061909 autophagosome-lysosome fusion]
        rationale: Reviewed as an interaction-mediator bucket in autophagosome-lysosome docking. The relation to fusion is contextual and should not project generic fusion to all members.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking
        status=context_only scope=too_broad_to_propagate GO=[GO:0061909 autophagosome-lysosome fusion]
        rationale: Reviewed as an autophagosome-lysosome docking context. The subtree mixes component buckets and modulators, so generic fusion propagation should come only from narrower reviewed mechanism leaves.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0061906 autophagosome localization | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome
- GO:0061906 autophagosome localization | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules
- GO:0061906 autophagosome localization | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules|HOPS-BORC complex bridging
