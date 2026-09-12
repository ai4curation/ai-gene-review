# CDC37L1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q7L3B6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CDC37L1/CDC37L1-ai-review.yaml](CDC37L1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CDC37L1/CDC37L1-ai-review.html](CDC37L1-ai-review.html)
- Gene notes: present - [genes/human/CDC37L1/CDC37L1-notes.md](CDC37L1-notes.md)
- GOA TSV: present - [genes/human/CDC37L1/CDC37L1-goa.tsv](CDC37L1-goa.tsv)
- UniProt record: present - [genes/human/CDC37L1/CDC37L1-uniprot.txt](CDC37L1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CDC37L1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CDC37L1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDC37L1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDC37L1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CDC37L1 (Hsp90 co-chaperone Cdc37-like 1, also called Harc, "Hsp90-associating relative of Cdc37") is a cytoplasmic co-chaperone of the CDC37 family and a paralog of the kinase-specific Hsp90 co-chaperone CDC37. It self-associates and forms complexes with the molecular chaperones Hsp70 and Hsp90 as well as with Hsp90 co-chaperones and adaptors including CDC37, STIP1/Hop, FKBP4 and PPID. Through distinct domains it engages Hsp90 (central/C-terminal region) and Hsp70/Hop (C-terminal region), acting as an adaptor that promotes the interaction of client proteins with the Hsp70 and Hsp90 chaperone systems and thereby contributing to client (notably protein kinase) folding, maturation and stabilization. It is broadly expressed (brain, heart, kidney, liver, placenta and skeletal muscle) and is phosphorylated on serine residues.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 5

## PN Consistency Summary

- **Consistency:** Consistent. Notes, YAML, and PN all frame CDC37L1 (Harc) as a cytoplasmic HSP90/HSP70 co-chaperone (CDC37 paralog). GO:0051879 verified real. The review's repeated MODIFY of bare GO:0005515 IPI rows (WITH HSP90AA1/AB1) → GO:0051879 directly matches the PN projection. No contradictions.
- **PN story / NEW pressure:** PN asserts Hsp90 binding (GO:0051879), which is not present verbatim in GOA (GOA has GO:0031072 heat shock protein binding IBA + bare GO:0005515 IPI to HSP90AA1/AB1). The review already proposes GO:0051879 via MODIFY of the IPI rows, so the PN story is captured by the review and defensibly more specific than the existing heat-shock-protein-binding parent. ADD is effectively already in the review; no over-reach.
- **Evidence alignment:** PN listed no reference titles for this row. Review evidence is genome-scale interactome screens (PMID:25036637 Taipale chaperome map is the most informative; PMID:21988832/25416956/33961781/40205054). WITH partners (HSP90AA1 P07900, HSP90AB1 P08238, STIP1 P31948) underpin the GO:0051879 call. No divergence.
- **Verdict:** Consistent; PN's GO:0051879 is defensible and already operationalized in the review (MODIFY of IPI rows). No new pressure beyond the review.

## Full Consistency Review

- **UniProt:** Q7L3B6 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|no characteristic domain` ; **PN-node mapping:** leaf/`group`/`class`/branch all `no_mapping`; `[type] HSP90 cochaperone` → `mapped` GO:0051879 Hsp90 protein binding (`more_specific_than_existing_goa`).
- **Consistency:** Consistent. Notes, YAML, and PN all frame CDC37L1 (Harc) as a cytoplasmic HSP90/HSP70 co-chaperone (CDC37 paralog). GO:0051879 verified real. The review's repeated MODIFY of bare GO:0005515 IPI rows (WITH HSP90AA1/AB1) → GO:0051879 directly matches the PN projection. No contradictions.
- **PN story / NEW pressure:** PN asserts Hsp90 binding (GO:0051879), which is not present verbatim in GOA (GOA has GO:0031072 heat shock protein binding IBA + bare GO:0005515 IPI to HSP90AA1/AB1). The review already proposes GO:0051879 via MODIFY of the IPI rows, so the PN story is captured by the review and defensibly more specific than the existing heat-shock-protein-binding parent. ADD is effectively already in the review; no over-reach.
- **Mapping strategy:** No change. PN maps conservatively at the `[type]` altitude (cochaperone), with the family/system containers left unmapped — appropriate given CDC37 vs CDC37L1 client divergence. `more_specific_than_existing_goa` is accurate (GO:0051879 is a child concept of the generic heat shock / protein binding annotations).
- **Evidence alignment:** PN listed no reference titles for this row. Review evidence is genome-scale interactome screens (PMID:25036637 Taipale chaperome map is the most informative; PMID:21988832/25416956/33961781/40205054). WITH partners (HSP90AA1 P07900, HSP90AB1 P08238, STIP1 P31948) underpin the GO:0051879 call. No divergence.
- **Verdict:** Consistent; PN's GO:0051879 is defensible and already operationalized in the review (MODIFY of IPI rows). No new pressure beyond the review.

**Recommended edits:** None required. (Review already maps the HSP90-binding IPI evidence to GO:0051879, aligning with the PN node.)

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CDC37L1/CDC37L1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | no characteristic domain
- UniProt: Q7L3B6
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|no characteristic domain
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
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
