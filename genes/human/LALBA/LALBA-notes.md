# LALBA (Human alpha-lactalbumin, UniProt P00709) curation notes

Part of a family-batched review of alpha-lactalbumin across human, mouse, rat and cow
(human/LALBA, mouse/Lalba, rat/Lalba, BOVIN/LALBA); conclusions and actions are kept
identical across the four orthologs for the same claim.

## Sources used
- OpenScientist deep research report (`LALBA-deep-research-openscientist.md`) read first and treated
  as leads; all claims used in the review were checked against cached PubMed records.
- UniProt entry (LALBA-uniprot.txt): curated FUNCTION "Regulatory subunit of lactose synthase,
  changes the substrate specificity of galactosyltransferase in the mammary gland making glucose
  a good acceptor substrate for this enzyme."

## Core biology (verified)
- Lactose synthase is a 1:1 complex of B4GALT1 (catalytic) and alpha-lactalbumin (regulatory)
  [PMID:11419947 "The lactose synthase (LS) enzyme is a 1:1 complex of a catalytic component,
  beta1,4-galactosyltransferse (beta4Gal-T1) and a regulatory component, alpha-lactalbumin (LA)"].
- Mechanism: LA holds glucose in the B4GALT1 acceptor site [PMID:11419947 "Thus, the role of LA is
  to hold Glc by hydrogen bonding with the O-1 hydroxyl group in the acceptor-binding site on
  beta4Gal-T1"]; kinetic specifier mechanism [PMID:3922406 "exert its substrate-specifying action
  through competitive and mutually exclusive binding with the N-acetylglucosamine analogues
  accompanied by an increased affinity for glucose"].
- GO representation: LALBA does not catalyse UDP-Gal + Glc = UDP + lactose (GO:0004461, verified
  definition in OLS). Captured as enables GO:0140767 enzyme-substrate adaptor activity (OLS
  definition: adaptor that recruits substrate to enzyme, contributing to substrate selection),
  contributes_to GO:0004461. GO has no lactose synthase complex term (OLS search, 2026-10-24);
  Complex Portal models it. Used GO:1990234 transferase complex (is_a catalytic complex
  GO:1902494, which human B4GALT1 review uses).
- Location of action: Golgi lumen [PMID:34125364 "The lactose synthase complex is formed by
  B4GALT1 and LALBA in the Golgi"]; then secreted [PMID:34125364 "Lactose, LALBA, and B4GALT1
  within vesicles are secreted by exocytosis"]. LALBA is soluble; Golgi membrane rows (human) were
  modified to Golgi lumen.
- Knockouts: Stinnakre et al. 1994 [PMID:8022817 "They produce a highly viscous milk that pups
  appear to be unable to remove from the mammary gland. This milk is rich in fat and protein and is
  devoid of alpha-lactalbumin and lactose."]; Stacey et al. 1995 [PMID:7708733 "Homozygous null
  females are alpha-lac-deficient, produce reduced amounts of thickened milk containing little or
  no lactose, and cannot sustain their offspring."; "Females homozygous for the humanized allele
  lactate normally"]. Bovine transgene rescue [PMID:10095792].
- Calcium: [PMID:8765309 "all alpha-lactalbumins strongly bind Ca(II), but only some c-type
  lysozymes do so."]; [PMID:1918521 bovine site Asp82/87/88 + carbonyls 79/84; CNBr-cleaved loop
  protein "still competent in lactose biosynthesis, although activity was reduced to 1/40th"].

## Lysozyme-family inheritance (IBA)
- Lost lytic activity [PMID:9307874 "Specific amino acid substitutions in alpha-lactalbumin account
  for the loss of the enzyme activity of lysozyme"]; [PMID:21676251 "lacks its bacteriolytic
  activity"]. Trace lytic activity reported at 2-45 x 10^-6 [PMID:3579965] and ~3.6 x 10^-5
  [PMID:8368501] of hen lysozyme: not physiological. IBA lysozyme activity and defence response to
  Gram+/Gram- bacterium were REMOVED (no PANTHER family review exists for PTHR11407 in this repo).
- Antibacterial peptides only after proteolysis [PMID:10076060 "alpha-Lactalbumin in contrast to its
  polypeptide fragments was not bactericidal against all the bacterial strains tested."].

## HAMLET/BAMLET
- Non-native complex of partially unfolded protein with oleic acid [PMID:23130929]; oleic acid is
  the cytotoxic agent [PMID:23580643 "the protein portion of HAMLET ... is not the origin of their
  cytotoxicity"]. Not treated as an in vivo function (human apoptosis/signalling TAS rows removed).

## Open doubts
- Whether lactation (GO:0007595) should be proposed: not added, since LALBA's contribution is via
  lactose synthesis, already captured; flagged implicitly in suggested questions.

## Review follow-up (PR #5395 reviewer suggestions, 2026-10-24)

- Complex rows: reason now states that the human B4GALT1 review uses GO:1902494 catalytic complex
  and that GO:1990234 transferase complex is a more specific descendant of it.
- Added the lactose synthase complex entry to proposed_new_terms, mirroring the B4GALT1 review
  (same name, definition, parent GO:1902494 and RHEA:12404 mapping); the suggested question now
  points at it.
- is_active_in extracellular region (IBA, PTN000150627): source defect recorded against GO_Central
  (is_active_in -> located_in); the action stays KEEP_AS_NON_CORE.
- InterPro2GO IPR000545 -> GO:0004461: source defect recorded (enables -> contributes_to). The human
  row is a UniProt combined IEA (GO_REF:0000120) built from InterPro2GO plus an Ensembl Compara
  transfer of the mouse MGI IDA, so its defect explanation attributes the fix upstream.
- Calcium-binding core function now also lists GO:0005576 extracellular region (the structural Ca2+
  site maintains the fold of the secreted protein in milk).
