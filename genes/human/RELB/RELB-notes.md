# RELB review notes

## PTHR24169 context

RELB is the human `PTHR24169:SF18` RelB subfamily member. In this branch it is
reviewed with the missing NFKB1, NFKB2 and REL reviews while the complete RELA
review on `main` acts as the family comparator.

## Evidence synthesis

RelB is a Rel-homology-domain NF-kappaB subunit that preferentially works with
NFKB2 p52 in the noncanonical pathway. Reactome describes p100:RELB as a
cytosolic complex that is processed to p52:RELB and then translocated into the
nucleus to stimulate noncanonical NF-kappaB target-gene expression
[Reactome:R-HSA-5607720; Reactome:R-HSA-5607741].

The GOA rows for chromatin, kappaB cis-regulatory DNA binding, noncanonical
NF-kappaB signaling and positive regulation of RNA polymerase II transcription
are core. The RelB-deficiency lymphocyte row was kept as a non-core immune
development phenotype because the cited human deficiency report established
that RelB is required for T- and B-lymphocyte maturation and function
[PMID:26385063]. The TLR3/IFN-beta repression rows were also kept as a direct
but stimulus-specific RelB/c-Rel regulatory context [PMID:22065573, "RelB and
cRel negatively regulate Toll-like receptor 3-mediated"].

The NEK6 centrosome rows were kept as peripheral interaction/localization
evidence. The synapse and osmotic-stress IEA rows were treated as
over-annotations because their supporting transfers do not identify a direct
RelB activity outside the NF-kappaB transcription-factor cycle.

RelB also has experimentally curated repressor contexts, including HMGB1/H1
assembly of a RelB repressor complex at the TNF-alpha promoter during endotoxin
tolerance and CLOCK-BMAL1 repression enhanced by NFKB2/p52. Those rows were kept
as non-core because the central conserved RelB role is as a p52/p50 NF-kappaB
heterodimer subunit in noncanonical NF-kappaB transcriptional activation.

## Automated research

`just deep-research human RELB --provider perplexity` was not rerun after the
NFKB1 provider check failed with only `claude_code` available. No
`RELB-deep-research-perplexity.md` artifact was created or filled manually.
