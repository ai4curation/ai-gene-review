# rft-2 (C. elegans, Y47D7A.14, UniProt G4SDH4) - manual literature research

No deep-research provider API keys were available in this session, so this
summary was compiled manually from the cached publications and the UniProt record.

## Identity and family

- RFT-2 is a 476-aa (isoform b) multi-pass membrane protein of the SLC52 /
  riboflavin transporter (RFVT) family (Pfam PF06237, InterPro IPR009357,
  PANTHER PTHR12929:SF10) [file:worm/rft-2/rft-2-uniprot.txt].
- It is one of two tandemly arranged C. elegans orthologs of human RFVT3
  (SLC52A3) [PMID:23483992 "Two potential orthologs of the human riboflavin
  transporter 3 (hRFVT3) were identified in the C. elegans genome, Y47D7A.16 and
  Y47D7A.14, which share 33.7 and 30.5% identity, respectively, with hRFVT3"].
- C. elegans cannot synthesise riboflavin [PMID:23483992 "Like humans, the
  nematode C. elegans lacks the biosynthetic machinery necessary to synthesize
  riboflavin, being dependent solely upon dietary uptake"].

## Transport activity (direct evidence)

- rft-2 cDNA expressed in ARPE-19 cells increased [3H]riboflavin uptake
  [PMID:23483992 "In a separate experiment with three trials, rft-2 transfected
  cells also had significantly higher riboflavin uptake compared to controls"].
- Both proteins were described as specific riboflavin transporters, with RFT-1
  more active; detailed kinetics (Km 1.4 uM, acidic pH dependence,
  Na+-independence) were measured for RFT-1 only [PMID:23483992 "both were
  specific riboflavin transporters, although the rft-1 encoded protein had
  greater transport activity"].

## Expression and regulation

- rft-2 promoter::mCherry is expressed in the intestine and pharynx
  [PMID:23483992 "Expression of rft-2 is localized mainly to the intestine and
  pharynx"].
- rft-2 mRNA is up-regulated under riboflavin deficiency and down-regulated by
  supplementation [PMID:25963255 "Abundance of rft-2 transcript was upregulated in
  riboflavin-deficient conditions (10 nM), while it was downregulated with
  riboflavin-supplemented conditions (2 mM)"] (abstract only).

## Phenotype

- RNAi knockdown reduces egg laying/fertility, more strongly when combined with
  rft-1 RNAi, and riboflavin supplementation partially rescues the double
  knockdown [PMID:23483992 "Knocking down the two transporters individually via
  RNA interference resulted in a severe loss of fertility that was compounded in a
  double knockdown"]. This is a consequence of riboflavin deficiency, not a
  direct reproductive role.

## Subcellular location

- Not determined experimentally for RFT-2 (only transcriptional reporters were
  used). UniProt infers cell membrane by similarity (ECO:0000305); human RFVT3 and
  RFVT1/2 are plasma membrane transporters. An apical intestinal location is
  plausible but unshown.

## UPR

- The HEP annotation to IRE1-mediated UPR comes from the genome-wide microarray
  study PMID:16184190; rft-2/Y47D7A.14 is not named in the main text. This
  indicates transcriptional responsiveness only.
