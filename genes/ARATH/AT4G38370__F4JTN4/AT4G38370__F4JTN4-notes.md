# AT4G38370__F4JTN4 (F4JTN4, At4g38370) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM file or prediction-evidence folder was opened.

### Entry identity and folder choice

- F4JTN4 is the UniProt reference-proteome (UP000006548) entry for At4g38370, from the genome
  annotation (EMBL AEE86920.1, RefSeq NP_568040.1). It carries the locus's TAIR GO rows.
- Its 225-residue sequence is identical to Q0WW53 (RIKEN cDNA entry), which is reviewed in
  `genes/ARATH/AT4G38370/` [file:ARATH/AT4G38370__F4JTN4/AT4G38370__F4JTN4-bioinformatics/RESULTS.md
  "- Identical sequences: True"]. Because the symbol folder is taken by Q0WW53, this entry uses the
  `<HOST>__<ACC>` convention, fetched with `just fetch-gene ARATH F4JTN4 --alias AT4G38370__F4JTN4`.
- Because the sequences are identical, the catalytic-residue mapping made for Q0WW53
  (`genes/ARATH/AT4G38370/AT4G38370-bioinformatics/RESULTS-rereview.md`) applies residue for residue
  and is cited, not repeated.

### Deep research

- `just deep-research-falcon ARATH F4JTN4 --alias AT4G38370__F4JTN4 --fallback perplexity-lite`
  failed: falcon "Failed to authenticate", perplexity fallback HTTP 401 (quota exceeded). No
  deep-research file exists in this folder. The falcon report for the same locus in the Q0WW53
  folder is used instead [file:ARATH/AT4G38370/AT4G38370-deep-research-falcon.md "Exact searches for
  AT4G38370 and Q0WW53 did not identify a publication establishing its reaction, substrate, cellular
  localization, physiological pathway, or mutant phenotype."].
- PubMed/Europe PMC rechecks (done for the Q0WW53 re-review on the same day) found no functional
  study of At4g38370, Q0WW53 or F4JTN4.

### Evolutionary placement (no transfer possible)

- PANTHER PTHR47821, single subfamily SF2; PANTHER 19 tree root PTN005357400, 47 leaves (plants,
  algae, diatom, Monosiga). No Swiss-Prot members, no human/yeast/E. coli members, no PAINT/IBA
  annotations. No experimentally characterised member exists, so no function is transferred.
- Characterised branch-1 enzymes (PGAM1, GpmA in PTHR11931; TIGAR in PTHR46517) are in different
  PANTHER families and serve only as fold-level comparators for catalytic-residue retention.

### New bioinformatics (`AT4G38370__F4JTN4-bioinformatics/sequence_features.py`)

- Confirms identity to Q0WW53. No classical pat4, pat7 or bipartite NLS pattern. N-terminal
  hydrophobicity is low (max KD window mean 0.15), so no signal peptide. No positive sequence signal
  for nuclear targeting.

### Decisions on GOA rows

- GO:0003674 ND: ACCEPT. No experimental MF; predicted catalysis is too unspecific to replace ND.
- GO:0008150 ND: ACCEPT. No process known; nothing transferable from other families.
- GO:0005634 nucleus ISM (AtSubP): UNDECIDED. Single classifier prediction, no NLS, no experimental
  localisation; neither supported nor contradicted.

### Core function

- Predicted histidine-dependent phosphotransfer catalysis (His17/Glu109/His173 retained); no GO MF
  asserted. Two BIOLOGY knowledge gaps (substrate/reaction; localisation) with matching experiments.

### What is experimentally established in this species

- Only that the protein is expressed (large-scale proteomics, PMID:22223895; PE level 1). Every
  functional statement in the review is a sequence-based inference.
