# BURP16 (OsBURP16, OsWGP1; Q7XES5; Os10g0409400) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: OsBURP16 was requested as the closest experimentally studied relative of the
ProtNLM2 benchmark gene ORYSI/B8BAB0 (indica allele of OsBURP12). No ProtNLM2 file or
prediction-evidence folder was opened for this review.

### Data state
- `just fetch-gene ORYSJ BURP16` created the UniProt and GOA files. GOA has **zero**
  annotations for Q7XES5 (no IEA, no IBA, no experimental rows).
- Deep research failed: falcon "Failed to authenticate"; the perplexity-lite fallback
  returned HTTP 401 (insufficient quota). No deep-research file exists. The review uses
  the cached publications listed below plus a web search, which found no further
  primary literature on this gene.

### Sequence and family
- 344 aa, signal peptide 1-25 (sequence analysis), BURP domain 128-341, four predicted
  N-glycosylation sites; PE 2 (transcript level) in UniProt.
- PANTHER PTHR31458:SF2. In the PANTHER 19 tree its only relative below the grass
  duplication node PTN000779097 is OsBURP12 (Q6ZA27); eudicot PG1beta-like proteins
  (tomato GP1, AtPGL1-3) join only at the Mesangiosperma node PTN004827825
  [file:ORYSJ/BURP16/BURP16-bioinformatics/RESULTS.md].
- The only PAINT IBD in the family (PTN004827911, Brassicaceae, seed AT1G70370) does not
  cover OsBURP16, so cell-wall terms were not propagated to it. I treat that as a
  deliberate curator decision and do not add GO:0009505 plant-type cell wall.
- OsBURP16 lacks the FTNYG/FxxY repeat region entirely (0 units vs 21 FxxY in tomato
  GP1) but keeps the four BURP CH dipeptides at the conserved spacing. The defining
  structural feature of the tomato PG1 beta subunit is therefore absent.

### Literature
- Ding et al. 2009 [PMID:19363683 "Two genes (OsBURP05 and OsBURP16) were responsive to
  all the stress treatments"]: genome-wide family; abstract only.
- Liu et al. 2014 [PMID:24237159]: the only functional study.
  - Expression: mainly young leaves, leaf lamina, leaf cushion and internodes;
    transcripts induced by cold, drought (PEG) and NaCl. ABA: the abstract says induced,
    but the results text says "Treatment with 100 μm ABA caused a decrease in the
    transcriptions of OsBURP16" — internal inconsistency, so I do not use ABA response.
  - Localisation: **not tested**; only a TMHMM prediction "may both mainly be localized
    outside the cell membrane".
  - Ubi::OsBURP16 overexpression (three lines): reduced uronic acid / homogalacturonan,
    weaker ruthenium red staining, 3- to 6-fold higher PG activity in young leaves,
    reduced cell adhesion and leaf breaking force, higher cuticular transpiration, and
    hypersensitivity to cold, salt and drought.
  - "Attempts to generate mutants or RNAi plants of OsBURP16 have so far not been
    successful" — no loss-of-function data exist.
  - The PG1beta-subunit identity of OsBURP16 is a family-based assumption in the paper
    ("encodes one putative PG1β subunit precursor"); no interaction with a PG catalytic
    subunit was tested.
- Jin et al. 2020 [PMID:32005373]: OsEIL2 binds the OsBURP16 promoter and activates its
  transcription; OsEIL2 overexpression lowers pectin by raising PG activity. This is
  regulation *of* OsBURP16 (abstract only).
- Tomato GP1 [PMID:1392611] and AtPGL3 [PMID:26106400]: family context only (cell wall
  localisation; GP1 associates with PG2). Not one-to-one orthologs.

### Decisions
- No existing annotations to review.
- One NEW CC: GO:0005576 extracellular region, from the signal peptide plus SF2
  membership; flagged as computational, not experimental.
- No NEW BP/MF. The overexpression phenotypes (more PG activity, less pectin) are
  consistent with OsBURP16 promoting PG action, but overexpression in planta cannot
  distinguish a direct PG-regulator role from indirect effects, and no loss-of-function
  evidence exists. Stress hypersensitivity is a downstream organismal phenotype. Stress
  induction of transcripts is expression data only.
- For transfer to B8BAB0/OsBURP12: what is experimentally established for OsBURP16 in
  rice is only (i) stress-inducible transcription and (ii) overexpression phenotypes.
  Molecular activity and localisation are inferred.
