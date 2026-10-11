# SIM1 notes

Deep research: the client reported a timeout after 600 s ("All providers failed"), so the
literature work was done manually with PubMed and the cached `publications/` files. The provider
finished afterwards and `SIM1-deep-research-falcon.md` is committed; it was checked against this
review on 2026-10-11.

- It agrees on the core annotation: a nuclear bHLH-PAS transcription factor acting mainly as a
  heterodimer with ARNT2 (and with ARNT in cell assays), preferring TACGTG-containing elements,
  required for PVN, supraoptic and anterior periventricular neuroendocrine development.
- It answers suggested question 1, which has been rewritten accordingly. Postnatal CNS deletion of
  Sim1 is by itself sufficient to cause hyperphagic obesity in mouse, dosage-dependently, with
  reduced hypothalamic Oxt and PVN Mc4r and without global PVN hypocellularity or loss of the
  examined projections [PMID:20220015]. The postnatal role is therefore separable from the
  developmental one; what remains open is the mechanism.
- It cautions on exactly the point question 2 asks about: reduced Oxt or Mc4r expression in a
  Sim1 mutant does not establish either as a directly bound SIM1 target, and Brn2 was not induced
  in the cell-line screen that found 268 candidate SIM1/ARNT2-responsive transcripts. The complete
  set of directly occupied human hypothalamic targets is unresolved.
- On the p.R171H variant, a 2026 biochemical study found impaired DNA-responsive reporter activity
  with preserved ARNT/ARNT2 association, and purified wild-type and R171H complexes were not
  distinguishable by its mobility-shift assays, so the defect is narrower than loss of all
  intrinsic DNA binding.

## Function
- bHLH-PAS TF requiring ARNT/ARNT2 [PMID:23778136 "One of the aryl hydrocarbon receptor nuclear translocators, either ARNT or ARNT2, is required as a dimerization partner for SIM1 to function as a transcription factor, with mouse knockout studies suggesting that ARNT2 is the in vivo partner in the hypothalamus"]; [PMID:10640708 "we provide evidence that Sim1 and Arnt2 form dimers in vitro"].
- PVN/SON development: [PMID:9784500 "we show that SIM1 controls the development of these secretory neurons at the final stages of their differentiation"].
- Obesity: [PMID:11448938 "Sim1 heterozygous mice are viable but develop early-onset obesity, with increased linear growth, hyperinsulinemia and hyperleptinemia"]; human translocation [PMID:10587584 "it disrupts the SIM1 gene on 6q"]; human LoF variants [PMID:23778136]; melanocortin link [PMID:16728530 "Our results demonstrate that Sim1 heterozygotes are resistant to hypothalamic melanocortin signaling"].

## Annotation notes
- Ureteric bud development (IEA from mouse) left UNDECIDED: expression in developing kidney is documented (PMID:8812055) but the functional source was not reviewed.
- HuRI ARNT2 protein-binding row modified to protein heterodimerization activity.
- NEW hypothalamus cell differentiation (GO:0021979), mouse IMP.
- No AIGR module covers hypothalamic development; SIM1 is not a part of `leptin_melanocortin_signaling` (it is a developmental TF, not a signalling step). Feeding behaviour was not annotated: SIM1 is required for the neurons, not shown to perform the behavioural step.
