# folD2 curation notes

## Evidence

The reviewed UniProt record identifies Q88KM5 as bifunctional FolD2 and assigns
RHEA:22812 and RHEA:23700
[file:PSEPK/folD2/folD2-uniprot.txt
"DE   RecName: Full=Bifunctional protein FolD 2"; "Xref=Rhea:RHEA:22812";
"Xref=Rhea:RHEA:23700"]. Q88KM5 and Q88LI7 are both assigned to
PTHR48099:SF5 in the local member table, while PTN000002250 has positive IBD
rows for GO:0004488 and GO:0004477
[file:interpro/panther/PTHR48099/PTHR48099-paint.tsv].

The final OpenScientist gene report independently recovers the bifunctional
NADP-linked FolD assignment, but it also reports unsaved pairwise identities
and exact residue alignments, transfers E. coli essentiality as ortholog
context, and suggests FolD2 is the principal housekeeping copy. Those claims
are not propagated because the report itself states that no KT2440-specific
biochemical or knockout study was found and that paralog division of labor is
unresolved
[file:PSEPK/folD2/folD2-deep-research-openscientist.md
"No *P. putida*-specific biochemical or knockout study of FolD2 was found"].

The refreshed max3 OpenScientist pathway report maps both full-length FolD
paralogs to both core operations but frames the target assignments as homology
rather than direct KT2440 enzymology. It still treats expression, essentiality,
and the identity of any dominant copy as open questions
[file:projects/P_PUTIDA/deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md
"check expression/essentiality context and which is the housekeeping copy"].

## Assessment

The catalytic assignments are high-confidence family inferences rather than
direct KT2440 measurements. Both specific activities are accepted. The
cytoplasm parent is retained as non-core because cytosol is already present,
and the broad oxidoreductase parent is likewise retained as non-core. No
paralog-specific physiological claim is made.
