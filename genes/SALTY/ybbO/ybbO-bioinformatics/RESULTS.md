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

### Which Salmonella/E. coli substitutions could matter?

Each substitution was scored by the minimum side-chain distance to the catalytic
Ser133/Tyr146 midpoint in the AlphaFold model, its BLOSUM62 score, the conservation of the
Salmonella residue across the 49 orthologues, and how many orthologues carry the E. coli
residue. The nearest ten:

  sub	dist_A	pLDDT	BLOSUM62	%orth_query_res	#orth_with_ecoli_res	other residues at position
  Y84F	8.5	95	3	31%	34/49	-
  V86M	11.1	97	1	39%	15/49	ILT
  S104A	12.9	97	1	16%	20/49	T
  R207L	13.4	87	-2	6%	46/49	-
  D208G	14.7	87	-1	6%	21/49	KMPST
  L250M	15.7	93	2	41%	27/49	FI
  D17E	16.1	97	2	6%	19/49	AILV
  D210E	16.4	90	2	8%	43/49	Q
  S256G	16.6	61	0	35%	25/49	AHNT
  L227M	17.1	98	2	59%	16/49	IV

(full table in `orthology_and_residues.out`)

- None of the 24 is at a conserved position: the Salmonella residue is found in at most
  63% of orthologues, and the E. coli residue occurs in at least 11 other orthologues at
  every position. Nothing points to a functional change specific to either species.
- The most plausible modulators of substrate preference are:
  - **Y84F** (8.5 A, the only one in the pocket): loss of one hydroxyl beside the NNAG
    motif. Phe is the majority residue (34/49), so Salmonella Tyr84 is the less common state.
  - **S104A** (12.9 A): immediately before the catalytic N105 on helix alpha-E; Salmonella
    Ser is a minority residue (16%).
  - **R207L / D208G / D210E**: a cluster in a lower-confidence segment (pLDDT 87-90) that
    probably corresponds to the flexible SDR substrate-binding loop. The apo model may
    show it open, so these distances may overstate how far it is from a bound substrate.
    R207L and D208G each remove a charge, and Salmonella R207 and D208 are rare among
    orthologues (6% each).
- The most radical change, R74C (BLOSUM62 -3), is 30 A away on the surface.
- These are prioritised hypotheses for comparative kinetics or swap mutants, not
  established functional differences.

## N-terminal start site of E. coli YbbO

Number of residues each YbbO entry carries before the position aligned to Salmonella Met1
(the conserved MQKSVLITG start):

  0 aa: 34, 13 aa: 16
  P0AFP4 extension: 13 aa (P0AFP4 in the orthologue set)

The 13-residue extension (MTHKATEILTGKV in P0AFP4) is present in the 269-aa models of
Escherichia, Shigella and Klebsiella entries and absent from the other 34. Annotated starts
are often propagated within a clade, so this suggests, but does not show, that the
upstream start is a gene-model artefact. N-terminal proteomics would settle it.

## Interpretation

Q7CR11 is the one-to-one Salmonella orthologue of E. coli YbbO, a characterised
NADPH-dependent aldehyde reductase. With 90.6% identity, conserved synteny, an intact
tetrad, and an active-site pocket identical apart from one variable position, transfer of
the NADPH-dependent aldehyde reductase activity (GO:0008106) is well justified. The
physiological aldehyde substrate is unknown in both organisms.

Fitness data: `just fetch-fitness SALTY ybbO` could not reach any FEBA data source in
this environment (and mapped STM0505 to the wrong organism code, SB2B), so no fitness
evidence was used.
