# HTR2C notes

Deep research providers unavailable; research from UniProt (P28335), cached publications, Reactome.

## Identity / function
- 5-hydroxytryptamine (serotonin) receptor 2C: class A 7TM GPCR. [UniProt "G protein-coupled
  receptor for 5-hydroxytryptamine (serotonin)"].
- Couples to Gq/G11 -> phospholipase C-beta -> DAG + IP3 -> intracellular Ca2+ release and PKC;
  also modulates PI3K and ERK. [UniProt "HTR2C is coupled to G(q)/G(11) G alpha proteins and
  activates phospholipase C-beta"]. Beta-arrestin biased signaling. RNA-edited isoforms.
- CNS roles: appetite/feeding regulation, mood/anxiety, POMC/CRH neuron modulation, insulin
  sensitivity.
- P34968 (ISS donor) = mouse 5-HT2C; P28335 = human HTR2C itself (identical protein binding = self).

## Localization (cell-surface benchmark)
- CELL-SURFACE plasma-membrane 7TM GPCR, ligand pocket accessible from the extracellular side.
  [UniProt "Cell membrane; Multi-pass membrane protein"]. In neurons dendrite/synapse.
- Conclusion: plasma membrane, cell-surface accessible.

## Curation
- 5-HT2C is Gq/PLC-coupled, NOT cyclic-nucleotide-coupled. GO:0007187 (GPCR signaling coupled to
  cyclic nucleotide second messenger, IBA) is a mis-leveled propagation -> MODIFY to PLC-activating
  serotonin receptor signaling.
- Generic GPCR/serotonin/PLC signaling terms MODIFY/TOO_GENERAL toward the specific PLC-activating
  serotonin receptor signaling (GO:0007208) and Gq/11-coupled serotonin receptor activity.
- Bare protein binding (RAMPs, PDZ MPDZ, screens) REMOVE under policy; self-association kept as
  identical protein binding. Behavioral/appetite/CRH/nervous-system processes kept as non-core.
