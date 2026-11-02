# gtl-2 review notes

## 2026-10-28 session

- `just fetch-gene worm gtl-2` hit two UniProt read timeouts / a 429 before succeeding; it resolved
  Q20766 (WormBase F54D1.5, WBGene00001796, GeneID 178036), which matches the requested accession.
  GOA has 9 rows: 4 IBA (PTN001013045 TRPM node), 4 IEA (InterPro IPR005821, SubCell), 1 IDA
  (basal plasma membrane, PMID:20221407).
- No deep-research API; literature summary in `gtl-2-deep-research-manual.md`.
- Key paper PMID:20221407 read in full (cached full text): GTL-2::GFP basal membrane of excretory
  cell; GTL-2-dependent outwardly rectifying La3+-sensitive current in excretory cells; selectivity
  NOT measured; hypermagnesemia (~1.5x Mg2+) and Mg2+-specific hypersensitivity; gtl-1 lf suppresses.
- Other full-text papers: PMID:22100061 (epidermal wound Ca2+ requires GTL-2, cell-autonomous),
  PMID:21549603 (epidermal/excretory/pharynx expression; acr-2(gf) suppression via ion homeostasis),
  PMID:34032213 (pathogen avoidance), PMID:26606136 (gon-2 revertant screen). PMID:24564792 abstract only.

## Decisions

- MF: keep at monoatomic cation channel activity (IBA ACCEPT; IEA ion channel -> MODIFY to cation channel).
  Not refined to calcium or magnesium channel because GTL-2 selectivity was never measured
  [PMID:20221407 "we were not able to determine the relative permeability of GTL-2 to different cations"].
- BP: metal ion transport IBA -> MODIFY to magnesium ion transmembrane transport (GTL-2-dependent
  current + basal localization + Mg2+-specific excretion defect + tissue-specific rescue). Ca2+
  transport left as a question (epidermal Ca2+ influx data are genetic only).
- NEW magnesium ion homeostasis (IMP, PMID:20221407). Who performs the step? GTL-2 itself is the
  proposed basal-membrane entry route for Mg2+ into the excretory cell, so it does part of the work
  of Mg2+ excretion. Comparator: human TRPM7 (Q96QT4) carries GO:0010960/GO:0010961 in GOA; TRPM6 carries
  GO:1903830. Phenotypes in neurons (convulsions), pathogen avoidance, clozapine and gonadogenesis
  are downstream/systemic and are not proposed.
- CC: basal plasma membrane IDA ACCEPT; plasma membrane IBA ACCEPT (also epidermal surface);
  membrane IEA -> MODIFY plasma membrane.
- Wound healing / epidermal Ca2+ influx not proposed as NEW (single study, could be indirect via
  systemic ions, gating unknown); raised as a suggested question.
