# A0A3B6NKR6 (wheat glucuronokinase-family protein) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted.

Identity: A0A3B6NKR6 = TraesCS6A02G071400.1 (chr 6A), 360 aa, TrEMBL PE4. It is full length
relative to Arabidopsis GLCAK1 (Q93ZC9, 362 aa) and GLCAK2 (Q9LY82, 366 aa), with both Pfam GHMP
domains and the GLSGSSA phosphate-binding loop. It is not a fragment or isoform. It is one
homeolog of a wheat glucuronokinase gene (the 6B/6D homeologs were not reviewed here).

Evolutionary grounding (file:WHEAT/A0A3B6NKR6/A0A3B6NKR6-bioinformatics/RESULTS-rereview.md):
- PANTHER PTHR38710:SF1 (single subfamily), shared with GLCAK1 and GLCAK2.
- PANTHER 19 tree: within Viridiplantae, grasses (Zea) and eudicots differ by speciation only,
  so the wheat protein is an ortholog. GLCAK1/GLCAK2 (81.5% identity) are an eudicot-lineage
  paralog pair; wheat is about 65% identical to each.
- PAINT: a glucuronokinase-activity IBD sits at PTN008680403 (seed AT3G01640, 2026). The cytosol
  IBA comes from PTN000048555, a node seeded by mevalonate kinases (Mvk/ERG12) that is absent from
  the PTHR38710 tree. The same node carries mevalonate kinase activity and GO:0019287. PAINT did not
  propagate the mevalonate kinase activity term to this family; only cytosol reached it.

Literature: Pieslinger et al. 2010 [PMID:19951951 "AtGlcAK is a novel plant sugar kinase able to
phosphorylate d-GlcA to d-GlcA-1-phosphate in the presence of ATP."], which also reports strict
D-GlcA specificity and a cytosolic prediction. Shrestha et al. 2022 [PMID:36464707] reports YFP-GLCAK2
at the PM/ER/tonoplast and an AHL-priming role. That paper is paralog-specific and not transferred.
The falcon deep-research file does not cite the primary paper and is kept only as background.

Changes from the previous version:
- GO:0019287 mevalonate pathway: MARK_AS_OVER_ANNOTATED changed to REMOVE. It is a wrong
  UniPathway/superfamily mapping; the enzyme is a GlcA-specific sugar-1-kinase.
- GO:0005829 cytosol: ACCEPT kept, now supported by the primary paper. The mevalonate-kinase
  donor node is noted.
- GO:0005524 ATP binding: KEEP_AS_NON_CORE kept.
- NEW GO:0047940 and GO:0006065: evidence changed from IEA without a reference to ISS from
  PMID:19951951, now grounded by subfamily orthology. GO:0006065 passes the participation test
  because the enzyme catalyses a pathway step. Comparator: UGD2/UGD4 carry GO:0006065 by IDA.
- Description rewritten. Grass type II cell-wall speculation removed.

Relative to review next: Arabidopsis GLCAK1 (Q93ZC9, At3g01640), the biochemically characterised
ortholog in the same subfamily. There is no review in genes/ARATH.
