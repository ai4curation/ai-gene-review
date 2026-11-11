# BPP2 FII (P22502 / TUBE_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `FII`
- **UniProt ID**: `P22502` (`TUBE_BPP2`)
- **Protein**: Tail tube protein gpFII (172 aa, 19.1 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:1825255** (Temple et al., 1991, *Virology*):
   - Sequenced the `FI` and `FII` genes of bacteriophage P2 and confirmed the `FII` reading frame by N-terminal amino acid sequencing of purified gpFII from mature virions.
   - Quotes:
     - `"The major structural components of the contractile tail of bacteriophage P2 are proteins FI and FII, which are believed to be the tail sheath and tube proteins, respectively."`
     - `"The coding regions were confirmed by location of the Fam4 mutation and by N-terminal amino acid sequencing of both proteins."`
2. **PMID:3458177** (Christie & Calendar, 1985, *J. Mol. Biol.*):
   - Characterized the `F` operon transcript encoding the two major tail structural proteins (`FI` and `FII`).
   - Quote: `"It codes for a small transcript, the function of which is unknown, and for two proteins known to be structural components of the phage tail."`

## Annotation Review Decisions
- `GO:0046718` (`symbiont entry into host cell`, IEA): **MODIFY** to `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098026` (`virus tail, tube`).
- `GO:0098026` (`virus tail, tube`, IEA): **ACCEPT**.
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA): **ACCEPT** — the rigid inner gpFII tube is driven through the host outer membrane and periplasm during sheath contraction to form the conduit for viral DNA ejection.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:1825255`): N-terminal sequencing of purified virion proteins confirms gpFII is the major structural subunit of the inner tail tube.
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:1825255`): gpFII polymerizes around the tape measure protein (gpT) on the baseplate to form the inner tail tube scaffold required for sheath (gpFI) assembly.
