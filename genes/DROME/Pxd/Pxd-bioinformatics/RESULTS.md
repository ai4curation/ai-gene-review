# Pxd (Q01603) active-site and PANTHER tree / PAINT placement check

Script: `pxd_tree_and_sites.py` (standard library only; reads the local UniProt file and
`interpro/panther/PTHR11475/PTHR11475-paint.tsv`, and fetches the PANTHER PTHR11475 tree).
Raw output: `pxd_tree_and_sites.out`.

## Catalytic residues

Q01603 retains His185 (distal His, proton acceptor), Arg331 (transition-state stabiliser) and His437 (proximal heme-iron ligand) at the PROSITE-ProRule PRU00298 positions.
Nothing in the sequence suggests a pseudo-enzyme, which agrees with the measured peroxidase activity of the recombinant protein.

## PANTHER tree placement (unfiltered tree)

Pxd is the leaf PTN000158989 in subfamily SF86. The root of its ancestor path is PTN000158755 (speciation, taxonomic range LUCA).
The nearest ancestors are PTN000158981, the duplication that separates Pxd from CG4009 (both SF86), and above that PTN000158980 (speciation, Diptera).
PTN008518854, the duplication that separates the cardinal (Q9VCW2), CG42331 (Q9VC42, labelled CG13632 in the PANTHER tree) and Pxd/CG4009/CG10211 lineages, has taxonomic range Hexapoda-Crustacea in the unfiltered tree.
It therefore predates the insects; it only looks fly-specific when the tree is filtered to model organisms.
Its parent PTN007509807 (duplication, Arthropoda) also contains cysu and the Pxt plus Irc clade.

## PAINT IBD nodes inherited by Pxd

Of the 15 IBD assertions in PTHR11475, Pxd descends from only one: PTN000158755 GO:0004601 peroxidase activity.
Pxd does not descend from the nodes carrying extracellular region (PTN000895746), thiocyanate peroxidase activity (PTN008518865, PTN008518867), iodide peroxidase activity and thyroid hormone generation (PTN002607745), defense response to bacterium (PTN002607724), or the dual-oxidase NADPH oxidase terms (PTN000239643, PTN000944147, PTN001735877).
The halide and thiocyanate oxidising activities of vertebrate myeloperoxidase, lactoperoxidase and eosinophil peroxidase are therefore not phylogenetically assigned to Pxd.

## Subtree of PTN007509807 (filtered to fly, human, mouse, worm, zebrafish)

`(cysu,(Pxt,Irc)PTN008518852,(cd,CG13632,((CG4009,Pxd)PTN000158981,CG10211)PTN008970748)PTN008518854)PTN007509807`
