# ASPFU mcr1 notes

## 2026-10-24

- Seeded Q4WJW8 with `just fetch-gene ASPFU mcr1`; GOA contains three PAINT
  rows from PTHR19370 and three UniProt/ARBA/InterPro IEA rows, but no direct
  A. fumigatus PMID annotations.
- `just deep-research-falcon ASPFU mcr1 --fallback perplexity-lite` failed
  because no research provider credentials were available in this shell, so
  this review used the cached UniProt/GOA/PAINT records, targeted web/PubMed
  searches, and cached primary literature for the S. cerevisiae MCR1 source
  annotations.
- PTHR19370 separates A. fumigatus mcr1 (Q4WJW8) into the
  MCR1/NADH-cytochrome b5 reductase 2 subfamily `PTHR19370:SF171`, while A.
  fumigatus cbr1 (Q4X0B5) is in the CBR1-like `PTHR19370:SF184` branch.
- `PTN000452207` carries the MCR1 mitochondrial localization and broad
  NAD(P)H-dependent cytochrome-b5 reductase molecular-function assertions. The
  molecular-function row is seeded by S. cerevisiae MCR1 and PGA3 at a broad
  eukaryotic node, so the broad term is retained as a deliberate node-level
  assertion rather than refined on the PAINT row; the separate Rhea/EC mapping
  captures the NADH-specific child `GO:0090524`.
- `PTN000452208` carries `GO:0006696 ergosterol biosynthetic process` from an
  S. cerevisiae MCR1 source. PMID:10622712 reconstituted Candida CYP51 sterol
  14alpha-demethylation with a yeast microsomal cytochrome b5/NADH-cytochrome
  b5 reductase chain, which supports the CBR1 branch rather than directly
  establishing an ER ergosterol role for mitochondrial MCR1.
- Manual searches for direct A. fumigatus mcr1 work by `AFUA_1G04540`,
  `Q4WJW8`, and A. fumigatus NADH-cytochrome-b5-reductase queries did not find
  primary evidence that changes the PAINT-backed MCR1-clade assessment; the
  newer hits were database, reagent, expression, or genome-scale proteome
  records rather than mcr1 functional characterization.
