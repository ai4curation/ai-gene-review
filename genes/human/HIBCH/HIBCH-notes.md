# HIBCH review notes

Gene: **HIBCH** (3-hydroxyisobutyryl-CoA hydrolase, mitochondrial), human, UniProt **Q6NVY1**, HGNC:4908, GeneID 26275, EC 3.1.2.4.

## Summary of function

HIBCH is a mitochondrial-matrix enzyme of the enoyl-CoA hydratase/isomerase
(crotonase) superfamily that catalyzes a step of **valine catabolism**: the
hydrolysis of **3-hydroxyisobutyryl-CoA (HIBYL-CoA)** to **3-hydroxyisobutyrate**
(3-hydroxy-2-methylpropanoate) + free **CoA** (EC 3.1.2.4). By deacylating this
intermediate it diverts the pathway to the free-acid branch and is thought to
prevent accumulation of the upstream reactive intermediate **methacrylyl-CoA**.

- Catalytic activity and function (UniProt): "Hydrolyzes 3-hydroxyisobutyryl-CoA
  (HIBYL-CoA), a saline catabolite. Has high activity toward isobutyryl-CoA."
  [file:human/HIBCH/HIBCH-uniprot.txt "Hydrolyzes 3-hydroxyisobutyryl-CoA (HIBYL-CoA), a saline"]
- Reaction (UniProt CATALYTIC ACTIVITY): 3-hydroxy-2-methylpropanoyl-CoA + H2O =
  3-hydroxy-2-methylpropanoate + CoA + H(+); EC=3.1.2.4; Rhea:RHEA:20888.
  [file:human/HIBCH/HIBCH-uniprot.txt "EC=3.1.2.4;"]
- Pathway (UniProt): "Amino-acid degradation; L-valine degradation."
  [file:human/HIBCH/HIBCH-uniprot.txt "Amino-acid degradation; L-valine degradation."]
- Family (UniProt SIMILARITY): "Belongs to the enoyl-CoA hydratase/isomerase family."
  [file:human/HIBCH/HIBCH-uniprot.txt "Belongs to the enoyl-CoA hydratase/isomerase family."]
- Subcellular location (UniProt): Mitochondrion (ECO:0000250). N-terminal transit
  peptide 1..32; mature chain 33..386. [file:human/HIBCH/HIBCH-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"]

## Primary biochemistry

[PMID:8824301 Hawes et al. 1996, J Biol Chem — cloning + biochemistry; abstract-only in cache]
- "beta-Hydroxyisobutyryl-CoA (HIBYL-CoA) hydrolase is responsible for the specific
  hydrolysis of HIBYL-CoA, a saline catabolite, as well as the hydrolysis of
  beta-hydroxypropionyl-CoA, an intermediate in a minor pathway of propionate metabolism."
- Homology: "showed significant homology to the enoyl-CoA hydratase/isomerase enzyme family."
- Recombinant human enzyme expressed in E. coli reproduced the rat substrate specificity.
- Tissue expression: "predominant expression in liver, heart, and kidney"; UniProt TISSUE
  SPECIFICITY adds kidney/heart/muscle/brain, not lung.
- This is the reference behind both the EXP and IDA `GO:0003860` MF annotations in GOA, and
  Reactome R-HSA-70881.

## Disease / genetic requirement

- HIBCH deficiency (HIBCHD, MIM 250620): autosomal recessive inborn error of valine
  metabolism; delayed psychomotor development, neurodegeneration, increased lactic acid,
  basal ganglia lesions (Leigh-like). [file:human/HIBCH/HIBCH-uniprot.txt "An autosomal recessive inborn error of valine metabolism."]
  First described by Loupatty et al. 2007 (PMID:17160907; Y122C variant) — not in local cache.
- Reactome R-HSA-9916727 "HIBCH mutants don't synthesize beta-hydroxyisobutyrate": lists
  pathogenic variants (Y122C, C163F, G317F, K377*, G345S) with decreased protein/activity in
  fibroblasts.

[PMID:40056416 Li et al. 2025, Cell Rep — abstract-only in cache; basis of FlyBase IMP + IDA]
- "The absence of HIBCH or ECHS1, two Leigh syndrome genes, in cultured cells results in
  abnormal mitochondrial morphology and respiratory defects."
- Loss of HIBCH elevates lysine methacrylation (Kmea), reflecting accumulation of the
  reactive valine-pathway intermediate methacrylyl-CoA (HIBCH's upstream substrate pool):
  "Elevated lysine methacrylation (Kmea) is observed in both HIBCH- and ECHS1-deficient cells
  and fly tissues." This is the genetic (IMP) support for the L-valine catabolic process
  annotation and (IDA) for mitochondrial matrix localization.

## Localization evidence

- IDA mitochondrial matrix (GO:0005759) from PMID:40056416 (FlyBase).
- IDA mitochondrion (GO:0005739) from HPA immunofluorescence (GO_REF:0000052).
- HTP mitochondrion from PMID:34800366 (MitoCoP high-confidence human mitochondrial proteome;
  HIBCH is one entry among the mitochondrial proteome).
- Reactome TAS matrix (R-HSA-9916727, R-HSA-70881).
- All consistent; matrix (GO:0005759) is the most specific/correct compartment for this
  soluble matrix enzyme.

## GO term verification (OLS, current)
- GO:0003860 = 3-hydroxyisobutyryl-CoA hydrolase activity (MF). Definition: "3-hydroxy-2-
  methylpropanoyl-CoA + H2O = CoA + 3-hydroxy-2-methylpropanoate." — matches EC 3.1.2.4 / RHEA:20888. Not obsolete.
- GO:0006574 = L-valine catabolic process (BP). Not obsolete.
- GO:0005759 = mitochondrial matrix (CC). Not obsolete.

## Curation decisions (16 GOA annotations)

Core, kept as core (ACCEPT):
- GO:0003860 MF — EXP (PMID:8824301), IDA (PMID:8824301): defining catalytic activity.
- GO:0003860 MF — TAS (Reactome R-HSA-9916727): the disease-context reaction annotation.
- GO:0006574 L-valine catabolic process — IMP (PMID:40056416): core BP.
- GO:0005759 mitochondrial matrix — IDA (PMID:40056416): core, most specific location.

ACCEPT (correct but redundant/electronic support for the core):
- GO:0003860 MF — IBA (GO_REF:0000033), IEA (GO_REF:0000120 InterPro/EC/RHEA).
- GO:0006574 — IBA (GO_REF:0000033), IEA (GO_REF:0000041 UniPathway).
- GO:0005759 mitochondrial matrix — TAS Reactome R-HSA-9916727, R-HSA-70881.

KEEP_AS_NON_CORE (correct but broader/less specific than the core term):
- GO:0009083 branched-chain amino acid catabolic process — TAS (Reactome R-HSA-70895): correct
  but broad parent of L-valine catabolic process.
- GO:0005739 mitochondrion — IBA, IEA (SubCell), IDA (HPA), HTP (PMID:34800366): correct
  compartment, subsumed by the more specific mitochondrial matrix annotations.

No REMOVE actions: every annotation is biologically correct for HIBCH. No experimental
annotations second-guessed. No bare "protein binding" annotations present in GOA for this gene.

## Core functions (synthesized)
1. MF GO:0003860 (3-hydroxyisobutyryl-CoA hydrolase activity); BP GO:0006574 (L-valine
   catabolic process); location GO:0005759 (mitochondrial matrix).
</content>
</invoke>
