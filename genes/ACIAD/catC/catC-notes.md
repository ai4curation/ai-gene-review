# catC (Acinetobacter baylyi ADP1, Q43932) notes

## Provenance

- Deep research was attempted with `just deep-research ACIAD catC --provider falcon`
  (2026-10-23) and failed with "Failed to authenticate"; no other provider key is
  configured. The review uses the UniProt record and cached primary literature.
- Reviewed as the ADP1 exemplar of the CatC step in
  `modules/catechol_ortho_cleavage.yaml`.

## Evidence summary

- catC encodes muconolactone isomerase in the catBCDE cluster [PMID:3003031 "catC,
  muconolactone isomerase (EC 5.3.3.4)"], and the cloned fragment complements a P.
  putida catC mutant [PMID:3003031 "complemented P. putida mutants with lesions in catB,
  catC, pcaD, and pcaE genes"].
- Muconolactone isomerase was purified from A. calcoaceticus and compared with the P.
  putida enzyme [PMID:4215816 title "Muconolactone isomerase from Acinetobacter
  calcoaceticus and Pseudomonas putida"]; the cache holds only the citation (no
  abstract), so it is used as corroboration only.
- catC lies in the catBCIJFD operon [PMID:8125318].
- Family: NCBIfam TIGR03221 (muconolactone delta-isomerase), Pfam PF02426. No PANTHER
  family is assigned in UniProt.

## Review decisions

- Accept GO:0016159 (core).
- Refine GO:0042952 to GO:0019615 catechol catabolic process, ortho-cleavage.
