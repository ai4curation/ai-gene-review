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

## 2026-10-12 Ortholog/family audit

- GOA refreshed (`just fetch-gene mouse Cd48`): no change in rows; all 31 GOA rows covered (the two RGD-derived GO:0032991 ISO rows are a duplicate pair covered by one entry). The NEW GO:0045953 entry is not a GOA row and is retained.
- Compared with genes/human/CD48 (DRAFT) and genes/rat/Cd48 (DRAFT). No other SLAM-family reviews (CD2, CD244, SLAMF*) exist in the repository yet.
- Heterotypic cell-cell adhesion (GO:0034113, IBA, PTN008532944): rat ACCEPTs as core, human keeps as non-core, mouse had kept as non-core. Rodent CD48 is the principal CD2 counter-receptor and the weak CD2-CD48 adhesion is measured directly with the murine proteins [PMID:12356317 "these measurements between extended membrane surfaces directly confirm that the low-affinity CD2-CD48 bond generates weak adhesion"]; human CD2 binds mainly CD58. Mouse flipped to ACCEPT and the term added to the CD2-ligand core function, matching rat. Human left as non-core (species difference, not an inconsistency).
- Natural killer cell activation (GO:0030101): human ACCEPT (activating CD48-2B4 axis in human), rat UNDECIDED (no rat data), mouse MODIFY to regulation of NK cell activation (inhibitory in mouse [PMID:15123744 "NK lysis of CD48(+) tumor and allogeneic targets is inhibited by 2B4 ligation"]). These differences reflect documented species divergence and were left as is.
- Mast cell activation, protein-containing complex, membrane raft, receptor ligand activity: consistent across the three rodent/human reviews.
- No donor-side defects found in human or rat CD48 that required editing.
- Status set to COMPLETE.
