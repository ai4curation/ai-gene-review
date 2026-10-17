# Nu1 (P03707) - Terminase small subunit (gpNu1)

## Summary
- **Gene symbol**: `Nu1`
- **UniProt ID**: `P03707`
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Protein**: Terminase small subunit (`gpNu1`, 181 aa)

## Biological Function
- Forms the small regulatory/DNA-recognition subunit (`gpNu1`) of the bacteriophage lambda terminase holoenzyme, which assembles as a heterotrimeric protomer ($\mathrm{gpA_1 \cdot gpNu1_2}$, 114.2 kDa) capable of further associating into a homogeneous tetramer of heterotrimers [PMID:15755448].
- Recognizes and binds the three R elements (R3, R2, R1) within the `cosB` sub-site of the cohesive end site (`cos`) via an N-terminal winged helix-turn-helix (wHTH) dimerization/DNA-binding domain, and acts cooperatively with *Escherichia coli* integration host factor (IHF) to strongly bend `cos` DNA and position the large subunit (`gpA`) at `cosN` for site-specific nicking and packaging initiation [PMID:16618107].
- Contains a low-affinity, DNA-stimulated ATPase active site that regulates viral DNA binding and `cos` cleavage dynamics [PMID:2965248, PMID:8611586].

## Curation Decisions
- **ACCEPT**:
  - `GO:0044374` (`sequence-specific DNA binding, bending`, IDA `PMID:16618107`)
  - `GO:0016887` (`ATP hydrolysis activity`, IDA `PMID:2965248`, `PMID:8611586`, IEA `GO_REF:0000116`)
  - `GO:0005524` (`ATP binding`, IEA `GO_REF:0000043`)
  - `GO:0019073` (`viral DNA genome packaging`, IDA `PMID:15755448`)
  - `GO:0097710` (`viral terminase, small subunit`, IDA `PMID:15755448`)
  - `GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`)
- **MODIFY**:
  - `GO:0000166` (`nucleotide binding`) -> `GO:0005524` (`ATP binding`)
  - `GO:0003677` (`DNA binding`) -> `GO:0044374` (`sequence-specific DNA binding, bending`)
  - `GO:0016787` (`hydrolase activity`) -> `GO:0016887` (`ATP hydrolysis activity`)
