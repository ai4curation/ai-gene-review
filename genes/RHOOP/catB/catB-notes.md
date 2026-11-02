# catB (Rhodococcus opacus 1CP, P95608) notes

## Provenance

- Deep research was attempted with `just deep-research RHOOP catB --provider falcon`
  (2026-10-23) and failed with "Failed to authenticate"; no other provider key is
  configured. The review uses the UniProt record and cached primary literature.
- Strain 1CP was originally described as Rhodococcus erythropolis 1CP.
- Reviewed as the actinobacterial exemplar of the CatB step in
  `modules/catechol_ortho_cleavage.yaml` and as the reference protein of the PTHR48080
  family review.

## Evidence summary

- Muconate cycloisomerase was purified from benzoate-grown 1CP [PMID:7751292 "Muconate
  cycloisomerase (EC 5.5.1.1) and chloromuconate cycloisomerase (EC 5.5.1.7) were
  purified from extracts of Rhodococcus erythropolis 1CP cells grown with benzoate or
  4-chlorophenol, respectively."]. The gene was cloned using peptide sequence of that
  enzyme [PMID:8990288 "Based on sequences of the N terminus and of tryptic peptides of
  the muconate cycloisomerase, a fragment of the corresponding gene has now been
  amplified"], so P95608 is the purified benzoate-induced enzyme.
- The 1CP muconate cycloisomerase converts 2-chloromuconate only to
  5-chloromuconolactone and cannot dehalogenate [PMID:7751292]; 1CP has a separate
  chloromuconate cycloisomerase for chlorophenol degradation. GO:0018850 is therefore
  over-annotation from the InterPro IPR013370 mapping.
- Family: NCBIfam TIGR02534 (muconate cycloisomerase), the same model as proteobacterial
  CatB, but PANTHER places P95608 in PTHR48080 (D-galactonate dehydratase-related,
  SF3), not in PTHR48073 with proteobacterial CatB. Both are mandelate
  racemase/muconate lactonizing enzyme families of the enolase superfamily.

## Review decisions

- Accept GO:0018849 (core) and GO:0030145.
- Remove GO:0009063 (superfamily conserved-site over-mapping).
- Mark GO:0018850 as over-annotated; refine GO:0003824 to GO:0018849.
