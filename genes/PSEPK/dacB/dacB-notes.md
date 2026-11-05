# dacB (PSEPK, UniProt Q88L37) curation notes

## 2026-11-04 (Claude, AI-assisted), PR #5959 review follow-up

- Dropped the NEW row GO:0031504 peptidoglycan-based cell wall organization and
  took the term out of core_functions. Its only support was the P. aeruginosa
  bifunctional enzymology (PMID:27716106), which establishes the activity, not a
  cell-wall-organization process. The PBP4 phenotype evidence (PMID:16855223, E.
  coli) is about daughter-cell separation, and the E. coli review now records it
  as GO:0000920 septum digestion after cytokinesis. No PBP4 review (E. coli,
  P. aeruginosa, P. putida) now carries GO:0031504, so the three dacB reviews and
  the PBP7 reviews agree. GO:0000270 records the direct participation.
- The GO:0006508 InterPro2GO removal is recorded as a source defect addressed to
  InterPro (IPR000667), not GOA-EBI.
