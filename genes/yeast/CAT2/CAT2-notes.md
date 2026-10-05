# CAT2 curation notes

## 2026-10-01 update: GOA refresh, PTHR22589 IBA review, and YeastPathways rows

- Force-refreshed CAT2 from QuickGO and UniProt. The current GOA snapshot has
  20 live rows; five missing live assertions were seeded into the review, and
  five stale source rows were preserved with `retired: true`.
- Re-read the cached PTHR22589 PAINT export. All four CAT2 IBA rows trace to
  `PANTHER:PTN001097241`, the fungal Cat2/CRAT node, and all four are sound
  transfers: carnitine O-acetyltransferase activity, mitochondrion, peroxisome,
  and carnitine metabolic process. Budding yeast CAT2 itself appears among the
  descendant evidence, which is expected target-as-seed grounding rather than
  circular support.
- Resolved the newly imported YeastPathways `GO_REF:0000123` rows from the
  carnitine-shuttle GO-CAM. The RCA molecular-function and carnitine-shuttle
  process rows are consistent with Cat2's reversible acetyl transfer between
  acetyl-CoA and carnitine. The RCA `GO:0005829 cytosol` row was removed as an
  import artifact from an aggregate carnitine O-acetyltransferase reaction:
  endogenous Cat2 is mitochondrial/peroxisomal, while the cytosolic arm of the
  yeast shuttle is better represented by Yat2 in the pathway model.
- The UniProt/QuickGO refresh also restored a 1995 primary peroxisome-localization
  annotation from PMID:7628448. The paper is abstract-only in the cache, but the
  abstract directly states that yeast carnitine acetyltransferase is present in
  both mitochondria and peroxisomes.
- Searched for newer Cat2 literature. PMID:38377076 directly tested Cat2 in a
  2024 dual-targeting/PerMit overexpression assay and supports the established
  mitochondrial/peroxisomal targeting framework, but it does not justify a new
  endogenous tethering-process annotation for CAT2.
- Changed the retired IntAct `GO:0005515 protein binding` row from the legacy
  `MARK_AS_OVER_ANNOTATED` action to `REMOVE`, because the cross-species
  two-hybrid screen does not establish an informative physiologic binding
  activity for the yeast enzyme.
