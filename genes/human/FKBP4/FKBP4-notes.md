# FKBP4 (FKBP52) research notes

UniProt: Q02790. 459 aa. EC 5.2.1.8 (peptidyl-prolyl cis-trans isomerase / rotamase).
Domains: two FKBP-type PPIase domains (50-138 active; 167-253), three TPR repeats (270-386).

## Core biology (well-established)
- Immunophilin with PPIase + co-chaperone activity; component of steroid receptor
  heterocomplexes via interaction with HSP90 [file:human/FKBP4/FKBP4-uniprot.txt
  "Immunophilin protein with PPIase and co-chaperone activities. Component of steroid
  receptors heterocomplexes through interaction with heat-shock protein 90 (HSP90)."].
- Binds HSP90 via TPR domain; ternary complexes with HSP90/HSP70 and steroid receptors
  (GR/NR3C1, AR, PR, MR/NR3C2). Promotes intracellular trafficking of steroid receptors
  between cytoplasm and nucleus [uniprot "May play a role in the intracellular trafficking
  of heterooligomeric forms of steroid hormone receptors between cytoplasm and nuclear
  compartments."]. FKBP52 is a POSITIVE regulator of GR/AR/PR (contrast FKBP5/FKBP51 which
  is negative).
- Recruits dynein motor to receptor-HSP90 complexes, promoting NR3C1 transport to nucleus
  [uniprot "Interacts with dynein; causes partially NR3C1 transport to the nucleus."].
- PPIase activity controls neuronal growth cones via TRPC1 channel opening
  [PMID:19945390; uniprot "The isomerase activity controls neuronal growth cones via
  regulation of TRPC1 channel opening."]; F67/D68 mutation reduces catalytic activity toward TRPC1.
- Regulator of microtubule dynamics by inhibiting MAPT/TAU promotion of microtubule assembly
  [uniprot "Also acts as a regulator of microtubule dynamics by inhibiting MAPT/TAU ability
  to promote microtubule assembly."]; C-terminal region (375-458) prevents tubulin polymerization.
- May have protective role against oxidative stress in mitochondria (shuttles mito->nucleus)
  [PMID:21730050; uniprot "May have a protective role against oxidative stress in mitochondria."].
- Inhibited by FK506; binds immunosuppressant FK506 (FKBP = FK506-binding protein).

## Interactions
- HSP90AA1/HSP90AB1 (TPR-mediated), HSP70, HSF1 (in HSP90 multichaperone complex repressing HSF1),
  GLMN/FAP48, S100A1/A2/A6 (Ca2+-dependent, TPR; S100A1/A2 inhibit FKBP4-HSP90), AR, MAPT/TAU,
  CDC37, tubulin, PHYH, dynein.
- p23 (PTGES3) + FKBP4 interact with hAgo2 and activate RNAi [PMID:23741051 "the Hsp90
  cochaperones Cdc37, Aha1, FKBP4, and p23 are required for efficient RNAi. Whereas FKBP4 and
  p23 form a stable complex with hAgo2"].
- Mixed Hsp90-cochaperone complexes: PPIase replaces Sti1/Hop in the cycle [PMID:21170051
  "Upon addition of a PPIase cochaperone to the Hsp90-Sti1 complex, an asymmetric ternary
  complex is preferentially formed."].

## Subcellular location
Cytoplasm/cytosol (primary), mitochondrion, nucleus, cytoskeleton/microtubule, axon/growth cone.
Detected in extracellular exosomes (HDA proteomics — likely passive secretion, non-core).

## Interactome / proteomics PMIDs (mostly IPI bare protein binding)
14638689, 19875381, 20133804, 20188096(S100), 21170051, 21360678, 21730179(AR), 23741051(Ago2),
25036637(Taipale chaperone net), 25277244(Hsp27 net), 28514442, 32296183, 32707033, 33961781,
35063084(Tau), 36115835. 9660753 = HSP90 binding (IPI). 11583998=HSF1. 12604780=GLMN.

## Action plan
- PPIase activity (IDA PMID:11350175, IBA, IEA): ACCEPT core MF GO:0003755.
- heat shock protein binding (IPI 9660753 HSP90; IEA): ACCEPT — core co-chaperone MF GO:0031072.
- protein folding (IBA/IEA/IDA/TAS): KEEP_AS_NON_CORE (co-chaperone assists HSP90; PPIase is a
  foldase-type activity but "protein folding" BP is downstream/generic).
- FK506 binding GO:0005528: ACCEPT (defining property; immunophilin).
- cytosol/cytoplasm (multiple): ACCEPT one IDA; redundant Reactome TAS cytosol KEEP_AS_NON_CORE.
- mitochondrion (EXP PMID:21730050; IEA): ACCEPT (experimental).
- nucleus / nucleoplasm: KEEP_AS_NON_CORE (shuttling; trafficking role).
- cytoskeleton/microtubule/axon/growth cone: KEEP_AS_NON_CORE (tubulin/TAU regulation, ISS).
- protein-macromolecule adaptor activity GO:0030674 (TAS 2378870): ACCEPT — captures co-chaperone
  adaptor role bridging receptor to HSP90/dynein.
- nuclear glucocorticoid receptor binding GO:0035259 (IEA): KEEP_AS_NON_CORE / accept-ish (real GR binding).
- negative regulation of microtubule polymerization / neuron projection (ISS): KEEP_AS_NON_CORE.
- ATP binding / GTP binding (IEA Ensembl from mouse P30416): MARK_AS_OVER_ANNOTATED — no evidence
  FKBP52 is an ATPase/GTPase; these are dubious electronic transfers.
- RNA binding (HDA PMID:22658674): KEEP_AS_NON_CORE (high-throughput RNA-interactome capture).
- phosphoprotein binding GO:0051219 (IEA): KEEP_AS_NON_CORE.
- extracellular exosome (HDA): KEEP_AS_NON_CORE.
- protein binding IPI block: KEEP_AS_NON_CORE generally; MODIFY the HSP90 ones to Hsp90 protein
  binding where partner is HSP90AA1/AB1; AR partner -> KEEP_AS_NON_CORE (real, informs AR pathway).


## 2026-10-26 androgen-receptor module augmentation

Reviewed the complete existing annotation inventory while retaining the imported fields and row counts. The focused changes distinguish AR evidence from GR/PR chaperone models; no new process annotation was manufactured from a necessity phenotype. Existing activities and client systems outside AR remain in scope. UniProt source-section metadata was derived with the normal backfill helper.
The 69 imported rows are preserved. Human prostate cancer cells show FKBP52 contributions to AR dimerization/chromatin binding without an import defect [PMID:34057812]. Mouse Fkbp4 knockout selectively impairs androgen-dependent reproductive tissues but preserves AR ligand binding/nuclear entry [PMID:17142810]; this is comparative mouse evidence. Removed the claim that FKBP5 antagonizes all the same receptors. Preserve the NR3C1/dynein adaptor role without making it an obligatory AR mechanism. PPIase core support now quotes direct human comparative enzymology [PMID:11350175], not a UniProt protein name. Folding is a core process in which the protein performs work; HSP90 binding and cytosol refine broader terms. Current UniProt Q02790 and PTHR46512 entries place FKBP4 in PTHR46512:SF9. PTHR10516 and PTHR46512 PAINT caches share PTN002471265 IBD records; no mechanical repointing or circular-donor claim is warranted.

PANTHER19.0 release classification independently resolves this target to PTHR10516:SF25, whereas current UniProt resolves it to PTHR46512:SF9. Both are source-supported; retain explicit source provenance rather than mechanically replacing one with the other.

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Rows: GO:0005739 IEA (GO_REF:0000044, SL-0173) and GO:0005739 EXP (PMID:21730050, UniProt).
No sub-compartment rows.

Checks:
- UniProt Q02790: [file:human/FKBP4/FKBP4-uniprot.txt "Mitochondrion {ECO:0000269|PubMed:21730050}"],
  plus the notes "Shuttles from mitochondria to nucleus; co-localizes in mitochondria with the
  glucocorticoid receptor (PubMed:21730050)" and "The TPR repeats mediate mitochondrial
  localization". The SL-0173 IEA row derives from this curated location.
- PMID:21730050 (Gallo et al. 2011 JBC) is titled and abstracted for FKBP51 only:
  [PMID:21730050 "FKBP51 is a major mitochondrial factor that undergoes nuclear-mitochondrial"].
  The cached copy is abstract-only. The PMC full text (PMC3191054, pmc.ncbi.nlm.nih.gov,
  read 2026-10-25) mentions FKBP52 only in the Introduction (background on FKBP52 and
  steroid receptors) and Methods ("The UPJ56 rabbit antiserum against FKBP52 was a kind gift
  from Dr. William Pratt"; "Plasmids encoding for the PPIase domain of FKBP52"). Results,
  figure legends and Discussion report localization, TPR dependence and H2O2-induced nuclear
  shuttling for FKBP51 only; the PPIase-domain experiment tests whether FKBP51 localization
  is affected.
- QuickGO: PMID:21730050 is attached only to Q02790 (FKBP4); FKBP5 (Q13451) UniProt gives
  Cytoplasm and Nucleus (by similarity) only.
- MitoCarta3.0: FKBP4 not listed (MS/MS "0-25crude", 2 tissues).

Outcome: both rows KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED; source_defect
WRONG_GENE_PRODUCT (UNIPROT, CHECK, PROBABLE) on the EXP row, suggesting Q13451. The
PMID:21730050 finding statement and the description sentence on mitochondria were corrected.
Still to revisit (outside the mitochondrion rows): the nucleus and other rows that quote
"Shuttles from mitochondria to nucleus" as support, and the suggested question on the
mitochondria-to-nucleus translocation of FKBP4, rest on the same mis-attributed paper.

- Update (2026-10-25, review of PR #5539): the items listed above as still to revisit are done. The nucleus and four nucleoplasm rows now cite UniProt's dynein-dependent NR3C1 nuclear transport and its by-similarity Nucleus location instead of "Shuttles from mitochondria to nucleus"; the nucleus summary, UniProt finding statement, suggested question and experiment no longer presuppose an FKBP4 mitochondrial pool.
