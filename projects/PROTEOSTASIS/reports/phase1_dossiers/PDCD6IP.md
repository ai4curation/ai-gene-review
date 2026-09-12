# PN dossier: PDCD6IP

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/PDCD6IP/PDCD6IP-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Localization of the ESCRT-III complex
- UniProt: Q8WUM4
- In branches: ALP
- Notes: Binds to ATG13-ATG3 complexes to recruit ESCRT-III for autophagosome closure
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Synergies in exosomes and autophagy pathways for cellular homeostasis and metastasis of tumor cells | Cell & Bioscience | Full Text (biomedcentral.com)
    - ATG12–ATG3 interacts with Alix to promote basal autophagic flux and late endosome function | Nature Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|Localization of the ESCRT-III complex
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups factors that affect ESCRT-III localization during sealing, but the current member set mixes endosomal sorting and SNARE trafficking genes rather than one clean shared autophagy-specific GO term.
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
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
