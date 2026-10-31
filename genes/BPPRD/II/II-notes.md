# Enterobacteria phage PRD1 gene II (Adsorption protein P2, P27378)

## Summary
Gene `II` encodes the monomeric receptor-binding adsorption spike protein P2 (591 aa, ~63.8 kDa; UniProt `P27378`, `P2_BPPRD`) of Enterobacteria phage PRD1. P2 is an elongated, club-shaped monomer (`PDB:1N7U`, `PDB:1N7V`) composed of a distal pseudo-beta-propeller receptor-binding head and an extended beta-sheet tail shaft anchored at the five-fold capsid vertices via interactions with the P31 (`XXXI`) penton base and the P5 (`V`) trimeric spike [PMID:17416681, file:BPPRD/II/II-uniprot.txt]. P2 specifically recognizes and binds the host cell conjugative plasmid-encoded mating pair formation (Mpf) surface receptor complex (encoded by IncP, IncN, or IncW broad-host-range plasmids in Gram-negative bacteria), triggering vertex disassembly, membrane tube formation, and viral DNA delivery [PMID:17416681, file:BPPRD/II/II-uniprot.txt].

## Domain Architecture & Structural Features
- **Length**: 591 aa (initiator Met-1 removed by host; mature chain residues 2–591; intramolecular disulfide bond `Cys254-Cys277`) [file:BPPRD/II/II-uniprot.txt].
- **InterPro / Pfam / SUPFAM / Gene3D**:
  - `InterPro:IPR015297` (`Phage_PRD1_P2`), `InterPro:IPR015949` (`Phage_PRD1_P2_N`), `InterPro:IPR015948` (`Phage_PRD1_P2_C`), `InterPro:IPR036325` (`P2_sf`).
  - `Pfam:PF09214` (`Prd1-P2`), `SUPFAM:SSF89428` (`Adsorption protein p2`).
  - `Gene3D:2.105.10.10` (`Pseudo beta propeller`) and `Gene3D:2.70.250.10` (`receptor-binding protein prd1-p2, domain 3`) [file:BPPRD/II/II-uniprot.txt].
- **Vertex Architecture & Entry Triggering**:
  - P2 is a monomer located off the 5-fold symmetry axis at the receptor-binding vertices, interacting near the capsid shell with the homotrimeric P5 spike and the P31 penton base [PMID:17416681].
  - Engagement of the host mating complex receptor by P2 (or experimental removal of P2) causes the P5 spike to move onto the 5-fold axis and disorder, inducing a conformational switch in the P31 penton base that initiates vertex opening for viral membrane nanotube transformation and DNA delivery [PMID:17416681, file:BPPRD/II/II-uniprot.txt].

## Literature & Annotation Review
- **`GO:0019062` (`virion attachment to host cell`, IEA, `GO_REF:0000043`)**:
  - Action: `MODIFY` to `GO:0098670` (`entry receptor-mediated virion attachment to host cell`). P2 specifically mediates high-affinity attachment to the host plasmid-encoded conjugative mating complex entry receptor to initiate infection [PMID:17416681, file:BPPRD/II/II-uniprot.txt].
- **`GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`)**:
  - Action: `MODIFY` to `GO:0098670` (`entry receptor-mediated virion attachment to host cell`). P2's direct molecular role in the viral entry pathway is receptor recognition and attachment (`GO:0098670`, which is `part_of` `GO:0046718`) coupled to conformational triggering of vertex uncapping [PMID:17416681, file:BPPRD/II/II-uniprot.txt].
- **Core Function**:
  - `GO:0039660` (`structural constituent of virion`), directly involved in `GO:0098670` (`entry receptor-mediated virion attachment to host cell`).
