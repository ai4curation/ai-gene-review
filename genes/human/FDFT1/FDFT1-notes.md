# FDFT1 (Squalene synthase / farnesyl-diphosphate farnesyltransferase 1) review notes

UniProtKB: P37268 | HGNC:3629 | EC 2.5.1.21 | Human (NCBITaxon:9606)

## Function (verified)

FDFT1 is **squalene synthase (SQS/SS)**, also called farnesyl-diphosphate
farnesyltransferase 1 (FPP:FPP farnesyltransferase). It catalyses the **first
committed step of sterol biosynthesis**: the reductive head-to-head (1'-1)
condensation of **two molecules of farnesyl diphosphate (FPP) to squalene**,
proceeding via a stable **presqualene diphosphate (PSQPP)** intermediate and an
NAD(P)H-dependent reduction.

- UniProt FUNCTION [file:human/FDFT1/FDFT1-uniprot.txt]: "Catalyzes the condensation
  of 2 farnesyl pyrophosphate (FPP) moieties to form squalene. Proceeds in two
  distinct steps. In the first half-reaction, two molecules of FPP react to form the
  stable presqualene diphosphate intermediate (PSQPP) ... In the second half-reaction,
  PSQPP undergoes heterolysis, isomerization, and reduction with NADPH or NADH to form
  squalene. It is the first committed enzyme of the sterol biosynthesis pathway."
- Catalytic activity (Rhea:RHEA:32295, EC 2.5.1.21): 2 (2E,6E)-farnesyl diphosphate +
  NADPH + H+ = squalene + 2 diphosphate + NADP+. Also uses NADH (RHEA:32299).
  Requires Mg2+ cofactor (PubMed:24531458).
- PATHWAY (UniProt): Terpene metabolism; lanosterol biosynthesis; lanosterol from
  farnesyl diphosphate: step 1/3.
- [PMID:10896663 "Squalene synthase catalyzes the biosynthesis of squalene, a key
  cholesterol precursor, through a reductive dimerization of two farnesyl diphosphate
  (FPP) molecules."] and "Because FPP is located at the final branch point in the
  isoprenoid biosynthesis pathway, its conversion to squalene through the action of
  squalene synthase represents the first committed step in the formation of cholesterol"
  — establishes both the reaction and the branch-point/committed-step role. This is the
  human SQS crystal structure paper (2.15 A, residues 39-370).
- [PMID:24531458] structural insights into catalytic mechanism, Mg2+/NADP binding sites
  (abstract not cached; used as ECO:0000269 support in UniProt for the reactions).
- [PMID:8474436 "Squalene synthetase (farnesyl diphosphate:farnesyl diphosphate
  farnesyltransferase; EC 2.5.1.21) is thought to represent a major control point of
  isoprene and sterol biosynthesis in eukaryotes."] Human/yeast conservation; human
  cDNA can rescue S. cerevisiae ERG9 disruption; predicted C-terminal membrane-spanning
  ~50 kDa protein.

## Branch point biology

FPP sits at the branch point of the isoprenoid pathway. SQS commits FPP specifically to
the sterol branch (squalene -> lanosterol -> cholesterol), diverting it away from the
non-sterol branches (dolichol, ubiquinone/CoQ, heme A, protein prenylation). This makes
SQS a pharmacological target (statin-sparing lipid-lowering; inhibitors TAK-475/lapaquistat,
zaragozic acids) that lowers sterol synthesis without depleting the non-sterol isoprenoids
depleted by HMG-CoA reductase inhibition.

## Localization

C-terminally anchored **endoplasmic reticulum membrane** protein.
- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Multi-pass membrane
  protein" (two C-terminal TM helices, FT TRANSMEM 284-304 and 384-404; the catalytic
  domain 31-370 is cytosolic-facing, consistent with the ER GO:0098554 cytoplasmic-side
  annotation).
- GOA has IDA (HPA immunofluorescence, GO_REF:0000052) to endoplasmic reticulum, plus
  IBA/ISS/TAS/IEA to ER membrane. HPA reports low tissue specificity; widely expressed.

## Disease

**Squalene synthase deficiency (SQSD; MIM:618156)** — autosomal recessive congenital
disorder of cholesterol biosynthesis. [PMID:29909962] (Coman et al. 2018, Am J Hum Genet)
first characterised it: profound developmental delay, brain abnormalities, 2/3 syndactyly
of toes, facial dysmorphism, low total and LDL cholesterol, abnormal urine organic acids
(heptadecanoid / methylsuccinate features from accumulated FPP-derived metabolites). SLOS-like.
UniProt DISEASE + TISSUE SPECIFICITY (widely expressed) cite this paper. (Abstract not cached;
used only as background, not as supporting_text.)

## Protein-protein interactions (IPI, GO:0005515)

GOA carries many `protein binding` (GO:0005515) IPI annotations from high-throughput
interactome maps. These are bare protein-binding and per policy should be
MARK_AS_OVER_ANNOTATED (not informative; not core function; not removed).
- PMID:23864651 — GLP-1R interactome (MYTH split-ubiquitin Y2H + CO-IP). FDFT1/SQS
  (P37268) appears as one of many GLP-1R (P43220) interactors; membrane-based screen. No
  functional consequence for SQS shown.
- PMID:25910212 — "Widespread macromolecular interaction perturbations in human genetic
  disorders" (edgotyping); interactome-scale.
- PMID:32296183 — HuRI, the human binary reference interactome (Y2H). FDFT1 shown to bind
  ~16 partners (AQP6, ARL13B, CD74, CD79A, CLN5, CREB3, ELOVL4, FAM209A, GJA8, GPR152,
  JAGN1, NCAPH2, PANX1, SLC10A1, SLC35C2, TLCD4, TMX2 in UniProt INTERACTION block). Many
  are ER/membrane proteins; consistent with an ER-membrane enzyme co-detected in
  membrane-Y2H, but none establish a specific molecular function beyond catalysis.

## Annotation-set assessment (GOA, P37268)

Core (ACCEPT):
- GO:0051996 squalene synthase [NAD(P)H] activity — MF, has EXP (PMID:10896663), IBA, IEA
- GO:0006695 cholesterol biosynthetic process — BP, IBA
- GO:0005789 endoplasmic reticulum membrane — CC, IBA is_active_in + ISS/TAS/IEA located_in
- GO:0005783 endoplasmic reticulum — CC, IDA (HPA)

Accept (correct, broader or context):
- GO:0045338 farnesyl diphosphate metabolic process — BP (FPP is the substrate)
- GO:0006694 steroid biosynthetic process — BP (broad parent of sterol/cholesterol biosynth)
- GO:0008610 lipid biosynthetic process — BP (broad but true)
- GO:0016765 transferase, transferring alkyl/aryl (other than methyl) groups — MF (EC 2.5.1.-
  parent of the squalene-synthase activity; correct but general)
- GO:0016020 membrane — CC (general; true)

MARK_AS_OVER_ANNOTATED:
- GO:0005515 protein binding (x3 PMIDs) — bare protein binding, uninformative HT interactome.
