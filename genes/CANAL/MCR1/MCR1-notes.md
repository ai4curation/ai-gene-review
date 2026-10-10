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
  These are sound for Candida MCR1, but the molecular-function term should be
  refined to the Rhea/EC-backed NADH-specific child `GO:0090524`.
- `PTN000452208` carries `GO:0006696 ergosterol biosynthetic process` from an
  S. cerevisiae MCR1 source. PMID:10622712 reconstituted Candida CYP51 sterol
  14alpha-demethylation with purified yeast cytochrome b5 and NADH-cytochrome
  b5 reductase, so it supports the biochemical possibility of a direct electron
  transfer step.
- Searches for newer direct C. albicans MCR1 work by `Q59M70`, `MCR1`, and
  "Candida albicans cytochrome b5 reductase" did not find primary evidence
  that changes the core mitochondrial reductase assessment; the newer hits were
  expression/proteome or product-catalog records rather than MCR1 functional
  characterization.
