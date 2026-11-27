# prpD (P77243, b0334) notes

## Session log (2026-10-23)

- Provider deep research (`just deep-research ECOLI prpD --provider ...`) could not be run in this session because provider API credentials were unavailable. No `*-deep-research-*.md` file was created; the review relies on the curated UniProt entry and cached publications (all abstract-only).
- Added comparative references PMID:11294638 (Salmonella PrpD, already cached) and PMID:28956599 (stereochemistry).

## Function

- PrpD = AcnC, the residual aconitase of acnAB mutants [PMID:11782506 "Inactivation of prpD abolished the residual aconitase activity of an AcnAB-null strain"]; most active with 2-methylcitrate [PMID:11782506 "Purified PrpD catalysed the dehydration of citrate and isocitrate but was most active with 2-methylcitrate."].
- AcnC is minor [PMID:11782506 "represents no more than 5% of total wild-type aconitase activity"].
- Pathway step: [PMID:12473114 "the isomerization of (2S,3S)-methylcitrate to (2R,3S)-2-methylisocitrate requires a novel enzyme, methylcitrate dehydratase (PrpD), and the well-known enzyme, aconitase (AcnB), of the tricarboxylic acid cycle"]; Km [PMID:12473114 "PrpD is specific for (2S,3S)-methylcitrate (Km = 440 micro m)"].
- Lack of strict stereospecificity [PMID:28956599 "We also showed for the first time that the E. coli homologue PrpD exhibited the same lack of stereospecificity."].

## Conflicts noted

- Fe-S: E. coli PrpD reported with one labile [2Fe-2S] [PMID:11782506 "having one unstable [2Fe-2S] cluster per monomer, which is needed for maximum catalytic activity"], but Salmonella PrpD [PMID:11294638 "Homogeneous PrpD enzyme did not contain an iron-sulfur center"]. Kept 2Fe-2S binding as non-core.
- cis-aconitate hydration: Brock et al. report hydration at 5x lower rate [PMID:12473114], Blank et al. report PrpD "failed to hydrate cis-aconitate and related substrates containing double bonds" [PMID:11782506]. Aconitate hydratase activity kept as non-core in all rows.

## Curation decisions

- Accept: 2-methylcitrate dehydratase activity (3 rows), propionate catabolic process.
- Non-core: aconitate hydratase activity (3 rows), 2Fe-2S cluster binding (2 rows).
- Over-annotated: TCA cycle (UniPathway IEA).
- Modify: propionate metabolic process (IBA) -> propionate catabolic process.
- Too general: lyase activity.
