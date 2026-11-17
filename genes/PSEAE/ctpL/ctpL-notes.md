# ctpL (PA4844, Q9HUW6) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUW6 --alias ctpL` (accession fetch after the
symbol query hit a UniProt 429). Accession Q9HUW6 matches the worklist. No deep-research
provider keys were available; literature is from the cached publications and the UniProt
record. Seed papers PMID:10852870, PMID:24038698 are abstract-only (PMC101905, PMC3837763
full text not retrievable through the PubMed MCP or Europe PMC); PMID:27353565 full text
is cached.

## Identity

- MCP chemoreceptor, PTHR32089:SF119. Two TM helices (6-26, 306-326) around a large
  periplasmic region (27-305), then cytoplasmic HAMP (327-380) and MCPsignal (385-621)
  domains. Belongs to the Pho regulon (induced by Pi limitation via PhoB; repressed by
  PhoU) [PMID:10852870].

## Literature

- Pi chemoreceptor. The ctpL mutant fails to respond to low (0.01 mM) Pi, and the ctpH
  ctpL double mutant is defective in Pi taxis at all concentrations
  [PMID:10852870 "Conversely, the ctpL single mutant could not respond to P(i) at the concentration of 0.01 mM."];
  [PMID:10852870 "The ctpH ctpL double mutant was defective in P(i) taxis at any concentration ranging from 0.01 to 10 mM."].
- Indirect sensing. CtpL does not bind Pi directly; the Pi-loaded periplasmic binding
  protein PstS binds CtpL and stimulates it
  [PMID:27353565 "We demonstrate that the ligand binding domain (LBD) of CtpH but not CtpL binds Pi directly."];
  [PMID:27353565 "We identify the periplasmic ligand binding protein PstS as the protein that binds in its Pi loaded state to CtpL, resulting in receptor stimulation."].
- Also the 4-chloroaniline / catechol chemoreceptor (screen of all 26 MCP mutants)
  [PMID:24038698 "CtpL, a chromosomally encoded chemoreceptor, was responsible for the positive chemotactic response toward 4CA."].

## Annotation decisions

- Chemotaxis (IBA, IEA, IMP), detection of phosphate ion (IMP), positive chemotaxis
  (IMP): ACCEPT (core). Transmembrane signaling receptor activity (IEA): ACCEPT core MF.
  Plasma membrane (IEA): ACCEPT. Signal transduction (IEA): MODIFY to GO:0007166.
  Membrane (IEA): TOO_GENERAL (plasma membrane entails it).
- Action counts: ACCEPT 6, MODIFY 1, TOO_GENERAL 1.
- No source defects; the PseudoCAP seed row is sound.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001280296 | GO:0006935 chemotaxis | 10 | 215 (22 taxa) | GO:0006935, IMP, PMID:10852870 | SOUND | The ctpL mutant loses low-Pi taxis and the ctpH ctpL double mutant loses Pi taxis at all concentrations; CtpL is the receptor that transduces the stimulus (via Pi-loaded PstS). Also the 4CA/catechol receptor (PMID:24038698). | PctA, PctB, PctC, CtpH, CtpM, Aer (PseudoCAP IMP); B. subtilis McpC (IDA/IMP positive chemotaxis); B. subtilis and H. salinarum HemAT (IDA aerotaxis) | Yes; independent IDA seeds and six other PseudoCAP seeds |

The node-level assessment of PTN001280296 is recorded once in `pctB-notes.md` (all five
chemoreceptors reviewed in that batch SOUND; node term chemotaxis suits the PTHR32089 MCP
clade; no GO_CENTRAL defect). ctpL is consistent with it. The only leaf oddity (Dictyostelium
AlyL lysozyme-like proteins placed in the clade) is a PANTHER family-placement issue raised
on pctB.
