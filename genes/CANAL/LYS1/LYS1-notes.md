# LYS1 (P43065) notes

- Direct Candida evidence: `LYS1` encodes the NAD(+), L-lysine-forming
  saccharopine dehydrogenase that catalyzes the final step of fungal
  alpha-aminoadipate L-lysine biosynthesis. Garrad and Bhattacharjee mapped the
  C. albicans STN57 and WD1-3-6 mutants to the saccharopine dehydrogenase step
  and showed that cloned Candida `LYS1` restored SDH activity in C. albicans and
  S. cerevisiae lys1 mutants [PMID:1429460 "two (STN57 and WD1-3-6) were blocked
  at the saccharopine dehydrogenase step"]. Garrad, Schmidt, and Bhattacharjee
  then localized and sequenced the gene and showed plasmid-borne Candida `LYS1`
  complementing a S. cerevisiae SDH mutant [PMID:7927784 "YpBRG2 has been shown
  to complement the"]. Guo, Garrad, and Bhattacharjee later assayed recombinant
  CaLys1p and used site-directed mutagenesis to find conserved residues required
  for activity [PMID:16292576 "amino acid substitutions as essential for C.
  albicans Lys1p SDH activity"].
- PAINT/paralog split: P43065 is in `PTHR11133:SF23`, with S. cerevisiae LYS1,
  S. pombe lys3, and Neurospora lys-4. That is the fungal NAD(+),
  L-lysine-forming branch. S. cerevisiae LYS9 and S. pombe lys9 are in the
  separate `PTHR11133:SF22` NADP(+), L-glutamate-forming branch. The fungal
  L-lysine biosynthesis process IBA to Candida LYS1 comes from
  `PANTHER:PTN000875292`, not the LYS9/lys9 `PTN000875327` node.
- Decision summary: the broad `GO:0004753 saccharopine dehydrogenase activity`
  IBA from the eukaryotic `PTN000123605` node is a specificity problem rather
  than a bad PAINT transfer, so MODIFY to `GO:0004754`. The exact IDA, IMP, IGI,
  ISS, IEA, and fungal-process IBA rows are all supported. CGD's root `ND`
  cellular-component row is just a no-data placeholder and should be removed.
  The broad PAINT/ARBA cytoplasm rows can stand; unlike budding-yeast Lys1,
  Candida LYS1 has no fetched direct peroxisome evidence or GOA peroxisome row.
- Newer-paper search: the 2016 Candida lysine-regulation paper showed that
  lysine deprivation induces `LYS1`, `LYS12`, and `LYS22` transcription
  [PMID:27303701 "the expression of LYS1, LYS12, and LYS22 was highly induced"].
  PMID:16733732 used `LYS1` and `LYS5` sequences as Candida diagnostic PCR
  targets; it confirms the sequence but does not add a new GO-relevant activity
  or process for Lys1.
- Deep research note: the default Falcon deep-research attempt failed because
  no research provider was configured (`agentapi` missing and no provider API
  keys available). I therefore used the cached Candida publications, UniProt,
  local PANTHER/PAINT tables, sibling fungal reviews, and targeted literature
  search instead of creating a generated `LYS1-deep-research-falcon.md`.
