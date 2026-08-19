# PP_3254 curation notes

## 2026-08-13 purine-salvage boundary review

The species-aware module report nominated PP_3254 because PF01048 is broadly
named a nucleoside phosphorylase domain. The exact family evidence resolves the
ambiguity: Q88HU9 is PTHR46832:SF1, the 5'-methylthioadenosine/
S-adenosylhomocysteine nucleosidase lineage, and its GOA carries the two
corresponding hydrolytic molecular functions.

PP_3254 is therefore excluded from the PpnP-linked purine salvage module. An
MtnN nucleosidase uses water to cleave modified adenosine metabolites; it does
not provide the phosphate-dependent purine-ribonucleoside-to-base reaction
needed for the module's first step. Direct Q88HU9 enzymology is still absent.

## 2026-08-19 OpenScientist follow-up

The completed OpenScientist report retrieves the same PTHR46832:SF1 and
MTA/SAH nucleosidase assignment
[file:PSEPK/PP_3254/PP_3254-deep-research-openscientist.md "PANTHER
classifies it as subfamily **PTHR46832:SF1**"]. It also incorrectly identifies
the KT2440 adenine phosphoribosyltransferase as PP_0746; the local reviewed
UniProt record identifies `apt` as PP_4266
[file:PSEPK/apt/apt-uniprot.txt "OrderedLocusNames=PP_4266"]. Its downstream
pathway-absence and flux claims were therefore not imported into the review.
