# FKBPL PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UIM3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FKBPL/FKBPL-ai-review.yaml](FKBPL-ai-review.yaml)
- AIGR review HTML: present - [genes/human/FKBPL/FKBPL-ai-review.html](FKBPL-ai-review.html)
- Gene notes: present - [genes/human/FKBPL/FKBPL-notes.md](FKBPL-notes.md)
- GOA TSV: present - [genes/human/FKBPL/FKBPL-goa.tsv](FKBPL-goa.tsv)
- UniProt record: present - [genes/human/FKBPL/FKBPL-uniprot.txt](FKBPL-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FKBPL.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FKBPL.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBPL.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBPL.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: FKBPL (FK506-binding protein-like, also known as WISp39) is a divergent member of the FKBP family that retains tetratricopeptide (TPR) repeats but lacks a canonical catalytically active FKBP-type peptidyl-prolyl isomerase domain, so it has no established rotamase activity. It acts as an HSP90 co-chaperone that, through its TPR region, binds HSP90 and, together with the cyclin-dependent kinase inhibitor p21 (CDKN1A), forms a ternary complex that controls p21 protein stability, thereby linking FKBPL to cell-cycle and DNA-damage/radiation responses (it was originally identified as a stress-response gene implicated in induced radioresistance). FKBPL also exists as a secreted, extracellular protein with potent anti-angiogenic activity, a property exploited by FKBPL-derived therapeutic peptides. It is ubiquitously expressed with higher levels in testis.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 8

## PN Consistency Summary

- **Consistency:** Notes, review YAML, and PN mapping are fully consistent. All three correctly frame FKBPL/WISp39 as a **non-canonical, catalytically inactive FKBP** (no functional PPIase domain) that acts as a TPR/HSP90 co-chaperone forming a ternary HSP90AB1–p21(CDKN1A) complex regulating p21 stability, plus a secreted anti-angiogenic pool. No contradiction.
- **PN story / NEW pressure:** GO:0051879 (OLS-verified) is **not** in FKBPL's GOA (GOA MF rows are all bare protein binding to ANKRD49/CALCOCO2 HT-interactome hits — HSP90 is not among the IPI WITH partners), confirming PN's more_specific_than_existing_goa. The review **adds** GO:0051879 as the single core molecular function (supported by UniProt FUNCTION/SUBUNIT). This matches the PN projection exactly. Conclusion: legitimate ADD, executed in the review. No over-reach: PN correctly does NOT project PPIase activity (which would be wrong for this degenerate FKBP).
- **Evidence alignment:** PN dossier lists no reference titles for FKBPL; alignment is by biology (HSP90 co-chaperone). Review evidence is reviewer-supplied (PMID:10521921 radioresistance/NAS; PMID:25767277 anti-angiogenic/extracellular; PMID:15664193 cited in notes for the WISp39–p21–HSP90 mechanism; recurrent ANKRD49/CALCOCO2 HT hits). The core HSP90/p21 mechanism rests on UniProt + PMID:15664193 rather than a GOA-anchored row.
- **Verdict:** Consistent; PN GO:0051879 projection validated and added as the core MF; subtype-level PPIase correctly withheld. **Recommended edits:** none required; [REF] optionally add PMID:15664193 (Jascur et al., WISp39/HSP90/p21) as an explicit reference entry in the review YAML to anchor the GO:0051879 core function (currently it is only in notes, with the YAML core_function relying on UniProt text).

## Full Consistency Review

- **UniProt:** Q9UIM3 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain containing`. **PN-node mapping:** type `HSP90 cochaperone`=mapped→**GO:0051879 Hsp90 protein binding** (more_specific_than_existing_goa); subtype `CC-TPR and PPIase domain containing`=no_mapping (correctly declines a subtype-level PPIase mapping because members are mixed/non-canonical); group/class/branch=no_mapping.
- **Consistency:** Notes, review YAML, and PN mapping are fully consistent. All three correctly frame FKBPL/WISp39 as a **non-canonical, catalytically inactive FKBP** (no functional PPIase domain) that acts as a TPR/HSP90 co-chaperone forming a ternary HSP90AB1–p21(CDKN1A) complex regulating p21 stability, plus a secreted anti-angiogenic pool. No contradiction.
- **PN story / NEW pressure:** GO:0051879 (OLS-verified) is **not** in FKBPL's GOA (GOA MF rows are all bare protein binding to ANKRD49/CALCOCO2 HT-interactome hits — HSP90 is not among the IPI WITH partners), confirming PN's more_specific_than_existing_goa. The review **adds** GO:0051879 as the single core molecular function (supported by UniProt FUNCTION/SUBUNIT). This matches the PN projection exactly. Conclusion: legitimate ADD, executed in the review. No over-reach: PN correctly does NOT project PPIase activity (which would be wrong for this degenerate FKBP).
- **Mapping strategy:** Cleanly handled. The subtype no_mapping is the key correct decision — it prevents propagating PPIase activity (GO:0003755) to a non-catalytic member, the same restraint the FKBP8 dossier applies in reverse. Gene-level review and PN projection agree on the one defensible shared MF (HSP90 binding). No mapping change needed.
- **Evidence alignment:** PN dossier lists no reference titles for FKBPL; alignment is by biology (HSP90 co-chaperone). Review evidence is reviewer-supplied (PMID:10521921 radioresistance/NAS; PMID:25767277 anti-angiogenic/extracellular; PMID:15664193 cited in notes for the WISp39–p21–HSP90 mechanism; recurrent ANKRD49/CALCOCO2 HT hits). The core HSP90/p21 mechanism rests on UniProt + PMID:15664193 rather than a GOA-anchored row.
- **Verdict:** Consistent; PN GO:0051879 projection validated and added as the core MF; subtype-level PPIase correctly withheld. **Recommended edits:** none required; [REF] optionally add PMID:15664193 (Jascur et al., WISp39/HSP90/p21) as an explicit reference entry in the review YAML to anchor the GO:0051879 core function (currently it is only in notes, with the YAML core_function relying on UniProt text).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/FKBPL/FKBPL-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CC-TPR and PPIase domain containing
- UniProt: Q9UIM3
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed HSP90 cochaperone subtype with FKBP/PPIase-like members. The parent HSP90-cochaperone mapping captures the shared HSP90-binding role; a subtype-level PPIase mapping would overstate the activity for all members.
    - [type] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051879 Hsp90 protein binding]
        rationale: This PN type groups HSP90 cochaperones. Hsp90 protein binding is the most defensible shared GO molecular-function target for propagation.
    - [group] Cytonuclear proteostasis|Chaperone|HSP90 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
