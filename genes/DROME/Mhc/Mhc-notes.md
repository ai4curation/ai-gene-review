# Mhc review notes

- UniProt P05661 (MYSA_DROME), FBgn0264695; fetched with `just fetch-gene DROME Mhc`; 48 GOA rows.
- No deep-research provider; literature summary in `Mhc-deep-research-manual.md`.
- Full text read: PMID:15051736, PMID:21680742, PMID:22496423, PMID:24915196, PMID:28973424,
  PMID:17603108, PMID:26896675 (Mhc-GFP fTRG lines). Abstract only: PMID:8995523, PMID:8887536,
  PMID:12927543, PMID:15075240, PMID:16154586, PMID:18462751, PMID:16297904, PMID:16580994,
  PMID:10471711, PMID:17546092, PMID:18199432, PMID:38944040.

## Decisions worth flagging

- GO:0005703 polytene chromosome puff (IDA, PMID:10471711): UNDECIDED. Abstract is an EMS
  flight-muscle screen and says the nearby complementation groups "are shown to be in different
  loci"; full text not retrievable. Looks like a cytological-map statement rather than protein
  localization, but I cannot see the curator's evidence.
- GO:0050821 protein stabilization (IMP, PMID:22496423): MARK_AS_OVER_ANNOTATED. The paper
  shows the E701K mutation makes myosin itself less stable and aggregation-prone
  ["To our knowledge, this is the first direct structural evidence of altered myosin stability
  resulting from an SH1-SH2 mutation."]; that is the mutant protein's own stability, not
  Mhc stabilizing another protein.
- GO:0071689 muscle thin filament assembly (IMP, PMID:24915196): MARK_AS_OVER_ANNOTATED. Adult
  RNAi lengthens thin filaments; myosin influences thin-filament length indirectly; Mhc does not
  assemble thin filaments.
- GO:0043520 regulation of myosin II filament assembly (IDA, PMID:28973424): MODIFY to
  GO:0071688 striated muscle myosin thick filament assembly; the assay is self-assembly of the
  MHC rod itself, i.e. participation, not regulation.
- GO:0042692 muscle cell differentiation (IMP, PMID:16297904): MARK_AS_OVER_ANNOTATED; MHC is
  a product of differentiation (expression reduced in CanB2 mutants).
- MRP (myosin rod protein) is a product of the Mhc locus (internal promoter), so PMID:8995523
  and PMID:12927543 evidence on MRP applies to the gene product family under this accession,
  though P05661 isoforms listed by UniProt are the full-length MHCs.

## No NEW terms

Considered adding GO:0005859 muscle myosin complex and GO:0071688 thick-filament assembly as
NEW; both are instead reached as MODIFY replacements of existing rows, so no NEW rows needed.
