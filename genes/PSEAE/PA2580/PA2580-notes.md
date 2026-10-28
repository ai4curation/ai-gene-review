# PA2580 (Q9I0Q6, MdaB) notes

## Identity

- UniProt Q9I0Q6, unreviewed, 196 aa; locus PA2580, no gene name in the
  entry. Name "NADPH:quinone oxidoreductase MdaB", EC 1.6.5.10, FAD cofactor,
  homodimer and cytoplasm are all ARBA-predicted, not curated. Domain: Pfam
  PF02525 Flavodoxin_2 (flavodoxin-like fold, 2-188); InterPro IPR052397
  NADPH-QR_MdaB; PANTHER PTHR46305:SF3 (NADPH:quinone oxidoreductase MdaB).
  No TM segment or signal peptide.

## Literature

- Green et al. 2014 (PMID:25085734; abstract only, J Microbiol, not in PMC):
  the P. aeruginosa MdaB orthologue (PA2580), purified with four other
  quinone reductases, reduces quinones by two-electron transfer
  [PMID:25085734 "In in vitro assays, each enzyme was shown to reduce quinone
  substrates with only minimal semiquinone formation."]. Overexpression gave
  no H2O2 protection in wild type [PMID:25085734 "However, when each was
  individually over-expressed in P. aeruginosa no overt H2O2-protective
  phenotype was observed."], but did in a katA mutant [PMID:25085734 "in a
  katA mutant, H2O2 challenged strains over-expressing the WrbA and MdaB
  orthologs grew significantly better than the empty plasmid control."]. No
  PA2580 loss-of-function mutant is reported in the abstract.
- Helicobacter pylori MdaB (HP_0630, a PTN002922793 leaf): knockout is
  sensitive to O2, H2O2, organic hydroperoxides and paraquat and colonises
  mice poorly; the purified enzyme is an NADPH-preferring two-electron quinone
  reductase [PMID:14977943 "The mdaB mutant is also more sensitive to H(2)O(2),
  organic hydroperoxides, and the superoxide-generating agent paraquat.";
  "preferably uses NADPH as an electron donor"]. H. hepaticus MdaB mutant is
  likewise oxidative-stress sensitive [PMID:17923370 "The mdaB mutant was also
  more sensitive to oxidative stress reagents such as H(2)O(2), cumene
  hydroperoxide, t-butyl hydroperoxide, and paraquat."].
- E. coli MdaB (P0AEY5, the other MF seed): FAD flavoprotein of the
  DT-diaphorase type; a null mutant is not menadione-sensitive, and the
  authors favour protection against polyketides [PMID:16630630 "This work
  suggests that the redox cycle formed by these proteins protects E. coli from
  the toxic effects of polyketide compounds rather than the oxidative stress of
  menadione alone."].

## Participation test

MdaB itself catalyses the two-electron reduction of quinones, which is the
step that avoids semiquinone-driven ROS production; so a role in the
oxidative stress response is participation, not just a downstream phenotype.
For P. aeruginosa the evidence is weak (gain of function in a katA background
only; no effect in wild type), but for the clade the claim is independently
supported by knockout phenotypes in H. pylori and H. hepaticus MdaB. The E.
coli null result is a caveat, not a contradiction. The PseudoCAP MF row is
right in substance but rests on in vitro enzyme assays, which are IDA, not
IMP.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002922793 | GO:0034599 cellular response to oxidative stress | 1 (sole) | 9 (8 taxa) | GO:0034599, IMP, PMID:25085734 (PseudoCAP) | SOUND | Seed is weak (overexpression protects only a katA mutant; no wild-type or loss-of-function phenotype), but MdaB does the protective chemistry itself, and the term holds for the clade on independent knockout evidence from H. pylori HP_0630 (PMID:14977943), a leaf of the node and a better seed. |
| PTN002922793 | GO:0003955 NAD(P)H dehydrogenase (quinone) activity | 2 | 9 (8 taxa) | GO:0003955, IMP, PMID:25085734 (PseudoCAP) | SOUND | Purified enzyme reduces quinones (two-electron); the right evidence code is IDA, not IMP. Second seed E. coli MdaB. |

## Decisions summary

- ACCEPT: NAD(P)H dehydrogenase (quinone) activity (IBA, IMP), cytosol (IBA).
- MODIFY: catalytic activity (IEA) to GO:0003955; cytoplasm (IEA) to cytosol.
- UNDECIDED: NADPH dehydrogenase (quinone) activity (IEA from EC 1.6.5.10):
  the PA enzyme's NADPH preference is not in the abstract.
- KEEP_AS_NON_CORE: cellular response to oxidative stress (IBA, IMP).
- PSEUDOCAP defect: MF row evidence code IMP should be IDA.
