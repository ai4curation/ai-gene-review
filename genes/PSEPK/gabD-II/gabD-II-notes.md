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

## 2026-10-15 — re-review after OpenScientist TreeGrafter control batch

The blinded OpenScientist stress test of GO:0004777
[file:PSEPK/gabD-II/gabD-II-hypotheses/function-hypothesis-go-0004777/openscientist.md
"The recommended curation lead is to **retain the SSADH function but generalize or replace the cofactor**"]
recommended MODIFY to GO:0009013 (SSADH, NAD(P)+). It was blinded to gene
context and its panel held only GabD, ALDH5A1 and YneI.

Checks made in this re-review (scratch alignments, Biopython PairwiseAligner,
global, BLOSUM62, gap open -10 / extend -0.5; identities as % of the 490-aa
query; sequences from UniProt REST):

- Q88EN2 vs E. coli GabD P25526: 50.8% (report 51.7%)
- Q88EN2 vs Halomonas elongata DoeC E1V7V8: 52.2%
- Q88EN2 vs KT2440 DavD Q88RC0 (glutarate-semialdehyde DH): 50.2%
- Q88EN2 vs human ALDH5A1 P51649: 48.4% (report 48.2%)
- Q88EN2 vs E. coli Sad/YneI P76149: 31.6% (report 35.4%)

UniProt E1V7V8 (Swiss-Prot DoeC) is in PANTHER PTHR43353:SF5, the same
subfamily as Q88EN2, and itself carries the TreeGrafter GO:0004777 and
GO:0009450 rows; its reaction is recorded as RHEA:45764 (L-aspartate
4-semialdehyde + NAD+ + H2O = L-aspartate + NADH), NAD+-dependent by curator
inference, and its disruption blocks growth on ectoine. KEGG: PP_4421 K15785
(L-2,4-diaminobutyrate transaminase), PP_4422 K00135, PP_4423 K15784
(N2-acetyl-L-2,4-diaminobutanoate deacetylase), all on the complement strand.

GO has no term for non-phosphorylating aspartate-semialdehyde dehydrogenase:
RHEA:45764 is only a narrowMatch on GO:0004029, and GO:0004073 is the
phosphorylating EC 1.2.1.11 reaction. A proposed_new_terms entry was added as
an ontology-gap record; it is not used as a core function.

Decision: GO:0004777 and GO:0036243 stay UNDECIDED. The report's facts
(active GabD-clade enzyme) hold, but its MODIFY target still asserts the
succinate-semialdehyde substrate that the doe-like locus disputes, and its
NADP+ lean is a fingerprint, not a measurement. The report's PMIDs are not
cached and were not imported.
