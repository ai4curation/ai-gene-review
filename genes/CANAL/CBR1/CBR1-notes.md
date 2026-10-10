# CANAL CBR1 Notes

## 2026-10-10

- Seeded `CANAL/CBR1` with 19 current GOA rows and reviewed them against the
  `PTHR19370` PAINT cache.
- The C. albicans protein `Q59P03` is in `PTHR19370:SF184`, the CBR1-like
  NADH-cytochrome b5 reductase subfamily. PAINT places both
  `GO:0004128 cytochrome-b5 reductase activity, acting on NAD(P)H` and
  `GO:0005886 plasma membrane` on Saccharomycetales
  `PANTHER:PTN001064671`.
- The CBR1 activity IBA is phylogenetically sound and the broad NAD(P)H parent
  was kept as a non-core PAINT assertion. The Candida UniProt record already
  carries the exact RHEA-backed NADH-specific child, `GO:0090524`, so the
  non-PAINT `GO:0004128` transfers were changed to `MODIFY -> GO:0090524`.
- C. albicans CBR1 was identified in a plasma membrane proteomics experiment,
  but the local `PMID:19824013` cache is abstract-only and does not expose the
  protein table. Following CGD's direct curation, the IDA row is kept; the IBA
  seeded by the same CGD row is also kept as a non-core PAINT-supported
  localization.
- The yeast donor literature establishes that Cbr1 reduces Dph3 from NADH:
  PMID:27694803 reports, "we identified Saccharomyces cerevisiae cytochrome b5
  reductase (Cbr1) as a NADH-dependent reductase for Dph3." The same paper
  supports the tRNA wobble role because CBR1 deletion alone reduced mcm5s2U
  formation.
- `GO:0090560 2-(3-amino-3-carboxypropyl)histidine synthase activity` is the
  Dph1-Dph2 radical-SAM activity rather than CBR1's own reductase reaction.
  CBR1 provides electrons to Dph3 and can be a reductase component of the
  Dph1-Dph2-Dph3 complex; the row is therefore modified to a proposed
  `NADH-dependent Dph3 reductase activity` term for `RHEA:71231`.
- The S. cerevisiae literature places Cbr1 at both the ER and mitochondrial
  outer membrane, and PMID:10622712 shows that a fungal b5/b5R system can
  support C. albicans CYP51 in vitro. The current Candida GOA rows assert only
  plasma-membrane and mitochondrial outer-membrane localization, so this review
  leaves the inferred outer-membrane rows as non-core and records ER
  localization and sterol electron transfer as Candida-specific questions.
- Web searches for newer C. albicans-specific CBR1 literature found no direct
  re-characterization after the 2009 plasma membrane proteome. A 2015
  Xanthophyllomyces dendrorhous CBR study includes the C. albicans, S. pombe,
  S. cerevisiae, and N. crassa CBR1/CBR2 proteins in a fungal phylogeny, but it
  does not add direct evidence for Candida CBR1.
