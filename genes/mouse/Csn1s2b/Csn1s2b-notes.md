# Csn1s2b (mouse epsilon-casein / alpha-S2-casein-like B, P02664) - review notes

- Second murine alpha-s2-like casein (PTHR16656:SF5); mice have 5 functional casein genes [PMID:21789179 "There are 5 functional casein genes in the mouse whereas most other species (including ruminants) only express 3 or 4 functional genes"].
- UniProt FUNCTION: "Important role in the capacity of milk to transport calcium phosphate." (curated, no specific experiment on mouse epsilon-casein found).
- No mouse-specific functional or knockout data located in PubMed searches; function inferred from family membership (Pfam PF00363 Casein, PROSITE PS00306).
- zymogen binding IBA: same bovine t-PA ligand blot source as Csn1s2a [PMID:8186264] -> over-annotation.

## Deep research
- OpenScientist deep research not available at time of review.
- UniProt PE level 2 (transcript evidence only).

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ (and checked against the
abstracts) for the points used.

- No contradiction with the review's family-inferred core function (GO:0140314,
  extracellular, milk). The report describes Csn1s2b as a "secreted milk phosphoprotein",
  but UniProt P02664 is PE 2 (transcript level) and no phosphosites are annotated; the
  review's description, which says the protein has not been characterized individually,
  is kept.
- Verified the report's sequence point that the only cysteine (position 8) is in the
  signal peptide, so the mature chain is cysteine-free and cannot form the disulfide dimers
  seen for bovine alpha-s2-casein. This argues further against the propagated zymogen
  binding (t-PA binding by disulfide-dimeric bovine alpha-s2-casein), which stays
  MARK_AS_OVER_ANNOTATED. The report's claim that alpha-s1 and beta caseins dimerize via
  cysteines was not adopted (not verified for beta-casein).
- Added to the core function: PMID:18420601 (phosphoserine domains of alpha-s caseins
  stabilize calcium phosphate nanoclusters) and the report's sequence-analysis quote on the
  acidic Ser-x-Glu/Asp region.
- Not used: predicted C-terminal antibacterial peptides (inferred only), STAT5/GR
  regulation, FAM20C, and knockout data for other caseins (PMID:16698927, 20704729), which
  do not test Csn1s2b.
- No new GO:0140314 existing-annotation row was added (validation warns that the core term
  is not in existing_annotations); with transcript-level evidence only, the core function
  stays an inference rather than a NEW annotation, as originally decided.
