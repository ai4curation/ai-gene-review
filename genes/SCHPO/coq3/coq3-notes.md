# coq3 (O74421, SPCC162.05) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (HAMAP MF_03190) and the cached
literature; PMID:24911838 was read in full.

## Literature

- Deletion abolishes CoQ10 [PMID:24911838 "Here, we expand these findings by identifying
  ten genes (dps1, dlp1, ppt1, and coq3-9) that are required for CoQ synthesis."]
- Human COQ3 needs a mitochondrial targeting sequence to complement [PMID:24911838
  "Targeting of HsCOQ3 and HsCOQ7 to the mitochondria successfully recovered defective
  CoQ10 production by the S. pombe Δcoq3 (Figure 6C) and Δcoq7 (Figure 7A) strains."]
- Arabidopsis COQ3 complements [PMID:24911838 "Expression of AtCOQ3, AtCOQ4 and AtCOQ5
  recovered CoQ10 production by the S. pombe Δcoq3, Δcoq4 and Δcoq5 strains,
  respectively (Figures 9A–C)."]
- Mitochondrial GFP localisation [PMID:24911838 "The Dps1, Ppt1/Coq2, Coq3, Coq4, Coq5,
  Coq6, Coq7, Coq8, and Coq9 GFP fusion proteins also localized to the mitochondria"]
- No S. pombe enzymology: both O-methyltransferase activities rest on HAMAP MF_03190 and
  cross-species complementation.

## Audit decisions (2026-11)

- GO:0120537 (quinone form of the final methylation) changed from KEEP_AS_NON_CORE to
  ACCEPT, matching the S. cerevisiae COQ3 review where both redox-form terms are
  accepted.
- core_functions split into two entries (GO:0010420 and GO:0061542), matching the two
  module annotons that use coq3.
- Inner-membrane EXP (PomBase) accepted: the paper shows only whole-mitochondrion GFP,
  but the claim agrees with yeast Coq3 IDA evidence.
