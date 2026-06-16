# PN dossier: VPS37A

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS37A/VPS37A-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q8NEZ2
- In branches: ALP, UPS
- Notes: Component of the ESCRT-I complex, involved in autophagosome closure. Specifically called out for directing recruitment of ESCRT machinery to autophagophore. Also, localizes to phagophore and recruits ESCRT machinery for phagophore closure
- PN references (titles):
    - A helical assembly of human ESCRT-I scaffolds reverse-topology membrane scission | Nature Structural & Molecular Biology
    - VPS37A directs ESCRT recruitment for phagophore closure | Journal of Cell Biology | Rockefeller University Press (rupress.org)
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000813 ESCRT I complex]
        rationale: This leaf is restricted to ESCRT-I components used in autophagophore sealing. The shared GO assertion is ESCRT I complex membership.
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
- UniProt: Q8NEZ2
- In branches: ALP, UPS
- Notes: Component of the ESCRT-I complex, involved in autophagosome closure. Specifically called out for directing recruitment of ESCRT machinery to autophagophore. Also, localizes to phagophore and recruits ESCRT machinery for phagophore closure
- PN references (titles):
    - A helical assembly of human ESCRT-I scaffolds reverse-topology membrane scission | Nature Structural & Molecular Biology
    - VPS37A directs ESCRT recruitment for phagophore closure | Journal of Cell Biology | Rockefeller University Press (rupress.org)
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

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | ESCRT-I complex | UEV (Type 2)
- UniProt: Q8NEZ2
- In branches: ALP, UPS
- Signature domains: cd11685
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex|UEV (Type 2)
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
