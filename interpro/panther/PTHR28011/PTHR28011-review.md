# PANTHER Family Review: PTHR28011

## Family overview

| Property | Value |
|----------|-------|
| Family ID | PTHR28011 |
| Official family name | NON-CLASSICAL EXPORT PROTEIN 1 |
| InterPro entry | IPR024242 (NCE101) |
| Subfamily | PTHR28011:SF1, NON-CLASSICAL EXPORT PROTEIN 1 |
| Cached family size | 275 proteins across 729 taxon records; 1 subfamily |
| Reviewed representatives | *S. pombe* nce101 (C6Y4B6, 58 aa); *S. cerevisiae* NCE101 (Q02820, 53 aa) |
| PAINT source node | PTN001997334 |

PTHR28011 contains very small NCE101-family proteins. Cached PANTHER metadata places all
275 proteins in one subfamily and reports no experimental structure. The two reviewed
representatives share that subfamily, and both carry a predicted hydrophobic segment. No
molecular activity or interaction partner is known for either reviewed representative.
The similar names NCE102 and NCE103 refer to unrelated proteins recovered from the same
historical screen and must not be treated as paralogs or family members.

## IBA propagation assessment

| GO ID | Label | Aspect | Node | Action | Assessment |
|-------|-------|--------|------|--------|------------|
| GO:0009306 | protein secretion | BP | PTN001997334 | KEEP_AS_NON_CORE | The propagation remains inside the single NCE101 subfamily and there is no target-specific evidence of loss. However, the sole PAINT seed is *S. cerevisiae* NCE101; the OpenScientist database audit identifies its annotation as IGI from an overexpression screen for non-classical galectin-1 export (PMID:8655575). That study did not resolve whether the 53-aa product was export machinery, cargo, or an indirect modulator. The IBA is therefore a defensible phylogenetic context but not an experimentally established core function of *S. pombe* nce101. |

The short donor list is not itself a weakness, and the IBA is not a pairwise similarity
transfer. The limitation is biological: the ancestral node was seeded by an experimentally
indirect and mechanistically ambiguous descendant annotation. There is no evidence that
the *S. pombe* lineage lost an ancestral role, so removal would overstate the available
evidence; retaining the term as non-core preserves the PAINT judgment while exposing its
uncertainty.

## Review status

- **Date:** 2026-09-01
- **Status:** DRAFT
- **Basis:** PANTHER metadata and PAINT slice, UniProt, SCHPO nce101 GOA/review, and PMID:8655575
