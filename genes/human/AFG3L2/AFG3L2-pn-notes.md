# AFG3L2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y4W6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1345)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AFG3L2/AFG3L2-ai-review.yaml](AFG3L2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AFG3L2/AFG3L2-ai-review.html](AFG3L2-ai-review.html)
- Gene notes: present - [genes/human/AFG3L2/AFG3L2-notes.md](AFG3L2-notes.md)
- GOA TSV: present - [genes/human/AFG3L2/AFG3L2-goa.tsv](AFG3L2-goa.tsv)
- UniProt record: present - [genes/human/AFG3L2/AFG3L2-uniprot.txt](AFG3L2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AFG3L2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AFG3L2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AFG3L2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AFG3L2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AFG3L2/AFG3L2-deep-research-falcon.md](AFG3L2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AFG3L2 is a mitochondrial inner membrane m-AAA protease subunit with AAA+ ATPase and zinc metalloendopeptidase domains exposed to the matrix side of the inner membrane. It assembles as AFG3L2 homohexamers and as AFG3L2-SPG7 heterohexamers that use ATP hydrolysis to unfold, translocate, and cleave mitochondrial substrates. Its major roles include protein quality control of newly synthesized or misassembled inner-membrane proteins, processing of selected mitochondrial proteins such as MRPL32 and PINK1, and regulatory degradation of substrates including EMRE/SMDT1, SLC25A39, SLC25A45, and TMBIM5/GHITM. Through these proteolytic activities AFG3L2 supports mitochondrial respiratory-chain assembly, calcium uniporter regulation, mitochondrial glutathione homeostasis, mitochondrial morphology, and neuronal maintenance.
- Existing/core annotation action counts: ACCEPT: 43; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 6; MODIFY: 17; NEW: 1

## PN Consistency Summary

- **Consistency:** Deep research (falcon), review YAML, and PN annotation agree on the core picture: AFG3L2 is the m-AAA inner-membrane AAA+/M41 zinc metalloprotease performing mitochondrial protein QC, processing (MRPL32), and regulated degradation (EMRE, SLC25A39/45, PINK1, TMBIM5). One deliberate, well-flagged divergence: the PN group projects GO:0005759 mitochondrial matrix as the localization target, but the review rejects this (AFG3L2 is an integral inner-membrane protein with matrix-facing catalytic domains) and keeps GO:0005743 mitochondrial inner membrane. The NEW row's `reason` explicitly states the matrix projection is not accepted. No contradiction beyond this intentional correction.
- **PN story / NEW pressure:** PN class target GO:0035694 mitochondrial protein catabolic process (verified real, non-obsolete) is added as a NEW (IC) annotation and used to MODIFY the generic GO:0006508 proteolysis / GO:0030163 protein catabolic process rows. Defensible and conservative — directly supported by SLC25A39 degradation papers (PMID:37917749, 38157846). Verdict: ADD (already implemented in review).
- **Evidence alignment:** PN dossier carries no reference titles; review is densely evidenced (PMID:31327635, 29932645, 19748354, 27642048, 28396416, 37917749, 38157846, 41075794). PN projection TSV is cited as supporting file for GO:0035694. No PMID-level conflicts.
- **Verdict:** Consistent; PN GO:0035694 correctly adopted as NEW; PN matrix (GO:0005759) projection correctly overruled at gene level. **Recommended edits:** none required. Optional [MAP]: flag mitochondrial-proteostasis "Matrix protease" group GO:0005759 as too specific for inner-membrane matrix-facing proteases (consider GO:0005743 or no_mapping).

## Full Consistency Review

- **UniProt:** Q9Y4W6 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease` ; **PN-node mapping:** group `mapped` ok_for_propagation GO:0005759 mitochondrial matrix; class `mapped` GO:0035694 mitochondrial protein catabolic process; branch `no_mapping`.
- **Consistency:** Deep research (falcon), review YAML, and PN annotation agree on the core picture: AFG3L2 is the m-AAA inner-membrane AAA+/M41 zinc metalloprotease performing mitochondrial protein QC, processing (MRPL32), and regulated degradation (EMRE, SLC25A39/45, PINK1, TMBIM5). One deliberate, well-flagged divergence: the PN group projects GO:0005759 mitochondrial matrix as the localization target, but the review rejects this (AFG3L2 is an integral inner-membrane protein with matrix-facing catalytic domains) and keeps GO:0005743 mitochondrial inner membrane. The NEW row's `reason` explicitly states the matrix projection is not accepted. No contradiction beyond this intentional correction.
- **PN story / NEW pressure:** PN class target GO:0035694 mitochondrial protein catabolic process (verified real, non-obsolete) is added as a NEW (IC) annotation and used to MODIFY the generic GO:0006508 proteolysis / GO:0030163 protein catabolic process rows. Defensible and conservative — directly supported by SLC25A39 degradation papers (PMID:37917749, 38157846). Verdict: ADD (already implemented in review).
- **Mapping strategy:** Gene refines, does not change, the node. The class→GO:0035694 mapping is correct and adopted. The group→GO:0005759 matrix mapping is too specific/wrong-compartment for AFG3L2; review's rejection is sound (matrix-facing topology ≠ matrix residence).
- **Evidence alignment:** PN dossier carries no reference titles; review is densely evidenced (PMID:31327635, 29932645, 19748354, 27642048, 28396416, 37917749, 38157846, 41075794). PN projection TSV is cited as supporting file for GO:0035694. No PMID-level conflicts.
- **Verdict:** Consistent; PN GO:0035694 correctly adopted as NEW; PN matrix (GO:0005759) projection correctly overruled at gene level. **Recommended edits:** none required. Optional [MAP]: flag mitochondrial-proteostasis "Matrix protease" group GO:0005759 as too specific for inner-membrane matrix-facing proteases (consider GO:0005743 or no_mapping).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AFG3L2/AFG3L2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Matrix protease
- UniProt: Q9Y4W6
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005759 mitochondrial matrix]
        rationale: This PN group identifies matrix-local protease systems. The source is a compartmental proteostasis bucket, so the mitochondrial matrix cellular-component term is the conservative propagation target.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0005759 mitochondrial matrix | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
