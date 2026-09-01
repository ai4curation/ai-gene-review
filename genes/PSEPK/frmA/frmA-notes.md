# frmA evidence notes

## 2026-09-01

Q88MF5 is classified in PANTHER subfamily `PTHR43880:SF12`, whose exact label
is `ALCOHOL DEHYDROGENASE CLASS-3`. The reviewed E. coli FrmA protein P25437 is
in the same subfamily and has direct evidence for glutathione-dependent
formaldehyde dehydrogenase activity. The module therefore uses SF12 as a
lineage container together with the exact required-function constraint
GO:0051903; membership in this broader class-3 lineage alone is not treated as
proof that every member has the FrmA reaction specificity. [UniProtKB:P25437]

The target's cytosol annotation is a TreeGrafter IEA supported by
`PANTHER:PTN002466975`. It is biologically plausible but is retained as
non-core because no direct KT2440 localization evidence was found. The PAINT
cache contains a broader ancestral node, `PANTHER:PTN000191653`, supported by
experimentally characterized FrmA proteins, but the target's descent from that
specific node was not established from the local data. The module therefore
does not assert an ancestral node.

As with FrmC, direct biochemical and isotope-resolved genetic evidence is
still needed to establish the proposed consecutive FrmA-FrmC route in KT2440.

The KT2440 study provides direct physiological support for a role in
formaldehyde tolerance: PP_1616 was induced 9.2-fold after formaldehyde
exposure, and its insertion mutant failed to grow at 1.5 mM formaldehyde. It
does not directly assay the FrmA reaction. [PMID:21261833 "the change was
9.2-fold for PP1616"; PMID:21261833 "PP_1616d‐isomer specific 2‐hydroxy acid
dehydrogenaseNo growth"]

OpenScientist completed a full gene-level report on 2026-09-01. It explicitly
found no direct biochemical characterization of Q88MF5 and identified the GSNO
role as a conserved-family inference rather than a KT2440 experiment. The
report's stronger statements about target localization, oligomeric state,
kinetics, and pathway inputs were not imported because they derive from
orthologs or general biochemical context. [file:PSEPK/frmA/frmA-deep-research-openscientist.md
"No direct biochemical characterization of the KT2440 protein itself.";
file:PSEPK/frmA/frmA-deep-research-openscientist.md "GSNO-reductase role not
experimentally demonstrated in KT2440."]
