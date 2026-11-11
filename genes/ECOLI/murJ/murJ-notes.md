# murJ (P0AF16) curation notes

Escherichia coli K-12 MurJ (formerly MviN/YceN; b1069, JW1056), 511 aa, 14-TM
inner-membrane protein of the MOP (multidrug/oligosaccharidyl-lipid/polysaccharide)
exporter superfamily, MurJ/MviN family (HAMAP MF_02078, TIGR01695, Pfam PF03023,
TCDB 2.A.66.4.3, CDD MATE_MurJ_like, PANTHER PTHR47019:SF1).

No deep-research file was generated; notes compiled manually from cached
publications and UniProt. FEBA fitness data could not be fetched (no FEBA data
source reachable); murJ is essential.

## Requirement for peptidoglycan synthesis

- Essential gene; a ts mviN mutant swells, bursts, and accumulates lipid II
  [PMID:18708495 "These results indicated that MviN is involved in murein synthesis."].
- Ruiz identified MurJ bioinformatically as the candidate lipid II flippase and
  showed lipid-linked precursor accumulation on depletion
  [PMID:18832143 "Here, I present genetic and biochemical data that confirm the requirement of MurJ for peptidoglycan biosynthesis and that are in agreement with a role of MurJ as a flippase."].

## Flippase activity (in vivo)

- Sham et al. 2014 built an in vivo flippase assay: periplasmically delivered
  colicin M cleaves only flipped lipid II, so ColM products report flipping.
  MTSES rapidly inactivates the single-Cys MurJ A29C variant, and this abolishes
  ColM processing of lipid II in cells and spheroplasts
  [PMID:25013077 "We combined these approaches to demonstrate that MurJ is the lipid II flippase in Escherichia coli."].
  Flipping persisted when FtsW was depleted in a rodA deletion background
  [PMID:25013077 "this result suggests that SEDS proteins are not responsible for lipid II flippase activity in vivo"].
- MurJ requires membrane potential; dissipation traps it in an inactive
  outward-facing state [PMID:29558128 "We conclude that membrane potential is required for MurJ function in E. coli"].
- B. subtilis MurJ or Amj can substitute for E. coli MurJ in lipid II flipping
  [PMID:25918422 "Furthermore, expression of Amj or MurJBs in E. coli supports lipid II flipping and viability in the absence of E. coli MurJ."].

## Structure

- Topology: 14 TM segments with a solvent-exposed central cavity; charged cavity
  residues (R18, R24, D39, R52, R270) are essential
  [PMID:23935042 "Using in vivo topological studies, we demonstrate that MurJ has 14 transmembrane domains"].
- Crystal structures of Thermosipho africanus MurJ in inward- and
  outward-facing states support alternating access
  [PMID:28024149, PMID:30988294]; E. coli MurJ crystallized in a "squeezed"
  intermediate [PMID:35660157].
- Native MS: E. coli MurJ binds lipid II more than FtsW does; A29/D269 mutations
  weaken binding; MurJ co-purifies with cardiolipin and cardiolipin competes with
  lipid II [PMID:29461535 "Furthermore, we reveal cardiolipins associate with MurJ but not FtsW, and exogenous cardiolipins reduce lipid II binding to MurJ."].

## The MurJ vs FtsW/RodA debate

- FtsW in vesicles/proteoliposomes promoted lipid II transbilayer movement
  [PMID:21386816 "purified FtsW induced the transbilayer movement of Lipid II in model membranes."].
- SEDS proteins (RodA, FtsW) were then shown to be peptidoglycan polymerases
  [PMID:27525505 "Our genetic and biochemical analyses indicate that SEDS proteins constitute a family of peptidoglycan polymerases."],
  which explains their requirement for lipid II consumption without requiring
  them to be flippases.
- UniProt still flags the controversy (CC MISCELLANEOUS). Curation view: MurJ is
  the physiological lipid II flippase in E. coli (in vivo ColM assay, rapid
  chemical inactivation, structural mechanism); FtsW's in vitro flippase activity
  is treated as non-core in the ftsW review. A purified MurJ flippase assay in
  proteoliposomes has not been reported, so the direct biochemical demonstration
  remains a gap.

## Location

- Inner membrane, multipass: global topology study (PMID:15919996) and the
  MurJ-specific topology study (PMID:23935042).
- Localizes in the lateral membrane and at midcell; midcell recruitment needs a
  complete divisome, lipid II synthesis, and FtsW/PBP3 activity
  [PMID:30112777 "Here we show that MurJ localizes both in the lateral membrane and at midcell, and is recruited to midcell simultaneously with late-localizing divisome proteins and proteins MraY and MurG."].

## Keyword process terms

The UniProt entry has keyword "Cell shape" but no corresponding GOA IEA row
exists for P0AF16 in the current GOA file, so nothing to judge. MurJ transports
precursor; it does not regulate cell shape and such a term should not be added.

## Annotation decisions

- GO:0015648 lipid-linked peptidoglycan transporter activity: core MF (ACCEPT all).
- GO:0015836 lipid-linked peptidoglycan transport and GO:0034203 glycolipid
  translocation: both describe the flipping process (ACCEPT).
- GO:0034204 lipid translocation (IBA): true but general; MODIFY to GO:0034203.
- GO:0009252: ACCEPT (MurJ performs the transport step of the pathway).
- GO:0000935 division septum: KEEP_AS_NON_CORE (also lateral membrane).
- GO:1901612 cardiolipin binding: KEEP_AS_NON_CORE (in vitro native MS;
  regulatory relevance unproven).

## Module consistency

modules/peptidoglycan_precursor_biosynthesis.yaml murJ_activity annoton
(GO:0015648, plasma membrane, P0AF16 representative) matches the core function.
