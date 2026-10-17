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

## Falcon deep research (DNAH12-deep-research-falcon.md, 835 s, 23 citations)
Checked against the cached full texts:
- PMID:39071892: patient AY0749 kept DNAH1 and DNAI2 but lost SPAG6
  [PMID:39071892 "the expression levels of DNAH1 and DNAI2 were
  predominantly normal, whereas the expression of SAPG6 was mostly
  absent"]. This conflicts with the eLife report of DNAH1 loss; added as a
  suggested question.
- PMID:39071892 cohort frequency is 3/1532. ICSI gave one live birth
  (AY0749), one clinical pregnancy (NJ0278), and one couple (XM0178)
  awaiting transfer. The report's claim of a miscarriage is not in the
  cached text, so I have not used it.
- New: PMID:36792588 (DNALI1) IP-MS from human sperm recovers DNAH12; DNAH12
  stays in DNALI1-mutant sperm.
- New: PMID:39849482 (IQUB) RS1 loss depletes DNAH12, which places it near RS1.
- The report flags a length discrepancy: Geng cites a predicted 3960-aa
  protein, while UniProt Q6ZR08 and the eLife construct are 3092 aa.

## Variant nomenclature (checked against sequences)
- Q6ZR08 (3092 aa, ENST00000351747) and NM_001366028.2 (3960 aa, isoform 4)
  differ by 19 residues upstream of about position 772. So p.Gln2077Ter
  (c.6229C>T) and p.Gln2096Ter (c.6286C>T) are the same nonsense allele;
  the flanking sequence YKQSV is identical in both.
- That allele is reported in PMID:40146200 (P9), PMID:39071892 (NJ0278),
  PMID:42321500 (patient 2) and PMID:39267058 (candidate), all in Chinese
  men. ClinVar has it twice: VCV 3899932 and VCV 5006672.
- PMID:34791246 genotype from OMIM's ClinVar records: p.Pro1389Leu /
  p.Ser2178Ter (NM_001366028); VCV 3899930 and 3899931.

## Ortholog, family and missing IBAs (checked 2026-10-11)
- Mouse ortholog: Dnah12, MGI:107720, UniProt Q3V0Q1, 3086 aa.
- Human DNAH12 has no IBA (QuickGO: 12 annotations, none IBA, none NOT).
  Mouse Dnah12 has 8 IBAs from three PAINT nodes: PTN000743491 (motor
  activity, intermediate chain and light intermediate chain binding, cilium
  movement, 9+2 motile cilium), PTN008951089 (inner dynein arm assembly,
  sperm flagellum assembly) and PTN008503981 (inner dynein arm).
- Cause: the PANTHER 19 API classifies the orthologs into different families.
  Human Q6ZR08 is in subfamily PTHR46532:SF11 ("DYNEIN AXONEMAL HEAVY CHAIN
  12") of family PTHR46532 ("MALE FERTILITY FACTOR KL5"; 34 leaves, and
  DNAH12 is its only human or mouse member). Mouse Q3V0Q1 is in subfamily
  PTHR10676:SF255 (also "DYNEIN AXONEMAL HEAVY CHAIN 12") of family PTHR10676
  ("DYNEIN HEAVY CHAIN FAMILY PROTEIN"), whose tree contains PTN000743491 and
  PTN008951089. Names are from interpro/panther/panther.obo. Both subfamilies
  are correctly named, so the anomaly is the family-level placement only.
  Checked with the PANTHER treeinfo and geneinfo services.
- The PTN008951089 IBD for GO:0036159 is seeded by DNAH3 (Q8TD57), DNAH7
  (Q8WXX0) and MGI:2683040, all structural IDA heavy chains
  (interpro/panther/PTHR10676/PTHR10676-paint.tsv). That passes the
  comparator check for proposing GO:0036159 on DNAH12. The other
  GO:0036159 holders in this corpus (CCDC39/CCDC40) carry it as
  acts_upstream_of_or_within.
- A third assignment exists: the InterPro/UniProt PANTHER cross-references
  put both in PTHR22878:SF70 (named "DYNEIN HEAVY CHAIN 2, AXONEMAL").
  interpro/panther/PTHR22878/PTHR22878-entries.csv lists human, mouse and rat
  DNAH12 all in SF70.
- Human DNAH12 is listed in projects/paint/human-no-IBA.tsv under
  PTHR46532.
