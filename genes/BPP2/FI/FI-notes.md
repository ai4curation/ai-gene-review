# BPP2 FI (P22501 / TSP_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `FI`
- **UniProt ID**: `P22501` (`TSP_BPP2`)
- **Protein**: Tail sheath protein gpFI (396 aa, 43.1 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:1825255** (Temple et al., 1991, *Virology*):
   - Sequenced the `FI` and `FII` genes of bacteriophage P2, mapped the `Fam4` amber mutation to `FI`, and confirmed the N-terminal amino acid sequences of both purified virion proteins.
   - Quotes:
     - `"The major structural components of the contractile tail of bacteriophage P2 are proteins FI and FII, which are believed to be the tail sheath and tube proteins, respectively."`
     - `"The coding regions were confirmed by location of the Fam4 mutation and by N-terminal amino acid sequencing of both proteins."`
2. **PMID:3981640** (Linderoth et al., 1986, *Virology*):
   - Identified sequence homology between P2 gpFI and the bacteriophage T4 tail sheath protein gp18.
   - Quote: `"Starting from a region known to be in the P2 F gene from work by Temple et al. [Virology (1985), in press], an open reading frame yields a primary structure with homology to the gp18 tail sheath protein of T4."`
3. **PMID:3458177** (Christie & Calendar, 1985, *J. Mol. Biol.*):
   - Characterized the `F` operon promoter and transcript encoding the two major tail structural proteins (`FI` and `FII`).
   - Quote: `"It codes for a small transcript, the function of which is unknown, and for two proteins known to be structural components of the phage tail."`

## Annotation Review Decisions
- `GO:0030430` (`host cell cytoplasm`, IEA & ISS): **KEEP_AS_NON_CORE** — gpFI is synthesized in the host cell cytoplasm prior to assembling onto the baseplate-tail tube complex, whereas its mature core site of action is the virion tail sheath (`GO:0098027`).
- `GO:0046718` (`symbiont entry into host cell`, IEA): **MODIFY** to `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098027` (`virus tail, sheath`).
- `GO:0098027` (`virus tail, sheath`, IEA): **ACCEPT**.
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA): **ACCEPT**.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:1825255`): N-terminal sequencing of virion structural proteins and `Fam4` genetics confirm gpFI is the major structural subunit of the contractile tail sheath.
- **NEW** `GO:0098003` (`viral tail assembly`, IMP, `PMID:1825255`): `FI` (`Fam4`) is essential for assembling the contractile tail sheath around the inner tail tube.
