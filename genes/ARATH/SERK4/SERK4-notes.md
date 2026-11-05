# SERK4 review notes

- 2026-10-28: fetched SERK4 (Q9SKG5, At2g13790, GeneID 815862); 46 GOA rows.
  Cached all GOA PMIDs plus PMID:22253607, PMID:21693696, PMID:34535661,
  PMID:23921992. Abstract-only: 17600708, 11706164, 18667726, 20108170,
  19105183, 19616764, 23921992.
- No deep-research API keys; literature synthesis written by hand in
  SERK4-deep-research-manual.md.

## Decisions

- Core MF: transmembrane receptor protein Ser/Thr kinase activity (GO:0004675)
  acting as co-receptor (dual-specificity; Tyr autophosphorylation
  [PMID:19124768 "all appear to be dual-specificity kinases"]).
  General kinase rows (GO:0004672, GO:0004674) MODIFIED to GO:0004675.
- GO:0004714 (receptor tyrosine kinase) from EC 2.7.10.1 mapping: marked over-
  annotated; Tyr autophosphorylation in vitro is not receptor-TK signalling.
- Core BPs: BR signalling (accepted, IGI with BRI1/SERK1/BAK1
  [PMID:22253607 "SERK1, BAK1, and BKK1 are the major players for BR signaling"]),
  PRR signalling (NEW, GO:0002221; covers flg22/elf18 PAMPs, Pep1 DAMP and SCOOP
  phytocytokines; SERK4 is a kinase-active co-receptor that transphosphorylates
  with the receptor, so it does work in the pathway; comparator BAK1 carries
  GO:0140426 in GOA).
- Plant-type HR rows (IBA + IGI): bak1 bkk1 shows spontaneous cell death - SERK4
  restrains cell death; MODIFY to negative regulation of programmed cell death
  (GO:0043069), source_defects recorded.
- Chloroplast ISM REMOVE (signal peptide + TM; secretory pathway).
- Mitochondrion HDA: over-annotated, SEC profiling of membrane fraction.
- Seedling development IMP: lethality is secondary to autoimmune cell death,
  over-annotated.
- Hypoxia HEP: expression only, over-annotated.
- Bare protein binding (15 rows): REMOVE per policy; interactions are real
  (ECD screens), informative partner binding captured by GO:0033612 rows.
- Stomatal development: not added as NEW; SERK4 is the least important SERK in
  this pathway [PMID:26320950 "descending order of importance from BAK1, SERK2, SERK1 to SERK4"].

## 2026-10-28 correction: protein phosphorylation row (PR #5674 review)

The GO:0006468 protein phosphorylation ISS row is now ACCEPT rather than MODIFY to protein
autophosphorylation. SERK4 also transphosphorylates its partner LRR receptor kinases, and GO has no more
specific term for phosphorylating another protein. Autophosphorylation is recorded as a separate NEW
GO:0046777 IDA row (PMID:19105183; UniProt PTM).
