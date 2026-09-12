# P4HA1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P13674
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/P4HA1/P4HA1-ai-review.yaml](P4HA1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/P4HA1/P4HA1-ai-review.html
- Gene notes: present - [genes/human/P4HA1/P4HA1-notes.md](P4HA1-notes.md)
- GOA TSV: present - [genes/human/P4HA1/P4HA1-goa.tsv](P4HA1-goa.tsv)
- UniProt record: present - [genes/human/P4HA1/P4HA1-uniprot.txt](P4HA1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/P4HA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/P4HA1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HA1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/P4HA1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/P4HA1/P4HA1-deep-research-falcon.md](P4HA1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: P4HA1 is the catalytic alpha-1 subunit of collagen prolyl 4-hydroxylase (C-P4H; EC 1.14.11.2), an endoplasmic reticulum-lumenal, Fe(II)- and 2-oxoglutarate-dependent dioxygenase. The active enzyme is an alpha2-beta2 heterotetramer in which the beta subunit is P4HB (protein disulfide-isomerase, PDI); the two catalytic alpha subunits provide the peptide-substrate-binding and Fe2OG dioxygenase domains, while P4HB acts as a structural subunit and retains the tetramer in the ER lumen through its C-terminal KDEL sequence (the alpha subunit lacks a retention signal). C-P4H catalyzes the post-translational formation of trans-4-hydroxy-L-proline from proline residues in -Xaa-Pro-Gly- sequences of procollagen and other proteins, consuming O2 and 2-oxoglutarate (which is decarboxylated to succinate and CO2) and requiring ascorbate (vitamin C) to maintain the active-site iron in the reduced state. 4-Hydroxyproline is essential for the thermal stability of the collagen triple helix, making this the key rate-limiting modification in collagen maturation and a central enzyme of collagen biosynthesis. Two enzyme isotypes exist (type I, with P4HA1, and type II, with the paralog P4HA2); the alpha-1 and alpha-2 subunits do not form mixed tetramers. P4HA1 is broadly expressed, with highest levels in collagen-producing tissues.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent. Review, deep research, PN annotation, and mapping all describe the catalytic alpha-1 subunit of collagen prolyl 4-hydroxylase (C-P4H, EC 1.14.11.2), the alpha2-beta2 heterotetramer with P4HB/PDI, ER-lumenal. PN "collagen processing/folding" placement matches the rate-limiting 4-Hyp modification that stabilizes the triple helix.
- **PN story / NEW pressure:** PN asserts collagen biosynthetic process (GO:0032964) as new_to_goa — and indeed P4HA1 GOA has NO collagen-process BP term (only GO:0030199 collagen fibril organization, kept non-core). The review independently flags this gap in proposed_new_terms, recommending GO:0018401 peptidyl-proline hydroxylation to 4-hydroxy-L-proline / GO:0032964. Both GO:0032964 and GO:0018401 verified real via OLS. Conclusion: genuine ADD; PN projection and review agree a BP term is missing. GO:0018401 (direct catalytic BP) is arguably more precise than GO:0032964, but GO:0032964 is the better cross-gene PN-group term.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review core evidence: IDA PMID:9211872, TAS PMID:2543975 (cloning), structural PMID:24207127. Review adds many cancer/fibrosis refs (PMID:39568592, 38907027, 35368589 MBL substrate, etc.) absent from PN — expected divergence; PN focuses on canonical collagen biochemistry, review on full functional literature. Core biochemistry aligns.
- **Verdict:** Consistent; PN GO:0032964 ADD is genuinely new to GOA and corroborated by the review's own proposed_new_terms (BP gap real).

## Full Consistency Review

- **UniProt:** P13674 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO=GO:0032964 collagen biosynthetic process (class/branch=no_mapping). Projection goa_status=new_to_goa.
- **Consistency:** Consistent. Review, deep research, PN annotation, and mapping all describe the catalytic alpha-1 subunit of collagen prolyl 4-hydroxylase (C-P4H, EC 1.14.11.2), the alpha2-beta2 heterotetramer with P4HB/PDI, ER-lumenal. PN "collagen processing/folding" placement matches the rate-limiting 4-Hyp modification that stabilizes the triple helix.
- **PN story / NEW pressure:** PN asserts collagen biosynthetic process (GO:0032964) as new_to_goa — and indeed P4HA1 GOA has NO collagen-process BP term (only GO:0030199 collagen fibril organization, kept non-core). The review independently flags this gap in proposed_new_terms, recommending GO:0018401 peptidyl-proline hydroxylation to 4-hydroxy-L-proline / GO:0032964. Both GO:0032964 and GO:0018401 verified real via OLS. Conclusion: genuine ADD; PN projection and review agree a BP term is missing. GO:0018401 (direct catalytic BP) is arguably more precise than GO:0032964, but GO:0032964 is the better cross-gene PN-group term.
- **Mapping strategy:** Correct. Catalytic subunit; group-level GO:0032964 is appropriate and not over-broad (it is narrower than the unmapped parent class). No change to node needed.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review core evidence: IDA PMID:9211872, TAS PMID:2543975 (cloning), structural PMID:24207127. Review adds many cancer/fibrosis refs (PMID:39568592, 38907027, 35368589 MBL substrate, etc.) absent from PN — expected divergence; PN focuses on canonical collagen biochemistry, review on full functional literature. Core biochemistry aligns.
- **Verdict:** Consistent; PN GO:0032964 ADD is genuinely new to GOA and corroborated by the review's own proposed_new_terms (BP gap real).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/P4HA1/P4HA1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: P13674
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
