# mlaC (P0ADV7) curation notes

## Deep research
- `just deep-research ECOLI mlaC --provider perplexity` was attempted on 2026-10-23 and failed:
  "Provider 'perplexity' not available. Available: falcon, openscientist". No deep-research file
  generated; review based on cached primary literature and UniProt.

## Literature summary
- Founding Mla paper (mlaC mutants accumulate outer-leaflet PL) [PMID:19383799 "We propose that the Mla pathway constitutes a bacterial intermembrane PL trafficking system."]
- 1.5 Å crystal structure with diacyl lipid in hydrophobic pocket; binds MlaFEDB, MlaD, MlaA-OmpF [PMID:28388411 "The two acyl chains of the lipid insert snugly into the protein core where they are protected from solvent"].
- MlaD spontaneously transfers PLs to MlaC (higher affinity in MlaC) [PMID:30284446 "we demonstrated using purified proteins that MlaD spontaneously transfers PLs to MlaC"].
- Point-to-point [14C]-PL transfer between MlaC and MlaFEDB nanodiscs; ATP drives net retrograde transfer [PMID:34873038 "Therefore, we have shown that PLs equilibrate between MlaC and MlaFEDB, and ATP hydrolysis drives overall transport in the retrograde direction."]
- Apo-MlaC structure, pivoting beta-sheet; authors argued for anterograde export (disputed) [PMID:31235958].
- MlaC-MlaD cryo-EM at 1:6 and 2:6 stoichiometry [PMID:39080293].
- MlaC docks at MlaA periplasmic base [PMID:38092770].

## Decisions
- Protein binding (MlaD IPI): REMOVE per policy.
- Phospholipid transport IMP: MODIFY -> GO:0120010 (refinement).
- GO:0030288 IBA/IDA: ACCEPT. GO:0042597 IEA: MODIFY -> GO:0030288.
- GO:0120010 IBA/IDA: ACCEPT.
- NEW: GO:0120014 phospholipid transfer activity (IDA, PMID:34873038) and GO:0005543 phospholipid binding
  (IDA, PMID:28388411). GO:0120014 is not an is_a descendant of GO:0005543, so both are informative.
- Core functions: (1) GO:0120014 (primary; definition matches the MlaC carrier exactly);
  (2) GO:0005543 binding state, retained so the module's MlaC annoton (GO:0005543) has gene-level grounding.
