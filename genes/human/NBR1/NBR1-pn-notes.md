# NBR1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q14596
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NBR1/NBR1-ai-review.yaml](NBR1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/NBR1/NBR1-ai-review.html
- Gene notes: present - [genes/human/NBR1/NBR1-notes.md](NBR1-notes.md)
- GOA TSV: present - [genes/human/NBR1/NBR1-goa.tsv](NBR1-goa.tsv)
- UniProt record: present - [genes/human/NBR1/NBR1-uniprot.txt](NBR1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NBR1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NBR1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NBR1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NBR1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/NBR1/NBR1-deep-research-falcon.md](NBR1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: NBR1 (Next to BRCA1 gene 1 protein) is a multidomain ubiquitin-binding selective autophagy receptor (cargo receptor) that, together with and parallel to its partner SQSTM1/p62, bridges ubiquitinated cargo to the ATG8/LC3 family on the forming autophagosome. Its domain architecture comprises an N-terminal PB1 domain that mediates self-oligomerization and heterodimerization with SQSTM1/p62, a ZZ-type zinc finger, two ATG8/LC3-interacting (LIR) regions that bind MAP1LC3A/B/C and GABARAP/GABARAPL1/GABARAPL2, and a C-terminal ubiquitin-associated (UBA) domain that binds K48- and K63-linked polyubiquitin. By simultaneously engaging polyubiquitinated substrates through its UBA domain and lipidated ATG8 proteins through its LIR motifs, NBR1 delivers ubiquitinated proteins to autophagosomes and also nucleates ubiquitin-positive condensates, promoting the formation of protein aggregates that are then cleared by macroautophagy (aggrephagy). NBR1 is predominantly cytoplasmic/cytosolic and is found at the phagophore assembly site and within autophagosomes, is delivered to and degraded in lysosomes, and additionally localizes to peroxisomal membranes (where it acts with p62 as a receptor for ubiquitinated PEX5 during pexophagy), to late endosomes, and, in striated muscle, to the sarcomeric M line in association with titin. Beyond bulk and aggregate clearance, NBR1 mediates selective autophagic degradation of specific innate-immune signaling factors, targeting ubiquitinated IRF3 and MAVS to autophagosomes and thereby negatively regulating type I interferon production; this pathway is exploited by influenza A virus, whose PB1 protein hijacks NBR1 to degrade MAVS. NBR1 also clears the senescence-associated factor SRBD1 and acts as a PB1-domain signaling scaffold in additional contexts. Its aggregation-promoting activity is modulated by GSK3-mediated phosphorylation at Thr-586. Through orthology, NBR1 is also implicated in p38/MAPK scaffolding and in the negative regulation of osteoblast differentiation and bone mineralization.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 38; NEW: 3; REMOVE: 1; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Highly consistent. Deep research (Rasmussen 2022 JCB; Vargas 2023 NRMCB) confirms archetypal SLR — UBA polyUb binding, LIR, AH+UBA peroxisome targeting, p62-body recruitment. Review and PN both center the cargo-adaptor/receptor MF. Notable nuance both capture: NBR1/p62 can be dispensable for aggrephagy in some cell types (Trapannone 2023) — receptor redundancy, not a contradiction. Review REMOVEs GO:0005758 mito intermembrane space (no support; only colocalizes with mitochondria during mitophagy) — well-justified.
- **PN story / NEW pressure:** Review proactively adds the same receptor MF the PN elevates: GO:0160247 autophagy cargo adaptor activity as **NEW** (action: NEW), plus GO:0035973 aggrephagy NEW and GO:0032480 negative regulation of type I IFN production NEW. Review also proposes a child term `pexophagy receptor activity` under GO:0160247. So PN's GO:0000425 pexophagy (process) is captured by review only at the MF/locational level, not as the BP term GO:0000425 — a minor gap (review has peroxisomal-membrane locations + proposed pexophagy-receptor MF but no GO:0000425 BP annotation).
- **Evidence alignment:** Strong ALP-branch overlap (Kirkin 2009 "A Role for NBR1...", TRAF6/midbody, CEP55, peroxisome receptor). Review adds Rasmussen 2022 reconstitution not in PN refs.
- **Verdict:** CONSISTENT and convergent — review already adds GO:0160247 NEW. Minor: consider adding GO:0000425 pexophagy BP to match PN projection. **Recommended edits:** consider [YAML] add existing/new GO:0000425 pexophagy (involved_in) to NBR1 review to mirror PN projection and SQSTM1 co-receptor evidence.

## Full Consistency Review

- **UniProt:** Q14596 · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (~1021 lines)
- **PN placement:** ALP `Autophagy substrate selection|Selective autophagy receptor|{Pexophagy,Aggrephagy,Midbody autophagy}` + UPS `Ubiquitin and UBL binding|trafficking|selective autophagy|UBA` ; **PN-node mapping:** Pexophagy→GO:0000425, Aggrephagy→GO:0035973, Midbody→GO:0160247 cargo adaptor; ancestors no_mapping/context_only.
- **Consistency:** Highly consistent. Deep research (Rasmussen 2022 JCB; Vargas 2023 NRMCB) confirms archetypal SLR — UBA polyUb binding, LIR, AH+UBA peroxisome targeting, p62-body recruitment. Review and PN both center the cargo-adaptor/receptor MF. Notable nuance both capture: NBR1/p62 can be dispensable for aggrephagy in some cell types (Trapannone 2023) — receptor redundancy, not a contradiction. Review REMOVEs GO:0005758 mito intermembrane space (no support; only colocalizes with mitochondria during mitophagy) — well-justified.
- **PN story / NEW pressure:** Review proactively adds the same receptor MF the PN elevates: GO:0160247 autophagy cargo adaptor activity as **NEW** (action: NEW), plus GO:0035973 aggrephagy NEW and GO:0032480 negative regulation of type I IFN production NEW. Review also proposes a child term `pexophagy receptor activity` under GO:0160247. So PN's GO:0000425 pexophagy (process) is captured by review only at the MF/locational level, not as the BP term GO:0000425 — a minor gap (review has peroxisomal-membrane locations + proposed pexophagy-receptor MF but no GO:0000425 BP annotation).
- **Mapping strategy:** Mappings sound. KEY PATTERN fully realized: review independently elevated GO:0160247 over bare protein binding (~12 IPI kept non-core). PN GO:0160247 (more_specific_than_existing_goa) matches the review's NEW exactly.
- **Evidence alignment:** Strong ALP-branch overlap (Kirkin 2009 "A Role for NBR1...", TRAF6/midbody, CEP55, peroxisome receptor). Review adds Rasmussen 2022 reconstitution not in PN refs.
- **Verdict:** CONSISTENT and convergent — review already adds GO:0160247 NEW. Minor: consider adding GO:0000425 pexophagy BP to match PN projection. **Recommended edits:** consider [YAML] add existing/new GO:0000425 pexophagy (involved_in) to NBR1 review to mirror PN projection and SQSTM1 co-receptor evidence.

## PN Dossier Context

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

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
