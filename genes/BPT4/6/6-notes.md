# Gene 6 (gp6) Curation Notes — Bacteriophage T4 (P19060)

## Overview
- **Gene symbol**: `6` (encodes baseplate wedge protein gp6)
- **UniProt accession**: `P19060`
- **Organism**: *Tequatrovirus T4* (Bacteriophage T4; `NCBITaxon:10665`)

## Biological Role and Architecture
- **Inner baseplate ring and wedge assembly**: Twelve copies of gp6 (660 aa per monomer) form an interdigitated ring of six dimers that constitutes the major structural framework of the inner baseplate surrounding the central hub (`file:BPT4/6/6-uniprot.txt`; `file:BPT4/6/6-deep-research-falcon.md`, PubMed 19523898, PubMed 27193680).
- **Subunit contacts**: Within each wedge, two copies of gp6 form a `(gp6)2-gp7` heterotrimeric core module via a triple-helical bundle (two helices from the gp6 dimer and one from gp7). Across wedges, gp6 monomers interdigitate by forming an N-terminal dimer within one wedge and a C-terminal dimer with the neighboring wedge, tying the six baseplate wedges into a continuous circular ring (`file:BPT4/6/6-uniprot.txt`; `file:BPT4/6/6-deep-research-falcon.md`, PubMed 19523898).
- **Role in sheath contraction**: During the infection-triggered dome-to-star conformational transition of the baseplate, the N- and C-terminal dimer interfaces of gp6 remain intact while the internal hinge angle between its N- and C-terminal halves shifts by ~15 degrees, expanding the gp6 ring diameter by ~10 Å (`file:BPT4/6/6-deep-research-falcon.md`, PubMed 19523898). Within the `gp25-(gp6)2-gp7` module, this hinge motion repositions the gp6 N-terminal region and attached gp25 to propagate the conformational signal that initiates tail sheath (gp18) contraction (`file:BPT4/6/6-uniprot.txt`; `file:BPT4/6/6-deep-research-falcon.md`, PubMed 27193680).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0098003` (`viral tail assembly`, IEA): Essential wedge component required to circularize the six baseplate wedges and form the inner baseplate ring.
  - `GO:0098025` (`virus tail, baseplate`, IEA/IDA): Directly localized to the inner baseplate by chemical cross-linking (PubMed 2403438) and atomic-resolution cryo-EM (PubMed 27193680).
- **KEEP_AS_NON_CORE**:
  - `GO:0042802` (`identical protein binding`, IPI, PubMed 19523898): Directly supported by X-ray crystallography and cryo-EM showing N-terminal and C-terminal gp6 homodimerization; retained as non-core.
- **MODIFY**:
  - `GO:0098015` (`virus tail`, IEA) -> `GO:0098025` (`virus tail, baseplate`).
