# Curation Notes: Bacteriophage T4 `41` (DNA helicase gp41, P04530)

## Overview
- **Gene symbol:** `'41'` (gp41)
- **UniProt ID:** `P04530` (`HELI_BPT4`)
- **Length:** 475 amino acids
- **Function:** Essential hexameric 5'-3' replicative DNA helicase (DnaB-like superfamily 4 helicase) and catalytic motor of the T4 primosome (with gp61 primase), required for origin-dependent and recombination-dependent viral DNA replication.

## Biological Role and Mechanism
- gp41 is an ATP-dependent (and GTP-dependent) superfamily 4 (DnaB-like) replicative DNA helicase that assembles into a toroidal homohexamer upon NTP binding (`PMID:8107085`, PubMed 7479928).
- Translocating 5' -> 3' along the lagging-strand single-stranded DNA template (`PMID:8107085`), gp41 unwinds duplex DNA ahead of the leading-strand DNA polymerase (gp43) at the replication fork (`PMID:10871615`, `PMID:15781450`, PubMed 11459969, PubMed 23578280).
- On gp32-coated replication forks, D-loops, and Holliday junctions, loading of the gp41 hexamer requires the helicase loader protein gp59, which displaces gp32 and coordinates coupling of the helicase to the replisome (`PMID:10871615`, `PMID:15781450`).
- Together with the oligoribonucleotide primase gp61, gp41 forms the T4 primosome, strongly stimulating gp61-catalyzed pentaribonucleotide primer synthesis on the lagging strand (PubMed 11459969, PubMed 16096350).

## Review of Existing GO Annotations
- `GO:0003678` (DNA helicase activity, IEA, GO_REF:0000120 & IDA, `PMID:10871615`): **ACCEPT**. Core catalytic activity of gp41 in unwinding duplex and branched DNA substrates.
- `GO:0017116` (single-stranded DNA helicase activity, IDA, `PMID:8107085`): **ACCEPT**. Directly supported by `PMID:8107085`, which characterizes ssDNA-dependent NTPase translocation and helicase unwinding by gp41 along ssDNA.
- `GO:0004386` (helicase activity, IEA, GO_REF:0000043) & `GO:0016787` (hydrolase activity, IEA, GO_REF:0000043): **MODIFY** to `GO:0003678` (DNA helicase activity).
- `GO:0005524` (ATP binding, IEA, GO_REF:0000120): **ACCEPT**. ATP (or GTP) binding induces hexamerization and powers DNA translocation (`PMID:8107085`).
- `GO:0000166` (nucleotide binding, IEA, GO_REF:0000043): **MODIFY** to `GO:0005524` (ATP binding).
- `GO:0003677` (DNA binding, IEA, GO_REF:0000043): **ACCEPT**. gp41 directly binds single-stranded and forked DNA substrates (`PMID:10871615`, `PMID:8107085`).
- `GO:0039686` (bidirectional double-stranded viral DNA replication, IEA, GO_REF:0000002 & IDA, `PMID:15781450`): **ACCEPT**. Essential replicative helicase at T4 replication forks (`PMID:15781450`).
- `GO:0006260` (DNA replication, IEA, GO_REF:0000120) & `GO:0039693` (viral DNA genome replication, IEA, GO_REF:0000043): **MODIFY** to `GO:0039686` (bidirectional double-stranded viral DNA replication).
- `GO:0006269` (DNA replication, synthesis of primer, IEA, GO_REF:0000043): **KEEP_AS_NON_CORE**. gp41 assembles with the primase gp61 into the primosome complex and is required to activate lagging-strand RNA primer synthesis, although the polymerase active site that synthesizes the RNA primer resides in gp61.
