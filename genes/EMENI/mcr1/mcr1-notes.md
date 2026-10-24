# EMENI mcr1 notes

## 2026-10-24

- Seeded Q5BG98 with `just fetch-gene EMENI mcr1`; GOA contains three
  PAINT rows from PTHR19370 and three UniProt/ARBA/InterPro IEA rows, but no
  direct A. nidulans PMID annotations.
- `just fetch-gene-pmids EMENI mcr1` found no PMID-backed GOA rows.
- `just deep-research-falcon EMENI mcr1 --fallback perplexity-lite` failed
  because no research provider credentials were available in this shell, so
  this review used the cached UniProt/GOA/PAINT records, targeted web/PubMed
  searches, and cached primary literature for the S. cerevisiae MCR1 source
  annotations.
- PTHR19370 places A. nidulans mcr1 (Q5BG98/AN0432) in the
  MCR1/NADH-cytochrome b5 reductase 2 subfamily `PTHR19370:SF171`, the same
  branch as A. fumigatus mcr1 and S. cerevisiae MCR1.
- `PTN000452207` carries the MCR1 mitochondrial localization and broad
  NAD(P)H-dependent cytochrome-b5 reductase molecular-function assertions. The
  molecular-function row is seeded by S. cerevisiae MCR1 (`SGD:S000001633`)
  and PGA3 (`SGD:S000004594`, UniProt Q12746) at a broad eukaryotic node, so
  the IBA supports only the broad parent for A. nidulans mcr1; the separate
  Rhea/EC mapping captures the NADH-specific child `GO:0090524`.
- `PTN000452208` carries `GO:0006696 ergosterol biosynthetic process` from an
  S. cerevisiae MCR1 source. PMID:10622712 reconstituted Candida CYP51 sterol
  14alpha-demethylation with a yeast microsomal cytochrome b5/NADH-cytochrome
  b5 reductase chain, which supports the CBR1 branch rather than directly
  establishing an ER ergosterol role for mitochondrial MCR1.
- Manual searches for direct A. nidulans mcr1 work by `AN0432`, `ANIA_00432`,
  `Q5BG98`, and A. nidulans NADH-cytochrome-b5-reductase queries did not find
  primary evidence that changes the PAINT-backed MCR1-clade assessment. A 2025
  AtfA oxidative-stress transcriptomics paper mentions mcr1 as a mitochondrial
  NADH-cytochrome b5 reductase in a regulated-gene list, but is not direct
  functional evidence for the protein.
