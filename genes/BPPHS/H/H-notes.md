# Gene Review Notes: Enterobacteria phage phiX174 gene H (P03646)

## Overview
- **Gene symbol**: `H`
- **UniProt ID**: `P03646` (`H_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: Minor spike protein / DNA pilot protein H (gpH, 328 aa, 34.4 kDa)
- **Phage lifecycle module**: `phage_adsorption_entry.yaml` (LPS receptor recognition and transient decameric alpha-helical periplasmic DNA delivery tube) and `phage_capsid_assembly.yaml` (Incorporation into 12S pre-assembly complexes)

## Biological Function & Mechanism
1. **Incorporation into 12S Pre-assembly Complexes & Mature Virion**:
   - Twelve copies of protein H are incorporated into the phiX174 procapsid and mature virion (one monomer associated with each of the twelve 5-fold `12S` pentameric pre-assembly intermediates) (`PMID:8158636`, `file:BPPHS/H/H-uniprot.txt`).
2. **LPS Receptor Recognition & Decameric Periplasmic DNA Delivery Tube**:
   - Protein H participates in lipopolysaccharide (LPS)-mediated receptor recognition and undergoes a conformational change triggered by the lipid A moiety of host LPS (`PMID:1094682`, `file:BPPHS/H/H-uniprot.txt`).
   - Upon host attachment and dissociation of the G spike pentamer at the infecting 5-fold vertex, ten copies of protein H oligomerize inside the capsid and protrude through the opened vertex to form a 170-Angstrom-long, 22-Angstrom-internal-diameter decameric alpha-helical barrel tube (`PMID:24336205`).
   - The central coiled-coil domain (residues 143-282, PDB: `4JPN`, `4JPP`) forms a continuous hydrophilic lumen constructed of ten long alpha-helices with a right-handed superhelical coiled-coil at the N-terminal half and a left-handed coiled-coil at the C-terminal half (`PMID:24336205`).
   - Cryo-electron tomography shows that this transient tail-like H tube spans the host outer membrane, periplasmic space, and inner membrane to conduct the circular single-stranded DNA genome into the host cytoplasm before dissociating (`PMID:24336205`).

## GO Annotation Review Summary
- **Accepted core terms (`ACCEPT`)**:
  - `GO:0019028` (`viral capsid`, IEA): 12 copies of gpH are packaged within the icosahedral capsid (`PMID:8158636`, `file:BPPHS/H/H-uniprot.txt`).
  - `GO:0039638` (`lipopolysaccharide-mediated virion attachment to host cell`, IMP from `PMID:1094682`).
  - `GO:0042802` (`identical protein binding`, IPI from `PMID:24336205`): homo-oligomerization of 10 gpH monomers into the alpha-helical barrel tube.
- **Modified term (`MODIFY`)**:
  - `GO:0046718` (`symbiont entry into host cell`, IEA) -> `MODIFY` to `GO:0039678` (`symbiont genome ejection through host cell envelope`), the specific descendant term that precisely captures the role of the periplasm-spanning gpH tube in transporting the viral DNA genome across the bacterial cell envelope (`PMID:24336205`).
