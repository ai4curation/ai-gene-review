# folD1 curation notes

## Evidence

The reviewed UniProt record identifies Q88LI7 as bifunctional FolD1 and assigns
the NADP-linked dehydrogenase reaction RHEA:22812 and cyclohydrolase reaction
RHEA:23700 [file:PSEPK/folD1/folD1-uniprot.txt
"DE   RecName: Full=Bifunctional protein FolD 1"; "Xref=Rhea:RHEA:22812";
"Xref=Rhea:RHEA:23700"]. The local PANTHER member table places both KT2440 FolD
paralogs in PTHR48099:SF5, and canonical PAINT assigns GO:0004488 and
GO:0004477 at PTN000002250
[file:interpro/panther/PTHR48099/PTHR48099-paint.tsv].

The OpenScientist pathway report treats folD1 and folD2 as coverage for both
FolD reactions but explicitly leaves their paralog-specific division of labor
unresolved
[file:projects/P_PUTIDA/deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md
"two full-length bifunctional FolD copies (folD1, folD2)"].

## Assessment

The exact activities are supported strongly by reviewed family/EC/Rhea
annotation, not by a direct KT2440 biochemical study. The curation therefore
accepts both catalytic terms and tetrahydrofolate interconversion, retains the
correct but broad catalytic/oxidoreductase parents as non-core, and makes no
claim that folD1 is the dominant paralog.
