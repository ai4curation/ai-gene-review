# Enterobacteria phage PRD1 gene V (Spike protein P5, P22536)

## Summary
Gene `V` encodes the homotrimeric vertex spike protein P5 (340 aa, ~34.4 kDa; UniProt `P22536`, `P5_BPPRD`) of Enterobacteria phage PRD1. P5 is a multidomain fibrous spike protein located at the 5-fold icosahedral vertices (`PDB:1YQ5`, `PDB:1YQ6`, `PDB:1YQ8`), where its N-terminal penton-like jelly-roll domain binds directly to the homopentameric penton base protein P31 (`XXXI`) and its proximal shaft interacts laterally with the monomeric receptor-binding spike protein P2 (`II`) [PMID:17416681, file:BPPRD/V/V-uniprot.txt]. P5 is strictly required for the incorporation and stabilization of P2 at the virion vertices [PMID:17416681].

## Domain Architecture & Structural Features
- **Length**: 340 aa (initiator Met-1 removed by host; mature chain residues 2–340) [file:BPPRD/V/V-uniprot.txt].
- **InterPro / Pfam / Gene3D**:
  - N-terminal penton-binding domain (`Domain-1`, residues 2–122): shares 38% sequence identity with penton protein P31 (`XXXI`), classified in `InterPro:IPR015043` (`Phage_PRD1_P5_spike_N`) / `Pfam:PF08948` (`PRD1_P5_spike_N`) [PMID:17416681, file:BPPRD/V/V-uniprot.txt].
  - Central collagen-like triple-helix region (residues 123–141, containing `Gly-X-Y` repeats) followed by a glycine-rich flexible hinge [PMID:17416681, file:BPPRD/V/V-uniprot.txt].
  - C-terminal trimeric beta-stranded knob head domain (`Domain-2`, residues 142–340; `PDB:1YQ5`, `PDB:1YQ6`, `PDB:1YQ8`): `InterPro:IPR015044` (`Phage_PRD1_P5_C`), `InterPro:IPR038663` (`PRD1_P5_C_sf`), `Pfam:PF08949` (`PRD1_P5_C`), and `Gene3D:2.60.120.670` (`Minor capsid protein`) [file:BPPRD/V/V-uniprot.txt].
- **Subunit & Vertex Interactions**:
  - P5 forms a homotrimer bound directly to the P31 penton base at the 5-fold vertices [PMID:17416681, file:BPPRD/V/V-uniprot.txt].
  - In wild-type virions, P5 and the monomeric receptor-binding protein P2 form two separate spikes at the vertex that interact near the capsid shell; without P5, no P2 is incorporated into the virion [PMID:17416681].
  - Dissociation of P2 (either in `P2-` mutants or upon host receptor engagement) causes the P5 spike to shift onto the 5-fold symmetry axis and become disordered, coupled to a conformational switch in the P31 penton that initiates vertex opening [PMID:17416681].

## Literature & Annotation Review
- **`GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043`)**:
  - Action: `MODIFY` to `GO:0098029` (`icosahedral viral capsid, spike`), which is already experimentally annotated to `V` (`PMID:17416681`).
- **`GO:0098029` (`icosahedral viral capsid, spike`, IMP, `PMID:17416681`)**:
  - Action: `ACCEPT`. Cryo-EM reconstructions of wild-type and spike-mutant PRD1 virions directly demonstrate that P5 forms the trimeric vertex spike bound to the P31 penton base [PMID:17416681].
- **Core Function**:
  - `GO:0039660` (`structural constituent of virion`), directly involved in `GO:0019069` (`viral capsid assembly`) and `GO:0019062` (`virion attachment to host cell`).
