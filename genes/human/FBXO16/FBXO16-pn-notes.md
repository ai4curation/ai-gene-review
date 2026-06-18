# FBXO16 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IX29
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO16/FBXO16-ai-review.yaml](FBXO16-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO16/FBXO16-ai-review.html
- Gene notes: missing - genes/human/FBXO16/FBXO16-notes.md
- GOA TSV: present - [genes/human/FBXO16/FBXO16-goa.tsv](FBXO16-goa.tsv)
- UniProt record: present - [genes/human/FBXO16/FBXO16-uniprot.txt](FBXO16-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO16.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO16.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO16/FBXO16-deep-research-falcon.md](FBXO16-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO16 (F-box only protein 16) is an F-box "other" (FBXO) family protein that serves as the substrate-recognition component of an SCF (SKP1-CUL1-F-box protein) / CRL1 Cullin-RING E3 ubiquitin-protein ligase complex. Through its F-box domain (residues 86-132) it docks onto SKP1 within the SCF scaffold, while its C-terminal region recruits specific substrate proteins for ubiquitination and subsequent proteasomal degradation; the catalytic transfer of ubiquitin is performed by the RING subunit RBX1 and an E2 enzyme, not by FBXO16 itself; consistently, its F-box domain is required for assembling a functional ligase complex while its C-terminal region mediates substrate recognition (e.g. binding the RRM3 domain of hnRNPL and the C-terminus being essential for beta-catenin binding). FBXO16 acts predominantly in the nucleus and drives K48-linked polyubiquitination of its targets. Reported substrates include the nuclear pool of beta-catenin/CTNNB1 (suppressing Wnt/TCF output such as c-Myc and Cyclin D1), the RNA-binding protein hnRNPL (whose degradation restrains MAPK/RAS/Wnt outputs), the autophagy-initiating kinase ULK1 (K48-linked polyubiquitination, suppressing autophagy), and the NF-kappa-B subunit RELA/p65 (as the substrate-recognition component of a PDLIM2-containing CRL1 complex that degrades nuclear p65). Through these targets FBXO16 has been implicated as a putative tumor suppressor (attenuating beta-catenin-driven epithelial-to-mesenchymal transition and ovarian/glioblastoma progression; in ovarian cancer it is down-regulated by MIR937 amplification, stabilizing ULK1) and as a negative regulator of NF-kappa-B inflammatory signaling. The protein is expressed in several tissues (heart, spleen, colon; tissue-enhanced in epididymis and pituitary) and exists as two alternatively spliced isoforms.
- Existing/core annotation action counts: ACCEPT: 2; KEEP_AS_NON_CORE: 1

## PN Consistency Summary

- **Consistency:** Consistent. DR ↔ YAML agree FBXO16 is a nuclear-acting CRL1/SCF substrate receptor driving K48-linked degradation of beta-catenin, hnRNPL, ULK1, RELA/p65. Review ACCEPTs SCF complex (GO:0019005) and SCF-dependent catabolism (GO:0031146); GO:1990756 is the core MF, matching PN.
- **PN story / NEW pressure:** PN asserts the adaptor MF. GO:1990756 (verified real) is NOT in GOA for FBXO16 — but, as with FBXO8, it appears only in `core_functions`, not as a NEW `existing_annotation`; FBXO16 has NO MF annotation in its existing_annotations at all (only protein binding IPI + two NAS CC/BP). So the adaptor MF is a defensible ADD that the review states but does not formally annotate. Validated substrates present (not substrate-less).
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:32296183 (binary interactome, LOW), 34445249 (SCF/ComplexPortal CPX-7926), plus Falcon substrate leads (Khan 2019, Ji 2021, Zhang 2024, Sugimoto-Ishige 2025). Expansion, no conflict.
- **Verdict:** Consistent; PN adaptor mapping appropriate and matches review core function.

## Full Consistency Review

- **UniProt:** Q8IX29 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other` ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent. DR ↔ YAML agree FBXO16 is a nuclear-acting CRL1/SCF substrate receptor driving K48-linked degradation of beta-catenin, hnRNPL, ULK1, RELA/p65. Review ACCEPTs SCF complex (GO:0019005) and SCF-dependent catabolism (GO:0031146); GO:1990756 is the core MF, matching PN.
- **PN story / NEW pressure:** PN asserts the adaptor MF. GO:1990756 (verified real) is NOT in GOA for FBXO16 — but, as with FBXO8, it appears only in `core_functions`, not as a NEW `existing_annotation`; FBXO16 has NO MF annotation in its existing_annotations at all (only protein binding IPI + two NAS CC/BP). So the adaptor MF is a defensible ADD that the review states but does not formally annotate. Validated substrates present (not substrate-less).
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 at right altitude. Class GO:0061630 too_broad. A nuclear-localization theme (DR) is not yet annotated but PN does not assert it either.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:32296183 (binary interactome, LOW), 34445249 (SCF/ComplexPortal CPX-7926), plus Falcon substrate leads (Khan 2019, Ji 2021, Zhang 2024, Sugimoto-Ishige 2025). Expansion, no conflict.
- **Verdict:** Consistent; PN adaptor mapping appropriate and matches review core function.
- **Recommended edits:** [YAML] consider adding GO:1990756 as a NEW MF `existing_annotation` (currently FBXO16 carries no MF annotation; the adaptor activity lives only in core_functions) — mirrors the explicit NEW done for FBXO15. [MAP] none.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO16/FBXO16-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | other
- UniProt: Q8IX29
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: (none)
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|other
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
