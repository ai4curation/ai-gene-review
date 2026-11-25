# paaK (P76085) notes — E. coli K-12 phenylacetate-CoA ligase

## Deep research
- 2026-10-23: `just deep-research-falcon ECOLI paaK` failed ("Exception: Failed to authenticate"; all providers failed).
  Perplexity/OpenAI keys not configured. No deep-research file; review is based on cached publications and UniProt.

## Function
- PaaK activates phenylacetate to phenylacetyl-CoA, the first (and committed) step of the aerobic paa "box" pathway.
  [PMID:9748275 "The paaK gene codes for a phenylacetyl-CoA ligase that catalyzes the activation of PA to phenylacetyl-CoA (PA-CoA)."]
- Teufel et al. 2010 used purified PaaK to make phenylacetyl-CoA for pathway reconstitution.
  [PMID:20660314 "enzymatically converted to phenylacetyl-CoA ( Fig. 1 B , compound II) using phenylacetate-CoA ligase (PaaK, the first enzyme of the pathway)"]
- Phenylacetyl-CoA (the PaaK product) is the inducer that relieves PaaX repression of the paa operon [PMID:9748275 "As PA-CoA is the true inducer"].
- UniProt: curated FUNCTION/CATALYTIC ACTIVITY with ECO:0000269 PubMed:9748275; ANL superfamily (Pfam PF00501 AMP-binding, PF14535), NCBIfam TIGR02155 PA_CoA_ligase, PANTHER PTHR43439.

## GOA review summary
- GO:0047475 (IBA, IEA, IMP, IEP) ACCEPT. The IEP evidence code on an MF is odd (expression pattern evidence does not
  support a catalytic activity); recorded as a probable source defect for EcoCyc (CHECK).
- GO:0016405 CoA-ligase activity (IMP) -> MODIFY to GO:0047475 (already present).
- GO:0010124 (IBA, IEA, IMP) ACCEPT.
