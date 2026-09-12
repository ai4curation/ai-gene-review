# SQSTM1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q13501
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SQSTM1/SQSTM1-ai-review.yaml](SQSTM1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SQSTM1/SQSTM1-ai-review.html
- Gene notes: present - [genes/human/SQSTM1/SQSTM1-notes.md](SQSTM1-notes.md)
- GOA TSV: present - [genes/human/SQSTM1/SQSTM1-goa.tsv](SQSTM1-goa.tsv)
- UniProt record: present - [genes/human/SQSTM1/SQSTM1-uniprot.txt](SQSTM1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SQSTM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SQSTM1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SQSTM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SQSTM1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SQSTM1/SQSTM1-deep-research-falcon.md](SQSTM1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SQSTM1 (sequestosome-1, p62) is a multidomain cytoplasmic adaptor protein and the prototypical selective autophagy receptor. Its N-terminal PB1 domain drives homo-oligomerization (front-to-back filament-like arrays) and hetero-oligomerization with partners such as the atypical protein kinases PRKCZ/PRKCI, NBR1 and MAP2K5; a ZZ-type zinc finger binds RIPK1; a TRAF6-binding (TB) motif scaffolds TRAF6; an LC3-interacting region (LIR) binds ATG8-family proteins (LC3A/B/C, GABARAP/L1/L2); a KEAP1-interacting region (KIR) binds KEAP1 when phosphorylated at Ser-349; and a C-terminal UBA domain binds polyubiquitin, with a strong preference for K63-linked chains. By simultaneously binding ubiquitinated cargo through the UBA domain and the growing autophagosome through the LIR, p62 bridges ubiquitin-tagged substrates to the autophagy machinery. Multivalent ubiquitin binding combined with PB1-mediated polymerization drives liquid-liquid phase separation into "p62 bodies," membraneless condensates that concentrate ubiquitinated cargo for engulfment; p62 and its cargo are then degraded together. This underlies aggrephagy (clearance of ubiquitinated protein aggregates) and more specialized selective autophagy including pexophagy (via ubiquitinated PEX5), xenophagy/antibacterial autophagy and control of inflammasome and RIPosome components. p62 also contributes to PINK1/Parkin mitophagy, where it is recruited to depolarized mitochondria and mediates their perinuclear clustering, though it is largely dispensable for the mitochondrial clearance step itself. Independent of autophagy, phospho-Ser349 p62 sequesters KEAP1 into condensates, derepressing the transcription factor NRF2 (NFE2L2) to induce cytoprotective antioxidant/phase-II genes; SQSTM1 is itself an NRF2 target, forming a positive feedback loop. Through its PB1, ZZ and TB modules p62 serves as a signaling scaffold for NF-kB activation downstream of IL-1/TRAF6, NGF/TrkA and TNF/RIPK1, and it modulates additional pathways including mTORC1 signaling. p62 levels are an established readout of autophagic flux, and SQSTM1 variants cause Paget disease of bone, frontotemporal dementia/ALS, distal myopathy with rimmed vacuoles, and (recessively) childhood-onset neurodegeneration.
- Existing/core annotation action counts: ACCEPT: 122; KEEP_AS_NON_CORE: 150

## PN Consistency Summary

- **Consistency:** Strong agreement on the core selective-autophagy-receptor story across deep research, review, PN notes, and node mappings. Review ACCEPTs aggrephagy (GO:0035973), mitophagy (KEEP_AS_NON_CORE — recruitment but dispensable for clearance, PMID:20890124), pexophagy (GO:0000425, IDA PMID:26344566). No contradictions; PN notes (PEX5-ATM, TRAF6/ALFY midbody, bacteria) match review description.
- **PN story / NEW pressure:** PN surfaces three terms absent from GOA/review: GO:0098792 xenophagy (verified real; GOA has none — review only narrates antibacterial autophagy in `description`), GO:0160247 autophagy cargo adaptor activity (verified; review uses GO:0030674 protein-macromolecule adaptor + GO:0140036 reader instead), and GO:0070628 proteasome binding (verified; PB1/UBA shuttle role). Cargo-adaptor and xenophagy are defensible ADDs (the recurring receptor-MF elevation pattern); proteasome binding is plausible but weaker (PB1/UBA shuttle to proteasome is real but secondary).
- **Evidence alignment:** Strong overlap on ALP rows (Pankiv 17580304, Pilli/Wild xenophagy, ATM-pexophagy 26344566, TRAF6 midbody). PN UPS row 7 cites bare PMID 15340068 (proteasome-shuttle) not in review references.
- **Verdict:** CONSISTENT; defensible ADD of GO:0160247 cargo adaptor activity and GO:0098792 xenophagy to the review.

## Full Consistency Review

- **UniProt:** Q13501 (p62/sequestosome-1) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (very large, ~3380 lines; ~70 IPI bare-protein-binding entries kept non-core)
- **PN placement:** ALP `Autophagy substrate selection|Selective autophagy receptor|{Mitophagy,Pexophagy,Xenophagy,Aggrephagy,Midbody autophagy}` + `Autophagophore...|component recruitment` + UPS `Proteasome...|adaptors|PB1|UBA` and `Ubiquitin and UBL binding|trafficking|selective autophagy|UBA` ; **PN-node mapping:** leaf types mapped → GO:0000423 mitophagy, GO:0000425 pexophagy, GO:0098792 xenophagy, GO:0035973 aggrephagy, GO:0160247 cargo adaptor (midbody); UPS adaptors group → GO:0070628 proteasome binding; all ancestors no_mapping/context_only.
- **Consistency:** Strong agreement on the core selective-autophagy-receptor story across deep research, review, PN notes, and node mappings. Review ACCEPTs aggrephagy (GO:0035973), mitophagy (KEEP_AS_NON_CORE — recruitment but dispensable for clearance, PMID:20890124), pexophagy (GO:0000425, IDA PMID:26344566). No contradictions; PN notes (PEX5-ATM, TRAF6/ALFY midbody, bacteria) match review description.
- **PN story / NEW pressure:** PN surfaces three terms absent from GOA/review: GO:0098792 xenophagy (verified real; GOA has none — review only narrates antibacterial autophagy in `description`), GO:0160247 autophagy cargo adaptor activity (verified; review uses GO:0030674 protein-macromolecule adaptor + GO:0140036 reader instead), and GO:0070628 proteasome binding (verified; PB1/UBA shuttle role). Cargo-adaptor and xenophagy are defensible ADDs (the recurring receptor-MF elevation pattern); proteasome binding is plausible but weaker (PB1/UBA shuttle to proteasome is real but secondary).
- **Mapping strategy:** Mappings are sound and conservative (ancestors held back). The KEY PATTERN applies: elevate GO:0160247 cargo adaptor over bare protein binding. Review already captures this via GO:0030674; harmonizing to GO:0160247 would align review with PN.
- **Evidence alignment:** Strong overlap on ALP rows (Pankiv 17580304, Pilli/Wild xenophagy, ATM-pexophagy 26344566, TRAF6 midbody). PN UPS row 7 cites bare PMID 15340068 (proteasome-shuttle) not in review references.
- **Verdict:** CONSISTENT; defensible ADD of GO:0160247 cargo adaptor activity and GO:0098792 xenophagy to the review.

## PN Dossier Context

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

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
