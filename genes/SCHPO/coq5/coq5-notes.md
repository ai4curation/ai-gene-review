# coq5 (P87230, SPCC4G3.04c) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (HAMAP MF_03191, function by
similarity to human COQ5) and the cached literature; PMID:24911838 was read in full.

## Literature

- Deletion abolishes CoQ10 and accumulates intermediates rescued by coq5
  [PMID:24911838 "When the S. pombe coq5 gene was expressed in the Δcoq5 strain, the
  intermediate peaks disappeared and a CoQ10 peak was observed on the HPLC trace
  (Figure 7B)."]
- Arabidopsis COQ5 complements [PMID:24911838 "Expression of AtCOQ3, AtCOQ4 and AtCOQ5
  recovered CoQ10 production by the S. pombe Δcoq3, Δcoq4 and Δcoq5 strains,
  respectively (Figures 9A–C)."]; human COQ5 only weakly.
- No S. pombe enzymology.

## Audit decisions (2026-11)

- Actions retained; reasons added for HDA/IDA/EXP/IMP rows and propagation routes named.
- GO:0008168 and GO:0042181 kept TOO_GENERAL (specific descendants GO:0008425 and
  GO:0006744 asserted); the S. cerevisiae COQ5 review uses MODIFY for the same rows, the
  human COQ5 review TOO_GENERAL for GO:0008168. Either is policy-compliant.
- Core function GO:0008425 agrees with the module annoton.
