# PLK1 (P53350) curation notes

## Identity and architecture

- Human Polo-like kinase 1, 603 aa; N-terminal Ser/Thr kinase domain (~39-325) and C-terminal tandem polo-box domain (PBD, ~365-603) that binds Ser-[pThr/pSer]-Pro/X motifs (UniProt DOMAIN comment; deep research, Wyatt & McInnes 2024 model).
- Activation: Aurora A/BORA phosphorylate Thr210 in late G2 [PMID:18615013 "We find that aurora A can directly phosphorylate PLK1 on Thr 210, and that activity of aurora A towards PLK1 is greatly enhanced by Bora"]. Thr210 is the major activating site; Ser137 is not detectably phosphorylated in mitotic cells [PMID:12207013 "Thr-210 is a major phosphorylation site in activated Plk from mitotic HeLa cells"]. MYPT1-PP1 antagonizes Thr210 phosphorylation [PMID:18477460 "MYPT1 depletion increases phosphorylation of PLK1 at its activating site (Thr210) in vivo"].
- Kinase-domain structure with AMPPNP and PHA-680626 [PMID:17461553]; PBD crystal structures with CDC25C and PBIP1-derived phosphopeptides [PMID:17307877; PMID:19597481].

## Core functions (basis for `core_functions`)

1. **Mitotic entry (G2/M transition).** CDC25C phosphorylation/activation [PMID:11202906]; WEE1 S53 phosphorylation creating the beta-TrCP degron [PMID:15070733 "the major M-phase kinases polo-like kinase 1 (Plk1) and Cdc2 are responsible for the phosphorylation of S53 and S123, respectively"]; cyclin B1 phosphorylation on centrosomes in prophase [PMID:12524548]; FOXM1 activation after CDK1 priming [PMID:19160488]; NEBD via p150Glued S179 [PMID:20679239]. Reactome: Activation of Cdc25C, Inactivation of Wee1, Inactivation of Myt1.
2. **Centrosome maturation / bipolar spindle.** Antibody microinjection blocks functional maturation of mitotic centrosomes [PMID:8991084]; gamma-tubulin recruitment requires PLK1 [PMID:18477460]; Kizuna phosphorylation stabilizes spindle poles [PMID:16980960]; MST2 phosphorylation licenses NEK2A-driven centrosome disjunction [PMID:21723128]; NEK9 activation -> EG5 [PMID:21642957]; BORA turnover controls Aurora A localization [PMID:18521620]; PRC1 T602 phosphorylation prevents premature midzone formation [PMID:22621898].
3. **Kinetochore / segregation / APC/C activation.** Kinetochore docking on CDK1-phosphorylated BUB1 T609 [PMID:16760428]; SGO1-dependent kinetochore binding [PMID:17617734]; CENP-Q/U complex targets PLK1 to kinetochores [PMID:25395579]; CUL3-KLHL22 removes PLK1 from kinetochores for SAC satisfaction [PMID:23455478]; EMI1 degron phosphorylation -> APC/C activation [PMID:15148369]; CDC6 T37 -> separase release [PMID:21041660]. Cohesin removal by SA2 phosphorylation (Reactome R-HSA-1638803 / R-HSA-2466068).
4. **Cytokinesis.** Self-targeting to midzone via MKlp2 and PRC1 docking [PMID:12939256; PMID:17351640]; RACGAP1/HsCYK-4 S157 phosphorylation creates the ECT2 BRCT docking site required for furrowing [PMID:19468302; PMID:19468300 "Failure to phosphorylate HsCyk-4 blocks Ect2 recruitment to the central spindle and the subsequent induction of furrowing"]; midbody localization [PMID:30715179; PMID:41361016].

## Non-core / secondary roles (KEEP_AS_NON_CORE)

- DNA damage checkpoint recovery: CLASPIN degron [PMID:16885022], WEE1, 53BP1/CHK2 [PMID:20126263], MRE11 S649 [PMID:28512243]. PLK1 is *degraded* by APC/C-CDH1 to allow the G2 checkpoint [PMID:18662541] -- it opposes the checkpoint, hence MODIFY of GO:0007095 to negative regulation of DNA damage checkpoint (GO:2000002).
- DSB repair: RAD51 S14 [PMID:22325354]; mitotic MMEJ via RHNO1 [PMID:37440612] and POLQ [PMID:37674080].
- p53/p73 axis: TOPORS S718 [PMID:19473992], MDM2 S260 [PMID:19833129], GTSE1 S435 [PMID:20577264], p73 T27 [PMID:18174154]. Treated as over-annotation for the apoptosis/transcription process terms, consistent with the CDK1 review.
- Golgi (GORASP1), cilia (DVL2, NPHP1), meiotic SC disassembly (mouse, PMID:22854038).

## Curation decisions worth flagging

- **GO:0005515 protein binding (91 IPI rows):** REMOVE as uninformative except where the paper demonstrates phospho-dependent PBD docking, which was MODIFIED to GO:0051219 phosphoprotein binding (MKlp2, BUB1, CDC25C, TTDN1, PRC1, HBO1, MYPT1, FOXM1, PBIP1/CDC25C peptides, DVL2).
- **GO:0007062 sister chromatid cohesion (Reactome TAS x2):** MODIFY to GO:0045875 negative regulation of sister chromatid cohesion; PLK1 phosphorylation of SA2 removes cohesin.
- **GO:0007095 G2 DNA damage checkpoint signaling:** MODIFY to GO:2000002 (see above).
- **GO:0007346 regulation of mitotic cell cycle (CYLD paper):** MODIFY to GO:0010971 positive regulation of G2/M transition.
- **GO:0045184 establishment of protein localization:** MODIFY to GO:0071539 protein localization to centrosome (sSgo1 spindle-pole localization).
- **GO:0004672 protein kinase activity:** MODIFY to GO:0004674 (Ser/Thr specificity established).
- **GO:0019901 protein kinase binding (STK10, AURKA) and GO:0042802 identical protein binding (x3):** REMOVE as uninformative binding terms; PLK1 is the substrate of both kinases.
- **GO:0010997 APC/C binding:** MARK_AS_OVER_ANNOTATED; derived from PLK1 being an APC/C-CDH1 substrate.
- **UNDECIDED:** GO:0034451 centriolar satellite (IEA from mouse; source not examinable) and GO:0071168 protein localization to chromatin (PMID:21111234 cache is abstract-only and does not mention PLK1).
- No NEW terms proposed; the existing set already covers the core functions.

## Reference caveats

- PMID:23354166 is a Drosophila study; PMID:20534861 is HCV NS5A phosphorylation; PMID:18195732 abstract is about cyclin B1 (PLK1 outer-kinetochore localization presumably in full text); PMID:21111234 cached record does not mention PLK1.
- Abstract-only caches: 46 of 93 PMIDs; where the abstract does not show the relevant data the curator's full-text reading was deferred to (ACCEPT), per repository rules.
