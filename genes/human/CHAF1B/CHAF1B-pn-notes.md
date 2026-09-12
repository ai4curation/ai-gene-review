# CHAF1B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q13112
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHAF1B/CHAF1B-ai-review.yaml](CHAF1B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHAF1B/CHAF1B-ai-review.html](CHAF1B-ai-review.html)
- Gene notes: present - [genes/human/CHAF1B/CHAF1B-notes.md](CHAF1B-notes.md)
- GOA TSV: present - [genes/human/CHAF1B/CHAF1B-goa.tsv](CHAF1B-goa.tsv)
- UniProt record: present - [genes/human/CHAF1B/CHAF1B-uniprot.txt](CHAF1B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHAF1B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHAF1B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHAF1B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHAF1B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHAF1B (p60, CAF-1 subunit B) is the WD40-repeat medium subunit of Chromatin Assembly Factor 1 (CAF-1), a heterotrimeric histone H3-H4 chaperone composed of CHAF1A (p150), CHAF1B (p60), and RBBP4 (p48). Within CAF-1, p60 bridges the large subunit CHAF1A and the histone-binding subunit RBBP4, and the direct p150-p60 interaction is required for CAF-1-mediated nucleosome assembly. CAF-1 performs the first step of nucleosome assembly by depositing newly synthesized histones H3.1-H4 onto DNA in a replication-coupled (DNA-synthesis-dependent) manner, and it is also recruited to chromatin undergoing DNA repair. CHAF1B is built from an N-terminal seven-bladed WD40 beta-propeller and a C-terminal disordered region that is heavily phosphorylated in a cell-cycle-dependent fashion. The active complex resides in the nucleus, where it concentrates at DNA replication foci during S phase; during mitosis the p60 subunit is hyperphosphorylated, CAF-1 is inactivated, and p60 is displaced into the cytoplasm. The gene maps to chromosome 21q22.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 8; MARK_AS_OVER_ANNOTATED: 7; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. Review, notes, PN annotation and node mapping all agree CHAF1B (p60) is the WD40 medium subunit of the CAF-1 H3-H4 chaperone (bridges CHAF1A/p150 and RBBP4/p48; binds H3.1/H3.2/H3.1t), acting in replication-coupled nucleosome assembly. The review already carries GO:0140713 "histone chaperone activity" as a NEW (IC) annotation — matching the PN projection exactly. No contradictions.
- **PN story / NEW pressure:** PN projects GO:0140713 (verified real) as new_to_goa — confirmed: CHAF1B GOA captures histone contacts as histone binding (GO:0042393, NAS) and bare protein binding, but lacks the MF histone-chaperone-activity term. Already independently flagged ADD in the review (NEW GO:0140713; GO:0042393 retained as core). PN and review converge; nothing over-reaches.
- **Evidence alignment:** PN row carries no explicit reference list; the projected MF rests on the same CAF-1 evidence the review uses (PMID:7600578 p150/p60 + newly synthesized H3/acetyl-H4; PMID:8858152, PMID:14718166; UniProt H3.1/H3.2/H3.1t). Concordant; no divergence. Other interactome PMIDs (BioPlex etc., all ASF1A/B) are correctly MARK_AS_OVER_ANNOTATED.
- **Verdict:** CONSISTENT — PN GO:0140713 already captured by the review's NEW annotation. **Recommended edits:** none (review and PN aligned).

## Full Consistency Review

- **UniProt:** Q13112 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Nuclear proteostasis|Chaperone|Histone chaperone` ; **PN-node mapping:** Histone-chaperone group→GO:0140713 histone chaperone activity (new_to_goa). Chaperone class + NU branch = no_mapping.
- **Consistency:** Strong. Review, notes, PN annotation and node mapping all agree CHAF1B (p60) is the WD40 medium subunit of the CAF-1 H3-H4 chaperone (bridges CHAF1A/p150 and RBBP4/p48; binds H3.1/H3.2/H3.1t), acting in replication-coupled nucleosome assembly. The review already carries GO:0140713 "histone chaperone activity" as a NEW (IC) annotation — matching the PN projection exactly. No contradictions.
- **PN story / NEW pressure:** PN projects GO:0140713 (verified real) as new_to_goa — confirmed: CHAF1B GOA captures histone contacts as histone binding (GO:0042393, NAS) and bare protein binding, but lacks the MF histone-chaperone-activity term. Already independently flagged ADD in the review (NEW GO:0140713; GO:0042393 retained as core). PN and review converge; nothing over-reaches.
- **Mapping strategy:** Group-level mapping to the precise MF GO:0140713 (rather than broad "Nuclear proteostasis"/"Chaperone") is correct and avoids over-propagation. Same placement as CHAF1A; appropriate. No change needed.
- **Evidence alignment:** PN row carries no explicit reference list; the projected MF rests on the same CAF-1 evidence the review uses (PMID:7600578 p150/p60 + newly synthesized H3/acetyl-H4; PMID:8858152, PMID:14718166; UniProt H3.1/H3.2/H3.1t). Concordant; no divergence. Other interactome PMIDs (BioPlex etc., all ASF1A/B) are correctly MARK_AS_OVER_ANNOTATED.
- **Verdict:** CONSISTENT — PN GO:0140713 already captured by the review's NEW annotation. **Recommended edits:** none (review and PN aligned).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CHAF1B/CHAF1B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Nuclear proteostasis | Chaperone | Histone chaperone
- UniProt: Q13112
- In branches: NU
- PN-node mapping records (path + ancestors):
    - [group] Nuclear proteostasis|Chaperone|Histone chaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140713 histone chaperone activity]
        rationale: This PN group collects nuclear histone-chaperone factors involved in histone handling, deposition, or exchange. The PN bucket is narrower than general nuclear proteostasis and aligns well with the GO molecular function histone chaperone activity.
    - [class] Nuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the nuclear chaperone class. The current member set includes histone chaperone and nuclear proteostasis context, but the class is not a single GO-equivalent activity; the histone-chaperone child mapping carries the defensible propagation.
    - [branch] Nuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0140713 histone chaperone activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Nuclear proteostasis|Chaperone|Histone chaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
