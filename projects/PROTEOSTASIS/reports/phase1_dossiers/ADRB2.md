# PN dossier: ADRB2

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ADRB2/ADRB2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Lipophagy | Upstream lipophagy signaling
- UniProt: P07550
- In branches: ALP
- Notes: Mediates beta-adrenergic receptor-stimulated lipophagy which decreases following inhibition of autophagy
- PN references (titles):
    - Full article: β-adrenergic receptor-stimulated lipolysis requires the RAB7-mediated autolysosomal lipid degradation (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy|Upstream lipophagy signaling
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

## Projected GO annotations (1)
- GO:0061724 lipophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Lipophagy
