# Enterobacteria phage PRD1 gene III (Major capsid protein P3, P22535)

## Summary
Gene `III` encodes the major capsid protein P3 (395 aa, ~43 kDa; UniProt `P22535`, `CAPSD_BPPRD`) of the lipid-containing tectivirus Enterobacteria phage PRD1. P3 self-assembles into stable pseudohexameric homotrimers (`240` trimers per virion, `720` subunits total) that organize on a pseudo `T=25` icosahedral lattice (66–70 nm diameter) surrounding the internal phage lipid membrane vesicle [PMID:17416681, file:BPPRD/III/III-uniprot.txt]. Each P3 monomer adopts a tandem double-jelly-roll (two eight-stranded viral beta-barrels) architecture conserved across the Bamfordvirae/PRD1-adenovirus structural lineage (`PDB:1CJD`, `PDB:1GW7`, `PDB:1GW8`, `PDB:1HB5`, `PDB:1HB7`, `PDB:1HB9`, `PDB:1HQN`, `PDB:1HX6`, `PDB:1W8X`, `PDB:7OOK`).

## Domain Architecture & Structural Features
- **Length**: 395 aa (initiator Met-1 removed by host; mature chain residues 2–395) [file:BPPRD/III/III-uniprot.txt].
- **InterPro / Pfam / SUPFAM / Gene3D**:
  - `InterPro:IPR015108` / `InterPro:IPR016115` / `Pfam:PF09018` (`Phage_Capsid_P3_N`, N-terminal barrel domain).
  - `InterPro:IPR057669` / `Pfam:PF25514` (`P3_C`, C-terminal barrel domain).
  - `InterPro:IPR029053` (`Viral_coat`), `InterPro:IPR016112` (`VP_dsDNA_II`), `SUPFAM:SSF49749` (`Group II dsDNA viruses VP`).
  - `Gene3D:2.60.120.20` and `Gene3D:2.70.9.30` (`Viral coat protein p3`) [file:BPPRD/III/III-uniprot.txt].
- **Subunit & Lattice Organization**:
  - 240 copies of P3 homotrimers occupy the four unique quasi-equivalent positions across the 20 facets of the pseudo `T=25` icosahedral capsid [PMID:17416681, file:BPPRD/III/III-uniprot.txt].
  - Adjacent P3 facets are cemented along their edges by dimers of the 84-residue minor capsid tape-measure protein P30 (`XXX`), which is essential for stable P3 shell assembly onto the viral membrane vesicle [PMID:11697904, PMID:17416681].
  - At the 5-fold vertices, peripentonal P3 trimers interlock with the homopentameric penton base protein P31 (`XXXI`) and the integral inner-membrane vertex-stabilizing protein P16 (`XVI`) [PMID:17416681].

## Literature & Annotation Review
- **`GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043`)**:
  - Action: `MODIFY` to `GO:0019030` (`icosahedral viral capsid`). Cryo-EM and X-ray crystallographic structures (`PDB:1HX6`, `PDB:1W8X`) and three-dimensional reconstructions [PMID:17416681] establish that P3 forms the pseudohexameric capsomers of a pseudo `T=25` icosahedral viral capsid.
- **Core Function**:
  - `GO:0039660` (`structural constituent of virion`), directly involved in `GO:0019069` (`viral capsid assembly`).
