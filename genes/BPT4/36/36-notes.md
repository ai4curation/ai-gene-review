# Curation Notes: Bacteriophage T4 gene 36 (gp36; UniProt P03743)

## Identity and Nomenclature
- **Gene symbol**: `36`
- **Protein**: Long-tail fiber protein gp36 (221 aa, ~23.3 kDa)
- **UniProt**: `P03743` (`GP36_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Homotrimeric proximal subunit ("upper shin") of the distal long tail fiber**:
   - Each of the six ~145 nm long tail fibers (LTFs) of bacteriophage T4 has the stoichiometric composition `(gp34)3(gp35)1(gp36)3(gp37)3` (Cerritelli et al. 1996, PubMed 8635743; Leiman et al. 2010, PubMed 21138586).
   - Gene 36 encodes gp36 (221 aa, ~23.3 kDa), which forms a parallel homotrimer (~69 kDa) constituting the proximal segment ("upper shin", ~14 nm / 140 Å in length) of the ~750 Å distal half-fiber (Dickson 1973, PubMed 4583265; Cerritelli et al. 1996, PubMed 8635743; Hyman & van Raaij 2018, PubMed 29258245).
   - Within the distal half-fiber, the C-terminal domains of the gp36 trimer bind head-to-tail to the conserved N-terminal domain of the gp37 trimer ("lower shin" and adhesin tip), while the N-terminal domains of the gp36 trimer provide the binding platform for the monomeric hinge protein gp35 ("kneecap") that connects the distal and proximal (gp34) half-fibers.
2. **Ordered assembly pathway and chaperone requirement**:
   - In the LTF morphogenetic pathway, gp37 first folds and trimerizes with the assistance of the phage chaperones gp57A and gp38 (producing the `BC'` antigen intermediate).
   - Next, three copies of gp36 assemble onto the N-terminal end of the gp37 trimer with the assistance of the phage chaperone gp57A, adding the `B` antigen and lengthening the fiber by ~14 nm to form the `BBC'` intermediate (Ward et al. 1970, PubMed 4920352; Ward & Dickson 1971, PubMed 4944598).
   - Only after gp36 is incorporated can the monomeric gp35 hinge protein bind to complete the distal half-fiber (`ABBC'`) and enable joining to the gp34 proximal half-fiber (Terzaghi 1971, PubMed 4930861).

## Review of Existing GOA Annotations
- `GO:0098024` (`virus tail, fiber`, IEA `GO_REF:0000043`): **ACCEPT**. gp36 is an integral structural subunit forming the proximal shaft of the distal half of each long tail fiber.
- `GO:0098015` (`virus tail`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0098024` (`virus tail, fiber`). `GO:0098015` is a broader parent of `GO:0098024`, which is already present on the record.
- `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`, IEA `GO_REF:0000043`): **KEEP_AS_NON_CORE**. While gp37 directly binds host LPS/OmpC receptors at the distal tip, gp36 is an essential structural segment of the long tail fiber assembly that mechanically couples the receptor-binding gp37 tip to the gp35 hinge and gp34 proximal half-fiber during host attachment.
- `GO:0019062` (`virion attachment to host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`). Broader parent of `GO:0098671`.
- `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`). Overly broad keyword mapping; the LTF mediates reversible host cell attachment (`GO:0098671`) prior to baseplate triggering and genome ejection.
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): gp36 is a core structural polypeptide of the mature T4 virion long tail fiber (3 copies per LTF, 18 per virion).
  - `GO:0098004` (`virus tail fiber assembly`): Incorporation of the gp36 homotrimer onto the N-terminus of the gp37 trimer is an essential step in distal half-fiber morphogenesis required before gp35 attachment.
