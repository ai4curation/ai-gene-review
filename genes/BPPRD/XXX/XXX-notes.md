# Enterobacteria phage PRD1 gene XXX (Minor capsid protein P30, P27391)

## Summary
Gene `XXX` (synonym `P`) encodes the minor capsid tape-measure and cementing protein P30 (84 aa, ~9 kDa; UniProt `P27391`, `VP30_BPPRD`) of Enterobacteria phage PRD1. P30 is an extended proline-rich polypeptide that forms homodimers spanning the icosahedral edges between adjacent five-fold vertices (`PDB:1W8X`). By running beneath the major capsid protein P3 (`III`) facets from one vertex to the next (`60` copies of P30 per virion), P30 defines the pseudo `T=25` capsid size and cements the 20 P3 facets together onto the internal viral membrane vesicle [PMID:11697904, PMID:17416681, file:BPPRD/XXX/XXX-uniprot.txt].

## Domain Architecture & Structural Features
- **Length**: 84 aa (initiator Met-1 removed by host; mature chain residues 2–84) [file:BPPRD/XXX/XXX-uniprot.txt].
- **InterPro / Pfam**:
  - `InterPro:IPR015379` (`VP30`) / `Pfam:PF09300` (`Tecti-min-caps`, residues 2–84) [file:BPPRD/XXX/XXX-uniprot.txt].
- **Quaternary & Virion Architecture**:
  - Homodimers (`60` copies of P30 monomer, i.e., `30` dimers along the 30 icosahedral two-fold edges) extend across each facet boundary from one 5-fold vertex to the adjacent vertex (`PDB:1W8X`) [file:BPPRD/XXX/XXX-uniprot.txt, PMID:17416681].
  - Nonsense/null mutations in gene `XXX` abolish P3 outer shell assembly and result in accumulation of naked, empty phage-specific lipid membrane vesicles lacking the icosahedral protein coat [PMID:11697904].

## Literature & Annotation Review
- **`GO:0019028` (`viral capsid`, IEA, `GO_REF:0000120`)**:
  - Action: `MODIFY` to `GO:0019030` (`icosahedral viral capsid`). P30 is specifically an edge-spanning tape-measure and cementing component of the PRD1 icosahedral capsid [PMID:11697904, PMID:17416681].
- **`GO:0019069` (`viral capsid assembly`, IMP, `PMID:11697904`)**:
  - Action: `ACCEPT`. Mutants lacking P30 fail to assemble the icosahedral capsid shell and instead produce empty phage-specific membrane vesicles [PMID:11697904].
- **Core Function**:
  - `GO:0039660` (`structural constituent of virion`), directly involved in `GO:0019069` (`viral capsid assembly`).
