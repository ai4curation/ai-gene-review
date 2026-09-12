# EEF2K PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O00418
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EEF2K/EEF2K-ai-review.yaml](EEF2K-ai-review.yaml)
- AIGR review HTML: present - [genes/human/EEF2K/EEF2K-ai-review.html](EEF2K-ai-review.html)
- Gene notes: present - [genes/human/EEF2K/EEF2K-notes.md](EEF2K-notes.md)
- GOA TSV: present - [genes/human/EEF2K/EEF2K-goa.tsv](EEF2K-goa.tsv)
- UniProt record: present - [genes/human/EEF2K/EEF2K-uniprot.txt](EEF2K-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EEF2K.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EEF2K.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EEF2K.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EEF2K.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: EEF2K (eukaryotic elongation factor 2 kinase, also called calcium/calmodulin-dependent eEF2 kinase) is an atypical protein kinase of the alpha-kinase family, structurally unrelated to the classical eukaryotic protein-kinase superfamily and instead related to the myosin heavy chain kinases. Its single physiological substrate is the translation elongation factor eEF2, which it phosphorylates on Thr56; this phosphorylation prevents eEF2 from binding the ribosome, inactivating it and slowing the rate of peptide-chain elongation, thereby down-regulating global protein synthesis. EEF2K activity is strictly calcium/calmodulin-dependent and is further tuned by phosphorylation from multiple upstream signaling kinases (AMPK and TRPM7 activate it; mTOR/S6K, RSK and others inhibit it), coupling translation elongation to nutrient, energy and stress status. It acts in the cytosol and, in neurons, contributes to activity-dependent regulation of dendritic/synaptic translation.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 20; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Internal review/notes are consistent and correct: EEF2K is a Ca2+/calmodulin-dependent **alpha-kinase** whose sole substrate is eEF2 (core MF GO:0004686 elongation factor-2 kinase activity). This DIRECTLY CONTRADICTS the PN node, which files EEF2K among "elongation factors" and projects GO:0003746 translation elongation factor activity. EEF2K is the regulatory kinase, not an EF. The review even REMOVES GO:0008135 (translation factor activity, RNA binding) as a substrate-conflation error — the same conflation the PN projection makes.
- **PN story / NEW pressure:** Projected GO:0003746 is `more_specific_than_existing_goa` per dossier, but it is the wrong molecular function for this gene. EEF2K's function is already captured by GO:0004686 (in GOA, ACCEPTed core) and would be better served at the process level by GO:0045900 negative regulation of translational elongation (OLS-verified; already the review's MODIFY target for GO:0006414). The PN term **over-reaches / is wrong**.
- **Evidence alignment:** Dossier gives no reference titles. Review anchors PMID:9144159 (alpha-kinase founding paper), PMID:11015200, PMID:23184662 — all VERIFIED and about kinase activity, none supporting EF activity. Divergence: PN node has no citation backing an EF role.
- **Verdict:** Clear mis-mapping — EEF2K is the eEF2 kinase, not a translation elongation factor; GO:0003746 should not be projected. **Recommended edits:** [MAP] remove GO:0003746 projection for EEF2K; if a shared process is wanted use GO:0045900 negative regulation of translational elongation. Core MF GO:0004686 already in GOA.

## Full Consistency Review

- **UniProt:** O00418 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation elongation|assorted elongation factors` ; **PN-node mapping:** type `assorted elongation factors` → GO:0003746 translation elongation factor activity (mapped, ok_for_propagation); group `Translation elongation` → GO:0006414 context_only.
- **Consistency:** Internal review/notes are consistent and correct: EEF2K is a Ca2+/calmodulin-dependent **alpha-kinase** whose sole substrate is eEF2 (core MF GO:0004686 elongation factor-2 kinase activity). This DIRECTLY CONTRADICTS the PN node, which files EEF2K among "elongation factors" and projects GO:0003746 translation elongation factor activity. EEF2K is the regulatory kinase, not an EF. The review even REMOVES GO:0008135 (translation factor activity, RNA binding) as a substrate-conflation error — the same conflation the PN projection makes.
- **PN story / NEW pressure:** Projected GO:0003746 is `more_specific_than_existing_goa` per dossier, but it is the wrong molecular function for this gene. EEF2K's function is already captured by GO:0004686 (in GOA, ACCEPTed core) and would be better served at the process level by GO:0045900 negative regulation of translational elongation (OLS-verified; already the review's MODIFY target for GO:0006414). The PN term **over-reaches / is wrong**.
- **Mapping strategy:** EEF2K argues the `assorted elongation factors` type conflates true EFs (eEF1A/eEF2) with elongation *regulators*. Projecting GO:0003746 onto a kinase is a category error; recommend excluding kinases/regulators from that type's MF projection.
- **Evidence alignment:** Dossier gives no reference titles. Review anchors PMID:9144159 (alpha-kinase founding paper), PMID:11015200, PMID:23184662 — all VERIFIED and about kinase activity, none supporting EF activity. Divergence: PN node has no citation backing an EF role.
- **Verdict:** Clear mis-mapping — EEF2K is the eEF2 kinase, not a translation elongation factor; GO:0003746 should not be projected. **Recommended edits:** [MAP] remove GO:0003746 projection for EEF2K; if a shared process is wanted use GO:0045900 negative regulation of translational elongation. Core MF GO:0004686 already in GOA.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/EEF2K/EEF2K-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation elongation | assorted elongation factors
- UniProt: O00418
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation elongation|assorted elongation factors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003746 translation elongation factor activity]
        rationale: This PN type groups cytosolic elongation factors. Translation elongation factor activity is the shared molecular-function target.
    - [group] Translation|Cytosolic translation|Translation elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006414 translational elongation]
        rationale: This PN group is an elongation-context bucket, but it also contains tRNA synthetases, tRNA deacylases, and multisynthetase-complex members whose direct shared assertions are narrower molecular functions or complexes. The elongation relationship is retained as context only.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0003746 translation elongation factor activity | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Translation elongation|assorted elongation factors

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
