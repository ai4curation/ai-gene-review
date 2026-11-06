# TAV2_LOCUS3068 (DCL1, A0AAU9RFA2) Curation Notes — *Thlaspi arvense*

## Orthology and Domain Architecture
- **Gene symbol / Locus**: `TAV2_LOCUS3068` (`Tarvense_21196`, protein accession `CAH2039182.1`, UniProt `A0AAU9RFA2`, 1910 AA,Chromosome 1).
- **Ortholog**: Direct 1:1 ortholog of *Arabidopsis thaliana* **DCL1** (`AT1G01040`, `Q9SP32`, Endoribonuclease Dicer-like 1, 1910 AA).
- **Conserved Domain Architecture** ([TAV2_LOCUS3068-uniprot.txt](TAV2_LOCUS3068-uniprot.txt)):
  - `FT:DOMAIN 263..440`: Helicase ATP-binding (`PROSITE:PS51192`, `InterPro:IPR014001`)
  - `FT:DOMAIN 658..836`: Helicase C-terminal (`PROSITE:PS51194`, `InterPro:IPR001650`)
  - `FT:DOMAIN 847..942`: Dicer dsRNA-binding fold (`PROSITE:PS51327`, `InterPro:IPR005034`)
  - `FT:DOMAIN 1189..1321`: PAZ domain (`PROSITE:PS50821`, `InterPro:IPR003100`)
  - `FT:DOMAIN 1364..1522` & `1563..1711`: Tandem RNase III domains (`PROSITE:PS50142`, `InterPro:IPR000999`)
  - `FT:DOMAIN 1737..1800` & `1832..1907`: Tandem C-terminal dsRNA-binding motifs (`DRBM`, `PROSITE:PS50137`, `InterPro:IPR014720`)

## Biological Function & Homeostatic miR162 Feedback Loop
- **Primary Core Function**: Endoribonuclease Dicer-like 1 (`DCL1`) is the catalytic core of the nuclear plant Microprocessor complex (with HYL1 and SE) that cleaves primary miRNA transcripts (`pri-miRNAs`) and precursor miRNAs (`pre-miRNAs`) via its tandem RNase III domains (`RNase IIIa` and `RNase IIIb`) to produce mature ~21-nt miRNA/miRNA* duplexes ([PMID:38918606](../../../publications/PMID_38918606.md)).
- **Pennycress miRNA Biogenesis & miR162 Negative Feedback**:
  - Nunn et al. 2022 ([PMID:34990041](../../../publications/PMID_34990041.md)) identified 72 miRNA-producing loci across the chromosome-level *Thlaspi arvense* genome (`T_arvense_v2`), including `tar-mir-162a` on scaffold 3 (`31,739,144–31,739,240 (-)`, mature 21-nt 3p sequence `TCGATAAACCTCTGCATCCAG`).
  - Cross-reference against the pennycress transcriptome ([thlar_mirna_targets.tsv](../../../projects/THLAR_OILSEED/mirna_targets/thlar_mirna_targets.tsv)) confirms that `TAV2_LOCUS3068` (`A0AAU9RFA2`) carries the conserved `miR162` target site at CDS nucleotides `3073..3094` (expectation score `2.0`, aligned across the exon junction encoding the PAZ-linker region), matching the experimentally verified Category-0 degradome cleavage site in *Arabidopsis* `DCL1` (`AT1G01040.1`, `p = 0.00042` in [tardb_ath_degradome.tsv](../../../projects/THLAR_OILSEED/mirna_targets/tardb_ath_degradome.tsv)).
  - **Curation Principle (Actor vs. Substrate)**: `TAV2_LOCUS3068` (`DCL1`) is the **catalytic enzyme** of `GO:0035196` (*miRNA processing*). The fact that its own mRNA is cleaved by `miR162`-loaded RISC is homeostatic negative feedback on `DCL1` expression; `DCL1`'s annotation to `GO:0035196` is valid because the DCL1 protein itself catalyzes pri/pre-miRNA cleavage.

## Review of Existing GOA Annotations (14 IEA rows)
1. `GO:0004525` (*ribonuclease III activity*, `IEA`) — **ACCEPT** (core molecular function).
2. `GO:0005524` (*ATP binding*, `IEA`) — **ACCEPT** (core cofactor/helicase activity of the DExD/H-box helicase domain).
3. `GO:0035196` (*miRNA processing*, `IEA`) — **ACCEPT** (core biological process).
4. `GO:0005634` (*nucleus*, `IEA`) — **ACCEPT** (core cellular component; plant DCL1 acts in nuclear dicing bodies / nucleoplasm).
5. `GO:0000166` (*nucleotide binding*, `IEA`) — **MODIFY** to `GO:0005524` (*ATP binding*).
6. `GO:0003723` (*RNA binding*, `IEA`) — **MODIFY** to `GO:0003725` (*double-stranded RNA binding*).
7. `GO:0016787` (*hydrolase activity*, `IEA`) — **MODIFY** to `GO:0004525` (*ribonuclease III activity*).
8. `GO:0016891` (*RNA endonuclease activity producing 5'-phosphomonoesters, hydrolytic mechanism*, `IEA`) — **MODIFY** to `GO:0004525` (*ribonuclease III activity*).
9. `GO:0006396` (*RNA processing*, `IEA`) — **MODIFY** to `GO:0035196` (*miRNA processing*).
10. `GO:0009616` (*RNAi-mediated antiviral immune response*, `IEA`) — **KEEP_AS_NON_CORE** (secondary role; DCL4 and DCL2 are the primary antiviral Dicers in Brassicaceae).
11. `GO:0030422` (*siRNA processing*, `IEA`) — **KEEP_AS_NON_CORE** (secondary role in endogenous hairpin/nat-siRNA processing).
12. `GO:0003677` (*DNA binding*, `IEA`, `InterPro:IPR006935`) — **REMOVE** (false-positive domain-to-GO projection from `IPR006935` `Helicase/UvrB_N`; DCL1 binds dsRNA, not DNA).
13. `GO:0005737` (*cytoplasm*, `IEA`, `TreeGrafter` `PANTHER:PTN004466737`) — **REMOVE** (phylogenetic over-propagation from metazoan cytosolic Dicer clades; plant DCL1 is nuclear).
14. `GO:0010267` (*ta-siRNA processing*, `IEA`, `ARBA:ARBA00090672`) — **REMOVE** (false-positive ARBA rule over-propagated across plant DCL paralogs; DCL4 catalyzes ta-siRNA processing from TAS dsRNA precursors, whereas DCL1 only produces the upstream triggering miRNAs).
