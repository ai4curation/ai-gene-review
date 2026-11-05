# Bhmt (rat) review notes

- 2026-10-28: Created review. fetch-gene resolved O09171 (BHMT1_RAT, RGD:621496, GeneID 81508) as
  expected; 30 GOA rows.
- Literature: see `Bhmt-deep-research-manual.md` (no provider keys; manual synthesis).
- Core function: betaine-homocysteine S-methyltransferase activity (GO:0047150), zinc-dependent,
  homotetramer; in cytosol (and a minor nuclear pool) [PMID:28288879 "Nuclear BHMT is an active
  homotetramer in normal liver"]. Processes: L-methionine salvage (homocysteine remethylation) and
  amino-acid betaine catabolic process.
- methyltransferase activity rows -> MODIFY to GO:0047150.
- GO:0006577 amino-acid betaine metabolic process -> MODIFY to child GO:0006579 (checked with OAK:
  GO:0006579 is_a GO:0006577).
- GO:0071265 L-methionine biosynthetic process -> MODIFY to GO:0071267 L-methionine salvage (OAK:
  GO:0071267 is_a GO:0071265).
- NOT S-adenosylmethionine metabolic process (ISO from human, BHF-UCL IDA PMID:18230605): derived from
  "S-adenosylmethionine does not inhibit BHMT" [PMID:18230605]. Absence of inhibition is a regulation
  statement, not a participation statement; but BHMT indeed does not use or make SAM, so the negation is
  defensible. Kept as non-core.
- PMID:17669278 complex/complex-binding rows: abstract only, co-purification on an affinity resin;
  over-annotated.
- PMID:15845641 IDA rows: abstract does not mention BHMT; full text not available. Activity is established
  independently for rat Bhmt (PMID:12487625, PMID:28288879), so methyltransferase row MODIFY and BHMT
  activity row ACCEPT deferring to curator.
- extracellular region (serum proteomics, PMID:23083309) and extracellular exosome (ISO from human) are
  leakage/proteomic captures of a cytosolic enzyme -> over-annotated.
