# glcD (P0AEP9, b2979) notes

## Deep research
- 2026-10-23: `just deep-research ECOLI glcD --provider perplexity` failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist"; no API
  key in this environment). No provider deep-research file exists; this review is
  based on the cached publications and the UniProt record.

## Summary of evidence
- GlcD is a subunit of the E. coli glycolate oxidase (glycolate dehydrogenase)
  GlcDEF, encoded in the glcDEFGB operon with malate synthase G
  [PMID:8606183 "The insertional mutation by a chloramphenicol acetyltransferase cassette in either glcD, glcE, or glcF abolished glycolate oxidase activity, indicating that presumably these proteins are subunits of this enzyme."].
- GlcD and GlcE resemble flavoenzymes; GlcF resembles iron-sulfur proteins
  [PMID:8606183 "The proteins encoded from glcD and glcE displayed similarity to several flavoenzymes, the one from glcF was found to be similar to iron-sulfur proteins"].
- Enzyme is membrane-associated
  [PMID:2689218 "The enzyme was found to be largely associated with the cytoplasmic membranes."].
- Biochemistry (Lord 1972; abstract not available in cache, data from UniProt
  curation tied to PMID:4557653): Km 40 uM glycolate, Km 0.7 mM D-lactate, no
  direct reaction with O2, DCIP and PMS as artificial acceptors
  [file:ECOLI/glcD/glcD-uniprot.txt "Does not link directly to O(2), and"];
  [file:ECOLI/glcD/glcD-uniprot.txt "KM=40 uM for glycolate {ECO:0000269|PubMed:4557653};"].
- Domain architecture: full PCMH FAD-binding domain + FAD-oxidase C-terminal
  domain (Pfam PF01565, PF02913; NCBIfam TIGR00387 glcD) -> catalytic FAD subunit.

## Curation decisions
- GO:0003973 (S)-2-hydroxy-acid oxidase activity is O2-dependent by definition;
  E. coli enzyme does not use O2 -> MODIFY to GO:0019154 glycolate dehydrogenase activity.
- GO:0009339 glycolate oxidase complex: definition cites PMID:4557653/PMID:8606183
  but describes an FMN, H2O2-producing, cytoplasmic enzyme (checked via OAK
  sqlite:obo:go). Accepted as the intended complex term; definition issue raised
  in suggested_questions.
- D-lactate dehydrogenase activity: kept as non-core (lower affinity, partially
  purified enzyme).
- DNA damage response IEP (PMID:11967071 global microarray): over-annotation.
