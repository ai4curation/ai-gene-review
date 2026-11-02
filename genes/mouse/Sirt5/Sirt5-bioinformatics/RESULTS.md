# Sirt5 (mouse, Q8K2C6) vs human SIRT5 (Q9NXA8): acyl-pocket conservation

Script: `compare_acyl_pocket.py` (stdlib only; reads the cached UniProt flat files).
Raw output: `compare_acyl_pocket.out`.

## Results

- Both proteins are 310 aa; a gapless comparison gives 267/310 identical residues (86.1%),
  and 243/274 (88.7%) over the mature chain after the 36-residue transit peptide.
- The acyl-pocket residues that bind the carboxylate of succinyl/malonyl/glutaryl groups
  are conserved: mouse Y102 and R105 match human Y102 and R105.
- The catalytic His158 (mutated to Tyr in mouse, abolishing activity, in PMID:19410549) and
  the four zinc-binding cysteines (C166, C169, C207, C212) are identical.

## Interpretation

Mouse and human SIRT5 are 1:1 orthologs in PANTHER subfamily PTHR11085:SF10 and are the
two experimental seeds of PAINT node PTN000119399. The specificity-determining residues are
identical, so the acidic-acyl preference measured on the human enzyme in vitro is expected
to hold for mouse Sirt5; mouse-specific evidence for the activities comes independently from
Sirt5 knockout tissues (hyper-succinylation and hyper-glutarylation).
