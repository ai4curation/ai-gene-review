# ARG1 (Arginase-1, human, UniProtKB:P05089) — review notes

## Summary of function
ARG1 is the cytosolic, liver-type (type I) arginase, a binuclear manganese
metalloenzyme that catalyzes the terminal (fifth) step of the urea cycle:
L-arginine + H2O -> L-ornithine + urea (EC 3.5.3.1). It regenerates ornithine to
close the cycle and produces the urea that is excreted. It is a homotrimer, each
subunit binding two Mn(2+) ions. Beyond hepatic ureagenesis, ARG1 is
constitutively expressed in neutrophil granules and released during inflammation,
where local arginine depletion suppresses T-cell (and NK-cell) proliferation /
cytokine production — a myeloid immunoregulatory role. Loss-of-function variants
cause argininemia / arginase deficiency, a urea cycle disorder distinguished by
progressive spastic diplegia/paraparesis rather than the neonatal hyperammonemic
crises typical of proximal UCDs.

## Key verbatim citations

- Terminal urea-cycle step + disease:
  [PMID:3540966 "Arginase (EC 3.5.3.1) catalyzes the last step of the urea cycle in the liver of ureotelic animals. Inherited deficiency of the enzyme results in argininemia, an autosomal recessive disorder characterized by hyperammonemia."]

- Catalytic activity / Mn metalloenzyme:
  [PMID:17562323 "Arginase is a manganese metalloenzyme that catalyzes the hydrolysis of l-arginine to yield l-ornithine and urea."]
  [PMID:21728378 "Arginase is a binuclear manganese metalloenzyme that hydrolyzes L-arginine to form L-ornithine and urea"]
  [PMID:21728378 "Arginase I is a cytosolic enzyme found predominantly in the liver, and arginase II is a mitochondrial enzyme found at highest concentrations in the kidney."]

- Binuclear Mn cluster / structure:
  [PMID:16141327 "The ultrahigh-resolution structure of the human arginase I-ABH complex yields an unprecedented view of the binuclear manganese cluster"]

- Homotrimer / quaternary structure:
  [PMID:22959135 "Our study reinforced the role of Arg308 residue for assembly of the ARG1 homotrimer."]

- Neutrophil/granulocyte expression + azurophil granule + antimicrobial:
  [PMID:15546957 "in human leukocytes arginase I is constitutively expressed only in granulocytes"]
  [PMID:15546957 "arginase I is localized in azurophil granules of neutrophils and constitutes a novel antimicrobial effector pathway, likely through arginine depletion in the phagolysosome"]

- T-cell suppression via extracellular arginase / arginine depletion:
  [PMID:16709924 "arginase I is liberated from human granulocytes, and very high activities accumulate extracellularly during purulent inflammatory reactions. Human granulocyte arginase induces a profound suppression of T-cell proliferation and cytokine synthesis. This T-cell phenotype is due to arginase-mediated depletion of arginine in the T-cell environment, which leads to CD3zeta chain down-regulation"]

- CMTM6 interaction (ARG1 identified as MS interactor in a PD-L1/CMTM6 study; ARG1 itself not the paper's focus):
  UniProt: "INTERACTION WITH CMTM6, AND IDENTIFICATION BY MASS SPECTROMETRY" (RN[15], PMID:28813417).
  Paper abstract is about CMTM6 regulating PD-L1; ARG1 is one MS-detected CMTM6 co-precipitant.

- Sperm nucleus proteomics (HDA nucleus): PMID:21630459 is a bulk sperm-nuclear
  proteome catalog (403 proteins); ARG1 detection is a large-scale MS hit, not a
  dedicated study of nuclear ARG1 function.

## Disease (dismech Arginase_Deficiency.yaml)
"progressive spastic diplegia or paraparesis, seizures, intellectual disability,
and growth retardation... relatively infrequent hyperammonemia compared to other
urea cycle disorders." Neurotoxicity from arginine + guanidino compounds.

## GO term-definition checks (OLS)
- GO:0004053 arginase activity = "L-arginine + H2O = L-ornithine + urea" (exact MF). CORE.
- GO:0000050 urea cycle = full cycle; ARG1 does terminal step. CORE BP.
- GO:0016813 hydrolase acting on C-N linear amidines = PARENT of arginase activity
  (InterPro Mn-binding-site IEA); redundant/over-general vs GO:0004053 -> MODIFY.
- GO:0046872 metal ion binding = PARENT of GO:0030145 manganese ion binding;
  general -> MODIFY to GO:0030145 (which is verified, binuclear Mn cluster).
- GO:0006527 L-arginine catabolic process = verified BP (breakdown of L-arginine). ACCEPT.
- GO:0006525 arginine metabolic process = broader parent; keep (IBA/IEA).
- GO:0030145 manganese ion binding = binds 2 Mn2+/subunit. CORE MF (contributes_to).
- GO:0005829 cytosol = verified subcellular localization (arginase I cytosolic). CORE CC.
- GO:0005737 cytoplasm = parent of cytosol; keep.
- GO:0005576 extracellular region (IDA PMID:16709924) = neutrophil arginase released
  extracellularly; real but non-core (secondary immune role).
- GO:0035578 azurophil granule lumen / GO:0035580 specific granule lumen (Reactome
  neutrophil degranulation) = real neutrophil granule localization; non-core.
- GO:0005634 nucleus (HDA PMID:21630459) = bulk sperm-nucleus proteomics; likely
  not a functional nuclear localization -> non-core / over-annotated.
- GO:0070947 neutrophil-mediated killing of fungus (IMP PMID:15546957) = supported
  by fungicidal-activity paper; non-core immune role.
- GO:0042130 neg reg T cell proliferation (IDA/IBA PMID:16709924) = supported; non-core.
- GO:0060336 neg reg type II IFN signaling (IMP PMID:16709924) = downstream immune
  effect; keep as non-core.
- GO:0042832 defense response to protozoan / GO:0046007 neg reg activated T cell
  proliferation / GO:2000552 neg reg Th2 cytokine production (Ensembl GO_REF:0000107
  IEA from mouse Q61176) = orthology-transferred mouse immune roles; keep non-core.
- GO:0042127 regulation of cell population proliferation (ARBA IEA) = very general;
  over-annotated relative to the specific T-cell terms -> MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI CMTM6, PMID:28813417) = uninformative; MS
  interactor from a PD-L1 study -> non-informative binding, mark over-annotated.

## Deep research
falcon deep-research launched (`just deep-research-falcon human P05089 --alias ARG1`);
FAILED after 600s ("All providers failed" — falcon endpoint timeout). No
-deep-research-falcon.md file produced. Review grounded in the UniProt record, all 9
cached publications, and dismech Arginase_Deficiency.yaml. No DR file fabricated.
