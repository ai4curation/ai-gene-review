# arg11 (SPAC4G9.09c, UniProt P31318) notes

## Naming trap
- S. pombe arg11 = ARG5,6-type acetylglutamate kinase / NAGSA reductase polyprotein. S. cerevisiae ARG11 = ORT1 mitochondrial ornithine carrier (different protein).

## Evidence
- Van Huffel et al. 1992 (abstract only): [PMID:1313366 "The acetylglutamate kinase and acetylglutamate-phosphate reductase domains have been defined by their identity with the S. cerevisiae ARG5,6 protein."]; cloned by complementation [PMID:1313366 "were cloned by functional complementation of S. pombe arg3 and"]; no cross-complementation [PMID:1313366 "The cloned arg11 gene from S. pombe does not complement an arg5,6 mutation in S. cerevisiae"].
- UniProt cites EC 2.7.2.8 and EC 1.2.1.38 with ECO:0000269 from PMID:1313366; transit peptide 1..59; chains 60..550 (kinase) and 551..885 (reductase) [UniProt:P31318 "PTM: The protein precursor is probably cleaved into the two"]; [UniProt:P31318 "ACTIVITY REGULATION: The kinase activity is inhibited by arginine."].
- GO-CAM gomodel:6690711d00000916 models both activities (GO:0003991, GO:0003942) in mitochondrial matrix.

## Decisions
- All experimental rows accepted (deferred to curator, full text not cached).
- Cytoplasm (InterPro2GO) MODIFY -> matrix; NAD binding over-annotated (NADP enzyme); generic BPs/MF MODIFY.
- No NAGS/NAGK complex added: no S. pombe evidence (ARG5,6 has IPI in budding yeast) - raised as suggested question.
