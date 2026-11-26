# GRE3 (YHR104W, P38715) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- NADPH-dependent aldose reductase, AKR superfamily, monomer [UniProt:P38715]. Native enzyme purified as cytosolic, NADPH-specific, broad aldehyde/aldose substrate range [PMID:7747971 "The aldo-keto reductase is NADPH specific and catalyzes the reduction of a variety of aldehydes"].
- Xylose reductase: recombinant enzyme reduces xylose, ~80x NADPH over NADH; Y49F kills >98% activity [PMID:11481678 "It prefers NADPH as the co-enzyme by about 80-fold over NADH"].
- Major xylose reductase in vivo: [PMID:12271459 "Gre3p is the major D-xylose-reducing enzyme in S. cerevisiae"]; gre3 extracts have no detectable XR activity. Also one of three arabinose reducers (with YPR1, YJR096W).
- Methylglyoxal reductase: [PMID:11525399 "in vitro and in vivo assays of yeast aldose reductase activity indicate that methylglyoxal is an endogenous substrate of aldose reductase"]; GRE3 overexpression complements glo1. UniProt suggests MG reduction is the more likely physiological role because S. cerevisiae grows poorly on xylose.
- Stress induction (osmotic, ionic, oxidative, heat; HOG, Msn2/4) [PMID:10407268 "transcripts accumulate not only in response to osmotic stress but also to ionic, oxidative and heat stress"].
- Galactose -> galactitol when overexpressed; suppresses lithium galactose toxicity [PMID:18811659 "cells overexpressing the aldose reductase GRE3, which converts galactose to galactitol"]. Judged over-annotated as galactose catabolism.
- Multiple AKR deletion -> oxidative stress markers [PMID:17919749].
- mRNA association on protein arrays [PMID:21124907].

Pathway context: xylose oxidoreductase pathway step 1 (D-xylose + NADPH -> xylitol), EC 1.1.1.21 / 1.1.1.431. Verified.
Curation: Rhea-derived "alcohol dehydrogenase (NAD+) activity" (RHEA:12785) marked over-annotated (NADPH-preferring enzyme).
Added NEW: methylglyoxal reductase (NADPH) activity (GO:0043892), IDA PMID:11525399.
