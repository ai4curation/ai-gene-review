# ATAD3A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NVI7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1379)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATAD3A/ATAD3A-ai-review.yaml](ATAD3A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATAD3A/ATAD3A-ai-review.html](ATAD3A-ai-review.html)
- Gene notes: present - [genes/human/ATAD3A/ATAD3A-notes.md](ATAD3A-notes.md)
- GOA TSV: present - [genes/human/ATAD3A/ATAD3A-goa.tsv](ATAD3A-goa.tsv)
- UniProt record: present - [genes/human/ATAD3A/ATAD3A-uniprot.txt](ATAD3A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATAD3A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATAD3A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATAD3A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATAD3A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATAD3A/ATAD3A-deep-research-manual.md](ATAD3A-deep-research-manual.md)

## AIGR Review Snapshot

- Description: ATAD3A encodes a mitochondrial AAA+ ATPase that is anchored in the mitochondrial inner membrane, enriched at inner/outer membrane and mitochondria-ER contact regions, and associated with mitochondrial nucleoids. It supports mitochondrial network organization, mtDNA/nucleoid organization, and mitochondrial protein synthesis, and it can participate in stress-response signaling from mitochondria, including PERK modulation at mitochondria-ER contact sites and HRI-mediated integrated stress response signaling after mitochondrial DNA breaks.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 1; NEW: 2

## PN Consistency Summary

- **Consistency:** Consistent, with a deliberate, well-documented divergence from the projection. Deep research (manual synthesis), review YAML, and notes all describe ATAD3A as a mitochondrial inner-membrane AAA+ ATPase for network/nucleoid/mtDNA organization and mitochondrial translation, with secondary stress signaling (PERK, HRI/ISR). The PN mitophagy projection is explicitly evaluated and rejected in notes ("I did not add GO:0000423 mitophagy"). No internal contradiction.
- **PN story / NEW pressure:** PN asserts ATAD3A in mitophagy (GO:0000423, real term). PN Notes base this on a mouse Atad3a/Pink1 study (Nat Immunology) where Atad3a *suppresses* mitophagy. The review correctly declined to ADD mitophagy: human evidence shows ATAD3A normally restrains PINK1 accumulation, so a positive "involved_in mitophagy" annotation would mis-state directionality, and no direct cargo-marking/receptor role is shown. Verdict: PN story over-reaches; appropriately NOT added. Review instead ADDED GO:0032042 (mtDNA metabolic process) and GO:0032543 (mitochondrial translation) as NEW — both better-supported core functions.
- **Evidence alignment:** No overlap. PN cites one mouse mitophagy paper (Atad3a/Pink1, Nat Immunology); review is built on mitochondrial topology/nucleoid/translation papers (PMID:20154147, 17210950, 22453275, 18063578) plus stress-signaling papers (PMID:37832546, 39116259) — none shared with the PN row. The projection rests on evidence the review judged insufficient for a human mitophagy assertion.
- **Verdict:** Consistent; PN mitophagy projection correctly NOT added (over-reaches; directionally suppressive in source). No edits required.

## Full Consistency Review

- **UniProt:** Q9NVI7 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway` ; **PN-node mapping:** PINK/PRKN subtype `no_mapping`; Mitophagy type `mapped`, `ok_for_propagation_to_go` → GO:0000423 mitophagy (new_to_goa).
- **Consistency:** Consistent, with a deliberate, well-documented divergence from the projection. Deep research (manual synthesis), review YAML, and notes all describe ATAD3A as a mitochondrial inner-membrane AAA+ ATPase for network/nucleoid/mtDNA organization and mitochondrial translation, with secondary stress signaling (PERK, HRI/ISR). The PN mitophagy projection is explicitly evaluated and rejected in notes ("I did not add GO:0000423 mitophagy"). No internal contradiction.
- **PN story / NEW pressure:** PN asserts ATAD3A in mitophagy (GO:0000423, real term). PN Notes base this on a mouse Atad3a/Pink1 study (Nat Immunology) where Atad3a *suppresses* mitophagy. The review correctly declined to ADD mitophagy: human evidence shows ATAD3A normally restrains PINK1 accumulation, so a positive "involved_in mitophagy" annotation would mis-state directionality, and no direct cargo-marking/receptor role is shown. Verdict: PN story over-reaches; appropriately NOT added. Review instead ADDED GO:0032042 (mtDNA metabolic process) and GO:0032543 (mitochondrial translation) as NEW — both better-supported core functions.
- **Mapping strategy:** Gene is a defensible decline at this node (parallel to RAB7A/HSPA8 broader-rejection precedent): the Mitophagy type-leaf mapping is a class-level statement, but this gene's role is suppressive/indirect, so the projected term (GO:0000423) is broader/wrong-signed relative to the review's evidence.
- **Evidence alignment:** No overlap. PN cites one mouse mitophagy paper (Atad3a/Pink1, Nat Immunology); review is built on mitochondrial topology/nucleoid/translation papers (PMID:20154147, 17210950, 22453275, 18063578) plus stress-signaling papers (PMID:37832546, 39116259) — none shared with the PN row. The projection rests on evidence the review judged insufficient for a human mitophagy assertion.
- **Verdict:** Consistent; PN mitophagy projection correctly NOT added (over-reaches; directionally suppressive in source). No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATAD3A/ATAD3A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | Mitophagy | PINK/PRKN pathway
- UniProt: Q9NVI7
- In branches: ALP
- Notes: AAA+ ATPase involved in mitochondrial dynamics. By homology with mouse: deletion of Atad3a hyperactivates mitophagy. Atad3a normally facilitates import and processing of Pink1, absence causes accumulation and activates mitophagy.
- PN references (titles):
    - Atad3a suppresses Pink1-dependent mitophagy to maintain homeostasis of hematopoietic progenitor cells | Nature Immunology
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy|PINK/PRKN pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: The PN marking category for mitophagy captures upstream cargo-marking steps that commit mitochondrial substrates to the mitophagy pathway. That supports propagation to mitophagy.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|Mitophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
