# acs-1 (F46E10.1, WBGene00018488) - manual literature research

No deep-research API was available for this review. This file records a manual literature
search (PubMed queries `(acs-1[Title/Abstract] OR "ACS-1"[Title/Abstract]) AND elegans` and
`Kniazeva M[Author] AND Han M[Author]`) and reading of the cached publications. Provenance is
inline.

## Identity and family

- UniProt Q5TKA3 (unreviewed TrEMBL; 578 aa), gene acs-1, ORF F46E10.1, GeneID 179043,
  WormBase WBGene00018488 (isoform F46E10.1c / CE37772).
- Domains: AMP-dependent synthetase/ligase domain (Pfam PF00501, residues 29-422) and AMP-binding
  enzyme C-terminal domain (PF13193, residues 473-552); PROSITE PS00455 AMP-binding signature
  [file:worm/acs-1/acs-1-uniprot.txt "AMP-dependent synthetase/ligase"].
- PANTHER PTHR43201:SF5 "MEDIUM-CHAIN ACYL-COA LIGASE ACSF2, MITOCHONDRIAL", i.e. the ACSF2
  subfamily of ANL superfamily adenylate-forming enzymes. The UniProt protein name, EC 6.2.1.2 and
  the medium-chain/octanoate catalytic-activity lines all rest on ARBA rules only (ECO:0000256|ARBA),
  so they are predictions, not curated statements.
- Kniazeva et al. 2004 described ACS-1 as homologous to a very-long-chain FA CoA ligase
  [PMID:15340492 "ACS-1, very-long-chain FA CoA ligase"]. Zhang et al. 2011 (J Mol Biol) instead
  call it an acetyl-CoA synthetase [PMID:21704635 "The acs-1 gene encodes acetyl-CoA synthetase,
  which catalyzes the formation of acetyl-CoA from acetate and CoA"]; that statement is not
  supported by the domain/family assignment (acetyl-CoA synthetase is a different ANL subfamily)
  and is treated here as an error in that paper.
- No in vitro enzyme assay of ACS-1 has been published as far as this search found; the
  substrate range is inferred from genetics.

## Role in monomethyl branched-chain fatty acid (mmBCFA) synthesis

- Identified in a microarray screen for genes upregulated when the elongase ELO-5 is knocked down
  (mmBCFA-deficient worms) [PMID:15340492 "pnk-1, nhr-49, and acs-1 were upregulated in
  C17ISO-deficient elo-5(RNAi)"].
- acs-1 RNAi reduces mmBCFA levels [PMID:15340492 "RNAi of these two genes resulted in a
  significant loss in the mmBCFA fraction"].
- Kniazeva et al. 2008: "acs-1 encodes a very long-chain acyl-CoA synthetase that plays an
  essential role in mmBCFA biosynthesis and activation" [PMID:18676815]. acs-1(RNAi) worms given the
  precursor C13ISO remain C17ISO-deficient [PMID:18676815 "acs-1(RNAi) animals maintained with the
  C13ISO supplement (and therefore deficient for C17ISO)"], consistent with ACS-1 acting at a step
  that converts the shorter iso-FA into C17ISO (for example activation of the iso-FA to its CoA
  thioester for elongation by ELO-5), but the exact substrate is not demonstrated biochemically.
- acs-1 promoter is under feedback control by C17ISO levels; reporter expressed in intestine and
  CAN neurons [PMID:18676815 "An acs-1Prom∷GFP reporter is expressed in intestinal cells and
  canal-associated neurons (CAN) in L4 and adult animals"].
- Reviews from the same group list ACS-1 alongside BCKDH and ELO-5 as a key enzyme in de novo
  mmBCFA synthesis [PMID:23705068 "The key enzymes in this de novo synthesis pathway, including the
  branched-chain ketoacid dehydrogenase complex (BCKDC), an FA elongase (ELO-5), and an acyl CoA
  synthetase (ACS-1), are evolutionarily conserved"].

## Incorporation of C17ISO into phospholipids; embryonic and lipid-droplet phenotypes

- Kniazeva et al. 2012 (abstract only in cache): ACS-1 acting on C17ISO in the somatic gonad
  directs C17ISO into maternal phospholipids; loss causes defects in exocytosis/cytokinesis and
  early embryonic lethality suppressed by hyperactive IP3 signalling [PMID:22426533 "expression of
  ACS-1 in the somatic gonad guides the incorporation of C17ISO into certain phospholipids"].
- Zhang et al. 2021 (J Cell Biol, full text): acs-1 RNAi prevents intestinal lipid droplet growth,
  disrupts ER morphology, lowers C15iso/C17iso and TAG/PC/PE; dietary C17iso or C17iso-containing
  complex lipids rescue [PMID:34623380 "Dietary C17iso, or complex lipids with C17iso including
  phosphatidylcholine, phosphatidylethanolamine, and triacylglycerol, could fully restore the LD
  growth in the acs-1RNAi worms"]. These are downstream consequences of mmBCFA loss, not separate
  activities of ACS-1.
- Zhang et al. 2011 (klf-3 paper): acs-1 RNAi increases Oil Red O staining and causes reduced
  fertility, embryonic lethality and larval arrest [PMID:21704635]. The beta-oxidation
  interpretation in that paper is not supported by later work.

## Subcellular location

No subcellular localization data for ACS-1 were found. The ACSF2 subfamily name and ARBA
annotation imply mitochondria for the mammalian ortholog, but this is not tested in the worm.

## Summary

ACS-1 is an ANL-superfamily acyl-CoA synthetase (ACSF2 subfamily) that genetic data place in
monomethyl branched-chain fatty acid synthesis and in the channelling of C17ISO into membrane
phospholipids, in the intestine and somatic gonad. Its in vitro substrate specificity, and so the
chain-length class of its fatty acid-CoA ligase activity, has not been determined.
