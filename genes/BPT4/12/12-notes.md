# Gene 12 (Short tail fiber protein gp12) - Research Notes

## Overview
- **Gene symbol**: `12` (gp12)
- **UniProt ID**: `P10930`
- **Organism**: Bacteriophage T4 (`NCBITaxon:10665`, Tequatrovirus T4)
- **Length**: 527 amino acids (~56.2 kDa monomer)

## Biological Function & Architecture
- **Short Tail Fiber (STF) Adhesion Protein**: gp12 forms the six club-shaped short tail fibers (18 copies per virion; six homotrimers of ~52 nm length) that are stowed in a compact garland beneath the dome-shaped baseplate in the pre-attachment virion and unfold downward during the dome-to-star baseplate transition to bind irreversibly to the core lipopolysaccharide (LPS) region on the surface of Escherichia coli B hosts (PubMed 11743729; PubMed 27193680).
- **Modular Fibrous Structure & Octahedral Zinc-Binding Site**: Each gp12 homotrimer comprises an N-terminal pin-attachment domain (anchored to domain IV of the gp10 baseplate pin), a central intertwined beta-stranded/beta-helical shaft with a flexible hinge clamped by the gp11 adaptor trimer, and a C-terminal globular receptor-binding "head" domain (~residues 398–527) (PubMed 11743729; PubMed 27193680). Crystal structures of proteolytic fragments of gp12 (PubMed 11743729; PubMed 12914965) revealed an unusual buried `Zn2+` ion in the C-terminal receptor-binding domain, coordinated octahedrally by six histidine side chains (`His445` and `His447` from each of the three monomers). Proper folding and trimerization of gp12 in vivo require the phage-encoded cytoplasmic molecular chaperone gp57A.
- **Role in Baseplate Architecture and Host Attachment**: In the pre-attachment virion, the six gp12 trimers are held in a head-to-tail ring underneath the baseplate rim through interactions with gp10 and gp11. Upon long tail fiber sensing of the host surface, rotation of the gp10-gp11 pins releases the gp12 C-terminal heads and swivels the STFs by ~150° to point toward the outer membrane, locking the baseplate ~37 nm above the cell surface as the tail sheath contracts.

## Annotation Assessment Notes
- `GO:0098670` (`entry receptor-mediated virion attachment to host cell`, IEA from `GO_REF:0000043`): Core biological process (`ACCEPT`), as gp12 directly and irreversibly binds the core LPS receptor on the host outer membrane.
- `GO:0019062` (`virion attachment to host cell`, IEA from `GO_REF:0000043`) and `GO:0046718` (`symbiont entry into host cell`, IEA from `GO_REF:0000043`): True but overly general ancestors of `GO:0098670` (`MODIFY` to `GO:0098670`).
- `GO:0046872` (`metal ion binding`, IEA from `GO_REF:0000002`): True but overly general (`MODIFY` to `GO:0008270` `zinc ion binding`), because X-ray crystallography and anomalous scattering directly demonstrate an octahedrally coordinated `Zn2+` ion bound by His445 and His447 of each monomer in the C-terminal receptor-binding domain.
- `GO:0098024` (`virus tail, fiber`, IEA from `GO_REF:0000120`) and `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680): Both are accurate (`ACCEPT`), as gp12 forms the short tail fibers (`GO:0098024`) whose N-termini and stowed shafts are integral components of the baseplate periphery (`GO:0098025`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): Overly general parent term (`MODIFY` to both `GO:0098024` and `GO:0098025`).
