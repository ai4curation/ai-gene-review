# ERG12 notes

## 2026-10-24 Candida albicans review

- `just deep-research-falcon CANAL ERG12` was attempted before this manual review and failed
  because no provider API keys are configured; no provider deep-research file was created.
- Newer web searches did not identify a direct post-2024 Candida ERG12 biochemical paper. The
  recent Candida ergosterol literature mostly uses pathway diagrams or focuses on other Erg steps.
- UniProt A0A1D8PEL1 places Candida Erg12 in the reviewed PANTHER subfamily
  PTHR43290:SF2, `MEVALONATE KINASE`, and annotates the conserved reaction as
  `(R)-mevalonate + ATP = (R)-5-phosphomevalonate + ADP + H(+)`.
- PANTHER/PAINT has two relevant nodes: root `PTN000048555` for `GO:0004496`
  mevalonate kinase activity, `GO:0019287` IPP biosynthesis via mevalonate, and
  `GO:0005829` cytosol; and fungal node `PTN000825284` for `GO:0006696` ergosterol
  biosynthesis. The Candida ERG12 sequence is a PTHR43290:SF2 member, so the IBA rows
  are well placed.
- `PMID:14653518` is Candida-specific and supports sterol/prenylation pathway context:
  "Intermediates in the sterol pathway are involved in ergosterol synthesis, prenylation
  and dolichol synthesis." The cached abstract does not report a direct Candida Erg12
  enzyme assay.
- The direct enzymology and genetics in the cache are from S. cerevisiae. `PMID:1645230`
  reports "The nucleotide sequence of the ERG12 gene, encoding mevalonate kinase, from
  Saccharomyces cerevisiae is presented" and describes regulation in the sterol pathway.
  `PMID:16477420` used S. cerevisiae overexpressing mevalonate kinase to optimize a
  spectrophotometric assay and applied it to extracts with wild-type mevalonate kinase.
  `PMID:200835` classified ergosterol-auxotrophic yeast mutants and listed
  "mevalonic kinase (erg12)" among the deficient enzymatic activities.

## Curation decisions

- Accepted all three `GO:0004496` mevalonate kinase rows: the PAINT node, the combined
  InterPro/Rhea/EC IEA, and the ISS transfer from S. cerevisiae ERG12 are mutually
  consistent.
- Kept `GO:0005524` ATP binding as non-core because ATP is the phosphoryl donor of the
  kinase reaction, but substrate binding is subsidiary to the catalytic function.
- Added a non-core `NEW` `GO:0000287` magnesium ion binding row because Candida Erg12
  has UniProt Mg(2+) binding features transferred from the same rat mevalonate kinase
  donor that supports the sibling yeast and fission-yeast rows.
- Modified the broad cytoplasm IEA to `GO:0005829` cytosol. The cytoplasmic placement is
  true for Erg12, but GOA already carries the more specific cytosol annotations from PAINT
  and UniProtKB-SubCell.
- Accepted the cytosol PAINT and SubCell rows.
- Accepted the fungal-node `GO:0006696` ergosterol biosynthetic process IBA. Erg12 performs
  the first mevalonate-to-IPP step that supplies farnesyl diphosphate for fungal ergosterol
  synthesis.
- Kept the broad `GO:0008299` isoprenoid biosynthetic process row as non-core; it is true
  pathway context but less direct than `GO:0019287`.
- Accepted both `GO:0019287` IPP biosynthesis via mevalonate rows because mevalonate kinase
  directly performs step 1 of that process.
