# PLD6 / MitoPLD (human, Q8N2A8) - curation notes

## Literature search (2026-11-21)

No deep-research provider keys were available, so no `-deep-research-*.md` file
was generated. Searches run with the PubMed tools:

- `Zucchini endonuclease structure piRNA` -> 9 hits: 23064230, 29021243, 23086923,
  25179713, 23064227, 23143246, 29531043, 21397848, 21397847
- `MitoPLD OR PLD6 cardiolipin hydrolase` -> 36 hits (first 25 screened), incl.
  41640016, 40355014, 21397839, 22281006, 26711011, 21397847, 28852571, 24599962,
  28063496, 37569546
- `(PLD6 OR MitoPLD) AND (nuclease OR endonuclease)` -> 15 hits, incl. 28115634,
  27851737, 31996847, 33635934, 29444933, 28063496, 23064227, 23064230, 23086923
- `(MIGA2 OR mitoguardin) AND (PLD6 OR MitoPLD)` -> 26711011, 38843396, 38996145
  (last is a prognostic-signature paper, not relevant)
- `PLD6 cryo-EM structure` -> 0 hits (the PDB 9LKX/9LKY human EM entries on the
  UniProt record have no PubMed-indexed paper that this search found)

Cached with `just fetch-pmid` (in addition to the GOA references already present):
23064230, 23064227, 23086923, 21397847, 28063496, 24599962, 34800366, 38843396,
41640016, 31996847, 28115634.

## The two activities

### Cardiolipin phospholipase D (RHEA:44884, GO:0035755)

Evidence on the human protein:

- Choi et al. 2006 (PMID:17028579, abstract only in cache): MitoPLD on the outer
  face of mitochondria promotes Mfn-dependent fusion "by hydrolysing cardiolipin to
  generate phosphatidic acid". This is the IDA behind the GO and UniProt catalytic
  activity. Full text not available to me, so the assay details are not checked.
- Huang et al. 2011 (PMID:21397848, full text): a PA sensor translocates to
  mitochondria when wild-type, but not H156N or Delta39 cytosolic, MitoPLD is
  overexpressed ["However, increasing MitoPLD expression to cause PA production
  induced sensor translocation to the aggregated mitochondria"]. This shows
  catalysis-dependent PA at the mitochondrial surface; the substrate is not measured
  in this paper, which cites Choi 2006 for cardiolipin. The same paper states the
  lab could not detect nuclease activity ["As previously reported, we were unable to
  demonstrate nuclease activities for MitoPLD"].
- Zhang et al. 2016 (PMID:26711011): MIGA1/2 stabilize MitoPLD and its dimer;
  UniProt cites it for the catalytic activity (abstract does not describe the assay).
- Chen et al. 2026 (PMID:41640016): NME3 interacts with PLD6 to generate PA from
  cardiolipin on the OMM after depolarization (abstract only).

Evidence against / complicating:

- Ipsaro et al. 2012 (PMID:23064227, full text): recombinant soluble dimeric mouse
  PLD6 (mZuc) showed no cardiolipin hydrolysis by TLC or SRM-MS ["no significant
  changes in cardiolipin or PA were observed when comparing buffer controls to either
  wild-type or catalytically inactive mZuc proteins"]; structure resembles PLD-family
  nucleases more than phospholipases. Caveat: the construct lacked the TM anchor.
- Baba et al. 2014 (PMID:24599962, full text): MS lipidomics of mitochondria from
  MitoPLD-overexpressing HeLa cells showed no PA change ["However, lipid analysis by
  mass spectrometry failed to show significant changes in the PA content of
  mitochondria upon overexpression of MitoPLD"].
- Nishimasu et al. 2012 (PMID:23064230): fly and mouse Zuc are ssRNA endonucleases
  producing 5'-monophosphate ends; Voigt et al. 2012 (PMID:23086923): narrow
  ss-nucleic-acid groove at the dimer interface.

Judgement: the activity was reported on the human protein by the originating lab
and a mitochondrial-surface PA signal that depends on PLD6 catalysis has been seen
by several groups, so the IDA is not to be removed. But the substrate assignment
rests mainly on one lab's assay, a rigorous independent test with the mouse
ortholog was negative, and lipidomics did not detect a PA change. The activity is
real-but-contested, not the best-established function. All four GO:0035755 rows
-> KEEP_AS_NON_CORE, with the reason stated; the ssRNA endonuclease is taken as the
core molecular function.

### Single-strand-specific endonuclease (GO:0016891)

- Human PLD6 (aa 36-252) purified and assayed as a nuclease (Philip et al. 2017,
  PMID:28063496, Frohman lab) ["The nuclease activity of human PLD6, which is
  sequence independent, can be visualized..."].
- Mouse/fly orthologs: ssRNA/ssDNA endonuclease, 5' phosphate products, active-site
  mutants lose piRNAs in vivo (PMID:23064230, PMID:23064227); Zuc cleaves at
  consensus motifs in a silkworm cell-free system (PMID:31996847).

## Processes

- Mouse Pld6 knockout: male meiotic arrest, transposon derepression, primary piRNA
  loss; females fertile (PMID:21397847, PMID:21397848). Oocyte piRNAs fall ~50%
  (PMID:28115634).
- Human cells: mitochondrial fusion requires MitoPLD (PMID:17028579 IMP); TRABD,
  MIGA2, MFN2 and PLD6 form complexes that promote fusion (PMID:38843396).

## Location

- OMM, single-pass, N-terminal TM anchor (PMID:17028579; PMID:21397848).
- Golgi only from a mouse spermatocyte study (UniProt ECO:0000250, with a CAUTION
  noting the conflict with mitochondrial localization).
