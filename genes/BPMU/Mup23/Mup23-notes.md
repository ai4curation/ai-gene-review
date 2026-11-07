# Curation Notes: Escherichia phage Mu `Mup23` (`Q9T1X1`, Spanin, inner membrane subunit gp23 / i-spanin)

## Summary of Function
- **Product**: Inner membrane spanin subunit gp23 (`Mup23`, i-spanin, 128 aa, 14.3 kDa).
- **Architecture & Localization**: Single-pass type II inner membrane protein (`GO:0020002`) with an N-terminal transmembrane helix (`residues 7-23`) and a periplasmic alpha-helical coiled-coil ectodomain (`residues 24-128`, `GO:0044229`).
- **Role in Lysis**: Forms a periplasm-spanning heterocomplex with the outer-membrane lipoprotein spanin subunit gp23.1 (`Mup23.1`, o-spanin, encoded by an overlapping reading frame). Once the SAR-endolysin gp22 degrades the peptidoglycan meshwork, the gp23-gp23.1 spanin complex disrupts the host outer membrane (likely via inner-outer membrane fusion), completing cytolytic virion release (`GO:0044659`). Amber mutations in `Mup23` arrest lysis at the spherical-cell stage under divalent cation stabilization (`PMID:35471081`).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0020002` (`host cell plasma membrane`, IEA): Anchored in the host inner membrane via its N-terminal TMD.
- **MODIFY**:
  - `GO:0031640` (`killing of cells of another organism`, IEA) -> `GO:0044659` (`viral release from host cell by cytolysis`): Refines the broad keyword-derived cell-killing term to the specific phage cytolytic release process experimentally demonstrated for gp23 (`PMID:35471081`).
- **NEW**:
  - `GO:0044659` (`viral release from host cell by cytolysis`, `involved_in`, `PMID:35471081`): Experimental annotation matching the one already curated in GOA for its partner `Mup23.1`.
  - `GO:0044229` (`host cell periplasmic space`, `located_in`, `PMID:35471081`): The C-terminal coiled-coil domain spans the periplasmic space.
