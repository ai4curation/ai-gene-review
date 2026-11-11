# Bacteriophage T4 Gene 19 (gp19) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `19` encodes the major tail tube protein gp19 (UniProt `P13333`, 163 amino acids, ~18.8 kDa) (PubMed 2963141). It self-assembles into the central rigid cylindrical tube of the phage tail, which serves both as the structural core surrounded by the contractile gp18 sheath and as the hollow conduit through which viral genomic dsDNA is translocated from the capsid into the host *Escherichia coli* cell during infection.

## Structural Organization and Assembly
- **Stoichiometry and Architecture**: A total of 144 copies of gp19 assemble into 24 stacked hexameric rings arranged in a helical cylinder ~925 Å long and ~90 Å in external diameter, enclosing an internal lumen ~40 Å wide that houses the extended tape measure protein gp29 prior to infection (PubMed 27193680).
- **Initiation and Termination of Assembly**: Polymerization of gp19 requires a completed baseplate bearing the baseplate–tail tube junction rings formed by hexamers of gp48 and gp54 (the first two annuli of the tubular assembly) together with the tape measure protein gp29 anchored in the central hub. Tube elongation stops after 24 rings when the N-terminus of gp29 is reached, and the distal end of the gp19 tube is stabilized by the hexameric tail completion protein gp15 before head-to-tail joining.
- **Role in Infection**: During infection, contraction of the outer gp18 sheath drives the rigid gp19 tail tube mechanically through the host outer membrane and periplasm, creating a continuous transmembrane channel for genome ejection.

## Annotation Review Notes
- `GO:0098026` (`virus tail, tube`, IDA from PubMed 2963141 and IEA from `GO_REF:0000043`): Directly supported by sequencing, peptide characterization, and structural studies of gp19 as the tail tube subunit (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): Overly general parent term superseded by `GO:0098026` (`virus tail, tube`) (`MODIFY` -> `GO:0098026`).
- `GO:0005198` (`structural molecule activity`, IEA from `GO_REF:0000002`): Overly broad molecular function term; refined to `GO:0039660` (`structural constituent of virion`) (`MODIFY` -> `GO:0039660`).
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA from `GO_REF:0000043`): Accurately reflects the role of the gp19 tail tube as the puncturing shaft and DNA ejection channel (`ACCEPT`).
- `GO:0046718` (`symbiont entry into host cell`, IEA from `GO_REF:0000043`): Overly general parent term superseded by `GO:0099000` (`MODIFY` -> `GO:0099000`).
