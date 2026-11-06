# imuB curation notes

- ImuB lacks the conserved active-site residues required for Y-family polymerase activity. [PMID:20615954, "lack conserved active-site amino acids required for polymerase activity."]
- Ortholog experiments show that ImuB binds ImuA, DnaE2, and the beta clamp, supporting protein-macromolecule adaptor activity. [PMID:20615954, "DnaE2, as well as with the beta-clamp."]
- In P. putida, ImuB promotes stationary-phase mutant accumulation. [PMID:17331811, "accumulation of stationary-phase mutants up to two-fold."]

## Completion pass (ImuABC module curation)

- Status set to COMPLETE; the GO:0006281 MODIFY row now carries quotes and names its actual
  route: UniProt combined pipeline over UmuC domain IPR001126 plus TreeGrafter node
  PANTHER:PTN002440639 (not a PAINT IBA).
- KT2440 keeps GO:0019985 rather than GO:0042276: ImuB promotes mutation accumulation here
  but DnaE2 suppresses base substitutions, so the cassette's output in this organism is
  antagonistic rather than uniformly error-prone. [PMID:17331811]
