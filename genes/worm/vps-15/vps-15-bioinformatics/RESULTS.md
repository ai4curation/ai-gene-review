# VPS-15 pseudokinase gatekeeper check

Script: `gatekeeper_check.py` (global BLOSUM62 alignment of the N-terminal ~400 residues of
human VPS15/PIK3R4 Q99570 and C. elegans VPS-15 Q23669, sequences fetched live from UniProt).

## Result (run 2026-10-08)

- human R103 [gatekeeper (GTP specificity)] -> worm R101
- identical aligned positions in N-terminal 400 aa: 152

## Interpretation

Human VPS15 is a pseudokinase that binds GTP rather than ATP, with Arg103 at the gatekeeper
position responsible for nucleotide specificity (PMID:39913640). C. elegans VPS-15 keeps an
arginine at the equivalent position (R101), and the pseudokinase region is well conserved
(about 38% identity over the aligned N-terminal region). This is consistent with, but does
not prove, the worm protein being a GTP-binding pseudokinase. No biochemical data exist for
worm VPS-15.
