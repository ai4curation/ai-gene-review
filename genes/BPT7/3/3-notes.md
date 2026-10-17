# Curation Notes for Escherichia phage T7 gene 3 (Endonuclease I, P00641)

## Identity & Sequence Features
- **UniProt ID**: P00641 (`END1_BPT7`)
- **Gene symbol**: `3` (Endonuclease I, gp3, EC 3.1.21.2)
- **Length**: 149 AA (Class II protein)
- **Domains**:
  - `InterPro:IPR008029` / `Pfam:PF05367` (Bacteriophage T7 endonuclease I)
  - `InterPro:IPR011335` (Restriction endonuclease type II-like superfamily)
  - Homodimer with domain-swapped active sites containing a two-metal-ion catalytic center (Glu-20, Asp-55, Lys-67, Glu-65).

## Functional Evidence
- **Holliday junction resolution & branched DNA cleavage**:
  - T7 Endonuclease I (gp3) is a structure-selective junction-resolving enzyme that binds to four-way DNA junctions (Holliday junctions) as a homodimer (`K_d` ~ 1 nM) and introduces symmetrical paired cleavages across the junction point to resolve recombination and replication intermediates during phage DNA replication and packaging [PMID:9236119, "Endonuclease I is a DNA junction-selective resolving enzyme from bacteriophage T7. Using a nuclease-defective mutant that retains normal binding to DNA we show that the protein binds to four-way DNA junctions as a dimer, in common with other junction-resolving enzymes studied."].
- **Double-stranded and single-stranded DNA endonuclease & host chromosome degradation**:
  - Purified gp3 hydrolyzes both double-stranded and single-stranded DNA, with a strong preference for single-stranded or branched/mismatch-containing DNA over linear duplex DNA [PMID:5541763, "Bacteriophage T7 endonuclease. I. Properties of the enzyme purified from T7 phage-infected Escherichia coli B."].
  - Gene 3 amber mutants synthesize only limited phage DNA and fail to degrade the host *E. coli* chromosome, demonstrating that gp3 works together with the gp6 exonuclease to degrade host DNA into deoxynucleoside monophosphates that are recycled for phage DNA synthesis [PMID:5263754, "Gene 3 mutants synthesize only a limited amount of DNA. In addition, they are defective in carrying out the degradation of host DNA, suggesting that the gene 3 endonuclease is involved in this function."].

## GO Annotation Review Summary
- `GO:0008821` (`crossover junction DNA endonuclease activity`, IDA `PMID:9236119`) -> `ACCEPT` (core function).
- `GO:1990238` (`double-stranded DNA endonuclease activity`, IDA `PMID:5541763`, IMP `PMID:5263754`, IMP `PMID:5541763`) -> `ACCEPT` (core function).
- `GO:0099015` (`degradation of host chromosome by virus`, IEA `GO_REF:0000043`) -> `ACCEPT` (core process).
- `GO:0003677` (`DNA binding`, IEA `GO_REF:0000043`) -> `ACCEPT` (gp3 binds DNA junctions and duplex/single-stranded DNA; no more specific DNA-binding term is present in the GOA set).
- `GO:0004518` (`nuclease activity`), `GO:0004519` (`endonuclease activity`), `GO:0016787` (`hydrolase activity`) -> `MODIFY` to `GO:0008821` and `GO:1990238`.
- `GO:0008833` (`deoxyribonuclease IV (phage-T4-induced) activity`, IEA `GO_REF:0000120` via `EC:3.1.21.2`) -> `MODIFY` to `GO:0008821` and `GO:1990238` (EC 3.1.21.2 historically grouped phage endonucleases under the T4 DenA name, whereas T7 gp3 is Endonuclease I with Holliday junction resolvase and dsDNA endonuclease activity).
- `GO:0016032` (`viral process`, IEA `GO_REF:0000002`) -> `MODIFY` to `GO:0099015` (`degradation of host chromosome by virus`).
- `GO:0039657` (`symbiont-mediated suppression of host gene expression`, IEA `GO_REF:0000043`) -> `KEEP_AS_NON_CORE` (indirect consequence of degrading the host chromosome).
- `GO:0015074` (`DNA integration`, IEA `GO_REF:0000002`) -> `REMOVE` (bacteriophage T7 is strictly lytic and does not integrate into the host chromosome; gp3 resolves branched recombination/replication intermediates and degrades host DNA).
