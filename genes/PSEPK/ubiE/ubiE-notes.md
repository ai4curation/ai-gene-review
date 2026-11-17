# ubiE (PP_5011, Q88D17) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research (no provider keys); OpenScientist gene and pathway
reports read. Reviewed UniProt entry (HAMAP MF_01813). No KT2440 experiment.

- E. coli: [PMID:9045837 "provide evidence that it is required for the C methylation reactions
  in both ubiquinone and menaquinone biosynthesis."]
- KT2440 has no menaquinone pathway: project pathway report "not present in KT2440 (proteome
  searches for *menA* and *menD* return zero hits)". Hence menaquinone biosynthesis REMOVE (with
  a UniProt source defect for the unconditional HAMAP rule) and demethylmenaquinone
  methyltransferase activity MARK_AS_OVER_ANNOTATED (plausible capacity, no substrate).
- Aerobic respiration (UniRule) MARK_AS_OVER_ANNOTATED: product requirement, not participation.
- Ketone biosynthetic process (ARBA) and methyltransferase activity: MODIFY to GO:0006744 and
  GO:0008425 respectively.

Module agreement: `c_methyltransferase_activity` (GO:0008425). Consistent; the module note on
menaquinone methylation does not apply to KT2440.
