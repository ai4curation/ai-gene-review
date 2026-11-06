# spz5 (DNT2, NT2; UniProtKB:Q9VZX1) curation notes

## Literature search (2026-11-06)

No deep-research API keys were available, so `just deep-research` was not run. The FlyBase
hand-written description (`spz5-deep-research-flybase.md`) was checked claim by claim. Papers
read from the local cache (full text unless stated): PMID:19018662, PMID:23892553,
PMID:24124519, PMID:28373203, PMID:28846707, PMID:31088910, PMID:30361090 (abstract only),
PMID:30745142, PMID:39704728, PMID:42552905.

## Identity

- Spätzle-family cystine-knot protein; signal peptide 1-29, pro-domain 30-284, mature chain
  285-387 (UniProt FT). Readily cleaved by furin before secretion [PMID:23892553 "whereas DNT2 is
  consistently secreted from S2 cells as a mature, cleaved form consisting of the cystine-knot
  domain"; PMID:28373203 "DNT1 and 2 are cleaved intracellularly by conserved furins."].
- PANTHER PTHR23199:SF16; PAINT node PTN002354018. No PAINT IRD/IKR losses on the lineage.

## Receptors

- Toll-6 and Toll-7 [PMID:23892553 "Together, these data demonstrate that DNT1 binds Toll-7 and
  DNT2 binds promiscuously Toll-6 and Toll-7."]; purified DNT2 triggers Dif signalling via
  Toll-6/7 in S2 cells [PMID:23892553 "were stimulated with purified DNT2 this triggered a
  drosomycin-luciferase readout indicative of Dif signalling"].
- Kek-6 (truncated Trk-like) [PMID:28846707 "Kek-6 is expressed in the CNS, interacts
  genetically with DNTs and can bind DNT2 in signaling assays and co-immunoprecipitations."].
- Toll-2 by genetic interaction in the visual system [PMID:42552905 "Loss of function for DNT-2 or
  Toll-2 induced apoptosis, and Toll-2 knock-down prevented the pro-survival function of DNT-2."].
- Toll-1: Spz5 is a Toll-1 ligand independent of furin processing, and Spz5 accounts for most
  Toll-1 ligand activity of larval extract [PMID:30361090 "Here, we demonstrate that Spz5, a
  member of the Spz family of proteins, functions as a ligand for the Toll-1 receptor."]. Also
  in vitro Toll-1/Toll-7 binding and drosomycin activation [PMID:31088910].
- Glia: apoptotic neurons process Spz5, which activates a dSARM-dependent Toll-6 pathway in glia
  that induces Draper [PMID:30745142 "Neuronal apoptosis drives processing and activation of the
  Toll-6 ligand, Spätzle5."].

## Biological roles

- Neuronal survival, redundantly with DNT1 [PMID:19018662 "indicating redundancy between DNT1 and
  DNT2 for cell survival"]; via Toll-6 [PMID:23892553 "over-expression of Toll-6CY in all neurons
  rescued the apoptosis caused by loss of DNT2 function"]; PAM dopaminergic neurons via Toll-6
  [PMID:39704728 "Altogether, these data showed that DNT-2 functions via Toll-6 to maintain PAM
  neuron survival."].
- Motor axon targeting, mild [PMID:19018662 "Both ISNb/d and SNa projections are mildly affected in
  DNT2e03444/Df(3L)exel6092 mutant embryos."].
- Structural synaptic plasticity at the NMJ (retrograde, muscle-derived, with Kek-6 and Toll-6)
  [PMID:28846707 "Altogether, our data demonstrate that DNT2 is a retrograde ligand for Kek-6 at the
  NMJ and that DNT2 and Kek-6 are required together for synaptic structure and NMJ growth."] and
  in an adult dopaminergic circuit [PMID:39704728].
- Behaviour: larval crawling (PMID:28846707), adult locomotion and long-term memory
  [PMID:39704728 "Altering the levels of DNT-2 or Toll-6 also modified dopamine-dependent
  behaviours, including locomotion and long-term memory."].

## FlyBase description check

All claims traced: paralog of spz (PTHR23199; PMID:19018662); ligand of Toll-6 and kek6
(PMID:23892553, PMID:28846707); survival, axonal/dendritic growth and branching, synaptic
structural plasticity (PMID:28846707, PMID:39704728); larval locomotion (PMID:28846707) and adult
locomotion and long-term memory (PMID:39704728). Incomplete (omits Toll-7, Toll-1, Toll-2) but not
wrong -> VERIFIED.

## Decisions summary

- MF core: growth factor activity (GO:0008083); Toll binding rows MODIFY (ligand convention).
- BP core: NEW neurotrophin signaling pathway (GO:0038179); negative regulation of neuron
  apoptotic process; regulation of synaptic plasticity.
- Toll-1 (immune) Toll signaling pathway, innate immune response and AMP production rows are
  supported by two labs (PMID:30361090, PMID:31088910) and kept as non-core.
