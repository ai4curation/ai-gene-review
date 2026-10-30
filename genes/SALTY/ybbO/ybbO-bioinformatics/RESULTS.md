# ybbO (STM0505, Q7CR11) bioinformatics

Script: `compare_ecoli_ybbo.py` (run with `uv run python compare_ecoli_ybbo.py`);
raw output in `compare_ecoli_ybbo.out`.

## Ortholog comparison with E. coli YbbO (P0AFP4)

Global alignment (BLOSUM62, gap open -10, extend -0.5) of Salmonella Q7CR11 against
E. coli K-12 YbbO P0AFP4:

Q7CR11 length: 256; P0AFP4 length: 269
Aligned positions: 256; identical: 232; identity over shorter sequence: 90.6%

The alignment is collinear over the whole Salmonella protein; the only length
difference is a 13-residue N-terminal extension in the annotated E. coli sequence
(MTHKATEILTGKV), which suggests that the two proteins share the same start at the
conserved MQKSVLITG motif and the E. coli start may be called upstream.

## SDR signature residues in Q7CR11

Cofactor-binding TGxxxGxG motif at 8: TGCSSGIG
YxxxK motif at Y146/K150: YAASK

Y146 is the PROSITE-predicted proton acceptor (UniProt FT ACT_SITE 146). Together with
the Rossmann glycine-rich motif these are the hallmarks of a catalytically competent
classical SDR, so there is no sign that Q7CR11 is a pseudoenzyme.

## Interpretation

Q7CR11 is the Salmonella orthologue of E. coli YbbO, a characterised NADPH-dependent
aldehyde reductase. At 90.6% identity with conserved catalytic residues, transfer of
the NADPH-dependent aldehyde reductase activity (GO:0008106) is well justified. The
physiological aldehyde substrate is unknown in both organisms.

Fitness data: `just fetch-fitness SALTY ybbO` could not reach any FEBA data source in
this environment (and mapped STM0505 to the wrong organism code, SB2B), so no fitness
evidence was used.
