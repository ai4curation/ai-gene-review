# GLG1 (YKR058W, P36143) notes

Glycogenin-1, GT8 (EC 2.4.1.186). Redundant with GLG2. Module: glycogen_metabolism_fungal (priming step).

- "These genes encode self-glucosylating proteins that in vitro can act as primers for the elongation reaction catalyzed by glycogen synthase" [PMID:8524228]
- "Yeast cells defective in either GLG1 or GLG2 are similar to the wild type in their ability to accumulate glycogen" ; "Disruption of both genes results in the inability of the cells to synthesize glycogen despite normal levels of glycogen synthase" [PMID:8524228]
- Glycogen synthase activation state reduced in glg1 glg2 [PMID:8524228]
- "In Glg1p, two Tyr residues are implicated, Tyr232 and Tyr600" [PMID:8900126]
- Vacuole localisation in UniProt is by similarity to Komagataella C4R941 (glycophagy cargo) [UniProt:P36143]; S. cerevisiae glycogen is a non-preferred autophagy cargo [PMID:38832010].

## Curation decisions
- protein binding (Gsy2) x3 HTP: REMOVE (uninformative; interaction plausibly real).
- vacuole IEA/ISS: MARK_AS_OVER_ANNOTATED (cargo, not functional site).
- GO:0016757 -> MODIFY to GO:0008466.
