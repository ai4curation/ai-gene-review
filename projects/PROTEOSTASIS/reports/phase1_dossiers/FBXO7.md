# PN dossier: FBXO7

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO7/FBXO7-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Substrate selectivity regulator for selective autophagy | Mitophagy | PINK/PRKN pathway
- UniProt: Q9Y3I1
- In branches: ALP, UPS
- Notes: F-box only protein, component of SCF E3 ubiquitin ligase complex. Interacts with PINK1 and PRKN. Involved in translocation of PRKN to mitochondria. FBXO7 interacts with PINK1 and facilitate the translocation of Parkin/PINK1 translocation to the mitochondria.
- PN references (titles):
    - The Parkinson's disease–linked proteins Fbxo7 and Parkin interact to mediate mitophagy | Nature Neuroscience
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy|Mitophagy|PINK/PRKN pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN type groups substrate-selectivity regulators assigned to mitophagy. Those factors participate in mitophagy, but the PN category is more specific than the full process term.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBL domain | E3 ligases | CUL1 receptor / F-box
- UniProt: Q9Y3I1
- In branches: ALP, UPS
- Signature domains: (IPR029071)
- Auxiliary domains: IPR001810, IPR021625
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|E3 ligases|CUL1 receptor / F-box
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN subtype identifies a UBL-domain F-box/CUL1 receptor role. The safe shared molecular function is ubiquitin-like ligase-substrate adaptor activity rather than catalytic E3 activity.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|E3 ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This UBL-domain type is an E3-ligase context, but descendants include catalytic E3s as well as cullin receptor/adaptor components. Direct propagation is restricted to narrower subtypes.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain
        status=context_only scope=too_broad_to_propagate GO=[GO:0043130 ubiquitin binding]
        rationale: This group records UBL-domain protein context, but descendants include enzymes, adaptors, chaperone-related proteins, non-enzymatic proteins, and nucleic-acid factors. Propagation is restricted to narrower nodes.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | PI31, UBL
- UniProt: Q9Y3I1
- In branches: ALP, UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR021625, (IPR029071)
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|PI31, UBL
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy|Mitophagy
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|E3 ligases|CUL1 receptor / F-box
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
