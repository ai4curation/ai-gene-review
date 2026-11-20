# catA (Rhodococcus opacus 1CP, P95607) notes

## Provenance

- Deep research was attempted with `just deep-research RHOOP catA --provider falcon`
  (2026-10-23) and failed with "Failed to authenticate"; no other provider key is
  configured. The review uses the UniProt record and cached primary literature.
- Strain 1CP was described as Rhodococcus erythropolis 1CP and later reclassified as
  R. opacus 1CP; UniProt P95607 cites the 1CP sequence paper [PMID:8990288] under
  R. opacus.
- Reviewed as the Gram-positive (actinobacterial) exemplar of the CatA step in
  `modules/catechol_ortho_cleavage.yaml`.

## Evidence summary

- catA catB catC form one cluster in 1CP and the clone expresses all three activities
  [PMID:8990288 "The clone thus obtained expressed catechol 1,2-dioxygenase, muconate
  cycloisomerase, and muconolactone isomerase activities."].
- Crystal structures of the 1CP catechol 1,2-dioxygenase and its adducts with catechol
  and substituted catechols, with kcat measurements [PMID:20040374 "The first
  crystallographic structures of a catechol 1,2-dioxygenase from a Gram-positive
  bacterium Rhodococcus opacus 1CP (Rho 1,2-CTD), a Fe(III) ion containing enzyme
  specialized in the aerobic biodegradation of catechols"]. UniProt P95607 lists the
  corresponding PDB entries (3HGI, 3HHX, 3HHY, ...) although it does not cite the
  paper in its RX lines.
- Family: NCBIfam TIGR02438 (actinobacterial catechol 1,2-dioxygenase), not the
  proteobacterial TIGR02439; PANTHER PTHR33711:SF7. The actinobacterial enzymes are
  related to the Gram-negative chlorocatechol 1,2-dioxygenases [PMID:8990288].

## Review decisions

- Accept GO:0018576 (core) and GO:0008199.
- Refine GO:0003824 and GO:0016702 to GO:0018576, GO:0005506 to GO:0008199, and
  GO:0009712 to GO:0019615.
