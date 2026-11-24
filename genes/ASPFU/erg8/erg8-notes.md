# erg8 (AFUA_5G10680) notes

## Evidence journal

- Swiss-Prot curates Q4WV38/AFUA_5G10680 as A. fumigatus erg8, a phosphomevalonate kinase that converts 5-phosphomevalonate to 5-diphosphomevalonate [file:ASPFU/erg8/erg8-uniprot.txt, "5-phosphomevalonate is then further converted to 5-diphosphomevalonate by the phosphomevalonate kinase erg8 (AFUA_5G10680)."].
- The curated catalytic reaction is `(R)-5-phosphomevalonate + ATP = (R)-5-diphosphomevalonate + ADP`, and the pathway entry places Erg8 at step 2/3 of IPP biosynthesis from mevalonate [file:ASPFU/erg8/erg8-uniprot.txt, "Reaction=(R)-5-phosphomevalonate + ATP = (R)-5-diphosphomevalonate +"; file:ASPFU/erg8/erg8-uniprot.txt, "via mevalonate pathway; isopentenyl diphosphate from (R)-mevalonate:"].
- `PTHR31814:SF2` is the fungal phosphomevalonate kinase subfamily and includes Q4WV38 [file:ASPFU/erg8/erg8-uniprot.txt, "DR   PANTHER; PTHR31814:SF2; PHOSPHOMEVALONATE KINASE; 1."].
- Ferreira et al. 2005 gives A. fumigatus ergosterol-pathway context, though the cached abstract does not name erg8 directly [PMID:16110826, "About 20 genes are involved in the A. fumigatus ergosterol biosynthesis pathway. There are several duplicated genes in this pathway."].
- Yasmin et al. 2012 establishes mevalonate as a limiting precursor linking A. fumigatus ergosterol and siderophore biosynthesis, consistent with an essential upstream PMK step supplying IPP/FPP precursors [PMID:22106303, "Consistent with mevalonate being a limiting prerequisite for TAFC biosynthesis, we observed increased expression of 3-hydroxy-3-methyl-glutaryl (HMG)-CoA reductase (Hmg1) under iron starvation"].

## IBA and annotation decisions

- Accept the `GO:0004631` and `GO:0019287` IBAs from `PANTHER:PTN001274235`; the PAINT node is the sound fungal/plant GHMP phosphomevalonate kinase node.
- Accept `GO:0006696` from `PANTHER:PTN001274236`; Erg8 performs the PMK reaction that feeds ergosterol biosynthesis in fungi.
- Accept the corresponding IEA rows to the same molecular function and processes. They reinforce the same claims as the PAINT rows and the Q4WV38 Swiss-Prot record.
- Keep `GO:0005524` ATP binding as non-core because ATP binding is part of the PMK reaction but is less informative than the kinase molecular function.
- Remove the `GO:0005777` peroxisome IBA from plant node `PANTHER:PTN000781523`. The PTHR31814 family review marks this node as needing pruning for fungal Erg8 proteins.
- Newer-paper search: no newer paper directly characterizing A. fumigatus erg8 was found. A 2024 Aspergillus oryzae AoErg8 study exists, but it is cross-species corroboration only and is not needed for the A. fumigatus row-level decisions.
