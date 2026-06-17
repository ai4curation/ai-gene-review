# PN dossier: SEC62

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SEC62/SEC62-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Protein transport | SEC61 channel complex component
- UniProt: Q99442
- In branches: ER, ALP
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|SEC61 channel complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005784 Sec61 translocon complex]
        rationale: This PN group denotes SEC61 translocon components. The GO Sec61 translocon complex term is the direct cellular-component target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q99442
- In branches: ER, ALP
- Notes: Receptor for selective autophagy. An ER-resident autophagy receptor. Contains a conserved LC3-interacting region in the C-terminal cytosolic domain that is required for its function in recovER-phagy, but is dispensable for its function in the protein translocation machinery. Active in ERphagy
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Translocon component Sec62 acts in endoplasmic reticulum turnover during stress recovery
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN uses the community label ERphagy for selective autophagy of the endoplasmic reticulum, while GO uses the synonym reticulophagy. Receptor members of this PN category are suitable for propagation to the GO reticulophagy process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Microautophagy | Microreticulophagy
- UniProt: Q99442
- In branches: ER, ALP
- PN-node mapping records (path + ancestors):
    - [group] Autophagy-Lysosome Pathway|Microautophagy|Microreticulophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061709 reticulophagy]
        rationale: This group is an ER-autophagy context, but the source label is microreticulophagy and the members mix core autophagy factors with SEC62. Reticulophagy is kept as context only pending a more specific GO term or gene-level review.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport
- GO:0005784 Sec61 translocon complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|SEC61 channel complex component
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
