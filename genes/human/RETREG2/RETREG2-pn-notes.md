# RETREG2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NC44
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RETREG2/RETREG2-ai-review.yaml](RETREG2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/RETREG2/RETREG2-ai-review.html
- Gene notes: present - [genes/human/RETREG2/RETREG2-notes.md](RETREG2-notes.md)
- GOA TSV: present - [genes/human/RETREG2/RETREG2-goa.tsv](RETREG2-goa.tsv)
- UniProt record: present - [genes/human/RETREG2/RETREG2-uniprot.txt](RETREG2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RETREG2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RETREG2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RETREG2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RETREG2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/RETREG2/RETREG2-deep-research-falcon.md](RETREG2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: RETREG2 (reticulophagy regulator 2; also called FAM134A) is an endoplasmic-reticulum (ER) membrane protein of the FAM134/RETREG family (RETREG1/FAM134B, RETREG2/FAM134A, RETREG3/FAM134C) that functions as a selective-autophagy receptor for the ER (ER-phagy/reticulophagy). It is a multi-pass ER membrane protein whose transmembrane segments form a reticulon-homology domain (RHD) that bends and shapes ER membranes, and it carries a cytosolic LC3-interacting region (LIR) motif that binds ATG8-family proteins (LC3/GABARAP). RETREG2 is held in an inactive state under basal conditions and is activated by cellular stress; once activated it promotes ER fragmentation and delivers ER fragments into lysosomes by sequestering them into autophagosomes through its LIR-mediated interaction with ATG8 proteins, thereby driving selective turnover of the ER. Beyond bulk ER-phagy, the FAM134 paralogues contribute to ER membrane remodeling and to collagen quality control (the latter reported to be LIR-independent). RETREG2 localizes to the ER membrane.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Excellent. Deep-research notes, review YAML, PN annotation and PN-node mapping all agree RETREG2/FAM134A is an ER-anchored selective-autophagy (ER-phagy/reticulophagy) receptor: stress-activated, RHD shapes/curves ER, LIR binds ATG8 to deliver ER fragments to autophagosomes. PN's "ERphagy"→"reticulophagy synonym" rationale matches the review's `description`. No contradictions. Foundational refs shared (PMID:26040720, PMID:34338405).
- **PN story / NEW pressure:** PN projects GO:0061709 reticulophagy as new_to_goa. Verified real (OLS) and confirmed ABSENT from RETREG2 GOA (GOA carries GO:0140506 adaptor activity, GO:0061753 substrate-to-autophagosome, ER-membrane CC, but NOT the reticulophagy BP). The review captures the molecular function (GO:0140506 ER-autophagosome adaptor activity, ACCEPT/core) and the generic process (GO:0061753) but never asserts the specific BP reticulophagy. So GO:0061709 is a genuine, defensible **ADD** the review omits — and it is more specific/precise than the generic GO:0061753 already accepted. Conclude: ADD reticulophagy (verified real).
- **Evidence alignment:** Strong overlap. PN's single reference (FAM134 paralogues EMBO reports = PMID:34338405) is in the review (HIGH/VERIFIED). Review additionally anchors on the foundational FAM134 ER-phagy paper PMID:26040720.
- **Verdict:** Fully consistent; the reticulophagy BP is a justified ADD the review currently lacks (function captured at MF/generic-BP level only).

## Full Consistency Review

- **UniProt:** Q8NC44 (FAM134A) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (focused; ER-phagy receptor, RHD + LIR, collagen QC)
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy` ; **PN-node mapping:** type→mapped/ok_for_propagation_to_go GO:0061709 reticulophagy (ancestors group/class/branch all no_mapping containers).
- **Consistency:** Excellent. Deep-research notes, review YAML, PN annotation and PN-node mapping all agree RETREG2/FAM134A is an ER-anchored selective-autophagy (ER-phagy/reticulophagy) receptor: stress-activated, RHD shapes/curves ER, LIR binds ATG8 to deliver ER fragments to autophagosomes. PN's "ERphagy"→"reticulophagy synonym" rationale matches the review's `description`. No contradictions. Foundational refs shared (PMID:26040720, PMID:34338405).
- **PN story / NEW pressure:** PN projects GO:0061709 reticulophagy as new_to_goa. Verified real (OLS) and confirmed ABSENT from RETREG2 GOA (GOA carries GO:0140506 adaptor activity, GO:0061753 substrate-to-autophagosome, ER-membrane CC, but NOT the reticulophagy BP). The review captures the molecular function (GO:0140506 ER-autophagosome adaptor activity, ACCEPT/core) and the generic process (GO:0061753) but never asserts the specific BP reticulophagy. So GO:0061709 is a genuine, defensible **ADD** the review omits — and it is more specific/precise than the generic GO:0061753 already accepted. Conclude: ADD reticulophagy (verified real).
- **Mapping strategy:** Correct and conservative. Only the ERphagy leaf propagates (to a narrow, exactly-matching process term); the broad receptor/substrate-selection/branch ancestors are correctly no_mapping. Process-term projection here is narrower than (not broader than) the review's accepted MF/CC, so the TOMM20/HSPA8 "too broad" precedent does not apply. No node-status change warranted.
- **Evidence alignment:** Strong overlap. PN's single reference (FAM134 paralogues EMBO reports = PMID:34338405) is in the review (HIGH/VERIFIED). Review additionally anchors on the foundational FAM134 ER-phagy paper PMID:26040720.
- **Verdict:** Fully consistent; the reticulophagy BP is a justified ADD the review currently lacks (function captured at MF/generic-BP level only).
- **Recommended edits:** [YAML] add GO:0061709 reticulophagy (BP, involved_in; the specific process for this ER-phagy receptor) — currently absent; more precise than the accepted generic GO:0061753. Cite PMID:26040720/PMID:34338405.
- **2026-06-18 follow-up:** Implemented the YAML edit: added GO:0061709 reticulophagy as a NEW BP recommendation and added it to the core ER-phagy function while retaining GO:0061753 substrate localization to autophagosome.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/RETREG2/RETREG2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q8NC44
- In branches: ALP
- Notes: Adapter for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in ERphagy
- PN references (titles):
    - Role of FAM134 paralogues in endoplasmic reticulum remodeling, ER‐phagy, and Collagen quality control | EMBO reports (embopress.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN uses the community label ERphagy for selective autophagy of the endoplasmic reticulum, while GO uses the synonym reticulophagy. Receptor members of this PN category are suitable for propagation to the GO reticulophagy process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
