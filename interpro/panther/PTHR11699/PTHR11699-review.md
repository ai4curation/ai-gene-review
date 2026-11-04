# PANTHER Family Review: PTHR11699

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR11699 |
| **Family Name** | Aldehyde dehydrogenase |
| **Deep research source** | [PTHR11699-deep-research-falcon.md](PTHR11699-deep-research-falcon.md) |

## Falcon Deep Research Integration (2026-06-28)

**Source:** [PTHR11699-deep-research-falcon.md](PTHR11699-deep-research-falcon.md)

**Falcon verdict:** The absence of GO terms is appropriate because PTHR11699 is a broad, top-level ALDH family containing canonical enzymes, specialized semialdehyde dehydrogenases, fusion enzymes, multifunctional proteins, and pseudoenzymes. Any family-wide GO mapping would likely over-annotate at least some matched proteins (cuatlayotlolarte2023aldehydedehydrogenasediversity pages 1-2, brocker2013aldehydedehydrogenase(aldh) pages 14-18, liu2019crystalstructureof pages 11-13, heider2025thealdehydedehydrogenase pages 9-10). ACCEPT - retain no InterPro2GO mappings for PTHR11699; annotate only at more specific child/subfamily levels.

**Family-level synthesis:** The aldehyde dehydrogenase (ALDH) superfamily adopts a conserved three-domain architecture consisting of an N-terminal NAD(P)+-binding domain featuring a Rossmann fold, a catalytic domain of roughly equal size, and a smaller C-terminal oligomerization domain. Structural alignments across the superfamily reveal remarkably similar folds with RMSD values of 0.67-1.4 Å despite substantial sequence divergence.

**Curation use:** Use this Falcon report as support for conservative parent-family handling: keep broad parent mappings empty or minimal, and place specific GO functions on child entries, PAINT/PTN anchors, or representative members after manual review.

## Review Status

This free-text page is the legacy Falcon integration note. The authoritative review of
this family is the structured [PTHR11699-review.yaml](PTHR11699-review.yaml), whose
`review_status` is **COMPLETE** as of 2026-11-04: every (node, term) pair in
`PTHR11699-paint.tsv` carries a `node_assessment`, and the subfamilies, term assessments
and residue sites recorded there supersede anything stated here. The structured review
agrees with the Falcon verdict below that no family-wide GO mapping is safe.

- **Date**: 2026-06-28 (this page); 2026-11-04 (structured review)
- **Reviewer**: AI-assisted Falcon integration (this page); Claude (AI-assisted) for the structured review
- **Status**: superseded by the structured review, which is COMPLETE
- **Based on**: Falcon/Edison family deep research, local PANTHER metadata, and current InterPro2GO mapping context.
