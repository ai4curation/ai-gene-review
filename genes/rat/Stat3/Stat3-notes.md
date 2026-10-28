# Stat3 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Stat3` resolved P52631 (STAT3_RAT, Swiss-Prot reviewed; RGD:3772;
  GeneID 25125). First attempt timed out on UniProt; retry succeeded. 318 GOA rows over 142
  distinct terms.
- No deep research provider available; manual synthesis in `Stat3-deep-research-manual.md`.
- Key experimental paper PMID:19450559 (Barry et al. 2009) read in full: Stat3
  overexpression protects neonatal rat ventricular myocytes from simulated I/R, Y705F
  dominant-negative enhances death [PMID:19450559 "Overexpression of STAT3 in primary neonatal rat ventricular myocytes (NRVM) protects against I/R-induced cell death."].
  Supports GO:1900037 regulation of cellular response to hypoxia (IMP) as a non-core,
  context-specific process.

## Decisions of note

- Core MF: DNA-binding transcription activator activity, RNA Pol II-specific
  (GO:0001228 / GO:0000981), sequence-specific binding to cis-regulatory elements
  (GO:0000978), homodimerisation (GO:0042803). Core BP: JAK-STAT receptor signalling
  (GO:0007259) and gp130-family cytokine (IL-6) signalling; positive regulation of Pol II
  transcription (GO:0045944).
- PMID:22284190 (NMDAR-LTD) explicitly shows STAT3's role in LTD is independent of nuclear
  action [PMID:22284190 "the effects of inhibition of STAT3 are independent of an action within the nucleus"],
  which contradicts the SynGO row GO:0099527 postsynapse to nucleus signaling pathway.
  Marked as over-annotated rather than removed (curator may have relied on the
  pSTAT3 activation data); flagged for expert review.
- GO:0050804 modulation of chemical synaptic transmission: modified to the specific
  process actually shown, GO:0060292 long-term synaptic depression (is_a descendant via
  regulation of synaptic plasticity, checked with OAK).
- GO:0004879 nuclear receptor activity and GO:0030522 intracellular receptor signaling
  pathway: STAT3 is activated by receptor-associated kinases, not by ligand binding;
  marked as over-annotated.
- GO:0006606 protein import into nucleus: Stat3 is the cargo, not import machinery;
  marked over-annotated.
- Bare protein binding (Rac1, ephrinB1 IPIs) removed per protein-binding policy.
- GO:0035259 nuclear glucocorticoid receptor binding (GOA label says obsolete; OLS still
  lists it) modified to GO:0016922 nuclear receptor binding.
- GO:0045944 does not descend from GO:0010628 positive regulation of gene expression in the
  local GO build, so GO:0010628 rows were kept as non-core rather than modified.
- Physiological/organismal ISO terms (feeding, energy/glucose/temperature homeostasis,
  development) kept as non-core: real in mouse but downstream of the TF activity.
- No NEW terms proposed.
