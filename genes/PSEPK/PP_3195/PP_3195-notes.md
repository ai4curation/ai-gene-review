# PP_3195 curation notes

- UniProt Q88I07 names a Peptidase S9 catalytic-domain protein
  [file:PSEPK/PP_3195/PP_3195-uniprot.txt "RecName: Full=Peptidase S9 prolyl
  oligopeptidase catalytic domain-containing protein"]. This is a fold-level
  prediction, not evidence for a peptide substrate.
- OpenScientist identifies KEGG K26184/FdeB and the predicted R13077 lactone
  hydrolysis [file:PSEPK/PP_3195/PP_3195-deep-research-openscientist.md "KEGG
  links FdeB (K26184) to **reaction R13077**, classified as a **hydrolase**"] but
  explicitly reports no direct PP_3195 characterization
  [file:PSEPK/PP_3195/PP_3195-deep-research-openscientist.md "No direct
  biochemical or genetic characterization of PP_3195/FdeB itself has been
  published."].
- A committed global alignment gives 81.6% identity to the corresponding
  Herbaspirillum locus protein D8J0W6 and finds the same GVSLG motif in both
  sequences [file:PSEPK/PP_3195/PP_3195-bioinformatics/RESULTS.md "Pairwise
  identity over aligned residue pairs: 81.6%"]. Neither protein has direct
  R13077 evidence.
- GO:0052689 is retained as the substrate-neutral core MF. The automated
  serine-type peptidase and proteolysis annotations are removed because no
  peptide substrate or biological proteolysis role is supported. GO:0009812 is
  added at ISS level for the predicted pathway role.
- No cellular-component term is asserted. The report's AlphaFold triad geometry
  and cytoplasmic localization were not independently reproduced and are not
  needed to capture the defensible function.
