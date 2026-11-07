# mtrH (MTH_1156, O27224) notes

Methanothermobacter thermautotrophicus Delta H, tetrahydromethanopterin
S-methyltransferase subunit H (Mtr step 6 of hydrogenotrophic methanogenesis).
Round 7 of the ARCHAEA project. Companion review: genes/METTH/mtrA1.

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no `-deep-research-*.md` file was made.
PubMed E-utilities searches: "mtrH AND methanogen"; "MtrA AND Methanothermobacter";
"methyltetrahydromethanopterin coenzyme M methyltransferase thermoautotrophicum".
Only one primary paper is about MtrH itself (Hippler & Thauer 1999, PMID:10338124,
abstract only). Also cached and read: PMID:38530900 (full text; AlphaFold2 models of
MtrH and the MtrAs-MtrH subcomplex), PMID:27324530 (full text), PMID:27342374,
PMID:7737157, PMID:8001564, PMID:11248186 (abstracts).

## Strain caution

The biochemistry is on strain Marburg (now Methanothermobacter marburgensis). Delta H
MtrH (O27224) is 97.1% identical (301/310, no gaps) to Marburg MtrH (P80187)
[file:METTH/mtrH/mtrH-bioinformatics/RESULTS.md]. The organism of the MtrH purification
is not stated in the cached abstract of PMID:10338124.

## Biology

- MtrH catalyses the first half-reaction, methyl transfer from methyl-H4MPT to the
  cob(I)amide of MtrA [PMID:10338124 "We report here that the 34 kDa subunit MtrH catalyzes
  the methylation reaction. MtrH was purified and shown to exhibit
  methyltetrahydromethanopterin:cob(I)alamin methyltransferase activity."].
- It is related to the methyltetrahydrofolate:corrinoid methyltransferases MetH and AcsE
  [PMID:10338124 "Sequence comparison revealed similarity of MtrH with MetH from Escherichia
  coli and AcsE from Clostridium thermoaceticum"], and has the dihydropteroate synthase-like
  TIM barrel (InterPro IPR011005, Gene3D 3.20.20.20; AlphaFold2 models, PMID:38530900).
- Mechanism of the whole complex: Co(I) nucleophilic attack on the N5-methyl of
  methyl-H4MPT, then demethylation of methyl-cob(III)amide by CoM (Na+-dependent)
  [PMID:8001564; PMID:11248186 "demethylation being sodium ion-dependent"]. The
  methylation half-reaction (MtrH) is therefore not the Na+-coupled step.
- MtrH is the only soluble subunit, peripherally attached on the cytoplasmic side and
  easily lost [PMID:38530900 "Soluble MtrH, hosting the binding site for methyl-H4MPT is
  cytoplasmically attached to the residual MtrABCDEFG complex and easily lost during
  preparation"; PMID:27342374 "selective removal of the only soluble subunit MtrH with the
  membrane perturbing agent dimethyl maleic anhydride"; PMID:27324530 "MtrH as a peripheral
  protein without a membrane anchor"]. No TRANSMEM feature in O27224.
- Modelled methyl-H4MPT site (M. marburgensis numbering): pterin at the bottom of the TIM
  barrel with conserved AspH102, AsnH128, AspH195, AsnH229 in H-bonding distance; MtrH is
  predicted to be a homodimer, like MtgA [PMID:38530900]. Delta H O27224 has D102, N128, D195,
  N229 at the same positions (gapless alignment, 310 aa both). These are AlphaFold2-based
  models, not experimental structures.
- MtrH is also proposed to interact with the N-terminal segment of MtrB (AlphaFold2,
  PMID:38530900).

## GO term for MtrH's own activity

OLS search: no GO term for methyl-H4MPT:corrinoid protein (cob(I)amide) methyltransferase.
The closest existing term is GO:0042086 "5-methyl-5,6,7,8-tetrahydromethanopterin-dependent
methyltransferase activity" (methyl transfer to an acceptor, dependent on methyl-H4MPT),
which is the parent of GO:0030269 and fits MtrH's half-reaction. Analogous specific terms
exist for the folate case (GO:0102036 methyltetrahydrofolate:corrinoid/iron-sulfur protein
methyltransferase activity). Rhea has no reaction for the MtrH half-reaction (searches for
CHEBI:58116 return only RHEA:21144, RHEA:53492 and RHEA:75867, the last being the
methoxydotrophic MtoC-type reaction, EC 2.1.1.384). Decision: core MF GO:0042086, plus a
proposed_new_terms entry for the specific half-reaction; whole reaction GO:0030269
(RHEA:53492) as contributes_to.

## Decisions

- GO:0006730 ACCEPT; GO:0019386 ACCEPT.
- GO:0008168 MODIFY -> GO:0042086.
- GO:0030269 MARK_AS_OVER_ANNOTATED (pattern 16).
- GO:0035725 MARK_AS_OVER_ANNOTATED: soluble subunit, catalyses the non-Na+-coupled
  half-reaction; inherits the transport claim only from the over-annotated GO:0030269 row.
- NEW GO:0044677 complex (ISS), NEW GO:0031234 extrinsic component of cytoplasmic side of
  plasma membrane (IC).
- No PANTHER cross-reference in O27224.
