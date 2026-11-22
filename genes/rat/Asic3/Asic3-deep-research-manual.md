# Asic3 (rat, UniProt O35240) - manual literature synthesis

No deep-research API was available for this review; this summary was compiled by hand from the
cached publications in `publications/` and the UniProt record. Most primary papers are cached as
abstracts only (noted below).

## Identity
- Acid-sensing ion channel 3 (ASIC3; DRASIC; Accn3), RGD:708578, GeneID 286920, 533 aa.
- DEG/ENaC family (Pfam PF00858 ASC; InterPro IPR001873 ENaC; PANTHER PTHR11690:SF228 ACID-SENSING
  ION CHANNEL 3). Two transmembrane helices (20-40, 436-456), large extracellular domain, cytoplasmic
  N and C termini, GAS selectivity-filter motif (449-451) and a C-terminal PDZ-binding motif (530-533)
  [UniProt O35240 FT].

## Channel activity
- Cloned from rat DRG; in COS cells forms a proton-gated Na+ channel with a rapidly inactivating
  and a sustained current [PMID:9261094 "In COS cells, it forms a Na+ channel that responds to a drop
  of the extracellular pH with both a rapidly inactivating and a sustained Na+ current." (abstract only)].
- Co-assembles with ASIC2a into heteromeric channels mainly selective for sodium [PMID:10842183 "The
  reversal potential of the ASIC2a+3 current (>/=+20 mV) reflected a cationic current mainly selective
  for sodium." (abstract only)].
- Rat ASIC3 reproduces the acid-evoked current of cardiac ischemia-sensing afferents, opens near pH 7
  and interacts with Ca2+ [PMID:11120882 "ASIC3 and the native channel are both especially sensitive
  to pH, interact similarly with Ca(2+), and gate rapidly between closed, open, and desensitized
  states." (abstract only)]. UniProt lists Ca2+ permeation from this paper (CATALYTIC ACTIVITY
  Ca(2+)(in) = Ca(2+)(out), ECO:0000269|PubMed:11120882); Ca2+ flux is minor relative to Na+.
- Lactate enhances the channel by chelating extracellular divalent ions [PMID:11528414 "lactate,
  acting through extracellular divalent ions, dramatically increases activity of an acid-sensing ion
  channel (ASIC)" (abstract only)].
- Proton gating requires the Tyr72/Trp288 aromatic pair conserved across ASICs; substituting it in
  rat ASIC3 abolishes function [PMID:19074149 "Substitution of either one the aromatic residues by
  Ala or Gly in rat ASIC2a and ASIC3 also produced non-functional channels." (full text)].

## Localization
- Plasma membrane of soma and processes of DRG neurons [PMID:11842212 "Within cells, the ASICs are
  present mainly on the plasma membrane of the soma and cellular processes." (abstract only)].
- Surface level regulated by PDZ partners [PMID:15317815 "PSD-95 and Lin-7b altered current density
  by decreasing or increasing, respectively, the amount of ASIC3 on the cell surface."].
- Intracellular / perinuclear pool, redistributed by NHERF-1 [PMID:16234233 "In the presence of
  NHERF-1, the ASIC3 subcellular localization is modified, and the channel co-localizes with ezrin"].

## Partners (PDZ scaffolds and stomatins)
- CIPP (PATJ) PDZ4 binds the ASIC3 C terminus and raises current [PMID:11872753 "This interaction
  requires the C-terminal region of ASIC3 and the fourth PDZ domain of CIPP."].
- NHERF-1 [PMID:16234233 "We report here a PDZ-dependent and protein kinase C-modulated association
  between ASIC3 and the Na+/H+ exchanger regulatory factor-1 (NHERF-1) adaptor protein."].
- PSD-95, Lin-7b, MAGI-1b, PIST [PMID:15317815 "a PDZ-binding motif at the ASIC3 C terminus interacts
  with four different proteins that contain PDZ domains: PSD-95, Lin-7b, MAGI-1b, and PIST."].
- Stomatin co-immunoprecipitates and represses ASIC3 currents [PMID:22850675 "We show that
  dimerization is crucial for the repression of acid-sensing ion channel 3 (ASIC3) activity." (full
  text)]. STOML3 interaction is recorded in IntAct (PMID:17167420 abstract does not mention ASIC3).

## Physiology
- Acid/inflammatory pain sensor in rat: APETx2 blockade or siRNA knockdown is analgesic
  [PMID:18923424 "Both APETx2 and the in vivo knockdown of ASIC3 with a specific siRNA also have
  potent analgesic effects against primary inflammation-induced hyperalgesia in rat." (abstract only)].
- Proposed sensor of myocardial acidity in cardiac pain [PMID:11120882].
- Mouse knockout data (transferred by RGD ISO) implicate ASIC3 in mechanosensation, heat and
  mechanical hyperalgesia, but these phenotypes are modulatory; ASIC3 is not itself a thermosensor.
