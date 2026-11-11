# Curation Notes: Bacteriophage T4 gene 37 (gp37; UniProt P03744)

## Identity and Nomenclature
- **Gene symbol**: `37`
- **Protein**: Long-tail fiber protein gp37 (distal subunit / receptor-binding adhesin tip; 1026 aa, ~109.2 kDa)
- **UniProt**: `P03744` (`GP37_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Homotrimeric distal long tail fiber shaft and receptor-binding adhesin tip**:
   - Gene 37 encodes gp37 (1026 aa, ~109.2 kDa), which forms a parallel homotrimer (~327 kDa, ~55-63 nm long) constituting the major distal shaft ("lower shin") and the distal receptor-recognizing tip ("foot") of each of the six long tail fibers (`(gp34)3(gp35)1(gp36)3(gp37)3`) (Cerritelli et al. 1996, PubMed 8635743; Bartual et al. 2010, PubMed 21048084).
   - The 2.2 Å X-ray crystal structure of the C-terminal tip fragment (residues 785-1026, ~200 Å long; PDB: 2XGF) revealed three interwoven domains (Bartual et al. 2010, PubMed 21048084):
     - **Collar domain** (residues 785-816 and 860-881): contains a beta-prism and conserved tryptophan motif.
     - **Needle domain** (residues 817-859 and 882-930): an elongated, interwoven three-stranded beta-structure coordinating **seven hydrated Fe2+ ions** along the central 3-fold symmetry axis via conserved His-X-His (`HxH`) motifs (each Fe2+ octahedrally coordinated by six histidines, two from each monomer).
     - **Head domain** (residues 931-1026): the extreme distal globular receptor-binding domain (residues ~911-1026) containing deep lateral cavities and positively charged/aromatic loops that mediate reversible host receptor recognition.
2. **Host receptor recognition (OmpC and LPS) and host-range determination**:
   - In *Escherichia coli*, the gp37 head domain mediates the initial reversible adsorption of T4 by recognizing either outer membrane porin C (**OmpC**, on *E. coli* K-12) or the outer core glucosyl-alpha-1,3-glucose terminus of rough lipopolysaccharide (**LPS**, on *E. coli* B lacking OmpC) (Yu & Mizushima 1982, PubMed 7045112; Montag et al. 1990; Washizaki et al. 2016, PubMed 27058651).
   - Point mutations in the distal head domain (such as His929, Gly938, Gly958, Ala962, Glu970) switch or expand receptor specificity between OmpC and LPS or alter host range across *E. coli* and *Yersinia* strains.
   - Coordinated binding of at least three LTF tips to host receptors transmits a mechanical signal through the gp36-gp35-gp34 fiber to gp9 on the baseplate, triggering baseplate conformational switching and deployment of the gp12 short tail fibers for irreversible attachment.
3. **Chaperone-dependent folding and trimerization**:
   - Unlike T2/K3 homologs that carry an intramolecular C-terminal chaperone domain cleaved after folding, T4 gp37 lacks an autoproteolytic C-terminal chaperone and strictly requires two phage-encoded nonstructural chaperones—**gp57A** and **gp38**—to fold and trimerize into soluble, active fibers (Hashemolhosseini et al. 1996, PubMed 8892827; Bartual et al. 2010, PubMed 19913618).

## Review of Existing GOA Annotations
- `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`, IEA `GO_REF:0000043`): **ACCEPT**. gp37 is the primary reversible receptor-binding adhesin of T4, recognizing host cell surface LPS and OmpC.
- `GO:0019062` (`virion attachment to host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`). Broader parent of `GO:0098671`.
- `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`). Overly broad keyword mapping; gp37 specifically mediates reversible adhesion receptor attachment (`GO:0098671`).
- `GO:0098024` (`virus tail, fiber`, IEA `GO_REF:0000043`): **ACCEPT**. gp37 forms the distal shaft and tip of the long tail fiber.
- `GO:0098015` (`virus tail`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0098024` (`virus tail, fiber`). Broader parent of `GO:0098024`.
- `GO:0005198` (`structural molecule activity`, IEA `GO_REF:0000002`): **MODIFY** -> `GO:0039660` (`structural constituent of virion`). More specific molecular function term for a virion structural polypeptide.
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): gp37 is the major structural subunit of the distal long tail fiber (3 copies per LTF, 18 per virion).
  - `GO:0046872` (`metal ion binding`): X-ray crystallography (PDB: 2XGF) demonstrates that the gp37 needle domain coordinates seven iron ions (`Fe2+`) via conserved His-X-His motifs along the trimer axis.
