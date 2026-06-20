# PN dossier: AZI2

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/AZI2/AZI2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Autophagy receptor regulation | Xenophagy
- UniProt: Q9H6S1
- In branches: ALP
- Notes: Adapter protein for TBK1 complex, essential for xenophagy. Binds to CALCOCO2.
- PN references (titles):
    - The Cargo Receptor NDP52 Initiates Selective Autophagy by Recruiting the ULK Complex to Cytosol-Invading Bacteria - ScienceDirect
    - Full article: CALCOCO2/NDP52 initiates selective autophagy through recruitment of ULK and TBK1 kinase complexes (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Xenophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0098792 xenophagy]
        rationale: This PN type groups receptor-regulatory factors assigned to xenophagy. The source category sits inside the xenophagy mechanism rather than being equivalent to the full process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Xenophagy
