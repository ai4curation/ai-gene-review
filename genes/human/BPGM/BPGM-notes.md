# BPGM (bisphosphoglycerate mutase) — review notes

UniProtKB: P07738 (PMGE_HUMAN). Human. HGNC:1093. Chromosome 7.

## Core biology
- BPGM is the enzyme of the **Rapoport-Luebering shunt**, a branch of glycolysis that is highly
  expressed in erythrocytes.
- **Trifunctional enzyme** of the cofactor-dependent phosphoglycerate mutase (dPGM) family, BPG-dependent
  PGAM subfamily; shares the phospho-histidine catalytic mechanism.
  - PMID:2542247 abstract: "Bisphosphoglycerate mutase (EC 5.4.2.4.) is a trifunctional enzyme which
    displays synthase, mutase, and phosphatase activities."
- Principal activity: **2,3-bisphosphoglycerate synthase / bisphosphoglycerate mutase** (EC 5.4.2.4),
  converting 1,3-bisphosphoglycerate to 2,3-bisphosphoglycerate (2,3-BPG).
  - RHEA:17765: (2R)-3-phospho-glyceroyl phosphate = (2R)-2,3-bisphosphoglycerate + H(+); EC 5.4.2.4.
- Also a weak **phosphoglycerate mutase** activity (EC 5.4.2.11; RHEA:15901, 2-PG <=> 3-PG) and a
  **2,3-BPG phosphatase** activity degrading 2,3-BPG to 3-phosphoglycerate.
  - UniProt FUNCTION (PMID:21045285): "Plays a major role in regulating hemoglobin oxygen affinity by
    controlling the levels of its allosteric effector 2,3-bisphosphoglycerate (2,3-BPG). Also exhibits
    mutase (EC 5.4.2.11) activity."
  - UniProt ACTIVITY REGULATION (PMID:10477269, PMID:21045285): "At alkaline pH BPGM favors the synthase
    reaction; however, at lower pH the phosphatase reaction is dominant. Inhibited by citrate."
- **2,3-BPG** is the major allosteric effector that binds deoxyhemoglobin and **lowers hemoglobin oxygen
  affinity**, promoting O2 delivery to tissues (Reactome R-HSA-6798335: "In red blood cells, 2,3BPG is
  the main allosteric effector of hemoglobin, binding preferentially to the deoxygenated hemoglobin
  tetramer, thus reducing oxygen affinity"). The shunt also bypasses the ATP-generating PGK1 step of
  glycolysis.
- **Homodimer** (PMID:15258155, PMID:17052986). Cytosolic. Active-site His-11 forms the
  tele-phosphohistidine intermediate; His-89 proton donor/acceptor (UniProt ACT_SITE).

## Structure / localization
- 259 aa, 30 kDa. Multiple crystal structures (1T8P, 2HHJ, 7THI, etc.).
- Cytosolic (soluble erythrocyte enzyme). Also detected in placental syncytiotrophoblast
  (PMID:16246416) and reported in urinary-prostatic exosome proteomes (PMID:23533145, mass-spec).

## Disease
- Deficiency causes **bisphosphoglycerate mutase deficiency** = Erythrocytosis, familial, 8 (ECYT8;
  MIM:222800): low 2,3-BPG, increased hemoglobin-oxygen affinity, secondary erythrocytosis
  (PMID:1421379, PMID:15054810, PMID:2542247).
- PMID:2542247: mutant "89 Arg->Cys" (mature-protein numbering; = residue 90 in UniProt) shows synthase
  0.57% and mutase 4.1% of normal, phosphatase unaffected — active-site Arg near substrate binding.

## GOA annotations (17 lines) — review plan
- GO:0004082 bisphosphoglycerate mutase activity: appears 4x (IBA, IEA GO_REF:0000120, TAS Reactome,
  TAS PMID:2542247). ACCEPT the IBA as core MF; accept the others.
- GO:0005829 cytosol: IBA + TAS Reactome. ACCEPT (core localization).
- GO:0003824 catalytic activity (IEA InterPro): too general — MARK_AS_OVER_ANNOTATED (root-ish parent
  of the specific MF already present).
- GO:0004619 phosphoglycerate mutase activity (IEA UniProtKB-EC, EC 5.4.2.11): real secondary activity
  (UniProt lists EC 5.4.2.11). ACCEPT / KEEP_AS_NON_CORE.
- GO:0006096 glycolytic process (IEA): ACCEPT — Rapoport-Luebering shunt is a glycolytic branch.
- GO:0016868 intramolecular phosphotransferase activity (IEA InterPro): parent of the mutase MF; correct
  branch but less informative — KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding x3 (IPI, all WITH/FROM P15259 PGAM2; HuRI/BioPlex-type interactome papers):
  bare protein binding, uninformative -> MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
- GO:1901136 carbohydrate derivative catabolic process (TAS Reactome): the phosphatase/consumption of
  1,3-BPG; broad but defensible. KEEP_AS_NON_CORE.
- GO:0070062 extracellular exosome (HDA PMID:23533145): mass-spec exosome proteome; not the site of
  function. MARK_AS_OVER_ANNOTATED.
- GO:0005975 carbohydrate metabolic process (NAS PMID:2542247): broad parent of glycolysis;
  KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
- GO:0007585 respiratory gaseous exchange by respiratory system (TAS PMID:2542247): this term is about
  the respiratory *system* (breathing/lung gas exchange), NOT the erythrocyte O2-affinity role. BPGM's
  effect on O2 delivery is via hemoglobin, not respiratory-system gas exchange. Over-annotation /
  arguably wrong branch. MARK_AS_OVER_ANNOTATED.

## Core functions
- MF: GO:0004082 bisphosphoglycerate mutase activity.
- BP: GO:0006096 glycolytic process (the Rapoport-Luebering shunt branch that produces/degrades 2,3-BPG
  and regulates Hb O2 affinity). No dedicated "2,3-BPG metabolic process" term exists in GO.
- CC: GO:0005829 cytosol.
