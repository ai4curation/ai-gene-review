# HP1507 construct identity and cofactor-contact audit

Objective: determine whether native residues absent from the frozen O26037 sequence contact NADP in the experimentally determined NCTC11637 structure. No new structure is predicted.

Run `just fetch` and `just analyze` in this directory. Python 3.12 and its standard library are sufficient; `uv` manages the interpreter. Source structures are downloaded from RCSB without modification. The script reports the minimum protein/ligand heavy-atom distance for each selected residue, using the deposited coordinates and major alternate conformation. A 4.0-A proximity cutoff is an exploratory contact threshold, not a hydrogen-bond or functional assignment. The independent input is C. jejuni PLP-bound decarboxylase 3N29, with a different ligand and residue interval.

Sources: https://www.rcsb.org/structure/8H52 (PMID36283333); https://www.rcsb.org/structure/3N29 (PMID20534592). Refer to RESULTS.md for interpretation and limitations.
