# coq9 (O13850, SPAC19G12.11) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (function by similarity to human
COQ9 and S. cerevisiae Coq9) and the cached literature; PMID:24911838 and PMID:30661980
were read in full.

## Literature

- Deletion abolishes CoQ10 [PMID:24911838 "Overall, these data indicate that, like the
  S. pombe Δdps1, Δdlp1, Δppt1/coq2, Δcoq3, Δcoq7, and Δcoq8 strains described
  previously, the Δcoq4, Δcoq5, Δcoq6, and Δcoq9 strains are also unable to synthesize
  CoQ."]
- Human COQ9 does not complement [PMID:24911838 "Despite the inclusion of a mitochondrial
  targeting signal within its sequence, HsCOQ9 did not complement the S. pombe Δcoq9
  mutant (data not shown)."]
- Ortholog lipid binding [PMID:30661980 "We show that COQ9 repurposes the bacterial TetR
  fold to bind aromatic isoprenes with high specificity, including CoQ intermediates that
  likely reside entirely within the bilayer."]

## Audit decisions (2026-11)

- Actions unchanged (all ACCEPT); reasons and propagation routes added, truncated
  UniProt quotes completed, PMID:30661980 added as ortholog support.
- core_functions location set to the root mitochondrion: the inner-membrane row is IBA
  only and no S. pombe assay resolves the sub-compartment.
- Core function GO:0008289 agrees with the module annoton.
