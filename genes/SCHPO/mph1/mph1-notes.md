# mph1 (Mps1 homolog, S. pombe) — Gene Review Notes

UniProt: O94235 (MPS1_SCHPO). PomBase: SPBC106.01. Gene name mph1, synonym mps1.
EC 2.7.12.1 (dual-specificity protein kinase). 678 aa, kinase domain 316–607, ATP binding
322–330 + 345, active-site (proton acceptor) D442 (PROSITE).

NOTE: S. pombe mph1 = the Mps1-family spindle assembly checkpoint (SAC) kinase. This is
unrelated to budding-yeast/human MPH1 (a DNA helicase). Do not confuse.

## Identity and family
- Mph1 (Mps1p-like pombe homolog) is a member of the Mps1-like family of dual-specificity
  protein kinases, required for the spindle checkpoint in S. pombe; functions upstream of
  mad2 [PMID:9601094 "we report the isolation of a new spindle checkpoint gene, mph1
  (Mps1p-like pombe homolog), in the fission yeast Schizosaccharomyces pombe, that is required
  for checkpoint activation in response to spindle defects. mph1 functions upstream of mad2"].
- Functionally related to S. cerevisiae Mps1, but unlike Mps1, mph1 is NOT required for
  spindle pole body duplication and is not essential [PMID:9601094 "They differ in that Mps1p,
  but not mph1, has an additional essential role in spindle pole body duplication"; PMID:22281223
  "S. pombe Mph1 is the homolog of S. cerevisiae Mps1, but it is neither required for spindle
  pole duplication nor essential for cell viability"].

## Catalytic activity (MF)
- Mph1 is an active kinase that phosphorylates itself and Mad2 in vitro; D459A "kinase-dead"
  allele abolishes activity [PMID:22281223 "Mph1 is an active kinase that can phosphorylate
  itself and Mad2 in vitro; second, the D459A substitution has 'killed' Mph1 kinase activity"].
- Phosphorylates Spc7 in vitro on threonine residues of MELT motifs [PMID:22521786 "We find
  that Mph1 phosphorylates Spc7 in vitro on two threonine residues (T453 and T507) which are
  part of a repetitive motif of unknown function, termed the MELT motif"].
- Dual specificity (Ser/Thr/Tyr) — UniProt assigns EC 2.7.12.1 with Ser, Thr, and Tyr Rhea
  reactions. The directly demonstrated targets in S. pombe are Ser/Thr (Spc7 MELT threonines,
  Mad2/Mad3 serine/threonine sites). Tyr autophosphorylation is a family property; no direct
  pombe Tyr substrate demonstrated in cached refs but family is dual-specificity [PMID:9601094
  "Mps1-like family of dual specificity protein kinases"].

## Core BP: spindle assembly checkpoint (mitotic)
- Mph1 phosphorylates kinetochore Spc7 (KNL1) MELT repeats; this promotes Bub1-Bub3 recruitment
  required for SAC [PMID:22660415 "fission yeast Mph1 (MPS1 homologue) phosphorylates the
  kinetochore protein Spc7 (KNL1/Blinkin homologue) at the MELT repeat sequences. This
  phosphorylation promotes the in vitro binding to the Bub1-Bub3 complex, which is required for
  kinetochore-based SAC activation (Mad1-Mad2-Mad3 localization) and chromosome alignment"].
- Phosphodependent recruitment of Bub1 and Bub3 to Spc7 maintains the SAC [PMID:22521786
  "phosphorylation of the conserved MELT motifs in Spc7 by Mph1 (Mps1) recruits Bub1 and Bub3
  to the kinetochore and that this is required to maintain the SAC signal"].
- mph1Δ and kinase-dead are checkpoint defective; required for checkpoint arrest [PMID:22281223
  "The mph1-kd mutant was unable to arrest in mitosis, like mad2Δ and mph1Δ strains... We
  conclude that Mph1 kinase activity is required for checkpoint arrest"].
- Mph1 kinetochore localization is upstream/apical in SAC recruitment hierarchy [PMID:22825872
  "recruitment of the kinase Mph1 is of vital importance for a stable SAC arrest. An Mph1 mutant
  that eliminates kinetochore enrichment abolishes SAC signaling, whereas forced recruitment of
  this mutant to kinetochores restores SAC signaling"; "a three-layered hierarchy with Ark1 and
  Mph1 on top, Bub1 and Bub3 in the middle, and Mad3 as well as the Mad1-Mad2 complex at the
  lower end"].
- Centromere-tethered Mph1 is sufficient to recruit Bub1 (but not stable Mad1) and to arrest
  cells in a checkpoint-dependent manner [PMID:22184248 "localization of Mph1 at
  centromeres/kinetochores is sufficient to recruit Bub1"; "the fusion protein arrests cell
  cycle progression in a spindle-checkpoint dependent manner in fission yeast"].
- Mph1 kinase activity required for Mad2/Mad3 to stably bind APC/C (MCC-APC/C maintenance)
  [PMID:22281223 "Mad2p and Mad3p displayed a significantly reduced ability to bind stably to
  fission yeast APC/C in mph1-kd"; "Mph1 kinase activity is required to assemble and/or maintain
  MCC-APC/C complexes"].
- Mph1 phosphorylates Mad3 to inhibit Cdc20Slp1-APC/C and maintain checkpoint arrests
  [PMID:26882497 "we identify Mad3 as a substrate of fission yeast Mps1(Mph1) kinase... Mad3
  phospho-mimics are potent APC/C inhibitors in vitro... Mps1(Mph1) kinase-dependent
  modifications of Mad3 and Mad2 act in a concerted manner to maintain spindle checkpoint
  arrests"].
- Bub3-Bub1 binding to Spc7 MELT array toggles the checkpoint switch by licensing Bub1-Mad1-Mad2
  interaction, downstream of Mph1 phosphorylation [PMID:27618268 "Mph1 (Mps1) phosphorylates
  multiple conserved MELT motifs in the Spc7 (Spc105/KNL1) protein to recruit Bub1, Bub3, and
  Mad3 (BubR1) to kinetochores"; "multisite binding of Bub3 to the Spc7 MELT array toggles the
  spindle checkpoint switch by permitting Mph1 (Mps1)-dependent interaction of Bub1 with
  Mad1-Mad2"]. (This paper is a downstream-mechanism study; mph1 EXP MF annotation derived from it.)

## Localization (CC)
- Localizes to kinetochore, especially unattached kinetochores [PMID:22660415 "MPS1/Mph1 kinase
  locating at the unattached kinetochores initially creates a mark"; this paper is the IDA
  source for kinetochore]. Also kinetochore IDA from [PMID:22184248].
- Nucleus and cytosol from global YFP localization (HDA) [PMID:16823372 — genome-wide ORFeome
  localization study; mph1 scored nuclear/cytosolic].

## Chromosome segregation / biorientation (BP)
- Mph1 kinase has chromosome segregation functions even without spindle perturbation; mph1Δ and
  kd elevate chromosome loss [PMID:22281223 "These experiments demonstrate that Mph1 kinase has
  important chromosome segregation function(s), even when there are no extrinsic perturbations
  of spindle microtubules"]. Phosphorylation of Spc7 MELT promotes chromosome alignment/
  biorientation [PMID:22660415 "...required for kinetochore-based SAC activation... and
  chromosome alignment"].

## Meiosis (BP)
- mph1Δ shows meiosis I homolog non-disjunction; required for proper homolog disjunction at
  meiosis I [PMID:23370392 "Mph1, a member of the Mps1 family of spindle assembly checkpoint
  kinases, is required to prevent meiosis I homolog non-disjunction"; "We thus conclude that
  Mph1 is required for efficient homolog disjunction during meiosis I"]. Likely due to precocious
  anaphase I entry from a weakened SAC.
- Meiotic centromeric cohesion protection in anaphase I (GO:1990813), IMP from [PMID:28497540]
  (Miyazaki et al., meikin/Moa1-Plo1-Spc7-Bub1 pathway). Cached file is abstract-only; the SAC
  kinase Mph1 phosphorylating Spc7 in the Bub1-recruitment pathway is consistent with a meiotic
  cohesion-protection role via Bub1/Sgo1. Full text not in cache — defer to PomBase curator.

## Summary of action decisions
- MF kinase activities (protein Ser/Thr kinase IDA/EXP; Ser/Thr/Tyr; protein kinase; ATP
  binding; protein Ser kinase RHEA; protein Tyr kinase RHEA) — ACCEPT core; consolidate.
  Generic "protein kinase activity" IEA kept as non-core (subsumed by specific term).
- BP mitotic SAC signaling (multiple IMP/EXP/IBA/IEA) — ACCEPT core.
- BP nuclear chromosome segregation / chromosome segregation — KEEP_AS_NON_CORE (general,
  downstream consequence; SAC + biorientation is the mechanistic core).
- BP protein localization to kinetochore (IBA) — ACCEPT (Mph1 recruits Bub1-Bub3 etc).
- BP meiosis I, meiotic SAC signaling, meiotic centromeric cohesion protection — KEEP_AS_NON_CORE
  (meiosis-specific, real but not the central mitotic function).
- CC kinetochore (IDA) — ACCEPT core. nucleus, cytosol (HDA) — KEEP_AS_NON_CORE.
