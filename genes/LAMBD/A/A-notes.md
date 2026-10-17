# A (P03708) - Terminase large subunit (gpA)

## Summary
- **Gene symbol**: `A`
- **UniProt ID**: `P03708`
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Protein**: Terminase large subunit (`gpA`, 641 aa, EC 3.1.21.4)

## Biological Function
- Catalytic large subunit (`gpA`, TerL) of the bacteriophage lambda terminase complex, which forms a $\mathrm{gpA_1 \cdot gpNu1_2}$ heterotrimer with the small subunit `gpNu1` and assembles at the procapsid portal vertex (`gpB`) as a pentameric/tetrameric packaging motor [PMID:11866517, PMID:15755448, PMID:23134123].
- **N-terminal translocation motor domain (residues 1-179/350)**: Houses the high-affinity P-loop ATPase catalytic center (including Y46, K84, and catalytic glutamate E179 coupled to an arginine toggle) that powers rapid (>600 bp/s) mechanochemical translocation of viral dsDNA into the empty procapsid [PMID:10993723, PMID:11866517, PMID:30541105] as well as an intrinsic ATP-dependent strand-separation (`cosN` cohesive-end unwinding / helicase) activity that separates the 12-base nicked cohesive ends [PMID:8175794, PMID:23134123].
- **C-terminal maturation endonuclease domain (`gpA-DeltaN179`)**: Catalyzes $\mathrm{Mg^{2+}}$-dependent (or $\mathrm{Mn^{2+}}$-dependent), ATP-stimulated site-specific nicking of the `cosN` duplex to generate the 12-nt 5'-cohesive overhangs at the initiation and termination of unit-length genome packaging [PMID:2970303, PMID:8428984, PMID:1534952, PMID:17870092, PMID:23134123].
- **C-terminal portal/gpNu1 interaction**: The extreme C-terminal tether binds the procapsid portal complex (`gpB`) and facilitates procapsid docking (`complex II` formation) [PMID:2965251, file:LAMBD/A/A-uniprot.txt].

## Curation Decisions
- **ACCEPT**:
  - `GO:0009036` (`type II site-specific deoxyribonuclease activity`, EXP/IEA `PMID:1534952`, `PMID:17870092`, `PMID:23134123`, `PMID:2970303`, `PMID:7813453`, `GO_REF:0000120`)
  - `GO:0016887` (`ATP hydrolysis activity`, IDA/IMP/IEA `PMID:8428984`, `PMID:10993723`, `PMID:11866517`, `PMID:30541105`, `GO_REF:0000120`)
  - `GO:0003678` (`DNA helicase activity`, IDA `PMID:8175794`)
  - `GO:0005524` (`ATP binding`, IEA `GO_REF:0000120`)
  - `GO:0019073` (`viral DNA genome packaging`, EXP/IDA/IMP/IEA `PMID:10993723`, `PMID:11866517`, `PMID:2965251`, `PMID:8428984`, `PMID:30541105`, `GO_REF:0000104`)
  - `GO:0098009` (`viral terminase, large subunit`, IDA/IEA `PMID:11866517`, `GO_REF:0000104`)
  - `GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`)
- **MODIFY**:
  - `GO:0000166` (`nucleotide binding`) -> `GO:0005524` (`ATP binding`)
  - `GO:0004518` (`nuclease activity`) and `GO:0004519` (`endonuclease activity`) -> `GO:0009036` (`type II site-specific deoxyribonuclease activity`)
  - `GO:0016787` (`hydrolase activity`) -> `GO:0016887` (`ATP hydrolysis activity`) and `GO:0009036` (`type II site-specific deoxyribonuclease activity`)
  - `GO:0046872` (`metal ion binding`) -> `GO:0000287` (`magnesium ion binding`)
