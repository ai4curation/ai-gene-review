# PYCR1 (human) — gene review notes

UniProt: P32322 (P5CR1_HUMAN); HGNC:9721; NCBI Gene 5831; chromosome 17q25.
Source files read: `PYCR1-uniprot.txt`, `PYCR1-goa.tsv`, cached `publications/PMID_*.md`,
`reactome/R-HSA-70664.md`. No deep-research file (falcon out of credits) — notes are
grounded directly in the local records.

## Core identity and function

PYCR1 is **pyrroline-5-carboxylate reductase 1**, EC 1.5.1.2, a mitochondrial
NAD(P)H-dependent oxidoreductase that catalyzes the **last step of proline
biosynthesis**: reduction of (S)-1-pyrroline-5-carboxylate (P5C) to L-proline.

- [file:human/PYCR1/PYCR1-uniprot.txt "Oxidoreductase that catalyzes the last step in proline"] /
  "biosynthesis, which corresponds to the reduction of pyrroline-5-" (CC FUNCTION, lines 238-239).
- UniProt CATALYTIC ACTIVITY: L-proline + NADP(+) = (S)-1-pyrroline-5-carboxylate + NADPH + 2 H(+)
  (RHEA:14109) and the NAD(+) counterpart (RHEA:14105); EC=1.5.1.2. PhysiologicalDirection is
  right-to-left, i.e. P5C -> proline.
- UniProt PATHWAY: [file:human/PYCR1/PYCR1-uniprot.txt "Amino-acid biosynthesis; L-proline biosynthesis; L-proline"]
  from L-glutamate 5-semialdehyde: step 1/1.
- Cofactor preference: [file:human/PYCR1/PYCR1-uniprot.txt "concentrations, has higher specific activity in the presence of NADH"]
  (physiologic conditions). Consistent with Reactome using the NADH reaction.
- GO term IDs verified against current ontology (OLS): GO:0004735 pyrroline-5-carboxylate reductase
  activity; GO:0055129 L-proline biosynthetic process; GO:1902792 pyrroline-5-carboxylate reductase
  complex; GO:0005759 mitochondrial matrix — all non-obsolete, labels current.

## Structure / assembly

- Homodecamer = pentamer of dimers. [PMID:16730026 "a decameric architecture with five homodimer subunits"]
  (first human crystal structure; also mutagenesis of Glu221, Rossmann motif).
- [PMID:28258219 "PYCR1 forms a concentration-dependent decamer in solution, consistent with the"]
  pentamer-of-dimers assembly (sedimentation velocity + crystallography). This paper corrected the
  earlier mis-assignment of the cofactor site: NADPH binds the N-terminal Rossmann fold, ~25 Å from
  the previously proposed C-terminal site. T238A mutant has decreased P5C reductase activity.
- Early biochemistry: [PMID:2722838 "suggesting that the native enzyme exists as a 10- to"] 12-mer
  (human erythrocyte enzyme; NADH vs NADPH kinetics; note this paper argued a possible NADP+-
  generating role in erythrocytes, i.e. proline oxidation direction — a cell-type-specific nuance).

## Localization

- Mitochondrion / mitochondrial matrix.
- [PMID:19648921 "an enzyme involved in proline metabolism, localizes to mitochondria"] (co-localization).
- [PMID:23024808 "are localized in the mitochondria, and primarily involved in the conversion of glutamate to proline"]
  (subcellular fractionation; PYCR1 & PYCR2 mitochondrial, PYCRL cytoplasmic).
- Reactome places the reaction in the mitochondrial matrix (R-HSA-70664, TAS).

## Substrate/route specialization (De Ingeniis 2012, PMID:23024808, full text)

- [PMID:23024808 "PYCR1 contributes primarily to production of proline from glutamate"]; under some
  conditions (no extracellular proline, high ornithine) it can also use the ornithine route, but this
  is unlikely physiological. PYCR2 exclusively glutamate route; PYCRL exclusively ornithine route.
- NADH-preferring, product-(proline)-inhibited (mitochondrial PYCRs).

## Disease

- UniProt DISEASE: ARCL2B [MIM:612940] and ARCL3B [MIM:614438] — autosomal recessive cutis laxa,
  progeroid/De Barsy-like. Caused by PYCR1 variants (evidence PubMed:19576563, 19648921, 22052856).
- [PMID:19648921] (Nat Genet): mutations cause cutis laxa with progeroid features; patient fibroblasts
  show altered mitochondrial morphology, membrane potential, and
  [PMID:19648921 "increased apoptosis rate upon oxidative stress were evident in fibroblasts from affected individuals"].

## Interactions / non-core roles

- DJ-1/PARK7: [PMID:23743200 "DJ-1 directly bound to PYCR1 in vivo and in"] vitro;
  [PMID:23743200 "DJ-1 enhanced the enzymatic activity of PYCR1 in vitro"];
  [PMID:23743200 "DJ-1 and PYCR1 colocalized in mitochondria"];
  [PMID:23743200 "involved in regulation of mitochondrial membrane potential"];
  [PMID:23743200 "cells knocked down for DJ-1 and PYCR1 showed lower viability under oxidative stress conditions"]
  — shared anti-oxidative-stress pathway.
- ORAOV1/LTO1: [PMID:24930674 "ORAOV1 bound to pyrroline-5-carboxylate reductase (PYCR), which is associated with proline metabolism"]
  and ROS production in esophageal cancer.
- TNPO2: binary interaction from HuRI interactome (PMID:32296183) — generic protein binding only.

## Curation decisions (summary)

- **Core**: GO:0004735 (MF), GO:0055129 (BP), GO:1902792 (complex), GO:0005759 mitochondrial matrix
  (location). All catalytic-activity, proline-biosynthesis, complex, and mitochondrial-localization
  annotations ACCEPTed (experimental IDA/IBA/IEA/TAS all concordant).
- **KEEP_AS_NON_CORE**: oxidative-stress response (GO:0034599), regulation of mitochondrial membrane
  potential (GO:0051881), the over-specific GO:1903377 (neuron intrinsic apoptotic — cell lines used,
  not neuron-specific), and the two identical-protein-binding (homo-oligomerization) annotations.
- **MARK_AS_OVER_ANNOTATED** (not REMOVE — experimental IPI): the three bare "protein binding"
  (GO:0005515) annotations (DJ-1, TNPO2, ORAOV1/LTO1). Interactions are real but the plain MF term is
  uninformative; per policy these IPI annotations are marked over-annotated rather than removed.
- No annotations REMOVEd. No experimental annotations removed.
