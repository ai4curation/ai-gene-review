# fyu1 (SPCC1322.04; UniProt P78811) notes

## Experimental (S. pombe)
- Buchheit et al. 2011 (abstract-only): [PMID:21862693 "we could enhance the glucoside production rate in fission yeast by overexpressing the fission yeast gene SPCC1322.04, a potential UDP-glucose pyrophosphorylase (UGPase), but not by overexpression of SPCC794.10, and therefore suggest to name this gene fyu1 for fission yeast UGPase1"]. PomBase coded this IMP for GO:0003983 and GO:0006011; it is an overexpression readout. Deferred to curator.
- [UniProt:P78811 "Reaction=alpha-D-glucose 1-phosphate + UTP + H(+) = UDP-alpha-D-glucose"]; [UniProt:P78811 "SIMILARITY: Belongs to the UDPGP type 1 family."].
- Location cytoplasm + nucleus from GFP screen [UniProt:P78811 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}. Nucleus"].
- Paralog SPCC794.10 (appears as IBA donor for cytoplasm) did not raise glucoside production.
- Ortholog UGP1: [PMID:7588797 "encodes UDP-glucose pyrophosphorylase (UGPase), the enzyme which catalyses the reversible formation of UDP-Glc from glucose 1-phosphate and UTP"].

## GO-CAM
- Not in any cached PomBase GO-CAM.

## Decisions
- MF and UDP-glucose metabolic rows accepted; core BP GO:0120530 (as for UGP1 review), not yet in GOA.
- Glycogen metabolic process IBA kept non-core; S. pombe glycogen metabolism is poorly characterized (a web search did not establish whether S. pombe makes glycogen), so not removed.
- Nucleus (HDA, IEA) and uridylyltransferase activity kept non-core.
