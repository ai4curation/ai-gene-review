# Curation Notes: Bacteriophage T4 `dda` (ATP-dependent DNA helicase Dda, P32270)

## Overview
- **Gene symbol:** `dda` (gpDda)
- **UniProt ID:** `P32270` (`DDA_BPT4`)
- **Length:** 439 amino acids
- **Function:** Non-hexameric superfamily 1B (SF1B) ATP-dependent 5'-3' DNA helicase that unwinds duplex DNA as a monomer or cooperative oligomer, displaces DNA-bound protein roadblocks (such as host RNA polymerase), stimulates replication origin initiation, and promotes template switching during replication fork repair.

## Biological Role and Mechanism
- Dda (DNA-dependent ATPase) is a 439-amino-acid SF1B helicase that couples ssDNA-stimulated ATP hydrolysis to rapid (~250 bp/s) 5' -> 3' translocation and duplex DNA unwinding (`PMID:1328208`, `PMID:12411580`).
- Pre-steady-state kinetic studies established that Dda is capable of rapid oligonucleotide unwinding as a functional monomer (`PMID:12411580`), while multiple monomers arrayed along longer single-stranded tails act streptavidin- and RNA-polymerase-displacement motors via functional cooperativity (`PMID:7806534`, PubMed 22504228).
- During T4 infection, Dda plays an early role in origin-dependent DNA replication initiation, provides an alternative helicase pathway to gp41 for replication past DNA-bound RNA polymerase barriers (`PMID:7806534`), and acts with the UvsX recombinase to promote replication fork strand switching across DNA lesions (`PMID:17823128`).

## Review of Existing GO Annotations
- `GO:0043139` (5'-3' DNA helicase activity, IEA, GO_REF:0000003; EXP, `PMID:12411580`; EXP, `PMID:17823128`): **ACCEPT**. Directly and specifically captures the core 5'-3' DNA unwinding activity of Dda across all three annotations.
- `GO:0004386` (helicase activity, IEA, GO_REF:0000043 & IDA, `PMID:7806534`): **MODIFY** to `GO:0043139` (5'-3' DNA helicase activity). Both rows share the parent term `GO:0004386`, which is refined by the specific descendant `GO:0043139` already present in the review.
- `GO:0016887` (ATP hydrolysis activity, IEA, GO_REF:0000116 & EXP, `PMID:1328208`): **ACCEPT**. Dda is a DNA-dependent ATPase that hydrolyzes ATP to fuel 5'-3' ssDNA translocation and duplex unwinding (`PMID:1328208`).
- `GO:0005524` (ATP binding, IEA, GO_REF:0000043): **ACCEPT**. Essential for ATP hydrolysis and helicase motor activity.
- `GO:0000166` (nucleotide binding, IEA, GO_REF:0000043): **MODIFY** to `GO:0005524` (ATP binding).
- `GO:0016787` (hydrolase activity, IEA, GO_REF:0000043): **MODIFY** to `GO:0043139` (5'-3' DNA helicase activity) and `GO:0016887` (ATP hydrolysis activity).
- `GO:0016853` (isomerase activity, IEA, GO_REF:0000043): **REMOVE**. Automated keyword mapping artifact resulting from EC 5.6.2.3 (`5'-3' DNA helicase`) historically or cross-map-wise triggering a broad EC 5 / isomerase keyword rule. Dda is a translocase/helicase and ATPase, not an isomerase.
- `GO:0006260` (DNA replication, IEA, GO_REF:0000043): **ACCEPT**. Dda stimulates T4 DNA replication initiation at origins and facilitates replication fork progression past protein roadblocks (`PMID:1328208`, `PMID:7806534`).
