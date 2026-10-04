# ANKRD40 notes

- Uncharacterized; brain-enhanced (HPA). PAN-GO 0. PTHR24192 has no annotated PAINT nodes; the metadata and entries files are committed.
- 18 × GO:0005515:
  - **AHCY ×6 → MODIFY to GO:0019899 enzyme binding.** These come from Rolland Y2H, Sahni 2015, Fragoza 2019, BioPlex 2.0 and 3.0, and OpenCell (endogenous tagging); IntAct NbExp=10. It is the one reproducible interaction.
  - The other 12 rows (FXR1, SDCBP, RAD23A, PIN1, LTA, RCBTB1, ULK4, RFC3) are single-screen hits → REMOVE.
- ND rows: MF ND → REMOVE, since the AHCY enzyme binding supersedes it. CC and BP ND → ACCEPT. The MZF1 nuclear-body interactome [PMID:39954358, abstract] lists ANKRD40 under "protein folding" as a category label, which does not establish a location or process.
- knowledge_gaps: WHOLLY_DARK, with the AHCY interaction as the concrete lead.

## Round 2 (reviewer, PR #4130)

- **New finding from the reviewer's OpenCell suggestion.** OpenCell did tag ANKRD40 (cell line 1389, N-terminal, HEK293T): golgi_3, cytoplasmic_1, vesicles_1. The OpenCell legend defines grade 3 as "Prominent signal" (read from the site bundle by ANKRD40-bioinformatics/opencell_localization.py). Changes:
  - NEW GO:0005794 Golgi apparatus (IDA, PMID:35271311).
  - The CC ND row becomes REMOVE, as superseded.
  - The gap becomes MF_DARK, since a location is now known.
  - AHCY in OpenCell is cytoplasmic and nucleoplasmic (grade 3), not Golgi. Where the two proteins meet is a question.
- The boundary now states the actual criterion, cross-method reproducibility. PIN1 recurs in two Y2H maps, and LTA, RCBTB1 and ULK4 in two BioPlex releases, but none spans methods.
- The REMOVE reasons now state the removal rationale, not just the deposited interaction. The BP reason cites the PTHR24192 metadata (go_terms: null). The six AHCY-source papers are now relevance MEDIUM.
