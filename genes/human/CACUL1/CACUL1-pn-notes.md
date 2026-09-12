# CACUL1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86Y37
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CACUL1/CACUL1-ai-review.yaml](CACUL1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CACUL1/CACUL1-ai-review.html](CACUL1-ai-review.html)
- Gene notes: present - [genes/human/CACUL1/CACUL1-notes.md](CACUL1-notes.md)
- GOA TSV: present - [genes/human/CACUL1/CACUL1-goa.tsv](CACUL1-goa.tsv)
- UniProt record: present - [genes/human/CACUL1/CACUL1-uniprot.txt](CACUL1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CACUL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CACUL1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CACUL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CACUL1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CACUL1 (CDK2-associated and cullin domain-containing protein 1; also known as CAC1 / C10orf46) is a poorly characterized 369-amino-acid human protein containing a single cullin-repeat-like domain with disordered N- and C-terminal regions. Despite its name and cullin-fold homology, it is much shorter than canonical cullins (~750-900 aa) and there is no experimental evidence that it nucleates a functional cullin-RING ubiquitin ligase or carries a neddylation/RBX module. The best-supported activity, from a single study, is physical association with the cyclin-dependent kinase CDK2 and promotion of CDK2 kinase activity, consistent with a role in G1/S cell-cycle progression and proliferation; the protein is highly expressed in cancer tissues and cell lines, and its abundance varies across the cell cycle. A second study reported CACUL1 as a nuclear-receptor (estrogen receptor alpha) co-regulator that, in association with the histone demethylase LSD1/KDM1A, can repress ERalpha-dependent transcription. CACUL1 has also been recovered as a yeast two-hybrid interactor of ARMC5. Overall, CACUL1 is a lightly characterized cell-cycle-associated protein whose detailed molecular mechanism remains undefined.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 1

## PN Consistency Summary

- **Consistency:** CONTRADICTION flagged. Deep-research notes and the review explicitly argue CACUL1 is NOT a functional cullin-RING scaffold: it is a 369-aa protein with only a cullin-repeat-LIKE fold, far shorter than canonical cullins (~750-900 aa), lacking any RBX/neddylation module, with no evidence it nucleates a CRL. The review MARK_AS_OVER_ANNOTATED the two IEA cullin-domain-transfer terms (GO:0006511, GO:0031625) precisely on these grounds. Its best-supported function is CDK2 binding/activation (PMID:19829063) plus ERalpha co-repression (PMID:23178685). The PN node label itself hedges ("degenerate, possible CUL3 inhibitor"). The PN group mapping to GO:0160072 scaffold activity therefore directly conflicts with the review's conclusion.
- **PN story / NEW pressure:** Over-reaches. PN's projected GO:0160072 (verified real via OLS) asserts a ubiquitin-ligase-scaffold MF that the review rejects as a domain-homology over-annotation. There is no experimental support for scaffold/CRL activity. Do NOT add — this is an over-reach analogous to (worse than) the rejected broader-term precedents. The gene's defensible MF is GO:0019901 protein kinase binding (CDK2), already accepted as core in the review.
- **Evidence alignment:** PN cites 26238671 (a CUL3-related paper, basis for the "possible CUL3 inhibitor" hedge). Review's evidence (PMID:19829063 CDK2, 23178685 ERalpha, 28169274 ARMC5 Y2H) does not overlap; PN evidence is not in the review and supports a speculative CUL3-regulator role not adopted by the review.
- **Verdict:** Inconsistent — PN over-reaches. GO:0160072 scaffold MF should not propagate to CACUL1 (no scaffold evidence; review treats cullin-fold terms as over-annotation).

## Full Consistency Review

- **UniProt:** Q86Y37 (CAC1, C10orf46) · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cullin|degenerate, possible CUL3 inhibitor` ; **PN-node mapping:** type node `degenerate, possible CUL3 inhibitor` no_mapping; group node `Cullin` mapped → GO:0160072 ubiquitin ligase complex scaffold activity (ok_for_propagation, new_to_goa); class context_only (GO:0061630, too_broad).
- **Consistency:** CONTRADICTION flagged. Deep-research notes and the review explicitly argue CACUL1 is NOT a functional cullin-RING scaffold: it is a 369-aa protein with only a cullin-repeat-LIKE fold, far shorter than canonical cullins (~750-900 aa), lacking any RBX/neddylation module, with no evidence it nucleates a CRL. The review MARK_AS_OVER_ANNOTATED the two IEA cullin-domain-transfer terms (GO:0006511, GO:0031625) precisely on these grounds. Its best-supported function is CDK2 binding/activation (PMID:19829063) plus ERalpha co-repression (PMID:23178685). The PN node label itself hedges ("degenerate, possible CUL3 inhibitor"). The PN group mapping to GO:0160072 scaffold activity therefore directly conflicts with the review's conclusion.
- **PN story / NEW pressure:** Over-reaches. PN's projected GO:0160072 (verified real via OLS) asserts a ubiquitin-ligase-scaffold MF that the review rejects as a domain-homology over-annotation. There is no experimental support for scaffold/CRL activity. Do NOT add — this is an over-reach analogous to (worse than) the rejected broader-term precedents. The gene's defensible MF is GO:0019901 protein kinase binding (CDK2), already accepted as core in the review.
- **Mapping strategy:** This gene argues AGAINST propagating the Cullin-group GO:0160072 mapping to CACUL1. The type node (`degenerate, possible CUL3 inhibitor`) is correctly no_mapping, but the group→GO:0160072 projection should be suppressed/excepted for CACUL1 because it is a degenerate non-scaffold member. The group mapping may be fine for bona fide cullins, but CACUL1 should be flagged as a member that does not inherit it.
- **Evidence alignment:** PN cites 26238671 (a CUL3-related paper, basis for the "possible CUL3 inhibitor" hedge). Review's evidence (PMID:19829063 CDK2, 23178685 ERalpha, 28169274 ARMC5 Y2H) does not overlap; PN evidence is not in the review and supports a speculative CUL3-regulator role not adopted by the review.
- **Verdict:** Inconsistent — PN over-reaches. GO:0160072 scaffold MF should not propagate to CACUL1 (no scaffold evidence; review treats cullin-fold terms as over-annotation).
- **Recommended edits:** Suppress/except the Cullin-group GO:0160072 projection for CACUL1; mark the node mapping as not-inherited for this degenerate member. [MAP]

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CACUL1/CACUL1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cullin | degenerate, possible CUL3 inhibitor
- UniProt: Q86Y37
- In branches: UPS
- Signature domains: IPR001373
- Auxiliary domains: (none)
- PN references (titles):
    - 26238671
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin|degenerate, possible CUL3 inhibitor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual, regulatory, adaptor, or uncertain UPS bucket. The shared label does not by itself establish a safe gene-level GO propagation.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160072 ubiquitin ligase complex scaffold activity]
        rationale: This PN group captures cullin or cullin-associated scaffold roles in ubiquitin ligase complexes. The shared GO molecular-function target is ubiquitin ligase complex scaffold activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0160072 ubiquitin ligase complex scaffold activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
