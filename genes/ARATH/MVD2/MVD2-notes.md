# MVD2 (At3g54250, F4JCU3) notes

## Identity

- UniProt F4JCU3 (MVD2_ARATH), name MVD2 (ECO:0000305); synonym MDD2 (Henry 2015). The TAIR
  cross-reference on the UniProt record gives the TAIR symbol as **MDD2** (`TAIR; AT3G54250; MDD2.`);
  NCBI Gene 824592 has no symbol. Folder `genes/ARATH/MVD2` as assigned by the coordinator; the
  TAIR symbol discrepancy is reported back rather than acted on.
- 419 aa, 89% identical to MVD1 over a global alignment (computed with the PMK-bioinformatics
  aligner). PTHR10977:SF3, TIGR01240, IPR029765. UniProt flags the older EMBL model CAB70999.1 as an
  erroneous gene model; the current model is fine.

## Literature search (2026-11-18)

Same PubMed queries as for MVD1 and PMK (see those notes); only Henry et al. 2015 (PMID:26216978)
reports experimental data on MVD2. No localisation, mutant or expression study of MVD2 was found.
Henry 2015 full text could not be retrieved (PNAS blocks PMC XML; Europe PMC 500), and its abstract
does not mention the MDDs.

## Activity

- UniProt (ECO:0000269, PMID:26216978): specific for MVAPP; Km 26 uM and kcat 3.2 s-1 for MVAPP,
  Km 4600 uM and kcat 0.034 s-1 for MVAP. MVAPP constants are identical to those UniProt lists for
  MVD1 from the same paper (possible but not checkable).
- MVAP decarboxylation is 10,000-fold less efficient: noise-level, not annotated.

## Localisation

- No experiment on MVD2. UniProt's peroxisome location and PTS2 motif are by similarity to MVD1
  (ECO:0000250). The 40-48 segment is identical to MVD1's (SVTLDPDHL) and is not a consensus PTS2
  (`genes/ARATH/PMK/PMK-bioinformatics/RESULTS.md`). Given 89% identity with MVD1, the same targeting
  behaviour is the likely default, but it is untested; the Simkin 2011 abstract does not even say
  which paralog was fused.
- Nucleus ISM (AtSubP) has no support: MARK_AS_OVER_ANNOTATED, as for other AtSubP nucleus rows in
  the corpus.
- MVD2 is absent from the Aryal 2014 cytosolic-fraction proteome (absence uninformative).

## IBA / PAINT

- PTN000104601 MF IBD lists AT3G54250 among its seeds (its IDA from Henry 2015); sound.
- BP IBD seeds do not include AT3G54250; the inheritance is sound (MVD2 performs the same step).
- Cytosol IBD seeded by human and mouse MVD only; for the plant clade it conflicts with the
  peroxisomal plant data, as for MVD1. `just paint-losses ARATH MVD2`: no loss on the lineage.
