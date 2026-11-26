# Gene 5 (P00581) Notes — Escherichia phage T7 (`BPT7`)

## Overview
- **Gene symbol**: `5`
- **UniProtKB accession**: `P00581` (`DPOL_BPT7`, DNA-directed DNA polymerase, EC 2.7.7.7 / EC 3.1.11.-)
- **Length**: 704 amino acids (~79.7 kDa)
- **Domains**:
  - N-terminal 3'-5' proofreading exonuclease domain (`InterPro:IPR034699` `DPOL_T7`, `InterPro:IPR012337` `RNaseH-like_sf`, `InterPro:IPR036397` `RNaseH_sf`, residues 5–192; catalytic metal-binding triad Asp5, Glu7, Asp174).
  - C-terminal family A DNA-directed DNA polymerase palm/fingers/thumb domain (`InterPro:IPR001098`, `InterPro:IPR002298`, `Pfam:PF00476` `DNA_pol_A`, residues 416–698; active-site Asp475, Asp654).
  - Unique 76-residue thioredoxin-binding domain (TBD) inserted into the thumb subdomain (`PMID:20696935`, `PMID:23012374`).

## Literature & Function Summary
- **Holoenzyme assembly with host thioredoxin (`TrxA`, `P0AA25`)** (`PMID:2703498`, `PMID:20696935`, `PMID:23012374`):
  - Isolated gp5 is a distributive DNA polymerase with 3'-5' single- and double-stranded DNA exonuclease activity (`PMID:2703498`).
  - Binding of host *E. coli* thioredoxin (`P0AA25`) in a 1:1 stoichiometry to the TBD insertion induces conformational remodeling in the thumb domain that increases DNA contact surface and converts gp5 into a highly processive replicative polymerase (`PMID:20696935`, `PMID:23012374`).
- **3'-5' proofreading exonuclease activity** (`PMID:2703498`, `PMID:1846298`):
  - Resides in the N-terminal domain and excises misincorporated 3'-terminal nucleotides to ensure high replication fidelity (`PMID:1846298`).
- **Replisome coordination with gp4 helicase-primase (`P03692`)** (`PMID:8528255`, `PMID:21606333`, `PMID:24591606`, `PMID:30265524`, `PMID:30679383`):
  - Direct interaction between gp5/TrxA and the C-terminal acidic tail and helicase/primase domains of gp4 (`P03692`) couples unwinding, primer handoff, leading- and lagging-strand synthesis, and dynamic polymerase exchange at the replication fork (`PMID:21606333`, `PMID:24591606`, `PMID:30265524`, `PMID:30679383`).

## Curation Decisions
- **ACCEPT**:
  - `GO:0003887` (`DNA-directed DNA polymerase activity`, IDA `PMID:23012374`, IDA `PMID:30265524`, IEA `GO_REF:0000120`).
  - `GO:0008408` (`3'-5' exonuclease activity`, IMP `PMID:2703498`, IEA `GO_REF:0000120`).
  - `GO:0003677` (`DNA binding`, IEA `GO_REF:0000120`), `GO:0000166` (`nucleotide binding`, IEA `GO_REF:0000104`), `GO:0046872` (`metal ion binding`, IEA `GO_REF:0000043`).
  - `GO:0005515` (`protein binding`, IPI `PMID:20696935` with `P0AA25`, IPI `PMID:30679383` with `P03692`, IPI `PMID:8528255` with `P03692`).
  - `GO:0039693` (`viral DNA genome replication`, IEA `GO_REF:0000043`), `GO:0006261` (`DNA-templated DNA replication`, IDA `PMID:30265524`, IEA `GO_REF:0000002`), `GO:0090592` (`DNA synthesis involved in DNA replication`, IMP `PMID:21606333`).
- **MODIFY (refinement of broad parent terms to specific activities already present)**:
  - `GO:0003676` (`nucleic acid binding`) -> `GO:0003677` (`DNA binding`).
  - `GO:0003824` (`catalytic activity`) -> `GO:0003887` (`DNA-directed DNA polymerase activity`) and `GO:0008408` (`3'-5' exonuclease activity`).
  - `GO:0004518` (`nuclease activity`), `GO:0004527` (`exonuclease activity`), `GO:0004529` (`DNA exonuclease activity`), `GO:0016787` (`hydrolase activity`) -> `GO:0008408` (`3'-5' exonuclease activity`).
  - `GO:0016740` (`transferase activity`), `GO:0016779` (`nucleotidyltransferase activity`), `GO:0034061` (`DNA polymerase activity`) -> `GO:0003887` (`DNA-directed DNA polymerase activity`).
  - `GO:0006260` (`DNA replication`) -> `GO:0039693` (`viral DNA genome replication`) and `GO:0006261` (`DNA-templated DNA replication`).
