# SIM1 notes

Deep research (`just deep-research-falcon human SIM1`) timed out after 600 s ("All providers failed"),
so the literature work was done manually with PubMed and the cached `publications/` files.

## Function
- bHLH-PAS TF requiring ARNT/ARNT2 [PMID:23778136 "One of the aryl hydrocarbon receptor nuclear translocators, either ARNT or ARNT2, is required as a dimerization partner for SIM1 to function as a transcription factor, with mouse knockout studies suggesting that ARNT2 is the in vivo partner in the hypothalamus"]; [PMID:10640708 "we provide evidence that Sim1 and Arnt2 form dimers in vitro"].
- PVN/SON development: [PMID:9784500 "we show that SIM1 controls the development of these secretory neurons at the final stages of their differentiation"].
- Obesity: [PMID:11448938 "Sim1 heterozygous mice are viable but develop early-onset obesity, with increased linear growth, hyperinsulinemia and hyperleptinemia"]; human translocation [PMID:10587584 "it disrupts the SIM1 gene on 6q"]; human LoF variants [PMID:23778136]; melanocortin link [PMID:16728530 "Our results demonstrate that Sim1 heterozygotes are resistant to hypothalamic melanocortin signaling"].

## Annotation notes
- Ureteric bud development (IEA from mouse) left UNDECIDED: expression in developing kidney is documented (PMID:8812055) but the functional source was not reviewed.
- HuRI ARNT2 protein-binding row modified to protein heterodimerization activity.
- NEW hypothalamus cell differentiation (GO:0021979), mouse IMP.
- No AIGR module covers hypothalamic development; SIM1 is not a part of `leptin_melanocortin_signaling` (it is a developmental TF, not a signalling step). Feeding behaviour was not annotated: SIM1 is required for the neurons, not shown to perform the behavioural step.
