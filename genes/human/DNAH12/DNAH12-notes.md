# DNAH12 notes

## Gene-disease status
- Biallelic DNAH12 loss of function causes asthenoteratozoospermia / MMAF
  (MONDO:0978302 spermatogenic failure 100) [PMID:40146200 "we unveiled six
  biallelic mutations in DNAH12 that co-segregate recessively with male
  infertility in the studied families"].
- Replicated by an independent cohort plus a knockout mouse [PMID:39071892
  "the Dnah12 knock-out mouse revealed severe spermatogenesis failure and
  validated the same male infertility phenotype"], and by two further LoF
  alleles [PMID:42321500].
- The 2021 candidate report (PMID:34089056) left causality open because the
  two missense variants may have been in cis.

## Structure
- 3092 aa, the shortest DNAH. UniProt annotates the stem, AAA1-AAA5 and a
  stalk, but no AAA6, and Pfam has no microtubule-binding domain hit
  [PMID:40146200 "it is the shortest member and lacks a typical
  microtubule-binding domain (MTBD) in the DNAH family"].
- Consequence for GO: the IEA motor-activity and microtubule-based movement
  terms are marked over-annotated, not removed (the paper's figure shows an
  "MT-like" region).

## Mechanism
- Binds DNALI1 and DNAH1 and recruits them to the IDA; binds RSPH1, RSPH9
  and DNAJB13 and helps keep the central pair stable [PMID:40146200].
- Specific to the flagellum: knockout mice have normal tracheal cilia
  [PMID:40146200 "DNAH12 deficiency did not show effects on cilium
  organization and function"].
- ICSI works in patients and mice [PMID:40146200, PMID:39071892,
  PMID:42522280].

## Curation decisions
- Proposed NEW: GO:0036159 inner dynein arm assembly (DNAH12 is itself an
  IDA heavy chain and binds the subunits it recruits, so it does part of
  the work of the process).
- MODIFY dynein complex -> inner dynein arm.
- dynein intermediate chain binding: UNDECIDED (no DNAH12-specific data).
