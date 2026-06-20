# PN dossier: CCDC50

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/CCDC50/CCDC50-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Individual substrates
- UniProt: Q8IVM0
- In branches: ALP, UPS
- Notes: Delivers ubiquitinated NLRP3 inflammasome to autophagosome for degradation
- PN references (titles):
    - CCDC50 suppresses NLRP3 inflammasome activity by mediating autophagic degradation of NLRP3 | EMBO reports (embopress.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Individual substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160247 autophagy cargo adaptor activity]
        rationale: This PN category groups receptors such as TRIM-family factors that bind specific substrates and recruit autophagy components for their turnover. That aligns best with autophagy cargo adaptor activity rather than with a single selective-autophagy process term.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | macroautophagy | MIU
- UniProt: Q8IVM0
- In branches: ALP, UPS
- Signature domains: PMID: 16499958
- Auxiliary domains: (none)
- PN references (titles):
    - 16499958
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|macroautophagy|MIU
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a selective-autophagy or trafficking subdivision under a UPS binding context. The autophagy context is real, but this node is too indirect for automatic GO propagation.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|macroautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This PN type is an autophagy-related trafficking context, but the earlier TRAPP review showed that generic autophagy propagation from component or binding-context buckets can be too strong. Keep as context unless gene-level evidence supports macroautophagy.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Individual substrates
