# Gnmt (rat, P13255) - manual literature synthesis

No deep-research provider API keys were available for this session, so this
summary was compiled by hand from the cached publications in `publications/`
and the UniProt record (`Gnmt-uniprot.txt`). Every claim carries inline
provenance.

## Identity and structure

- Rat glycine N-methyltransferase, 293 aa (Met1 removed), class I-like
  SAM-dependent methyltransferase fold, GNMT family (PANTHER PTHR16458; InterPro
  IPR014369) [file:rat/Gnmt/Gnmt-uniprot.txt "Belongs to the class I-like SAM-binding methyltransferase superfamily"].
- Homotetramer [PMID:22037183 "GNMT is a tetramer of identical 32 kDa subunits."].
  In the closed structure the N-terminal segment of one subunit corks the active
  site of the neighbour; this gives auto-inhibition at low AdoMet and forces out
  the product AdoHcy [PMID:10756111 "The N-terminal section of the adjacent subunit occupies the AdoMet binding site and thus inhibits the methyltransfer reaction"].
- Arg175 binds glycine; catalysis is an SN2 attack of the glycine amino N on the
  SAM methyl [PMID:12859184 "The second substrate Gly binds to Arg175 and is brought into the Gly pocket."].

## Catalytic activity

- SAM + glycine -> SAH + sarcosine (EC 2.1.1.20) [PMID:12859184 "Glycine N-methyltransferase (GNMT) catalyzes the S-adenosyl-l-methionine- (SAM-) dependent methylation of glycine to form sarcosine."].
- KM 36 uM (SAM), 0.43 uM (glycine) per UniProt citing PMID:12859184.
- kcat rises from rat to mouse to human enzyme [PMID:15340920 "There is an increase in kcat when going from rat to mouse to human"].

## Physiological role: SAM disposal / SAM:SAH ratio

- [PMID:18501206 "is an important regulatory enzyme, which serves to remove excess S-adenosylmethionine, the universal methyl donor in the cell, by the methylation of glycine"].
- [PMID:10756111 "These properties of GNMT are particularly suited for regulation of the cellular AdoMet/AdoHcy ratio."].
- Retinoids raise hepatic GNMT activity ~2-fold in male rats and reduce
  SAM-dependent creatinine synthesis [PMID:12054489 "retinoid compounds significantly elevated hepatic GNMT activity and abundance"].
- Betaine supplementation of ethanol-fed rats upregulates hepatic cytosolic GNMT
  together with BHMT and MAT1 [PMID:19239903 "Significant upregulation of betaine homocysteine methyltransferase-1, methionine adenosyl transferase-1, and glycine N-methyltransferase"].
  This is expression evidence only.

## Folate binding and regulation

- GNMT is the rat liver cytosolic folate-binding protein II [PMID:6587377 "Purification of glycine N-methyltransferase resulted in the separation of two enzyme species, one that contained bound folate and one that did not."].
- 5-methyltetrahydrofolate pentaglutamate is a specific, potent inhibitor [PMID:3838667 "is bound with high specificity, and is a powerful inhibitor of the enzyme"].
- Two folates per tetramer at intersubunit sites [PMID:17158459 "In the GNMT-folate complex, two folate binding sites were located in the intersubunit areas of the tetramer."].
- N-acetylation of Val1 in native enzyme makes folate inhibition far more potent
  without changing binding [PMID:18501206 "The native, N-acetylated form of the enzyme shows 50% inhibition at 1.3 microM concentration of the pentaglutamate while the recombinant non-acetylated form shows 50% inhibition at 590 microM."];
  structural basis in extra hydrogen bonds [PMID:22037183 "In the folate-recombinant GNMT complex only one hydrogen bond is established."].

## Location and tissue distribution

- Liver cytosol [PMID:6587377]; periportal hepatocytes, kidney proximal tubules,
  exocrine pancreas, submaxillary striated ducts, jejunal villus epithelium, and a
  nuclear pool in liver [PMID:8278367 "Close examination of the liver indicated GNMT in the nucleus; this site was confirmed by purification of the nuclei and measurement of enzyme activity."].

## Secondary activity

- Reactome (rat) includes Gnmt among methyltransferases demethylating
  Se-adenosylselenomethionine [Reactome:R-RNO-2408545 "remove a methyl group from adenosylselenomethionine (AdoSeMet) to leave adenosylselenohomocysteine (AdeSeHCys)"].
