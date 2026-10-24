# lptC (P0ADV9, E. coli K-12) notes

## Provenance
- Provider deep research was NOT run for this gene; no `*-deep-research-*.md` file exists.
- Sources used: UniProt record (`lptC-uniprot.txt`), and cached publications
  PMID:18424520, PMID:20720015, PMID:21169485, PMID:22668317, PMID:29449493,
  PMID:30894744 (full text); PMID:16765569 and PMID:17309111 (abstract only).
- No new PMIDs fetched.
- Style/consistency model: `genes/PSEPK/lptC/lptC-ai-review.yaml`.

## Key points
- Bitopic IM protein with a periplasmic beta-jellyroll [PMID:30894744 "LptC has a single N-terminal TM helix (TMC) and a periplasmic β-jellyroll domain (C-bjr)."].
- Binds LPS; LptA displaces LPS from LptC but not vice versa [PMID:20720015].
- The LptC TM helix inserts between LptF and LptG, and LptC inhibits LptB2FG ATPase in nanodiscs [PMID:30894744]. This regulatory role is not asserted as a GO MF; it is raised in suggested_questions.
- LptBFGC stoichiometry is 2:1:1:1 [PMID:20720015], so the LptC dimer seen on overexpression [PMID:21169485] is marked over-annotated.

## Decisions
- GO:0017089 -> MODIFY to GO:0140332 (PSEPK lptC used MARK_AS_OVER_ANNOTATED; MODIFY is used here per current correct-but-general guidance).
- GO:1990351 -> MODIFY to GO:0062051; GO:0016020 -> MODIFY to GO:0005886; GO:0046836 -> MODIFY to GO:0015920.
- Bare protein binding (3 rows) -> REMOVE.
