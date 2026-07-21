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

The max3 OpenScientist gene report found no direct biochemical or genetic
characterization of Q88CH8. It independently recapitulates the target
UniProt/family assignment, but its pairwise identities, exact residue mapping,
generic cytosolic localization, and phenotypes transferred from other
bacteria were not saved as reproducible analyses or demonstrated in KT2440;
those claims are not used here
[file:PSEPK/fau/fau-deep-research-openscientist.md
"No direct biochemical characterization of the P. putida enzyme"].

The refreshed max3 OpenScientist pathway report maps fau to the optional
5-formyl-THF salvage operation and treats its ppu04981 primary-bucket
assignment as a cross-mapping discrepancy. This remains homology/domain
evidence rather than a target enzyme assay
[file:projects/P_PUTIDA/deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md
"Covers the optional salvage branch"].

## Assessment

The specific cyclo-ligase activity and tetrahydrofolate interconversion are
accepted on strong family/reaction evidence. GO:0009396 is retained as
non-core because forming 5,10-methenyl-THF is within the broader folate
biosynthetic process, while GO:0030272 states the salvage chemistry precisely.
No direct KT2440 enzyme assay was found.
