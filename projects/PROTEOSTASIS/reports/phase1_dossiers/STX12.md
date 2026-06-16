# PN dossier: STX12

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/STX12/STX12-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex activity modulator
- UniProt: Q86Y82
- In branches: ALP
- Notes: Works with ESCRT-III complex (and is a genetic modifier for mutations in CHMP2B) for autophagosome closure, along with its binding partner VTI1A. Knockdown of STX12 or its binding partner VTI1A leads to accumulation of the autophagy marker LC3, affects autophagosome maturation, and blocks autophagic flux. Also, is a recycling endosome SNARE that regulates autophagosome closure and acts upstream of ESCRT-III.
- PN references (titles):
    - Syntaxin 13, a Genetic Modifier of Mutant CHMP2B in Frontotemporal Dementia, Is Required for Autophagosome Maturation - ScienceDirect
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex activity modulator
        status=context_only scope=too_broad_to_propagate GO=[GO:0000815 ESCRT III complex]
        rationale: Reviewed as an ESCRT-III activity modulator. It is related to ESCRT-III but should not project ESCRT-III complex membership to all members.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | Localization of the ESCRT-III complex
- UniProt: Q86Y82
- In branches: ALP
- Notes: Works with ESCRT-III complex (and is a genetic modifier for mutations in CHMP2B) for autophagosome closure, along with its binding partner VTI1A. Knockdown of STX12 or its binding partner VTI1A leads to accumulation of the autophagy marker LC3, affects autophagosome maturation, and blocks autophagic flux. Also, is a recycling endosome SNARE that regulates autophagosome closure and acts upstream of ESCRT-III.
- PN references (titles):
    - Syntaxin 13, a Genetic Modifier of Mutant CHMP2B in Frontotemporal Dementia, Is Required for Autophagosome Maturation - ScienceDirect
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
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

## PN row 3: Autophagy-Lysosome Pathway | Microautophagy | General microautophagy machinery | ESCRT-III complex component
- UniProt: Q86Y82
- In branches: ALP
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000815 ESCRT III complex]
        rationale: This leaf is a component bucket for ESCRT-III machinery used in microautophagy contexts. The shared GO assertion is ESCRT III complex membership.
    - [group] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component
