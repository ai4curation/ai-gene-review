# ruvC curation notes

- Q88NJ2 is the RuvC crossover-junction endonuclease in the KT2440 `ruvCAB` locus. Its target record specifies symmetric nicking and the resulting 5-prime-phosphate/3-prime-hydroxyl ends [UniProtKB:Q88NJ2, "yielding a 5'-phosphate and a 3'-hydroxyl group"].
- The E. coli RuvC structure and mutational analysis establish a dimeric RNase-H-like nuclease with four acidic catalytic residues [PMID:7923356, "the catalytic center, comprising four acidic residues, lies at the bottom of a cleft that nicely fits a DNA duplex"]. Conservation supports transfer to KT2440, but no direct KT2440 cleavage assay is available.
- PP_0151 is not a second RuvC-family enzyme; its secretion signal and DUF2388/TIGR02448 assignment are incompatible with this intracellular RNase-H-like resolvase mechanism.

## 2026-11-09 re-review (Claude, AI-assisted; module audit)

- Nucleic acid binding is MODIFY to four-way junction DNA binding (GO:0000400); DNA endonuclease activity is TOO_GENERAL against GO:0008821. DNA repair and DNA recombination are MODIFY to recombinational repair (GO:0000725). Every row now carries quoted support.
- 2026-11-10: the GO:0008821 reason now distinguishes the three HAMAP ACT_SITE residues annotated on Q88NJ2 from the four-acidic-residue catalytic center described for E. coli RuvC.
