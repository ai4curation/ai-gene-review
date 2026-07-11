# CPS1 (human, P31327) review notes

Deep research: falcon run polled (~12 min) but did NOT land before review; grounded instead in
UniProt (P31327), seeded GOA, cached publications, and the dismech CPS1D disorder file.

## Core biology (verified)

- ~1500-aa mitochondrial-matrix multidomain enzyme; catalyzes the FIRST committed step of the urea
  cycle: NH4+ + HCO3- + 2 ATP -> carbamoyl phosphate + 2 ADP + Pi + 2 H+ (EC 6.3.4.16).
  [UniProt P31327 CATALYTIC ACTIVITY; Rhea:RHEA:18029]
- Glutamine-INDEPENDENT (ammonia-dependent). "Glutamine is utilized as the endogenous source of
  ammonia by all types of CPS except CPS1. The inability of human CPS1 to use glutamine is explained
  by the replacement by serine (Ser294) in this enzyme of the key catalytic cysteine of the catalytic
  triad." [PMID:26592762 "Glutamine is utilized as the endogenous source of ammonia by all types of CPS31464748 except CPS12"]
  UniProt: "The type-1 glutamine amidotransferase domain is defective."
- ABSOLUTE requirement for the allosteric activator N-acetyl-L-glutamate (NAG). Without NAG, activity
  is <=2% of NAG-saturated. [PMID:26592762 "in its absence CPS1 exhibits ≤2% of the activity at NAG saturation"]
  NAG binds the C-terminal L4 (MGS-like) domain. [UniProt BINDING 1391..1449 N-acetyl-L-glutamate]
- Ionic activators: potassium and magnesium; K+ coordinated in L1 K-loop, Mg2+ coordinates ADP.
  [PMID:26802762... PMID:26592762 "having at its center a coordinated potassium ion (thus the name K-loop)"; "CPS1 affinities for its essential ionic activators potassium and magnesium are increased importantly by NAG"]
- Location: mitochondrial matrix. [UniProt SUBCELLULAR LOCATION Mitochondrion; PMID:22002106; TRANSIT 1..38 Mitochondrion]
- Quaternary: monomer-dimer equilibrium, monomer predominant. [PMID:26592762 "behavior of human CPS1 in solution as a monomer-dimer system in rapid equilibrium in which the monomer predominates"; PMID:6249820 native MW ~190k, monomer ~165k]
- Km values: ATP 0.47 mM, HCO3- 4 mM, NH4+ 1 mM (recombinant) [PMID:23649895]; NAG Km ~0.1 mM [PMID:6249820]
- Tissue: primarily liver and small intestine. [UniProt TISSUE SPECIFICITY]
- Disease: CPS1 deficiency (CPS1D), autosomal recessive urea-cycle disorder, severe neonatal
  hyperammonemia; >130 private missense mutations. [PMID:21120950; MONDO:0009376; dismech]
- Recombinant human CPS1 established EC 6.3.4.16 and kinetics. [PMID:23649895, PMID:24813853]
- Regulation by acylation: glutarylation (increases fasting) and succinylation removed by SIRT5
  (deacylation activates). [UniProt PTM; PMID:24703693; Reactome R-HSA-9955504]

## Over-annotation / dubious annotations

- GO:0004088 carbamoyl-phosphate synthase (glutamine-hydrolyzing) activity (IBA/IEA): this is the
  activity of CPS II (CAD, cytosolic, pyrimidine). CPS1 is ammonia-dependent and lacks a functional
  glutaminase (defective GATase, Ser294). MODIFY -> GO:0004087. [PMID:26592762; UniProt DOMAIN comment]
- GO:0004175 endopeptidase activity (IEA GO_REF:0000107, Ensembl Compara ortholog transfer): CPS1 is
  a ligase, not a protease. Implausible ortholog-transfer artifact. REMOVE.
- GO:0005509 calcium ion binding, GO:0005543 phospholipid binding (IEA GO_REF:0000107): no evidence;
  CPS1 uses K+/Mg2+ not Ca2+, no lipid-binding role in the matrix. REMOVE (ortholog-transfer).
- Bare GO:0005515 protein binding (IPI PMID:12620389 Raf 2-hybrid; PMID:15161933 & PMID:20618440
  14-3-3 proteomics): uninformative; the interactions (ARAF/RAF1/YWHAZ in UniProt INTERACTION) are
  large-scale-screen hits, not established functional partners. MARK_AS_OVER_ANNOTATED / do not
  elevate to core; keep bare term as non-core at most.
- GO:0042311 vasodilation (IMP), GO:0046209 nitric oxide metabolic process (IMP), GO:0019240
  L-citrulline biosynthetic process (NAS) all from PMID:14718356: a T1405N-polymorphism genotype-
  association study of NO metabolites/forearm blood flow. Indirect downstream physiology (CPS1 ->
  carbamoyl-P -> citrulline -> arginine -> NO), not a direct CPS1 function. Over-annotation.
  [PMID:14718356 "a polymorphism in the gene encoding carbamoyl-phosphate synthetase 1 influences nitric oxide production as well as vascular smooth muscle reactivity"]
- GO:0050667 homocysteine metabolic process (IDA) and GO:0072341 modified amino acid binding (IDA)
  from PMID:20031578: this is a GWAS SNP-plasma-homocysteine association (rs7422339), NOT an IDA of
  direct binding or metabolism. The evidence code is misapplied. However GO:0072341 modified amino
  acid binding IS actually correct for CPS1 for a different reason: it binds N-acetyl-L-glutamate (a
  modified amino acid). [PMID:20031578 "novel associations with CPS1 (2q34; rs7422339..."]
- GO:0019433 triglyceride catabolic process (IMP PMID:9711878): the cited paper is a prenatal
  diagnosis of CPS1D by a missense mutation; NO triglyceride content. Misassigned. REMOVE.
- GO:0032496 response to LPS (IDA PMID:15897806): CPS1 is released/fragmented into circulation under
  septic (LPS) conditions as a biomarker of hepatic mitochondrial injury; CPS1 is not a participant
  in the LPS-response process. Over-annotation of a downstream biomarker phenomenon.
  [PMID:15897806 "circulating CPS-1 might serve as a novel serum marker indicating mitochondrial impairment"]
- GO:0042645 mitochondrial nucleoid (IDA PMID:18063578): CPS1 co-purifies with native mtDNA nucleoids
  as an abundant matrix protein; the paper explicitly notes several metabolic proteins "were not
  observed to cross-link to mtDNA." Likely co-purification, not a genuine nucleoid localization.
- GO:0005730 nucleolus (IEA GO_REF:0000044 + IDA GO_REF:0000052) and GO:0005886 plasma membrane
  (IEA/ISS): UniProt does list Nucleus/nucleolus (PMID:22002106) and Cell membrane (by similarity to
  mouse Q8C196, "cell surface of hepatocytes"). These are unusual moonlighting/secondary localizations
  for a matrix enzyme; keep as non-core.
- Ensembl-Compara IEA response-to-stimulus terms (GO_REF:0000107): a large block of "response to X"
  (glucagon, cAMP, glucocorticoid, LPS, zinc, oleic acid, starvation, food, FGF, GH, dexamethasone,
  alcohol, amino acid, amine, steroid hormone, toxic substance, xenobiotic) plus liver/midgut/
  hepatocyte development and monoatomic anion homeostasis. These are expression-regulation /
  physiological-context transfers from rodent orthologs, not core function; keep as non-core.
- GO:0006207 de novo pyrimidine nucleobase biosynthetic process (IEA GO_REF:0000002) and GO:0090407
  organophosphate biosynthetic process (IEA GO_REF:0000117 ARBA): pyrimidine biosynthesis is CPS II
  (CAD), not CPS1; MODIFY/over-annotation. organophosphate is a broad ARBA mapping.
- GO:0006541 L-glutamine metabolic process (IBA/IEA): reflects the glutamine-dependent CPS family
  ancestor; human CPS1 does NOT use glutamine. Over-annotation.
