# Gene Review Notes: Enterobacteria phage phiX174 gene G (P03643)

## Overview
- **Gene symbol**: `G`
- **UniProt ID**: `P03643` (`G_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: Major spike protein G (gpG, 175 aa, 19.0 kDa)
- **Phage lifecycle module**: `phage_capsid_assembly.yaml` (Pentameric vertex spikes of the T=1 capsid) and `phage_adsorption_entry.yaml` (Primary LPS receptor attachment and vertex opening)

## Biological Function & Mechanism
1. **Pentameric Vertex Spikes of the Virion**:
   - Sixty copies of major spike protein G (175 aa, eight-stranded antiparallel beta-barrel fold) form 12 prominent pentameric spikes at the 5-fold vertices of the T=1 icosahedral capsid (`PMID:1370343`, `PMID:8158636`, `file:BPPHS/G/G-uniprot.txt`).
   - Each G pentamer encloses a hydrophilic axial channel across the 5-fold vertex that houses density from minor spike/pilot protein H (`PMID:1370343`).
   - During morphogenesis in the host cytoplasm, five gpG monomers assemble into a `6S` pentamer, which joins an F coat pentamer (`9S`), internal scaffold B, and pilot protein H to form the `12S` pre-assembly complex (`file:BPPHS/G/G-uniprot.txt`, `PMID:9305849`).
2. **Host LPS Receptor Attachment & Entry Initiation**:
   - Protein G mediates initial attachment of the virion to host bacterial lipopolysaccharide (LPS) and is a major determinant of phage host range (`file:BPPHS/G/G-uniprot.txt`).
   - Upon productive LPS engagement at the infecting vertex, the G spike pentamer dissociates from the F capsid coat, exposing the F protein EF loops and allowing pilot protein H to protrude and form the genome-delivery tube (`file:BPPHS/G/G-uniprot.txt`).

## GO Annotation Review Summary
- **Accepted core terms (`ACCEPT`)**:
  - `GO:0019028` (`viral capsid`, IEA): gpG forms the 12 pentameric vertex spikes of the mature capsid (`PMID:1370343`, `PMID:8158636`).
  - `GO:0019062` (`virion attachment to host cell`, IEA): gpG attaches the virion to bacterial LPS receptors (`file:BPPHS/G/G-uniprot.txt`).
- **Non-core terms (`KEEP_AS_NON_CORE`)**:
  - `GO:0030430` (`host cell cytoplasm`, IEA): gpG is synthesized and assembled into 6S/12S/108S intermediates in the host cytoplasm prior to virion release.
  - `GO:0046718` (`symbiont entry into host cell`, IEA): gpG receptor binding and vertex dissociation initiate the entry pathway leading to H-mediated DNA ejection.
- **Removed erroneous InterPro mapping (`REMOVE`)**:
  - `GO:0044003` (`symbiont-mediated perturbation of host process`, IEA from `InterPro:IPR003515`): gpG is a structural capsid spike and LPS-binding attachment protein; it does not perturb or modulate a host physiological or biochemical pathway.
