# Gene 6 (P00638) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `6`
- **UniProtKB accession**: `P00638` (`EXRN_BPT7`, Exonuclease, EC 3.1.11.3)
- **Length**: 300 amino acids (~34.5 kDa)
- **InterPro / Pfam**: `InterPro:IPR020046` / `Pfam:PF02739` (`5_3_exonuc_N`, 5'-3' exonuclease, N-terminal resolvase-like domain); `InterPro:IPR029060` (`PIN-like_dom_sf`).

## Literature & Function Summary
- **Dual 5'-3' dsDNA exonuclease and RNase H (RNA-DNA hybrid ribonuclease) activities** (`PMID:364424`, `PMID:2170664`, `PMID:1325707`):
  - **Degradation of host chromosome**: Degrades host *E. coli* chromosomal DNA into deoxynucleoside 5'-monophosphates (dNMPs) that serve as precursors for viral DNA synthesis (`file:genes/BPT7/6/6-uniprot.txt`).
  - **RNA primer removal in viral DNA replication**: Shinozaki and Okazaki (1978) (`PMID:364424`) and Nakai and Richardson (1990) (`PMID:2170664`) demonstrated that the RNase H (RNA-DNA hybrid ribonuclease) activity of gp6 excises the 5'-terminal RNA primers synthesized by gp4 primase at Okazaki fragments and replication origins.
  - **Concatemer formation and selective viral DNA packaging**: Son and Serwer (1992) (`PMID:1325707`) and `PMID:2170664` showed that 5'-3' exonucleolytic resection of the 160-bp terminal direct repeats by gp6 exposes single-stranded 3' overhangs that anneal to form concatemers and prevent premature degradation of newly replicated DNA, stimulating selective T7 DNA packaging.

## Curation Decisions
- **ACCEPT**:
  - `GO:0051908` (`double-stranded DNA 5'-3' DNA exonuclease activity`, IEA `GO_REF:0000003`).
  - `GO:0004523` (`RNA-DNA hybrid ribonuclease activity`, IDA `PMID:364424`).
  - `GO:0003677` (`DNA binding`, IEA `GO_REF:0000002`).
  - `GO:0099015` (`degradation of host chromosome by virus`, IEA `GO_REF:0000043`).
- **KEEP_AS_NON_CORE**:
  - `GO:0039657` (`symbiont-mediated suppression of host gene expression`, IEA `GO_REF:0000043`): indirect downstream consequence of host chromosome degradation rather than direct transcriptional/translational inhibition.
- **MODIFY**:
  - `GO:0004518` (`nuclease activity`), `GO:0016787` (`hydrolase activity`), `GO:0140640` (`catalytic activity, acting on a nucleic acid`) -> `GO:0051908` (`double-stranded DNA 5'-3' DNA exonuclease activity`) and `GO:0004523` (`RNA-DNA hybrid ribonuclease activity`).
  - `GO:0004527` (`exonuclease activity`) -> `GO:0051908` (`double-stranded DNA 5'-3' DNA exonuclease activity`).
- **NEW**:
  - `GO:0039693` (`viral DNA genome replication`, `involved_in`, IMP `PMID:2170664`): gp6 removes RNA primers from lagging-strand Okazaki fragments and generates 3' overhangs for concatemer formation during viral DNA replication.
  - `GO:0019073` (`viral DNA genome packaging`, `involved_in`, IDA `PMID:1325707`): gp6 directly stimulates in vitro concatemerization-packaging of T7 DNA.
