# Capn3 (rat) review notes

## 2026-10-28: initial review

- `just fetch-gene rat Capn3` resolved UniProt P16259 (CAN3_RAT; RGD:2269; GeneID 29155), 105 GOA rows.
- No deep-research API: literature work in `Capn3-deep-research-manual.md`.
- Full text read: PMID:20460380 (Na+-dependent autolysis; uses partially purified rat wild-type p94
  [PMID:20460380 "When the incubations were carried out with both ions at varying concentrations using WT
  p94 partially purified from rat GC"]), PMID:37298357 (rat and human muscle; Na+ effect only without K+),
  PMID:21295580 (mouse C129S knock-in, non-proteolytic SR role).
- Abstract only: PMID:18676612, PMID:19144634, PMID:14506720, PMID:12663060, PMID:11904300,
  PMID:15726428, PMID:20139084, PMID:15138196. PMC full text for 18676612 and 19144634 could not be
  retrieved through the PubMed tool (empty body). The experimental rows resting on them were not
  removed.
- Donor tracing (QuickGO, mouse Q64691): the ISO/ISS mouse rows come from PMID:18676612
  (structural constituent, adaptor, complex assembly, Ca2+ release, protein localization to membrane,
  plasma membrane, cytosol), PMID:20460380 (sodium ion binding, salt stress, cellular response to calcium,
  programmed cell death), PMID:20139084 (satellite-cell activation, myoblast differentiation, G1-to-G0,
  transcription, positive regulation of proteolysis) and PMID:15138196 (myofibril assembly, sarcomere
  organization).

## Decisions worth flagging

- Programmed cell death (mouse IDA PMID:20460380, rat ISO): the paper mentions apoptosis only in its
  introduction [PMID:20460380 "regulate various cellular functions, such as signal transduction,
  autophagy, and apoptosis"]. Marked over-annotated; recorded a WRONG_TERM CHECK source defect against
  the UniProt mouse row.
- Positive regulation of satellite cell activation (mouse IDA PMID:20139084): the paper shows CAPN3
  promoting the quiescent reserve-cell pool, the opposite direction to activation. Modified to
  regulation of myoblast differentiation; WRONG_TERM CHECK source defect.
- Signaling receptor binding (IPI with mouse RyR1): RyR1 is a calcium-release channel; binding was in a
  membrane extract. UNDECIDED with a WRONG_TERM CHECK defect.
- Sodium: Na+-dependent autolysis is reproducible in vitro but not at physiological K+ (PMID:37298357);
  sodium-dependent self proteolysis kept as non-core, sodium ion binding UNDECIDED, salt stress
  over-annotated.
- Plasma membrane / Z disc rows UNDECIDED: rat fibre data place calpain-3 within the filament lattice
  near the N2A line and triads, and it is not washed out with membranes.

## Core functions

1. Ca2+-dependent cysteine endopeptidase with intramolecular autolysis, bound to titin in myofibrils.
2. Non-proteolytic adaptor role in the triad/SR Ca2+-release complex (mouse evidence, transferred).
