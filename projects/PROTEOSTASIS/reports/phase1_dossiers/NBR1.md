# PN dossier: NBR1

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/NBR1/NBR1-ai-review.yaml
- PN workbook rows: 4

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Pexophagy
- UniProt: Q14596
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent pexophagy, midbody autophagy. Its amphipathic α-helical J domain, the ubiquitin-associated (UBA) domain, the LC3-interacting region and the coiled-coil domain are necessary to mediate pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6,  important for efficient clearance of midbody ring derivatives by autophagy. Binds to midbody protein CEP55 to facilitate midbody clearance.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - NBR1 acts as an autophagy receptor for peroxisomes
    - A Role for NBR1 in Autophagosomal Degradation of Ubiquitinated Substrates
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - Midbody accumulation through evasion of autophagy contributes to cellular reprogramming and tumorigenicity
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Pexophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000425 pexophagy]
        rationale: This PN path groups receptors for selective autophagic turnover of peroxisomes. The role is part of, but not equivalent to, the full GO pexophagy process, so propagation scope is appropriate.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Aggrephagy
- UniProt: Q14596
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent pexophagy, midbody autophagy. Its amphipathic α-helical J domain, the ubiquitin-associated (UBA) domain, the LC3-interacting region and the coiled-coil domain are necessary to mediate pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6,  important for efficient clearance of midbody ring derivatives by autophagy. Binds to midbody protein CEP55 to facilitate midbody clearance.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - NBR1 acts as an autophagy receptor for peroxisomes
    - A Role for NBR1 in Autophagosomal Degradation of Ubiquitinated Substrates
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - Midbody accumulation through evasion of autophagy contributes to cellular reprogramming and tumorigenicity
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: This PN path denotes receptors that recognize aggregation cargo for the aggrephagy pathway. The category is not identical to the GO process term, but propagation to aggrephagy is appropriate because membership in this receptor class implies direct participation in that process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Midbody autophagy
- UniProt: Q14596
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent pexophagy, midbody autophagy. Its amphipathic α-helical J domain, the ubiquitin-associated (UBA) domain, the LC3-interacting region and the coiled-coil domain are necessary to mediate pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6,  important for efficient clearance of midbody ring derivatives by autophagy. Binds to midbody protein CEP55 to facilitate midbody clearance.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - NBR1 acts as an autophagy receptor for peroxisomes
    - A Role for NBR1 in Autophagosomal Degradation of Ubiquitinated Substrates
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - Midbody accumulation through evasion of autophagy contributes to cellular reprogramming and tumorigenicity
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Midbody autophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160247 autophagy cargo adaptor activity]
        rationale: Midbody-autophagy receptors such as SQSTM1 link ubiquitinated midbody material to the autophagy machinery. GO does not currently expose a dedicated midbody-autophagy process term in the local ontology cache, so the receptor activity term is the best available mapping target.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | selective autophagy | UBA
- UniProt: Q14596
- In branches: ALP, UPS
- Signature domains: IPR015940
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|selective autophagy|UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a selective-autophagy or trafficking subdivision under a UPS binding context. The autophagy context is real, but this node is too indirect for automatic GO propagation.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|selective autophagy
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
- GO:0000425 pexophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Pexophagy
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Midbody autophagy
