# CFL1 review notes

## 2026-11-27

Reviewed CFL1 as part of the PTHR11913 ADF/cofilin family with DSTN and the
pre-existing CFL2 review.

- Core function: ubiquitous non-muscle cofilin that binds G-actin and F-actin
  and directly severs/depolymerizes actin filaments. The key direct human
  biochemical evidence is PMID:11812157.
- PAINT: the eukaryotic PANTHER node PTN000227258 soundly carries cytoplasm,
  actin cytoskeleton, actin filament binding and actin filament
  depolymerization. The Amniota PTN001375639 mitotic cytokinesis placement is
  treated as sound for CFL1. Plant polymerization and fungal cortical-actin
  placements are branch-specific and should not be used as human CFL1 evidence.
- Protein binding: rows naming ACTB, ACTG1 or ACTC1 were changed to actin
  binding. Non-actin GO:0005515 rows were either removed as generic binding
  when the cached source supported only a physical association, or left
  undecided when the exact high-throughput pair could not be traced from the
  cached publication text.
- Stress and nuclear rows: UniProt curates nucleus-matrix localization from
  PMID:15580268, and CFL1 can form nuclear actin rods under stress, but the
  cached paper is abstract-only and does not quote the nuclear-matrix assay.
  The TAS/IEA nuclear rows are therefore left UNDECIDED rather than removed.
- Stimulus and phenotype rows transferred from rodent Cfl1 were reviewed as
  context around phosphorylation-dependent cofilin regulation. Rows where the
  named process was too far upstream or downstream of CFL1's own actin-severing
  work were marked MARK_AS_OVER_ANNOTATED.
- Reactome R-HSA-8950581 records IL-12-dependent CFL1 expression in T cells
  and not a localization assay; the GO:0005829 cytosol TAS row is left
  UNDECIDED without opening a source defect.

No production GO-CAM in `gocams/index.tsv` centers on CFL1. Existing modules
mention cofilin in prose as an actin-remodeling effector, but PTHR11913 itself
does not form a standalone multi-part biological module.
