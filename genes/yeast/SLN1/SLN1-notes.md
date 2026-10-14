# SLN1 (YIL147C, UniProt P39928) curation notes

## Identity and architecture

- 1220 aa hybrid sensor histidine kinase; two predicted TM helices (23-46, 334-354) flanking an
  extracellular (periplasmic) domain (47-333); cytoplasmic HAMP, HisKA/HATPase transmitter
  (573-928, phospho-His576) and C-terminal CheY-like receiver (1089-1210, phospho-Asp1144)
  [file:yeast/SLN1/SLN1-uniprot.txt "Histidine kinase that acts as an osmosensor at the plasma membrane."].
- PANTHER PTHR43047:SF72 (two-component histidine protein kinase family); no HPt domain.

## Biochemistry: phosphorelay

- Posas et al. 1996 (abstract only in cache): [PMID:8808622 "This phosphorelay system is initiated
  by the autophosphorylation of Sln1p at His576. This phosphate is then sequentially transferred to
  Sln1p-Asp-1144, then to Ypd1p-His64, and finally to Ssk1p-Asp554."] and
  [PMID:8808622 "Ypd1p binds to both Sln1p and Ssk1p and mediates the multistep phosphotransfer reaction (phosphorelay)."]
- Ault et al. 2002 (full text): Sln1 receiver is an obligate intermediate between kinase and Ypd1
  [PMID:12455952 "Sln1R is an obligate intermediate in the phosphorelay reaction between Sln1p and Ypd1p"];
  activated allele sln1-22 (P1148S) shifts the phosphotransfer equilibrium toward Ypd1
  [PMID:12455952 "arises from a shift in the phosphotransfer equilibrium from Sln1p to Ypd1p"].
- Ostrander & Gorman 1999 (full text): ECD acts as a dimerization/activation domain; TMD1 required for
  osmotic regulation [PMID:10198019 "These experiments are consistent with
  the hypothesis that the ECD of Sln1p functions as a dimerization and activation
  domain but that osmotic regulation of activity requires the presence of the
  first TMD."].
- Structure of Ypd1 in complex with the Sln1 receiver domain (1OXB/1OXK/2R25)
  [PMID:14656441 "Here we report the first crystal
  structure of a prototypical monomeric histidine-containing phosphotransfer (HPt)
  protein YPD1 in complex with its upstream phosphodonor, the response regulator
  domain associated with SLN1."].

## Signalling logic

- Active (phosphorylated) under low osmolarity; hyperosmotic stress / loss of turgor inactivates
  Sln1, Ssk1 becomes unphosphorylated and activates Ssk2/Ssk22 -> Pbs2 -> Hog1
  [PMID:12821642 "Loss of turgor inactivates the Sln1 histidine kinase activity, leading to subsequent phosphorylation and activation of the HOG MAPK pathway."].
- Second branch: Ypd1 -> Skn7 Asp427 (nuclear TF; OCH1, TRX2 targets)
  [PMID:9843501 "the Sln1 kinase and Ypd1
  phosphorelay intermediate regulate the activity of two distinct response
  regulators, Ssk1p and Skn7p."].
- sln1 null lethality is due to HOG hyperactivation (suppressed by ssk1, ssk2, pbs2, hog1 deletion)
  [file:yeast/SLN1/SLN1-deep-research-falcon.md, section 4.1].

## Sensing

- Turgor sensor: nystatin, cell-wall removal and hyperosmotic stress all inactivate Sln1; periplasmic
  aa 138-150 essential [PMID:12821642]. Exact physical variable unresolved.

## Localization

- Plasma membrane: fractionation [PMID:10198019 "Wild-type cells and strains expressing the truncation constructs from low-copy-number vectors show a higher percentage (∼80%) of Sln1p in the plasma membrane fraction"];
  Sln1-GFP at cell rim [PMID:14665464 "Sln1p-GFP localized to the rim of the cell, consistent with the expected plasma membrane localization of the sensor kinase"].

## Annotation issues noted

- GO:0009927 histidine phosphotransfer kinase activity: current definition ("Serves as a phospho-His
  intermediate enabling the transfer of phospho group between a hybrid kinase and a response
  regulator") describes the HPt role, which in yeast is Ypd1. Sln1 is the hybrid kinase donor and
  lacks an HPt domain. However, SGD (IDA+IMP, PMID:12455952), EcoCyc/EcoliWiki (BarA), TAIR (AHK1)
  and PAINT (PTHR43047 node) all apply it to hybrid kinases too, so this is a community convention
  (possibly predating the definition revision). Kept as non-core; raised as a question.
- GO:0005515 (Ypd1, PMID:14656441): uninformative; the relevant function (phosphodonor to Ypd1) is
  captured by GO:0000155 / phosphorelay. REMOVE (interaction itself is real).
- No NEW terms proposed: GO:0007234 already captures the process; the Sln1-Skn7 branch (OCH1
  transcription) is downstream output via Ypd1/Skn7 and would be indirect.
