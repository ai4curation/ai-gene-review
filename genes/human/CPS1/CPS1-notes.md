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


## 2026-10-12: source-specific reassessment

This dated assessment supersedes incompatible interpretations in the preserved earlier journal, especially the blanket rejection of non-mitochondrial pools, all response annotations, and all positive binding screens. The original observations remain visible; biological conclusions below distinguish measured activity, association, expression markers and unresolved source scope.

### Catalysis and products

CPS1 performs ammonia-dependent carbamoyl-phosphate synthesis, with two ATP-dependent phosphorylation steps, NAG activation and catalytic Mg/K. The compact functional synthesis is one GO:0004087 core in mitochondrial matrix, linked to carbamoyl-phosphate biosynthesis and the urea cycle. The structures contain ADP rather than directly imaged ATP. [PMID:26592762, "N-acetyl-L-glutamate (NAG) as essential activator"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4655335/)

The [2013 original author-uploaded paper](https://www.researchgate.net/publication/236643612_Molecular_Characterization_of_Carbamoyl-Phosphate_Synthetase_CPS1_Deficiency_Using_Human_Recombinant_CPS1_as_a_Key_Tool) describes residues 40–1500 plus a 28-residue His tag; the 2015 construct deletes residues 1–37. Neither is silently equated with the official alternative products. The listed 2013 corrigendum, PMID:30740827, is authenticated but its operative text remains inaccessible. Native-human and independent 2015 evidence also support the reaction. Full Methods for PMID:24813853 and PMID:6249820 remain unavailable; their positive experimental claims are retained with explicit curator deference.

The official sequences reconstruct to 1500, 1049 and 1506 residues. Product 2 loses residues 1–451; product 3 replaces the initial methionine with MPQIIKM. Sequence retention does not establish equivalent import, processing or catalytic coupling. The human splice-defect paper PMID:8486760 reports 11% residual liver activity, and PMID:7416778 reports approximately half mean control duodenal activity; neither supports a universal complete-abolition statement.

### Ancestral inference and specific chemistry

The human leaf genuinely descends from the current cytoplasm, glutamine and ammonia IBD nodes. The target sequence and current MSA agree exactly. Off-path IRDs, including the shared-source addition at PTN000892125, are not human loss annotations. A target among its own experimental descendants is legitimate support.

The glutamine-hydrolyzing MF is refined to the established ammonia reaction, explicitly considering the inherited contributes_to qualifier: a bacterial large chain can contribute without possessing a glutaminase. Human CPS1 is a single-chain ammonia enzyme, rather than an established partnered human glutamine-hydrolyzing complex. In contrast, GO:0006541 covers pathways; loss of direct hydrolysis alone does not resolve every downstream pathway participation, so the broad BP remains UNDECIDED. The retrieved GO:0090407 definition has an apparent deoxyribose-specific wording anomaly; the actual carbamoyl-phosphate biosynthetic term supplies precise positive coverage.

### Cancer metabolism and the operative correction

In KRAS/LKB1-mutant lung-cancer cells, CPS1 depletion/rescue and isotope tracing support a context-dependent contribution of ammonia nitrogen to pyrimidines. [PMID:28538732, "from ammonia into pyrimidines"](https://pmc.ncbi.nlm.nih.gov/articles/PMC5472349/)

The [operative Nature correction](https://www.nature.com/articles/s41586-019-1133-3) must accompany that interpretation: the reported m/z 140/79 signal "was phosphorylethanolamine, not carbamoyl phosphate" [PMID:31043737]. Carbamoyl phosphate was below the assay threshold, and the original Letter was not corrected online. The correction does not withdraw the separate pyrimidine tracing and dependency results. No measured carbamoyl-phosphate accumulation is used here.

### Binding, localization and conditional complexes

The exact positive Raf interactions used CPS1 residues 420–771 and defined RAF1/ARAF fragments. Their known MAP kinase kinase kinase class supports a binding refinement, without making CPS1 a kinase. The 14-3-3 affinity/TAP results similarly support the partner class while leaving direct topology unresolved. PMID:20618440 Table 2 misdescribes CPS1 as CAD; the actual CPS1 identification and positive curated pair remain distinct from that background error.

The [original nucleoid study](https://www.researchgate.net/publication/5783906_The_Layered_Structure_of_Human_Mitochondrial_DNA_Nucleoids) identifies CPS1 NP_001866 as "Class I" [PMID:18063578], with native TFAM/mtSSB peptide counts 5/21 and crosslinked counts 21/0. The old no-crosslink premise is incorrect. Association in these preparations does not establish autonomous DNA binding or a nucleoid-maintenance mechanism.

The cell-surface transfer is supported by actual mouse hepatocyte experiments, including the "surface of non-permeabilized primary mouse hepatocytes" [PMID:34799567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8604956/). The human HepG2 functional experiments and mouse surface imaging are separate. The reported ELISA uses hepatocyte lysate, so it is not relabeled as a purified-human binary-binding assay. HPA nucleolar metadata and the ethanol-study cytosolic detection are also retained at their specific assay scope. No HPA image pixels were inspected.

Rat calcium/phospholipid binding and the SBTI-associated CPS1/FDH/BHMT complex are positive secondary observations, not disproven by predominant monomeric enzyme in a different preparation. PMID:17669278 Figure 4 tests FDH/SBTI directly; it does not resolve a CPS1-specific interaction with an assembled complex. The putative native proteolytic fragment in PMID:15304357 remains uncertain at human/full-length scope. Full-text access is not invented where recovery failed.

### Responses, developmental markers and pathway scope

The rat LPS study measures altered ureagenic output: "decreased UNSR by 40%" [PMID:17539997]. This differs from the separate observation of LPS-induced circulating CPS1 in humans and baboons, but the broad response definition accommodates both at their actual scope. The alcohol study also measures a significant 2.27-fold protein increase after eight weeks, separately from its protein-damage experiments. No repair or protective activity is inferred from those observations.

The broad response terms explicitly include gene expression, enzyme production and changes of state. The observed toxicant, oleate, FGF4 and glucocorticoid-dependent CPS1 changes can therefore support existing non-core response annotations without an additional protective/signaling requirement. In contrast, the developmental terms concern progression to a mature organ or cell phenotype; abstract-only developmental expression/marker studies leave their exact participation claims UNDECIDED. This distinction preserves positive evidence without treating every expressed marker as a developmental effector.

Citrulline biosynthesis is a pathway: CPS1 performs upstream precursor synthesis even though OTC performs the final citrulline-forming reaction. Vascular, nitric-oxide, homocysteine, triglyceride and monoatomic-anion claims retain explicit uncertainty where exact source/mechanistic scope remains unresolved. This does not treat all expression observations as participation or all indirect phenotypes as false.

### Historical and current source representation

The reconciled review has 79 active assertions and two retired historical source forms. All 78 original assertion objects remain unchanged, including 49 omitted WITH/FROM lists; complete modern identities are separately listed in the evidence index. The retired InterPro-only metal record and aggregate Raf record are not biological removals. All three original product records and all 30 original reference identities/findings remain preserved. The evidence index supplies source provenance and literal records, not independent experimental evidence.


## 2026-10-12: targeted evidence clarification

This dated clarification supersedes the earlier calcium-binding retention and downstream-nitrogen rationale above. It preserves the historical journal and positive experimental observations. Electronic annotation methods are evaluated from their actual sources; they are neither categorically protected nor rejected. Supported non-core claims require positive evidence. UNDECIDED marks an unresolved claim and is not acceptance. The action distribution is an outcome of those decisions, not a removal quota.

### Secondary binding and pathway scope

The rat calcium study reports a roughly 130-kDa binding band but the accessed abstract does not explain its CPS1 identification. That is appreciably smaller than intact human CPS1. The identity or processing explanation and human transfer remain UNDECIDED; catalytic Mg/K dependence and missing calcium in particular structures do not invalidate a calcium-binding assay by themselves. [PMID:9506839](https://pubmed.ncbi.nlm.nih.gov/9506839/) remains an abstract-only source.

The phospholipid annotation is refined to cardiolipin binding, GO:1901612, using the positive selective-interaction result in [PMID:1898084](https://pubmed.ncbi.nlm.nih.gov/1898084/). Other tested anionic phospholipids also interacted, so the refinement does not claim cardiolipin exclusivity. The three ligand annotations that converge on GO:0072341 retain their different original sources; this is precision of existing assertions rather than three new functions.

For GO:0006541, the unresolved question is the actual human pathway step represented by the ancestral or domain-derived annotation. Direct glutamine hydrolysis is lost, and ammonia-specific catalysis supports the molecular-function replacement. That biochemical result alone does not settle every multistep process in the broader term, while a possible nitrogen origin supplies no positive participation evidence. Both process rows therefore remain UNDECIDED.

The [2010 14-3-3 original](https://doi.org/10.1111/j.1742-4658.2010.07730.x), Tables 1–2 and the TAP Methods, reports mitochondrial CPS1 among the ceramide-condition isolates. Its CAD background explanation is incorrect and is not transferred to CPS1. The measured partner class supports 14-3-3 protein binding at association scope; neither direct contact nor a CPS1 apoptosis mechanism is asserted. The 2004 GST-bait observation and the 2010 TAP observation retain distinct assay descriptions.

### Direct source access and ontology wording

The [full publisher correction](https://doi.org/10.1038/s41586-019-1133-3), in its first body paragraph, explicitly describes the MRM 140/79 transition and the exact quotation already retained above. This full text is distinct from the shorter cached correction summary. The misidentified signal, more selective follow-up transitions and below-threshold carbamoyl-phosphate result are stated in the correction itself; the original Letter was not corrected online. No new quotation is added here.

The GO:0070409 refinement rests directly on CPS1 chemistry. Raw [QuickGO GO:0090407](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0090407) and [OLS GO:0090407](https://www.ebi.ac.uk/ols4/ontologies/go/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0090407) responses on 2026-10-12 both pair its organophosphate label with a deoxyribose-specific definition. This is an observed service response, not a locally combined child definition; no causal diagnosis of the ontology or API is needed for the annotation decision. The original source identifier remains unchanged.

For stable navigation to the previously read originals, use [PMID:18063578 DOI](https://doi.org/10.1074/jbc.M708444200) and [PMID:23649895 DOI](https://doi.org/10.1002/humu.22349) only as authenticated identifiers where noted in the source index. The evidence index distinguishes canonical publication locators from the actual author-upload or indexed access route. Its captured records and hashes document provenance, not new experiments or independent corroboration.


## 2026-10-12: association scope and inspectable source text

The homocysteine-process judgment is now MARK_AS_OVER_ANNOTATED, superseding the earlier UNDECIDED call. The complete available Results in [PMID:20031578](https://doi.org/10.1161/CIRCGENETICS.108.829804) establish a replicated, female-specific genotype–plasma-homocysteine association. Its Discussion explicitly leaves the mechanism open [PMID:20031578 "further biological experiments are needed"]. This is positive evidence of the reported study's scope: it does not identify a CPS1-performed homocysteine reaction or pathway step. Full Methods remain unrecovered; the judgment does not assert that all possible experiments were excluded or that the association is false. The preserved IDA code is not rewritten.

The distinct [PMID:14718356](https://doi.org/10.1161/01.HYP.0000112424.06921.52) abstract reports real vascular challenge responses and nitric-oxide metabolite measurements. Its vasodilation and nitric-oxide-process assertions remain UNDECIDED because the performed pathway contribution is unresolved at the accessed scope. A precursor-synthesis role and an indirect genotype association are not interchangeable, and no universal genotype-association rule is applied.

The quotation and MRM 140/79 statement in the earlier cancer-metabolism entry are attributed to the **publisher Amendment, DOI:10.1038/s41586-019-1133-3, first main body paragraph**, not to the shorter machine-cached summary. The [short exact passage and precise public locator](CPS1-primary-excerpts.md#publisher-amendment-doi101038s41586-019-1133-3) make this distinction inspectable without claiming that the cache contains the full paragraph. The misidentified signal and below-threshold carbamoyl-phosphate result remain unchanged.

The GO:0090407 wording observation is a dated service-response observation, not a diagnosis of an ontology defect. The [source excerpt file](CPS1-primary-excerpts.md#dated-go0090407-service-fields) now reproduces the exact target IDs, labels and returned definition fields from both successful responses; the [evidence index](CPS1-evidence-index.yaml) retains the retrieval URLs, times, field paths and full-response hashes. These literal fields establish what was captured and remain inspectable offline even if the live services later change. They are not biological evidence for the replacement, which rests on CPS1's directly demonstrated carbamoyl-phosphate chemistry.
