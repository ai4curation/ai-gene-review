# pps1 (SPCC1442.12, UniProt O94584) notes

- CDP-DAG-dependent PS synthase, ortholog of S. cerevisiae CHO1 (P08456); PANTHER PTHR14269:SF61 [UniProt:O94584]. Naming trap: S. pombe cho1 is NOT this enzyme (it is the OPI3 ortholog).
- "We therefore conclude that pps1 encodes the major PS synthase activity in S. pombe" [PMID:17905925]; deletion has no detectable PS and negligible in vitro activity [PMID:17905925 "They do not produce detectable phosphatidylserine in vivo and possess negligible in vitro phosphatidylserine synthase activity"].
- ER location: "based on the similarity of Pps1-GFP localization to other ER resident proteins, such as BiP" [PMID:17905925]. C-terminal GFP fusion is non-functional: "Since Pps1-GFP fusion proteins are lacking in functionality" [PMID:17905925] - relevant to ORFeome (C-terminal YFP) cytosol/cytoplasm HDA calls.
- Plasma membrane + ER for GFP-Pps1 [PMID:38598031 "Green fluorescent protein (GFP)-Pps1 was localized at the plasma membrane and endoplasmic reticulum regardless of the stress conditions."]; salt sensitivity [PMID:38598031].
- PS gradient at cell tips [PMID:27852900 "We find that PS preferably accumulates at cell tips and defines a gradient of negative charges along the cell surface."].

## Notable decisions
- GO:0016024 CDP-DAG biosynthetic process (EXP, PMID:1324908): MODIFY -> GO:0006659. PS synthase consumes CDP-DAG; it does not make it.
- Cytosol HDA: MARK_AS_OVER_ANNOTATED (integral membrane protein; C-terminal tag non-functional).
- Cytoplasmic vesicle membrane (UniProt SubCell): MARK_AS_OVER_ANNOTATED (structures "of unknown origin").
- PE biosynthesis, PM organization, salt responses: KEEP_AS_NON_CORE (downstream of PS).
