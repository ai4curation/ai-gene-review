# Ligand inventory of Corynebacterium sp. U-96 heterotetrameric sarcosine oxidase crystal structures

Question: does the SoxA (alpha, chain A) subunit carry an iron-sulfur cluster, as
the InterPro2GO mapping from IPR001041 (2Fe-2S ferredoxin-type domain) implies
(GO:0051536 iron-sulfur cluster binding)? Which subunit carries which cofactor?

Method: `python3 pdb_ligands.py` queries the RCSB Data API for the non-polymer
entities of the six PDB entries listed in the UniProt records (1VRQ, 1X31, 3AD7,
3AD8, 3AD9, 3ADA; chain A = SoxA Q50LF0, B = SoxB Q50LF2, C = SoxG Q50LE9,
D = SoxD Q50LF1). Raw output: `pdb_ligands.tsv` (run 2026-11-04).

Results (from pdb_ligands.tsv):

- Chain A (SoxA): NAD in all six entries; folinic acid (FON) in 1VRQ; sulphate.
  No iron-sulfur ligand (FES, SF4, F3S) in any entry.
- Chain B (SoxB): FAD and FMN in all six entries; dimethylglycine (1VRQ, 1X31),
  methylthioacetate (3AD7), pyrrole-2-carboxylate (3AD8), sulphite (3ADA).
- Chain C (SoxG): sulphate only.
- Chain D (SoxD): one zinc ion in all six entries.

Conclusion: no iron-sulfur cluster is modelled in any of the six structures, in
any chain. The only metal is the SoxD zinc. The 2Fe-2S ferredoxin-type InterPro
signature on SoxA therefore marks a fold, not a bound cluster, in this protein.
Absence of a modelled ligand is strong but not absolute evidence (a labile
cluster lost during purification would also be absent); the cofactor
reinvestigation of the purified enzyme (PMID:11902668) likewise found only NAD+,
FAD and covalent FMN.
