# FBXW10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5XX13
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW10/FBXW10-ai-review.yaml](FBXW10-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW10/FBXW10-ai-review.html
- Gene notes: missing - genes/human/FBXW10/FBXW10-notes.md
- GOA TSV: present - [genes/human/FBXW10/FBXW10-goa.tsv](FBXW10-goa.tsv)
- UniProt record: present - [genes/human/FBXW10/FBXW10-uniprot.txt](FBXW10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW10/FBXW10-deep-research-falcon.md](FBXW10-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW10 (ubiquitin ligase-specificity factor) is a large (1052 aa) member of the F-box/WD40 (FBXW) family, containing an F-box motif and WD40 repeats together with coiled-coil regions. F-box proteins act as the interchangeable substrate-recognition subunits of SCF (SKP1-CUL1-F-box)-type cullin-RING E3 ubiquitin ligase complexes, in which the F-box motif docks onto SKP1/CUL1 and the WD40 propeller recruits substrates for ubiquitination by the RBX1-bound E2, committing them to proteasomal degradation; the F-box protein itself is the substrate adaptor and is not catalytic. Curated interactome resources classify FBXW10 as an E3 cullin-RING-ligase (CRL) adaptor with F-box plus WD40 repeats. FBXW10 is testis-enriched in expression. Functional data are limited: in a study of laminopathy-associated lamin A rod-domain mutants, FBXW10 transcript was induced several-fold in cells expressing these mutants, and ectopic FBXW10 expression depleted heterochromatin protein 1 isoforms HP1-alpha (CBX5) and HP1-beta (CBX1) but not HP1-gamma in a proteasome-dependent manner, implicating FBXW10 in turnover of these chromatin proteins under conditions of nuclear stress. FBXW10 has been reported mutated (missense, nonsense and frameshift) in T-cell prolymphocytic leukemia and was nominated as a candidate susceptibility gene (an in-frame WD-propeller deletion, p.Ile440del) in familial non-medullary thyroid cancer, and it shows tumor-type-specific expression changes in pan-cancer analyses. Its direct, physiological ubiquitination substrates and its assembly into a defined SCF complex have not been biochemically demonstrated; the HP1 isoforms are best regarded as candidate/affected substrates rather than validated direct targets.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 10

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research (falcon), review YAML, PN annotation and PN-node mapping all describe FBXW10 as a poorly characterized SCF F-box/WD40 substrate receptor (non-catalytic adaptor). The review's `proposed_new_terms` explicitly proposes GO:1990756, exactly matching the PN projection. No contradictions.
- **PN story / NEW pressure:** PN asserts the substrate-adaptor MF (GO:1990756) which is NOT in FBXW10's GOA (no MF adaptor/scaffold term present — confirmed in goa.tsv). GO:1990756 is real (OLS verified: "brings together a ubiquitin-like ligase and its substrate... F-box/BTB/POZ proteins") and is the canonical F-box receptor MF. Verdict: ADD GO:1990756 — already independently proposed in the review.
- **Evidence alignment:** Aligned. PN ref 15340381 = PMID:20498703 (lamin A mutants target HP1 via FBXW10), which is the review's sole experimental PMID and is marked relevance HIGH / correctness VERIFIED. Falcon adds interactome (Poirson 2017) and disease genetics; no divergence.
- **Verdict:** Consistent; PN GO:1990756 add is defensible and already mirrored in the review. No changes needed.

## Full Consistency Review

- **UniProt:** Q5XX13 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40` ; **PN-node mapping:** group=mapped, ok_for_propagation_to_go, GO:1990756 (substrate-adaptor MF); subtype/type=no_mapping; projected GO:1990756 goa_status=new_to_goa.
- **Consistency:** Fully consistent. Deep research (falcon), review YAML, PN annotation and PN-node mapping all describe FBXW10 as a poorly characterized SCF F-box/WD40 substrate receptor (non-catalytic adaptor). The review's `proposed_new_terms` explicitly proposes GO:1990756, exactly matching the PN projection. No contradictions.
- **PN story / NEW pressure:** PN asserts the substrate-adaptor MF (GO:1990756) which is NOT in FBXW10's GOA (no MF adaptor/scaffold term present — confirmed in goa.tsv). GO:1990756 is real (OLS verified: "brings together a ubiquitin-like ligase and its substrate... F-box/BTB/POZ proteins") and is the canonical F-box receptor MF. Verdict: ADD GO:1990756 — already independently proposed in the review.
- **Mapping strategy:** Correct. FBXW10 is a Cul1/SCF F-box WD40 receptor; catalysis is RBX1's. GO:1990756 (receptor/adaptor) is the right category, not scaffold (GO:0160072) and not catalytic (GO:0061630). Scope ok_for_propagation. The class-level GO:0061630 is correctly held as too_broad context_only.
- **Evidence alignment:** Aligned. PN ref 15340381 = PMID:20498703 (lamin A mutants target HP1 via FBXW10), which is the review's sole experimental PMID and is marked relevance HIGH / correctness VERIFIED. Falcon adds interactome (Poirson 2017) and disease genetics; no divergence.
- **Verdict:** Consistent; PN GO:1990756 add is defensible and already mirrored in the review. No changes needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW10/FBXW10-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: Q5XX13
- In branches: UPS
- Signature domains: IPR036047
- Auxiliary domains: IPR001680
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40
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
