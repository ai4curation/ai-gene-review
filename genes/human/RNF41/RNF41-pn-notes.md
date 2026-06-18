# RNF41 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H4P4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF41/RNF41-ai-review.yaml](RNF41-ai-review.yaml)
- AIGR review HTML: missing - genes/human/RNF41/RNF41-ai-review.html
- Gene notes: present - [genes/human/RNF41/RNF41-notes.md](RNF41-notes.md)
- GOA TSV: present - [genes/human/RNF41/RNF41-goa.tsv](RNF41-goa.tsv)
- UniProt record: present - [genes/human/RNF41/RNF41-uniprot.txt](RNF41-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF41.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF41.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF41.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF41.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RNF41 (RING finger protein 41; also known as NRDP1, neuregulin receptor degradation protein-1, and FLRF) is a 317-residue RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27). It has an N-terminal RING-type zinc finger (catalytic residues Cys34/His36/Asp56) that recruits a ubiquitin-charged E2 conjugating enzyme, a degenerate SIAH-type zinc finger, and a C-terminal dimerization/substrate-binding domain that engages substrates and the deubiquitinase USP8. RNF41 directs ubiquitination and, for several targets, proteasomal degradation of a defined substrate set. Its best-characterized substrates are the neuregulin receptor tyrosine kinases ErbB3 and ErbB4 (but not EGFR or ErbB2): RNF41 binds the ErbB3 cytoplasmic tail in an activation-independent manner and mediates growth-factor-independent ubiquitination and ER-associated/proteasomal degradation, thereby setting steady-state ErbB3/ErbB4 levels and restraining ErbB2/ErbB3-driven proliferative signaling and tumor growth. RNF41 also ubiquitinates and degrades the giant inhibitor-of-apoptosis protein BIRC6/BRUCE/Apollon, thereby promoting apoptosis, and ubiquitinates the E3 ligase PRKN/Parkin, accelerating its degradation, lowering Parkin activity and increasing reactive oxygen species (linking RNF41 to oxidative stress and Parkinson disease biology and to RNF41-PRKN regulation of late mitophagy). In innate immunity RNF41 polyubiquitinates MYD88 (limiting MyD88-dependent pro-inflammatory cytokines) and promotes TRIF-dependent type I interferon production and TBK1/IRF3 activation, and it ubiquitinates the erythropoietin and interleukin-3 receptors to control hematopoietic progenitor differentiation. RNF41 itself is regulated by autoubiquitination-driven proteasomal turnover that is counteracted by the deubiquitinase USP8 and by sequestration into endoplasmic-reticulum tubules by the reticulon Rtn4A/Nogo-A. It localizes mainly to the cytosol and perinuclear region, with a regulated pool on the ER tubular network.
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 32; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent with a coverage gap. Deep research, review and PN agree RNF41 is a genuine catalytic RING E3 (Cys34/His36/Asp56; RING mutations abolish activity) degrading ErbB3/ErbB4, BRUCE/BIRC6 (→apoptosis) and Parkin/PRKN (→↑ROS). The PN row1 mitophagy story = "CLEC16A-RNF41-USP8 complex maintains mitochondrial function / late mitophagy; also ubiquitinates BIRC6 to upregulate autophagy" (tandfonline beta-cell paper). The review NOTES the RNF41-PRKN/CLEC16A late-mitophagy role in `description` and a suggested_question, but the cited beta-cell mitophagy paper is NOT in the review's references and there is NO mitophagy/autophagy BP annotation. So the PN's mitophagy assertion is mentioned but not evidenced or annotated in the review.
- **PN story / NEW pressure:** Row1 projects GO:0000423 mitophagy as new_to_goa (verified real; confirmed ABSENT from GOA — RNF41 GOA has ligase MF/polyUb/proteasomal-catabolism but no mitophagy/autophagy BP). This is a candidate **ADD** but rests on the CLEC16A-RNF41-USP8 complex / late-mitophagy mechanism whose primary paper the review did not assess (UniProt cites PMID:24949970, not cached). Verify before adding. Row2 GO:0061630 = already_in_goa_exact — keep catalytic ligase MF as core (KEY PATTERN; RNF41 is unambiguously a catalytic RING E3, review ACCEPTs).
- **Evidence alignment:** Divergent on the mitophagy arm. PN row1 ref (beta-cell ubiquitin-dependent mitophagy complex, tandfonline) is NOT in the review. Review's catalytic/substrate evidence (PMID:18541373 Parkin, PMID:14765125 BRUCE, PMID:11867753/27353365 ErbB3, PMID:15314180 USP8) is rich but covers the UPS/ligase side, not the mitophagy paper. PN row2 "19489725 / rev" is a family-review pointer.
- **Verdict:** Consistent on catalytic ligase core (in GOA); the mitophagy ADD is plausible but the PN's primary mitophagy reference is absent from the review — verify before treating GO:0000423 as settled.

## Full Consistency Review

- **UniProt:** Q9H4P4 (NRDP1/FLRF) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (very thorough; catalytic RING E3; ErbB3/ErbB4, BRUCE, Parkin substrates; mitophagy complex; 2 PN rows)
- **PN placement:** row1 `ALP|...|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway`; row2 `UPS|E3 ubiquitin and UBL ligases|RING|SIAH / SINA`. **PN-node mapping:** row1 Mitophagy type→mapped GO:0000423 mitophagy (PINK/PRKN subtype no_mapping); row2 RING group→mapped GO:0061630 ubiquitin protein ligase activity (class context_only/too_broad).
- **Consistency:** Mostly consistent with a coverage gap. Deep research, review and PN agree RNF41 is a genuine catalytic RING E3 (Cys34/His36/Asp56; RING mutations abolish activity) degrading ErbB3/ErbB4, BRUCE/BIRC6 (→apoptosis) and Parkin/PRKN (→↑ROS). The PN row1 mitophagy story = "CLEC16A-RNF41-USP8 complex maintains mitochondrial function / late mitophagy; also ubiquitinates BIRC6 to upregulate autophagy" (tandfonline beta-cell paper). The review NOTES the RNF41-PRKN/CLEC16A late-mitophagy role in `description` and a suggested_question, but the cited beta-cell mitophagy paper is NOT in the review's references and there is NO mitophagy/autophagy BP annotation. So the PN's mitophagy assertion is mentioned but not evidenced or annotated in the review.
- **PN story / NEW pressure:** Row1 projects GO:0000423 mitophagy as new_to_goa (verified real; confirmed ABSENT from GOA — RNF41 GOA has ligase MF/polyUb/proteasomal-catabolism but no mitophagy/autophagy BP). This is a candidate **ADD** but rests on the CLEC16A-RNF41-USP8 complex / late-mitophagy mechanism whose primary paper the review did not assess (UniProt cites PMID:24949970, not cached). Verify before adding. Row2 GO:0061630 = already_in_goa_exact — keep catalytic ligase MF as core (KEY PATTERN; RNF41 is unambiguously a catalytic RING E3, review ACCEPTs).
- **Mapping strategy:** Row2 catalytic-RING→GO:0061630 is correct (exact, in GOA, multiple IDA). Row1 mitophagy leaf→GO:0000423: defensible in principle (RNF41-PRKN-CLEC16A is a real mitophagy module) but the PINK/PRKN subtype is no_mapping and the propagation flows from the Mitophagy-type node; for RNF41 the role is regulatory/late-stage (autophagosome-lysosome fusion) rather than RNF41 being a cargo-marking receptor, so "Marking substrates for selective autophagy" placement is a slightly loose fit. Status `mapped` is acceptable if the late-mitophagy evidence is confirmed.
- **Evidence alignment:** Divergent on the mitophagy arm. PN row1 ref (beta-cell ubiquitin-dependent mitophagy complex, tandfonline) is NOT in the review. Review's catalytic/substrate evidence (PMID:18541373 Parkin, PMID:14765125 BRUCE, PMID:11867753/27353365 ErbB3, PMID:15314180 USP8) is rich but covers the UPS/ligase side, not the mitophagy paper. PN row2 "19489725 / rev" is a family-review pointer.
- **Verdict:** Consistent on catalytic ligase core (in GOA); the mitophagy ADD is plausible but the PN's primary mitophagy reference is absent from the review — verify before treating GO:0000423 as settled.
- **Recommended edits:** [REF/WB] obtain/assess the PN-cited CLEC16A-RNF41-USP8 beta-cell mitophagy paper (and UniProt's PMID:24949970 late-mitophagy citation) — both absent from the review; they are the basis for GO:0000423. [YAML] if verified, add GO:0000423 mitophagy (regulation-of-mitophagy may fit better given RNF41's late/fusion-stage role) — currently the mitophagy role is mentioned in `description` but unannotated and uncited.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/RNF41/RNF41-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Mitophagy | PINK/PRKN pathway
- UniProt: Q9H4P4
- In branches: ALP, UPS
- Notes: Important for mitophagy as part of CLEC16A-RNF41-USP8 complex. Also ubiquitinates BIRC6 to upregulate autophagy.
- PN references (titles):
    - Full article: A ubiquitin-dependent mitophagy complex maintains mitochondrial function and insulin secretion in beta cells (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: The PN marking category for mitophagy captures upstream cargo-marking steps that commit mitochondrial substrates to the mitophagy pathway. That supports propagation to mitophagy.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | SIAH / SINA
- UniProt: Q9H4P4
- In branches: ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR013010
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|SIAH / SINA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
