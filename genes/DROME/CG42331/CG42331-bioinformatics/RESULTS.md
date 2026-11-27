# CG42331 (Q9VC41) isoform, active-site and tree-placement check

Script: `isoform_and_tree_check.py` (standard library only; fetches Q9VC42 from UniProt REST
and the PANTHER 19.0 PTHR11475 tree, filtered to fly, human, mouse, worm and zebrafish).
Raw output: `isoform_and_tree_check.out`.

## Isoform identity

Q9VC41 is 1439 aa and is an exact C-terminal suffix of Q9VC42 (1615 aa), starting at Q9VC42 residue 177.
Q9VC41 corresponds to FlyBase CG42331-PC; Q9VC42 corresponds to CG42331-PB and CG42331-PD.
Q9VC42 has a predicted signal peptide at residues 1..22, which Q9VC41 lacks.
The N-terminus of Q9VC41 begins at the start of the animal haem peroxidase domain (MPASERYRTHDGTCNN), so the peroxidase domain itself is complete in Q9VC41.

## Catalytic and heme-linking residues in Q9VC41

All residues at the PROSITE-ProRule PRU00298 positions are the expected ones.
Asp85 and Glu217 are the covalent heme links. His86 is the distal proton acceptor and Arg214 the transition-state stabiliser.
His318 is the proximal heme iron ligand. The Ca2+ site is formed by Asp87, Thr159, Tyr161, Asp163 and Ser165.
The UniProt CAUTION line ("Lacks conserved residue(s) required for the propagation of feature annotation") therefore does not mean that a core catalytic residue is missing.

## PANTHER tree placement

The ancestors of the CG42331 leaf (PTN001290380, subfamily SF109) in the pruned tree are listed below, nearest last.
PTN000895837 (duplication) leads to PTN000895765 (speciation), then PTN007509807 (duplication), then PTN008518854 (duplication).

PTN008518854 is a Drosophila-specific duplication node and resolves as a polytomy of three lineages:
cardinal (cd, SF141), CG42331 (SF109), and the clade of Pxd and CG4009 (both SF86) with CG10211 (SF134).
Its sister lineages within PTN007509807 are cysu (SF106) and the Pxt (SF4) plus Irc (SF125) clade.

No vertebrate, nematode or other model-organism ortholog sits in SF109. The closest relatives are fly paralogs from the same insect-specific expansion.
The best-characterised of these are Pxd (Q01603; IDA peroxidase activity) and cardinal (ommochrome synthesis, IMP).
Neither is closer to CG42331 than the other in this tree.
