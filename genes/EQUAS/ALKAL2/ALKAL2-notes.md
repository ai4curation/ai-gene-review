# ALKAL2 (donkey, A0A9L0J5U7) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry, Ensembl gene model ENSEASG00005022004, 160 aa.

## Identity and sequence
- Donkey record names the protein "ALK and LTK ligand 2" and places it in the ALKAL family by ARBA [file:EQUAS/ALKAL2/ALKAL2-uniprot.txt "Belongs to the ALKAL family."]. InterPro IPR029364 (ALKL1/2), PANTHER PTHR28676:SF2.
- Global alignment to human Q6UX46: 86.18% identity over all 152 human residues; augmentor domain essentially invariant; the two intramolecular disulfide pairs and ALK-contact residues conserved [file:EQUAS/ALKAL2/ALKAL2-bioinformatics/RESULTS.md "Human Cys66, the interchain (dimer) disulfide cysteine in the N-terminal variable region, maps to donkey Tyr67"].
- The missing dimer cysteine matches the human study calling it primate-specific [PMID:30061385 "a fifth, primate-specific cysteine located in the N-terminal variable region mediates dimerization"], and deletion of the variable region barely affects activity [PMID:30061385 "deletion of the N-terminal variable region minimally affects the activity of AUG-α toward LTK or ALK stimulation in cultured cells"].

## Function (human ortholog)
- Secreted cytokine ligand of the RTKs ALK and LTK [file:EQUAS/ALKAL2/ALKAL2-bioinformatics/ALKAL2-human-Q6UX46-uniprot.txt "Cytokine that acts as a physiological ligand for receptor"].
- FAM150B (=ALKAL2) binds and activates ALK [PMID:26418745 "that FAM150A and FAM150B are potent ligands for human ALK that bind to the"]; downstream ERK5 and ERK1/2 phosphorylation [PMID:26418745 "This response was observed at the level of ALK receptor phosphorylation (pALK-Y1604), and with downstream pERK5"].
- Structures: ALKAL2 three-helix-bundle cytokine drives ALK/LTK dimerization near the membrane [PMID:34646012 "The cognate cytokines ALKAL1 and ALKAL2 are monomeric three-helix bundles"]; ligand-membrane interaction stabilizes the complex [PMID:34819673 "This orientation is further stabilized by an interaction between the ligand and the membrane."].
- Location: secreted; associates with the cell membrane after ALK binding [file:EQUAS/ALKAL2/ALKAL2-bioinformatics/ALKAL2-human-Q6UX46-uniprot.txt "Following interaction with"].

## Annotation decisions
- extracellular region: ACCEPT. plasma membrane: KEEP_AS_NON_CORE (ligand surface association, not a resident membrane protein).
- receptor signaling protein tyrosine kinase activator activity and receptor tyrosine kinase binding: ACCEPT (core ligand function).
- TreeGrafter positive regulation of ERK1/2 and ERK5 cascades: KEEP_AS_NON_CORE (downstream readouts of ALK activation, experimentally seen for human ALKAL2).

## ProtNLM2
- One GO prediction: GO:0005576 extracellular region (exactly in donkey GOA) -> CNN. No non-GO ProtNLM2 rows (function text or location) for this accession in the frozen TSV.
