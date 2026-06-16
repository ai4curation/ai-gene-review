# PN dossier: TBK1

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/TBK1/TBK1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, direct | Modulator of mTORC1 activity
- UniProt: Q9UHD2
- In branches: ALP, UPS
- Notes: Enhances GTP exchange by SMCR8 by phosphorylation. Can activate or inhibit mTORC1 by phosphorylating MTOR or RPTOR, respectively. Also phosphorylates autophagy receptors Optinuerin (OPTN), NDP52, TAX1BP1, and P62 when bound to TANK, linking ubiquitinated cargo to autophagic membranes. Constitutive interaction of TBK1 with OPTN and OPTN binding with ubiquitin chains are essential for TBK1 recruitment and kinase activation on mitochondria.
- PN references (titles):
    - Full article: Multifaceted role of SMCR8 as autophagy regulator (tandfonline.com)
    - TBK1 (TANK-binding kinase 1)-mediated regulation of autophagy in health and disease - ScienceDirect
    - Phosphorylation of OPTN by TBK1 enhances its binding to Ub chains and promotes selective autophagy of damaged mitochondria | PNAS
    - Expanding the ubiquitin code through post-translational modification
    - The ubiquitin kinase PINK1 recruits autophagy receptors to induce mitophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, direct|Modulator of mTORC1 activity
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, direct
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class organizes upstream signaling inputs to autophagy initiation. Because the subtree contains generic insulin, AMPK, mTORC1, nutrient-sensing, and miscellaneous signaling components, class-level propagation to regulation of autophagy would over-annotate many genes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Autophagy receptor regulation | Mitophagy
- UniProt: Q9UHD2
- In branches: ALP, UPS
- Notes: Enhances GTP exchange by SMCR8 by phosphorylation. Can activate or inhibit mTORC1 by phosphorylating MTOR or RPTOR, respectively. Also phosphorylates autophagy receptors Optinuerin (OPTN), NDP52, TAX1BP1, and P62 when bound to TANK, linking ubiquitinated cargo to autophagic membranes. Constitutive interaction of TBK1 with OPTN and OPTN binding with ubiquitin chains are essential for TBK1 recruitment and kinase activation on mitochondria.
- PN references (titles):
    - Full article: Multifaceted role of SMCR8 as autophagy regulator (tandfonline.com)
    - TBK1 (TANK-binding kinase 1)-mediated regulation of autophagy in health and disease - ScienceDirect
    - Phosphorylation of OPTN by TBK1 enhances its binding to Ub chains and promotes selective autophagy of damaged mitochondria | PNAS
    - Expanding the ubiquitin code through post-translational modification
    - The ubiquitin kinase PINK1 recruits autophagy receptors to induce mitophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: The PN receptor-regulation type for mitophagy captures factors that tune receptor activity within the mitophagy pathway. This supports propagation to mitophagy while preserving that the source is a regulatory sub-role.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBL domain | other enzymes | kinase
- UniProt: Q9UHD2
- In branches: ALP, UPS
- Signature domains: IPR041087
- Auxiliary domains: IPR000719
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|other enzymes|kinase
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|other enzymes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain
        status=context_only scope=too_broad_to_propagate GO=[GO:0043130 ubiquitin binding]
        rationale: This group records UBL-domain protein context, but descendants include enzymes, adaptors, chaperone-related proteins, non-enzymatic proteins, and nucleic-acid factors. Propagation is restricted to narrower nodes.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy
