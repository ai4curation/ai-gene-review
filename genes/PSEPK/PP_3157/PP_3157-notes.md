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
- 2026-11-11 (PR #6250 review): the TIGR02067 model description associates HisN with histidine
  prototrophs lacking HAD- or PHP-type HolPases, but KT2440 also encodes the HAD-type PP_5147
  (NF052360, reciprocal best hit of PA0335). KT2440 therefore does not fit that distribution
  expectation, so the ACCEPT rests only on the TIGR02067 score and the motif-5/motif-6 signatures,
  not on the distribution argument. PMID:28720084 itself shows family-model membership alone is not
  decisive (only one of C. glutamicum's four hisN homologs has HolPase activity), which is why the
  motif evidence is required. Also noted in the description: motif-1 Gly41 (Asp in validated
  HisN) and motif-3 Arg (Lys preferred). The PROSITE PS00629 quote moved to the GO:0042578 row,
  since an IMPase-superfamily signature supports membership, not HolPase specificity.
