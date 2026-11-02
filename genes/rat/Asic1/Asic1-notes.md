# Asic1 (rat) review notes

## Session 1 (2026-10-28)

- fetch-gene resolved P55926 (ASIC1_RAT, RGD:71062, GeneID 79123); 61 GOA rows.
- No deep-research API; literature synthesis in `Asic1-deep-research-manual.md`.
- Core function: pH-gated, Na+-selective cation channel (GO:0160125) at the plasma /
  postsynaptic membrane [PMID:9062189 "Heterologous expression of ASIC induces an
  amiloride-sensitive cation (Na+ > Ca2+ > K+) channel which is transiently activated by
  rapid extracellular acidification."]. The many generic channel/transport MF and BP rows
  are MODIFIED to GO:0160125 / GO:0035725.
- The ISO NOT|enables GO:0160128 row (With UniProtKB:P78348-1) was propagated from a
  primate-only, non-functional human isoform [PMID:21036899 "Human ACCN2 transcript variant
  1 (hVariant 1) is not present in rodents"]; REMOVED and recorded as a source defect for
  RGD.
- Behavioural rows (fear, memory, associative learning) kept as non-core; response to
  amphetamine, negative regulation of neurotransmitter secretion and sour taste marked
  over-annotated (indirect phenotypes or correlative expression).
- PMID:19074149 (full text read): rat ASIC1a Tyr72/Trp288 mutants lose proton-gated
  current but reach the surface (biotinylation) - supports the cell surface IDA and the
  IMP transport row.
- Curation gap (not a knowledge gap): no rat row for dendritic spine; mouse evidence
  [PMID:17060608] supports it but no NEW row added (location is non-core here).
