# glcF (P52074, b4467) notes

## Deep research
- 2026-10-23: perplexity deep research is unavailable in this environment
  (failed for glcD: "Provider 'perplexity' not available. Available: falcon,
  openscientist"). Review based on cached publications and the UniProt record.

## Summary of evidence
- glcF insertion mutant loses glycolate oxidase activity; GlcF resembles
  iron-sulfur proteins
  [PMID:8606183 "the one from glcF was found to be similar to iron-sulfur proteins"].
- GlcF detected only in the membrane fraction (full text, curated by UniProt)
  [file:ECOLI/glcF/glcF-uniprot.txt "And the GlcF subunit itself could only be detected in"].
- Two 4Fe-4S ferredoxin-type domains with 8 ligating Cys (PROSITE PRU00711), two
  CCG domains (Pfam PF02754)
  [file:ECOLI/glcF/glcF-uniprot.txt "Note=Binds 2 [4Fe-4S] clusters. {ECO:0000255|PROSITE-ProRule:PRU00711};"].
- IBA plasma membrane row is grounded in GlcF and GlpC (P0A996, anaerobic
  glycerol-3-phosphate dehydrogenase subunit C; checked at rest.uniprot.org).

## Curation decisions
- iron-sulfur cluster binding -> MODIFY to GO:0051539 4 iron, 4 sulfur cluster binding.
- Glycolate dehydrogenase activity rows accepted; core function via
  contributes_to_molecular_function (presumed electron-transfer subunit).
- NEW: part_of GO:0009339 glycolate oxidase complex.
