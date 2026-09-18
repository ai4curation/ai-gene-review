# MTCH2 (Q9Y6C9) curation notes

## 2026-09-04 — Finishing pass on ai-review.yaml (PAINT no-IBA project)

Completed the review pass over all 22 existing_annotations entries; status
moved INITIALIZED → COMPLETE (validation clean, no warnings).

Key points and changes:

- Core function is settled: MTCH2 is the mitochondrial outer membrane protein
  insertase for alpha-helical substrates
  [PMID:36264797 "Cumulatively, the requirement for MTCH2 in vivo and in vitro
  for TA insertion, together with its reconstituted insertase activity and
  physical association with substrates, rigorously establishes MTCH2 as an
  insertase for α-helical mitochondrial outer membrane proteins."]. The three
  IDA annotations from that paper (GO:0032977 membrane insertase activity,
  GO:0045040 protein insertion into mitochondrial outer membrane, GO:0005741
  mitochondrial outer membrane) are ACCEPTed as core. Apoptosis (tBID
  receptor), mitochondrial fusion, lipid homeostasis, and stem cell
  differentiation annotations are all kept as non-core — mouse-derived,
  plausibly downstream of the insertase function (fusion machinery and
  apoptotic effectors themselves require OMM insertion).
- Added structured `propagation_review` blocks to the two generic IBA CC
  annotations (GO:0005739 mitochondrion, GO:0016020 membrane): root cause
  TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH. The IBA sources (mouse Mtch2
  MGI:1929260, human MTCH1 Q9NZJ7, and MTCH2 itself) are all sound; the terms
  are simply parents of the experimentally demonstrated GO:0005741.
- Changed the two bare protein-binding (GO:0005515) IPI rows from REMOVE to
  MARK_AS_OVER_ANNOTATED, matching project convention: the interactions were
  experimentally detected (HuRI Y2H partners APOC1/P02654 and ATP5MJ isoform
  P56378-2 [PMID:32296183]; TOM-interactome partner MUL1/Q969V5
  [PMID:40105103], which UniProt records in SUBUNIT: "Interacts with MUL1/MAPL
  (PubMed:40105103)"), so the rows are not wrong, just uninformative. No
  informative MF replacement is currently supportable for either.
- Kept REMOVE for GO:0005634 nucleus (HDA, sperm nucleus proteomics
  PMID:21630459): a high-throughput proteomics contaminant call; MTCH2 is a
  multi-pass OMM protein with no nuclear evidence, and sperm midpiece
  mitochondria are a classic contamination source in sperm-head preparations.
- Family note (PTHR10780): MTCH1/MTCH2 sit in the SLC25 mitochondrial-carrier
  fold family but have diverged from metabolite transport to insertase
  function — a caution for any family-level transport/carrier propagation. See
  interpro/panther/PTHR10780/PTHR10780-review.yaml.
