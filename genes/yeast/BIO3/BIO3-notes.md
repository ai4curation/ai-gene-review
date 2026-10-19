# BIO3 (YNR058W, P50277) notes

## Identity
- Adenosylmethionine-8-amino-7-oxononanoate aminotransferase (DAPA aminotransferase, BioA), EC 2.6.1.62; class-III PLP-dependent aminotransferase, BioA subfamily; 480 aa, single Aminotran_3 (PF00202) domain, PANTHER PTHR42684 [UniProt:P50277].
- Uses SAM as amino donor to convert KAPA (8-amino-7-oxononanoate) to DAPA [UniProt:P50277 "It is the only aminotransferase known to utilize SAM as an amino donor"].
- Clustered with BIO4 (DTBS) and BIO5 (KAPA/DAPA permease) on chromosome XIV [PMID:10333520 "This mutant allowed the characterization of a bio cluster (BIO3-4-5)."].

## Evidence
- [PMID:10333520 "We demonstrate that BIO3 (YNR058w) and BIO4 (YNR057c) encode, respectively, a 7, 8-diaminopelargonic acid aminotransferase and a dethiobiotin synthase, involved in the biotin biosynthesis pathway."] (abstract only in cache).
- S288C is a biotin auxotroph lacking the BIO1/BIO6 pimeloyl branch; biotin prototrophy genes were reacquired by HGT and gene duplication (Hall & Dietrich 2007, PMID:18073433; web search, not cached).

## PAINT issue
- IBA "dethiobiotin synthase activity" and "mitochondrion" come from PANTHER node PTN000241344 (taxon Eukaryota) seeded only by Arabidopsis AT5G57590 (BIO1), a mitochondrial bifunctional BioD-BioA fusion. Yeast Bio3 has no BioD domain; yeast DTBS is the separate BIO4 product. The DTBS IBA is a domain-architecture mismatch. The repo's PANTHER_IBA_REVIEW losses table lists an IRD for GO:0005739 below PTN000241344 (loss node PTN001736499), so PAINT already recognises the mitochondrion assertion does not hold across the clade.
