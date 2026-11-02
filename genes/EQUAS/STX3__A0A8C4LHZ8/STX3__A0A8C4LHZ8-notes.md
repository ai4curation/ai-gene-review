# STX3 (donkey, A0A8C4LHZ8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of A0A8C4LHZ8, the UniProt gene-centric canonical protein of donkey STX3
(Ensembl ENSEASG00005007989), as the characterised relative of the ProtNLM2 benchmark model
A0A9L0J901 (`genes/EQUAS/STX3`). No ProtNLM2 files or prediction-evidence folders were opened.

### Setup

- Folder `STX3__A0A8C4LHZ8` because `genes/EQUAS/STX3` already holds A0A9L0J901. Fetched with
  `just fetch-gene EQUAS A0A8C4LHZ8 --alias STX3__A0A8C4LHZ8`; stub id confirmed as A0A8C4LHZ8.
- Deep research failed: falcon "Failed to authenticate"; the perplexity-lite fallback returned HTTP
  401 (insufficient quota). No deep-research file exists. Literature was gathered from PubMed searches
  and cached with `just fetch-pmid`.

### Identity and evolutionary grounding

- PANTHER PTHR19957:SF34 (SYNTAXIN-3), same subfamily as human Q13277, mouse Q64704, rat Q08849.
- `STX3__A0A8C4LHZ8-bioinformatics/RESULTS.md`: 96.5-97.9 percent identity to human/rodent syntaxin 3A;
  61.6 percent to STX1A, 40.1 percent to STX4. FMDE apical targeting motif at residues 31-34; zero-layer
  Q225; Phobius TM 264-288.
- `../STX3/STX3-bioinformatics/RESULTS-rereview.md` classifies this product as syntaxin 3A (3A exons for
  both SNARE C-terminal half and anchor). Syntaxin 3B is the retinal ribbon-synapse form and kidney expresses
  only 3A [PMID:18683220 "In contrast, nonneuronal tissues, such as kidney, express only syntaxin 3A."], so
  3B-specific functions (ribbon synapse exocytosis, photoreceptor) were not transferred.
- PAINT: fusogenic activity, vesicle fusion, SNARE complex, endomembrane system and intracellular protein
  transport at the family-wide node PTN000461349; exocytosis and plasma membrane at PTN000461524;
  postsynapse and exocytic insertion of neurotransmitter receptor at PTN002717040 (single seed MGI:103077,
  from PMID:23395379). No PAINT node asserts apical plasma membrane.

### Literature (mammalian syntaxin 3, not donkey)

- Apical plasma membrane SNARE in polarised epithelia, targeted by FMDE motif [PMID:16785322 "This result
  indicates that the apical targeting signal of syntaxin 3 is centered around the first four residues (FMDE)
  of this conserved motif and that the residues F31, D33, and E34 play a critical role."].
- Complexes with Munc-18-2, SNAP-23 and cellubrevin [PMID:9701566]; Munc18-2/Vamp7/Stx3 apical cargo
  exocytosis [PMID:26553929]; CFTR exocytosis [PMID:20844248]; apical protein delivery [PMID:11003604].
- Human loss of function causes variant MVID [PMID:24726755 "STX3 is an apical receptor involved in membrane
  fusion of apical vesicles in enterocytes."].
- Mast cell regulated and compound exocytosis [PMID:30563839, PMID:24323579]; beta-cell newcomer granule
  fusion [PMID:23132338]; postsynaptic AMPAR exocytosis in LTP [PMID:23395379]; neurite growth and
  arachidonic acid target [PMID:16598260] (not annotated: outgrowth is a downstream outcome).

### Decisions

- ACCEPT: SNARE binding, fusogenic activity, plasma membrane, exocytosis, vesicle fusion, SNARE complex.
- KEEP_AS_NON_CORE: intracellular protein transport, endomembrane system, postsynapse, exocytic insertion of
  neurotransmitter receptor to postsynaptic membrane (lineage-specific PAINT node; splice form used in the
  LTP study unspecified).
- MODIFY: membrane -> plasma membrane; vesicle-mediated transport -> exocytosis + vesicle fusion; membrane
  fusion -> vesicle fusion.
- MARK_AS_OVER_ANNOTATED: cytoplasm (ARBA), plasma membrane bounded cell projection (ARBA).
- NEW: apical plasma membrane (ISS), on ortholog plus conserved-motif evidence; PAINT omission noted and
  raised as a suggested question rather than treated as a contradiction.
- Nothing is experimentally established in donkey; every function is an orthology inference.
- Validation warning: local ontology cache still labels GO:0005484 "SNAP receptor activity"; GOA label
  "helical-bundle zippering fusogenic activity" kept as provided.
