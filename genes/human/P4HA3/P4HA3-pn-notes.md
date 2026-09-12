# P4HA3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q7Z4N8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/P4HA3/P4HA3-ai-review.yaml](P4HA3-ai-review.yaml)
- AIGR review HTML: missing - genes/human/P4HA3/P4HA3-ai-review.html
- Gene notes: present - [genes/human/P4HA3/P4HA3-notes.md](P4HA3-notes.md)
- GOA TSV: present - [genes/human/P4HA3/P4HA3-goa.tsv](P4HA3-goa.tsv)
- UniProt record: present - [genes/human/P4HA3/P4HA3-uniprot.txt](P4HA3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/P4HA3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/P4HA3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HA3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HA3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/P4HA3/P4HA3-deep-research-falcon.md](P4HA3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: P4HA3 (prolyl 4-hydroxylase subunit alpha-3) is the third catalytic alpha-subunit isoform of collagen prolyl 4-hydroxylase (C-P4H). The active enzyme is an alpha2-beta2 heterotetramer in which the two catalytic alpha subunits combine with two beta subunits that are identical to protein disulfide isomerase (PDI/P4HB). P4HA3 is an endoplasmic reticulum lumenal, Fe(II)- and 2-oxoglutarate-dependent dioxygenase that, using L-ascorbate as a cofactor and molecular oxygen as co-substrate, hydroxylates proline residues in -X-Pro-Gly- triplets of procollagen and related proteins to form trans-4-hydroxyproline (consuming 2-oxoglutarate and producing succinate and CO2). 4-hydroxyproline formation is essential for folding and thermal stability of the collagen triple helix. The alpha-3 isoenzyme has catalytic properties similar to the type I and type II C-P4Hs but with intermediate peptide-substrate binding properties, and its mRNA is expressed broadly but at much lower levels than the alpha(I)/alpha(II) isoforms, being most abundant in placenta, liver, and fetal skin and detectable in vascular smooth muscle and the fibrous cap of atherosclerotic lesions.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 4

## PN Consistency Summary

- **Consistency:** Consistent. Review, deep research, PN annotation, and mapping describe the third catalytic alpha-3 subunit of C-P4H (EC 1.14.11.2), [alpha(III)]2-beta2 tetramer with PDI, ER-lumenal; intermediate peptide-binding properties; broadly but weakly expressed. PN placement matches. EXP evidence (PMID:14500733) anchors the catalytic function.
- **PN story / NEW pressure:** PN asserts GO:0032964 as new_to_goa; P4HA3 GOA has no collagen-process BP term (only MF/CC). GO:0032964 verified real via OLS. Unlike P4HA1/P4HA2, this review has proposed_new_terms: [] — it did not flag the BP gap, so the PN projection actually adds a BP role the review omitted. The projection is nonetheless defensible (same catalytic logic as the paralogs) and consistent with the review's BP-free MF annotations. Conclusion: defensible ADD.
- **Evidence alignment:** PN dossier mapping-only. Review core: EXP PMID:14500733 (founding characterization), reviews PMID:34009234. Numerous cancer-biomarker refs (PMID:36588128, 39362976, 39504328, 39394821) beyond PN scope — expected divergence. Core biochemistry aligns.
- **Verdict:** Consistent; PN GO:0032964 ADD defensible and genuinely new to GOA; minor note that this review omitted the BP-gap proposal its paralogs made.

## Full Consistency Review

- **UniProt:** Q7Z4N8 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO=GO:0032964 collagen biosynthetic process (class/branch=no_mapping). Projection goa_status=new_to_goa.
- **Consistency:** Consistent. Review, deep research, PN annotation, and mapping describe the third catalytic alpha-3 subunit of C-P4H (EC 1.14.11.2), [alpha(III)]2-beta2 tetramer with PDI, ER-lumenal; intermediate peptide-binding properties; broadly but weakly expressed. PN placement matches. EXP evidence (PMID:14500733) anchors the catalytic function.
- **PN story / NEW pressure:** PN asserts GO:0032964 as new_to_goa; P4HA3 GOA has no collagen-process BP term (only MF/CC). GO:0032964 verified real via OLS. Unlike P4HA1/P4HA2, this review has proposed_new_terms: [] — it did not flag the BP gap, so the PN projection actually adds a BP role the review omitted. The projection is nonetheless defensible (same catalytic logic as the paralogs) and consistent with the review's BP-free MF annotations. Conclusion: defensible ADD.
- **Mapping strategy:** Correct. Catalytic subunit; group-level GO:0032964 appropriate, narrower than unmapped class. No node change. For paralog-uniformity, the review's empty proposed_new_terms is a minor inconsistency vs P4HA1/P4HA2 (which propose GO:0018401/GO:0032964).
- **Evidence alignment:** PN dossier mapping-only. Review core: EXP PMID:14500733 (founding characterization), reviews PMID:34009234. Numerous cancer-biomarker refs (PMID:36588128, 39362976, 39504328, 39394821) beyond PN scope — expected divergence. Core biochemistry aligns.
- **Verdict:** Consistent; PN GO:0032964 ADD defensible and genuinely new to GOA; minor note that this review omitted the BP-gap proposal its paralogs made.
- **Recommended edits:** [YAML] Consider adding a peptidyl-proline-hydroxylation / collagen-biosynthetic-process entry to P4HA3 proposed_new_terms (GO:0018401 / GO:0032964) for parity with P4HA1/P4HA2 and to match the PN projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/P4HA3/P4HA3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: Q7Z4N8
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
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
