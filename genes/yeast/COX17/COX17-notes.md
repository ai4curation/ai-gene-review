# COX17 curation notes

## 2026-10-01 current-GOA and IBA re-review

Reviewed *Saccharomyces cerevisiae* **COX17/YLL009C** after a current GOA/UniProt
refresh. Cox17 is the core mitochondrial intermembrane-space copper chaperone that
donates copper to both Sco1 and Cox11 for cytochrome c oxidase assembly. The
refreshed GOA did not seed new review rows; it de-duplicated two exact duplicate
GOA source lines and backfilled exact PAINT, InterPro and UniProt-SubCell
supporting entities on the existing automated rows.

### IBA / PAINT review

All three IBA rows point to a single node in `PTHR16719-paint.tsv`:

- `PANTHER:PTN000423136 -> GO:0005758 mitochondrial intermembrane space`, seeded
  by yeast, mouse and human COX17.
- `PANTHER:PTN000423136 -> GO:0033617 mitochondrial respiratory chain complex IV
  assembly`, seeded by yeast, mouse and human COX17.
- `PANTHER:PTN000423136 -> GO:0016531 copper chaperone activity`, seeded by yeast,
  pig and human COX17.

All three transfers are sound. COX17 itself in the `WITH/FROM` is target evidence
that PAINT used to place the ancestral IBD, not a circular propagation. The node is
the narrow COX17 copper-chaperone family, and the target has direct experimental
evidence for the transferred molecular function, process and IMS localization.

### Literature checked

Cached publications were sufficient for the existing rows:

- PMID:15199057: direct in vitro copper transfer from Cox17 to both Sco1 and
  Cox11; source of the copper chaperone activity and copper transport rows.
- PMID:15465825 and PMID:9585572: independent biochemical support for Cu(I)
  binding and cuprous-thiolate cluster formation.
- PMIDs 8662933 and 9407107: original COX17 characterization, cytochrome oxidase
  assembly phenotype, and dual cytosol/IMS localization.
- PMID:22984289: Bax-release IMS proteomics supporting IMS localization.
- PMID:8078902: verified as a COX10/heme A:farnesyltransferase paper that does
  not support the MGI COX17 rows.

A 2024-2026 search found newer papers that mention COX17 in human disease or
other copper-pathway contexts, plus a 2025 characterization of Trypanosoma Cox17,
but no newer yeast COX17 primary study that changes these calls.

Followed up on PR #3733 by changing the PMID:8078902-backed `GO:0005739
mitochondrion` row from `KEEP_AS_NON_CORE` to `REMOVE`: the term is true for
Cox17, but the row's COX10 reference makes the evidence chain invalid, and
GO:0005739 is independently retained through the two HDA rows.
