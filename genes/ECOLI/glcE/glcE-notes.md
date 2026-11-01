# glcE (P52073, b4468) notes

## Deep research
- 2026-10-23: `just deep-research` with perplexity was not attempted separately for
  glcE after it failed for glcD in this environment ("Provider 'perplexity' not
  available. Available: falcon, openscientist"). Review based on cached
  publications and the UniProt record.

## Summary of evidence
- glcE insertion mutant loses glycolate oxidase activity
  [PMID:8606183 "The insertional mutation by a chloramphenicol acetyltransferase cassette in either glcD, glcE, or glcF abolished glycolate oxidase activity, indicating that presumably these proteins are subunits of this enzyme."].
  Possible polarity on downstream glcF is not excluded by the abstract.
- GlcE resembles flavoenzymes
  [PMID:8606183 "The proteins encoded from glcD and glcE displayed similarity to several flavoenzymes"].
  It has the PCMH FAD-binding domain (residues 1-173) but no FAD-oxidase C-terminal
  domain [file:ECOLI/glcE/glcE-uniprot.txt "DR   Pfam; PF01565; FAD_binding_4; 1."].
- Historical sequence caution: the original EMBL entry fused glcE and glcF by a
  frameshift [file:ECOLI/glcE/glcE-uniprot.txt "Note=Fuses together glcE and glcF."].
- Membrane association of the enzyme activity
  [PMID:2689218 "The enzyme was found to be largely associated with the cytoplasmic membranes."].

## Curation decisions
- Glycolate dehydrogenase activity rows accepted; core function expressed as
  contributes_to_molecular_function since GlcE is a non-catalytic-domain subunit.
- FAD binding (GO:0071949) kept as non-core (domain-based, not measured).
- NEW: part_of GO:0009339 glycolate oxidase complex (GlcD carries it, GlcE did not).
