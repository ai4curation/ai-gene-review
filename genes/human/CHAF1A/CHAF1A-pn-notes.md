# CHAF1A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q13111
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHAF1A/CHAF1A-ai-review.yaml](CHAF1A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHAF1A/CHAF1A-ai-review.html](CHAF1A-ai-review.html)
- Gene notes: present - [genes/human/CHAF1A/CHAF1A-notes.md](CHAF1A-notes.md)
- GOA TSV: present - [genes/human/CHAF1A/CHAF1A-goa.tsv](CHAF1A-goa.tsv)
- UniProt record: present - [genes/human/CHAF1A/CHAF1A-uniprot.txt](CHAF1A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHAF1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHAF1A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHAF1A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHAF1A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHAF1A (p150) is the large subunit of Chromatin Assembly Factor 1 (CAF-1), a heterotrimeric histone H3-H4 chaperone composed of CHAF1A, CHAF1B (p60) and RBBP4 (p48). CAF-1 performs the first step of nucleosome assembly, depositing newly synthesized histones H3 and H4 (the replicative variant H3.1) onto DNA during replication-coupled and repair-coupled chromatin assembly; histones H2A/H2B are subsequently added to complete the octamer. CHAF1A binds histones H3-H4 directly and couples assembly to the replication fork by binding the sliding clamp PCNA via its N-terminal region. It also contains a PxVxL motif that binds the chromo shadow domain of HP1 (CBX5), contributing to heterochromatin maintenance by delivering newly synthesized HP1 proteins to heterochromatic replication foci. CHAF1A homodimerizes, an activity required for chromatin assembly, and acts in the nucleus, concentrating at DNA replication foci during S phase.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 17; NEW: 3

## PN Consistency Summary

- **Consistency:** Strong. Review, notes, PN annotation and node mapping all agree CHAF1A (p150) is the large subunit of the CAF-1 H3-H4 histone chaperone, depositing H3.1-H4 in replication-coupled nucleosome assembly. The review already carries GO:0140713 "histone chaperone activity" as a NEW (IC) annotation — exactly matching the PN projection. No contradictions.
- **PN story / NEW pressure:** PN projects GO:0140713 (verified real; in CHAF1A/B reviews already) as new_to_goa — confirmed: GOA captures histone interactions only as bare protein binding / chromatin binding, with no MF histone-chaperone term. Already independently flagged ADD in the review (NEW GO:0140713, plus NEW GO:0042393 histone binding and GO:0006334 nucleosome assembly). PN and review converge; nothing over-reaches.
- **Evidence alignment:** PN row carries no explicit reference list, but the projected MF rests on the same CAF-1 biology the review documents with PMID:8858152, PMID:14718166, PMID:7600578, PMID:21570500 (direct H3/H4 binding). Concordant; no divergence.
- **Verdict:** CONSISTENT — PN GO:0140713 already captured by the review's NEW annotation. **Recommended edits:** none (review and PN aligned).

## Full Consistency Review

- **UniProt:** Q13111 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Nuclear proteostasis|Chaperone|Histone chaperone` ; **PN-node mapping:** Histone-chaperone group→GO:0140713 histone chaperone activity (new_to_goa). Chaperone class + NU branch = no_mapping.
- **Consistency:** Strong. Review, notes, PN annotation and node mapping all agree CHAF1A (p150) is the large subunit of the CAF-1 H3-H4 histone chaperone, depositing H3.1-H4 in replication-coupled nucleosome assembly. The review already carries GO:0140713 "histone chaperone activity" as a NEW (IC) annotation — exactly matching the PN projection. No contradictions.
- **PN story / NEW pressure:** PN projects GO:0140713 (verified real; in CHAF1A/B reviews already) as new_to_goa — confirmed: GOA captures histone interactions only as bare protein binding / chromatin binding, with no MF histone-chaperone term. Already independently flagged ADD in the review (NEW GO:0140713, plus NEW GO:0042393 histone binding and GO:0006334 nucleosome assembly). PN and review converge; nothing over-reaches.
- **Mapping strategy:** Node mapping is correctly placed at the "Histone chaperone" group (narrower than generic "Nuclear proteostasis"/"Chaperone"), aligning to a precise MF (GO:0140713) rather than a broad process — appropriate, not TOMM20/HSPA8-style over-broad. No change needed.
- **Evidence alignment:** PN row carries no explicit reference list, but the projected MF rests on the same CAF-1 biology the review documents with PMID:8858152, PMID:14718166, PMID:7600578, PMID:21570500 (direct H3/H4 binding). Concordant; no divergence.
- **Verdict:** CONSISTENT — PN GO:0140713 already captured by the review's NEW annotation. **Recommended edits:** none (review and PN aligned).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CHAF1A/CHAF1A-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Nuclear proteostasis | Chaperone | Histone chaperone
- UniProt: Q13111
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
