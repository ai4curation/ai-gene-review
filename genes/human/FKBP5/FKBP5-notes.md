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


## 2026-10-26 androgen-receptor module augmentation

Reviewed the complete existing annotation inventory while retaining the imported fields and row counts. The focused changes distinguish AR evidence from GR/PR chaperone models; no new process annotation was manufactured from a necessity phenotype. Existing activities and client systems outside AR remain in scope. UniProt source-section metadata was derived with the normal backfill helper.
The 48 imported rows are preserved. FKBP51 inhibits GR/PR in established contexts yet positively regulates AR in human prostate cancer cells. Recombinant assays show recruitment of p23 to ATP-bound HSP90; cell assays show increased androgen-binding competent AR [PMID:20048054]. FKBP51 supports AR dimerization/chromatin binding without a nuclear-import requirement [PMID:34057812]. Normal male reproductive physiology after mouse Fkbp5 loss [PMID:17142810] is not a contradiction of cancer-context human activity. PPIase evidence now uses direct human enzymology [PMID:11350175]. Retained AKT/PHLPP1 scaffold function. Membrane-fraction HDA remains UNDECIDED because soluble proteins can associate transiently with membranes [PMID:19946888]. Q13451 resolves to PTHR46512:SF9; legacy PTHR10516 PAINT PTN002471265 provenance remains legitimate.

PANTHER19.0 release classification independently resolves this target to PTHR10516:SF26, whereas current UniProt resolves it to PTHR46512:SF9. Both are source-supported; retain explicit source provenance rather than mechanically replacing one with the other.

## 2026-10-26: integration source-cache check

Normal fetching supplied the previously uncached PMID:26101251 and PMID:31434731 cited above, and Reactome:R-HSA-9909510. The latter is the reaction “FKBP5 binds CHUK:IKBKB:IKBKG”; corrected the reference title to its fetched title. The cytosol annotation remains supported independently by the curated UniProt localization statement, and no annotation payload or action changed.


## PR5554 member follow-up — 2026-10-26

Explicitly preserved and superseded the 2026-10-10 manual OMICS_EVIDENCE history for membrane association. Peripheral association does not require a membrane anchor. The NK membrane-fraction abstract does not resolve FKBP5-specific identification/controls, and publisher full text returned HTTP 403; UNDECIDED reflects that unresolved biological association, not an integral-membrane requirement. Project tracker remains parent-owned.

All original annotation payloads were compared before/after and preserved; only reviewer assessments, source evidence, and the specified core-function location were changed.
