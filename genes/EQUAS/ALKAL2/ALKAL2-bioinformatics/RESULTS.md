# ALKAL2: donkey-human sequence comparison

Script: `align_to_human.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5).
Command: `uv run python align_to_human.py ../ALKAL2-uniprot.txt ALKAL2-human-Q6UX46-uniprot.txt 66 97 100 111 123 125 134 147`
Raw output: `alignment_output.txt`. Human record Q6UX46 was downloaded from the UniProt REST API (`ALKAL2-human-Q6UX46-uniprot.txt`).

## Results

- The donkey sequence A0A9L0J5U7 (160 residues) aligns to human Q6UX46 (152 residues) with 86.18% identity across 152 paired residues, covering 100% of the human sequence.
- Identity is highest in the C-terminal augmentor domain: donkey 101-150 are 50/50 identical to human 99-148.
- The four augmentor-domain cysteines that form the two intramolecular disulfides in human (Cys111-Cys147, Cys125-Cys134) are conserved (donkey Cys113, Cys149, Cys127, Cys136).
- Residues mutated in the human ALK-binding studies are conserved (human Phe97, His100, Arg123 map to donkey Phe99, His102, Arg125).
- Human Cys66, the interchain (dimer) disulfide cysteine in the N-terminal variable region, maps to donkey Tyr67, so the donkey protein lacks that cysteine.
- Both proteins have a predicted 24-residue signal peptide (donkey SignalP 1..24).

## Interpretation

The donkey protein is a full-length ALKAL2 ortholog with an intact augmentor domain; loss of the variable-region cysteine is consistent with the human study describing it as primate-specific, and that cysteine is not required for ALK/LTK activation.
