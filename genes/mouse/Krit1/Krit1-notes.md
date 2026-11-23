# Krit1 (mouse, Q6S5J6) review notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted. This review treats mouse Krit1 in its own right and
separates functions shown with mouse material from functions inferred from human KRIT1
(O00522).

### Deep research

`just deep-research-falcon mouse Krit1 --fallback perplexity-lite` failed: the Edison
API returned `403 Forbidden` on `/auth/login`, and the perplexity-lite fallback also
exited non-zero. No deep-research file exists for this gene. The review was written from
the cached publications listed below, the mouse UniProt record, and (as orthology
background only) the completed human KRIT1 review.

### Evolutionary grounding

- PANTHER: Q6S5J6 is in PTHR13283:SF11 (KREV INTERACTION TRAPPED PROTEIN 1), the same
  subfamily as human KRIT1 O00522 and zebrafish krit1 (F1REV3)
  [file:mouse/Krit1/Krit1-uniprot.txt "PANTHER; PTHR13283:SF11; KREV INTERACTION TRAPPED PROTEIN 1; 1."].
  The FRMD8 subfamilies of PTHR13283 have a different function (iRhom/ADAM17 stabilization),
  so nothing is transferred between KRIT1 and FRMD8.
- PAINT (interpro/panther/PTHR13283/PTHR13283-paint.tsv): mouse Krit1 (MGI:1930618) is an IBD
  seed at PTN002665063 for cell redox homeostasis (GO:0045454) and regulation of establishment
  of cell polarity (GO:2000114), and at PTN002665064 (vertebrates) for negative regulation of
  angiogenesis (GO:0016525). Microtubule binding at PTN002665063 is seeded by human only;
  A/P axis specification at PTN002665063 by zebrafish only; plasma membrane at PTN004412369
  (eukaryotes) by human, FRMD8 and a worm gene.
- ISO/ISS/Ensembl-Compara rows all come from human O00522, a 1:1 ortholog in the same
  subfamily; these transfers are evolutionarily sound, but they are inferences, not mouse data.

### What is shown with mouse Krit1 or mouse cells (experimental in this species)

- Embryonic vascular requirement: Krit1-null embryos die mid-gestation with primary vascular
  defects (dilated cranial vessels from E8.5, enlarged caudal dorsal aorta with increased EC
  proliferation, narrowed branchial arch arteries) and loss of arterial Efnb2/Notch markers
  [PMID:14993192 "Homozygous mutant embryos die in mid-gestation and the first detectable defects are exclusively vascular in nature"].
- Endothelial barrier / RhoA-ROCK: Krit1+/- mouse ECs have twofold higher monolayer
  permeability and raised pMLC; Krit1+/- mice show increased brain and lung leak reversed
  by fasudil [PMID:20308363 "Krit1+/− endothelial monolayers were twofold more permeable than WT."].
- ROS homeostasis: Krit1-/- MEFs have elevated ROS, lower SOD2/FoxO1, and ROS falls on
  re-expression [PMID:20668652 "ROS levels in KRIT1(-/-) cells are significantly and dose-dependently reduced after restoration of KRIT1 expression"].
- Autophagy: Krit1-KO MEFs show suppressed autophagy via mTOR up-regulation [PMID:26417067].
  Indirect; not annotated.
- HEG1-KRIT1-CCM2: mouse KRIT1 expressed in HEK293 is pulled down by the HEG1 tail and
  greatly enhances CCM2 recruitment to it
  [PMID:19151727 "demonstrating that KRIT1 significantly facilitates CCM2 interaction with the HEG1 receptor tail"].
- CCM2/CCM2L competition for CCM1 binding [PMID:22898778]; Nd1-L (Ivns1abp) binding
  needing an intact FERM domain (isoform KRIT1A but not KRIT1B) [PMID:22970292].
- Endocardial Krit1 deletion (Nfatc1Cre;Krit1fl/fl) causes MEKK3-dependent Klf2/Klf4 and
  Adamts4/5 up-regulation and loss of cardiac jelly [PMID:25625206]; neonatal endothelial
  deletion gives MEKK3-KLF2/4-dependent lesions [PMID:27027284] and EndMT [PMID:23748444].
  These are organismal or transcriptional outputs. The step that restrains MEKK3 is
  done by CCM2 (it binds MEKK3), so no MAPK-regulation term is proposed for Krit1.

### What is inferred from human KRIT1 (same subfamily) and not shown with mouse protein

- Rap1 effector binding through the FERM F1/F2 lobes (PMID:9285558, PMID:21633110,
  PMID:22577140; human protein).
- Microtubule binding and PI(4,5)P2 binding (PMID:17916086; human protein).
- ICAP1 competition with beta1 integrin (PMID:23317506; human protein).

### Decisions

- Bare protein binding: REMOVE, except PMID:19151727 (HEG1), MODIFY → protein-macromolecule
  adaptor activity, because the paper shows KRIT1 bridging CCM2 to the HEG1 tail.
- GTPase regulator activity → MODIFY to small GTPase binding (effector, not GAP/GEF).
- integrin activation → MODIFY to positive regulation of integrin activation (same as human).
- regulation of angiogenesis (NAS) → MODIFY to negative regulation of angiogenesis.
- cytoskeleton → MODIFY to microtubule cytoskeleton; anchoring junction → MODIFY to
  adherens junction (same as human).
- A/P axis specification IBA → REMOVE: its only seed is a zebrafish knockdown body-axis
  phenotype, an organismal consequence, not axis patterning.
- Angiogenesis/proliferation/migration/apoptosis/polarity/redox: KEEP_AS_NON_CORE (true
  downstream outputs of the junctional adaptor role).
- NEW: negative regulation of Rho protein signal transduction (GO:0035024) from mouse
  Krit1+/- ECs (PMID:20308363). Krit1 does part of this work: it is a junctional component
  of the complex that holds RhoA/ROCK down, not only a substrate or a read-out.
  The comparator check is consistent with this: the human KRIT1 review proposes the same
  term from PMID:21633110.
- No vasculogenesis / blood vessel development term was added: the Krit1-/- phenotype
  shows the gene is necessary, which does not say which step Krit1 itself performs.
