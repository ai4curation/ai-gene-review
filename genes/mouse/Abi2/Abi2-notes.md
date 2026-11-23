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

## 2026-10-12 Ortholog/family audit

- GOA refreshed: no change; all GOA rows covered (59 rows, 51 entries, duplicates differing only in WITH/FROM).
- Compared with genes/human/ABI2 and genes/human/ABI3 (no ABI1/Abi1 review exists; genes/ARATH/ABI1 is an unrelated ABA-insensitive phosphatase). All three share PANTHER PTHR10460 and treat signaling adaptor activity + SCAR complex as the core function; family IBAs (lamellipodium, SCAR complex, signaling adaptor activity, actin-based cell projection, neuron migration non-core) are handled identically.
- Mitophagy (GO:0000423): mouse ISO kept as non-core, but the human source IDA (PMID:38081847) had been marked over-annotated. The full text shows ABI2 is the WRC subunit bound directly by the phosphorylated GRAF1 SH3 domain [PMID:38081847 "Using GST-fusion precipitation, we further confirmed a direct association between ABI2 and GRAF1 and mapped the interaction site to the GRAF1 SH3 domain"], though ABI2 itself was not depleted. Harmonized the human review to KEEP_AS_NON_CORE, deferring to the experimental curator.
- Small GTPase binding (GO:0031267, contributes_to): human IDA was MODIFY to signaling adaptor activity, ignoring the contributes_to qualifier; mouse ISO kept as non-core. Harmonized human to KEEP_AS_NON_CORE (complex-level activity via SRA1/CYFIP1).
- Minor residual differences left as reviewer judgement: nucleus/nucleoplasm and identical protein binding are MARK_AS_OVER_ANNOTATED in mouse but KEEP_AS_NON_CORE in human; ubiquitin protein ligase binding is non-core in mouse, ACCEPT in human.
