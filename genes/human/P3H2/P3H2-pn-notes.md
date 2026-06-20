# P3H2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IVL5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/P3H2/P3H2-ai-review.yaml](P3H2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/P3H2/P3H2-ai-review.html
- Gene notes: present - [genes/human/P3H2/P3H2-notes.md](P3H2-notes.md)
- GOA TSV: present - [genes/human/P3H2/P3H2-goa.tsv](P3H2-goa.tsv)
- UniProt record: present - [genes/human/P3H2/P3H2-uniprot.txt](P3H2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/P3H2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/P3H2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P3H2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P3H2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/P3H2/P3H2-deep-research-falcon.md](P3H2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: P3H2 (prolyl 3-hydroxylase 2, also LEPREL1/MLAT4) is an endoplasmic reticulum-lumenal, 2-oxoglutarate/Fe(II)-dependent dioxygenase (EC 1.14.11.7) of the leprecan/prolyl 3-hydroxylase family (P3H1/P3H2/P3H3). It catalyzes post-translational formation of (trans-)3-hydroxyproline on procollagen, hydroxylating the first proline in Gly-Pro-4Hyp triplets and requiring a pre-existing 4-hydroxyproline in the third position. P3H2 shows high activity toward the basement-membrane collagen type IV (COL4A1), which has the highest 3-hydroxyproline content of all collagens, and lower activity toward collagen I; it is thus considered the principal modifier of basement-membrane collagens, complementing the fibrillar-collagen isoenzyme P3H1. The enzyme uses Fe(II) and L-ascorbate (vitamin C) as cofactors and 2-oxoglutarate as a co-substrate. The 708-residue precursor has an N-terminal signal sequence, tetratricopeptide (TPR) repeats, an Fe2OG dioxygenase (prolyl 4-hydroxylase alpha-type) catalytic domain, and a C-terminal KDEL-type ER-retention motif that retains it in the ER/sarcoplasmic reticulum; it is also detected in the Golgi. P3H2 is broadly expressed with enrichment in basement-membrane-rich tissues such as kidney and in muscle. Loss-of-function variants cause autosomal-recessive high myopia with cataract and vitreoretinal degeneration (MCVD), consistent with a role in ocular/lens-capsule basement-membrane collagen biogenesis.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 8; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research (notes + falcon), review YAML, PN annotation, and node mapping all describe an ER-lumenal 2-OG/Fe(II) prolyl 3-hydroxylase (EC 1.14.11.7) acting on procollagen, especially basement-membrane collagen IV. No contradictions. PN places it under collagen processing/folding; review core function is GO:0019797 procollagen-proline 3-dioxygenase activity in GO:0005788 ER lumen.
- **PN story / NEW pressure:** PN asserts the shared "collagen biosynthetic process" role. This is essentially already captured: GOA has GO:0032963 collagen metabolic process (the direct parent of GO:0032964; verified via OLS), accepted in the review. GO:0032964 is one step more specific and defensible (verified real, child of GO:0032963). Conclusion: low-pressure ADD of GO:0032964 (or rely on existing GO:0032963) — the substrate-specific story is captured; the projection is a justified mild refinement, not an over-reach.
- **Evidence alignment:** PN dossier carries no reference titles (mapping-only). Review evidence: IDA PMID:18487197 (collagen IV characterization), PMID:15063763 (ER/Golgi localization), plus KO/disease papers (PMID:29491144, 35499085). Substrate-specificity story (collagen IV) underpins the PN "collagen processing" placement; consistent.
- **Verdict:** Consistent and well-curated; PN collagen-biosynthesis story already captured (GO:0032963) with GO:0032964 a defensible narrower ADD.

## Full Consistency Review

- **UniProt:** Q8IVL5 (LEPREL1) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO=GO:0032964 collagen biosynthetic process (class/branch = no_mapping). Projection goa_status=more_specific_than_existing_goa.
- **Consistency:** Fully consistent. Deep research (notes + falcon), review YAML, PN annotation, and node mapping all describe an ER-lumenal 2-OG/Fe(II) prolyl 3-hydroxylase (EC 1.14.11.7) acting on procollagen, especially basement-membrane collagen IV. No contradictions. PN places it under collagen processing/folding; review core function is GO:0019797 procollagen-proline 3-dioxygenase activity in GO:0005788 ER lumen.
- **PN story / NEW pressure:** PN asserts the shared "collagen biosynthetic process" role. This is essentially already captured: GOA has GO:0032963 collagen metabolic process (the direct parent of GO:0032964; verified via OLS), accepted in the review. GO:0032964 is one step more specific and defensible (verified real, child of GO:0032963). Conclusion: low-pressure ADD of GO:0032964 (or rely on existing GO:0032963) — the substrate-specific story is captured; the projection is a justified mild refinement, not an over-reach.
- **Mapping strategy:** Correct. Group-level mapping with class/branch deliberately unmapped is sound (collagen processing group is substrate-coherent). GO:0032964 is narrower than P3H2's existing GO:0032963 and matches review BP framing; not broader (contrast TOMM20/HSPA8/RAB7A rejected-as-broader precedent). Catalytic gene, correctly handled.
- **Evidence alignment:** PN dossier carries no reference titles (mapping-only). Review evidence: IDA PMID:18487197 (collagen IV characterization), PMID:15063763 (ER/Golgi localization), plus KO/disease papers (PMID:29491144, 35499085). Substrate-specificity story (collagen IV) underpins the PN "collagen processing" placement; consistent.
- **Verdict:** Consistent and well-curated; PN collagen-biosynthesis story already captured (GO:0032963) with GO:0032964 a defensible narrower ADD.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/P3H2/P3H2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: Q8IVL5
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

## Projected GO annotations (1)
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
