# Srebf1 (rat, P56720) - manual literature synthesis

No deep-research API was available for this review. This file was written by the
reviewer from cached publications in `publications/` and the UniProt record
`Srebf1-uniprot.txt`. Every claim carries inline provenance.

## Identity and architecture

- Rat Srebf1 encodes sterol regulatory element-binding protein 1 (SREBP-1), 1134 aa
  (isoform SREBP-1A displayed; SREBP-1C/ADD1 differs at the N-terminus).
  The precursor has a cytoplasmic N-terminal transactivation/bHLH-ZIP region (bHLH
  domain 317-367, leucine zipper 367-388), two transmembrane helices (482-502,
  537-557) separated by a short lumenal loop, and a cytoplasmic C-terminal regulatory
  domain [Srebf1-uniprot.txt FT TRANSMEM/DOMAIN].
- Rat ADD1 was first cloned from an adipocyte cDNA library as a bHLH-leucine zipper
  factor [PMID:8336713 "we have identified a novel member of the bHLH-leucine zipper
  transcription factor family designated ADD1"] that "can function as a
  sequence-specific transcriptional activator" and activates through a binding site in
  the fatty acid synthase 5' flank [PMID:8336713].

## DNA binding and transcriptional activation

- ADD1/SREBP1 has dual DNA specificity [PMID:7739539 "ADD1/SREBP1 has dual DNA sequence
  specificity, binding to both an E-box motif (ATCACGTGA) and a non-E-box sequence
  previously shown to be important in cholesterol metabolism, sterol regulatory element
  1 (SRE-1; ATCACCCCAC)"]; it "activates transcription through both the carbohydrate
  response E-box element and SRE-1" [PMID:7739539]. An atypical tyrosine in the basic
  region controls SRE-1 recognition [PMID:7739539].
- In rat adipocytes, a dominant-negative ADD1 showed that obesity-related FAS
  overexpression is ADD1/SREBP-dependent, and in vitro binding showed SREBP2 can
  displace ADD1/SREBP1 from the FAS SRE [PMID:9786926].
- PCSK9 is an SREBP-1c target: a responsive element 335-355 bp upstream of the ATG was
  verified and dominant-negative SREBP-1c blunted insulin induction [PMID:16407292].
- In rat H4IIEC3 cells, nuclear SREBP-1c binds SRE / SRE-related sequences of
  lipogenic target genes, which honokiol inhibits [PMID:19371623].

## Activation by regulated proteolysis

- Nascent SREBP-1c sits in the ER membrane and moves to the Golgi in COPII vesicles for
  two sequential cleavages [PMID:19158095 "Nascent SREBP-1c is synthesized and embedded
  in the endoplasmic reticulum (ER) and must be transported to the Golgi in coatomer
  protein II (COPII) vesicles"].
- In rat hepatocytes insulin selectively stimulates SREBP-1c (not SREBP-2) processing by
  Akt-dependent phosphorylation of the precursor, which increases binding of the
  SCAP-SREBP-1c complex to Sar1-Sec23/24 [PMID:19158095].
- UniProt (by similarity to human/hamster): tight complex with SCAP in ER/Golgi;
  cleavage by MBTPS1 (lumenal loop) then MBTPS2 (first TM); nuclear form is
  proteasomally degraded [Srebf1-uniprot.txt CC SUBUNIT/PTM].
- PUFA suppress proteolytic release of SREBP-1 in rat liver [PMID:12421847]; DHA
  accelerates 26S-proteasome-dependent loss of nuclear SREBP-1 in rat hepatocytes
  [PMID:16222032]; central leptin impairs SREBP-1c maturation in rat WAT [PMID:18801905];
  ethanol (via acetaldehyde) increases mature SREBP-1 in rat hepatoma cells
  [PMID:12036955].

## Physiological regulation and role

- Rat hepatocytes: SREBP-1c transcription is induced by insulin and repressed by
  glucagon/cAMP; dominant-negative ADD1/SREBP-1c abolishes glucose induction of L-PK,
  FAS, S14 and ACC [PMID:10207099].
- LXR/RXR induce SREBP-1c transcription (mouse) [PMID:11090130]; insulin induces it via
  LXR and Sp1 (cultured hepatocytes) [PMID:24458133].
- Expression responses reported in rat: fructose feeding [PMID:11934685], progesterone
  in preadipocytes [PMID:11278421], retinoic acid in osteoblastic cells [PMID:9121491],
  fetal lung development [PMID:12896875], HIV protease inhibitors in muscle/liver
  [PMID:18171911], palmitate (down) in H4IIEC3 cells [PMID:19332540], NDGA (down) in
  high-fructose rat liver [PMID:26394137].
- Genetics: an SHR Srebf1 allele with reduced SREBP-1 expression protects against
  dietary hepatic cholesterol accumulation; congenic/transgenic correction restores it
  [PMID:18071061].

## Isoforms

- SREBP-1A: higher activity, cholesterogenic and lipogenic targets; SREBP-1C (ADD1):
  predominant, weaker, preferentially lipogenic [Srebf1-uniprot.txt CC FUNCTION, by
  similarity].
