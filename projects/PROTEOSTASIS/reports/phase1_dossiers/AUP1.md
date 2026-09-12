# PN dossier: AUP1

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/AUP1/AUP1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Retrotranslocation channel complex
- UniProt: Q9Y679
- In branches: ER, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Retrotranslocation channel complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Lipophagy | Ubiquitination of lipid droplet surface proteins
- UniProt: Q9Y679
- In branches: ER, ALP, UPS
- Notes: Recruits E2-ligase UBE2G2 to lipid droplets to ubiquitinate surface proteins for lipophagy
- PN references (titles):
    - Ancient Ubiquitous Protein 1 (AUP1) Localizes to Lipid Droplets and Binds the E2 Ubiquitin Conjugase G2 (Ube2g2) via Its G2 Binding Region* ♦ - Journal of Biological Chemistry (jbc.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy|Ubiquitination of lipid droplet surface proteins
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061724 lipophagy]
        rationale: This PN type denotes factors that mark lipid cargo for selective autophagy. The category is narrower than the full lipophagy process, so propagation scope is the correct fit.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | protein quality control | ERAD cofactor | CUE
- UniProt: Q9Y679
- In branches: ER, ALP, UPS
- Signature domains: IPR003892
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor|CUE
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway]
        rationale: This PN type groups ubiquitin/UBL-binding factors that act as ERAD cofactors in protein-quality-control contexts. The best available GO target in the local cache is ubiquitin-dependent glycoprotein ERAD pathway, used here at propagation scope.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control
        status=context_only scope=too_broad_to_propagate GO=[GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process]
        rationale: This PN group is a protein-quality-control context bucket, but its descendants include ERAD cofactors, HSP70 cochaperone context, stalled-chain recognition, and other mixed roles. Direct propagation should come from narrower nodes such as ERAD cofactor.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0061724 lipophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy
- GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor
