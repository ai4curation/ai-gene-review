# alg-2 PTHR45918 review notes

PTHR45918 is a coherent ALG2 family with a single reviewed subfamily,
PTHR45918:SF1. Neurospora crassa Q8X0H8 is in that subfamily, and PAINT places
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
copies from yeast are accepted as the two core molecular functions.

Targeted PubMed searches on 2026-11-06 for alg-2 plus Neurospora crassa and the
ORF identifiers B12N19.090 and NCU03503 did not find a direct Neurospora alg-2
biochemical or localization paper. The single hit came from an Arabidopsis
ARGONAUTE paper and is a gene-name false positive.

Falcon deep research failed locally because the `agentapi` executable was not
available to `deep-research-client`; no `alg-2-deep-research-falcon.md` file was
created.
