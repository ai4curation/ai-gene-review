# Cd48 (mouse, P18181) review notes

## 2026-10-04
- Deep research NOT run: all providers broken in this environment (falcon 402, openai 401, perplexity missing). Review based on UniProt P18181, cached GOA PMIDs, and the human CD48 review (genes/human/CD48).
- Fetched PMID:9881969 and PMID:17950006 (identifiers taken from the UniProt P18181 reference list; cached titles/abstracts confirmed correct).
- Key mouse evidence:
  - CD48 is the mouse CD2 counter-receptor, GPI-anchored [PMID:1383383 "These results indicate that CD48 is a ligand for mouse CD2 and is involved in regulating T cell activation."]
  - mCD48 binds m2B4 [PMID:9841922 "purified soluble mCD48 bound m2B4 with a six- to ninefold higher affinity (Kd approximately 16 microM at 37 degreesC) than its other ligand, CD2."]
  - CD2:CD48 enhances TCR signaling via rafts [PMID:9881969 "We demonstrate that CD2:CD48 interactions enhance TCR-mediated functions."]
  - Mouse NK: 2B4/CD48 reported inhibitory [PMID:16002700 "In human NK cells, 2B4/CD48 interaction induces activation signals, whereas in murine NK cells it sends inhibitory signals."]
- Could not verify a PMID for the Cd48-/- T cell activation knockout paper (bgpt quota exhausted); not cited.
- Decisions: protein binding (CD2) -> MODIFY to GO:0050839; protein-containing complex (rat ISO) -> over-annotated; extracellular region rows non-core; others accepted.
