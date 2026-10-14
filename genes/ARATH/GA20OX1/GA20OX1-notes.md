# GA20OX1 (GA5, AtGA20ox1; At4g25420; UniProt Q39110) - curation notes

- Accession Q39110 = GAOX1_ARATH verified.
- Falcon deep research attempted and failed (exit code 1).

## Function
- GA12 -> GA15 -> GA24 -> GA9 (RHEA:60772) [PMID:7630935 "each of which oxidized GA12 at C-20 to GA15, GA24, and the C19 compound GA9, a precursor of bioactive GAs"]; GA53 -> GA44, GA19 -> GA20 [PMID:7604047].
- ga5 nonsense allele [PMID:7604047]; ga5 has reduced C19-GAs [PMID:2236013].
- Partially redundant with GA20ox2 for elongation growth, flowering, fertility [PMID:18069939].

## Regulation (non-core)
- GA feedback repression [PMID:10330476 "Negative feedback regulation of GA5 expression was demonstrated in stems of Arabidopsis by bioactive GAs but not by inactive GA."]
- Long-day/far-red induction [PMID:7604047; PMID:15923331].

## Curation decisions
- short-day photoperiodism, flowering (IEP) -> KEEP_AS_NON_CORE. Evidence is transcript induction on SD->LD transfer, which does not place GA20ox1 in either SD or LD photoperiodic flowering; GA is classically required for Arabidopsis flowering under short days (ga1 fails to flower in SD; Wilson et al. 1992 Plant Physiol, not cached), consistent with the curator's SD term. GA20ox1/GA20ox2 redundantly promote flowering time [PMID:18069939]. The SD-only ga5-3 phenotype in PMID:15923331 is for EOD-FR petiole elongation, not flowering. (Earlier draft MODIFYed to long-day; reverted after PR review.)
- GA signaling TAS over-annotated; leaf development (overexpression) non-core.
