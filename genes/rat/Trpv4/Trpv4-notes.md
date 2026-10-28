# Trpv4 (rat) review notes

## Session 1 (create review)

- `just fetch-gene rat Trpv4` resolved Q9ERZ8 (TRPV4_RAT, RGD:69337, GeneID 66026). 186 GOA rows.
- No deep-research keys: literature synthesis is in `Trpv4-deep-research-manual.md`.
- Full text read: PMID:11081638 (VR-OAC cloning, rat channel physiology), PMID:20650893
  (beta-arrestin 1/AIP4 ubiquitination, rat VSMC), PMID:20657843 (cytoskeleton
  interaction), PMID:21262839 (AQP4/TRPV4, rat astrocytes), PMID:23021218 (mouse adipocytes,
  added as source for the many mouse ISO rows).
- Abstract only: PMID:22962011, PMID:23136043, PMID:32706268, PMID:11025659, PMID:14581612.

### ISO donor identities (checked against RGD REST)

- RGD:13967072 = pig TRPV4 (speciesTypeKey 9).
- RGD:12381920 = dog TRPV4 (speciesTypeKey 6).
- MGI:MGI:1926945 = mouse Trpv4; UniProtKB:Q9HBA0 = human TRPV4; UniProtKB:Q9EPK8 = mouse.

### Main decisions

- Core MF: calcium channel activity (GO:0005262) for a polymodal Ca2+-permeable
  nonselective cation channel; stretch-activated Ca channel (GO:0015275) and osmosensor
  activity (GO:0005034) accepted for the osmo/mechanosensing gating mode.
- Core BP: calcium ion import across plasma membrane (GO:0098703, most specific transport
  term in GOA set); generic transport parents MODIFY to it. Cellular hypotonic response
  and osmosensory signaling accepted; generic stress/osmotic parents MODIFY to GO:0071476.
- GO:0071477 cellular hypotonic salinity response MODIFIED to GO:0071476: PMID:11081638
  shows the channel ignores isotonic Na+ reduction.
- Adipocyte program (Ye et al. 2012, mouse): cell-autonomous ERK1/2-dependent chemokine and
  Pgc1a effects kept as non-core; organism-level metabolic phenotypes (energy/glucose
  homeostasis, response to insulin, diet-induced thermogenesis) and transcription/gene
  expression terms marked over-annotated (downstream knockout phenotypes).
- NOT p38 MAPK cascade (mouse ISO) accepted as non-core: Ye 2012 reports no p38 activation.
- NOT rows from PMID:23136043 (heart rate, blood pressure, response to osmotic stress)
  UNDECIDED: abstract only; the NOT blood pressure claim sits uneasily with agonist-induced
  circulatory collapse reported elsewhere, but I could not read the data.
- Focal adhesion IDA (PMID:20657843) marked over-annotated: the paper says only "resemble
  focal adhesion points" without a marker, and PMID:11081638 found no colocalization with
  paxillin.
- ATP transport/export (pig ISO): channel lets ATP-releasing pathways run downstream of
  Ca2+ but does not transport ATP; marked over-annotated.
- Bare protein binding (AQP4 IPI) removed per policy; the AQP4 complex is described in
  core functions and suggested questions.

### Curation follow-ups (not knowledge gaps)

- Consider a regulatory volume decrease / cell volume homeostasis annotation from
  PMID:21262839 (rat astrocyte siRNA) - currently only a pig ISO row carries GO:0045794.
