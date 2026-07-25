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

The max3 OpenScientist gene report independently recapitulates both activities
from the reviewed target record, states that no PP_1945-specific biochemical
or genetic study was found, and leaves paralog usage unresolved. Its unsaved
pairwise identities and exact residue mapping, gene-neighborhood model,
transferred essentiality/druggability, and downstream-consumer claims are not
used as target-level evidence
[file:PSEPK/folD1/folD1-deep-research-openscientist.md
"No direct experimental data on PP_1945"].

The refreshed max3 OpenScientist pathway report maps both full-length FolD
paralogs to both core operations but frames the target assignments as homology
rather than direct KT2440 enzymology. Its coverage call does not resolve
expression, essentiality, or paralog dominance
[file:projects/P_PUTIDA/deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md
"two full-length FolD paralogs"; "direct KT2440 enzymology"].

## Assessment

The exact activities are supported strongly by reviewed family/EC/Rhea
annotation, not by a direct KT2440 biochemical study. The curation therefore
accepts both catalytic terms and tetrahydrofolate interconversion, retains the
correct but broad catalytic/oxidoreductase parents as non-core, and makes no
claim that folD1 is the dominant paralog.
