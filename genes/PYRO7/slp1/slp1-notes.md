# slp1 (G4N906, MGG_10097) – Magnaporthe oryzae Secreted LysM Protein 1 – curation notes

## 2026-10-02 initial review

Sources: UniProt G4N906 (Swiss-Prot), slp1-deep-research-falcon.md, cached PMID:22267486 (abstract only),
PMID:24642938 (abstract only, newly cached; PMID verified by PubMed search), PMID:34761375 (full text).

### Biology
- Secreted during invasion of rice cells; accumulates at fungal wall / rice plasma membrane interface
  [PMID:22267486 "We demonstrate that Slp1 accumulates at the interface between the fungal cell wall and the rice plasma membrane"].
- Apoplastic effector in the EIHM compartment, not BIC; secretion requires COPII cargo receptor MoErv29
  [PMID:34761375 "the apoplastic effector MoSlp1 was found within the EIHM compartment in Guy11 but not the ΔMoerv29 mutant"].
  (Note: the task brief says "biotrophic interface"; strictly it is the apoplastic EIHM interface, not the BIC.)
- Binds chitin; competes with CEBiP; suppresses ROS + defense gene expression
  [PMID:22267486 "Slp1 competes with CEBiP for binding of chitin oligosaccharides"].
- Required for full virulence; dispensable when CEBiP silenced
  [PMID:22267486 "gene silencing of CEBiP in rice allows M. oryzae to cause rice blast disease in the absence of Slp1"].
- Alg3 N-glycosylation at 3 sites needed for stability and chitin binding
  [PMID:24642938 "required to maintain protein stability and the chitin binding activity of Slp1"].
- Deep research: SPR Kd 2.4 nM for (GlcNAc)8; no chitinase protection (unlike Avr4); homodimer (UniProt).

### Annotation decisions
- GO:0005576 extracellular region EXP + IEA: ACCEPT.
- GO:0140403 effector-mediated suppression of host innate immune response (TAS, PHI-base, PMID:34761375):
  MODIFY -> GO:0140423 effector-mediated suppression of host PTI signaling (QuickGO-verified; is_a
  GO:0052034 is_a GO:0140403). Cited paper is about MoErv29 secretion, not Slp1 activity; real evidence is
  PMID:22267486. Matches ECP6 (FULFL) which carries GO:0140423 by EXP.
- NEW GO:0008061 chitin binding (IDA, PMID:22267486). Comparators: ECP6 (IDA), OsCEBiP.

### Project question notes
- Q1: Only process term is symbiont-side (GO:0140403); no plant-side defense terms. Backed by literature
  (TAS), not IEA, though the TAS citation is the wrong paper.
- Q2: No InterPro2GO leakage: no receptor/perception terms on Slp1; chitin binding was missing entirely,
  even though it is the defining activity (no IEA from LysM domain maps it).
