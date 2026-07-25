# GPAM (GPAT1) review notes

UniProt: Q9HCL2 (GPAT1_HUMAN). Gene symbol GPAM (HGNC:24865); synonyms GPAT1, KIAA1560.
EC 2.3.1.15. 828 aa. Evidence at protein level (PE 1). Family: GPAT/DAPAT family.

## Core biology (from UniProt Q9HCL2)

GPAM encodes **glycerol-3-phosphate acyltransferase 1, mitochondrial (GPAT1)**, the
enzyme that catalyzes the **essential, committed, rate-limiting first step of
glycerolipid biosynthesis**.

- FUNCTION: "Mitochondrial membrane protein that catalyzes the essential" "first step
  of biosynthesis of glycerolipids such as triglycerides," "phosphatidic acids and
  lysophosphatidic acids" (PubMed:18238778, PubMed:19075029, PubMed:36522428). It
  "Esterifies acyl-group from acyl-coenzyme A (acyl-CoA) to the sn-1 position of
  glycerol-3-phosphate, to produce lysophosphatidic acid" (PubMed:18238778)
  [file:human/GPAM/GPAM-uniprot.txt].
- Reaction (Rhea:RHEA:15325, EC 2.3.1.15): sn-glycerol 3-phosphate + acyl-CoA →
  1-acyl-sn-glycero-3-phosphate (lysophosphatidic acid, LPA) + CoA
  [file:human/GPAM/GPAM-uniprot.txt].
- Substrate preference: cryo-EM structure shows GPAT1 "Has a narrow" "hydrophobic
  binding cleft that selects for a linear acyl chain"; "Catalytic activity is higher
  for substrates with a" "16-carbon acyl chain" (i.e., palmitoyl-CoA, saturated)
  (PubMed:36522428) [file:human/GPAM/GPAM-uniprot.txt].
- PATHWAY: "Phospholipid metabolism; CDP-diacylglycerol biosynthesis; CDP-"
  "diacylglycerol from sn-glycerol 3-phosphate: step 1/3" (UPA00557/UER00612)
  [file:human/GPAM/GPAM-uniprot.txt]. GPAT1 provides the LPA that feeds the branch
  point for both storage (triacylglycerol) and membrane (glycerophospholipid,
  including PA → CDP-DAG) lipid synthesis.

## Subcellular location

- SUBCELLULAR LOCATION: "Mitochondrion outer membrane"; "Peripheral membrane protein";
  "Associated with the mitochondrion" "outer membrane of hepatic cells via a patch of
  basic residues" (PubMed:36522428) [file:human/GPAM/GPAM-uniprot.txt]. Topology:
  cytoplasmic N-terminus (1..87), an intramembrane segment (88..118), and a large
  cytoplasmic catalytic domain (119..828); the enzyme faces the cytosol on the outer
  mitochondrial membrane. Mutating a patch of basic residues (R89/H98/R100/H101/R102/
  R107/R108/R118 → E) abrogates mitochondrial localization (PubMed:36522428)
  [file:human/GPAM/GPAM-uniprot.txt].
- HTP mitochondrial proteome study (PMID:34800366) independently places GPAM in
  mitochondria.

## Structure / mechanism

- Cryo-EM structures 8E4Y / 8E50 (80-828), 3.4 Å (PubMed:36522428). HXXXXD motif
  (residues 230..235) essential for acyltransferase activity; His230, His233, Gly273,
  Arg278, Phe313, Arg318 mutations abolish catalysis; Met388 impairs it
  [file:human/GPAM/GPAM-uniprot.txt].

## Regulation / physiology

- Ser695 phosphorylated (liver, large-scale; PubMed:18318008, PubMed:24275569).
- Tissue-enhanced in adipose tissue and liver (HPA). GPAT1 is the predominant hepatic
  isoform; overexpression drives hepatic triacylglycerol accumulation / steatosis
  (background biology; GPAM prefers saturated palmitoyl-CoA).
- Reactome: GPAM gene expression cooperatively stimulated by RUNX1 + ESR1
  (R-HSA-8932020); high GPAM correlates with better breast-cancer survival.

## Cited-reference notes (important for annotation review)

- **PMID:18238778** (Chen et al. 2008, "AGPAT6 is a novel microsomal GPAT"): cached
  entry is **abstract-only** (`full_text_available: false`) and the abstract is about
  **AGPAT6/GPAT4**, a *different* (microsomal/ER) paralog — NOT GPAM/GPAT1. However
  UniProt cites this paper as an **ECO:0000269 (experimental)** source for GPAM's
  FUNCTION and multiple CATALYTIC ACTIVITY reactions (RHEA:15325, 37195, 37199, 37203,
  35723, 35727), so the full text clearly also characterizes GPAM/GPAT1 activity. Per
  curation policy, experimental annotations (EXP/IMP/IDA) sourced from this paper are
  ACCEPTed (do not REMOVE on the basis of an abstract about a paralog). GOA carries
  EXP + IMP GPAT-activity and IDA triglyceride-biosynthesis annotations from it.
- **PMID:19075029** (Zhao et al. 2009, "ALCAT1 … acyltransferase of multiple anionic
  lysophospholipids"): cached entry **abstract-only**; abstract foregrounds **ALCAT1**.
  UniProt nonetheless cites it as ECO:0000269 for a GPAM catalytic activity
  (1-acyl-sn-glycero-3-phospho-(1'-sn-glycerol) + acyl-CoA → diacyl-PG + CoA,
  RHEA:33203), and GOA has IMP annotations from it to GPAT activity (GO:0004366) and
  phosphatidylglycerol biosynthetic process (GO:0006655). Experimental (IMP), so not
  REMOVEd; kept per policy though the PG-biosynthesis role is a minor secondary
  activity, not the core function.
- **PMID:32296183** (Luck et al. 2020, HuRI reference interactome): supports the bare
  `protein binding` (GO:0005515) IPI. UniProt lists one INTERACTION: Q9HCL2–Q9UHD4
  (CIDEB), NbExp=3, IntAct EBI-7600236↔EBI-7062247 [file:human/GPAM/GPAM-uniprot.txt].
  Bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED (never REMOVE an
  IPI protein-binding per policy).
- **PMID:34800366** (Morgenstern et al. 2021, high-confidence mitochondrial proteome):
  HTP support for mitochondrial localization (GO:0005739).

## Annotation-review summary

Core, well-supported:
- MF: **glycerol-3-phosphate O-acyltransferase activity (GO:0004366)** — EXP/IMP/ISS/
  IBA/IEA all converge; ACCEPT the experimental one, keep redundant informative IEA/IBA.
- CC: **mitochondrial outer membrane (GO:0005741)** — Reactome TAS + UniProt SubCell
  IEA, consistent with cryo-EM. ACCEPT.
- BP: **triglyceride biosynthetic process (GO:0019432)** (IDA/IBA/TAS) and
  **phosphatidic acid biosynthetic process (GO:0006654)** (TAS/ISS) — core downstream
  processes served by GPAT1's LPA product. ACCEPT / KEEP.

Over-annotations / non-core / to correct:
- `plasma membrane (GO:0005886)` IEA (InterPro): GPAT1 is an outer-mitochondrial-
  membrane enzyme; plasma-membrane placement is a mis-transferred bacterial-PlsB-style
  InterPro default → REMOVE (clearly-wrong IEA).
- `acyltransferase activity (GO:0016746)` / `…transferring groups other than amino-acyl
  (GO:0016747)` IEA: correct but too general parents of GO:0004366 → MARK_AS_OVER_ANNOTATED.
- `lipid metabolic process (GO:0006629)` / `phospholipid biosynthetic process
  (GO:0008654)` / `glycerophospholipid metabolic process (GO:0006650)` IEA/IBA: correct
  but general → KEEP_AS_NON_CORE.
- `CDP-diacylglycerol biosynthetic process (GO:0016024)` IEA (UniPathway UPA00557):
  matches the UniProt PATHWAY line (step 1/3); GPAT1 supplies the LPA that begins this
  route → KEEP_AS_NON_CORE.
- `diacylglycerol biosynthetic process (GO:0006651)` ISS, `phosphatidylglycerol
  biosynthetic process (GO:0006655)` IMP: downstream / minor secondary; non-core.
- `protein binding (GO:0005515)` IPI: MARK_AS_OVER_ANNOTATED (uninformative).
</content>
