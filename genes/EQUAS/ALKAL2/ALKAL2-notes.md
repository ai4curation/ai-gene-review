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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon EQUAS ALKAL2 --fallback perplexity-lite` failed (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). No deep-research file was created; this re-review uses the four cached full-text papers (PMID:26418745, PMID:30061385, PMID:34646012, PMID:34819673), the human Swiss-Prot record and the existing sequence comparison.

### Identity
- A0A9L0J5U7 is the full-length donkey ALKAL2 gene model (160 aa vs 152 aa for human Q6UX46; 100% coverage of human, 86% identity, augmentor domain 50/50 identical, all four intramolecular-disulfide cysteines and ALK-contact residues conserved) [file:EQUAS/ALKAL2/ALKAL2-bioinformatics/RESULTS.md "covering 100% of the human sequence"]. Not a fragment or isoform. The only notable difference is loss of the primate-specific dimerizing cysteine (human Cys66 -> donkey Tyr67).

### Evolutionary grounding
- Donkey and human ALKAL2 are both in PANTHER PTHR28676:SF2 (ALK AND LTK LIGAND 2); ALKAL1 is the paralog subfamily SF1. Function transfer from human ALKAL2 is therefore within-subfamily orthology.
- The TreeGrafter node PTN009109768 transferred ERK1/2 and ERK5 regulation but not the human IDA terms cytokine activity (GO:0005125) or positive regulation of neuron projection development (GO:0010976). Treated as deliberate; neither is added. Neurite outgrowth in PC12 cells is a readout of ALK activation, not ALKAL2 participation.
- No PANTHER family review for PTHR28676 exists under interpro/panther/ (only entries/metadata files), so no subfamily-placement disagreement to report. No module covers ALK/LTK signaling.

### Decision changes vs the previous pass
- GO:0030298 receptor signaling protein tyrosine kinase activator activity: ACCEPT -> MODIFY to GO:0030297 transmembrane receptor protein tyrosine kinase activator activity. GO:0030298 is defined for "receptor signaling protein tyrosine kinase" and lacks a signaling receptor activator parent; ALK and LTK are transmembrane RTKs [PMID:34646012 "are recently deorphanized receptor tyrosine kinases"], which is GO:0030297's definition, and that term is what other RTK ligands carry (QuickGO human: EGF, NGF, VEGFA, EFNA5, NRG1...). core_functions MF updated to match; raised as a suggested question since the ALK axis consistently uses GO:0030298.
- NEW GO:0007169: retained (ligand initiates the pathway), but its UniProt DR GO-line quote was replaced with publication text, as DR GO lines restate annotations.
- Other rows unchanged: extracellular region ACCEPT; plasma membrane KEEP_AS_NON_CORE; receptor tyrosine kinase binding ACCEPT; ERK1/2 and ERK5 regulation KEEP_AS_NON_CORE.
- Added reference_review blocks for the four PMIDs.

### Relative
- Closest characterised relative: human ALKAL2 (Q6UX46), same PANTHER subfamily SF2. No review exists in the repo (genes/human/ALKAL2 absent), so it is the next review target.
