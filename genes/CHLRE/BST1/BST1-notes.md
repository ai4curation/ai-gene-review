# BST1 (Chlamydomonas reinhardtii) review notes

UniProt A0A2K3CTN0 (TrEMBL, "Uncharacterized protein"); locus Cre16.g662600 / CHLRE_16g662600v5.
Paralogs (KEGG `conv/uniprot` mapping, 2026-10-03; UniProt REST returned 503 at the time):
BST2 = Cre16.g663400 -> A0A2K3CTQ2; BST3 (LCI11) = Cre16.g663450 -> A0A2K3CTP3.

## Deep research

`scripts/deep_research_wrapper.py CHLRE BST1 falcon --fallback perplexity-lite` was run once
(2026-10-03): falcon returned HTTP 402 Payment Required, and the perplexity-lite fallback
failed because the perplexity provider is not available. No deep-research file exists; the
review is built from the primary literature below.

## Identity and family

- Bestrophin / YneE / VCCN family (InterPro IPR044669, Pfam PF25539 Bestrophin_2,
  PANTHER PTHR33281:SF19), per UniProt record. Closest land-plant homolog is Arabidopsis
  VCCN1 (~30% identity) [PMID:31391312 "The most similar protein in terrestrial plants, the
  thylakoid localized AtVCCN1 protein of Arabidopsis (17), has approximately a 30% sequence
  identity with BST1–3."]
- Three paralogs clustered on chr 16 [PMID:31391312 "BST1 (Cre16.g662600), BST2
  (Cre16.g663400), and BST3 (Cre16.g663450) (collectively BST1–3) are paralogous
  bestrophin-like genes"].
- Predicted chloroplast transit peptide [PMID:31391312 "predicted that each BST protein had a
  chloroplast transit peptide and was likely to be a chloroplast membrane protein"].
- Homology model: pentameric bestrophin, anion-selective pore [PMID:31391312 "the selective
  pore is positively charged, supporting the hypothesis that BST1–3 transport negatively
  charged ions"].

## Expression

- Low-CO2 induced, CIA5-dependent [PMID:31391312 "the cia5 mutant exhibited severely
  reduced expression of BST1 and BST3 under both CO2 conditions"]; BST1 lowest of the three
  [PMID:31391312 "BST1 had a lower level of expression than BST2 or BST3"].

## Localization

- Thylakoid membranes, enriched at pyrenoid periphery (Venus fusion, PSAD promoter)
  [PMID:31391312 "All 3 BST-like proteins localized to the thylakoid membranes of the
  chloroplast"]. The UniProt "Cell membrane" (ARBA) location and resulting GO plasma membrane
  IEA are wrong for this chloroplast paralog.
- Distinct from BST4/RBMP1, which sits in pyrenoid tubules [PMID:39240724 "While BST1-3
  localizes throughout the thylakoid membrane and is enriched at the pyrenoid periphery"].

## Interactions

- Interactome: BST1 interacts with LCIC and with BST3/LCI11 and BST2 [PMID:28938113 "LCI11
  and Cre16.g662600 directly interact, and both also interact with another bestrophin-like
  protein, Cre16.g663400."].

## Phenotypes

- bst3 single knockout: weak phenotype -> redundancy [PMID:31391312 "This led us to think
  that BST1 or BST2 function might be redundant with BST3"].
- Triple RNAi (bsti): poor growth at low CO2, higher K1/2(Ci), less 14Ci accumulation
  [PMID:31391312 "These results indicate that BST1–3 play an important role in Ci uptake and
  fixation in low CO2 conditions in Chlamydomonas."]. There is no BST1-specific mutant.
- pmf: knockdown gives a slight decrease, opposite to Arabidopsis vccn1 [PMID:31391312 "The
  presence of AtVCCN1 decreases pmf in Arabidopsis, but the presence of the 3 BST proteins
  increases pmf in Chlamydomonas."].

## Transport activity: status of evidence (key question for module)

- Bicarbonate delivery to lumenal CAH3 is a proposal [PMID:31391312 "We propose that BST1–3
  are the transporters that bring HCO3− to CAH3 inside the thylakoid."].
- I searched PubMed (2026-10-03; queries: bestrophin AND chlamydomonas; BST4 AND pyrenoid;
  bestrophin AND thylakoid; thylakoid AND bicarbonate AND channel/transporter; BST1/BST3 AND
  Chlamydomonas). I found **no** electrophysiology, reconstitution or heterologous transport
  assay for BST1, BST2 or BST3.
- The only Chlamydomonas thylakoid bestrophin tested electrophysiologically is BST4, which
  gave no currents in Xenopus oocytes. The authors state that HCO3- channel function is
  unsupported by data [PMID:39240724 "BST4 may function as an HCO3− channel, like that proposed
  for BST1-3 (Mukherjee et al. 2019), but there are currently no data to support this
  hypothesis"].
- Diatom PtBST1 knockout nearly abolishes the inducible CCM [PMID:38478576], which is
  consistent with the model but is also genetic evidence only.
- Conclusion: anion channel activity (GO:0005253) is a sound family-level inference. Bicarbonate
  transmembrane transporter / bicarbonate channel activity (GO:0015106 / GO:0160133) is a
  plausible but untested hypothesis. The IBA voltage-gated chloride channel (VCCN1-derived)
  over-specifies.

## Annotation decisions (summary)

- GO:0005247 voltage-gated chloride channel activity (IBA): MODIFY -> GO:0005253
- GO:0005886 plasma membrane (IEA): REMOVE
- GO:0019684 photosynthesis, light reaction (IBA): MARK_AS_OVER_ANNOTATED
- GO:0042651 thylakoid membrane (IBA): ACCEPT
- GO:1902476 chloride transmembrane transport (IEA): MODIFY -> GO:0098656
- NEW GO:0009535 chloroplast thylakoid membrane (IDA, PMID:31391312)
