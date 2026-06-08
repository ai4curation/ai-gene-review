# mad2 (SPBC20F10.06, O14417) — S. pombe — Curation Notes

Mad2 is a core component of the spindle assembly checkpoint (SAC) in fission yeast.
HORMA-domain protein (UniProt: DOMAIN 13..197 HORMA). PDB 4AEZ is the S. pombe
MCC (Mad2-Mad3-Cdc20/Slp1) structure.

## Core function: SAC / APC-Cdc20 inhibition

- Mad2 is a spindle checkpoint component whose overexpression activates the
  checkpoint and arrests at metaphase-to-anaphase; mad2Δ is hypersensitive to
  TBZ and bypasses mitosis without a normal spindle.
  [PMID:9223296 "We have isolated mad2 , a spindle checkpoint component in fission yeast, and shown that mad2 overexpression activates the checkpoint and causes a cell cycle arrest at the metaphase-to-anaphase transition"]
  [PMID:9223296 "A haploid strain containing a mad2 deletion mutation ( mad2 Δ ) was viable, but the strain was hypersensitive to TBZ"]
  [PMID:9223296 "mad2 Δ cells, therefore, bypass mitosis in the absence of a normal spindle"]
  Genetic evidence that the checkpoint arrests by inhibiting APC-dependent proteolysis.
  [PMID:9223296 "the spindle checkpoint imposes a cell cycle arrest by inhibiting APC-dependent proteolysis"]

- Mad2 binds Slp1 (Cdc20 homolog); disruption of the Mad2-Slp1 interaction
  abolishes the checkpoint. Mad2 targets Slp1 and prevents it promoting proteolysis.
  [PMID:9461438 "Mad2 formed a complex with Slp1, a WD (tryptophan-aspartic acid)-repeat protein essential for the onset of anaphase. When the physical interaction between the two proteins was disrupted, the spindle checkpoint was no longer functional."]
  [PMID:9461438 "This relief of dependence appears to be a result of deregulation of ubiquitin-dependent proteolysis mediated by the anaphase-promoting complex."]

## MCC = Mad2-Mad3-Cdc20(Slp1) in S. pombe; inhibits APC/C

- Crystal structure of S. pombe MCC (Mad2, Mad3, Cdc20). C-Mad2 stabilizes the
  complex by positioning Mad3 KEN box to bind Cdc20. MCC inhibits APC/C by
  obstructing degron sites on Cdc20.
  [PMID:22437499 "using the crystal structure of Schizosaccharomyces pombe MCC (a complex of mitotic spindle assembly checkpoint proteins Mad2, Mad3 and APC/C co-activator protein Cdc20), we reveal the molecular basis of MCC-mediated APC/C inhibition"]
  [PMID:22437499 "Mad2, in the closed conformation (C-Mad2), stabilizes the complex by optimally positioning the Mad3 KEN-box degron to bind Cdc20."]
  [PMID:22437499 "The MCC inhibits the APC/C by obstructing degron recognition sites on Cdc20 (the substrate recruitment subunit of the APC/C) and displacing Cdc20"]

- Mad2 and Mad3 stably bind mitotic APC/C; Mad2-APC/C binding is bridged by
  direct interaction with Cdc20; up to ~8% of APC/C co-depletes with Mad2.
  [PMID:18556659 "we find that the Mad3 and Mad2 spindle checkpoint proteins interact stably with the APC/C in mitosis"]
  [PMID:18556659 "Mad2 interaction with the APC/C is most likely bridged by direct interaction with Cdc20"]
  [PMID:18556659 "in fission yeast, where Slp1 is the Cdc20 homolog that we will refer to as Cdc20 hereafter"]
  Mad2 binds APC/C each mitosis (every cell cycle).
  [PMID:22281223 "Thus Mad2p and Mad3p bind to the APC/C each mitosis, even under optimal growth conditions, demonstrating that the fission yeast spindle checkpoint is active every cell cycle."]

- Mph1 (Mps1) kinase phosphorylates Mad2; needed for stable Mad2/Mad3 APC/C binding.
  [PMID:22281223 "Mph1 is an active kinase that can phosphorylate itself and Mad2 in vitro"]
  [PMID:22281223 "Mad2p and Mad3p displayed a significantly reduced ability to bind stably to fission yeast APC/C in mph1-kd"]
  Mad2 dimerization (R133/Q134) and phosphorylation (S92) important for Cdc20-APC/C binding & checkpoint maintenance.
  [PMID:26882497 "Mps1Mph1 kinase-dependent modifications of Mad3 and Mad2 act in a concerted manner to maintain spindle checkpoint arrests"]

## Localization

- Mad2-Slp1 colocalize to unattached kinetochores in prometaphase-like arrest;
  once attached, only Mad2 stays on the spindle. Interphase: nuclear periphery
  and chromatin, abolished in mad1Δ.
  [PMID:11950879 "the Mad2-Slp1 complex was stable and the two proteins were colocalized to unattached kinetochores"]
  [PMID:11950879 "only Mad2 was found associated to the spindle"]
  [PMID:11950879 "During interphase, Mad2 was localized to the nuclear periphery as well as to the chromatin domain. This localization was abolished in a yeast strain lacking Mad1"]

- Mad2 accumulates at unattached kinetochores; loading requires Mis6 and Nuf2
  complexes; Mis6 physically interacts with Mad2 when checkpoint active.
  [PMID:15930132 "the spindle checkpoint proteins, such as Mad2 and Bub1, accumulate at kinetochores that do not associate with the spindle"]
  [PMID:15930132 "The Mis6-complex physically interacts with Mad2 under the condition that the Mad2-dependent checkpoint is activated."]
  [PMID:15930132 "the Mis6-complex, in collaboration with the Nuf2-complex, monitors the spindle-kinetochore attachment state and acts as a platform for Mad2 to accumulate at unattached kinetochores"]

- Klp5/6 mutant: Mad2 recruited to unattached kinetochores (Mad2 marks
  unattached, Bub1 marks tensionless).
  [PMID:12426374 "In klp5 mutants, spindle checkpoint proteins Mad2 and Bub1 are recruited to mitotic kinetochores for a prolonged duration, indicating that these kinetochores are unattached."]

- Alp14 (ch-TOG/XMAP215) is a component of the Mad2-dependent spindle checkpoint;
  Mad2 localizes to unattached kinetochore dots in alp14 mutant.
  [PMID:11432827 "Alp14 itself is a component of the Mad2-dependent spindle checkpoint cascade"]
  [PMID:11432827 "Mad2 localizes to these dots, which is consistent with the notion that these represent unattached kinetochores"]

## Mad1-Mad2 complex / Mad1 dependence

- Mad1 forms a tetrameric complex with Mad2; Mad1-bound Mad2 dimerizes with soluble
  Mad2 to induce Cdc20 binding. Mad1 needed for Mad2 kinetochore localization.
  [PMID:24477934 "Mad1 forms a tetrameric complex with the checkpoint protein Mad2"]
  [PMID:24477934 "At unattached kinetochores, Mad1-bound Mad2 dimerizes with soluble Mad2 to induce binding of the latter to Cdc20"]
  [PMID:24477934 "In S. pombe, the kinases Ark1 and Mph1, as well as Bub1 and Bub3, are required to bring Mad1:Mad2 to unattached kinetochores"]

- Mad1 binds Mad2 (interactant in GOA). Mad1 also has SAC-independent role anchoring
  Cut7 kinesin for chromosome congression (about Mad1, not direct Mad2 function).
  [PMID:26258632 "fission yeast Mad1 binds the plus-end-directed kinesin-5 motor protein Cut7"]

- Ark1 (aurora)/survivin required for full Mad2 kinetochore association and Mad2-Mad3
  complex formation.
  [PMID:12676091 "it was required for two aspects of Mad2 function that accompany checkpoint activation: full-scale association with kinetochores and formation of a complex with Mad3"]

- Robustness: stoichiometric inhibition of Slp1/Cdc20 by checkpoint proteins;
  ~20% reduction of core checkpoint proteins can impair signalling.
  [PMID:24161933 "Checkpoint-mediated stoichiometric inhibition of the anaphase activator Cdc20 (Slp1 in Schizosaccharomyces pombe)"]

## Meiosis

- Mad2 (and Bub1) required to prevent MI non-disjunction events.
  [PMID:11331883 "Both proteins are required to prevent the occurrence of non-disjunction events in MI"]
- Meiosis I SAC context (aurora B repositioning).
  [PMID:21920317 "this undesirable biorientation of univalents persists and eventually evades the spindle assembly checkpoint"]
- Nup132 loss activates SAC in meiosis I (kinetochore assembly defect).
  [PMID:26483559 "depletion of Nup132 activates the spindle assembly checkpoint in meiosis I"]

## Curation decisions summary

- Core MF: anaphase-promoting complex binding (GO:0010997) ACCEPT; the generic
  "protein binding" (GO:0005515) IPI entries are uninformative -> MARK as such
  but cannot improve term except to note Slp1/Cdc20/Mad1/Mad3 partners.
- GO:0140678 molecular function inhibitor activity (contributes_to) — supported by
  MCC structure/APC inhibition; ACCEPT (core, inhibitor of APC/Cdc20).
- Core BP: GO:0007094 mitotic SAC signaling ACCEPT; GO:0045841 negative regulation
  of metaphase/anaphase transition ACCEPT.
- Core CC: GO:0000776 kinetochore, GO:0033597 MCC ACCEPT; nucleus/nuclear periphery/
  chromatin localization KEEP_AS_NON_CORE; mitotic spindle microtubule / SPB
  KEEP_AS_NON_CORE (transient, spindle association after attachment per 11950879).
- Meiosis terms (1905318, 0033316) ACCEPT (KEEP_AS_NON_CORE; SAC also operates in meiosis).
