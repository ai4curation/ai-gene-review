# FKBP4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q02790
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FKBP4/FKBP4-ai-review.yaml](FKBP4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/FKBP4/FKBP4-ai-review.html](FKBP4-ai-review.html)
- Gene notes: present - [genes/human/FKBP4/FKBP4-notes.md](FKBP4-notes.md)
- GOA TSV: present - [genes/human/FKBP4/FKBP4-goa.tsv](FKBP4-goa.tsv)
- UniProt record: present - [genes/human/FKBP4/FKBP4-uniprot.txt](FKBP4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FKBP4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FKBP4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBP4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FKBP4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: FKBP4 (FKBP52, also called the 52 kDa FK506-binding protein, p59 or HSP-binding immunophilin) is a cytoplasmic immunophilin and HSP90 co-chaperone. It contains two FKBP-type peptidyl-prolyl cis-trans isomerase (PPIase/rotamase) domains (the N-terminal domain carries the active site and is inhibited by FK506) and three C-terminal tetratricopeptide (TPR) repeats that mediate binding to the EEVD motif of HSP90. Through its TPR domain it is incorporated, together with HSP90 and HSP70, into the mature heterocomplexes of steroid hormone receptors (glucocorticoid, androgen, progesterone and mineralocorticoid receptors), where it acts as a positive regulator of receptor hormone-binding affinity and nuclear translocation. By recruiting cytoplasmic dynein to the receptor-HSP90 complex it promotes retrograde, microtubule-dependent transport of activated receptors toward the nucleus. Beyond steroid signaling, its PPIase activity regulates TRPC1 channel opening to control neuronal growth-cone chemotropic guidance, and it modulates microtubule dynamics by antagonizing the tau (MAPT) protein. It localizes mainly to the cytosol but also to mitochondria, the nucleus, the cytoskeleton and axonal projections, and shuttles between these compartments. FKBP4 is the functional antagonist of its paralog FKBP5 (FKBP51), which is a negative regulator of the same steroid receptors.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 44; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 8

## PN Consistency Summary

- **Consistency:** Strong. Review, notes and PN agree FKBP52 is a catalytically active FKBP PPIase (N-terminal domain, FK506-inhibited) AND an HSP90 co-chaperone (TPR→EEVD) in steroid-receptor heterocomplexes, plus a dynein-recruiting adaptor. Both the catalytic (PPIase) and scaffold/co-chaperone MFs are distinguished — prompt's catalytic-vs-scaffold check satisfied. Core MFs = GO:0003755, GO:0031072, GO:0030674. No contradictions.
- **PN story / NEW pressure:** Nothing new. PN's GO:0003755 already in review (core, ACCEPT). PN's GO:0051879 (Hsp90 binding) already present in review ×6 — so the "more_specific_than_existing_goa" projection is **already captured**, not a NEW pressure.
- **Evidence alignment:** PN carries no extra reference titles; review GO:0031072/0051879 supported by GOA IPI PMID:9660753 (HSP90). Consistent.
- **Verdict:** Fully consistent; PN adds no new defensible term (both projected terms already in review). **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** Q02790 (FKBP52) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear|Chaperone|HSP90 system|HSP90 cochaperone|CC-TPR and PPIase domain`; `Cytonuclear|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type` ; **PN-node mapping:** mapped → GO:0051879 (Hsp90 protein binding, more_specific_than_existing_goa), GO:0003755 (PPIase activity, already_in_goa_exact)
- **Consistency:** Strong. Review, notes and PN agree FKBP52 is a catalytically active FKBP PPIase (N-terminal domain, FK506-inhibited) AND an HSP90 co-chaperone (TPR→EEVD) in steroid-receptor heterocomplexes, plus a dynein-recruiting adaptor. Both the catalytic (PPIase) and scaffold/co-chaperone MFs are distinguished — prompt's catalytic-vs-scaffold check satisfied. Core MFs = GO:0003755, GO:0031072, GO:0030674. No contradictions.
- **PN story / NEW pressure:** Nothing new. PN's GO:0003755 already in review (core, ACCEPT). PN's GO:0051879 (Hsp90 binding) already present in review ×6 — so the "more_specific_than_existing_goa" projection is **already captured**, not a NEW pressure.
- **Mapping strategy:** PN type node maps to broad GO:0031072 at the subtype but elects GO:0051879 (the narrower, OLS-confirmed child) at the projection level, matching the review. Conservative and correct: subtype-level PPIase mapping is withheld (mixed-member node) while the gene genuinely carries PPIase. No mapping change.
- **Evidence alignment:** PN carries no extra reference titles; review GO:0031072/0051879 supported by GOA IPI PMID:9660753 (HSP90). Consistent.
- **Verdict:** Fully consistent; PN adds no new defensible term (both projected terms already in review). **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/FKBP4/FKBP4-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CC-TPR and PPIase domain containing
- UniProt: Q02790
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

## PN row 2: Cytonuclear proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | FKBP type
- UniProt: Q02790
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
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Cytonuclear proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|FKBP type

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
