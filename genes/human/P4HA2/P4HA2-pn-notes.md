# P4HA2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O15460
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/P4HA2/P4HA2-ai-review.yaml](P4HA2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/P4HA2/P4HA2-ai-review.html
- Gene notes: present - [genes/human/P4HA2/P4HA2-notes.md](P4HA2-notes.md)
- GOA TSV: present - [genes/human/P4HA2/P4HA2-goa.tsv](P4HA2-goa.tsv)
- UniProt record: present - [genes/human/P4HA2/P4HA2-uniprot.txt](P4HA2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/P4HA2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/P4HA2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HA2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HA2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/P4HA2/P4HA2-deep-research-falcon.md](P4HA2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: P4HA2 (prolyl 4-hydroxylase subunit alpha-2) is one of three catalytic alpha-subunit isoforms of collagen prolyl 4-hydroxylase (C-P4H), an endoplasmic reticulum-lumenal enzyme. The active enzyme is an alpha2-beta2 heterotetramer in which the beta subunit is P4HB (protein disulfide isomerase, PDI) acting as a structural and ER-retention subunit; the two alpha-2 chains carry the catalytic sites. As a 2-oxoglutarate- and Fe(II)-dependent dioxygenase, P4HA2 catalyzes the post-translational formation of trans-4-hydroxy-L-proline in -Xaa-Pro-Gly- sequences of procollagen (and other proteins), consuming 2-oxoglutarate and O2 and producing succinate and CO2. 4-Hydroxyproline is essential for the folding and thermal stability of the collagen triple helix. The active-site iron is coordinated by a 2-His-1-carboxylate facial triad, and L-ascorbate (vitamin C) is required as a cofactor to maintain the iron in the reduced Fe(II) state. The type II tetramer contributes a substantial fraction of total prolyl 4-hydroxylase activity in human cells, is expressed in heart, placenta, lung and pancreas, and does not co-assemble with the type I (P4HA1) alpha subunit into mixed tetramers. Variants in P4HA2 cause autosomal dominant nonsyndromic high myopia (MYP25), consistent with a role in scleral collagen and extracellular matrix.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review, deep research, PN annotation, and mapping describe the type II catalytic alpha-2 subunit of C-P4H (EC 1.14.11.2), alpha2-beta2 with P4HB, ER-lumenal; collagen 4-Hyp formation for triple-helix stability. PN placement matches. The review additionally surfaces non-canonical substrates (mTOR Pro2341 hydroxylation PMID:38654109; SUFU PMID:38909089) flagged non-core pending confirmation — these do not contradict the PN canonical-collagen placement.
- **PN story / NEW pressure:** PN asserts GO:0032964 as new_to_goa; P4HA2 GOA has NO BP term at all (verified via goa.tsv). The review's proposed_new_terms explicitly recommends adding GO:0019471/GO:0018401/GO:0032964. GO:0032964 and GO:0018401 verified real via OLS. Conclusion: genuine ADD, fully corroborated by the review. Defensible.
- **Evidence alignment:** PN dossier mapping-only. Review core: IDA/TAS PMID:9211872 (type II tetramer characterization), authoritative review PMID:32969070. Many cancer/non-canonical-substrate refs (PMID:38654109, 38909089, 38857058, 41096640) are beyond the PN canonical-biochemistry scope — expected divergence. Core collagen biochemistry aligns.
- **Verdict:** Consistent; PN GO:0032964 ADD genuinely new to GOA and matches the review's own proposed BP terms (BP gap real).

## Full Consistency Review

- **UniProt:** O15460 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO=GO:0032964 collagen biosynthetic process (class/branch=no_mapping). Projection goa_status=new_to_goa.
- **Consistency:** Consistent. Review, deep research, PN annotation, and mapping describe the type II catalytic alpha-2 subunit of C-P4H (EC 1.14.11.2), alpha2-beta2 with P4HB, ER-lumenal; collagen 4-Hyp formation for triple-helix stability. PN placement matches. The review additionally surfaces non-canonical substrates (mTOR Pro2341 hydroxylation PMID:38654109; SUFU PMID:38909089) flagged non-core pending confirmation — these do not contradict the PN canonical-collagen placement.
- **PN story / NEW pressure:** PN asserts GO:0032964 as new_to_goa; P4HA2 GOA has NO BP term at all (verified via goa.tsv). The review's proposed_new_terms explicitly recommends adding GO:0019471/GO:0018401/GO:0032964. GO:0032964 and GO:0018401 verified real via OLS. Conclusion: genuine ADD, fully corroborated by the review. Defensible.
- **Mapping strategy:** Correct. Catalytic subunit; group-level GO:0032964 appropriate, narrower than the unmapped class node. No node change required. (Note GO:0009055 electron transfer activity in GOA was MARK_AS_OVER_ANNOTATED in the review — unrelated to the PN MF/BP projection.)
- **Evidence alignment:** PN dossier mapping-only. Review core: IDA/TAS PMID:9211872 (type II tetramer characterization), authoritative review PMID:32969070. Many cancer/non-canonical-substrate refs (PMID:38654109, 38909089, 38857058, 41096640) are beyond the PN canonical-biochemistry scope — expected divergence. Core collagen biochemistry aligns.
- **Verdict:** Consistent; PN GO:0032964 ADD genuinely new to GOA and matches the review's own proposed BP terms (BP gap real).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/P4HA2/P4HA2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: O15460
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
