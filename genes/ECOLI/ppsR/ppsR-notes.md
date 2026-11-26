# ppsR (P0A8A4) notes

## Literature search (2026-11-24)

- PubMed `phosphoenolpyruvate synthase regulatory protein Escherichia coli` (7 hits;
  only PMID:20044937 is about PpsR/PSRP; the others concern PEP synthase or unrelated
  topics). `DUF299 PEP synthetase regulatory protein phosphorylation` and
  `ppsR Escherichia coli PEP synthetase regulation threonine` returned 0 hits.
- GOA references: PMID:20044937 (full text cached), PMID:15911532 (proteome
  localisation, abstract-only), PMID:15690043 (interaction screen).
- No deep-research provider file was generated. The E. coli protein has one primary
  biochemical paper (Burnell 2010); mechanistic detail (Thr phosphorylation, PPi
  product) is inferred from the maize PDRP homolog.

## Findings

- E. coli DUF299 (PpsR/PSRP) catalyses ADP-dependent inactivation and Pi-dependent
  activation of PEP synthase (PEPS) [PMID:20044937 "establishes that E. coli DUF299
  catalyzes both the ADP-dependent inactivation and the Pi-dependent activation of
  PEPS."].
- Bifunctional ADP-dependent kinase / Pi-dependent pyrophosphorylase [PMID:20044937
  "first report of a bifunctional regulatory enzyme catalysing an ADP-dependent
  phosphorylation and a Pi-dependent pyrophosphorylation reaction in bacteria"].
- Native PSRP is a tetramer (gel filtration). Inactivation needs the catalytic His of
  PEPS to be phosphorylated (pyruvate inhibits inactivation); the regulatory residue is
  a Thr next to the catalytic His (scheme, by analogy with PPDK/PDRP).
- The assays are PEPS activity assays; PPi formation and phospho-Thr were not measured
  directly for the E. coli enzyme.

## Staged RHEA rows

- RHEA:48580 ([PEPS]-phosphate + Pi + H+ = PEPS + PPi; EC 2.7.4.28) -> broadMatch
  GO:0016776. The reactivation consumes Pi, not water, and is a phosphoryl transfer to
  phosphate: GO:0016776 is the right class and the hydrolase GO:0004721 (on the IBA row)
  is the wrong one. The GOA UniRule row on GO:0016776 is ACCEPTed, so the row is backed.
- RHEA:46020 (ADP-dependent PEPS kinase; EC 2.7.11.33) -> broadMatch GO:0004672. The
  IBA GO:0004672 row is ACCEPTed (also backs it). GO:0004674 is defined with ATP -> ADP,
  so the UniRule GO:0004674 row is generalised to GO:0004672.
