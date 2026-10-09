# NPHP4 notes

Deep research: skipped. Falcon times out and perplexity-lite is unavailable in this environment. The review is based on cached publications, UniProt O75161 and PubMed.

## Key findings
- In Chlamydomonas, NPHP4 is part of the transition-zone barrier [PMID:25150219 "NPHP4 functions at the transition zone as an essential part of a barrier that regulates both membrane and soluble protein composition of flagella"]. It sits distally, near the membrane [PMID:25150219 "NPHP4 is stably incorporated into the distal part of the flagellar transition zone, close to the membrane and distal to CEP290"].
- In C. elegans, NPHP-4 belongs to the NPHP module [PMID:21422230 "MKS-6 and NPHP-4 are collectively required for BB/TZ attachments to membrane."].
- NPHP4 bridges NPHP1 and RPGRIP1L [PMID:17558407; PMID:21565611].
- It is needed for timely tight-junction formation [PMID:19755384].
- It organizes the subapical actin network through INTU/DAAM1 [PMID:26644512 "NPHP4 interacts with Inturned, which facilitated the formation of a tertiary complex between NPHP4 and the actin-nucleating protein Daam1."].
- It regulates Wnt signaling through JADE1 [PMID:22654112 "NPHP4 stabilizes protein levels of Jade-1 and promotes the translocation of Jade-1 to the nucleus."]. This is kept as non-core.

## Decisions
- NAS rows citing PMID:12006559 (an NPHP1-only paper): structural molecule activity was removed; actin organization was kept as non-core on the basis of PMID:26644512; cell-cell adhesion was marked over-annotated.
- All protein-binding rows were removed as uninformative.
- No molecular function is set in core_functions.
