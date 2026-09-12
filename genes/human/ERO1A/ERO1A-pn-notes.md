# ERO1A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96HE7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ERO1A/ERO1A-ai-review.yaml](ERO1A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ERO1A/ERO1A-ai-review.html](ERO1A-ai-review.html)
- Gene notes: present - [genes/human/ERO1A/ERO1A-notes.md](ERO1A-notes.md)
- GOA TSV: present - [genes/human/ERO1A/ERO1A-goa.tsv](ERO1A-goa.tsv)
- UniProt record: present - [genes/human/ERO1A/ERO1A-uniprot.txt](ERO1A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ERO1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ERO1A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERO1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERO1A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ERO1A (ERO1-like protein alpha, formerly ERO1L; endoplasmic reticulum oxidoreductin-1 alpha) is an ER membrane-associated, FAD-dependent flavoprotein sulfhydryl oxidase (EC 1.8.3.2) that drives oxidative protein folding in the endoplasmic reticulum. It reoxidizes the protein disulfide isomerase P4HB/PDI, regenerating PDI's active-site disulfide so that PDI can catalyze further rounds of disulfide-bond formation in nascent secretory proteins; the electrons abstracted are passed via bound FAD to molecular oxygen, producing hydrogen peroxide. It is a peripheral membrane protein on the lumenal side of the ER, retained there through its interaction with ERP44, and is also detected in the Golgi lumen and secreted. Its enzymatic activity is tightly regulated by intramolecular regulatory disulfide bonds (involving Cys94/Cys99/Cys104/Cys131) to limit reactive-oxygen-species accumulation, and is further tuned by FAM20C-mediated phosphorylation at Ser145. ERO1A is induced by hypoxia via the HIF pathway and during the unfolded protein response. Through oxidative folding it supports maturation of disulfide-rich secretory cargo such as immunoglobulins, and participates in ER-stress responses, cholera-toxin retrotranslocation, and ER redox homeostasis.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 23; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Notes, review YAML, and the *corrected* PN type-node mapping are consistent: ERO1A is an FAD-dependent sulfhydryl OXIDASE that reoxidizes PDI, not an isomerase. Review core MF = GO:0016971 (EXP PMID:11707400/29858230, ACCEPT) and it explicitly **MARK_AS_OVER_ANNOTATED** the GO:0015035 protein-disulfide reductase rows (wrong directionality). The dossier rationale documents this correction explicitly. **Internal PN tension:** the parent `Protein disulfide isomerases` group still maps GO:0003756 and the projected-annotations list still projects GO:0003756 to ERO1A as new_to_goa — which contradicts the corrected type node and the review (which never asserts isomerase activity for this oxidase).
- **PN story / NEW pressure:** GO:0016971 (OLS-verified) is already in GOA (EXP) and ACCEPTed — captured, no NEW pressure. GO:0003756 (verified real) should NOT be added to ERO1A: it is biologically wrong for an oxidase (the review asserts oxidase, not isomerase; cf. the reductase over-annotation it rejects). Conclusion on the group projection: **over-reaches** for ERO1A.
- **Evidence alignment:** PN dossier lists no reference titles. Review oxidase evidence (PMID:11707400, 29858230, 10671517, GOA-anchored to GO:0016971/GO:0016972) is reviewer-supplied; the ERO1A↔P4HB redox-relay interaction (PMID:20802462) cross-links to the P4HB review (where it appears as ERO1A protein binding). Alignment is by shared biology and the cross-referenced relay partner.
- **Verdict:** Consistent at the (corrected) gene/type level; GO:0016971 validated and captured. The lingering **group-level GO:0003756 projection over-reaches** and should not land on ERO1A. **Recommended edits:** [MAP] suppress/override the GO:0003756 projection for ERO1A (and ERO1B) so the PDI-reoxidation oxidase children inherit only GO:0016971, not the parent isomerase term (matches the already-corrected type node and the review's oxidase-vs-isomerase distinction).

## Full Consistency Review

- **UniProt:** Q96HE7 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Folding enzyme|Protein disulfide isomerases|Protein disulfide isomerase reoxidation`. **PN-node mapping:** type `PDI reoxidation`=mapped→**GO:0016971 flavin-dependent sulfhydryl oxidase activity** (corrected in batch-5 after gene-level review); parent group `Protein disulfide isomerases`=mapped→**GO:0003756 protein disulfide isomerase activity** (new_to_goa); class/branch=no_mapping.
- **Consistency:** Notes, review YAML, and the *corrected* PN type-node mapping are consistent: ERO1A is an FAD-dependent sulfhydryl OXIDASE that reoxidizes PDI, not an isomerase. Review core MF = GO:0016971 (EXP PMID:11707400/29858230, ACCEPT) and it explicitly **MARK_AS_OVER_ANNOTATED** the GO:0015035 protein-disulfide reductase rows (wrong directionality). The dossier rationale documents this correction explicitly. **Internal PN tension:** the parent `Protein disulfide isomerases` group still maps GO:0003756 and the projected-annotations list still projects GO:0003756 to ERO1A as new_to_goa — which contradicts the corrected type node and the review (which never asserts isomerase activity for this oxidase).
- **PN story / NEW pressure:** GO:0016971 (OLS-verified) is already in GOA (EXP) and ACCEPTed — captured, no NEW pressure. GO:0003756 (verified real) should NOT be added to ERO1A: it is biologically wrong for an oxidase (the review asserts oxidase, not isomerase; cf. the reductase over-annotation it rejects). Conclusion on the group projection: **over-reaches** for ERO1A.
- **Mapping strategy:** The type-level correction (→GO:0016971) is exactly right and the model fix to follow. The problem is purely inheritance: the group node `Protein disulfide isomerases` lumps catalytic PDIs (P4HB), non-catalytic members (ERP27), and the EROs (oxidases), so its GO:0003756 projection mislabels the oxidase children. Note GO:0016971 is itself a GO child of GO:0015035 reductase, so the over-annotation the review rejects is the *parent* term, not the accepted child — the directionality argument (not the hierarchy) is what justifies the review's split.
- **Evidence alignment:** PN dossier lists no reference titles. Review oxidase evidence (PMID:11707400, 29858230, 10671517, GOA-anchored to GO:0016971/GO:0016972) is reviewer-supplied; the ERO1A↔P4HB redox-relay interaction (PMID:20802462) cross-links to the P4HB review (where it appears as ERO1A protein binding). Alignment is by shared biology and the cross-referenced relay partner.
- **Verdict:** Consistent at the (corrected) gene/type level; GO:0016971 validated and captured. The lingering **group-level GO:0003756 projection over-reaches** and should not land on ERO1A. **Recommended edits:** [MAP] suppress/override the GO:0003756 projection for ERO1A (and ERO1B) so the PDI-reoxidation oxidase children inherit only GO:0016971, not the parent isomerase term (matches the already-corrected type node and the review's oxidase-vs-isomerase distinction).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/ERO1A/ERO1A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases | Protein disulfide isomerase reoxidation
- UniProt: Q96HE7
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Folding enzyme|Protein disulfide isomerases|Protein disulfide isomerase reoxidation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016971 flavin-dependent sulfhydryl oxidase activity]
        rationale: Corrected after gene-level review (proteostasis batch 5). This PN type is the ERO1 "PDI reoxidation" step, whose members (ERO1A/ERO1L, ERO1B/ERO1LB) are FAD-dependent sulfhydryl OXIDASES that reoxidize PDI to regenerate its active site — they do not themselves catalyze protein disulfide isomerization. The previous target GO:0003756 (protein disulfide isomerase activity) was incorrect for this node and would mislabel the oxidases as isomerases (both ERO1A and ERO1B reviews mark the protein-disulfide reductase/isomerase terms as over-annotations). The correct shared molecular function is GO:0016971 flavin-dependent sulfhydryl oxidase activity, which both genes carry with experimental (EXP) evidence in GOA.
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases|Protein disulfide isomerase reoxidation

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
