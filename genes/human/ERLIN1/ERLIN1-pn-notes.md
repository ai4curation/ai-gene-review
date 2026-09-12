# ERLIN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75477
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ERLIN1/ERLIN1-ai-review.yaml](ERLIN1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/ERLIN1/ERLIN1-ai-review.html
- Gene notes: present - [genes/human/ERLIN1/ERLIN1-notes.md](ERLIN1-notes.md)
- GOA TSV: present - [genes/human/ERLIN1/ERLIN1-goa.tsv](ERLIN1-goa.tsv)
- UniProt record: present - [genes/human/ERLIN1/ERLIN1-uniprot.txt](ERLIN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ERLIN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ERLIN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERLIN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERLIN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ERLIN1/ERLIN1-deep-research-falcon.md](ERLIN1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ERLIN1 (SPFH1, ER lipid raft-associated protein 1) is a single-pass type II endoplasmic reticulum (ER) membrane protein with a lumenal SPFH/prohibitin (band 7) domain, belonging to the band 7/mec-2 (stomatin-prohibitin-flotillin) family. It associates with lipid-raft-like domains of the ER membrane and functions as a scaffold rather than an enzyme. ERLIN1 forms a large ring-shaped heteromeric complex with its homolog ERLIN2 (SPFH2); the ERLIN1/ERLIN2 complex binds inositol 1,4,5-trisphosphate receptor (IP3R) tetramers and, together with the ER ubiquitin ligase RNF170, mediates the ER-associated degradation (ERAD) of activated IP3Rs, thereby controlling calcium signaling. The erlins are cholesterol-binding proteins that restrict SREBP activation: they associate with the SCAP-SREBP-Insig machinery to promote its ER retention and thus negatively regulate cholesterol and fatty acid biosynthesis, contributing to cellular cholesterol homeostasis. ERLIN1 also interacts with the ER ubiquitin ligases AMFR/gp78 and SYVN1/HRD1, linking it to sterol-accelerated ERAD. Loss-of-function variants in ERLIN1 cause autosomal recessive hereditary spastic paraplegia (SPG62).
- Existing/core annotation action counts: ACCEPT: 28; KEEP_AS_NON_CORE: 11

## PN Consistency Summary

- **Consistency:** Strong. Deep research (Veronese 2024 scaffold/TMUB1-RNF170; Cogan 2024 SPG62; Manganelli 2021 rafts/MAM) ↔ review YAML (ERAD of IP3R, cholesterol binding, SREBP restriction, ER-membrane raft, E3-ligase binding) ↔ PN annotation (BAND 7 noncatalytic ERLIN/RNF170 complex; ERAD) all agree. No contradictions. ERLIN dossier identical to ERLIN2 (shared complex).
- **PN story / NEW pressure:** PN asserts ERAD + non-catalytic E3-complex membership. Both already captured: GO:0036503 (IDA PMID:19240031, multiple ECs) and GO:0031625 ubiquitin protein ligase binding (IEA) are present. The 2024 scaffold/cholesterol-esterification/secretory-pathway role (Veronese, PMID:38782601) is NOT in GOA but is cited in references. No new term is forced; the most defensible additions would be MF GO:0160072 "ubiquitin ligase complex scaffold activity" (verified real) capturing the non-catalytic adaptor role. Verdict: largely already captured; scaffold-activity term is an optional ADD.
- **Evidence alignment:** PN cites only opaque workbook IDs (1610068, 41481136 — not PMIDs of the key ERLIN papers). Review/notes anchor to PMID:19240031, 24217618, 21343306, 38782601 + ComplexPortal CPX-7121. Divergence is presentational, not substantive.
- **Verdict:** Consistent and high-quality; PN story already captured by GOA/review. GO:0000151 projection mildly over-reaches (non-catalytic scaffold); prefer GO:0000835 / GO:0160072.

## Full Consistency Review

- **UniProt:** O75477 (ERLN1_HUMAN, SPFH1) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (all annotations actioned; no PENDING).
- **PN placement:** `ER proteostasis|Organelle-specific protein degradation|ER associated degradation|ER handling of ERAD substrates` and `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|RNF170 / ERLIN complex|noncatalytic / BAND 7` ; **PN-node mapping:** [group ERAD] mapped/exact GO:0036503; [type ER-handling] mapped/ok_for_propagation GO:0036503; [group idiosyncratic RING complex] mapped/ok_for_propagation GO:0000151 ubiquitin ligase complex; subtype/type/branch no_mapping; UPS class context_only/too_broad GO:0061630.
- **Consistency:** Strong. Deep research (Veronese 2024 scaffold/TMUB1-RNF170; Cogan 2024 SPG62; Manganelli 2021 rafts/MAM) ↔ review YAML (ERAD of IP3R, cholesterol binding, SREBP restriction, ER-membrane raft, E3-ligase binding) ↔ PN annotation (BAND 7 noncatalytic ERLIN/RNF170 complex; ERAD) all agree. No contradictions. ERLIN dossier identical to ERLIN2 (shared complex).
- **PN story / NEW pressure:** PN asserts ERAD + non-catalytic E3-complex membership. Both already captured: GO:0036503 (IDA PMID:19240031, multiple ECs) and GO:0031625 ubiquitin protein ligase binding (IEA) are present. The 2024 scaffold/cholesterol-esterification/secretory-pathway role (Veronese, PMID:38782601) is NOT in GOA but is cited in references. No new term is forced; the most defensible additions would be MF GO:0160072 "ubiquitin ligase complex scaffold activity" (verified real) capturing the non-catalytic adaptor role. Verdict: largely already captured; scaffold-activity term is an optional ADD.
- **Mapping strategy:** ERAD mapping (GO:0036503) is correct and already-in-GOA-exact. The GO:0000151 projection over-reaches slightly: the ERLIN1/2 complex (CPX-7121) is a non-catalytic BAND 7 scaffold, whereas GO:0000151 is a *catalytic* ubiquitin-ligase complex. GO:0000835 "ER ubiquitin ligase complex" (verified real) is the more accurate, still-broader-than-GOA target if a complex CC is projected.
- **Evidence alignment:** PN cites only opaque workbook IDs (1610068, 41481136 — not PMIDs of the key ERLIN papers). Review/notes anchor to PMID:19240031, 24217618, 21343306, 38782601 + ComplexPortal CPX-7121. Divergence is presentational, not substantive.
- **Verdict:** Consistent and high-quality; PN story already captured by GOA/review. GO:0000151 projection mildly over-reaches (non-catalytic scaffold); prefer GO:0000835 / GO:0160072.

**Recommended edits:** [MAP] Replace/qualify the GO:0000151 group projection with GO:0000835 "ER ubiquitin ligase complex" (CC) for the ERLIN/RNF170 assembly, noting ERLINs are non-catalytic BAND 7 subunits. [YAML, optional] Consider adding MF GO:0160072 "ubiquitin ligase complex scaffold activity" to core_functions for the adaptor role.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/ERLIN1/ERLIN1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | ER handling of ERAD substrates
- UniProt: O75477
- In branches: ER, UPS
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|ER handling of ERAD substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type captures ER-lumenal and membrane-local ERAD handling steps prior to retrotranslocation. These steps are mechanistic parts of the broader ERAD pathway, so propagation to ERAD pathway is appropriate.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic RING complex | RNF170 / ERLIN complex | noncatalytic / BAND 7
- UniProt: O75477
- In branches: ER, UPS
- Signature domains: (none)
- Auxiliary domains: IPR001107
- PN references (titles):
    - 1610068
    - 41481136
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|RNF170 / ERLIN complex|noncatalytic / BAND 7
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|RNF170 / ERLIN complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|ER handling of ERAD substrates
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
