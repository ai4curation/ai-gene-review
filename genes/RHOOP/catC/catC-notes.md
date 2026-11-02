# catC (Rhodococcus opacus 1CP, P95609) notes

## Provenance

- Deep research was attempted with `just deep-research RHOOP catC --provider falcon`
  (2026-10-23) and failed with "Failed to authenticate"; no other provider key is
  configured. The review uses the UniProt record and cached primary literature.
- Reviewed as the actinobacterial exemplar of the CatC step in
  `modules/catechol_ortho_cleavage.yaml`.

## Evidence summary

- catC is the third gene of the 1CP catABC cluster, and the clone expresses
  muconolactone isomerase activity [PMID:8990288 "The clone thus obtained expressed
  catechol 1,2-dioxygenase, muconate cycloisomerase, and muconolactone isomerase
  activities."; "the genes are transcribed in the order catA catB catC"].
- UniProt records partial protein sequencing (residues 2-21) from the same paper.
- Family: NCBIfam TIGR03221 (muconolactone delta-isomerase), Pfam PF02426; no PANTHER
  family assigned.

## Review decisions

- Accept GO:0016159 (core); refine GO:0042952 to GO:0019615.
