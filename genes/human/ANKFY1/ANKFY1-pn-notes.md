# ANKFY1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9P2R3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1366)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ANKFY1/ANKFY1-ai-review.yaml](ANKFY1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ANKFY1/ANKFY1-ai-review.html](ANKFY1-ai-review.html)
- Gene notes: present - [genes/human/ANKFY1/ANKFY1-notes.md](ANKFY1-notes.md)
- GOA TSV: present - [genes/human/ANKFY1/ANKFY1-goa.tsv](ANKFY1-goa.tsv)
- UniProt record: present - [genes/human/ANKFY1/ANKFY1-uniprot.txt](ANKFY1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ANKFY1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ANKFY1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ANKFY1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ANKFY1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ANKFY1/ANKFY1-deep-research-falcon.md](ANKFY1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ANKFY1 encodes Rabankyrin-5, a large ankyrin-repeat, BTB/POZ, and FYVE-domain protein that acts on PI3P- and Rab5-positive endosomal membranes. It binds activated Rab5-family GTPases and phosphatidylinositol phosphate lipids to regulate early endosome fusion, macropinocytosis, retromer-dependent endosome-to-Golgi and Golgi-to-lysosome trafficking, and receptor internalization. Recent work shows that ANKFY1 also recruits and stabilizes ATG2A on PI3P-rich endosomal membranes during autophagy, promoting ATG2A-mediated lipid transfer from endosomes to phagophores for autophagosome growth and completion.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 9; MODIFY: 4; NEW: 1; UNDECIDED: 2

## PN Consistency Summary

- **Consistency:** **CONTRADICTION (placement-level).** PN places ANKFY1 in UPS as a Cul3 substrate receptor (BTB/ankyrin domain architecture), but DR ↔ notes ↔ review YAML all curate ANKFY1 as a PI3P-/Rab5-binding endosomal effector (Rabankyrin-5) and ATG2A-bridging autophagy factor. GOA has NO ubiquitin-ligase/CUL3 terms (only GO:0031267 Rab5 binding, GO:1901981 PI3P binding). The UPS placement rests on domain signature (BTB-BACK/ankyrin), not function.
- **PN story / NEW pressure:** PN's sole projected term **GO:1990756 (verified real, new_to_goa): review explicitly REJECTS** — no validated CUL3 membership, substrate recognition, or adaptor activity for ANKFY1; the BTB region is present but not functionally ubiquitin-ligase. Over-reaches. Instead the review ADDS **GO:0000045 autophagosome assembly** (verified real; `action: NEW`, IMP, PMID:38622126 — ANKFY1 depletion impairs autophagosome growth, enhances ATG2A lipid transfer). The genuine proteostasis link is ALP (autophagosome formation), not UPS.
- **Evidence alignment:** PN cites PMID:15071497, 23912815 (titles only, generic). Review/notes anchor on PMID:15328530 (Rabankyrin-5/Rab5/PI3P), 22284051 (EHD1/retromer/M6PR), 24102721 (RhoD), and the key PMID:38622126 (ATG2A). No overlap with PN's cited PMIDs — divergent evidence base reflecting the placement conflict.
- **Verdict:** PN UPS/Cul3 placement and GO:1990756 projection over-reach; review correctly rejects and instead adds GO:0000045 (ALP). Domain-driven mis-placement.

## Full Consistency Review

- **UniProt:** Q9P2R3 (Rabankyrin-5) · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** 1 row, UPS. `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin`. **PN-node mapping:** group (Cul3 substrate receptor)=`mapped`→GO:1990756 ubiquitin-like ligase-substrate adaptor activity (new_to_goa); class (E3 ligases)=`context_only`→GO:0061630; subtype/type/branch=`no_mapping`.
- **Consistency:** **CONTRADICTION (placement-level).** PN places ANKFY1 in UPS as a Cul3 substrate receptor (BTB/ankyrin domain architecture), but DR ↔ notes ↔ review YAML all curate ANKFY1 as a PI3P-/Rab5-binding endosomal effector (Rabankyrin-5) and ATG2A-bridging autophagy factor. GOA has NO ubiquitin-ligase/CUL3 terms (only GO:0031267 Rab5 binding, GO:1901981 PI3P binding). The UPS placement rests on domain signature (BTB-BACK/ankyrin), not function.
- **PN story / NEW pressure:** PN's sole projected term **GO:1990756 (verified real, new_to_goa): review explicitly REJECTS** — no validated CUL3 membership, substrate recognition, or adaptor activity for ANKFY1; the BTB region is present but not functionally ubiquitin-ligase. Over-reaches. Instead the review ADDS **GO:0000045 autophagosome assembly** (verified real; `action: NEW`, IMP, PMID:38622126 — ANKFY1 depletion impairs autophagosome growth, enhances ATG2A lipid transfer). The genuine proteostasis link is ALP (autophagosome formation), not UPS.
- **Mapping strategy:** ANKFY1 should be EXCLUDED from the Cul3-substrate-receptor GO:1990756 projection (domain-only mis-bucketing, analogous to the broader/wrong-bucket precedents). Its proteostasis relevance belongs in the autophagy branch via ATG2A-mediated phagophore growth.
- **Evidence alignment:** PN cites PMID:15071497, 23912815 (titles only, generic). Review/notes anchor on PMID:15328530 (Rabankyrin-5/Rab5/PI3P), 22284051 (EHD1/retromer/M6PR), 24102721 (RhoD), and the key PMID:38622126 (ATG2A). No overlap with PN's cited PMIDs — divergent evidence base reflecting the placement conflict.
- **Verdict:** PN UPS/Cul3 placement and GO:1990756 projection over-reach; review correctly rejects and instead adds GO:0000045 (ALP). Domain-driven mis-placement.
- **Recommended edits:** none to ANKFY1-ai-review.yaml. [MAP] exclude ANKFY1 from the Cul3-substrate-receptor GO:1990756 projection (no CUL3/adaptor evidence; function is Rab5/PI3P endosomal + ATG2A autophagy). Consider re-homing ANKFY1's proteostasis placement to ALP.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ANKFY1/ANKFY1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul3 substrate receptor | BTB-BACK, variant | ankyrin
- UniProt: Q9P2R3
- In branches: UPS
- Signature domains: IPR000210, IPR049763
- Auxiliary domains: IPR002110
- PN references (titles):
    - 15071497 / rev
    - 23912815 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant|ankyrin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK, variant
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
