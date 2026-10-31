# Msed_1456 (A4YGR1, HPCAS_METS5) notes

Automated deep research was unavailable for this gene. These notes come from
manual literature research (NCBI E-utilities searches, the full-text cached
publications listed below, and the UniProt record).

## Identity

- Msed_1456 is 3-hydroxypropionyl-CoA synthetase (HPCS), EC 6.2.1.36, 661 aa,
  an AMP-forming acyl-CoA synthetase (ANL superfamily; UniProt "Belongs to the
  ATP-dependent AMP-binding enzyme family"). InterPro places it in the
  acetyl-CoA ligase family (IPR011904, TIGR02188 Ac_CoA_lig_AcsA) and PANTHER
  PTHR24095 (acetyl-coenzyme A synthetase), which is why acetyl-CoA synthetase
  terms are propagated to it.
- Identified by purification of the native enzyme from autotrophically grown
  *M. sedula* and an internal peptide [PMID:18165310 "Based on the internal peptide sequence determined for purified 3-hydroxypropionyl-CoA synthetase, a gene was identified in the genome of M. sedula which codes for a protein with an internal sequence that is a 100% match for the determined peptide sequence."].

## Activity and substrate specificity

- Reaction [PMID:18165310 "The first enzyme, 3-hydroxypropionyl-CoA synthetase, catalyzes the following reaction: 3-hydroxypropionate + ATP + CoA → 3-hydroxypropionyl-CoA + AMP + PP i ."].
- Kinetics [PMID:18165310 "The enzyme had a high affinity for ATP and 3-hydroxypropionate, with apparent K m values of 45 μM for ATP and 180 μM for 3-hydroxypropionate."].
- Specificity: 3HP and propionate are equivalent; acrylate ~10-fold lower
  kcat/Km; acetate and butyrate only weakly used, attributed to low affinity
  [PMID:18165310 "The specificities ( k cat / K m ) of the enzyme with respect to 3-hydroxypropionate and propionate were similar but were decreased about 10-fold for acrylate (Table 4 )."]
  [PMID:18165310 "The enzyme, therefore, is specific for 3-hydroxypropionate and propionate."].
- Independent comparison by Hawkins et al. [PMID:23258541 "Similarly, Msed_1456, which catalyzes the ligation of CoA to 3HP in the 3HP/4HB pathway, has equal activity on propionate and 3HP, and therefore it might have residues in the active site that help stabilize the hydroxyl group of 3HP."].
- The *M. sedula* acetate-activating enzyme is a different paralog, Msed_1353
  [PMID:23258541 "Msed_1353 was active on propionate and acetate, but not on 4HB."].
  This, plus the weak acetate affinity of Msed_1456, makes the acetyl-CoA
  synthetase activity and acetyl-CoA biosynthesis IEA rows family-level
  over-annotation (ARCHAEA pattern 1-like: a substrate-diverged ANL member
  inheriting the family-founder name).
- Homotetramer of 78 kDa subunits [PMID:18165310 "3-Hydroxypropionyl-CoA synthetase, therefore, exists as a homotetramer."].
- Induced under autotrophy [PMID:18165310 "3-Hydroxypropionyl-CoA synthetase is up-regulated eightfold in autotrophically versus heterotrophically grown M. sedula , supporting its proposed role during CO 2 fixation in this archaeon and possibly other members of the Sulfolobaceae family."].

## Pathway

- Activates 3-hydroxypropionate, the first committed step of the reductive
  conversion 3HP -> 3HP-CoA -> acryloyl-CoA -> propionyl-CoA, in the first half of
  the 3HP/4HB cycle. Acetyl-CoA is regenerated in the second half via
  4-hydroxybutyrate [PMID:18079405 "This intermediate was reduced to 4-hydroxybutyrate and converted into two acetyl-CoA molecules via 4-hydroxybutyryl-CoA dehydratase."].
  Msed_1456 itself does not produce acetyl-CoA.
- GO:0043427 "carbon fixation by 3-hydroxypropionate cycle" (OLS, checked
  2026-10-31): "An autotrophic carbon dioxide fixation pathway by which two
  molecules of carbon dioxide are fixed to form glyoxylate ... Malyl-CoA is
  thought to be cleaved to acetyl-CoA, the starting molecule, and glyoxylate".
  This is the *Chloroflexus* pathway; *M. sedula* lacks malyl-CoA lyase
  [PMID:18165310 "l -Malyl-CoA lyase activity was not detected in cell extracts of M. sedula ( 14 )."].
  No GO term for the 3HP/4HB cycle exists (OLS search). Following the
  Msed_0709 review, the IDA/IEA GO:0043427 rows are MODIFIED to the NTR
  "carbon fixation by 3-hydroxypropionate/4-hydroxybutyrate cycle" plus
  GO:0015977 carbon fixation. The activity evidence of the IDA is sound.
- Recombinant *M. sedula* HPCS is insoluble alone in *E. coli*; it is
  soluble only when co-expressed with 3HP-CoA dehydratase Msed_2001, and the
  two interact in yeast two-hybrid
  [PMID:27771364 "Only when both enzymes were co-expressed in E. coli could HPCS be obtained in soluble, active form"]
  [PMID:27771364 "The results demonstrate that HPCS and HPCD interact in vivo in yeast, although there is no evidence of interaction between ACR and SSR (Figure 2)."].
  Possible substrate channelling; not annotated (Y2H only).

## Other

- PMID:27722922 and PMID:27300329 (engineering of part of the cycle in
  E. coli / in vitro) were cached but are not used; 27722922 is abstract-only.
