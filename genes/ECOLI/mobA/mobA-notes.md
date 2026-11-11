# mobA (P32173) notes, E. coli K-12

Deep research providers were unavailable for this session (no API keys), so no
`-deep-research-<provider>.md` file exists. The review is built from the UniProt record
and the cached publications (all abstract-only). PMID:10978348 (Temple and Rajagopalan
2000) was cached for this review.

## Identity

- UniProt P32173, molybdenum cofactor guanylyltransferase, EC 2.7.7.77; synonyms chlB, mob,
  narB; b3857. MobA family (HAMAP MF_00316, PANTHER PTHR19136).
- Curated function [file:ECOLI/mobA/mobA-uniprot.txt "Transfers a GMP moiety from GTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin guanine dinucleotide (Mo-MGD) cofactor."]; also bis-MGD; GTP-specific.

## Evidence

- chlB mutants lack MGD [PMID:1648082 "cells of chlB mutants were found to contain elevated levels of molybdopterin but no detectable molybdopterin guanine dinucleotide"].
- Defined in vitro bis-MGD assembly into DMSOR [PMID:10978348 "Escherichia coli MobA, molybdopterin-Mo, GTP, and MgCl(2) are required and sufficient for the in vitro activation of purified DMSOR expressed in the absence of MobA."].
- Structure; GTP in the N-terminal half, MPT site in the C-terminal half [PMID:10978347 "the GTP-binding site is located in the N-terminal half of the molecule"].
- N-terminal domain sets nucleotide specificity, C-terminal domain the acceptor protein
  (PMID:21081498).

## Curation decisions

- Generic MF rows (GO:0003824, GO:0016779 IBA and ARBA, GO:0070568) MODIFY to GO:0061603.
- GO:0006777 and GO:0019720 MODIFY to GO:1902758 (bis-MGD biosynthesis), which the gene
  carries by IMP and IBA. Same treatment applied to PSEPK/mobA.
- Bare protein binding (two IPI rows) removed per policy.
- Mg ion binding (IDA) and GTP binding kept as non-core; cytoplasm kept as non-core (no direct
  cytosol evidence for MobA).
