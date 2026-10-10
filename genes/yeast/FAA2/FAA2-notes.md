# FAA2 (YER015W; FAM1; UniProt P39518) notes

- Medium/long-chain acyl-CoA synthetase; C9-C13 preferred, C7-C17 tolerated [PMID:8206942 "C9:0-C13:0 are preferred and have equivalent activities, although C7:0-C17:0 fatty acids are tolerated"].
- Intraperoxisomal activation of medium-chain fatty acids [PMID:8670886 "Medium-chain fatty acids are activated inside peroxisomes hby the acyl-CoA synthetase Faa2p"]; peripheral, matrix side of peroxisomal membrane, PTS1 import [UniProt:P39518].
- Re-esterifies (V)LCFAs released by Pxa1p/Pxa2p [PMID:22493507 "The Pxa1p-Pxa2p complex functionally interacts with the acyl-CoA synthetases Faa2p and/or Fat1p on the inner surface of the peroxisomal membrane"].
- Overexpression rescues nmt1-181 by activating endogenous C14:0 [PMID:7962057 "Overexpression of Faa2p can rescue nmt1-181 cells due to activation of an endogenous pool of C14:0"].
- FAM1-1 suppressor gains a mitochondrial presequence; wild type lacks one [PMID:7988550]. Mitochondrial HDA hits likely peroxisome co-purification.

## Pathway-context observations
- FAA2 is the only Faa paralog acting inside peroxisomes; it is the true activation step of peroxisomal beta-oxidation (medium-chain directly, long/very-long-chain as re-esterification after Pxa1/2). EC 6.2.1.3 assignment is OK but its signature activity is medium-chain (GO:0031956).
- ER IBA (from ER-type ACSLs) does not fit this PTS1 peroxisomal enzyme; cytosol RCA removed.
- GO:0015916 fatty-acyl-CoA transport IGI (PMID:18757502) left UNDECIDED (abstract only; acyl-CoA transport is Pxa1/Pxa2's).
