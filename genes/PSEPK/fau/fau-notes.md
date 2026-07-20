# fau curation notes

## Evidence

Q88CH8 is assigned EC 6.3.3.2/RHEA:10488 and the
PTHR23407:SF1 5-formyltetrahydrofolate cyclo-ligase family
[file:PSEPK/fau/fau-uniprot.txt
"DE   RecName: Full=5-formyltetrahydrofolate cyclo-ligase";
"Xref=Rhea:RHEA:10488"]. Canonical PAINT assigns GO:0030272 at
PTN000601268 from experimentally supported family members including E. coli
YgfA. The same positive, non-negated PAINT node supports GO:0009396, which is
not restricted to de novo folate-ring synthesis
[file:interpro/panther/PTHR23407/PTHR23407-paint.tsv
"PTHR23407\tPTN000601268\tGO:0009396\tP\tIBD\tfalse"].

The OpenScientist pathway report correctly recognizes fau as the
5-formyl-THF salvage operation even though the local primary pathway
partition assigns it to ppu04981
[file:projects/P_PUTIDA/deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md
"functionally this is Step 4 of the carrier-interconversion module"].

## Assessment

The specific cyclo-ligase activity and tetrahydrofolate interconversion are
accepted on strong family/reaction evidence. GO:0009396 is retained as
non-core because forming 5,10-methenyl-THF is within the broader folate
biosynthetic process, while GO:0030272 states the salvage chemistry precisely.
No direct KT2440 enzyme assay was found.
