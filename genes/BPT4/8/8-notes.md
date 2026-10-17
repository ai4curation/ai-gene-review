# Gene 8 (gp8) Curation Notes — Bacteriophage T4 (P19062)

## Overview
- **Gene symbol**: `8` (encodes baseplate wedge protein gp8)
- **UniProt accession**: `P19062`
- **Organism**: *Tequatrovirus T4* (Bacteriophage T4; `NCBITaxon:10665`)

## Biological Role and Architecture
- **Intermediate baseplate wedge clamp**: gp8 (334 aa, ~38 kDa) forms a homodimer (6 dimers = 12 copies per baseplate) localized in the intermediate region of each of the six baseplate wedges (`file:BPT4/8/8-uniprot.txt`; `file:BPT4/8/8-deep-research-falcon.md`).
- **Role in ordered wedge assembly**: In the strictly sequential assembly pathway of the T4 baseplate wedge (`gp10 + gp7 -> gp10-gp7 + gp8 -> gp10-gp7-gp8 + gp6 -> + gp53 + gp25`), the gp8 homodimer binds to a flexible linker of gp7 that becomes stretched upon gp10-gp7 complex formation. By clamping and stabilizing this gp7 linker, gp8 reduces gp7 flexibility and positions gp7 so that two copies of gp6 can bind productively to complete the wedge core (`file:BPT4/8/8-uniprot.txt`; `file:BPT4/8/8-deep-research-falcon.md`, PubMed 27193680).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0098003` (`viral tail assembly`, IEA): Essential wedge assembly factor required for gp6 recruitment and completion of the six baseplate wedges.
  - `GO:0098025` (`virus tail, baseplate`, IEA/IDA): Directly resolved in the intermediate wedge region of the baseplate by X-ray crystallography and atomic cryo-EM (PubMed 27193680).
- **MODIFY**:
  - `GO:0098015` (`virus tail`, IEA) -> `GO:0098025` (`virus tail, baseplate`).
