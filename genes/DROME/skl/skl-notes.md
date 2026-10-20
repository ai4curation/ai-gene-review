# skl notes

## 2026-09-30

- Reviewed Drosophila `skl` as the fourth Reaper/Hid/Grim-region IAP antagonist
  comparator for the APOPTOSIS project.
- Centered the review on Sickle's N-terminal IAP-binding motif. Srinivasula et
  al. showed that Sickle binds DIAP1 and DIAP2 BIR domains, that deleting or
  mutating the N-terminal IBM disrupts IAP binding and caspase-promoting
  activity, and that Sickle relieves IAP inhibition of Dcp-1 and human caspases.
- Added a conservative new `GO:1990525 BIR domain binding` row from the direct
  DIAP1/DIAP2 binding and DIAP1-BIR2 structural evidence in PMID:11818063,
  because the seeded Sickle GOA rows contained only biological-process terms.
- Narrowed the experimental generic `GO:0006915 apoptotic process` rows to
  `GO:0097190 apoptotic signaling pathway`. The sources support Sickle acting
  upstream of caspase execution as an RHG-family IAP antagonist, often
  potentiating Grim, Reaper, or Hid, rather than performing the execution-phase
  proteolysis itself.
- Kept the corazonergic-neuron
  `GO:0010623 programmed cell death involved in cell development` row as
  non-core: the full-text genetic data support a minor role for `skl`, with
  `grim` as the dominant death gene and `skl` as a backup trigger in that
  developmental context.
- Left both the DOI-only Trends in Genetics NAS row and the ionizing-radiation
  row `UNDECIDED`. Sickle is clearly an apoptotic signaling protein, but that
  specific review source is not cached; the cached Christich et al. abstract
  proves genotoxic induction of `skl`, not a direct Sickle protein role in a
  specific ionizing-radiation response.
