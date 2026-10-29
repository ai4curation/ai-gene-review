# VRN2 curation notes

## Session 2026-10-05 (vernalization_flc_silencing module)

- Q8W5B1, At4g16845; Su(z)12 homolog (VEFS box). Falcon deep research failed.
- Maintenance, not initiation: [PMID:11719192 "In vrn2 mutants, FLC expression is downregulated normally in response to vernalization, but instead of remaining low, FLC mRNA levels increase when plants are returned to normal temperatures."]
- Constitutive association with FLC: [PMID:18854416 "VRN2 associates throughout the FLC locus independently of cold."]
- In vivo VRN2-PRC2: [PMID:26642436 "confirming that CLF occurs in both VRN2-PRC2 and EMF2-PRC2 complexes in vivo."]
- PHD-PRC2: [PMID:18854416 "a PHD-PRC2 complex forms composed of core PRC2 components (VRN2, SWINGER"].

## Decisions
- ISS DNA-binding transcription factor activity (from the Riechmann 2000 TF catalog) -> REMOVE; VRN2 is a PRC2 subunit, not a TF. The IEA regulation of DNA-templated transcription derived from it -> MODIFY to GO:0045814.
- Transcription corepressor binding (IPI with AGAMOUS, PMID:28825728) -> MODIFY to DNA-binding transcription factor binding (GO:0140297); the partner given in GOA is a MADS TF. The full text was not available.
- IBA DNA methylation-dependent constitutive heterochromatin (FIS2 seed) -> MODIFY to facultative heterochromatin formation.
- Seven protein binding rows -> REMOVE (complex membership captured by CC).
- NEW: part_of ESC/E(Z) complex (GO:0035098).
- Core function: contributes_to histone H3K27 methyltransferase activity (catalysed by CLF/SWN).
