# ELO1 (YJL196C, UniProt P39540) notes

## Identity and activity
- Fatty acid elongase 1, ELO family condensing enzyme (EC 2.3.1.199), ER multi-pass membrane protein [UniProt:P39540 "SIMILARITY: Belongs to the ELO family."; "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"].
- Isolated as elongation-defective mutant in fas background: elo1 "fails to efficiently elongate (12, 13, or 14) carbon fatty acids" [PMID:8702485].
- Independent isolation by Dittrich et al.: 12:0 elongation reduced to 0-10% while "16:0 elongation and VLCFA synthesis were unimpaired" [PMID:9546663]; the gene "identified as the known ELO1 sequence" [PMID:9546663].
- Rossler et al. 2003: "Elongase I extends C12-C16 fatty acyl-CoAs to C16-C18 fatty acids" and "Elongases I, II and III are specifically inactivated in, respectively, elo1, elo2 and elo3 mutants" [PMID:12684876].
- Unsaturated substrates: "Synthesis of C16:1Delta(11) was dependent on a functional ELO1 gene, indicating that Elo1p catalyzes carboxy-terminal elongation of unsaturated fatty acids" [PMID:10850979].

## Pathway context
- Module fatty_acid_elongation_cycle: ELO1 is an exemplar of the ELO/ELOVL condensing step (GO:0009922) in ER membrane.
- YeastCyc PWY-5080-1 (VLCFA biosynthesis I) lists ELO2/ELO3 but not ELO1; FASYN-ELONG2-PWY (yeastpathways summary) is the FAS (cytosolic FAS1/FAS2) pathway and does not include ELO1. ELO1 is genuinely not a VLCFA elongase (C12-C16 -> C16-C18), so its absence from PWY-5080-1 is defensible, but no YeastCyc pathway captures the medium-chain ER elongation step.

## Over-propagation from PANTHER PTN000125390
- VLCFA (GO:0042761 >C22) and sphingolipid biosynthesis IBAs come from ELO2/ELO3/ELOVL donors; ELO2 and ELO3 make the C26 VLCFA for sphingolipids [PMID:9211877 "produce the 26-carbon very long chain fatty acids that are precursors for ceramide and sphingolipids"]. ELO1 products are C16-C18 [PMID:12684876].
- PUFA elongation IBA: S. cerevisiae makes no polyunsaturated fatty acids (only OLE1 delta-9 desaturase); remove.
