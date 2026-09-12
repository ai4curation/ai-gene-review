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
