# ARL16 notes

- RIG-I inhibitor [PMID:21233210], human cells:
  - GTP-bound ARL16 binds the RIG-I CTD and blocks RNA binding.
  - Knockdown potentiates virus-induced IFN-beta.
- Cilia [PMID:35196065]:
  - Endogenous ARL16 sits along the ciliary axoneme in human RPE1 cells, plus cytosol and mitochondria (HSP60).
  - In human retina it is in the photoreceptor ciliary region and inner segment.
  - Arl16 knockout MEFs: fewer but longer cilia; IFT140 and INPP5E stuck at the Golgi.
- Atypical G-3 motif [PMID:38606629].

## GOA calls
- **Protein binding (30 rows) → REMOVE.** These are Y2H screens (neurodegeneration map, HuRI, HI-II-14) plus RIG-I. The RIG-I biology moves to a NEW BP row.
- **ACCEPT:** GTP binding, axoneme, cytoplasm.
- **UNDECIDED:** GTPase activity (atypical G-3; no hydrolysis measured).
- **Non-core:** mitochondrion, photoreceptor inner segment.
- **NEW:**
  - Negative regulation of RIG-I signaling pathway (IMP, human).
  - Protein localization to cilium (ISO from mouse Arl16, MGI:1917567).

## Review round 1 (PR #4178)
- NEW ciliary basal body (IDA, PMID:35196065), from the photoreceptor centrin 3 co-staining; UniProt records this location but GOA lacks it. Added as a core-function location.
- GTP binding now quotes the radiolabelled-GTP binding assay and the T37N / delta45-54 GTP-free mutants (PMID:21233210).
- Cytoplasm rows now quote only the diffuse cytosolic staining.
- Mitochondrion row notes the authors' attribution to a longer ARL16 variant.
- ISO donor MGI:1917567 verified as mouse Arl16 (UniProt B1ATY8).
