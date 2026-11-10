# PP_3157 (Q88I44) - Pseudomonas putida KT2440 curation notes

- New deep research could not be generated in this session (no provider API keys); the existing
  OpenScientist report (PP_3157-deep-research-openscientist.md) was used as secondary triage only.
- 2026-11-10: resolved the two UNDECIDED rows with a reproducible analysis,
  `PP_3157-bioinformatics/hisn_motif_analysis.py` (output in `PP_3157-bioinformatics/RESULTS.md`).
  Run from the repo root with `--cache-dir <download dir>`; downloads NCBIfam HMMs and UniProt
  proteomes, uses biopython + pyhmmer from the shared environment.
  - PP_3157 is the only KT2440 protein above the TIGR02067 (his_9_HisN) trusted cutoff; PAO1 has none
    (it uses the HAD-type PA0335). KT2440 CysQ is PP_0261 (TIGR01331), so PANTHER's CysQ-named
    subfamily PTHR43200:SF6 for PP_3157 is a naming artefact.
  - HisN motif residues from [PMID:28720084 "Motif 5 is the most characteristic motif of HisN
    orthologs."] are present: motif-5 R/G/D with aromatic flanks, motif-4 W..T L, motif-6 non-Gly.
    The C. glutamicum HisN control carries all 19 paper-named residues, validating the numbering.
  - One deviation: position 38 (motif 1, "highly conserved aspartate") is Gly in PP_3157.
- Broad phosphatase / phosphoric ester hydrolase rows changed to TOO_GENERAL (entailed by GO:0004401).
- Open biology: no KT2440 assay; flux sharing with the HAD-family PP_5147 is unknown.
