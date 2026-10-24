# UGP1 (YKL035W, P32861) notes

## Identity and activity
- Major UTP--glucose-1-phosphate uridylyltransferase (UGPase, EC 2.7.7.9), UDPGP type 1 family, homo-octamer [UniProt:P32861 "SUBUNIT: Homooctamer."].
- Identified as UGP1 by galU complementation, overexpression gives a 40-fold activity increase [PMID:7588797 "multi-copy expression of YKL248 resulted in a 40-fold increase in UGPase activity"].
- Essential [PMID:7588797 "showed that UGPase is essential for cell viability"]; lethality is due to cell-wall failure [PMID:9252577 "the loss of function of UGP1 is lethal mainly because of the inability of yeast cells to properly form the cell wall"].
- Recombinant ScUGP assayed alongside 10 other UGPases [PMID:40178507 "fungi Saccharomyces cerevisiae (ScUGP)"].
- Promiscuous in vitro uridylyl transfer to bisphosphonates and isoprenoid triphosphates [PMID:22580055 "UDP-glucose serves as uridylyl donor to triphosphate derivatives of the mevalonate pathway"] -> uridylyltransferase IDA kept non-core.

## Regulation / partitioning
- PAS kinases Psk1/Psk2 phosphorylate Ugp1 without changing activity; phosphorylated Ugp1 goes to the cell periphery and favours glucan over glycogen [PMID:17531808 "phosphorylation by Psk1 or Psk2 targets Ugp1 to the cell periphery"; "inability to phosphorylate Ugp1 is associated with a weak cell wall, decreased glucan content, and increased glycogen content"].
- The 4 'protein binding' IPI rows are all PSK1/PSK2 interactions (kinase-substrate) -> REMOVE as uninformative MF.

## Downstream pathways (precursor supply)
- UDP-Glc feeds glycogen, trehalose, beta-glucans and Dol-P-Glc; reducing UDP-Glc lowers glycogen and beta-glucan proportionally [PMID:9252577 "causing a proportional decrease in both glycogen and beta-glucans"].
- Process annotations for glycogen, trehalose and beta-1,6-glucan biosynthesis kept as non-core; core BP = GO:0120530 UDP-alpha-D-glucose biosynthetic process.
- YeastPathways RCA 'carbohydrate biosynthetic process' (PWY3O-1565, Dol-P-Glc superpathway) -> MODIFY to GO:0120530.

## Paralog
- YHL012W is a WGD paralog (UGPA2_YEAST); uncharacterised, cannot replace UGP1.
