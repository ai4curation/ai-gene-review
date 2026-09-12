# FBXO5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKT4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO5/FBXO5-ai-review.yaml](FBXO5-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO5/FBXO5-ai-review.html
- Gene notes: missing - genes/human/FBXO5/FBXO5-notes.md
- GOA TSV: present - [genes/human/FBXO5/FBXO5-goa.tsv](FBXO5-goa.tsv)
- UniProt record: present - [genes/human/FBXO5/FBXO5-uniprot.txt](FBXO5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO5/FBXO5-deep-research-falcon.md](FBXO5-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO5 (Early mitotic inhibitor 1, EMI1) is a cell-cycle regulatory protein that, despite containing an F-box, functions principally as a direct inhibitor of the anaphase-promoting complex/cyclosome (APC/C), the multisubunit E3 ubiquitin ligase that drives mitotic and cell-cycle progression. EMI1 accumulates from late G1 through S and G2 phase under E2F transcriptional control and binds tightly to the APC/C and its coactivators FZR1/CDH1 and CDC20. It acts as a pseudosubstrate/multimodal inhibitor: a conserved C-terminal D-box, linker, and tail together with a structured zinc-binding region (ZBR) engage distinct sites on APC/C to block substrate access at the D-box coreceptor (FZR1-ANAPC10) and to suppress ubiquitin-chain elongation by the APC/C E2 enzymes UBE2C/UBCH10 and UBE2S. By restraining APC/C during interphase, EMI1 stabilizes APC/C substrates such as cyclin A (CCNA2) and geminin (GMNN), thereby coupling DNA replication with mitosis, preventing rereplication, and protecting against DNA-damage-induced senescence. EMI1 levels are sharply controlled: at the G1/S transition it switches from being a substrate of APC/C(CDH1) to its inhibitor, and at the onset of mitosis it is phosphorylated by CDK1/2 and PLK1 to generate a DSGxxS phosphodegron recognized by the SCF(beta-TrCP/BTRC) ubiquitin ligase, leading to its degradation and APC/C activation. In oocyte meiosis the EMI1/EMI2 family provides cytostatic-factor activity that arrests cells through APC/C inhibition. EMI1 levels are dosage-sensitive for genome stability: reduced EMI1 causes chromosome instability, micronucleation, and DNA damage and is associated with cellular transformation, while EMI1 abundance is also shaped by post-transcriptional control (METTL16-mediated m6A mRNA stabilization and PTBP1-dependent exon-3 splicing), and FBXO5 is frequently dysregulated in cancers. EMI1 localizes to the nucleus and cytoplasm in interphase and to the spindle in mitosis.
- Existing/core annotation action counts: ACCEPT: 28; KEEP_AS_NON_CORE: 35; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** CONTRADICTION (substantive, by design). The PN places EMI1 in the SCF substrate-receptor group and projects GO:1990756 adaptor activity. The review (correctly per the SPECIAL CASE) treats EMI1 as a **non-canonical F-box whose dominant function is APC/C INHIBITION, not productive SCF substrate reception**: core MF = GO:1990948 ubiquitin ligase inhibitor activity (verified real; ACCEPT, IDA PMID:15148369). Review explicitly demotes the ComplexPortal SCF-receptor NAS to non-core and MARK_AS_OVER_ANNOTATED for SCF-dependent catabolism / protein ubiquitination (EMI1 is a SCF^BTRC *substrate*, not a productive receptor). Falcon DR ↔ review agree; both diverge from the PN node framing.
- **PN story / NEW pressure:** The PN role (generic SCF receptor → GO:1990756) is NOT supported as core for this gene and is contradicted by the well-documented inhibitor biology. No new term needed: the accurate MFs (GO:1990948 inhibitor activity; GO:0010997 anaphase-promoting complex binding; GO:1904667/GO:0051444 negative regulation of ligase/transferase) are already in GOA and accepted. A single 2024 report frames SCF^EMI1/RAD51, but the review rightly does not let it overturn the inhibitor role. Conclude: PN adaptor projection over-reaches for FBXO5.
- **Evidence alignment:** PN reference only "15340381 / rev". Review uses gene-specific primary literature: PMID:15148369 (inhibitor activity, IDA), 23708605 (DisProt IDR inhibition), 15148369/15469984-class APC/C-binding, 17875940 (genome-stability IMP), plus Falcon DR. No overlap with PN; review evidence is far richer and on-point.
- **Verdict:** PN node placement is misleading for EMI1 — adaptor projection (GO:1990756) should NOT propagate; review correctly anchors on GO:1990948 inhibitor activity (in GOA). Over-reach on the PN side.

## Full Consistency Review

- **UniProt:** Q9UKT4 (FBXO5/EMI1) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|ZBR-type ZnF` ; **PN-node mapping:** group `Cul1 substrate receptor`=`mapped`/ok_for_propagation→GO:1990756; F-box/ZBR subtype+type=`no_mapping`; class=`context_only`/too_broad→GO:0061630.
- **Consistency:** CONTRADICTION (substantive, by design). The PN places EMI1 in the SCF substrate-receptor group and projects GO:1990756 adaptor activity. The review (correctly per the SPECIAL CASE) treats EMI1 as a **non-canonical F-box whose dominant function is APC/C INHIBITION, not productive SCF substrate reception**: core MF = GO:1990948 ubiquitin ligase inhibitor activity (verified real; ACCEPT, IDA PMID:15148369). Review explicitly demotes the ComplexPortal SCF-receptor NAS to non-core and MARK_AS_OVER_ANNOTATED for SCF-dependent catabolism / protein ubiquitination (EMI1 is a SCF^BTRC *substrate*, not a productive receptor). Falcon DR ↔ review agree; both diverge from the PN node framing.
- **PN story / NEW pressure:** The PN role (generic SCF receptor → GO:1990756) is NOT supported as core for this gene and is contradicted by the well-documented inhibitor biology. No new term needed: the accurate MFs (GO:1990948 inhibitor activity; GO:0010997 anaphase-promoting complex binding; GO:1904667/GO:0051444 negative regulation of ligase/transferase) are already in GOA and accepted. A single 2024 report frames SCF^EMI1/RAD51, but the review rightly does not let it overturn the inhibitor role. Conclude: PN adaptor projection over-reaches for FBXO5.
- **Mapping strategy:** This gene SHOULD change/qualify the node. Like FBXO2/FBXO6 (lectin) but more strongly, EMI1 is an exception to the Cul1-substrate-receptor → GO:1990756 default. Recommend marking FBXO5/EMI1 (and ZBR-type-ZnF F-box) so the GO:1990756 projection is suppressed or flagged "non-canonical / APC-C inhibitor" rather than propagated as a productive adaptor.
- **Evidence alignment:** PN reference only "15340381 / rev". Review uses gene-specific primary literature: PMID:15148369 (inhibitor activity, IDA), 23708605 (DisProt IDR inhibition), 15148369/15469984-class APC/C-binding, 17875940 (genome-stability IMP), plus Falcon DR. No overlap with PN; review evidence is far richer and on-point.
- **Verdict:** PN node placement is misleading for EMI1 — adaptor projection (GO:1990756) should NOT propagate; review correctly anchors on GO:1990948 inhibitor activity (in GOA). Over-reach on the PN side.
- **Recommended edits:** none to FBXO5-ai-review.yaml (review is correct). [MAP] Flag FBXO5/EMI1 as a non-canonical F-box (APC/C inhibitor) so GO:1990756 is NOT propagated to it; its core MF is GO:1990948 ubiquitin ligase inhibitor activity.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO5/FBXO5-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | ZBR-type ZnF
- UniProt: Q9UKT4
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
