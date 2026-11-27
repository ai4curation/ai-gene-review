# Curation Notes: Bacteriophage T4 gene wac (Fibritin; UniProt P10104)

## Identity and Nomenclature
- **Gene symbol**: `wac` (Whisker antigen control)
- **Protein**: Fibritin (also called gpwac, collar protein, or whisker antigen control protein; 487 aa precursor / 486 aa mature, ~51.9 kDa)
- **UniProt**: `P10104` (`WAC_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Structural component of the virion neck (collar and whiskers)**:
   - Gene `wac` encodes fibritin (487 aa), which assembles into a parallel triple-stranded alpha-helical coiled-coil homotrimer (~530 Å / 53 nm long and ~20 Å in diameter) consisting of an N-terminal gp13-binding anchor domain (residues 1-80; PDB: 1OX3), a central shaft of 12 coiled-coil segments separated by flexible loop linkers, and a C-terminal 27-residue beta-propeller-like trimerization domain ("foldon", residues 458-484; PDB: 1AA0, 1AVY, 1RFO) that nucleates rapid trimer folding and registration (Efimov et al. 1994, PubMed 7932704; Tao et al. 1997, PubMed 9261070; Guthe et al. 2004, PubMed 15033360; Letarov et al. 2005, PubMed 15659683).
   - During late virion morphogenesis, **12 fibritin homotrimers** (36 polypeptide chains) attach via their N-terminal domains to the dodecameric neck protein gp13 just below the head-tail junction: six fibritin trimers bend around the neck to form the **collar** (~300 Å outer diameter), and six fibritin trimers project radially downward/outward to form the **whiskers** (Fokine et al. 2013, PubMed 23434847; PDB: 3J2O; Hu et al. 2015, PubMed 26261343).
2. **Assembly scaffold/chaperone for long tail fiber (LTF) attachment**:
   - Although `wac` is nonessential for plaque formation under laboratory conditions (`wac` amber mutants form small plaques and virions lacking collars/whiskers), fibritin accelerates the attachment of assembled long tail fibers to the baseplate during late morphogenesis: the whiskers bind the knee/hinge region of an LTF while its C-terminal tip interacts near the baseplate, positioning the proximal gp34 end for efficient docking onto baseplate protein gp9 (Terzaghi et al. 1979, PubMed 423246; Letarov et al. 2005, PubMed 15659683; Leiman et al. 2010, PubMed 21138586).
3. **Environmental sensor regulating long tail fiber retraction and infectivity**:
   - In the extracellular virion, the collar and whiskers bind the six long tail fibers in an upward-folded ("retracted") conformation against the tail sheath and neck (interacting with the gp35 kneecap and gp36/gp37 distal shaft). Under unfavorable environmental conditions (low ionic strength, low temperature, or low pH), fibritin holds the LTFs retracted to prevent non-productive adsorption; under permissive conditions, it allows LTF extension for host receptor scanning (Conley & Wood 1975; Terzaghi et al. 1979, PubMed 423246; Letarov et al. 2005, PubMed 15659683; Fokine et al. 2013, PubMed 23434847).
   - Additionally, during infection of *E. coli* expressing the CBASS bacterial cGAS (DncV) defense system, Lys100 of fibritin is targeted for ubiquitin-like covalent isopeptide conjugation to the C-terminal glycine of DncV by the Cap2 enzyme (Jenson et al. 2023, PubMed 36848932).

## Review of Existing GOA Annotations
- `wac-goa.tsv` currently contains no QuickGO annotations (`existing_annotations` was empty in the initialized stub, even though UniProt `P10104` has `DR   GO; GO:0044423; C:virion component; IEA:UniProtKB-KW`).
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): Fibritin is the structural subunit of the virion neck collar and whiskers (12 homotrimers per virion bound to gp13).
  - `GO:0098004` (`virus tail fiber assembly`): Fibritin functions as a virion-bound assembly scaffold that captures and positions long tail fibers for efficient attachment to the baseplate.
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`): By controlling the extension versus retraction of the long tail fibers in response to ionic strength and temperature, fibritin regulates LTF-mediated host cell attachment.
  - `GO:0044423` (`virion component`): Cryo-EM reconstructions (PDB: 3J2O) demonstrate that 12 fibritin trimers form the collar and whiskers at the neck of the mature T4 virion.
