# CANAL CBR1 Notes

## 2026-10-10

- Seeded `CANAL/CBR1` with 19 current GOA rows and reviewed them against the
  `PTHR19370` PAINT cache.
- The C. albicans protein `Q59P03` is in `PTHR19370:SF184`, the CBR1-like
  NADH-cytochrome b5 reductase subfamily. PAINT places both
  `GO:0004128 cytochrome-b5 reductase activity, acting on NAD(P)H` and
  `GO:0005886 plasma membrane` on `PANTHER:PTN001064671`.
- The CBR1 activity IBA is phylogenetically sound, but the propagated term is
  a NAD(P)H parent. The Candida UniProt record already carries the exact
  RHEA-backed NADH-specific child, `GO:0090524`, so the CBR1-family
  `GO:0004128` rows were changed to `MODIFY -> GO:0090524`.
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
  Dph1-Dph2 radical-SAM activity, not CBR1's reductase activity. CBR1 provides
  electrons to Dph3, and Dph3 feeds Dph1-Dph2; the row is therefore modified to
  a proposed `NADH-dependent Dph3 reductase activity` term for `RHEA:71231`.
- Web searches for newer C. albicans-specific CBR1 literature found no direct
  re-characterization after the 2009 plasma membrane proteome. A 2015
  Xanthophyllomyces dendrorhous CBR study includes the C. albicans, S. pombe,
  S. cerevisiae, and N. crassa CBR1/CBR2 proteins in a fungal phylogeny, but it
  does not add direct evidence for Candida CBR1.
