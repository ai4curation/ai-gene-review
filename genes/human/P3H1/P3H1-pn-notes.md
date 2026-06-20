# P3H1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q32P28
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/P3H1/P3H1-ai-review.yaml](P3H1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/P3H1/P3H1-ai-review.html
- Gene notes: present - [genes/human/P3H1/P3H1-notes.md](P3H1-notes.md)
- GOA TSV: present - [genes/human/P3H1/P3H1-goa.tsv](P3H1-goa.tsv)
- UniProt record: present - [genes/human/P3H1/P3H1-uniprot.txt](P3H1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/P3H1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/P3H1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P3H1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P3H1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/P3H1/P3H1-deep-research-falcon.md](P3H1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: P3H1 (prolyl 3-hydroxylase 1; gene LEPRE1, also known as leprecan-1 and growth suppressor 1) is an endoplasmic-reticulum-lumenal 2-oxoglutarate/Fe(II)-dependent dioxygenase (EC 1.14.11.7) of the leprecan family. It catalyzes the post-translational formation of 3-hydroxyproline at specific -Xaa-Pro-Gly- prolines in procollagen chains, most notably the alpha1(I)Pro986 residue of type I and type II collagen, a modification required for proper collagen triple-helix folding, assembly and stability. P3H1 is the catalytic core of the ER collagen prolyl 3-hydroxylation complex (the "PCP complex"), a 1:1:1 ternary assembly with cartilage-associated protein (CRTAP) and peptidyl-prolyl cis-trans isomerase B (PPIB/cyclophilin B). Within this complex P3H1 contributes prolyl 3-hydroxylase activity while PPIB provides cis-trans isomerase activity and CRTAP stabilizes the assembly and helps recruit collagen substrate; the complex also functions as a collagen chaperone. P3H1 carries a C-terminal KDEL ER-retrieval signal that retains it (and, with it, CRTAP) in the ER lumen. Catalysis requires a non-heme Fe(II) center, the co-substrate 2-oxoglutarate, molecular oxygen, and L-ascorbate (vitamin C) as cofactor. Loss-of-function mutations in LEPRE1 abolish alpha1(I)Pro986 3-hydroxylation, delay collagen folding and cause overmodification of the collagen helix, resulting in autosomal recessive osteogenesis imperfecta type 8 (OI8). A secreted chondroitin sulfate proteoglycan form of leprecan can also be deposited in the extracellular matrix.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 14; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Deep research ↔ review ↔ PN annotation fully consistent. P3H1 is correctly the catalytic core (procollagen-proline 3-dioxygenase, EC 1.14.11.7, GO:0019797) of the ER PCP complex (with CRTAP + PPIB), required for collagen helix folding/stability; loss causes recessive OI8. PN "ER collagen processing and folding" matches precisely.
- **PN story / NEW pressure:** No NEW GO pressure — catalytic, complex-membership, folding, stabilization and collagen-binding roles are all captured (GO:0019797, GO:0032963, GO:0032991, GO:0006457, GO:0050821, GO:0005518). Falcon added only disease/ER-stress context (PMID:31171565, 38926541). Conclude: already captured.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review evidence is extensive and PubMed-verified (PMID:39245686 cryo-EM, 17277775, 19846465, 22615817, 15044469, 19088120). No bibliographic conflict or divergence.
- **Verdict:** Review excellent and PN-consistent; the group→GO:0032964 mapping is sound and correctly branched (contrast with the over-broad lectin "N-glycosylation system" node). No changes needed.

## Full Consistency Review

- **UniProt:** Q32P28 (prolyl 3-hydroxylase 1 / LEPRE1 / leprecan-1) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE, very thorough (full annotation set + detailed notes + Falcon).
- **PN placement:** `ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding` ; **PN-node mapping:** group "ER collagen processing and folding" mapped→GO:0032964 (collagen biosynthetic process, ok_for_propagation, more_specific_than_existing_goa); class/branch no_mapping.
- **Consistency:** Deep research ↔ review ↔ PN annotation fully consistent. P3H1 is correctly the catalytic core (procollagen-proline 3-dioxygenase, EC 1.14.11.7, GO:0019797) of the ER PCP complex (with CRTAP + PPIB), required for collagen helix folding/stability; loss causes recessive OI8. PN "ER collagen processing and folding" matches precisely.
- **PN story / NEW pressure:** No NEW GO pressure — catalytic, complex-membership, folding, stabilization and collagen-binding roles are all captured (GO:0019797, GO:0032963, GO:0032991, GO:0006457, GO:0050821, GO:0005518). Falcon added only disease/ER-stress context (PMID:31171565, 38926541). Conclude: already captured.
- **Mapping strategy:** Group→GO:0032964 (collagen biosynthetic process) is defensible and verified real via OLS. It is broader than the review's accepted GO:0032963 (collagen metabolic process) only in being a biosynthesis-specific child — appropriate for the collagen-folding group and `more_specific_than_existing_goa` is reasonable (P3H1's GOA carries GO:0032963 metabolic, not the biosynthetic child). Unlike the lectin group node, this projection is the right branch (collagen biogenesis) for P3H1. Status/scope OK.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review evidence is extensive and PubMed-verified (PMID:39245686 cryo-EM, 17277775, 19846465, 22615817, 15044469, 19088120). No bibliographic conflict or divergence.
- **Verdict:** Review excellent and PN-consistent; the group→GO:0032964 mapping is sound and correctly branched (contrast with the over-broad lectin "N-glycosylation system" node). No changes needed.
**Recommended edits:** None.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/P3H1/P3H1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: Q32P28
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
