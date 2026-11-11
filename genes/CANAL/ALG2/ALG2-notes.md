# ALG2 PTHR45918 review notes

PTHR45918 is a coherent ALG2 family with a single reviewed subfamily,
PTHR45918:SF1. Candida albicans Q59LF2 is in that subfamily, and PAINT places
three IBD assertions at PTN000282458 for the eukaryotic ALG2 clade:
GO:0012505 endomembrane system, GO:0000033 alpha-1,3-mannosyltransferase
activity, and GO:0006488 dolichol-linked oligosaccharide biosynthetic process.

The alpha-1,3 IBA is biologically sound but parent-level; the better term is
GO:0004378, which names the GDP-Man + Man1GlcNAc2-PP-Dol reaction used by ALG2.
The endomembrane-system IBA is likewise a sound but broad localization and
should be refined to GO:0005789 endoplasmic reticulum membrane. The LLO process
IBA is correctly scoped and is the core biological process.

UniProt transfers both ALG2 catalytic reactions from S. cerevisiae P43636:
EC 2.4.1.132/RHEA:29515 for the alpha-1,3 step and
EC 2.4.1.257/RHEA:29519 for the alpha-1,6 step. Those two rows plus the ISS
copies from yeast are accepted as the two core molecular functions. The
EnsemblFungi GO:0033164 row traces to the same yeast biology but should be
modified to GO:0102704 because GO:0033164 describes the Och1-type outer-chain
initiation activity rather than the Alg2 Man2GlcNAc2-PP-Dol reaction.

Targeted PubMed searches on 2026-11-06 for ALG2 plus Candida albicans, the
SC5314 locus identifiers CAALFM_C604030WA, CaO19.1221 and CaO19.8808 did not
find a direct Candida ALG2 biochemical or localization paper. The two hits were
about Candida Pef1/membrane perturbation biology or Candida histidine kinases and
cell-wall mannan regulation, not this ALG2 mannosyltransferase.

Falcon deep research failed locally because the `agentapi` executable was not
available to `deep-research-client`; no `ALG2-deep-research-falcon.md` file was
created.
