# YPD1 (YDL235C, Q07688) curation notes

## Identity
- 167-aa stand-alone histidine-containing phosphotransfer (HPt) protein; HPt domain 24-129,
  phosphoacceptor His64 (UniProt Q07688; PROSITE PRU00110). PANTHER PTHR28242 (AHP1-5/YPD1 family).
- Historical alt name "Tyrosine phosphatase-dependent protein 1" reflects the PTP2 suppression
  genetics of the lethal ypd1 deletion; Ypd1 is not a phosphatase.

## Molecular function
- Multistep phosphorelay Sln1-His576 -> Sln1-Asp1144 -> Ypd1-His64 -> Ssk1-Asp554
  [PMID:8808622 "This phosphate is then sequentially transferred to Sln1p-Asp-1144, then to Ypd1p-His64, and finally to Ssk1p-Asp554."]
- Ypd1 binds both Sln1 and Ssk1 [PMID:8808622 "Ypd1p binds to both Sln1p and Ssk1p and mediates the multistep phosphotransfer reaction (phosphorelay)."]
- Also transfers phosphate to Skn7 [PMID:9843501 "the Sln1 kinase and Ypd1 phosphorelay intermediate regulate the activity of two distinct response regulators, Ssk1p and Skn7p."]
- Kinetics: Sln1-R1~P -> Ypd1 29 s-1, Kd 1.4 uM; Ypd1 -> Ssk1-R2 160 s-1, irreversible; Ypd1<->Skn7-R3 reversible
  [PMID:15628880 "phosphotransfer from YPD1 to SSK1-R2 is very rapid (160 s(-)(1)) and is strongly favored over phosphotransfer to SKN7-R3."]
- Ypd1 stabilises Ssk1-R2~P ~200-fold [PMID:11073911 "in the presence of YPD1, we found that the half-life of phosphorylated SSK1-R2 was dramatically extended (almost 200-fold longer than in the absence of YPD1)."]
- Crystal structure of Ypd1 in complex with the Sln1 receiver domain [PMID:14656441 "Here we report the first crystal structure of a prototypical monomeric histidine-containing phosphotransfer (HPt) protein YPD1 in complex with its upstream phosphodonor, the response regulator domain associated with SLN1."]
- GO: GO:0009927 histidine phosphotransfer kinase activity ("Serves as a phospho-His intermediate enabling the transfer of phospho group between a hybrid kinase and a response regulator.") exactly fits.

## Process
- Osmosensing: under normal osmolarity phosphorelay keeps Ssk1 phosphorylated/inactive; hyperosmotic stress
  reduces relay flux so unphosphorylated Ssk1 activates Ssk2/Ssk22-Pbs2-Hog1 (deep research; PMID:8808622).
  GO:0007234 osmosensory signaling via phosphorelay pathway (definition names Sln1) is exact.
- Skn7 branch: Sln1-Ypd1-Skn7 regulates OCH1/cell-wall genes (PMID:9843501, PMID:14665464). No extra
  process annotation proposed (Skn7 transcriptional outputs are downstream of the response regulator).

## Location
- GFPx2-Ypd1 in cytoplasm and nucleus, unchanged by osmotic stress or H64Q; heterokaryon assay shows
  nuclear export; nuclear Ypd1 required for Skn7 signalling
  [PMID:14665464 "Analysis of GFP x2 -Ypd1p revealed that the Ypd1p protein is distributed throughout the cytoplasm and in the nucleus under normal growth conditions."]
  [PMID:14665464 "These results indicate that nuclear localization of Ypd1p is necessary for signaling to Skn7p."]

## Protein binding (GO:0005515) rows
- Sln1 (P39928), PMID:14656441 co-crystal with Sln1 receiver domain -> MODIFY to GO:0043424 protein
  histidine kinase binding (Sln1 is a hybrid histidine kinase; same term SGD uses with PMID:8808622 IPI).
- Ssk1 (Q07084), PMID:18467557 (PCA) and PMID:18719252 (Y2H) HTP screens. Ssk1 is a response regulator;
  no informative GO "response regulator binding" MF exists, and the HTP papers do not assay activity ->
  REMOVE generic protein binding (interaction is real and biologically central; captured by GO:0009927).

## Decisions summary
- ACCEPT: GO:0009927 (IBA, IEA), GO:0007234 (IDA, IMP, IEA), GO:0000160 (IBA, IEA), nucleus/cytoplasm
  (IBA, IDA, IEA), GO:0043424 (IPI, IBA, IEA).
- MODIFY: GO:0016772 (IDA, IEA) -> GO:0009927; GO:0005515 Sln1 -> GO:0043424.
- REMOVE: GO:0005515 Ssk1 x2.
