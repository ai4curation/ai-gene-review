# AP5S1 (sigma-5): what the AP-5 structure says the subunit does

Regenerate with `uv run python sigma5_structure.py` in this directory. Structures are
downloaded from RCSB and sequences from UniProt at run time; expected sequence lengths
are asserted, and no result below is hardcoded.

## Inputs and chain verification

| chain | protein | modelled residues | UniProt span | numbering offset | fraction matching after offset |
|---|---|---|---|---|---|
| A | zeta5 (AP5Z1, mouse) | 671 | 1-787 | -1 | 0.9985 |
| B | beta5 (AP5B1, human) | 551 | 7-631 | 0 | 1.0 |
| C | sigma5 (AP5S1, human) -- the target | 182 | 1-199 | 0 | 1.0 |
| D | SPG11 WD40-hairpin (spatacsin, human) | 402 | 22-521 | 0 | 1.0 |
| E | mu5 (AP5M1, mouse) | 468 | 2-490 | 0 | 1.0 |
| S | sigma2 (AP2S1, mouse) in 2JKR | 142 | 1-142 | 0 | 1.0 |

Every chain indexes its UniProt sequence directly except zeta, whose deposited
numbering is shifted by one (an extra N-terminal residue in the construct); the offset
is found by scanning rather than assumed, and all zeta residue numbers below are
reported in UniProt coordinates.

Sequence lengths verified: {'Q9NUS5': 200, 'Q3U829': 807, 'Q2VPB7': 878, 'Q96JI7': 2443, 'Q8BJ63': 490, 'P62743': 142}

## Q1 -- sigma-5 sits on the zeta trunk, and touches nothing else

Free solvent-accessible surface of the isolated sigma-5 chain: 11230.0 A^2.

| partner subunit | sigma-5 residues in contact | buried sigma-5 surface (A^2) | closest approach (A) |
|---|---|---|---|
| zeta5 (AP5Z1, mouse) | 60 | 2621.8 | 2.16 |
| beta5 (AP5B1, human) | 0 | 0.0 | - |
| SPG11 WD40-hairpin (spatacsin, human) | 20 | 755.4 | 1.52 |
| mu5 (AP5M1, mouse) | 0 | 0.0 | - |

* sigma-5 residues at the zeta5 (AP5Z1, mouse) interface: M1, V2, L24, F29, G30, A31, H41, A43, E44, D46, R47, L48, R50, K51, M64, L67, Q68, Q70, A71, S72, G73, R74, P75, R95, G96, A97, F98, R99, T111, L120, H129, N131, L132, L133, L134, E136, G137, L152, L153, A154, S156, T157, L160, L161, R162, A163, D164, E167, T171, P175, H176, G177, Q178, L179, L180, F181, N183, Q185, F186, W198
* sigma-5 residues at the SPG11 WD40-hairpin (spatacsin, human) interface: L20, R22, S34, R45, L48, L49, K51, E52, L55, A56, R59, Q60, S63, M64, L67, L100, A101, E103, N104, P105

The zeta N-terminal segment tested is UniProt residues 1-40. It contacts 9 sigma-5 residues (L24, L120, L152, L153, A154, S156, T157, L160, L161); the zeta residues involved are [1, 2, 3, 5, 6, 9, 10].

## Q2 -- the acidic dileucine site

The site is defined from 2JKR: the sigma2 residues within 4.5 A of the bound CD4 dileucine peptide (modelled sequence `MSQIKRLLS`). That gives 19 residues: N9, R10, A11, R15, Y62, A63, G64, L65, F67, H85, V88, E89, N92, N97, V98, C99, E100, L101, L103.

Superposition method: Bio.PDB.cealign.CEAligner (Combinatorial Extension, CA atoms, sequence-independent), reference 2JKR chain S (sigma2).

| superposed chain | RMSD (A) | reference CA positions covered within 4 A (of 142) |
|---|---|---|
| sigma-5 (8YAB chain C) | 3.66 | 135 |
| positive control: second sigma2 copy (2JKR chain I) | 0.03 | 142 |
| negative control: beta5 solenoid (8YAB chain B) | 6.82 | 113 |

Read the RMSD column, not the coverage column: beta5 is a 551-residue solenoid, so its
CA atoms are dense enough to fall within 4 A of most reference positions whatever the
fold. RMSD separates the three cases cleanly, and sigma-5 sits between the identical
control and the unrelated fold, which is what a divergent homologue should do.

| sigma2 pocket residue | nearest sigma-5 CA | CA-CA distance (A) | structurally equivalent | same residue | that sigma-5 position contacts the zeta N-terminus |
|---|---|---|---|---|---|
| N9 | T9 | 1.3 | True | False | False |
| R10 | L10 | 2.71 | True | False | False |
| A11 | C21 | 2.0 | True | False | False |
| R15 | Y25 | 1.81 | True | False | False |
| Y62 | V117 | 1.62 | True | False | False |
| A63 | L118 | 1.86 | True | False | False |
| G64 | S119 | 1.79 | True | False | False |
| L65 | L120 | 1.2 | True | True | True |
| F67 | F122 | 0.41 | True | True | False |
| H85 | R140 | 0.88 | True | False | False |
| V88 | T143 | 1.64 | True | False | False |
| E89 | R144 | 1.9 | True | False | False |
| N92 | D148 | 1.25 | True | False | False |
| N97 | R151 | 3.12 | True | False | False |
| V98 | R151 | 1.92 | True | False | False |
| C99 | L152 | 2.18 | True | False | True |
| E100 | S156 | 4.07 | False | False | True |
| L101 | S156 | 2.18 | True | False | True |
| L103 | L159 | 1.99 | True | True | False |

Summary: of 19 sigma2 residues that contact the dileucine peptide, 18 have a structurally equivalent position in sigma-5 (CA within 4 A after superposition), 3 of those carry the identical residue, and 3 of them are in contact with the zeta N-terminus in the assembled AP-5 core.

## Sequence control -- can this comparison be made from sequence alone?

| paralog | length | % identity over aligned columns | alignment score | shuffled mean +- sd | z |
|---|---|---|---|---|---|
| AP2S1 (sigma2) | 142 | 20.7 | -55.0 | -81.1 +- 13.2 | 1.98 |
| AP1S1 (sigma1A) | 158 | 27.3 | -32.0 | -68.9 +- 11.9 | 3.09 |
| AP1S2 (sigma1B) | 157 | 24.1 | -51.0 | -71.1 +- 15.2 | 1.32 |
| AP1S3 (sigma1C) | 154 | 21.8 | -40.0 | -72.8 +- 14.9 | 2.21 |
| AP3S1 (sigma3A) | 193 | 23.0 | -49.0 | -69.6 +- 15.0 | 1.37 |
| AP3S2 (sigma3B) | 193 | 24.3 | -60.0 | -67.4 +- 14.2 | 0.52 |
| AP4S1 (sigma4) | 144 | 15.3 | -63.0 | -78.3 +- 11.7 | 1.3 |

Every pairwise alignment of sigma-5 against a human sigma paralog scores negative and
sits within a few standard deviations of shuffled sequence, so the correspondence used
in Q2 could not have been obtained from pairwise sequence alignment. That is consistent
with Hirst et al. 2011 (PMID:22022230), who needed profile methods (HHpred, probability
96.8% against sigma2) rather than BLAST to recognise this protein as a sigma subunit --
and it is why the mapping above is done on structures.

## Conclusion

1. Sigma-5 is the zeta-adaptin partner: it buries 2621.8 A^2 against the zeta trunk over 60 residues, and touches neither beta5 nor mu5. Structurally it occupies the position that sigma1/sigma2/sigma3 occupy in AP-1/AP-2/AP-3.

2. Sigma-5 is also part of the SPG11 binding surface, burying 755.4 A^2 against the SPG11 WD40-hairpin over 20 residues. This is a role the other AP sigma subunits do not have, and it is the structural counterpart of the pull-down result that SPG11 associates with the zeta/sigma-5 subcomplex and is needed to assemble the AP-5 heterotetramer.

3. The fold that carries the acidic dileucine site is retained (18 of 19 peptide-contacting positions have a structural equivalent) but the chemistry is not: only 3 of those positions carry the same residue. The hydrophobic pocket linings and the basic patch are the positions that change, and in the assembled AP-5 core 3 of the equivalent positions are covered by the zeta N-terminus. Retention of the sigma fold is therefore not evidence that sigma-5 reads dileucine sorting signals, and the structure gives a positive reason to think it does not.

4. This is a structural argument, not a binding assay. No one has tested AP-5 against a dileucine motif, so the claim defended here is the negative one: nothing in the structure supports annotating cargo-signal recognition to sigma-5.

