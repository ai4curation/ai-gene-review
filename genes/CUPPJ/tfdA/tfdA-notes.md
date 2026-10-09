# Notes: tfdA (2,4-D dioxygenase, Cupriavidus pinatubonensis JMP134)

Part of the category-4 counter-example set in
`projects/NONPHYSIOLOGICAL_REACTIONS.md`.

## Why this gene is in the set

2,4-dichlorophenoxyacetate is a synthetic herbicide from the 1940s, yet tfdA is
the committed entry step of a plasmid-borne catabolic pathway, located by
transposon mutagenesis of the degradation-negative phenotype and confirmed by
complementation
[PMID:3036764 "A 3-kilobase fragment of pJP4 cloned in a broad-host-range vector could complement the 2,4-D-negative phenotype of two mutants which lacked 2,4-D monooxygenase activity."].

Transferring tfdA alone to a cured derivative conferred growth on
phenoxyacetate as sole carbon and energy source
[PMID:3036764 "The recombinant strain could utilize phenoxyacetic acid as a sole source of carbon and energy."],
which also shows the chlorine substituents are not required for activity and
makes an unchlorinated aryloxyacetate a plausible ancestral substrate.

## Annotation finding: experimental evidence exists but is not annotated

The only MF annotation in GOA is a Rhea-derived IEA (GO_REF:0000116,
RHEA:48984, an exactMatch of GO:0018602). The term is correct. But the gene has
had Tn5 genetics, complementation and heterologous expression since 1987, plus
detailed mechanistic enzymology, none of it captured as IDA or IMP. The process
annotation GO:0046300 would merit IMP from the same work.

This is a curation gap, not an error, and it recurs across the set: SPHCR/pcpB
and XANAU/dhlA are in the same position. Consequence worth noting for the
project: the xenobiotic-degradation corner of GO looks electronically annotated
when it is actually among the better-characterized enzymology in the database.

GO:0016491 (root oxidoreductase, from IPR003819 which is the TfdA-family
signature itself) is redundant: MARK_AS_OVER_ANNOTATED.

## Other

Self-inactivating via oxidative hydroxylation of Trp-113 (UniProt PTM line,
ECO:0000269|PubMed:11457355). Not currently annotatable in GO in any obvious
way; raised as a question in the review.
