# ABCC10 (MRP7) curation notes

UniProt: Q5T3U5 (MRP7_HUMAN). HGNC:52. Gene ABCC10, synonyms MRP7, SIMRP7.
NCBI taxon 9606. 1492 aa; EC 7.6.2.2 and EC 7.6.2.3.

## Protein architecture / family
- Member of the ABC transporter superfamily, ABCC (MRP) family, "conjugate transporter"
  (TC 3.A.1.208) subfamily. PANTHER PTHR24223:SF330.
  [file:human/ABCC10/ABCC10-uniprot.txt "Belongs to the ABC transporter superfamily. ABCC family. Conjugate transporter (TC 3.A.1.208) subfamily."]
- "Long" MRP architecture: three transmembrane domains (TMD0 + TMD1 + TMD2) and two
  nucleotide-binding domains (NBDs). UniProt lists ~17 TM helices, two ABC transmembrane
  type-1 domains (285-563, 885-1210) and two ABC transporter (NBD) domains (598-824,
  1246-1479), with Walker-A ATP-binding motifs at 633-640 and 1280-1287.
  [PMID:23087055 "ABCC10 consists of three TMDs and two NBDs, and is one of the least well characterized family members"]
- Two splice isoforms: Q5T3U5-1 (Mrp7, spleen-specific) and Q5T3U5-2 (Mrp7A, widely
  expressed) [PMID:12566991]. Phosphorylated at Thr463/Ser467 (large-scale phosphoproteomics,
  PMID:18220336) — not functionally characterized.

## Molecular function / substrates (core)
- ATP-dependent efflux transporter of amphipathic/lipophilic organic anions.
- Transports glutathione S-conjugates (leukotriene C4) and glucuronide conjugates
  (17beta-estradiol-17-glucuronide). LTC4 is a high-affinity substrate (KM = 0.057 µM) that,
  with E2-17betaG, stimulates ABCC10 ATPase activity; GSH itself does NOT stimulate ABCC10
  (unlike ABCC1).
  [PMID:23087055 "We found that LTC4 and E217βG induced ABCC10 ATPase activity by 79.7% and 30%, respectively"]
  [PMID:15256465 "it is able to transport amphipathic anions such as 17beta-estradiol 17-(beta-d-glucuronide)"]
- Broad xenobiotic/drug efflux: confers resistance to taxanes (docetaxel strongest, 9-13
  fold; paclitaxel), vinca alkaloids, epothilone B, and the nucleoside analog Ara-C; NOT
  cisplatin.
  [PMID:15256465 "MRP7-transfected HEK293 cells exhibited the highest levels of resistance toward docetaxel (9-13-fold)"]
  [PMID:23087055 "Abcc10(-/-) mice exhibit increased tissue sensitivity and lethality resulting from paclitaxel exposure"]
- Directly measured ATPase activity: basal 5.5-12 nmol/min/mg; optimum pH 7.5; KM(ATP) ~3.2 mM;
  cation preference Mn2+>Mg2+>Ca2+>Co2+. Inhibited by cepharanthine, sorafenib, and several TKIs.
  [PMID:23087055 "ABCC10 ATPase activity was measured using an inorganic phosphate (Pi) release assay"]
- UniProt catalytic activities: EC 7.6.2.2 (xenobiotic), EC 7.6.2.3 (S-substituted glutathione),
  plus curated reactions for E2-17betaG and LTC4 export; a 2-5A (oligoadenylate) export reaction
  is annotated By similarity to mouse Q8R4P9. Does NOT transport glycocholate, taurocholate, MTX,
  folic acid, cAMP, or cGMP [PMID:12527806, via UniProt FUNCTION].

## Localization (core = plasma membrane, basolateral/basal)
- Cell membrane, multi-pass; basolateral in polarized epithelia.
  [PMID:23087055 "ABCC10 localized predominantly to the basolateral membranes in two independent ABCC10-overexpressing LLC-PK1 derivative cell lines"]
- Detected in plasma-membrane fraction of primary human fetal RPE cells (targeted proteomics)
  [PMID:28112518 "MPR7, OAT2 and RFC1 were detected in the hfRPE cells"].
- Testis/blood-testis barrier: basal membrane of Sertoli cells + peritubular myoid cells
  [PMID:35307651 "OCTN2, multidrug resistance protein (MRP) 3, MRP6, and MRP7 localized to SC basal membranes and peritubular myoid cells (PMCs) surrounding the seminiferous tubules."].
- A lysosomal-membrane HDA proteomics hit (PMID:17897319) is a discovery-screen artifact
  (crude placental lysosomal fraction, PM contamination likely); judged over-annotation.

## Review decisions summary (30 existing annotations)
- ACCEPT (22): ATP binding; ATP hydrolysis activity; 6x plasma membrane; 2x basolateral;
  2x basal plasma membrane; 4x ABC-type xenobiotic transporter activity; 2x ABC-type
  glutathione S-conjugate transporter activity; xenobiotic transport; 3x transmembrane
  transport; 2x leukotriene transport.
- MODIFY (2): membrane (GO:0016020) -> plasma membrane (GO:0005886);
  leukotriene metabolic process (GO:0006691) -> leukotriene transport (GO:0071716)
  (transporter does not metabolize leukotrienes).
- TOO_GENERAL (3): ABC-type transporter activity (GO:0140359, x2) and
  ATPase-coupled transmembrane transporter activity (GO:0042626) are is_a ancestors of the
  accepted GO:0008559 / GO:0015431. (ontology ancestry confirmed via OLS).
- MARK_AS_OVER_ANNOTATED (1): lysosomal membrane (GO:0005765).
- No UNDECIDED: all cited publications were accessible (23087055 and 35307651 full text;
  others abstract-only but sufficient for the localization/resistance claims reviewed).

## Reactome entries cited
- Reactome:R-HSA-1454916 "The ABCC family mediates organic anion transport" (plasma membrane TAS;
  ATPase-coupled transporter TAS).
- Reactome:R-HSA-382556 "ABC-family proteins mediated transport" (transmembrane transport TAS).

## Core functions chosen
1. ATP-dependent organic-anion (GSH-conjugate / glucuronide) export at the basolateral plasma
   membrane -> GO:0015431; directly_involved_in leukotriene transport (GO:0071716).
2. ATP-dependent xenobiotic/drug efflux (multidrug resistance) -> GO:0008559;
   directly_involved_in xenobiotic transport (GO:0042908).
