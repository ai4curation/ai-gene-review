# ispB review notes (P. putida KT2440, Q88Q11, PP_0687)

Reviewed for the ubiquinone_biosynthesis module; checked for consistency with
E. coli IspB (genes/ECOLI/ispB).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. The UniProt
  entry is unreviewed and its name, EC and reaction rest on ARBA only, so they
  are not used as support.
- Own analysis: `ispB-bioinformatics/` (global alignment with E. coli IspB,
  51.6% identity, chain-length residues and DDxxD motif conserved).

## Chain length

- P. aeruginosa makes Q9. [PMID:32409583 "we established that UQ9 is the major
  quinone of Pseudomonas aeruginosa"] The P. putida pathway audit in
  projects/P_PUTIDA also assumes UQ-9 but notes it was not measured.
- GO:0106350 (octaprenyl, C40) is therefore MODIFIED to the parent
  GO:0120531 prenyl diphosphate synthase activity; GO has no FPP-primed
  nonaprenyl term.
- The module lists Q88Q11 as a representative of the GO:0106350 IspB annoton;
  this should be revisited (coordinator informed).
- A NEW ISS row for ubiquinone biosynthetic process was added, matching E. coli
  IspB.
