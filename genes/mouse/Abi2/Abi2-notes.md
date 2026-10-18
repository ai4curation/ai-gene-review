# Abi2 (mouse, P62484) review notes

## Sources consulted
- PMID:15572692 (Grove et al. 2004), the Abi2 knockout paper; the cache holds the abstract and discussion. Source of all mouse IDA/IMP rows (lens, neuronal migration, spines, memory, adherens junctions). Key quotes:
  - "In the absence of Abi2, secondary lens fiber orientation and migration were defective in the eye, without detectable defects in proliferation, differentiation, or apoptosis."
  - "Loss of Abi2 also resulted in cell migration defects in the neocortex and hippocampus, abnormal dendritic spine morphology and density, and severe deficits in short- and long-term memory."
  - "Abi2 was expressed in both axons and dendritic spines."
- PMID:29911975 (Fan et al. 2018): "overexpression of either WAVE2 (Wasf2) or Abi2 in vivo rescues the cortical neuron migration defect of αKD neurons". This is a rescue experiment, not an Abi2 loss-of-function test.
- PMID:17101133 (abstract only): "Abi-2, like Abi-1, promoted the c-Abl-mediated phosphorylation of Mena and WAVE2".
- PMID:21107423 (WRC crystal structure, solved with Abi2): WAVE1:Abi2:HSPC300 trimer / four-helix bundle packing on Sra1.
- PMID:11516653: EYFP-Abi-2b at the tips of lamellipodia and filopodia.
- PMID:38081847 (human cells): GRAF1 phosphorylation recruits ABI2 and the WAVE2 complex to damaged mitochondria; branched actin is needed for mitochondrial clearance.
- PMID:18632609: TRIM32 binds and ubiquitinates Abi2, driving its degradation.
- Human ABI2 review (genes/human/ABI2) was the source of the ISO rows.

## Decisions
- Core: signaling adaptor activity (the best available MF for a non-catalytic WRC subunit), SCAR complex, lamellipodium/filopodium tip, positive regulation of Arp2/3 nucleation and of lamellipodium assembly, Rac signalling, cell migration.
- Neuronal (spine, synapse, SynGO-style rows), lens, AJ, memory, and mitophagy rows are kept as non-core: each is a tissue- or context-specific deployment of the WRC function.
- dendrite development (IMP): marked over-annotated, because the measured phenotype concerns spines, not dendrite development generally; GO:0061001 captures it.
- identical protein binding (ISO): marked over-annotated; the human source is high-throughput only, and ABI is a single subunit in the WRC.
- small GTPase binding is kept with contributes_to, which is correct because Rac1 binds CYFIP, not ABI2.
- No NEW terms were proposed. Kinase binding (Abl SH3 interaction) is by similarity only for mouse.

## Deep research (falcon) cross-check
- Abi2-deep-research-falcon.md agrees with the review: non-enzymatic WRC adaptor; Abl SH3 interaction; localization at lamellipodia, forming adherens junctions and dendritic spines. It also notes PIM1 phosphorylation of Ser183, which stabilizes ABI2 (Jensen et al. 2023, human). No change to any annotation decision.
