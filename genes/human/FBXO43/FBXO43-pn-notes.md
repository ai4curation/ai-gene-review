# FBXO43 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q4G163
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO43/FBXO43-ai-review.yaml](FBXO43-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO43/FBXO43-ai-review.html
- Gene notes: missing - genes/human/FBXO43/FBXO43-notes.md
- GOA TSV: present - [genes/human/FBXO43/FBXO43-goa.tsv](FBXO43-goa.tsv)
- UniProt record: present - [genes/human/FBXO43/FBXO43-uniprot.txt](FBXO43-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO43.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO43.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO43.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO43.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO43/FBXO43-deep-research-falcon.md](FBXO43-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO43 (Endogenous meiotic inhibitor 2, EMI2/ERP1) is a meiotic cell-cycle regulator and the closest paralog of FBXO5/EMI1. Despite containing an F-box, its established function is as a direct inhibitor of the anaphase-promoting complex/cyclosome (APC/C) ubiquitin ligase rather than as a canonical SCF substrate receptor. FBXO43 is the key component of cytostatic factor (CSF) activity that establishes and maintains the arrest of vertebrate oocytes at metaphase of the second meiotic division (MII) until fertilization, acting by binding and inhibiting the APC/C to stabilize cyclin B1 (CCNB1) and sustain CDK1 activity. Mechanistically, EMI2 docks onto the APC/C through a short C-terminal RL tail, and its C-terminal zinc-binding region (ZBR) both impairs association of the coactivator CDC20 with the APC/C core and inhibits APC/C catalytic activity (including UBE2C-dependent ubiquitin chain formation), so that inhibition reflects direct perturbation of APC/C rather than simple pseudosubstrate competition. Upon fertilization, a calcium signal triggers phosphorylation of FBXO43 (at residues including Ser76, Thr234 and Ser334 by kinases such as CaMKII and PLK1), generating a beta-TrCP-recognized phosphodegron that drives its ubiquitination and proteasomal degradation, relieving APC/C inhibition and allowing exit from MII and the metaphase-to-anaphase transition. FBXO43 binds directly to multiple APC/C subunits (ANAPC2, ANAPC4, CDC16, CDC23, ANAPC10, CDC26). It is expressed predominantly in the gonads (testis and oocyte), and loss-of-function variants cause human infertility: oocyte/embryo maturation arrest in females (OZEMA12) and spermatogenic failure/non-obstructive azoospermia with meiotic arrest in males (SPGF64).
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 5; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** **MAJOR PN-vs-review contradiction (the SPECIAL CASE).** Deep research + review correctly establish FBXO43/EMI2 as a non-canonical F-box that does NOT bind SKP1 (PMID:34595750) and is NOT an SCF substrate receptor — it is a direct APC/C INHIBITOR (gonad-restricted meiotic CSF). But the PN node files FBXO43 under "Cul1 substrate receptor" and projects GO:1990756 adaptor activity, which directly conflicts with the review (which MARK_AS_OVER_ANNOTATED on GO:0019005 and GO:0031146, and gives core MF = GO:1990948 ubiquitin ligase inhibitor activity). Review internally consistent and well-evidenced (PMID:34052850 OZEMA12, PMID:34595750 SPGF64, both VERIFIED).
- **PN story / NEW pressure:** Review adds NEW GO:1990948 "ubiquitin ligase inhibitor activity" (OLS-verified real; IMP from PMID:34595750) — the true core MF, absent from GOA. It also correctly REMOVEs the implausible ortholog-transfer IEA GO:1990090 "cellular response to NGF" (the flagged implausible IEA), and MARK_AS_OVER_ANNOTATED the mitotic-division IBA/IEA (paralog over-propagation from EMI1/FBXO5). Conclusion: PN over-reaches by projecting an adaptor MF onto an APC/C inhibitor; the defensible NEW term is GO:1990948, already in the review.
- **Evidence alignment:** PN cites only "15340381 / rev" (generic F-box). Review carries the disease/mechanism primaries (PMID:34052850, PMID:34595750) and Falcon EMI2 synthesis — strong divergence; PN's generic citation does not support the substrate-receptor placement.
- **Verdict:** Review correct; PN node mis-files FBXO43 and over-reaches with GO:1990756. **Recommended edits:** [MAP] exclude FBXO43/EMI2 from the GO:1990756 substrate-adaptor projection and flag as non-canonical F-box / APC/C inhibitor (core MF GO:1990948), mirroring FBXO5/EMI1.

## Full Consistency Review

- **UniProt:** Q4G163 (EMI2/ERP1) · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|ZBR-type ZnF` ; **PN-node mapping:** F-box subtype/type = no_mapping; group "Cul1 substrate receptor" = mapped, ok_for_propagation_to_go, GO:1990756; class = context_only/too_broad (GO:0061630).
- **Consistency:** **MAJOR PN-vs-review contradiction (the SPECIAL CASE).** Deep research + review correctly establish FBXO43/EMI2 as a non-canonical F-box that does NOT bind SKP1 (PMID:34595750) and is NOT an SCF substrate receptor — it is a direct APC/C INHIBITOR (gonad-restricted meiotic CSF). But the PN node files FBXO43 under "Cul1 substrate receptor" and projects GO:1990756 adaptor activity, which directly conflicts with the review (which MARK_AS_OVER_ANNOTATED on GO:0019005 and GO:0031146, and gives core MF = GO:1990948 ubiquitin ligase inhibitor activity). Review internally consistent and well-evidenced (PMID:34052850 OZEMA12, PMID:34595750 SPGF64, both VERIFIED).
- **PN story / NEW pressure:** Review adds NEW GO:1990948 "ubiquitin ligase inhibitor activity" (OLS-verified real; IMP from PMID:34595750) — the true core MF, absent from GOA. It also correctly REMOVEs the implausible ortholog-transfer IEA GO:1990090 "cellular response to NGF" (the flagged implausible IEA), and MARK_AS_OVER_ANNOTATED the mitotic-division IBA/IEA (paralog over-propagation from EMI1/FBXO5). Conclusion: PN over-reaches by projecting an adaptor MF onto an APC/C inhibitor; the defensible NEW term is GO:1990948, already in the review.
- **Mapping strategy:** **This gene SHOULD change the node treatment.** Per precedent (substrate-receptor MF rejected when the gene is not a receptor), GO:1990756 is wrong for FBXO43 — it is broader/incorrect, not narrower. FBXO43 should be excluded from the GO:1990756 projection / flagged as a non-canonical F-box (APC/C inhibitor), analogous to its paralog FBXO5/EMI1.
- **Evidence alignment:** PN cites only "15340381 / rev" (generic F-box). Review carries the disease/mechanism primaries (PMID:34052850, PMID:34595750) and Falcon EMI2 synthesis — strong divergence; PN's generic citation does not support the substrate-receptor placement.
- **Verdict:** Review correct; PN node mis-files FBXO43 and over-reaches with GO:1990756. **Recommended edits:** [MAP] exclude FBXO43/EMI2 from the GO:1990756 substrate-adaptor projection and flag as non-canonical F-box / APC/C inhibitor (core MF GO:1990948), mirroring FBXO5/EMI1.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO43/FBXO43-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | ZBR-type ZnF
- UniProt: Q4G163
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR044064
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|ZBR-type ZnF
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
