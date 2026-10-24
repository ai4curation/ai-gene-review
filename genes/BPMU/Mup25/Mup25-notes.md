# Curation Notes: Escherichia phage Mu `Mup25` (`Q9T1W9`, Releasin protein gp25)

## Summary of Function
- **Product**: Releasin protein gp25 (`Mup25`, 99 aa, 11.3 kDa; `IPR020269` / `PF10805`, `TCDB 1.E.66.1.1`).
- **Role in Lysis**: Single-pass inner membrane protein (`GO:0020002`, N-terminal TMD `residues 3-23` with a cytoplasmic C-terminal three-helix bundle domain) that defines a novel functional class of phage lysis regulators termed **releasins** (`PMID:35471081`). Phage Mu lacks a canonical holin/pinholin; instead, gp25 facilitates the extraction and release of the SAR-endolysin gp22 (`lys`) from the host inner membrane into the periplasm, overcoming the retention barrier imposed by `Lys6` and `Lys7` in the short cytoplasmic tail of gp22. Moreover, gp25 can also accelerate the release of heterologous SAR endolysins (`PMID:35471081`).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0020002` (`host cell plasma membrane`, IEA): Inner-membrane localization via its N-terminal transmembrane domain.
  - `GO:0044659` (`viral release from host cell by cytolysis`, IDA, `PMID:35471081`): Essential lysis regulator in the Mu lysis cassette.
  - `GO:0140913` (`viral release via disruption of host peptidoglycan cell wall`, IDA, `PMID:35471081`, `acts_upstream_of_positive_effect`): Accurately captures its upstream role in triggering SAR-endolysin release to degrade the peptidoglycan wall.
- **TOO_GENERAL**:
  - `GO:0031640` (`killing of cells of another organism`, IEA): Entailed by `GO:0044659`.
