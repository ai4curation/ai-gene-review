# SERPINH1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P50454
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SERPINH1/SERPINH1-ai-review.yaml](SERPINH1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SERPINH1/SERPINH1-ai-review.html](SERPINH1-ai-review.html)
- Gene notes: present - [genes/human/SERPINH1/SERPINH1-notes.md](SERPINH1-notes.md)
- GOA TSV: present - [genes/human/SERPINH1/SERPINH1-goa.tsv](SERPINH1-goa.tsv)
- UniProt record: present - [genes/human/SERPINH1/SERPINH1-uniprot.txt](SERPINH1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SERPINH1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SERPINH1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SERPINH1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SERPINH1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: SERPINH1 (Serpin H1, better known as HSP47, also called colligin / gp46) is an endoplasmic reticulum-resident, collagen-specific molecular chaperone. Although it belongs to the serpin superfamily by fold, it is non-inhibitory and does not act as a protease inhibitor. In the ER lumen HSP47 binds specifically to the folded triple-helical region of procollagen, stabilizing the nascent triple helix, preventing local unfolding and premature aggregation, and serving as a quality-control factor in collagen biosynthesis. HSP47 accompanies procollagen from the ER to the ER-Golgi intermediate compartment/cis-Golgi, where the lower pH triggers its release; it then recycles back to the ER through its C-terminal RDEL retrieval signal. It is heat-shock inducible. Loss-of-function variants cause autosomal-recessive osteogenesis imperfecta type X (OI10), underscoring its essential role in collagen maturation.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 5

## PN Consistency Summary

- **Consistency:** Strong. Review, notes and PN all describe HSP47 as an ER-resident, collagen-specific (non-inhibitory serpin) chaperone that binds the triple-helical procollagen region. Core MFs = collagen binding (GO:0005518) and protein folding chaperone (GO:0044183), in ER lumen/ERGIC. Review correctly MARKS_AS_OVER_ANNOTATED the inherited serpin protease-inhibitor activity. Fully consistent with the PN collagen-folding node.
- **PN story / NEW pressure:** PN asserts collagen biosynthetic process (GO:0032964, OLS-verified real, goa_status=new_to_goa — GOA confirms only GO:0030199 collagen fibril organization present, not GO:0032964). HSP47 is genuinely dedicated to collagen maturation (OI10 disease confirms essentiality), so a collagen-process BP is defensible. The review already has GO:0030199 (collagen fibril organization, KEEP_AS_NON_CORE) as its process annotation. GO:0032964 is a reasonable, slightly more upstream alternative/addition. Conclude: **ADD defensible but largely already captured** by GO:0030199 — marginal value.
- **Evidence alignment:** PN row carries no reference titles; review cites UniProt + collagen-chaperone literature. No conflict.
- **Verdict:** Consistent and high-quality. **Recommended edits:** optionally add GO:0032964 collagen biosynthetic process (KEEP_AS_NON_CORE) to align with PN, since it captures HSP47's ER-upstream role better than the existing GO:0030199 fibril-organization term [YAML]; otherwise no change.

## Full Consistency Review

- **UniProt:** P50454 (HSP47) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding` ; **PN-node mapping:** mapped → GO:0032964 (collagen biosynthetic process, new_to_goa)
- **Consistency:** Strong. Review, notes and PN all describe HSP47 as an ER-resident, collagen-specific (non-inhibitory serpin) chaperone that binds the triple-helical procollagen region. Core MFs = collagen binding (GO:0005518) and protein folding chaperone (GO:0044183), in ER lumen/ERGIC. Review correctly MARKS_AS_OVER_ANNOTATED the inherited serpin protease-inhibitor activity. Fully consistent with the PN collagen-folding node.
- **PN story / NEW pressure:** PN asserts collagen biosynthetic process (GO:0032964, OLS-verified real, goa_status=new_to_goa — GOA confirms only GO:0030199 collagen fibril organization present, not GO:0032964). HSP47 is genuinely dedicated to collagen maturation (OI10 disease confirms essentiality), so a collagen-process BP is defensible. The review already has GO:0030199 (collagen fibril organization, KEEP_AS_NON_CORE) as its process annotation. GO:0032964 is a reasonable, slightly more upstream alternative/addition. Conclude: **ADD defensible but largely already captured** by GO:0030199 — marginal value.
- **Mapping strategy:** Single clean node; status=mapped scope=ok is appropriate. GO:0032964 is neither broader nor narrower than the review's GO:0030199 (sibling process emphasising biosynthesis vs extracellular fibril assembly); HSP47 acts upstream in the ER, so GO:0032964 arguably fits HSP47's ER role better than fibril organization. No mapping change needed.
- **Evidence alignment:** PN row carries no reference titles; review cites UniProt + collagen-chaperone literature. No conflict.
- **Verdict:** Consistent and high-quality. **Recommended edits:** optionally add GO:0032964 collagen biosynthetic process (KEEP_AS_NON_CORE) to align with PN, since it captures HSP47's ER-upstream role better than the existing GO:0030199 fibril-organization term [YAML]; otherwise no change.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/SERPINH1/SERPINH1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: P50454
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
