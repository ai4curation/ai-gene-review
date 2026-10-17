# Gene Review Notes: Enterobacteria phage phiX174 gene J (P69592)

## Overview
- **Gene symbol**: `J`
- **UniProt ID**: `P69592` (`J_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: DNA-binding protein J (gpJ, 38 aa; 37 aa mature after initiator Met removal, 4.2 kDa)
- **Phage lifecycle module**: `phage_packaging_headful_cos.yaml` (Charge-neutralizing ssDNA condensation and internal scaffold displacement) and `phage_capsid_assembly.yaml` (Tethering of packaged ssDNA to the inner F capsid surface)

## Biological Function & Mechanism
1. **Co-packaging with Viral ssDNA & Displacement of Internal Scaffold B**:
   - Protein J is a small, highly basic, intrinsically disordered polypeptide (12 basic Arg/Lys residues in its N-terminal domains I and II and a conserved hydrophobic/aromatic C-terminal domain, `-WYVGGQQF`) (`PMID:11991963`, `file:BPPHS/J/J-uniprot.txt`).
   - During stage III packaging-coupled rolling-circle DNA synthesis, 60 copies of gpJ bind the nascent circular single-stranded DNA genome via electrostatic interactions, neutralizing backbone phosphate repulsion (`PMID:11991963`, `PMID:9305849`).
   - Upon entering the `108S` procapsid with the viral ssDNA, the aromatic C-terminus of gpJ binds into an interior cleft on each of the 60 major coat protein F subunits—the same binding site occupied by the C-terminus of internal scaffolding protein B (`PMID:9305849`, `PMID:11991963`, `file:BPPHS/J/J-uniprot.txt`).
   - This competitive displacement extrudes gpB through the 30-Angstrom procapsid pores and tethers the packaged ssDNA genome into an icosahedrally ordered layer lining the inner capsid surface, enabling the 8.5-Angstrom radial collapse of gpF into the mature `114S` virion (`PMID:11991963`, `PMID:8158636`).

## GO Annotation Review Summary
- **Accepted core terms (`ACCEPT`)**:
  - `GO:0003677` (`DNA binding`, IEA): binds and neutralizes the circular ssDNA genome (`PMID:9305849`, `PMID:11991963`).
  - `GO:0019028` (`viral capsid`, IEA): 60 copies of gpJ are bound to the interior surface of the F coat in the mature capsid (`PMID:8158636`, `PMID:11991963`).
- **Non-core term (`KEEP_AS_NON_CORE`)**:
  - `GO:0030430` (`host cell cytoplasm`, IEA): synthesized and co-packaged with ssDNA into procapsids in the host cytoplasm.
- **Proposed new annotation (`NEW`)**:
  - `GO:0019073` (`viral DNA genome packaging`, `qualifier: involved_in`, supported by `PMID:9305849`, `PMID:11991963`, and `file:BPPHS/J/J-uniprot.txt`): mediating ssDNA packaging into the procapsid by neutralizing DNA charge and displacing internal scaffold B is the primary biological process of protein J, yet GOA currently lacks any biological process annotation for P69592.
