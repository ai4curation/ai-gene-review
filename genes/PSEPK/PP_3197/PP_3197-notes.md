# PP_3197 curation notes

- UniProt Q88I05 is an unreviewed 313-aa protein described only as a
  glyoxalase-family protein; this establishes the broad VOC fold, not a
  glyoxalase reaction [file:PSEPK/PP_3197/PP_3197-uniprot.txt
  "SubName: Full=Glyoxalase family protein"].
- OpenScientist assigns PP_3197 to KEGG K26181/FdeC and R13075, but explicitly
  reports no direct target characterization
  [file:PSEPK/PP_3197/PP_3197-deep-research-openscientist.md "No direct
  experimental characterization of PP_3197 itself."].
- The experimental anchor is the Herbaspirillum seropedicae ortholog: an fdeC
  mutant accumulated the hydroxylated flavanone intermediate, supporting FdeC
  A-ring cleavage in that organism [PMID:27059806 "that is subsequently
  dioxygenated and cleaved at the A-ring by the FdeC"]. This is ISS support for
  PP_3197, not direct experimental evidence on KT2440.
- The exact reaction has no cached GO term. GO:0016702 is the most specific
  available two-oxygen-atom-incorporating MF; GO:0009812 is the available broad
  flavonoid BP because no catabolic child is present in the local ontology.
- A committed pairwise alignment reproduces 69.5% identity over 305 aligned
  residue pairs and exact conservation of the reported GCEHFTFHMG motif
  [file:PSEPK/PP_3197/PP_3197-bioinformatics/RESULTS.md "Pairwise identity over
  aligned residue pairs: 69.5%"]. This replaces the report's unreproduced 71.3%
  figure as the quantitative ISS support.
- No cellular-component assertion is made: the soluble/cytoplasmic assignment
  is prediction-only and is not needed to capture the core chemistry.
