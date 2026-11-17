# SLC43A1 (LAT3) review notes

- LAT3 is a Na+-independent, heavy-chain-independent, electroneutral facilitated-diffusion
  (uniport) transporter of large neutral/branched-chain L-amino acids (Leu, Ile, Val, Phe,
  Met) at the plasma membrane [PMID:12930836 "The transport of l-leucine was electroneutral and mediated by a facilitated diffusion"].
- Apical plasma-membrane / podocyte foot-process localization is directly shown
  [PMID:19443642 "LAT3 localizes to the apical plasma membrane of podocyte foot processes"].
- Bidirectional efflux lowers net accumulation of co-transporter substrates (iodocompounds)
  [PMID:26305885 "Cotransfection with LAT3 or LAT4 strongly diminished the cellular accumulation of 3,3'-T2 and MIT by LAT1 and LAT2"] — the two negative-regulation BP rows are kept non-core.

## Decisions
- Item-1 action framework (2026-11-14 ruling): generic substrate-named amino-acid parent
  terms treated as ACCEPT; only bare transmembrane-transport/transporter/solute parents
  TOO_GENERAL. Here GO:0006865, GO:0015171 and both GO:0015179 rows flipped TOO_GENERAL → ACCEPT
  (substrate-named, respectably specific). GO:0022857 and GO:0055085 remain TOO_GENERAL (bare
  MFS transmembrane transporter/transport parents).
- ER-membrane rows (GO:0005789, IEA+ISS): changed to MARK_AS_OVER_ANNOTATED per ORGANELLES
  rule 7. They are synthesis-only, resting on a By-similarity UniProt note from mouse Q8BSM7;
  there is no human ER assay, and GO:0005789 needs the protein's own TM/tail anchor plus an
  ER-specific assay on the endogenous protein. LAT3 is a plasma-membrane transporter.
