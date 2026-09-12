# FKBP5 (FKBP51) research notes

UniProt: Q13451. EC 5.2.1.8 (peptidyl-prolyl cis-trans isomerase). Two FKBP-type PPIase
domains + three TPR repeats. Two isoforms (Q13451-1 displayed; -2 = VSP_044820/VSP_044821).

## Core biology (well-established)
- Immunophilin with PPIase + co-chaperone activities [PMID:11350175; uniprot "Immunophilin
  protein with PPIase and co-chaperone activities"]. PPIase directly demonstrated (IDA PMID:11350175);
  EC 5.2.1.8; inhibited by FK506 and rapamycin.
- Component of unligated steroid receptor heterocomplexes via HSP90; maintains complex in
  cytoplasm when unliganded [uniprot "Component of unligated steroid receptors heterocomplexes...
  maintaining the complex into the cytoplasm when unliganded"]. NEGATIVE regulator of GR/PR
  (contrast FKBP4/FKBP52 positive). Upon ligand binding FKBP5 dissociates and FKBP4 takes its
  place [uniprot "Upon ligand binding dissociates from the complex and FKBP4 takes its place"].
- Part of heteromultimeric cytoplasmic complex with HSP90AA1, HSPA1A/B and steroid receptors.
- Regulator of Akt/AKT1: scaffolds AKT1-PHLPP1 to enhance AKT1 dephosphorylation -> negative
  regulation of PI3K/AKT signaling [PMID:28147277, PMID:28363942; uniprot "Acts as a regulator
  of Akt/AKT1 activity by promoting the interaction between Akt/AKT1 and PHLPP1"]. This is the
  basis for GO:0030674 adaptor activity (IDA) and GO:0051898 neg reg PI3K/AKT (IDA).
- IKK assembly: interacts with IKBKE/IKBKB, facilitates IKK complex assembly, NF-kB activation,
  IFN production [PMID:26101251, PMID:31434731].
- Stress/psychiatric genetics: FKBP5 polymorphisms (rs1360780) implicated in HPA-axis regulation,
  PTSD/depression risk (GR negative feedback). (Well-established in literature, not in GOA terms.)

## Subcellular location
Cytoplasm (primary), nucleus (both ISS from mouse Q64378; cytosol IDA HPA). Membrane (HDA) and
extracellular exosome (HDA) are high-throughput proteomics — non-core.

## Interactome IPI partners (bare protein binding)
Many are kinase clients consistent with HSP90 co-chaperone role: STK11/LKB1 (Q15831), CDK9 (P50750),
CDK15 (Q96Q40), MOS (P00540), SGK1 (O00141), EGFR (P00533), KSR2 (Q6VAB6), CILK1 (Q9UPZ9),
ULK3 (Q6PHR2), MCM7 (P33993), PYGB (P11216), CHUK/IKK-alpha (O15111), MAPT/tau (P10636-8),
USP49 (Q70CQ1), MCMBP (Q9BTE3-2). HSP90AA1 (P07900), HSP90AB1 (P08238). 9660753=HSP90 IPI.

## Action plan
- PPIase activity GO:0003755 (IDA/IBA/IEA): ACCEPT core MF.
- protein folding GO:0006457 (IBA/IEA/IDA/TAS): KEEP_AS_NON_CORE.
- FK506 binding GO:0005528 (IEA/TAS): ACCEPT.
- heat shock protein binding GO:0031072 (IPI 9660753 HSP90; IEA): ACCEPT core MF.
- adaptor activity GO:0030674 (IDA 28147277, AKT1-PHLPP1 scaffold): ACCEPT core MF.
- neg reg PI3K/AKT GO:0051898 (IDA 28363942): ACCEPT (real BP).
- cytoplasm/cytosol/nucleus: ACCEPT primary; redundant Reactome cytosol KEEP_AS_NON_CORE.
- membrane/exosome HDA: KEEP_AS_NON_CORE.
- protein binding IPI block: KEEP_AS_NON_CORE generally; MODIFY HSP90 partners (P07900/P08238)
  to Hsp90 protein binding; MARK_AS_OVER_ANNOTATED the broad multi-partner screens.
