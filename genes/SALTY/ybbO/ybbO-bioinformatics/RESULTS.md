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

## Orthology: is it 1:1?

Script: `orthology_and_residues.py`; raw output in `orthology_and_residues.out`.
Full-proteome Smith-Waterman searches (BLOSUM62) against the LT2 (UP000001014, 4533
proteins) and K-12 (UP000000625, 4403 proteins) reference proteomes:

Reciprocal best hit Q7CR11 <-> P0AFP4: True
Score gap forward (best / 2nd): 1203 / 201; reverse: 1203 / 216

The next-best hits on both sides are other classical SDRs (UcpA, FabG, YciK, YghA)
at 26-35% identity, so there is no in-paralogue in either genome that competes with
the orthologue. The gene neighbourhood is also conserved:

  LT2: STM0503=ybbM  STM0504=ybbN  STM0505=ybbO  STM0506=tesA  STM0507=ybbA
  K-12: b0491=fetB  b0492=cnoX  b0493=ybbO  b0494=tesA  b0495=ybbA

Reciprocal best hit, a large score gap and conserved synteny together make Q7CR11 and
P0AFP4 one-to-one orthologues.

## Residue conservation

Catalytic tetrad: N105(N) S133(S) Y146(Y) K150(K)

(Classical SDR tetrad, Asn on helix alpha-E, Ser, and the Tyr/Lys of YxxxK; the
NNAG motif at 80 and TGCSSGIG at 8 are the structural and cofactor motifs.) All four
tetrad residues are invariant across 49 Enterobacterales YbbO orthologues (61.6-100%
identity to Q7CR11).

Q7CR11 vs P0AFP4: 24 substituted positions. Mapped onto the AlphaFold model
(mean pLDDT 95), an approximate active-site pocket (36 residues with a side-chain atom
within 10 A of the catalytic Ser/Tyr) contains only one of them:

  in approximate pocket: 1 Y84F
  tetrad residues substituted: none

Y84 is itself variable among YbbO orthologues (31% conserved), so this is not a sign
of divergent specificity. The other substitutions cluster in the surface-exposed
segment 192-256 and at the N-terminus.

Of the 36 pocket residues, 22 are invariant in all YbbO orthologues. Eight are
invariant in YbbO yet differ from all four vertebrate SDR9C relatives used as IBA
donors (HSD17B6, RDH16, DHRS9, RDH5):

Candidate YbbO-specific pocket residues (invariant in YbbO orthologues, differ from all four vertebrate SDR9C relatives): I14 Y87 Q101 T131 R143 P178 F183 N198

These are candidate specificity-determining positions distinguishing the YbbO
orthogroup from the steroid/retinoid SDR9C dehydrogenases (R143 aligns to a gap in
three relatives, so that one is an insertion rather than a substitution). The pocket
is a distance cut-off on a predicted apo model without cofactor or substrate, so
these are hypotheses for mutagenesis, not established substrate contacts.

Caveat: the orthologue set is UniProt entries whose gene name is ybbO; names on
unreviewed entries are themselves propagated, but all 49 retain the tetrad and share
61.6% or more identity with Q7CR11.

## Interpretation

Q7CR11 is the one-to-one Salmonella orthologue of E. coli YbbO, a characterised
NADPH-dependent aldehyde reductase. With 90.6% identity, conserved synteny, an intact
tetrad, and an active-site pocket identical apart from one variable position, transfer of
the NADPH-dependent aldehyde reductase activity (GO:0008106) is well justified. The
physiological aldehyde substrate is unknown in both organisms.

Fitness data: `just fetch-fitness SALTY ybbO` could not reach any FEBA data source in
this environment (and mapped STM0505 to the wrong organism code, SB2B), so no fitness
evidence was used.
