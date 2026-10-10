# NEUCR mcr-1 notes

## 2026-10-10

- Seeded Q7SFY2 with `just fetch-gene NEUCR mcr-1`; GOA contains three PAINT
  rows from PTHR19370 and three UniProt/InterPro IEA rows, but no direct
  Neurospora PMID annotations.
- Falcon deep research failed because no research provider credentials were
  available in this shell, so this review used the cached UniProt/GOA/PAINT
  records, targeted web/PubMed searches, and cached primary literature for the
  S. cerevisiae MCR1 source annotations.
- PTHR19370 separates N. crassa mcr-1 (Q7SFY2) into the
  MCR1/NADH-cytochrome b5 reductase 2 subfamily `PTHR19370:SF171`, while
  N. crassa cbr1 (Q7RXL1) is in the CBR1-like `PTHR19370:SF184` branch.
- `PTN000452207` carries the MCR1 mitochondrial localization and broad
  NAD(P)H-dependent cytochrome-b5 reductase molecular-function assertions.
  These are sound for N. crassa mcr-1, but the molecular-function term should
  be refined to the Rhea/EC-backed NADH-specific child `GO:0090524`.
- `PTN000452208` carries `GO:0006696 ergosterol biosynthetic process` from an
  S. cerevisiae MCR1 source. PMID:10622712 reconstituted Candida CYP51 sterol
  14alpha-demethylation with purified yeast cytochrome b5 and NADH-cytochrome
  b5 reductase, so it supports the biochemical possibility of a direct electron
  transfer step.
- Searches for newer direct N. crassa mcr-1 work by `Q7SFY2`, `mcr-1`,
  `NCU03112`, and "Neurospora crassa NADH-cytochrome b5 reductase 2" did not
  find primary evidence that changes the PAINT-backed MCR1-clade assessment.
