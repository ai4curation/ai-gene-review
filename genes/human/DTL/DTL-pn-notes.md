# DTL PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NZJ0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DTL/DTL-ai-review.yaml](DTL-ai-review.yaml)
- AIGR review HTML: missing - genes/human/DTL/DTL-ai-review.html
- Gene notes: missing - genes/human/DTL/DTL-notes.md
- GOA TSV: present - [genes/human/DTL/DTL-goa.tsv](DTL-goa.tsv)
- UniProt record: present - [genes/human/DTL/DTL-uniprot.txt](DTL-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DTL.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DTL.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DTL.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DTL.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/DTL/DTL-deep-research-falcon.md](DTL-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: DTL (also known as CDT2, DCAF2, L2DTL, RAMP) is the substrate-recognition subunit (DCAF/substrate receptor) of the CRL4(CDT2) E3 ubiquitin ligase, a DDB1-CUL4 (CUL4A or CUL4B)-RBX1 cullin-RING ligase. DTL is a nuclear WD40-repeat beta-propeller protein that docks onto the DDB1 adaptor of the CUL4 scaffold via its WDXR/DDB1-binding motifs and confers substrate specificity to the complex. CRL4(CDT2) couples substrate ubiquitination to DNA-bound (chromatin-loaded) PCNA: substrates are recruited through a specialized PIP-degron (a PIP box bearing a basic "K+4" residue) that simultaneously engages PCNA on chromatin and the DTL propeller, so that ubiquitination occurs specifically at sites of DNA replication and repair. Through this PCNA-coupled mechanism CRL4(CDT2) drives the polyubiquitination and proteasomal degradation of the replication-licensing factor CDT1, the CDK inhibitor CDKN1A/p21, the histone H4K20 methyltransferase SET8/KMT5A, the helicase FBH1, and SDE2, and also targets CRY1 to influence the circadian clock. This activity prevents DNA re-replication, enforces the radiation-induced early G2/M checkpoint, and maintains genome stability. In undamaged proliferating cells CRL4(CDT2) additionally monoubiquitinates PCNA at Lys164 to promote translesion DNA synthesis. DTL itself is cell-cycle regulated: it peaks in G1/S, is degraded in mitosis by APC/C-Cdh1, and is controlled by SCF(FBXO11). DTL localizes to the nucleus/nucleoplasm and nuclear matrix, associates with chromatin, and is found at the centrosome during mitosis. DTL is frequently overexpressed in cancers such as hepatocellular carcinoma.
- Existing/core annotation action counts: ACCEPT: 41; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent on biology — DTL/CDT2 is the DCAF substrate receptor of CRL4(CDT2), recruiting PCNA-bound PIP-degron substrates (CDT1, p21, SET8, FBH1, SDE2). Divergence only in MF vocabulary: review uses GO:0030674 (protein-macromolecule adaptor activity, ACCEPTed from GOA IBA) for all three core functions; PN projects GO:1990756.
- **PN story / NEW pressure:** PN projects GO:1990756 as "more_specific_than_existing_goa." GOA already has GO:0030674 (enables, IBA) and GO:0004842 (contributes_to) — confirmed in goa.tsv; GO:1990756 is NOT in GOA. GO:1990756 (verified real; F-box/BTB receptor MF) is indeed more specific than the generic GO:0030674 for a CRL substrate receptor. Verdict: defensible ADD (more specific), but the reviewer deliberately preferred GO:0030674 as the receptor MF; this is a vocabulary judgment, not a substantive disagreement.
- **Evidence alignment:** PN row lists no references; the review is well-evidenced (PMID:16949367 Cdt1 destruction; 18794347 p21 recruitment; 17085480 G2/M checkpoint IMP; 20129063 PCNA K164 monoubiquitination). No conflict; PN under-cites.
- **Verdict:** Consistent; PN GO:1990756 is correctly categorized and a defensible more-specific add over the review's GO:0030674. **Recommended edits:** [YAML] optionally add/swap GO:1990756 as the DCAF substrate-receptor MF (more specific than GO:0030674), aligning with the PN projection.

## Full Consistency Review

- **UniProt:** Q9NZJ0 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other` ; **PN-node mapping:** group "Cul4A/Cul4B substrate receptor"=mapped, ok_for_propagation, GO:1990756 (substrate-adaptor MF); subtype/type=no_mapping; projected GO:1990756 goa_status=more_specific_than_existing_goa.
- **Consistency:** Consistent on biology — DTL/CDT2 is the DCAF substrate receptor of CRL4(CDT2), recruiting PCNA-bound PIP-degron substrates (CDT1, p21, SET8, FBH1, SDE2). Divergence only in MF vocabulary: review uses GO:0030674 (protein-macromolecule adaptor activity, ACCEPTed from GOA IBA) for all three core functions; PN projects GO:1990756.
- **PN story / NEW pressure:** PN projects GO:1990756 as "more_specific_than_existing_goa." GOA already has GO:0030674 (enables, IBA) and GO:0004842 (contributes_to) — confirmed in goa.tsv; GO:1990756 is NOT in GOA. GO:1990756 (verified real; F-box/BTB receptor MF) is indeed more specific than the generic GO:0030674 for a CRL substrate receptor. Verdict: defensible ADD (more specific), but the reviewer deliberately preferred GO:0030674 as the receptor MF; this is a vocabulary judgment, not a substantive disagreement.
- **Mapping strategy:** Correct category — DTL is a genuine DCAF substrate receptor, so GO:1990756 (receptor) is well placed (contrast DDB1, which is scaffold). Node status/scope appropriate; narrower than existing generic GOA.
- **Evidence alignment:** PN row lists no references; the review is well-evidenced (PMID:16949367 Cdt1 destruction; 18794347 p21 recruitment; 17085480 G2/M checkpoint IMP; 20129063 PCNA K164 monoubiquitination). No conflict; PN under-cites.
- **Verdict:** Consistent; PN GO:1990756 is correctly categorized and a defensible more-specific add over the review's GO:0030674. **Recommended edits:** [YAML] optionally add/swap GO:1990756 as the DCAF substrate-receptor MF (more specific than GO:0030674), aligning with the PN projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/DTL/DTL-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | WD40 | other
- UniProt: Q9NZJ0
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
