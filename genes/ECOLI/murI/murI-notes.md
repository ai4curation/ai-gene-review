# murI (P22634) curation notes

Escherichia coli K-12 MurI (glutamate racemase; synonyms dga, glr, yijA;
b3967, JW5550), 285 aa, aspartate/glutamate racemase family (HAMAP MF_00258,
TIGR00067, Pfam PF01177, PANTHER PTHR21198:SF2), cofactor-independent
two-cysteine (C92/C204 proton donor/acceptor) racemase.

No deep-research file was generated; notes compiled manually from cached
publications and UniProt. FEBA fitness data could not be fetched (no FEBA data
source reachable); murI is essential in media lacking D-glutamate.

## Function

- murI complements the only known D-Glu auxotroph (E. coli B/r WM335); depleted
  cells accumulate UDP-MurNAc-L-Ala and lyse
  [PMID:1355768 "Cells altered in the murI gene accumulate UDP-N-acetylmuramyl-L-alanine to a high level when depleted of D-glutamic acid."].
- Insertional mutagenesis shows murI is essential for D-glutamate synthesis;
  overproduced MurI has glutamate racemase activity
  [PMID:8098327 "The murI gene product was overproduced and identified as a glutamate racemase activity."].
- D-Glu is incorporated at position 2 of the stem peptide by MurD
  (UDP-MurNAc-L-Ala:D-Glu ligase); MurI is the sole route for D-Glu supply in
  E. coli.

## Regulation

- Purified MurI has an absolute in vitro requirement for UDP-MurNAc-L-Ala
  (the MurD substrate; KD 4 microM); no other precursor activates
  [PMID:8172902 "In vitro, the glutamate racemase activity shows an absolute requirement for UDP-N-acetylmuramoyl-L-alanine (UDP-MurNAc-L-Ala), the substrate of the D-glutamic acid-adding enzyme"].
  This feed-forward activation couples D-Glu formation to demand and avoids
  draining the L-Glu pool
  [PMID:8172902 "It adjusts the formation of D-glutamic acid to the requirements of peptidoglycan synthesis and avoids an excessive racemization of the intracellular pool of L-glutamic acid."].
- Crystal structure of E. coli MurI with D-Glu and UDP-MurNAc-L-Ala (PDB 2JFN)
  identifies the allosteric activator site; basal activity rises ~1000-fold with
  activator (UniProt ACTIVITY REGULATION, PMID:17568739)
  [PMID:17568739 "Here we describe three distinct mechanisms of regulation for the family of glutamate racemases: allosteric activation by metabolic precursors"].
  The E. coli enzyme is a monomer.

## Reported DNA gyrase inhibition (moonlighting) - judged peripheral

- Ashiuchi et al. 2002 reported that overproduction of E. coli MurI lowered
  plasmid copy number and supercoiling, and that MurI modulated E. coli DNA
  gyrase in vitro in the presence of UDP-MurNAc-L-Ala
  [PMID:12213801 "we found that the DNA gyrase of E. coli was modulated by the glutamate racemase of E. coli in the presence of UDP-N-acetylmuramyl-l-alanine"].
- Similar gyrase inhibition is better characterized for mycobacterial MurI,
  where it is independent of racemization [PMID:18757813].
- Judgement: for E. coli the evidence is a single study relying on
  overexpression and in vitro effects, with no follow-up showing a
  physiological gyrase-regulatory role at native MurI levels. GOA has no row for
  it and no NEW annotation is proposed; it is recorded as a suggested question.

## Annotation decisions

- GO:0008881 glutamate racemase activity: core MF (ACCEPT EXP/IDA/IBA/IEA).
- GO:0009252 peptidoglycan biosynthetic process: ACCEPT (MurI catalyses the
  D-Glu-producing step that feeds MurD).
- GO:0016855 and GO:0047661: correct but general ancestors of GO:0008881 -> MODIFY.
- GO:0005515 with TufA (EF-Tu) from a large-scale TAP/MS screen -> REMOVE
  (uninformative; EF-Tu is a highly abundant co-purifying protein).
- No CC annotation exists. MurI is a soluble cytoplasmic enzyme by structure
  and substrate location, but no direct localization assay was found; no NEW
  CC row is added.

## Module consistency

modules/d_amino_acid_cell_wall_precursor_supply.yaml murI_glutamate_racemase
annoton: family PANTHER:PTHR21198:SF2 (GLUTAMATE RACEMASE), GO:0008881,
GO:0009252, representative only PSEPK Q88PW2. P22634 is in the same
PANTHER subfamily (UniProt DR PANTHER PTHR21198:SF2) and is the experimentally
characterized enzyme (activity, kinetics, activator structure), so it would be a
good additional representative. The annoton function and process match this
review's core function.
