# CANAL MCR1 notes

## 2026-10-10

- Seeded Q59M70 with `just fetch-gene CANAL MCR1`; GOA contains three PAINT
  rows from PTHR19370, two UniProt/InterPro IEA rows, and two CGD `ND` root
  placeholders, but no direct Candida PMID annotations.
- Falcon deep research failed because no research provider credentials were
  available in this shell, so this review used the cached UniProt/GOA/PAINT
  records, targeted web/PubMed searches, and newly cached primary literature
  for the S. cerevisiae MCR1 source annotations.
- PTHR19370 separates C. albicans MCR1 (Q59M70) into the
  MCR1/NADH-cytochrome b5 reductase 2 subfamily `PTHR19370:SF171`, while
  C. albicans CBR1 (Q59P03) is in the CBR1-like `PTHR19370:SF184` branch.
- `PTN000452207` carries the MCR1 mitochondrial localization and broad
  NAD(P)H-dependent cytochrome-b5 reductase molecular-function assertions.
  The molecular-function row is seeded by S. cerevisiae MCR1 and PGA3 at a
  broad eukaryotic node, so the broad term is retained as a deliberate
  node-level assertion rather than refined on the PAINT row; the separate
  Rhea/EC mapping captures the NADH-specific child `GO:0090524`.
- `PTN000452208` carries `GO:0006696 ergosterol biosynthetic process` from an
  S. cerevisiae MCR1 source. PMID:10622712 reconstituted Candida CYP51 sterol
  14alpha-demethylation with a yeast microsomal cytochrome b5/NADH-cytochrome
  b5 reductase chain, which supports the CBR1 branch rather than directly
  establishing an ER ergosterol role for mitochondrial MCR1.
- Searches for newer direct C. albicans MCR1 work by `Q59M70`, `MCR1`, and
  "Candida albicans cytochrome b5 reductase" did not find primary evidence
  that changes the core mitochondrial reductase assessment; the newer hits were
  expression/proteome or product-catalog records rather than MCR1 functional
  characterization.
