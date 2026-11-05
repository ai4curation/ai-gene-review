# thiI (P77718, ECOLI) — curation notes

## 2026-11-05: literature search and review

No deep-research provider API keys were available in this session, so no
`-deep-research-*` file exists. The literature search was done by hand:

- PubMed `ThiI[Title] AND (tRNA OR thiouridine OR thiamin)`: 12 hits. The relevant
  ones were cached: PMID:21724998, PMID:21742874, PMID:19509301, PMID:18604845,
  PMID:16343540, PMID:11443125, PMID:10753862, PMID:10722656, PMID:10595545,
  PMID:9209060. The rest concern the unrelated *Aspergillus* thiamine transporter
  also named thiI.
- Targeted: PMID:15037613 (E. coli substrate specificity), PMID:22773787
  (B. subtilis thiI/nifZ), PMID:22904325 (M. maripaludis ThiI). Every cached entry is
  abstract-only.

Key points used in the review:

- E. coli ThiI makes s4U8 by U8 adenylation (PP-loop) and sulfur transfer from IscS
  through rhodanese Cys456 [PMID:15037613 "IscS catalyzes sulfur transfer from
  l-cysteine to ThiI, which utilizes Mg-ATP to activate uridine 8 in tRNA and
  transfers sulfur to give s4U"; PMID:10722656].
- The thiazole/thiamine role belongs to the rhodanese domain [PMID:21724998 "the
  C-terminal rhodanese domain of ThiI was sufficient for thiazole synthesis in
  vivo"]. Rhodanese-less ThiI (B. subtilis, archaea) is not needed for thiamine
  [PMID:22773787; PMID:22904325].
- InterPro2GO IPR020536 → GO:0004810 (CCA-adding) is wrong for every ThiI. Reported
  as https://github.com/geneontology/go-annotation/issues/6646 and recorded as a
  `source_defects` entry on the GO:0004810 row.

Found through the RHEA completeness project (projects/RHEA/RHEA-SWISSPROT-COMPLETENESS.md):
every one of the 287 Swiss-Prot entries carrying RHEA:24176 is annotated to GO:0004810 by
InterPro2GO.
