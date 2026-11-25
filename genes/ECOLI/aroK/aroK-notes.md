# aroK (P0A6D7) – Escherichia coli K-12 shikimate kinase I

## Provenance of these notes

Provider deep research (`just deep-research`) was unavailable for this review (no provider
key in the session), so no `-deep-research-*.md` file exists. These notes are compiled by
hand from the cached publications, the UniProt record (`aroK-uniprot.txt`) and the PANTHER
family review (`interpro/panther/PTHR21087/PTHR21087-review.yaml`). Literature checked:
PMID:1309529, PMID:7883721, PMID:8682786, PMID:3001029, PMID:12001235, PMID:23526945 (full
text), PMID:27558633 (full text), PMID:25294881, PMID:15911532, PMID:18304323. PMID:3001029 and
PMID:12001235 were fetched for this review.

## Identity and activity

- aroK (formerly urf1) lies immediately upstream of aroB in an aroK-aroB operon. Its product
  was identified as shikimate kinase I genetically: an aroK aroL double mutant is aromatic
  auxotrophic, while single mutants are not
  [PMID:1309529 "The auxotrophic requirements of a strain mutant for both urf1 and aroL (encoding shikimate kinase II) are consistent with shikimate kinase deficiency. We propose that urf1 encodes shikimate kinase I and that it be designated aroK."].
- Corrected sequence: AroK and AroL are of comparable length and homologous along their whole length
  [PMID:7883721 "The corrected sequence alters the length of the aroK coding region such that the AroK and AroL proteins are now of comparable length and the homology between them extends the entire length of the two enzymes."].
- Purified AroK has shikimate kinase activity, with lower specific activity than AroL
  [PMID:27558633 "The specific activity of AroK was 18 μmol/(min.mg), which was much lower than that of AroL (61 μmol/(min.mg), as shown in Fig."].
- His6-SKI (AroK) was purified and used as an active SK reference; a BzdR-SKI chimera rescues an aroK aroL mutant
  [PMID:23526945 "indicating that Q1 was able to rescue the lack of SK activity in the mutant strain."].
- Kinetics: Km for shikimate about 20 mM, about 100-fold higher than AroL (Km 200 uM)
  [PMID:3001029 "The Km for shikimate is approximately 100-fold lower than the Km of shikimate kinase I, suggesting that shikimate kinase II is the isoenzyme normally functioning in aromatic biosynthesis."].
- Crystal structure of AroK (PDB 1KAG, monomer; PMID:12001235): P-loop NTPase fold with a LID
  domain; Walker A ATP/Mg(2+) site at residues 14-19 (UniProt, ECO:0000250).
- Expression: aroK is constitutive, whereas aroL is repressed by TyrR/TrpR. Hence AroK activity
  does not depend on aromatic amino acid levels
  [PMID:27558633 "In contrast to AroL, the activity of AroK in the cell is independent of both the amount of extracellular aromatic amino acids and the level of tyrR gene product67."].

## Physiological role: core or not?

- AroL is the dominant biosynthetic isozyme under aromatic limitation (low Km, inducible), but
  AroK is a genuine, dedicated shikimate kinase. It alone supports aromatic prototrophy in aroL
  mutants (only the double mutant is auxotrophic, PMID:1309529), and it is constitutively
  present. Shikimate kinase activity in chorismate biosynthesis is therefore core for AroK. Its
  high Km makes it a redundant, constitutive contributor rather than a promiscuous side activity.
- Second activity: an aroK insertion confers mecillinam resistance independently of shikimate
  kinase loss, of aromatic metabolite availability and of polar effects. An allele lacking SK
  activity still confers mecillinam sensitivity
  [PMID:8682786 "Instead, we conclude that the AroK protein has a second activity, possibly related to cell division regulation, which confers mecillinam sensitivity."]
  [PMID:8682786 "We were able to separate the AroK activities mutationally with an aroK mutant allele lacking shikimate kinase activity but still able to confer mecillinam sensitivity."].
  The resistance depends on ppGpp, and the insertion partially suppresses ftsZ84(Ts).
  The molecular nature of this second activity is unknown; there is no GO term to assign. This is
  a genuine biological knowledge gap.
- Protamine (cationic antimicrobial peptide) resistance: aroK is CpxR-dependent and contributes
  to protamine resistance, apparently through aromatic metabolites such as indole that stimulate
  Cpx-regulated genes
  [PMID:25294881 "aroK, a CpxR-dependent gene that encodes a shikimate kinase in the tryptophan biosynthesis pathway, was also found to facilitate protamine resistance."].
  This is an indirect, metabolite-mediated effect.

## Location

- Cytosolic: detected in cytosolic fractions (PMID:15911532, PMID:18304323); soluble, no signal
  peptide or TM segment.

## Curation conclusions (summary)

- Core: shikimate kinase activity (GO:0004765) in chorismate biosynthetic process (GO:0009423),
  in the cytosol.
- Cytoplasm IEA refined to cytosol. ATP and Mg(2+) binding are kept as non-core cofactor
  binding. Response to antibiotic is kept as non-core phenotype context.
