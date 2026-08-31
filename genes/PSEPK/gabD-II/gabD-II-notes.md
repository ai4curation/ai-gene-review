# gabD-II evidence notes

## 2026-08-11

Q88EN2 has conflicting electronic cofactor assignments: NAD-specific
TreeGrafter transfer versus an NADP-specific submitter product/EC. Structural
work on an E. coli GabD-family enzyme supports NADP-linked chemistry at the
family level but is not an assay of Q88EN2. [PMID:20174634]

The GABA-shunt assignment and possible 4-hydroxybutyrate role are both
unresolved in KT2440. The simple UniProt gene-list search recovered sad-I,
sad-II, and gabD-II as named succinate-semialdehyde dehydrogenases, but this is
not an exhaustive search of all aldehyde-dehydrogenase paralogs. No gabD-I gene
name was found in that list; the gabD-II suffix therefore remains unexplained
and must not imply candidate completeness.

## 2026-08-31

The completed OpenScientist report challenges the submitted SSADH label and
places PP_4422 in a doe-like ectoine-catabolic locus. Its strongest evidence is
the immediate PP_4421-PP_4423 cluster: PP_4421 is an aminotransferase and
PP_4423 is an aspartoacylase-family hydrolase. PP_4424 and the PP_4425-PP_4428
polar-amino-acid ABC importer form broader neighborhood context, but strand
changes mean the report's description of the whole region as one same-strand
operon is not retained. The immediate cluster supports a DoeC-like
aspartate-4-semialdehyde dehydrogenase hypothesis, but does not establish the
substrate directly. [file:PSEPK/gabD-II/gabD-II-deep-research-openscientist.md
"No direct enzymatic assay of the KT2440 PP_4422 protein exists in the
literature"]

The report's identity percentages, motif interpretation, and literature links
remain provider-generated leads. They are not used here to assert a new
substrate-specific GO term. Until purified-enzyme or genetic evidence resolves
the competition between DoeC-like and SSADH functions, the substrate-specific
GO rows remain `UNDECIDED` and the core function is limited to NAD(P)-linked
aldehyde oxidation. Exclusion from the 4-hydroxybutyrate module means there is
no evidence for a physiological role in that pathway; it does not establish
that Q88EN2 lacks succinate-semialdehyde dehydrogenase side activity.
