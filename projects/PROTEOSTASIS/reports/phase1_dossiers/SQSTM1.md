# PN dossier: SQSTM1

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/SQSTM1/SQSTM1-ai-review.yaml
- PN workbook rows: 8

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | Miscellaneous function - autophagy component recruitment to autophagophore
- UniProt: Q13501
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, Ub-dependent pexophagy, zymophagy, xenophagy, virophagy, and midbody autophagy. Also SQSTM1 bodies (phase separated gels) sequester autophagy-related proteins and serve as a platform for autophagosome formation. Specificity for autophagy of peroxisomes (pexophagy) is provided by ATM phosphorylation of PEX5 at Ser 141, which promotes PEX5 monoubiquitylation at Lys 209, and recognition of ubiquitylated PEX5 by the autophagy adaptor protein p62, directing the autophagosome to peroxisomes to induce pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6 and that these proteins, as well as NBR1, are important for efficient clearance of midbody ring derivatives by autophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - p62/SQSTM1 Binds Directly to Atg8/LC3 to Facilitate Degradation of Ubiquitinated Protein Aggregates by Autophagy - ScienceDirect
    - Frontiers | Selective Autophagy Receptor p62/SQSTM1, a Pivotal Player in Stress and Aging | Cell and Developmental Biology (frontiersin.org)
    - p62/SQSTM1-droplet serves as a platform for autophagosome formation and anti-oxidative stress response | Nature Communications
    - ATM functions at the peroxisome to induce pexophagy in response to ROS
    - The Adaptor Protein p62/SQSTM1 Targets Invading Bacteria to the Autophagy Pathway
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - p62/SQSTM1 and ALFY interact to facilitate the formation of p62 bodies/ALIS and their degradation by autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|Miscellaneous function - autophagy component recruitment to autophagophore
        status=no_mapping scope= GO=[]
        rationale: This PN leaf is an explicit catch-all recruitment bucket rather than a coherent shared GO function or process class. The current members span scaffolding, cargo recruitment, and broad stress or membrane-traffic roles.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: Q13501
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, Ub-dependent pexophagy, zymophagy, xenophagy, virophagy, and midbody autophagy. Also SQSTM1 bodies (phase separated gels) sequester autophagy-related proteins and serve as a platform for autophagosome formation. Specificity for autophagy of peroxisomes (pexophagy) is provided by ATM phosphorylation of PEX5 at Ser 141, which promotes PEX5 monoubiquitylation at Lys 209, and recognition of ubiquitylated PEX5 by the autophagy adaptor protein p62, directing the autophagosome to peroxisomes to induce pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6 and that these proteins, as well as NBR1, are important for efficient clearance of midbody ring derivatives by autophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - p62/SQSTM1 Binds Directly to Atg8/LC3 to Facilitate Degradation of Ubiquitinated Protein Aggregates by Autophagy - ScienceDirect
    - Frontiers | Selective Autophagy Receptor p62/SQSTM1, a Pivotal Player in Stress and Aging | Cell and Developmental Biology (frontiersin.org)
    - p62/SQSTM1-droplet serves as a platform for autophagosome formation and anti-oxidative stress response | Nature Communications
    - ATM functions at the peroxisome to induce pexophagy in response to ROS
    - The Adaptor Protein p62/SQSTM1 Targets Invading Bacteria to the Autophagy Pathway
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - p62/SQSTM1 and ALFY interact to facilitate the formation of p62 bodies/ALIS and their degradation by autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN path denotes selective-autophagy receptors for mitochondrial cargo. The source category is a mechanistic sub-role within mitophagy, so propagation rather than exact equivalence is the correct scope.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Pexophagy
- UniProt: Q13501
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, Ub-dependent pexophagy, zymophagy, xenophagy, virophagy, and midbody autophagy. Also SQSTM1 bodies (phase separated gels) sequester autophagy-related proteins and serve as a platform for autophagosome formation. Specificity for autophagy of peroxisomes (pexophagy) is provided by ATM phosphorylation of PEX5 at Ser 141, which promotes PEX5 monoubiquitylation at Lys 209, and recognition of ubiquitylated PEX5 by the autophagy adaptor protein p62, directing the autophagosome to peroxisomes to induce pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6 and that these proteins, as well as NBR1, are important for efficient clearance of midbody ring derivatives by autophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - p62/SQSTM1 Binds Directly to Atg8/LC3 to Facilitate Degradation of Ubiquitinated Protein Aggregates by Autophagy - ScienceDirect
    - Frontiers | Selective Autophagy Receptor p62/SQSTM1, a Pivotal Player in Stress and Aging | Cell and Developmental Biology (frontiersin.org)
    - p62/SQSTM1-droplet serves as a platform for autophagosome formation and anti-oxidative stress response | Nature Communications
    - ATM functions at the peroxisome to induce pexophagy in response to ROS
    - The Adaptor Protein p62/SQSTM1 Targets Invading Bacteria to the Autophagy Pathway
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - p62/SQSTM1 and ALFY interact to facilitate the formation of p62 bodies/ALIS and their degradation by autophagy
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

## PN row 4: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Xenophagy
- UniProt: Q13501
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, Ub-dependent pexophagy, zymophagy, xenophagy, virophagy, and midbody autophagy. Also SQSTM1 bodies (phase separated gels) sequester autophagy-related proteins and serve as a platform for autophagosome formation. Specificity for autophagy of peroxisomes (pexophagy) is provided by ATM phosphorylation of PEX5 at Ser 141, which promotes PEX5 monoubiquitylation at Lys 209, and recognition of ubiquitylated PEX5 by the autophagy adaptor protein p62, directing the autophagosome to peroxisomes to induce pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6 and that these proteins, as well as NBR1, are important for efficient clearance of midbody ring derivatives by autophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - p62/SQSTM1 Binds Directly to Atg8/LC3 to Facilitate Degradation of Ubiquitinated Protein Aggregates by Autophagy - ScienceDirect
    - Frontiers | Selective Autophagy Receptor p62/SQSTM1, a Pivotal Player in Stress and Aging | Cell and Developmental Biology (frontiersin.org)
    - p62/SQSTM1-droplet serves as a platform for autophagosome formation and anti-oxidative stress response | Nature Communications
    - ATM functions at the peroxisome to induce pexophagy in response to ROS
    - The Adaptor Protein p62/SQSTM1 Targets Invading Bacteria to the Autophagy Pathway
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - p62/SQSTM1 and ALFY interact to facilitate the formation of p62 bodies/ALIS and their degradation by autophagy
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Xenophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0098792 xenophagy]
        rationale: This PN category captures receptors for selective autophagy of pathogens or pathogen-derived material. The receptor class is narrower than the GO xenophagy process, so this is a propagation mapping.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 5: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Aggrephagy
- UniProt: Q13501
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, Ub-dependent pexophagy, zymophagy, xenophagy, virophagy, and midbody autophagy. Also SQSTM1 bodies (phase separated gels) sequester autophagy-related proteins and serve as a platform for autophagosome formation. Specificity for autophagy of peroxisomes (pexophagy) is provided by ATM phosphorylation of PEX5 at Ser 141, which promotes PEX5 monoubiquitylation at Lys 209, and recognition of ubiquitylated PEX5 by the autophagy adaptor protein p62, directing the autophagosome to peroxisomes to induce pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6 and that these proteins, as well as NBR1, are important for efficient clearance of midbody ring derivatives by autophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - p62/SQSTM1 Binds Directly to Atg8/LC3 to Facilitate Degradation of Ubiquitinated Protein Aggregates by Autophagy - ScienceDirect
    - Frontiers | Selective Autophagy Receptor p62/SQSTM1, a Pivotal Player in Stress and Aging | Cell and Developmental Biology (frontiersin.org)
    - p62/SQSTM1-droplet serves as a platform for autophagosome formation and anti-oxidative stress response | Nature Communications
    - ATM functions at the peroxisome to induce pexophagy in response to ROS
    - The Adaptor Protein p62/SQSTM1 Targets Invading Bacteria to the Autophagy Pathway
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - p62/SQSTM1 and ALFY interact to facilitate the formation of p62 bodies/ALIS and their degradation by autophagy
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

## PN row 6: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Midbody autophagy
- UniProt: Q13501
- In branches: ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in aggrephagy, Ub-dependent mitophagy, Ub-dependent pexophagy, zymophagy, xenophagy, virophagy, and midbody autophagy. Also SQSTM1 bodies (phase separated gels) sequester autophagy-related proteins and serve as a platform for autophagosome formation. Specificity for autophagy of peroxisomes (pexophagy) is provided by ATM phosphorylation of PEX5 at Ser 141, which promotes PEX5 monoubiquitylation at Lys 209, and recognition of ubiquitylated PEX5 by the autophagy adaptor protein p62, directing the autophagosome to peroxisomes to induce pexophagy. Interacts with adaptor protein WDFY3/ALFY form a complex with the ubiquitin E3 ligase TRAF6 and that these proteins, as well as NBR1, are important for efficient clearance of midbody ring derivatives by autophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - p62/SQSTM1 Binds Directly to Atg8/LC3 to Facilitate Degradation of Ubiquitinated Protein Aggregates by Autophagy - ScienceDirect
    - Frontiers | Selective Autophagy Receptor p62/SQSTM1, a Pivotal Player in Stress and Aging | Cell and Developmental Biology (frontiersin.org)
    - p62/SQSTM1-droplet serves as a platform for autophagosome formation and anti-oxidative stress response | Nature Communications
    - ATM functions at the peroxisome to induce pexophagy in response to ROS
    - The Adaptor Protein p62/SQSTM1 Targets Invading Bacteria to the Autophagy Pathway
    - TRAF6 mediates ubiquitination of KIF23/MKLP1 and is required for midbody ring degradation by selective autophagy
    - p62/SQSTM1 and ALFY interact to facilitate the formation of p62 bodies/ALIS and their degradation by autophagy
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

## PN row 7: Ubiquitin Proteasome System | Proteasome and associated proteins | adaptors | PB1 | UBA
- UniProt: Q13501
- In branches: ALP, UPS
- Signature domains: IPR034866
- Auxiliary domains: IPR000270, IPR015940, IPR034866
- PN references (titles):
    - 15340068
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|PB1|UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|PB1
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070628 proteasome binding]
        rationale: This PN group captures proteasome adaptors and shuttle factors. Proteasome binding is the safe shared molecular-function target.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 8: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | selective autophagy | UBA
- UniProt: Q13501
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

## Projected GO annotations (6)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
- GO:0000425 pexophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Pexophagy
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Xenophagy
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Aggrephagy
- GO:0160247 autophagy cargo adaptor activity | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Midbody autophagy
- GO:0070628 proteasome binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
