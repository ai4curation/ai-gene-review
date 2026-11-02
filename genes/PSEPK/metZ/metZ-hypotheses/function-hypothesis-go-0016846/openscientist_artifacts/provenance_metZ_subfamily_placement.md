# Provenance: metZ (Q88LD4) subfamily placement & active site

## Needleman-Wunsch pairwise %identity vs Q88LD4 (query)
(scoring match +2 / mismatch -1 / gap -6; identity over aligned columns)

  82.1%  MetZ_Paeruginosa P55218  O-succinylhomoserine sulfhydrylase (transferase EC2.5.1.-) [characterized]
  38.0%  MetB_Ecoli      P00935  cystathionine gamma-synthase (transferase EC2.5.1.48)
  36.5%  CTH_human       P32929  cystathionine gamma-lyase (C-S lyase EC4.4.1.1) = PANTHER SF80 label
  25.0%  MetC_Ecoli      P06721  cystathionine beta-lyase (C-S lyase EC4.4.1.8)

## UniProt Q88LD4 (HAMAP MF_02056, MetZ subfamily)
- Recommended name: O-succinylhomoserine sulfhydrylase; EC 2.5.1.-
- Reaction: O-succinyl-L-homoserine + H2S -> L-homocysteine + succinate
- Cofactor: pyridoxal 5'-phosphate; Modified residue K219 = N6-(PLP)lysine (catalytic, intact)
- Pathway: L-methionine biosynthesis, L-homocysteine from OSHS, step 1/1

## QuickGO annotations (Q88LD4)
- GO:0016765 transferase activity (alkyl/aryl)  [UniRule UR000282477]   <-- branch-correct MF
- GO:0016846 carbon-sulfur lyase activity        [PANTHER PTN002273776, GO_REF:0000118] <-- disputed graft
- GO:0030170 PLP binding; GO:0019346 transsulfuration; GO:0071266 de novo Met biosynth; GO:0005737 cytoplasm

## GO:0016846 definition (OLS): "Catalysis of the elimination of hydrogen sulfide or substituted H2S."
  -> opposite direction to metZ (nets ADDITION of sulfide).

## Literature
- PMID 7704274 (Foglino 1995): metZ = direct sulfhydrylation of O-succinylhomoserine (P. aeruginosa).
- PMID 10482527 (Vermeij & Kertesz 1999): P. putida uses direct sulfhydrylation; NO cystathionine gamma-lyase present.

## Conclusion
Wrong-subfamily mis-placement. metZ is a transferase (sulfhydrylase), not a carbon-sulfur lyase.
GO:0016846 should be removed/replaced with a transferase-branch term (retain GO:0016765).

## Catalytic PLP-lysine conservation (Iteration 2)
Canonical transsulfuration Schiff-base Lys motif [S/A]-A-T-K-[F/Y]:
  Q88LD4 metZ   : SATKF @ K219   (query; matches UniProt Modified-residue feature)
  P55218 Pa MetZ: SATKY @ K219   (characterized sulfhydrylase - identical position)
  P00935 MetB   : C TKY @ ~198
  P32929 CTH    : SATKY @ ~212
  P06721 MetC   : A TKY @ ~210
=> Catalytic lysine present and correctly spaced in the query -> active site INTACT (not a pseudo-enzyme).
   Note: this Lys is shared by the whole family, so it confirms catalytic competence but does NOT by
   itself distinguish transferase (sulfhydrylase) from lyase; that distinction rests on the 82% identity
   to characterized MetZ sulfhydrylase and the curated EC 2.5.1.- reaction.
