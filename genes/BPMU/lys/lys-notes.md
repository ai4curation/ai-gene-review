# Curation Notes: Escherichia phage Mu `lys` (`Q9T1X2`, SAR-endolysin gp22 / Mup22)

## Summary of Function
- **Product**: Signal-anchor-release (SAR) endolysin gp22 (`lys` / `Mup22`, 171 aa, 18.9 kDa).
- **Enzymatic family**: Glycoside hydrolase family 24 (GH24; `IPR002196`, `PF00959`), lysozyme / N-acetylmuramidase (`EC 3.2.1.17`, `GO:0003796`).
- **Mechanism & Regulation**: Exported via the host Sec translocon as a single-pass type II inner membrane protein (`GO:0020002`) with an N-terminal transmembrane signal-anchor (`residues 1-24`). Unlike canonical SAR endolysins that escape spontaneously at high rates or rely solely on pinholins, gp22 has two basic residues (`Lys6` and `Lys7`) in its short cytoplasmic N-tail that retard spontaneous extraction from the bilayer (`PMID:35471081`). Phage Mu lacks a canonical holin and instead uses a single-pass type I membrane-tethered cytoplasmic protein, gp25 (`Mup25`, designated a "releasin"), to facilitate the release of gp22 from the inner membrane into the host periplasmic space (`GO:0044229`), where gp22 refolds into its active conformation (requiring catalytic residues `Glu37` and `Asp46`) and degrades the host peptidoglycan sacculus (`GO:0009253`) during cytolytic virion egress (`GO:0044659`) [PMID:35471081].

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0003796` (`lysozyme activity`, IEA): Core GH24 muramidase activity (`EC 3.2.1.17`), confirmed experimentally by complete loss of activity in the `E37A` active-site mutant (`PMID:35471081`).
  - `GO:0009253` (`peptidoglycan catabolic process`, IEA): Core biological process of degrading the bacterial cell wall sacculus.
  - `GO:0020002` (`host cell plasma membrane`, IEA): Initial membrane-tethered localization of the SAR domain prior to extraction.
  - `GO:0044659` (`viral release from host cell by cytolysis`, IDA & IMP, `PMID:35471081`): Direct experimental evidence of cytolytic phage release.
- **TOO_GENERAL**:
  - `GO:0003824` (`catalytic activity`), `GO:0016787` (`hydrolase activity`), `GO:0016798` (`hydrolase activity, acting on glycosyl bonds`), `GO:0061783` (`peptidoglycan muralytic activity`): Entailed by `GO:0003796` (`lysozyme activity`).
  - `GO:0016998` (`cell wall macromolecule catabolic process`): Entailed by `GO:0009253` (`peptidoglycan catabolic process`).
  - `GO:0031640` (`killing of cells of another organism`): Entailed by `GO:0044659` (`viral release from host cell by cytolysis`).
- **REMOVE**:
  - `GO:0042742` (`defense response to bacterium`, IEA): Spurious automated mapping from UniProt keyword `KW-0081` (`Bacteriolytic enzyme`). Phage endolysin-mediated lysis of its bacterial host cell is virion egress, not an antibacterial defense response.
- **NEW**:
  - `GO:0044229` (`host cell periplasmic space`, `located_in`, `PMID:35471081`): Captures the active soluble localization of gp22 after SAR extraction into the periplasm.
