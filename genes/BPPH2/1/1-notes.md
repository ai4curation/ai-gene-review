# Gene 1 (Membrane-associated replication scaffold protein gp1 / p1, P03679) — Curation Notes

## Summary of Function
Gene `1` of *Bacillus phage phi29* (`NCBITaxon:2884424`) encodes an 85-amino-acid (86 AA precursor before initiator methionine cleavage) early replication protein (gp1, p1; UniProt `P03679`). An internal translation initiation event also produces a shorter 53-AA isoform (protein delta-1, `P03679-2`).
In *Bacillus subtilis*-infected cells, protein p1 associates with the host cell membrane (`GO:0033644`) and self-assembles via its C-terminal coiled-coil-like region (residues 34–85) into large two-dimensional protofilament sheet structures (`PMID:11032825`, `PMID:12904294`). Through its N-terminal region (residues 1–33), p1 directly binds the viral primer terminal protein gp3 (`P03681`), compartmentalizing and anchoring the phi29 DNA replication machinery at the bacterial membrane to support efficient in vivo protein-primed viral DNA replication (`GO:0039693`) (`PMID:11032825`, `PMID:12904294`, `file:BPPH2/1/1-uniprot.txt`). Protein p1 also interacts with the host cell-division GTPase FtsZ (`file:BPPH2/1/1-uniprot.txt`).

## Domain Architecture & Structural Features
- **InterPro / Pfam / PIRSF**: `InterPro:IPR016408` (Phage phi-29 Gp1), `Pfam:PF26845` (`Phage_phi29_DNA_rep1`), `PIRSF:PIRSF004177` (`gp1_phi29`).
- **Modular organization**:
  - **N-terminal domain (residues 1–33)**: Hydrophilic region that directly binds the viral terminal protein gp3 (`PMID:11032825`).
  - **C-terminal polymerization domain (residues 34–85)**: Sufficient for self-association into protofilament sheets and peripheral association with the host bacterial membrane (`PMID:11032825`, `PMID:12904294`).

## Literature & Annotation Review
- `PMID:11032825`: Demonstrated that p1 is membrane-associated in *B. subtilis*-infected cells, self-assembles via its C-terminal 52 residues into protofilament sheets, and interacts directly with terminal protein p3 in vitro to compartmentalize viral DNA replication.
- `PMID:12904294`: Demonstrated by in vivo chemical cross-linking and cell fractionation that p1 assembles into membrane-associated multimeric structures in infected cells and is rate-limiting for in vivo phi29 DNA synthesis.
- `PMID:820555`: Showed that gene 1 mutants have reduced/defective phage DNA synthesis in vivo.
- **GO Annotation Decisions**:
  - `GO:0033644` (`host cell membrane`, EXP `PMID:11032825`, IDA `PMID:12904294`, IEA `GO_REF:0000044`): `ACCEPT`.
  - `GO:0016020` (`membrane`, IEA `GO_REF:0000002`): `MODIFY` to `GO:0033644` (`host cell membrane`).
  - `GO:0006260` (`DNA replication`): `MODIFY` to `GO:0039693` (`viral DNA genome replication`); `GO:0039693` (`viral DNA genome replication`): `ACCEPT`.
  - `GO:0016032` (`viral process`, IEA `GO_REF:0000002`): `TOO_GENERAL` (entailed by `GO:0039693`).
  - `GO:0003723` (`RNA binding`, IEA `GO_REF:0000043`): `KEEP_AS_NON_CORE` (based on UniProt keyword `KW-0694` from biochemical reports of sequence-nonspecific RNA binding by p1 in `PMID:9480849`/`PMID:15883018`, though its primary biological function is acting as a membrane-associated structural scaffold (`GO:0005198` / `GO:0032947`) for the viral replisome).
  - Note on `core_functions`: Because `GO:0005515` (`protein binding`) and `GO:0042802` (`identical protein binding`) are not permitted as `core_functions[].molecular_function`, we use `GO:0005198` (`structural molecule activity`) to represent p1's self-assembly into membrane-bound protofilament sheet scaffolds that compartmentalize `GO:0039693` (`viral DNA genome replication`) at `GO:0033644` (`host cell membrane`).
