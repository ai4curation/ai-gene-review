# GLMN PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92990
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GLMN/GLMN-ai-review.yaml](GLMN-ai-review.yaml)
- AIGR review HTML: missing - genes/human/GLMN/GLMN-ai-review.html
- Gene notes: missing - genes/human/GLMN/GLMN-notes.md
- GOA TSV: present - [genes/human/GLMN/GLMN-goa.tsv](GLMN-goa.tsv)
- UniProt record: present - [genes/human/GLMN/GLMN-uniprot.txt](GLMN-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GLMN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GLMN.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GLMN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GLMN.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/GLMN/GLMN-deep-research-falcon.md](GLMN-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: Glomulin (GLMN; also known as FAP48/FAP68, FKBP-associated protein) is a ~68 kDa, predominantly alpha-helical cytoplasmic protein (with a HEAT-repeat-like architecture) that functions as a regulatory component of cullin-RING ubiquitin ligase (CRL/SCF) complexes. It binds directly to the RING domain of RBX1 (ROC1) through its C-terminal half and masks the surface that RBX1 uses to recruit the E2 ubiquitin-conjugating enzyme CDC34, thereby inhibiting RBX1-dependent E3 ubiquitin ligase activity and blocking RBX1-mediated neddylation of CUL1. By sequestering RBX1, glomulin stabilizes assembled SCF/CRL components and controls the auto-ubiquitination and turnover of the F-box substrate receptor FBXW7, thereby influencing the abundance of FBXW7 substrates such as Cyclin E and c-Myc. Glomulin has been found in CRL/SCF assemblies containing RBX1 with CUL1, CUL2, CUL3, CUL4A, and in a CUL7-RBX1-SKP1-FBXW8 complex. Loss-of-function mutations in GLMN cause glomuvenous malformations, cutaneous venous lesions with abnormal smooth-muscle-like glomus cells, reflecting a requirement for glomulin in normal vascular development. An alternatively spliced shorter isoform (isoform 2, FAP48) was originally characterized as a ligand of the immunophilins FKBP12 (FKBP1A) and FKBP52 (FKBP4), and glomulin/FAP68 was also reported to bind the inactive hepatocyte growth factor receptor (MET) and modulate downstream p70 S6 kinase signaling; these immunophilin- and receptor-associated activities predate the discovery of the CRL-regulatory role and are mechanistically distinct from it. In innate immunity, glomulin also binds the RING domains of the cellular inhibitor of apoptosis proteins cIAP1 and cIAP2, inhibits their self-ubiquitination, and acts as a negative regulator of cIAP-mediated inflammasome activation and macrophage pyroptosis; the Shigella effector IpaH7.8 ubiquitinates glomulin to drive its degradation and enhance inflammation. Structurally, glomulin binds RBX1 with high affinity (Kd in the nanomolar range) through a region in its C-terminal half (approximately residues 300-594) that occludes the RBX1 surface used to recruit the E2 enzyme CDC34.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 16; UNDECIDED: 2

## PN Consistency Summary

- **Consistency:** Strong agreement across deep research (falcon, HIGH), review YAML, and dossier. Glomulin is a non-catalytic high-affinity RBX1-binding inhibitor (Kd ~38.6 nM, residues ~300-594) that masks the CDC34/E2 surface and inhibits CRL/SCF E3 activity, controlling FBXW7 turnover (Tron/Tron 2012 PMID:22405651; Duda 2012). Directionality (inhibitor) is consistent everywhere. All 33 GOA rows reviewed. No catalytic-ligase term assigned (correct).
- **PN story / NEW pressure:** The core inhibitory function is already well captured in GOA — GO:0055105 ubiquitin-protein transferase inhibitor activity (IBA+IGI, ACCEPT), GO:0031625 ubiquitin protein ligase binding, and CRL complex memberships. The review surfaces a genuine GO gap: the cIAP1/cIAP2-inflammasome axis (Suzuki 2018), proposed as a new term *without* an invented ID (correct). GO:0141086 negative regulation of inflammasome-mediated signaling pathway exists (verified real) and is a reasonable existing anchor for that proposed term.
- **Evidence alignment:** Convergent on the keystone paper: PN cites PMID:22405651, which is also the foundational, HIGH-relevance reference driving the review's core MF/BP/complex annotations. Review adds the older FAP48/FAP68 immunophilin and MET literature (8955134, 11164950, 11571281, 12604780, 11845407) as non-core, plus interactome PMIDs — all marked secondary; no conflict with the PN story.
- **Verdict:** Fully consistent; PN inhibitor mapping (GO:1904667) is well-aligned with the review (GO:0055105) — no over-reach, no missing-NEW pressure on the core function. **Recommended edits:** [YAML] optional — anchor the proposed "negative regulation of cIAP-mediated inflammasome activation" term to the now-existing GO:0141086 (verify scope) as the closest existing parent/match. No mapping change required.

## Full Consistency Review

- **UniProt:** Q92990 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|CRL regulator|CRL inhibitor` ; **PN-node mapping:** type mapped, scope=ok_for_propagation_to_go, GO:1904667 negative regulation of ubiquitin protein ligase activity (group/class context_only; branch no_mapping)
- **Consistency:** Strong agreement across deep research (falcon, HIGH), review YAML, and dossier. Glomulin is a non-catalytic high-affinity RBX1-binding inhibitor (Kd ~38.6 nM, residues ~300-594) that masks the CDC34/E2 surface and inhibits CRL/SCF E3 activity, controlling FBXW7 turnover (Tron/Tron 2012 PMID:22405651; Duda 2012). Directionality (inhibitor) is consistent everywhere. All 33 GOA rows reviewed. No catalytic-ligase term assigned (correct).
- **PN story / NEW pressure:** The core inhibitory function is already well captured in GOA — GO:0055105 ubiquitin-protein transferase inhibitor activity (IBA+IGI, ACCEPT), GO:0031625 ubiquitin protein ligase binding, and CRL complex memberships. The review surfaces a genuine GO gap: the cIAP1/cIAP2-inflammasome axis (Suzuki 2018), proposed as a new term *without* an invented ID (correct). GO:0141086 negative regulation of inflammasome-mediated signaling pathway exists (verified real) and is a reasonable existing anchor for that proposed term.
- **Mapping strategy:** Sound. PN GO:1904667 (BP, negative regulation of ubiquitin protein ligase activity — verified) is the regulation-side counterpart of the review's MF GO:0055105; both are correct and complementary in directionality. Not over-broad like the TOMM20/HSPA8/RAB7A precedents — it is specifically the negative/inhibitor sense, matching the "CRL inhibitor" type.
- **Evidence alignment:** Convergent on the keystone paper: PN cites PMID:22405651, which is also the foundational, HIGH-relevance reference driving the review's core MF/BP/complex annotations. Review adds the older FAP48/FAP68 immunophilin and MET literature (8955134, 11164950, 11571281, 12604780, 11845407) as non-core, plus interactome PMIDs — all marked secondary; no conflict with the PN story.
- **Verdict:** Fully consistent; PN inhibitor mapping (GO:1904667) is well-aligned with the review (GO:0055105) — no over-reach, no missing-NEW pressure on the core function. **Recommended edits:** [YAML] optional — anchor the proposed "negative regulation of cIAP-mediated inflammasome activation" term to the now-existing GO:0141086 (verify scope) as the closest existing parent/match. No mapping change required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/GLMN/GLMN-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | CRL regulator | CRL inhibitor
- UniProt: Q92990
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: (none)
- PN references (titles):
    - 22748924
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|CRL inhibitor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904667 negative regulation of ubiquitin protein ligase activity]
        rationale: This PN type captures cullin-RING ligase inhibitors. The matching GO process target is negative regulation of ubiquitin protein ligase activity.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator
        status=context_only scope=too_broad_to_propagate GO=[GO:1904666 regulation of ubiquitin protein ligase activity]
        rationale: This PN group records regulation of cullin-RING ligase systems, but the members include inhibitors, exchange factors, and modulators with different directionality. It is context only.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1904667 negative regulation of ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|CRL regulator|CRL inhibitor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
