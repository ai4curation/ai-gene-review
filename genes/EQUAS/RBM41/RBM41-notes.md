# RBM41 (donkey, A0A9L0IK51) - review notes

DONKEY40 cohort. 6 IEA GOA rows (4 TreeGrafter, 2 InterPro/combined). No cached RBM41 literature was available; NCBI E-utilities could not be reached from this session, so no primary RBM41 paper was consulted.

## Sequence
- [file:EQUAS/RBM41/RBM41-bioinformatics/RESULTS.md "95.83% identity over 408 paired residues"]; RRM: ["78 of 79 human residues in this span are identical"]. Donkey has a 24-residue insertion (175-198) in a non-domain region.

## Family
- [file:EQUAS/RBM41/RBM41-bioinformatics/interpro-IPR045164.md "It binds to the U11-associated 59K protein via its RRM1 and employs the RRM2 to bind hairpin III of the U12 small nuclear RNA (snRNA)."] (about RNPC3) and ["RBM41 contains only one RRM. Its biological function remains unclear."]
- Human UniProt: [file:EQUAS/RBM41/RBM41-bioinformatics/human-Q96IZ5-uniprot.txt "May bind RNA."]
- Human RBM41 carries the same IBAs (U12 snRNA binding, U12-type spliceosomal complex, mRNA splicing via spliceosome, pre-mRNA intronic binding) from PTN000413238.

## Decisions
- Accept U12 snRNA binding, U12-type spliceosomal complex, mRNA splicing via spliceosome as phylogenetic inference (PAINT node + RRM homology to RNPC3 RRM2). UNDECIDED pre-mRNA intronic binding (family's known contact is U12 snRNA). Nucleic acid binding and RNA binding marked TOO_GENERAL.
- ProtNLM2 GO:0003723 RNA binding: correct but less precise than GOA U12 snRNA binding (LSP).
