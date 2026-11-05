# Pck2 (rat) — manual literature research

No deep-research API was available for this session; this file records literature work done by
hand from cached publications (publications/PMID_*.md) and PubMed searches (2026-10-28).
It is not the output of any deep-research provider.

## Identity

- Gene: Pck2, phosphoenolpyruvate carboxykinase 2, mitochondrial (PEPCK-M); RGD:1311112; NCBI GeneID 361042.
- UniProt: GOA is keyed to the unreviewed TrEMBL entry F1LQJ7 (667 aa, Ensembl ENSRNOP00000025260).
  The accession requested for this review, B2RYG2 (663 aa, MGC cDNA, flagged "Fragment"), is the same
  gene (same symbol, RGD:1311112, GeneID 361042) but carries no GOA rows; the review is on F1LQJ7.
- F1LQJ7 begins "TLLPSPPSLT..." with no initiator methionine; the human PCK2 start (MAAL...) aligns to
  rat Met28 ("MAAMYLPGLRL..."), so residues 1-27 of the Ensembl model are probably 5' UTR translation.
- Family: GTP-dependent PEPCK (Pfam PF00821/PF17297, HAMAP MF_00452, PROSITE PS00505, PANTHER
  PTHR11561:SF11 "PHOSPHOENOLPYRUVATE CARBOXYKINASE [GTP], MITOCHONDRIAL").

## Enzyme activity and location

- Mammals have two PEPCK genes: PCK1 (cytosolic, PEPCK-C) and PCK2 (mitochondrial, PEPCK-M)
  [PMID:24177027 "PCK1 encodes PEPCK-C and resides on human chromosome 20q13.31. PCK2 encodes PEPCK-M and resides on human chromosome 14q11.2"].
- PEPCK-M acts in the matrix [PMID:24177027 "PEPCK that can either take place in the cytosol (PEPCK-C) or the mitochondrial matrix (PEPCK-M)"].
- Mn2+ is the most activating cation [PMID:24177027 "PEPCK-M binds a single divalent cation in tetrahedral coordination in the absence of substrates with Mn2+ being the most activating cation"].
- Rat liver: mitochondrial PEPCK activity measured in foetal, newborn and adult rat liver and
  indistinguishable kinetically from the soluble enzyme [PMID:6049928 "Kinetic and other studies on the properties of phosphoenolpyruvate carboxykinase have shown no differences between the soluble and mitochondrial enzymes"].
  In adult rat liver >90% of PEPCK activity is cytosolic (PCK1) [PMID:6049928 "more than 90% of the activity is in the cytoplasm"],
  so whole-liver PEPCK activity measurements (PMID:11440903, PMID:4353083; abstract-only) mostly report PCK1.
- Rat INS-1 832/13 cells and rat islets: PEPCK activity is mitochondrial, verified with glutamate
  dehydrogenase as a matrix marker [PMID:19635791 "Virtually all of the PEPCK activity from cells and islets was localized to the mitochondrial fraction when adjusted for leakage of mitochondrial contents into the cytosol fraction by parallel measurements of glutamate dehydrogenase activity from the same samples"].

## Biological roles (rat evidence)

- Insulin secretion (rat beta-cell line, rat islets): PEPCK-M consumes OAA and mtGTP to make PEP
  [PMID:19635791 "PEPCK-M will then consume oxaloacetate and GTP to produce PEP, GDP, and CO2"];
  up to 41% of islet PEP comes from PEPCK-M, and knockdown abolishes GSIS
  [PMID:19635791 "Silencing the PEPCK-M gene completely inhibited GSIS underscoring its central role in mitochondrial metabolism-mediated insulin secretion."].
- Hepatic gluconeogenesis (rat, ASO knockdown in vivo and in hepatocytes)
  [PMID:24497630 "Consistent with its predicted role, gluconeogenesis rates from hepatocytes lacking PEPCK-M are severely reduced for lactate, alanine, and glutamine, but not for pyruvate and glycerol."].
- Endotoxaemia/TNF lower hepatic Pck2 mRNA and PEPCK-M activity [PMID:19268478 "In rat endotoxemia, hepatic PCK2 mRNA and PEPCK-M enzyme activity decreased by 53% and 38%, compared to sham controls."].
- Prenatal dexamethasone programming of hepatic Pck2 expression [PMID:16570165 "Prenatal glucocorticoid exposure causes lifelong hyperglycaemia in rat offspring, associated with permanently increased hepatic phosphoenolpyruvate carboxykinase 2 (PCK2)"].

## Non-canonical protein kinase activity (human)

- Human PCK2 phosphorylates ACSL4 Thr679 and promotes ferroptosis in cancer cells (single study)
  [PMID:38720107 "in vitro kinase assays showed that PCK2 could directly phosphorylate ACSL4"].
  Not tested in rat; the paralog PCK1 has a reported analogous protein-kinase activity.
