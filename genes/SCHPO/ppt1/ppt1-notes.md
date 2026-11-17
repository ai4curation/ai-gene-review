# ppt1 / coq2 (Q10252, SPAC56F8.04c) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record and the cached literature;
PMID:11092853 and PMID:24911838 were read in full.

## Literature

- Disruption and complementation [PMID:11092853 "When we extracted ubiquinone from each
  strain, UQ-10 was detected in the wild-type strain, in NU609 harboring pREP1-PPT1, and
  in NU609 harboring pREP1-COQ2, but not in NU609 alone"]
- Mitochondrial localisation [PMID:11092853 "Ppt1-green fluorescent protein fusion
  proteins localized to the mitochondria, indicating that ubiquinone biosynthesis occurs
  in the mitochondria in S. pombe."] The paper does not fractionate sub-compartments.
- Human COQ2 complements [PMID:24911838 "All of the HsCOQ2 constructs restored the growth
  of the S. pombe Δppt1 strain (data not shown) and recovered its defective production of
  CoQ10 (Figure 5B)."]
- Overexpression raises UQ [PMID:17069919 "The yeast MTppt1 and ERppt1 transgenic lines
  showed about 3.7 and 5.1 times increment in UQ content"]

## Audit decisions (2026-11)

- GO:0016020 membrane changed from TOO_GENERAL to MODIFY -> GO:0005743, matching the
  S. cerevisiae and human COQ2 reviews.
- GO:0005743 IDA (PomBase, PMID:11092853) accepted: the paper shows mitochondria only,
  but the inner-membrane claim holds on topology (multi-pass, transit peptide) plus the
  mitochondrial GFP result and the yeast Coq2 EXP evidence; not overruled.
- Core function GO:0008412 agrees with the module's Coq2/UbiA annoton.
