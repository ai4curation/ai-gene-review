# CRYAB Gene Review Notes

## 2026-05-30 - PROTEOSTASIS PN small-HSP positive-control pass

Full review is present and marked complete. The local review supports CRYAB/HSPB5 as a small heat-shock-protein molecular chaperone with holdase activity. It modifies `GO:0051082 unfolded protein binding` to `GO:0140309 unfolded protein carrier activity` and treats `GO:0042026 protein refolding` as an imprecise foldase-style term for CRYAB biology. [file:human/CRYAB/CRYAB-ai-review.yaml; PMID:16303126; PMID:12235146]

PN curation conclusion: the PN small-HSP placements are appropriate, including cytonuclear and stress-context branches. The same caution as CRYAA applies: PN-derived chaperone propagation is valid at the small-HSP/holdase level, but should not erase the distinction between ATP-independent holdase activity and ATP-dependent protein refolding.

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Row: GO:0005739 IEA GO_REF:0000107 (Ensembl projection from mouse P23927). No sub-compartment
rows. Existing KEEP_AS_NON_CORE kept; added missing `qualifier: located_in` (as in GOA).

- Source check (QuickGO, 2026-10-25): mouse P23927 has one GO:0005739 row, IDA PMID:18191123
  (MGI). PMID:18191123 (fetched; full text) did the mitochondrial experiment in human ARPE-19
  cells: "A decrease in ARPE-19 total and cytosolic alphaB-crystallin expression with
  increasing CoCl(2) treatment and an increase in mitochondrial alphaB-crystallin were found."
  So the projection to human restates a human-cell observation, made on a mouse record.
- The mitochondrial fraction is a crude pellet; purity markers are named only for the
  nuclear/cytosolic split ("The purity of the fractions was checked by Western blot analysis
  with an antibody against histone H1"), no ER marker -> cannot separate from MAM (STOM lesson).
- Kept as a stress-induced, non-core pool (consistent with the anti-apoptotic literature
  summarized in the deep research: cytochrome c and VDAC interactions, Wang 2024 JCI Insight,
  not cached here).
- Rule 4: stay at root; soluble sHSP, no presequence or TM, no sub-mitochondrial assay.
- No is_active_in rows.
