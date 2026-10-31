# Curation Notes: Bacteriophage T4 gene 35 (gp35; UniProt P03742)

## Identity and Nomenclature
- **Gene symbol**: `35`
- **Protein**: Long-tail fiber protein gp35 ("hinge" or "kneecap" protein; 372 aa, ~40.1 kDa)
- **UniProt**: `P03742` (`GP35_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Monomeric hinge ("kneecap") connector of the T4 long tail fiber**:
   - Each of the six ~145 nm long tail fibers (LTFs) of bacteriophage T4 is assembled from a proximal half-fiber (a homotrimer of gp34) and a distal half-fiber (homotrimers of gp36 and gp37) joined at an angle by a single monomer of gp35, yielding a stoichiometric composition of `(gp34)3(gp35)1(gp36)3(gp37)3` per fiber (Cerritelli et al. 1996, PubMed 8635743; Leiman et al. 2010, PubMed 21138586; Hyman & van Raaij 2018, PubMed 29258245).
   - Unlike the trimeric fibrous shafts formed by gp34, gp36, and gp37, gp35 is an asymmetric monomer (~372 aa, ~40 kDa) that caps the N-terminal tip of the distal half-fiber (gp36 trimer) and creates the binding surface for the C-terminal domain of the proximal half-fiber (gp34 trimer), forming the characteristic "knee" bend of the LTF (Dickson 1973, PubMed 4583265; Leiman et al. 2010).
   - Assembly is strictly ordered: gp35 binds exclusively after gp36 trimerizes onto the N-terminal end of the folded gp37 trimer, converting the gp36-gp37 intermediate into the mature distal half-fiber capable of joining the gp34 proximal half-fiber (Terzaghi 1971, PubMed 4930861; Ward & Dickson 1971, PubMed 4944598). Unlike gp34, gp36, and gp37, gp35 folds as a monomer without requiring the phage chaperones gp57A or gp38.
2. **Repurposed carbohydrate-binding-like domains**:
   - Sequence and structural modeling indicate that gp35 contains tandem beta-jellyroll domains with similarity to carbohydrate-binding modules (CBMs) / PROSITE GG-type lectins (`PS51918`). However, in the LTF architecture these domains are repurposed to mediate asymmetric protein-protein interactions between the three-fold symmetric gp36 and gp34 trimers at the hinge joint rather than binding host cell surface carbohydrates directly (Hyman & van Raaij 2018, PubMed 29258245).

## Review of Existing GOA Annotations
- `GO:0098024` (`virus tail, fiber`, IEA `GO_REF:0000043`): **ACCEPT**. gp35 is an integral structural subunit forming the central hinge ("kneecap") of each long tail fiber.
- `GO:0098015` (`virus tail`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0098024` (`virus tail, fiber`). `GO:0098015` is a broader parent of `GO:0098024`, which is already present on the record.
- `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`, IEA `GO_REF:0000043`): **KEEP_AS_NON_CORE**. While gp37 forms the receptor-binding tip that directly contacts host LPS/OmpC, gp35 is an essential structural connector of the long tail fiber apparatus that transmits the receptor-binding signal from the distal half-fiber to the proximal half-fiber and baseplate during host attachment.
- `GO:0019062` (`virion attachment to host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`). Broader parent of `GO:0098671`.
- `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`). Overly broad keyword mapping; the LTF mediates reversible host cell attachment (`GO:0098671`) upstream of baseplate rearrangement and tail contraction.
- `GO:0030246` (`carbohydrate binding`, IEA `GO_REF:0000002`): **REMOVE**. Electronic inference from the PROSITE `GG_LECTIN` (`PS51918`) profile; structural and functional studies show that the CBM-like domains of gp35 form the protein-protein hinge interface linking the gp36 and gp34 trimers rather than functioning as a lectin/carbohydrate-binding adhesin.
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): gp35 is an essential structural protein of the T4 virion long tail fiber (1 monomer per LTF, 6 per virion).
  - `GO:0098004` (`virus tail fiber assembly`): Attachment of gp35 to the N-terminus of the gp36-gp37 complex is a required morphogenetic step that licenses joining of the distal and proximal half-fibers.
