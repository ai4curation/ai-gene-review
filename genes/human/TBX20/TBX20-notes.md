# TBX20 (human, Q9UMR3) curation notes

Automated deep research was unavailable for this session (falcon 402, OpenAI 401), so no
`-deep-research-<provider>.md` file exists. These notes were compiled manually from cached
publications (abstracts unless noted), UniProt, and QuickGO.

## Identity and domains

- T-box transcription factor (TBX1 subfamily); single T-box DNA-binding domain; UniProt function
  is ECO:0000250 (by similarity to mouse): "Acts as a transcriptional activator and repressor
  required for cardiac development and may have key roles in the maintenance of functional and
  structural phenotypes in adult heart."
- Disease: Atrial septal defect 4 (ASD4, MIM:611363) [PMID:17668378; PMID:19762328].
- Alternatively spliced: the long isoform (Tbx20a) carries C-terminal transactivation and
  transrepression domains [PMID:14550786 "Tbx20a uniquely carried strong transactivation and transrepression domains in its C terminus"].

## Molecular function

- Sequence-specific DNA binding at brachyury-like half sites [PMID:14550786 "Isoforms with an intact T-box bound specifically to DNA sites resembling the consensus brachyury half site, although with less avidity compared with the related factor, Tbx5"].
- In vivo ChIP-seq motif in adult mouse heart: AGGTGNTGACAG [PMID:22328084 "The TBX20 DNA-binding motif that we uncovered from our ChIP data ( 14 ) (consensus AGGTGNTGACAG) resembles known T-box DNA-binding motifs identified in vitro"].
- Human TBX20 included in HT-SELEX survey of human TF specificities [PMID:28473536] (TBX20 data are in supplementary tables; not quotable from the cached text).
- Dual activator/repressor: [PMID:22328084 "This analysis revealed a dual role for TBX20 as both a transcriptional activator and a repressor"].
- Activation of cardiac enhancers with partners: [PMID:15843409 "Tbx20 synergized with Isl1 and Gata4 to activate both the Mef2c and Nkx2-5 enhancers"]; [PMID:14550786 "Tbx20 physically interacted with cardiac transcription factors Nkx2-5, GATA4, and GATA5, collaborating to synergistically activate cardiac gene expression"].
- Human TBX20 ChIP/luciferase (Nppa, Gja5), gain-of-function I121M [PMID:19762328 "Tbx20-I121M resulted in a significantly enhanced transcriptional activity, which was further increased in the presence of co-transcription factors GATA4/5 and NKX2-5"].
- Interaction with TBX5 [PMID:15634698 "we show that TBX5 and TBX20 can physically interact and map the interaction domains"].
- Repression of Tbx2 in chamber myocardium [PMID:15843414 "Our data demonstrate a repressive activity for Tbx20 and place it upstream of Tbx2 in the cardiac genetic program"]; mechanism partly non-DNA-binding via Smad sequestration [PMID:19661464 "both Tbx20 and mutant isoforms of Tbx20 unable to bind DNA attenuate Bmp/Smad-dependent activation of Tbx2 by binding Smad1 and Smad5 and sequestering them from Smad4"].

## Biological processes (mostly mouse)

- Heart tube elongation / chamber formation [PMID:15901664 "The tube does not elongate, indicating a defect in recruitment of mesenchyme from the secondary heart field"; "Tbx20 is required for progression from the linear heart tube to a multi-chambered heart"].
- Outflow tract, RV, valves (graded knockdown) [PMID:15843409 "A mild knockdown led to persistent truncus arteriosus (unseptated outflow tract) and hypoplastic right ventricle"].
- AV canal formation and endocardial EMT via Bmp2 [PMID:21983003 "mice lacking Tbx20 in the AVC myocardium fail to form the AVC constriction, and the endocardial epithelial-mesenchymal transition (EMT) is severely perturbed"].
- Endocardial cushion mesenchyme proliferation/ECM (chick) [PMID:17064679].
- Cardiomyocyte proliferation [PMID:23751911 "The T-box transcription factor Tbx20 is necessary and sufficient to promote prenatal cardiomyocyte proliferation"].
- Adult cardiomyocyte homeostasis [PMID:22080862 "This ablation resulted in the onset of severe cardiomyopathy accompanied by arrhythmias"].
- Motor neurons: [PMID:15843409 role in Isl2/Hb9 regulation]; [PMID:17119020 "Tbx20 was required for the tangential and the trans-median movement of vestibuloacoustic neurons"].
- Human: ASD, valve defects, cardiomyopathy [PMID:17668378]; ASDII/PFO GOF variant [PMID:19762328]; Chinese CHD cohort ASD/TAPVC/TOF [PMID:18834961, abstract-only]; TBX20 expression in TOF biopsies [PMID:18275040, abstract-only].

## Points of curation interest

- Rat-derived GO:0043065 "positive regulation of apoptotic process" (RGD IMP, PMID:27572266) is
  directionally inverted relative to the paper: silencing TBX20 *induced* apoptosis
  [PMID:27572266 "Silencing of TBX20 in H9c2 and HEK293 cells significantly inhibited cell proliferation, induced cell apoptosis and led to G2/M cell cycle arrest"].
- Xenopus-derived endoderm formation / lateral mesoderm formation (ISS) rest on ectopic
  overexpression [PMID:14550786 "enforced expression of Tbx20a, but not Tbx20b, led to induction of mesodermal and endodermal lineage markers"], not loss-of-function; over-annotation.
- Module (cardiac_specification_network, tbox_tf annoton): GO:0000981 in heart development —
  consistent with this review.
