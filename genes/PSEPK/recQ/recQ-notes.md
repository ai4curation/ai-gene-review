# recQ curation notes

## 2026-08-08 pathway pass

The target catalytic description couples ATP hydrolysis to 3'-5' duplex-DNA
unwinding [file:PSEPK/recQ/recQ-uniprot.txt, "translocating in the 3'-5'
direction.; EC=5.6.2.4;"]. E. coli genetics supports cooperation of RecQ and
RecJ in presynaptic gap extension [PMID:35653392, "the extension of the ssDNA
gap (mediated by the nuclease RecJ and the helicase RecQ)"].

The imported replisome `part_of` annotation is not retained. It comes from a
broad TreeGrafter node, whereas the locally grounded RecQ PAINT node supports
chromosome/cytoplasm locations and helicase functions but not stable replisome
membership. Replication-associated activity alone is insufficient for a
complex-membership assertion.
