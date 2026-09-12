# AIPL1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NZN9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1355)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AIPL1/AIPL1-ai-review.yaml](AIPL1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AIPL1/AIPL1-ai-review.html](AIPL1-ai-review.html)
- Gene notes: present - [genes/human/AIPL1/AIPL1-notes.md](AIPL1-notes.md)
- GOA TSV: present - [genes/human/AIPL1/AIPL1-goa.tsv](AIPL1-goa.tsv)
- UniProt record: present - [genes/human/AIPL1/AIPL1-uniprot.txt](AIPL1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AIPL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AIPL1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AIPL1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AIPL1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AIPL1/AIPL1-deep-research-falcon.md](AIPL1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AIPL1 is a retina- and pineal-enriched FKBP-like/TPR-domain co-chaperone required for normal photoreceptor function. Its TPR region binds HSP90, while its FKBP-like domain binds prenyl/farnesyl moieties rather than acting as a peptidyl-prolyl isomerase. AIPL1 works with HSP90 to promote maturation and stable assembly of rod and cone phosphodiesterase 6 (PDE6), the cGMP phosphodiesterase that drives phototransduction. Loss of AIPL1 destabilizes PDE6 and causes severe early-onset retinal degeneration, including Leber congenital amaurosis 4.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 1; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent on the chaperone axis but a real tension on PPIase. Deep research (PMID:23737531, 35065964) and the review converge: the FKBP-like domain is a farnesyl/prenyl-binding module that does **not** have PPIase activity; the review REMOVEs the IEA GO:0003755 annotation. The PN row 2 / projection treat GO:0003755 as a propagatable FKBP-type activity ("already_in_goa_exact"). These directly contradict each other for AIPL1.
- **PN story / NEW pressure:** PN projects HSP-binding (GO:0031072, more_specific_than_existing_goa). Review goes one step finer with **action NEW GO:0051879 Hsp90 protein binding** (verified real), backed by direct biochemistry (PMID:35065964 1:2 closed-state binding; PMID:28973376). GOA confirms no existing HSP90/heat-shock term → genuinely additive. Verdict: ADD (review's GO:0051879 ⊂ PN's GO:0031072; review is the better target).
- **Evidence alignment:** Dossier carries no PN reference titles; review rests on AIPL1-specific primary literature (PMID:14555765, 23737531, 28973376, 35065964) — no conflict, review is better-sourced.
- **Verdict:** Consistent on HSP90; PPIase projection over-reaches for AIPL1 (correctly REMOVE'd in review).

## Full Consistency Review

- **UniProt:** Q9NZN9 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** two rows — `Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and PPIase domain containing` and `Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type` ; **PN-node mapping:** joint-cochaperone *type* mapped→GO:0031072 (heat shock protein binding, propagate); PPIase *group/type* mapped→GO:0003755 (PPIase activity, propagate; already_in_goa); subtype (mixed TPR/PPIase) no_mapping.
- **Consistency:** Mostly consistent on the chaperone axis but a real tension on PPIase. Deep research (PMID:23737531, 35065964) and the review converge: the FKBP-like domain is a farnesyl/prenyl-binding module that does **not** have PPIase activity; the review REMOVEs the IEA GO:0003755 annotation. The PN row 2 / projection treat GO:0003755 as a propagatable FKBP-type activity ("already_in_goa_exact"). These directly contradict each other for AIPL1.
- **PN story / NEW pressure:** PN projects HSP-binding (GO:0031072, more_specific_than_existing_goa). Review goes one step finer with **action NEW GO:0051879 Hsp90 protein binding** (verified real), backed by direct biochemistry (PMID:35065964 1:2 closed-state binding; PMID:28973376). GOA confirms no existing HSP90/heat-shock term → genuinely additive. Verdict: ADD (review's GO:0051879 ⊂ PN's GO:0031072; review is the better target).
- **Mapping strategy:** No node change needed. The HSP-binding mapping is sound. The PPIase mapping is the problem: it is correct family-wide but **wrong for AIPL1**, the diverged non-catalytic member. Subtype-level no_mapping already hedges this; gene-level evidence overrides the group/type propagation.
- **Evidence alignment:** Dossier carries no PN reference titles; review rests on AIPL1-specific primary literature (PMID:14555765, 23737531, 28973376, 35065964) — no conflict, review is better-sourced.
- **Verdict:** Consistent on HSP90; PPIase projection over-reaches for AIPL1 (correctly REMOVE'd in review).
- **Recommended edits:** [MAP] Flag GO:0003755 PPIase as a known false-positive for AIPL1 in the PPIase group/type mapping notes (gene-level exclusion), so the FKBP-type propagation does not re-assert PPIase activity on AIPL1.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AIPL1/AIPL1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70-HSP90 system integration | HSP70-HSP90 joint cochaperone | CC-TPR and PPIase domain containing
- UniProt: Q9NZN9
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone|CC-TPR and PPIase domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a mixed TPR/PPIase-domain subtype. Although several members are active peptidyl-prolyl isomerases, the bucket also contains PPIase-like cochaperones, so subtype-level PPIase propagation would overstate the shared activity.
    - [type] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031072 heat shock protein binding]
        rationale: This PN type groups joint HSP70/HSP90 cochaperones. The shared mechanistic assertion is binding heat-shock-protein chaperones, while narrower domain labels remain non-mapping unless they carry an independent activity.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | FKBP type
- UniProt: Q9NZN9
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes FKBP-family peptidyl-prolyl isomerases. The matching GO molecular-function term is appropriate for propagation.
    - [group] Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the cytonuclear peptidyl-prolyl isomerase branch. The matching GO molecular-function term is appropriate for propagation.
    - [class] Cytonuclear proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0031072 heat shock protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70-HSP90 system integration|HSP70-HSP90 joint cochaperone
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
