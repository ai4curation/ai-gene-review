# pvdE bioinformatics: architecture of the PTN000656738 leaves

## Question

PvdE (Q9I183) is the only seed of the PAINT IBD that places GO:0042626
ATPase-coupled transmembrane transporter activity at node PTN000656738
(PTHR24221). Do the leaves that inherit this IBA have the architecture of a
transporter (membrane domain plus nucleotide-binding domain), as PvdE does?

## Method

`node_leaf_architecture.py` reads the PANTHER leaf IBA GAF cached by
`projects/PSEUDOCAP/build_iba_seed_worklist.py` (`.cache/paint/leaf.gaf.gz`),
selects the GO:0042626 IBAs whose WITH/FROM names PTN000656738, and fetches
each leaf's UniProt length, TRANSMEM features and Pfam cross-references from
rest.uniprot.org. Classification: FULL_TMD_NBD (ABC_tran PF00005 plus
ABC_membrane PF00664 or at least four TM helices), NBD_ONLY (PF00005, no TM
helix, no PF00664), OTHER (anything else, including deleted entries).

Run from the repository root:

```
python3 genes/PSEAE/pvdE/pvdE-bioinformatics/node_leaf_architecture.py .cache/paint/leaf.gaf.gz > genes/PSEAE/pvdE/pvdE-bioinformatics/leaf_architecture.tsv
```

Output: `leaf_architecture.tsv` (one row per leaf). Run on 2026-10-28.

## Results

total leaves: 140; FULL_TMD_NBD=6; NBD_ONLY=126; OTHER=8

The 8 OTHER rows are 7 plant entries deleted from UniProt and one
poplar entry (POPTR_001G327600) with no TM helix.

The six FULL_TMD_NBD leaves are PvdE itself, Pseudomonas syringae SyrD, E. coli
and Salmonella YojI, M. tuberculosis Rv2326c and Chloroflexus Caur_0793 (ThiW).

The NBD_ONLY leaves include the energy-coupling factor ATPases (EcfA, EcfA1,
EcfA2, EcfAB, CbiO), the ModF double-NBD proteins, Neisseria FtsE (cell
division ATP-binding protein) and plant non-intrinsic ABC proteins such as
Arabidopsis ABCI11/NAP14.

## Interpretation

PTN000656738 is a clade defined by the nucleotide-binding domain: 126 of 140
leaves are soluble NBD-only proteins, and the node's other two IBDs are
NBD-appropriate (GO:0005524 ATP binding seeded by Thermotoga EcfA1/EcfA2;
GO:0043190 ABC transporter complex seeded by Salmonella CbiO). An NBD-only
subunit can at most contribute to an ATPase-coupled transporter activity
carried out by its complex, and FtsE belongs to the FtsEX system, which is not
generally regarded as a transporter. The GO:0042626 IBD, seeded only by the
full-length exporter PvdE, is therefore placed too deep: it is true for PvdE
and the few TMD-NBD fusion leaves but is an over-propagation (an `enables`
transporter activity on NBD-only proteins) for most leaves.

Caveat: the classification uses UniProt TRANSMEM features and Pfam xrefs, not
a fresh TM prediction or alignment; a NBD-only leaf could in principle be a
fragment, but 126 of 140 is far beyond what fragments would explain.
