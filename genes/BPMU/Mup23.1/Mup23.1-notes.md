# Curation Notes: Escherichia phage Mu `Mup23.1` (`P0DTL7`, Spanin, outer lipoprotein subunit gp23.1 / o-spanin)

## Summary of Function
- **Product**: Outer-membrane lipoprotein spanin subunit gp23.1 (`Mup23.1`, o-spanin, 113 aa precursor; 85 aa mature lipoprotein after cleavage of residues 1-28 at `Cys29`).
- **Genomic Organization**: Encoded by an overlapping reading frame (`CDS 23.1`, `Pfam:PF23793` `LysC`) embedded in the +1 frame relative to the 3' end of `Mup23` (`PMID:35471081`).
- **Role in Lysis**: Lipidated at `Cys29` (`N-palmitoyl` and `S-diacylglycerol`) and sorted to the periplasmic leaflet of the host bacterial outer membrane (`GO:0039662`). Its proline-rich ectodomain projects into the host periplasmic space (`GO:0044229`) to form the periplasm-spanning spanin complex with i-spanin gp23 (`Mup23`). Following degradation of the peptidoglycan layer by SAR-endolysin gp22, the gp23-gp23.1 spanin complex disrupts the outer membrane to complete cytolytic virion egress (`GO:0044659`) [PMID:35471081].

## Annotation Review Decisions
- **MODIFY**:
  - `GO:0020002` (`host cell plasma membrane`, IEA, from `SL-0376` `Host cell outer membrane`) -> `GO:0039662` (`host cell outer membrane`): `GO_REF:0000044` conservatively remapped `SL-0376` to `GO:0020002`, which in Gram-negative bacteria is the inner membrane. Because gp23.1 is an outer-membrane lipoprotein (o-spanin), replacing `GO:0020002` with `GO:0039662` (`host cell outer membrane`) restores the accurate compartment.
- **TOO_GENERAL**:
  - `GO:0031640` (`killing of cells of another organism`, IEA): Entailed by `GO:0044659` (`viral release from host cell by cytolysis`).
- **ACCEPT**:
  - `GO:0044659` (`viral release from host cell by cytolysis`, IDA, `PMID:35471081`): Direct experimental proof of o-spanin function in phage Mu lysis.
- **NEW**:
  - `GO:0039662` (`host cell outer membrane`, `located_in`, `PMID:35471081`) and `GO:0044229` (`host cell periplasmic space`, `located_in`, `PMID:35471081`).
