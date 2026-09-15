# kdpA curation notes

## Evidence assessment

PSEPK Q88FD7 is assigned to the KdpA family by UniProt and retains the role of
the potassium-selective, channel-like subunit. The E. coli KdpFABC crystal
structure directly places potassium in the KdpA selectivity filter and separates
the KdpA ion pathway from the KdpB ATPase machinery [PMID:28636601, "one
channel-like subunit (KdpA) belonging to the superfamily of potassium
transporters"]. The completed OpenScientist report independently identifies the
same architecture and explicitly notes that direct P. putida biochemical data
were not found [file:PSEPK/kdpA/kdpA-deep-research-openscientist.md].

## Curation decision

GO:0030955 is KdpA's own molecular function. GO:0008556 describes the complete
heteromeric pump and is accepted in substance, with the preferred
`contributes_to` relationship represented in `core_functions` rather than as a
no-op term replacement.
