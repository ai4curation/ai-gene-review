# PPIB PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P23284
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/PPIB/PPIB-ai-review.yaml](PPIB-ai-review.yaml)
- AIGR review HTML: present - [genes/human/PPIB/PPIB-ai-review.html](PPIB-ai-review.html)
- Gene notes: present - [genes/human/PPIB/PPIB-notes.md](PPIB-notes.md)
- GOA TSV: present - [genes/human/PPIB/PPIB-goa.tsv](PPIB-goa.tsv)
- UniProt record: present - [genes/human/PPIB/PPIB-uniprot.txt](PPIB-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/PPIB.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/PPIB.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PPIB.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PPIB.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: PPIB (peptidyl-prolyl cis-trans isomerase B; cyclophilin B / CypB; also called S-cyclophilin/SCYLP and rotamase B) is an endoplasmic reticulum-lumenal cyclophilin-type peptidyl-prolyl cis-trans isomerase (EC 5.2.1.8) that catalyzes the rate-limiting cis-trans isomerization of Xaa-Pro peptide bonds and thereby accelerates protein folding. It is retained in the ER lumen by a C-terminal retention motif and is a component of ER chaperone/foldase complexes, including the prolyl 3-hydroxylation complex with P3H1 (LEPRE1) and CRTAP that processes procollagen, and an ERp72(PDIA4)-cyclophilin B module that accelerates immunoglobulin folding. Loss-of-function mutations in PPIB cause autosomal-recessive osteogenesis imperfecta type IX, underscoring its role in collagen biogenesis and bone development. Beyond the ER, a secreted/cell-surface pool of cyclophilin B signals through the receptor CD147/EMMPRIN to promote leukocyte (neutrophil) chemotaxis, and the protein is exploited as a host factor by certain viruses (e.g. hepatitis C virus NS5B polymerase, measles virus). Its PPIase activity is inhibited by the immunosuppressant cyclosporin A.
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 32; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Fully consistent. Review, notes, and UniProt agree PPIB is a genuine ER-lumenal cyclophilin-type PPIase (EC 5.2.1.8, CsA-inhibited) and a component of the P3H1/CRTAP/PPIB collagen prolyl-3-hydroxylation complex; LoF causes osteogenesis imperfecta type IX. Both PN mappings align with the review's two core functions.
- **PN story / NEW pressure:** Two projections. (1) GO:0003755 (VERIFIED real) is already in GOA exact (IEA/IDA/ISS/NAS — confirmed in goa.tsv) and ACCEPTed as core — already captured, correct. (2) GO:0032964 collagen biosynthetic process (VERIFIED real via OLS) is NOT in PPIB GOA (confirmed: GOA has only collagen binding GO:0005518 and bone development GO:0060348) — a defensible NEW BP capturing PPIB's collagen-maturation role. Conclude: GO:0003755 already captured; GO:0032964 = ADD (defensible, real, novel-to-GOA).
- **Evidence alignment:** PN node carries no reference titles, but review evidence directly supports both stories: PMID:20676357 / PMID:2000394 (PPIase activity, VERIFIED), PMID:39245686 (P3H1/CRTAP/PPIB collagen complex) and PMID:20089953 (PPIB-null OI) for the collagen/bone biology. Note the nuanced NOT|protein folding and NOT|regulation of PTM (PMID:20089953: PPIB-null OI has normal collagen folding) — these qualify, but do not contradict, the broader collagen-biosynthesis role.
- **Verdict:** CONSISTENT — GO:0003755 already captured (correct); GO:0032964 is a sound NEW addition. **Recommended edits:** [YAML] consider adding GO:0032964 collagen biosynthetic process (involved_in) to PPIB existing/proposed terms, supported by PMID:39245686 + OI9 genetics, to align the review with the defensible PN projection.

## Full Consistency Review

- **UniProt:** P23284 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE (exhaustive; ~55 annotations, notes present, no provider deep-research file)
- **PN placement (2 rows):** `ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type` and `ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding` ; **PN-node mapping:** type+group (PPIases / Cyclophilin type)→GO:0003755 peptidyl-prolyl cis-trans isomerase activity (mapped/ok_for_propagation, already_in_goa_exact); collagen group→GO:0032964 collagen biosynthetic process (mapped/ok_for_propagation, new_to_goa); class/branch→no_mapping.
- **Consistency:** Fully consistent. Review, notes, and UniProt agree PPIB is a genuine ER-lumenal cyclophilin-type PPIase (EC 5.2.1.8, CsA-inhibited) and a component of the P3H1/CRTAP/PPIB collagen prolyl-3-hydroxylation complex; LoF causes osteogenesis imperfecta type IX. Both PN mappings align with the review's two core functions.
- **PN story / NEW pressure:** Two projections. (1) GO:0003755 (VERIFIED real) is already in GOA exact (IEA/IDA/ISS/NAS — confirmed in goa.tsv) and ACCEPTed as core — already captured, correct. (2) GO:0032964 collagen biosynthetic process (VERIFIED real via OLS) is NOT in PPIB GOA (confirmed: GOA has only collagen binding GO:0005518 and bone development GO:0060348) — a defensible NEW BP capturing PPIB's collagen-maturation role. Conclude: GO:0003755 already captured; GO:0032964 = ADD (defensible, real, novel-to-GOA).
- **Mapping strategy:** Mappings are appropriately scoped — narrow, member-supported MF/BP terms, not over-broad umbrellas (unlike the TOMM20/HSPA8/RAB7A rejections). GO:0032964 is well-matched to PPIB's documented collagen-processing function and bone-disease genetics. No mapping change needed.
- **Evidence alignment:** PN node carries no reference titles, but review evidence directly supports both stories: PMID:20676357 / PMID:2000394 (PPIase activity, VERIFIED), PMID:39245686 (P3H1/CRTAP/PPIB collagen complex) and PMID:20089953 (PPIB-null OI) for the collagen/bone biology. Note the nuanced NOT|protein folding and NOT|regulation of PTM (PMID:20089953: PPIB-null OI has normal collagen folding) — these qualify, but do not contradict, the broader collagen-biosynthesis role.
- **Verdict:** CONSISTENT — GO:0003755 already captured (correct); GO:0032964 is a sound NEW addition. **Recommended edits:** [YAML] consider adding GO:0032964 collagen biosynthetic process (involved_in) to PPIB existing/proposed terms, supported by PMID:39245686 + OI9 genetics, to align the review with the defensible PN projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/PPIB/PPIB-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Folding enzyme | Peptidyl-prolyl isomerases | Cyclophilin type
- UniProt: P23284
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN type denotes ER cyclophilin-family PPIases. The matching GO molecular function is appropriate for propagation.
    - [group] ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003755 peptidyl-prolyl cis-trans isomerase activity]
        rationale: This PN group is the ER peptidyl-prolyl isomerase family. The GO PPIase activity term is the appropriate propagation target for this folding enzyme bucket.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: P23284
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032964 collagen biosynthetic process]
        rationale: This PN group contains ER factors dedicated to collagen maturation, processing, and folding. Collagen biosynthetic process captures the shared substrate-specific pathway context.
    - [class] ER proteostasis|Maturation and folding of specific substrates
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases
- GO:0003755 peptidyl-prolyl cis-trans isomerase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Folding enzyme|Peptidyl-prolyl isomerases|Cyclophilin type
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
