# Curation Notes for Escherichia phage Mu B (P03763)

## Summary of Gene Function
- **Gene symbol**: `B` (locus tag `Mup04`; UniProt `P03763`, ATP-dependent target DNA activator B / MuB)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: MuB (`B`) is a 312-aa AAA+ ATPase (`GO:0016887` `ATP hydrolysis activity`, `GO:0005524` `ATP binding`) and non-specific DNA-binding protein (`GO:0003677` `DNA binding`) that selects target DNA sites for phage Mu transposition (`GO:0006313` `DNA transposition`) and viral DNA genome replication (`GO:0039693` `viral DNA genome replication`) [PMID:23776210, PMID:12049743, file:BPMU/B/B-uniprot.txt].
- **Mechanism of Target Selection & Target Immunity**:
  - In the presence of ATP and `Mg2+`, MuB polymerizes into right-handed helical filaments around double-stranded target DNA (`PMID:23776210`, `PMID:24478936`).
  - MuB recruits the MuA transposase (`A`) to target DNA sites and allosterically activates MuA's catalytic donor-cleavage and strand-transfer activities (`PMID:11060014`, `PMID:23776210`).
  - Conversely, when MuA is bound at the viral `attL`/`attR` ends, transient contact between MuA's C-terminal domain IIIbeta and adjacent DNA-bound MuB stimulates MuB's ATPase activity and promotes disassembly of MuB filaments from DNA regions proximal to the Mu genome, establishing **cis target immunity** (preventing self-destructive integration of Mu into its own genome) (`PMID:11060014`, `PMID:12049743`, `PMID:23776210`, `PMID:24478936`).

## Literature & Reference Notes
- **PMID:23776210** (Mizuno et al., 2013, PNAS): Solved the X-ray crystal structure of the Plu2670 MuB homolog and demonstrated by biochemical and mutational analysis of phage MuB that MuB is an AAA+ ATPase with two domains (an N-terminal 4-helix bundle that binds the C-terminal tail of MuA and a C-terminal AAA+ module containing Walker A, Walker B, Sensor I, and arginine finger motifs) that forms helical filaments to control target selection.
- **PMID:24478936** (Dramicanin et al., 2014, JBC): Showed that the N-terminal appendage of MuB acts as a structural regulatory switch coupling ATP hydrolysis, helical filament assembly, DNA binding, and allosteric communication with MuA.
- **PMID:11060014** (Yamauchi & Baker, 2000, JBC): Defined two separable roles of MuB in transposition: delivery of target DNA to the transpososome and allosteric activation of the MuA active site.
- **PMID:12049743** (Greene & Mizuuchi, 2002, EMBO J): Visualized dynamic MuB target-DNA complex assembly and MuA-stimulated disassembly (target immunity) at the single-molecule level by TIRF microscopy.

## Annotation Review Decisions
- `GO:0016887` (`ATP hydrolysis activity`, IEA & IMP `PMID:23776210`): `ACCEPT` (both rows).
- `GO:0005524` (`ATP binding`, IEA): `ACCEPT`.
- `GO:0003677` (`DNA binding`, IEA): `ACCEPT`.
- `GO:0006313` (`DNA transposition`, IEA): `ACCEPT`.
- `GO:0015074` (`DNA integration`, IEA): `ACCEPT`.
- `GO:0039693` (`viral DNA genome replication`, IEA): `ACCEPT`.
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
- `GO:0046872` (`metal ion binding`, IEA): `MODIFY` to `GO:0000287` (`magnesium ion binding`) (supported by `PMID:23776210` and UniProt `COFACTOR: Name=Mg(2+)`).
- Broad parent IEA terms (`GO:0000166` `nucleotide binding`, `GO:0006260` `DNA replication`, `GO:0016787` `hydrolase activity`, `GO:0032196` `transposition`): `TOO_GENERAL` as they are entailed by the accepted specific annotations.
