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
- GO:0017089 -> MODIFY to GO:0140332 per current correct-but-general guidance; the P. putida LptC review makes the same refinement.
- GO:1990351 -> MODIFY to GO:0062051; GO:0016020 -> MODIFY to GO:0005886; GO:0046836 -> MODIFY to GO:0015920.
- Bare protein binding (3 rows) -> REMOVE.


## 2026-11-07 — cross-taxon Lpt audit, E. coli member consultation

All original annotation rows, reference findings and core roles were reassessed. Source payloads/order, qualifiers and historical NEW lifecycle remain unchanged. Targeted full-primary reading supports the existing division between LptB ATPase, membrane extractor subunit contributions, bridge transfer and terminal LptDE translocation. Abstract-only source details are not treated as disproven or silently relabeled as newly inspected full-text evidence. Generic location/assembly quotations were strengthened where appropriate; no new annotation was added. PMID42844470 updates whole-bridge regulation: E. coli proteins and an engineered LptC-LptA fusion support the structural analysis, with E. coli functional controls; LPS-null A. baylyi is an expression host, not a new organismal activity assay. The normal cache remains abstract-only; independently acquired publisher full text is documented in the shared literature consultation. LptC self-binding is retained as non-core after examining the WT crosslink/reductant controls and soluble constructs in PMID21169485; monomeric results in PMID20720015 constrain native oligomerization rather than negate the measured interaction. The normal PAINT-loss check reports no IRD/IKR loss on this target lineage; this is not a whole-family uniformity claim. Default Falcon research was attempted normally and failed HTTP403 authentication; no provider report was created or overwritten. Manual source/ontology/preservation evidence is in analysis/module_audits/bacterial_lps_transport/ecoli-consultation/.
