# hutI (PA5092, Q9HU91) notes

## Identity

- UniProt Q9HU91 (HUTI_PSEAE), 402 aa, Swiss-Prot reviewed but PE 3 (inferred from
  homology). All functional annotation in the entry is HAMAP-Rule MF_00372 based
  [file:PSEAE/hutI/hutI-uniprot.txt "Catalyzes the hydrolytic cleavage of the carbon-nitrogen bond
  in imidazolone-5-propanoate to yield N-formimidoyl-L-glutamate"].
- Family: metallo-dependent hydrolase (amidohydrolase) superfamily, HutI family
  (HAMAP MF_00372, NCBIfam TIGR01224 hutI, InterPro IPR005920, PANTHER PTHR42752).
  HAMAP predicts metal ligands at 66, 68, 236, 311 and substrate/product contacts at 75,
  138, 171, 239, 313, 315, 316.
- Located in the PAO1 hut cluster (PA5091 hutG ... PA5106 hutF), next to hutG (PA5091).

## Biology (literature)

- HutI is the third enzyme of the universal histidine degradation pathway, hydrolysing
  4-imidazolone-5-propanoate to N-formimino-L-glutamate (FIGLU)
  [PMID:16990261 "Imidazolonepropionase (EC 3.5.2.7) catalyzes the third step in the universal histidine degradation pathway"].
  The B. subtilis HutI crystal structure shows a TIM-barrel amidohydrolase fold with a
  zinc ion in the active site and a substrate analog bound beside it
  [PMID:16990261 "X-ray fluorescence scan analysis confirmed that the bound metal ion was a zinc ion."].
  A further structure exists for A. tumefaciens HutI (PMID:17640072, abstract not available).
- In P. aeruginosa the first three steps are catalysed by HutH, HutU and HutI
  [PMID:16475788 "The first three steps for the degradation of histidine include the action of HutH, HutU, and HutI to convert L-histidine to N-formimino-L-glutamate."].
  Downstream, FIGLU is degraded by two branches (HutE four-step; HutF/HutG five-step)
  [PMID:22225844 "the histidine uptake and utilization (hut) pathway of Pseudomonas aeruginosa PAO1 contains two branches from the intermediate formiminoglutamate to the product glutamate"].
  The HutI step is common to both branches
  [PMID:17717196 "are common to both the four-step and the five-step pathways"].
- hutI sits in the HutC-repressed hutU-hutG operon, which is induced by urocanate (PMID:41641996;
  PMID:17717196 for P. fluorescens).
- I found no P. aeruginosa paper that assays imidazolonepropionase in PAO1 extracts, or that
  reports a hutI mutant. Imidazolonepropionase is rarely assayed directly because its
  substrate is unstable. This is my own background knowledge, not a cited fact.

## PMID:4290562 (Lessie & Neidhardt 1967), the PseudoCAP seed reference

- Abstract only. PMC276695 is a scanned article. MCP full text came back empty, and the
  PMC PDF is behind a browser challenge, so I could not read the full text.
- The abstract names the enzymes it studied: histidase (step I), urocanase (step II) and
  FIGLU degradation (step IV)
  [PMID:4290562 "Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine"].
  Step III, imidazolonepropionase, is the only step it does not mention. The abstract
  describes urocanase-deficient mutants, a histidine auxotroph, and catabolite-repression
  mutants, but no step III mutant.
- The paper predates gene cloning, so it cannot link any activity to PA5092. Nothing
  visible in it supports "imidazolonepropionase activity" or an IMP for hutI in
  "L-histidine catabolic process". The claims themselves are almost certainly true; the
  reference is what fails to support them.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000505272 | GO:0050480 imidazolonepropionase activity | 1 (sole seed) | 52 (50 taxa) | GO:0050480 imidazolonepropionase activity, IMP, PMID:4290562 (PseudoCAP) | UNVERIFIABLE | The 1967 paper (abstract only) studies steps I, II and IV and never mentions step III or a hutI mutant. It predates genes, so it cannot tie the activity to PA5092. The term itself is right for the clade: HutI is a conserved, HAMAP/TIGRFAM-defined family with a solved B. subtilis structure, and the node (LUCA, covering bacterial HutI and eukaryotic AMDHD1) fits a universal pathway enzyme. So the IBD's conclusion is sound but its only evidential anchor is not. It should be re-anchored on a characterized HutI if one exists. |
| PTN000505272 | GO:0006548 L-histidine catabolic process | 1 (sole seed) | 52 (50 taxa) | GO:0006548 L-histidine catabolic process, IMP, PMID:4290562 (PseudoCAP) | UNVERIFIABLE | Same paper, same problem: no hutI mutant is described. The process claim is correct (HutI performs step III of the pathway), and the node term suits the clade. The seed reference is the weak point. |

Leaf IBAs from this node include human AMDHD1 and mouse/rat Amdhd1, so the single
PseudoCAP seed supports the imidazolonepropionase IBAs on mammals too.

## Decisions summary

- ACCEPT: imidazolonepropionase activity (IBA, IEA, IMP), L-histidine catabolic process
  (IBA, IEA, IMP), cytoplasm (IEA).
- IMP rows are accepted on independent evidence (HAMAP family, structural homologs,
  operon context). Each carries a PSEUDOCAP source defect (WRONG_REFERENCE, CHECK, PROBABLE)
  because the cited abstract does not cover step III.
- The IBA MF row carries a GO_CENTRAL CHECK defect (SUSPECTED): the IBD at PTN000505272
  rests solely on this seed.
- MODIFY to GO:0050480: hydrolase activity; hydrolase activity acting on C-N (non-peptide)
  bonds; same in cyclic amides (all IEA, correct but general).
- KEEP_AS_NON_CORE: zinc ion binding, iron ion binding (HAMAP cofactor, Zn or Fe).
