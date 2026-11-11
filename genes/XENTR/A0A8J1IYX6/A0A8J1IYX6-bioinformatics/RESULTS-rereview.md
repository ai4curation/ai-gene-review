# A0A8J1IYX6 (LOC101732819) — AGC kinase placement, re-review 2026-10-21

Scripts: `compare_agc_rereview.py` (pairwise local alignment, output
`compare_agc_rereview.out.txt`) and `tree_agc_rereview.py` (MAFFT + p-distance
neighbour-joining, outputs `tree_agc_rereview.out.txt`,
`tree_agc_rereview_excl_Q96LW2.out.txt` and the two `.nwk` files). Sequences are
fetched live from UniProt REST.

## 1. PANTHER family scope

PANTHER PTHR24351 ("RIBOSOMAL PROTEIN S6 KINASE") is a broad AGC-kinase family.
Its member list (`interpro/panther/PTHR24351/PTHR24351-entries.csv`) contains the
human S6Ks and RSKs/MSKs, but also all PKC isoforms (PRKCA, PRKCB, PRKCG, PRKCD,
PRKCE, PRKCH, PRKCQ, PRKCI, PRKCZ), PKN1-3, AKT1-3 and SGK1-3. Membership in
PTHR24351 therefore does not place the protein outside the PKC group.
The InterPro API assigns the target to PTHR24351 (residues 42-416, E=1e-110) with
no subfamily (:SF) assignment.

## 2. Pairwise identity (target residues 105-424 vs comparators)

Best matches are the novel PKCs: PRKCQ 42.7% (279 columns), X. tropicalis prkcq
40.5%, X. tropicalis prkcd 41.7%, human PRKCD 41.0%. Then come the other PKCs
(36-38%), AKT1 38.4%, SGK1 34.9%, PKN1 37.1%, RSK1 33.2%, S6K1 35.1%, PKA 36.7%.
For calibration, a true vertebrate ortholog pair (human PRKCD 345-676 vs
X. tropicalis prkcd A0A6I8SIW5) gives 88.5% identity over 330 columns.

So the target's catalytic region is PKC-like (consistent with the
FunFam 1.10.510.10:FF:000048 "Protein kinase C" match) but is far too divergent
to be an ortholog of PRKCD or PRKCQ, both of which X. tropicalis already has
as separate genes.

## 3. Neighbour-joining placement

With all comparators, the target groups with human RSKR (SGK494, Q96LW2). RSKR is
classified by PANTHER in a different family (PTHR24355), and both sequences
have long branches, so this pairing is read as long-branch attraction rather than
a real relationship. With RSKR excluded, the target branches at the base of the
PKC + PKN clade (smallest clade containing it: PRKCA, PRKCD, PRKCE, PRKCH,
PRKCQ, PRKCI, PRKCZ, PKN1 and the two frog novel PKCs). It sits outside the
PKCdelta and PKCtheta ortholog clades, each of which pairs a frog with a human
sequence. The tree is unbootstrapped and only a rough placement: it puts the
target in the PKC/PKN superclade but resolves no closer relative.

## 4. Residue observations (local alignment to PRKCD)

- PRKCD K378 (beta-3 ATP lysine) maps to target K142 (UniProt BINDING 142).
- The HRD catalytic Asp (target D235) and DFG Asp (target D253) are retained
  (motifs IHRDLKPDN 232-240 and ICDFG 251-255).
- PRKCD activation-loop phosphorylation site T507 (in TFCGTPDY) maps to target
  **G269** (in LAGTPGY). The PDK1-type activation-loop phospho-acceptor Thr is
  therefore absent. The protein may have lost the usual PDK1-dependent activation
  step, or be weakly active. This is a sequence observation; nothing has been
  tested.
- The AGC C-terminal tail (367-424) has no recognisable FxxF(S/T)(F/Y)
  hydrophobic motif. The local alignment to PRKCD stops at PRKCD residue 624,
  so the PRKCD turn-motif and hydrophobic-motif region (after residue 624) has
  no aligned counterpart in the target.

## Conclusion

A0A8J1IYX6 is a complete (not fragmentary) 424-aa gene product. It has a
PKC-superclade-like AGC catalytic domain with the catalytic machinery retained,
but it is divergent, has no C1/C2 regulatory domains, and lacks the
activation-loop phospho-Thr. It is a distinct gene from X. tropicalis prkcd and
prkcq, not an isoform or gene model of either. Its function can only be inferred
at the level of protein Ser/Thr kinase activity.
