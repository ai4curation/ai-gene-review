---
title: "Alzheimer Disease Gene Review Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [APP, PSEN1, PSEN2, APOE, TREM2, SORL1, ABCA7, ADAM10, BACE1, NCSTN, APH1A, APH1B, PSENEN, CLU, BIN1, PICALM, CD33, CR1, CD2AP, INPP5D, PLCG2, ABI3, SPI1, MS4A4A, MS4A6A, EPHA1, FERMT2, CASS4, MAPT, GSK3B, CDK5, CDK5R1, LRP1, ABCA1]
---

# Alzheimer Disease Gene Review Project

## Overview

This project reviews human GO annotations for genes central to Alzheimer disease
genetics and biology. The scope combines Mendelian/familial Alzheimer disease
genes, high-confidence common and rare variant risk genes, and pathway genes
needed to curate reusable disease-relevant modules.

The initial project focus is human Alzheimer disease (`MONDO:0004975`) with
module curation in the root-level `modules/` directory.

## Model Species

**Primary: Homo sapiens (human)**

- UniProt species code: HUMAN
- Review scope: human gene annotation reviews plus pathway/module curation
- Initial gene set: bounded seed list for review; not every included gene is
  asserted to be independently causal for Alzheimer disease

## Genes for Review

### Priority 1: Foundational Alzheimer Genetics

| Gene | Rationale |
|------|-----------|
| APP | Amyloid precursor protein; central substrate for amyloid beta production |
| PSEN1 | Familial Alzheimer disease presenilin; gamma-secretase catalytic subunit |
| PSEN2 | Familial Alzheimer disease presenilin; gamma-secretase catalytic subunit |
| APOE | Major late-onset Alzheimer disease risk locus; lipid transport and amyloid clearance |
| TREM2 | Rare-variant microglial risk gene; innate immune signaling |
| SORL1 | Endosomal APP trafficking and amyloid processing risk gene |
| ABCA7 | Lipid transport/phagocytosis risk gene |
| ADAM10 | Alpha-secretase in non-amyloidogenic APP processing |

### Priority 2: Amyloid Processing and Tau Biology

| Gene | Module context |
|------|----------------|
| BACE1 | Beta-secretase initiating amyloidogenic APP processing |
| NCSTN | Gamma-secretase complex maturation and substrate recognition |
| APH1A | Gamma-secretase complex subunit |
| APH1B | Gamma-secretase complex subunit; AD-associated target signal in Open Targets |
| PSENEN | Gamma-secretase complex stabilizing subunit |
| MAPT | Tau pathology axis; microtubule-associated tau |
| GSK3B | Tau phosphorylation and kinase signaling context |
| CDK5 | Neuronal kinase implicated in tau phosphorylation biology |
| CDK5R1 | CDK5 regulatory subunit; neuronal kinase activation context |

### Priority 3: Lipid, Endocytosis, Complement, and Microglial Risk Network

| Gene | Module context |
|------|----------------|
| CLU | Apolipoprotein/chaperone risk gene; amyloid handling and complement context |
| BIN1 | Endocytosis and membrane remodeling risk gene |
| PICALM | Clathrin-mediated endocytosis and APP/ApoE trafficking risk gene |
| CD33 | Microglial immune receptor risk gene |
| CR1 | Complement receptor risk gene |
| CD2AP | Endocytosis/cytoskeletal adaptor risk gene |
| INPP5D | SHIP1; microglial phosphoinositide signaling risk gene |
| PLCG2 | Rare coding variant microglial signaling risk gene |
| ABI3 | Rare coding variant microglial cytoskeletal/immune risk gene |
| SPI1 | PU.1 transcription factor; myeloid/microglial regulatory risk locus |
| MS4A4A | MS4A locus representative; microglial/lipid biomarker genetics |
| MS4A6A | MS4A locus representative; Alzheimer disease GWAS signal |
| EPHA1 | Endocytosis/immune signaling risk gene |
| FERMT2 | Integrin/cytoskeletal adaptor risk gene |
| CASS4 | Cytoskeletal adaptor risk gene |
| LRP1 | ApoE receptor and APP/amyloid clearance pathway component |
| ABCA1 | ApoE lipidation and cholesterol efflux pathway component |

## Pathway Modules

Curate disease-relevant pathway and complex models as `ModuleReview` YAML files
under `modules/`:

| Module | Scope |
|--------|-------|
| `modules/alzheimer_disease_pathways.yaml` | Validated overview module with parts for APP processing/amyloid-beta handling, lipid/lipoprotein transport, microglial lipid-debris sensing, tau/cytoskeletal kinase biology, and endocytic/adhesion adaptor systems |

Rendered module page: `pages/modules/alzheimer_disease_pathways.html`.

Validate each module with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/<module>.yaml
```

## Source Anchors

- Open Targets Platform query for Alzheimer disease (`MONDO_0004975`), accessed
  2026-06-19. Top associated targets included APP, PSEN1, PSEN2, APOE, SORL1,
  ADAM10, TREM2, ABCA7, CLU, BIN1, PLCG2, and APH1B.
- GWAS Catalog REST query for `efo_trait=Alzheimer disease`, accessed
  2026-06-19, used to confirm the disease trait mapping and GWAS context.
- Bellenguez et al. 2022, "New insights into the genetic etiology of Alzheimer's
  disease and related dementias" ([PMID 35379992](https://pubmed.ncbi.nlm.nih.gov/35379992/)).
- Kunkle et al. 2019, "Genetic meta-analysis of diagnosed Alzheimer's disease
  identifies new risk loci and implicates amyloid beta, tau, immunity and lipid
  processing" ([PMID 30820047](https://pubmed.ncbi.nlm.nih.gov/30820047/)).
- Sims et al. 2017, "Rare coding variants in PLCG2, ABI3, and TREM2 implicate
  microglial-mediated innate immunity in Alzheimer's disease"
  ([PMID 28714976](https://pubmed.ncbi.nlm.nih.gov/28714976/)).

---

# STATUS

- [x] Create project scope and seed gene list
- [x] Fetch UniProt, GOA, and publication caches for all frontmatter genes
- [x] Run deep research or record manual notes for Priority 1 genes
- [x] Complete Priority 1 gene annotation reviews
- [x] Draft and validate Alzheimer pathway modules under `modules/`
- [x] Review Priority 2 and Priority 3 genes
- [x] Render project page and update project index

# NOTES

## 2026-06-19

- Created project scaffold with 34 human seed genes.
- Seed list is intentionally mixed: Mendelian AD genes, late-onset AD risk genes,
  and mechanistic pathway genes required for module curation.
- Open Targets and GWAS Catalog were used as scoping anchors; per-gene reviews
  still need the standard `just fetch-gene human <GENE>` and deep-research steps
  before curation decisions.
- Fetched and seeded missing Priority 1 gene data for PSEN1, PSEN2, APOE, TREM2,
  SORL1, ABCA7, and ADAM10. Publication-cache confirmation is complete for these
  genes: PSEN1 57/57, PSEN2 18/18, APOE 104/104, TREM2 31/31, SORL1 34/34,
  ABCA7 7/7, and ADAM10 44/44. Falcon deep research for PSEN1 stalled without
  writing an artifact; direct perplexity-lite failed with a 401 insufficient-quota
  error, so manual notes were started in `genes/human/PSEN1/PSEN1-notes.md`.
- Completed PSEN1 first-pass review: all 197 seeded GO annotations have review
  actions, core gamma-secretase function is defined, knowledge gaps are in
  `genes/human/PSEN1/PSEN1-notes.md`, and `just validate human PSEN1` passes
  cleanly. Action distribution: 65 ACCEPT, 52 KEEP_AS_NON_CORE, 57
  MARK_AS_OVER_ANNOTATED, 7 MODIFY, 16 UNDECIDED.
- Completed PSEN2 first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/PSEN2/PSEN2-notes.md` from cached UniProt/GOA/publication
  evidence. All 79 seeded GO annotations have review actions, core PSEN2
  gamma-secretase function is defined with late endosome/lysosome emphasis, and
  `just validate human PSEN2` passes cleanly. Action distribution: 40 ACCEPT, 24
  KEEP_AS_NON_CORE, 11 MARK_AS_OVER_ANNOTATED, 4 UNDECIDED.
- Completed APOE first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/APOE/APOE-notes.md` from cached UniProt/GOA/publication evidence.
  All 293 seeded GO annotations have review actions, core APOE
  lipid-transfer/lipoprotein-clearance functions are defined, and `just validate
  human APOE` passes cleanly. Action distribution: 145 ACCEPT, 120
  KEEP_AS_NON_CORE, 28 MARK_AS_OVER_ANNOTATED.
- Completed TREM2 first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/TREM2/TREM2-notes.md` from cached UniProt/GOA/publication
  evidence. All 273 seeded GO annotations have review actions, core TREM2
  lipid/apolipoprotein ligand-sensing and TYROBP-linked receptor signaling
  functions are defined, and `just validate human TREM2` passes cleanly. Action
  distribution: 117 ACCEPT, 151 KEEP_AS_NON_CORE, 5 MARK_AS_OVER_ANNOTATED.
- Completed SORL1 first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/SORL1/SORL1-notes.md` from cached UniProt/GOA/publication
  evidence. All 168 seeded GO annotations have review actions, core SORL1 cargo
  receptor, APP/amyloid-beta sorting, and Golgi/endosomal trafficking functions
  are defined, and `just validate human SORL1` passes cleanly. Action
  distribution: 92 ACCEPT, 44 KEEP_AS_NON_CORE, 25 MARK_AS_OVER_ANNOTATED, 4
  MODIFY, 3 UNDECIDED.
- Completed ABCA7 first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/ABCA7/ABCA7-notes.md` from cached UniProt/GOA/publication
  evidence. All 81 seeded GO annotations have review actions, core ABCA7
  ATP-coupled phospholipid transport, apoA-I phospholipid efflux, and
  phagocytic/amyloid-clearance functions are defined, and `just validate human
  ABCA7` passes cleanly. Action distribution: 55 ACCEPT, 20 KEEP_AS_NON_CORE, 4
  MODIFY, 2 MARK_AS_OVER_ANNOTATED.
- Completed ADAM10 first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/ADAM10/ADAM10-notes.md` from cached UniProt/GOA/publication
  evidence. All 151 seeded GO annotations have review actions, core ADAM10
  metalloendopeptidase/ectodomain-shedding, APP alpha-secretase, Notch, and
  regulated membrane-localization functions are defined, and `just validate
  human ADAM10` passes cleanly. Action distribution: 88 ACCEPT, 42
  KEEP_AS_NON_CORE, 19 MARK_AS_OVER_ANNOTATED, 1 MODIFY, 1 REMOVE.
- Fetched and seeded amyloid/gamma-secretase pathway batch data for BACE1,
  NCSTN, APH1A, APH1B, and PSENEN. Seeded GOA annotation counts: BACE1 140,
  NCSTN 99, APH1A 73, APH1B 43, PSENEN 71.
- Completed BACE1 first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/BACE1/BACE1-notes.md` from cached UniProt/GOA/publication
  evidence. All 140 seeded GO annotations have review actions, core BACE1
  beta-secretase/aspartyl endopeptidase, APP beta-cleavage, amyloid-beta
  formation, and TGN/endosomal trafficking functions are defined, and `just
  validate human BACE1` passes cleanly. Action distribution: 94 ACCEPT, 24
  KEEP_AS_NON_CORE, 20 MARK_AS_OVER_ANNOTATED, 2 MODIFY.
- Completed NCSTN first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/NCSTN/NCSTN-notes.md` from cached UniProt/GOA/publication
  evidence. All 99 seeded GO annotations have review actions, core nicastrin
  gamma-secretase complex adaptor/substrate-recruitment contribution to
  intramembrane aspartyl endopeptidase activity is defined, and `just validate
  human NCSTN` passes cleanly. Action distribution: 73 ACCEPT, 12
  KEEP_AS_NON_CORE, 10 MARK_AS_OVER_ANNOTATED, 4 MODIFY.
- Completed APH1A first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/APH1A/APH1A-notes.md` from cached UniProt/GOA/publication
  evidence. All 73 seeded GO annotations have review actions, core APH1A
  gamma-secretase complex adaptor/assembly contribution to intramembrane
  aspartyl endopeptidase activity is defined, and `just validate human APH1A`
  passes cleanly. Action distribution: 50 ACCEPT, 12 KEEP_AS_NON_CORE, 9
  MARK_AS_OVER_ANNOTATED, 2 MODIFY.
- Completed APH1B first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/APH1B/APH1B-notes.md` from cached UniProt/GOA/publication
  evidence. All 43 seeded GO annotations have review actions, core APH1B
  gamma-secretase complex adaptor/assembly contribution to intramembrane
  aspartyl endopeptidase activity is defined with APH1B-specific substrate
  preference questions, and `just validate human APH1B` passes cleanly. Action
  distribution: 37 ACCEPT, 4 MARK_AS_OVER_ANNOTATED, 1 MODIFY, 1
  KEEP_AS_NON_CORE.
- Completed PSENEN first-pass review: falcon deep research timed out after 180
  seconds without writing an artifact, so manual notes were created in
  `genes/human/PSENEN/PSENEN-notes.md` from cached UniProt/GOA/publication
  evidence. All 71 seeded GO annotations have review actions, core PEN-2
  gamma-secretase endopeptidase-activator contribution, presenilin
  endoproteolysis, complex stability, trafficking, and APP/Notch processing
  functions are defined, and `just validate human PSENEN` passes cleanly. Action
  distribution: 55 ACCEPT, 8 KEEP_AS_NON_CORE, 7 MARK_AS_OVER_ANNOTATED, 1
  MODIFY.
- Completed CLU second-pass cleanup: existing annotation reviews were already
  present, but status was still `IN_PROGRESS` and one repeated GO term had
  inconsistent actions. Reconciled `negative regulation of protein-containing
  complex assembly` to ACCEPT, added the available falcon deep-research file as
  supporting context, set status to COMPLETE, rendered the review, and `just
  validate human CLU` now passes cleanly. Action distribution: 73 ACCEPT, 56
  KEEP_AS_NON_CORE, 22 MARK_AS_OVER_ANNOTATED, 4 MODIFY.
- Completed BIN1 first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR46514`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/BIN1/BIN1-notes.md` from cached UniProt/GOA/PANTHER/publication
  evidence. All 112 seeded GO annotations have review actions, core BIN1
  BAR-domain phospholipid/membrane-curvature, lipid tubulation, endocytosis,
  clathrin/dynamin adaptor, synaptic vesicle, and T-tubule functions are
  defined, and `just validate human BIN1` passes cleanly. Action distribution:
  62 ACCEPT, 31 KEEP_AS_NON_CORE, 18 MARK_AS_OVER_ANNOTATED, 1 MODIFY.
- Completed PICALM first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR22951`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/PICALM/PICALM-notes.md` from cached UniProt/GOA/Reactome/publication
  evidence. All 113 seeded GO annotations have review actions, core PICALM
  phosphoinositide-bound clathrin adaptor, coated-vesicle curvature/maturation,
  clathrin coat assembly, and small R-SNARE cargo-sorting functions are defined,
  and `just validate human PICALM` passes cleanly. Action distribution: 80
  ACCEPT, 22 KEEP_AS_NON_CORE, 10 MARK_AS_OVER_ANNOTATED, 1 MODIFY.
- Completed CD33 first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR12035`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/CD33/CD33-notes.md` from cached UniProt/GOA/Reactome/PANTHER/publication
  evidence. All 45 seeded GO annotations have review actions, core CD33/Siglec-3
  sialic-acid binding, cell-surface inhibitory receptor signaling, ITIM-linked
  SHP-1/SHP-2 recruitment, and negative myeloid/monocyte activation functions
  are defined, and `just validate human CD33` passes cleanly. Action
  distribution: 29 ACCEPT, 5 KEEP_AS_NON_CORE, 8 MARK_AS_OVER_ANNOTATED, 2
  MODIFY, 1 UNDECIDED.
- Completed CR1 first-pass review: fetched gene data, GOA annotations,
  publications, and confirmed existing PANTHER family `PTHR45656`. Falcon deep
  research timed out after 180 seconds without writing an artifact, so manual
  notes were created in `genes/human/CR1/CR1-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. All 64 seeded GO
  annotations have review actions, core CR1/CD35 complement receptor activity,
  C3b/C4b binding, immune-adherence clearance, factor I cofactor/convertase
  decay, and negative complement-regulatory functions are defined, and `just
  validate human CR1` passes cleanly. Action distribution: 42 ACCEPT, 17
  KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED, 2 MODIFY.
- Completed CD2AP first-pass review: fetched gene data, GOA annotations,
  publications, and confirmed existing PANTHER family `PTHR14167`. Falcon deep
  research timed out after 180 seconds without writing an artifact, so manual
  notes were created in `genes/human/CD2AP/CD2AP-notes.md` from cached
  UniProt/GOA/PANTHER/publication evidence. All 72 seeded GO annotations have
  review actions, core CD2AP SH3-domain adaptor/scaffold, actin remodeling,
  junction/slit-diaphragm, and endosomal trafficking functions are defined, and
  `just validate human CD2AP` passes cleanly. Action distribution: 36 ACCEPT, 9
  KEEP_AS_NON_CORE, 19 MARK_AS_OVER_ANNOTATED, 7 MODIFY, 1 UNDECIDED.
- Completed INPP5D first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR46051`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/INPP5D/INPP5D-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. All 56 seeded GO
  annotations have review actions, plus one NEW phosphotyrosine-residue binding
  annotation was added to replace repeated generic protein-binding entries. Core
  SHIP1 PtdIns(3,4,5)P3/IP4 5-phosphatase, phosphotyrosine-motif recruitment,
  and immune receptor signal-attenuation functions are defined, and `just
  validate human INPP5D` passes cleanly. Action distribution: 34 ACCEPT, 4
  KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED, 12 MODIFY, 2 UNDECIDED, 1 REMOVE,
  1 NEW.
- Completed PLCG2 first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR10336`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/PLCG2/PLCG2-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. All 167 seeded GO
  annotations have review actions, core PLCG2 PIP2 phospholipase, IP3/DAG and
  calcium signaling, phosphotyrosine-dependent recruitment, BCR/antigen/C-type
  lectin receptor signaling, and membrane/raft/ruffle localization functions
  are defined, and `just validate human PLCG2` passes cleanly. Alzheimer-relevant
  TREM2/TLR microglial phenotypes were retained as important non-core cellular
  outcomes. Action distribution: 83 ACCEPT, 56 KEEP_AS_NON_CORE, 19 MODIFY, 7
  MARK_AS_OVER_ANNOTATED, 1 UNDECIDED, 1 REMOVE.
- Completed SPI1 first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR11849`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/SPI1/SPI1-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. Added the cached PU.1
  macrophage binding-site selection paper `PMID:23658224` as an extra reference.
  All 140 seeded GO annotations have review actions, core PU.1 ETS/PU-box
  cis-regulatory DNA binding, RNA polymerase II transcription-factor activity,
  pioneer/chromatin accessibility control, and B-cell/myeloid hematopoietic
  lineage functions are defined, and `just validate human SPI1` passes cleanly.
  Microglial/macrophage and immune-output terms were retained as non-core where
  they represent downstream cell-state consequences. Action distribution: 74
  ACCEPT, 32 KEEP_AS_NON_CORE, 21 MODIFY, 11 MARK_AS_OVER_ANNOTATED, 2
  UNDECIDED.
- Completed MS4A4A first-pass review: fetched gene data, GOA annotations,
  publications, and PANTHER family `PTHR23320`. Falcon deep research timed out
  after 180 seconds without writing an artifact, so manual notes were created in
  `genes/human/MS4A4A/MS4A4A-notes.md` from cached
  UniProt/GOA/PANTHER/publication evidence. All 9 seeded GO annotations have
  review actions, core four-pass MS4A4A membrane, plasma membrane raft, Golgi,
  and endoplasmic reticulum localization is defined, and `just validate human
  MS4A4A` passes cleanly. Generic interactome protein-binding annotations were
  marked over-annotated; TREM2/sTREM2 modulation was recorded as an
  Alzheimer-relevant unresolved biological question rather than an invented
  molecular function. Action distribution: 7 ACCEPT, 2
  MARK_AS_OVER_ANNOTATED.
- Completed MS4A6A first-pass review: fetched gene data, GOA annotations,
  publications, and confirmed PANTHER family `PTHR23320`. Falcon deep research
  timed out after 180 seconds without writing an artifact, so manual notes were
  created in `genes/human/MS4A6A/MS4A6A-notes.md` from cached
  UniProt/GOA/PANTHER/publication evidence. All 6 seeded GO annotations have
  review actions, core MS4A6A four-pass membrane/trans-Golgi localization is
  defined, and `just validate human MS4A6A` passes cleanly. The plasma-membrane
  IBA was modified to the directly supported trans-Golgi network term, while
  broad receptor-signaling and generic protein-binding annotations were marked
  over-annotated. Action distribution: 3 ACCEPT, 2
  MARK_AS_OVER_ANNOTATED, 1 MODIFY.
- Completed EPHA1 first-pass review: fetched gene data, GOA annotations,
  publications, Reactome records, and PANTHER family `PTHR46877`. Falcon deep
  research timed out after 180 seconds without writing an artifact, so manual
  notes were created in `genes/human/EPHA1/EPHA1-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. All 42 seeded GO
  annotations have review actions, core EPHA1 transmembrane ephrin receptor and
  receptor protein tyrosine kinase functions are defined, and `just validate
  human EPHA1` passes cleanly. Context-dependent adhesion, migration,
  angiogenesis, fibronectin-binding, and kinase-binding outputs were kept as
  non-core; indirect stress-fiber assembly transfers were marked
  over-annotated. Action distribution: 30 ACCEPT, 10 KEEP_AS_NON_CORE, 2
  MARK_AS_OVER_ANNOTATED.
- Completed FERMT2 first-pass review: fetched gene data, GOA annotations,
  publications, Reactome records, and PANTHER family `PTHR16160`. Falcon deep
  research timed out after 180 seconds without writing an artifact, so manual
  notes were created in `genes/human/FERMT2/FERMT2-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. All 85 seeded GO
  annotations have review actions, core kindlin-2 integrin-binding/co-activator,
  phosphoinositide/PIP3 membrane-engagement, and actin/ILK-linked
  focal-adhesion scaffold functions are defined, and `just validate human
  FERMT2` passes cleanly. Wnt, TGF-beta/Smad, EMT, endothelial barrier,
  trophoblast migration, and MSC fate outputs were kept as non-core; generic
  protein-binding and imprecise cell-surface terms were modified to more
  informative replacements. Action distribution: 52 ACCEPT, 30
  KEEP_AS_NON_CORE, 3 MODIFY.
- Completed CASS4 first-pass review: fetched gene data, GOA annotations,
  publications, and confirmed PANTHER family `PTHR10654`. Falcon deep research
  timed out after 180 seconds without writing an artifact, so manual notes were
  created in `genes/human/CASS4/CASS4-notes.md` from cached
  UniProt/GOA/PANTHER/publication evidence. All 15 seeded GO annotations have
  review actions, core CASS4/HEPL Cas-family focal-adhesion docking/scaffold,
  FAK/protein-tyrosine-kinase binding/regulation, cell spreading, and migration
  functions are defined, and `just validate human CASS4` passes cleanly. The
  broad receptor-tyrosine-kinase signaling IBA was modified to
  integrin-mediated signaling; AKT pathway activation was kept as non-core NSCLC
  context. Action distribution: 13 ACCEPT, 1 KEEP_AS_NON_CORE, 1 MODIFY.
- Completed MAPT first-pass review: fetched gene data, 198 GOA annotations,
  publications, and confirmed PANTHER family `PTHR11501`. Falcon deep research
  timed out after 180 seconds without writing an artifact, so manual notes were
  created in `genes/human/MAPT/MAPT-notes.md` from cached
  UniProt/GOA/PANTHER/publication evidence. All seeded annotations have review
  actions, core tau microtubule-stabilizing/axon/membrane-cortex linker
  function and Alzheimer-relevant tau self-assembly/neurofibrillary-tangle
  pathology are defined, and `just validate human MAPT` passes cleanly. Synaptic,
  mitochondrial, secretion, glial, stress-response, nuclear, and partner-binding
  contexts were kept as non-core where credible; generic `protein binding` and
  broad nucleic-acid/process terms were marked over-annotated. The `part_of
  tubulin complex` annotation was modified to tubulin binding. Action
  distribution: 77 ACCEPT, 70 KEEP_AS_NON_CORE, 50 MARK_AS_OVER_ANNOTATED, 1
  MODIFY.
- Completed GSK3B first-pass review: fetched gene data, 390 GOA annotations,
  publications, Reactome-derived entries, and confirmed PANTHER family
  `PTHR24057`. Falcon deep research timed out after 180 seconds without writing
  an artifact, so manual notes were created in
  `genes/human/GSK3B/GSK3B-notes.md` from cached
  UniProt/GOA/Reactome/PANTHER/publication evidence. All seeded annotations have
  review actions, core GSK3B ATP-dependent protein serine/threonine kinase,
  tau-protein kinase, Wnt/beta-catenin destruction-complex, protein-turnover,
  and glycogen/insulin metabolic-regulation functions are defined, and `just
  validate human GSK3B` passes cleanly. Broad apoptosis, EMT, ER-stress, mTOR,
  cilia, circadian, immune, synaptic, developmental, and centrosomal outputs were
  kept as non-core; generic `protein binding` and broad signal-transduction
  terms were marked over-annotated; generic kinase terms were modified to
  protein serine/threonine kinase activity. Action distribution: 172 ACCEPT, 126
  KEEP_AS_NON_CORE, 84 MARK_AS_OVER_ANNOTATED, 8 MODIFY.
- Completed LRP1 first-pass review: fetched gene data, 124 GOA annotations,
  publications, and confirmed PANTHER family `PTHR22722`. Falcon deep research
  timed out after 180 seconds without writing an artifact, so manual notes were
  created in `genes/human/LRP1/LRP1-notes.md` from cached
  UniProt/GOA/PANTHER/publication evidence. All seeded annotations have review
  actions, core LRP1 LDLR-family cargo/scavenger receptor, apolipoprotein and
  lipoprotein receptor, receptor-mediated endocytosis/internalization, amyloid
  beta clearance/transcytosis, blood-brain-barrier transport, and tau/MAPT uptake
  context are defined, and `just validate human LRP1` passes cleanly. Vascular,
  extracellular-matrix, inflammatory, infection/toxin, intracellular-domain, and
  signaling side branches were kept as non-core; generic protein/RNA/complex
  binding and broad signaling-receptor labels were marked over-annotated. Action
  distribution: 77 ACCEPT, 29 KEEP_AS_NON_CORE, 18 MARK_AS_OVER_ANNOTATED.
- Completed ABCA1 first-pass review: fetched gene data, 145 GOA annotations,
  publication caches, Reactome-derived entries, and confirmed the UniProt/PANTHER
  ABCA-family assignment `PTHR19229:SF34`. Falcon deep research timed out after
  180 seconds without writing an artifact, so manual notes were created in
  `genes/human/ABCA1/ABCA1-notes.md` from cached
  UniProt/GOA/Reactome/publication evidence. All seeded annotations have review
  actions, core ABCA1 ATP-coupled phospholipid transporter/floppase activity,
  apoA-I/apoE-linked lipidation and nascent HDL assembly, cholesterol efflux,
  reverse cholesterol transport, and plasma-membrane/endosomal localization are
  defined, and `just validate human ABCA1` passes cleanly. ApoA-I-triggered
  Cdc42/cAMP signaling, response/stimulus terms, ER/Golgi/perinuclear
  trafficking, platelet dense-granule and protein-secretion outputs were kept as
  non-core; generic binding and protein-cargo transport labels were
  over-annotated or modified to lipid-specific replacements. Action distribution:
  94 ACCEPT, 34 KEEP_AS_NON_CORE, 11 MARK_AS_OVER_ANNOTATED, 6 MODIFY.
- Completed ABI3 cleanup review: the existing Falcon deep-research-backed ABI3
  review was marked `COMPLETE`, duplicate `defense response to tumor cell`
  actions were aligned as non-core, and the Falcon deep-research report was
  cited in the core WAVE regulatory complex synthesis. All 47 seeded annotations
  have review actions, core ABI3/NESH signaling-adaptor membership in the SCAR/WAVE
  regulatory complex, actin-dependent migration/protrusion control, and
  lamellipodium regulation are defined, and `just validate human ABI3` passes
  cleanly. Action distribution: 25 ACCEPT, 12 KEEP_AS_NON_CORE, 9
  MARK_AS_OVER_ANNOTATED, 1 UNDECIDED.

## 2026-06-20

- Completed APP second-pass review cleanup: revised the standalone biological
  description, added local UniProt and Falcon deep-research references, added
  NEW review entries for APP cell-adhesion mediator activity, cell-adhesion
  molecule binding, and copper ion binding, and aligned duplicate-term actions
  for broad protein-metabolism, interleukin-1-response, and amyloid-beta LTP
  annotations. Knowledge-gap questions and suggested experiments now focus on
  evolved in-vivo APP isoform, fragment, adhesion, trophic-signaling,
  metal-binding, and intracellular-domain biology. `just validate human APP` and
  `just render human APP` pass cleanly. Action distribution: 251 ACCEPT, 80
  KEEP_AS_NON_CORE, 91 MARK_AS_OVER_ANNOTATED, 3 NEW, 1 REMOVE, 3 UNDECIDED
  across 429 annotations.
- Completed CLU second-pass review cleanup: added
  `genes/human/CLU/CLU-notes.md`, recorded manual reference-review metadata for
  the Falcon deep-research report, and added knowledge-gap questions plus
  suggested experiments focused on evolved in-vivo CLU extracellular holdase,
  complement MAC-inhibition, receptor-mediated client clearance, glycoform/redox
  regulation, and isoform biology. `just validate human CLU` and `just render
  human CLU` pass cleanly. Action distribution: 73 ACCEPT, 56 KEEP_AS_NON_CORE,
  22 MARK_AS_OVER_ANNOTATED, 4 MODIFY across 155 annotations.
- Completed ABI3 notes backfill: added `genes/human/ABI3/ABI3-notes.md` to
  capture WRC/adaptor, microglial actin-surveillance, phosphorylation, S209F,
  and model-interpretation evidence from UniProt, primary review citations, and
  the Falcon report. No YAML action changes were needed in this pass; `just
  validate human ABI3` passes cleanly.
- Completed PSEN1 second-pass audit: added `reference_review` metadata for the
  core gamma-secretase complex/substrate paper (PMID:15274632), the human
  gamma-secretase structure paper (PMID:26280335), and the ER calcium-leak paper
  (PMID:16959576), and appended notes explaining why unusual location
  annotations remain UNDECIDED pending fuller evidence. No annotation action
  changes were made; `just validate human PSEN1` and `just render human PSEN1`
  pass cleanly. Action distribution: 65 ACCEPT, 52 KEEP_AS_NON_CORE, 57
  MARK_AS_OVER_ANNOTATED, 7 MODIFY, 16 UNDECIDED across 197 annotations.
- Completed PSEN2 second-pass audit: added `reference_review` metadata for APP
  and Notch processing, PSEN2 catalytic aspartate, AP-1-dependent
  late-endosome/lysosome localization, and ER-mitochondria calcium-coupling
  evidence (PMIDs 15274632, 10497236, 10652302, 27293189, 21285369). The
  remaining UNDECIDED calls were left unchanged because they are hypoxia or
  specific synaptic-location transfers without direct cached support. `just
  validate human PSEN2` and `just render human PSEN2` pass cleanly. Action
  distribution: 40 ACCEPT, 24 KEEP_AS_NON_CORE, 11 MARK_AS_OVER_ANNOTATED, 4
  UNDECIDED across 79 annotations.
- Completed SORL1 second-pass audit: added `reference_review` metadata for the
  core APP/SORLA trafficking and amyloid-beta lysosomal-sorting evidence
  (PMIDs 16174740, 16407538, 17855360, 22621900, 24523320), and appended notes
  explaining why the remaining nuclear-envelope style localization annotations
  remain UNDECIDED. No annotation actions were changed; `just validate human
  SORL1` and `just render human SORL1` pass cleanly. Action distribution: 92
  ACCEPT, 44 KEEP_AS_NON_CORE, 25 MARK_AS_OVER_ANNOTATED, 4 MODIFY, 3
  UNDECIDED across 168 annotations.
- Completed ADAM10 second-pass audit: added `reference_review` metadata for the
  main ectodomain-shedding, APP alpha-secretase, synaptic endocytosis,
  L1-cleavage, and S. aureus alpha-toxin context papers (PMIDs 26686862,
  33731436, 23676497, 12475894, 30463011). The existing REMOVE for
  metallodipeptidase activity was retained because ADAM10 is a membrane
  metalloendopeptidase/sheddase, not a dipeptidase. `just validate human
  ADAM10` and `just render human ADAM10` pass cleanly. Action distribution: 88
  ACCEPT, 42 KEEP_AS_NON_CORE, 19 MARK_AS_OVER_ANNOTATED, 1 MODIFY, 1 REMOVE
  across 151 annotations.
- Completed INPP5D second-pass audit: reviewed the remaining REMOVE and
  UNDECIDED calls against cached evidence and appended notes. The NKG2A
  protein-binding annotation remains REMOVE because the cached PMID:9485206
  abstract explicitly says SHIP is not associated; the two remaining experimental
  protein-binding annotations remain UNDECIDED because abstract-only evidence
  does not expose SHIP1-specific support. No YAML action changes were needed;
  `just validate human INPP5D` passes cleanly. Action distribution remains 34
  ACCEPT, 4 KEEP_AS_NON_CORE, 12 MODIFY, 3 MARK_AS_OVER_ANNOTATED, 2 UNDECIDED,
  1 REMOVE, 1 NEW across 57 annotations.
- Completed PLCG2 second-pass audit: reviewed the remaining UNDECIDED and REMOVE
  calls against cached evidence and appended notes. The protein tyrosine kinase
  binding IPI remains UNDECIDED because PMID:32514138 is abstract-only in cache,
  while the Wnt signaling annotation remains REMOVE because PMID:18784435 does
  not support PLCG2 function in Wnt signaling. No YAML action changes were
  needed; `just validate human PLCG2` passes cleanly. Action distribution
  remains 83 ACCEPT, 56 KEEP_AS_NON_CORE, 19 MODIFY, 7
  MARK_AS_OVER_ANNOTATED, 1 UNDECIDED, 1 REMOVE across 167 annotations.
- Completed CD33 second-pass audit: reviewed the remaining UNDECIDED
  tau/protein-secretion annotation and appended notes. The PMID:27044754 cache
  names FRMD4A as the functional tau-release hit and does not expose the
  CD33-specific IMP evidence, so the annotation remains UNDECIDED rather than
  removed. No YAML action changes were needed; `just validate human CD33` passes
  cleanly. Action distribution remains 29 ACCEPT, 5 KEEP_AS_NON_CORE, 8
  MARK_AS_OVER_ANNOTATED, 2 MODIFY, 1 UNDECIDED across 45 annotations.
- Completed CD2AP second-pass audit: reviewed the remaining UNDECIDED
  tau/protein-secretion annotation and appended notes. The PMID:27044754 cache
  is abstract-only and foregrounds FRMD4A rather than CD2AP-specific evidence,
  so the experimental annotation remains UNDECIDED pending full-text or
  supplementary-data review. No YAML action changes were needed; `just validate
  human CD2AP` passes cleanly. Action distribution remains 36 ACCEPT, 9
  KEEP_AS_NON_CORE, 19 MARK_AS_OVER_ANNOTATED, 7 MODIFY, 1 UNDECIDED across 72
  annotations.
- Completed SPI1 second-pass audit: reviewed the two remaining generic
  `protein binding` IPI annotations against the cached abstracts and appended
  notes. PMID:21575865 foregrounds TMPRSS2:ERG interaction evidence and
  PMID:10207087 foregrounds MEF/AML1 interaction evidence, so both SPI1
  experimental annotations remain UNDECIDED pending full-text or
  supplementary-data review rather than being removed. No YAML action changes
  were needed. Action distribution remains 74 ACCEPT, 32 KEEP_AS_NON_CORE, 21
  MODIFY, 11 MARK_AS_OVER_ANNOTATED, 2 UNDECIDED across 140 annotations.
- Completed NCSTN second-pass audit: added `reference_review` metadata for the
  core nicastrin/gamma-secretase complex, APP/Notch proteolysis, and structural
  references. No annotation action changes were needed; `just validate human
  NCSTN` and `just render human NCSTN` pass cleanly. Action distribution remains
  73 ACCEPT, 12 KEEP_AS_NON_CORE, 10 MARK_AS_OVER_ANNOTATED, 4 MODIFY across 99
  annotations.
- Completed APH1A second-pass audit: added `reference_review` metadata for the
  main APH-1/gamma-secretase association, substrate processing, purified-complex
  and structural references. No annotation action changes were needed; `just
  validate human APH1A` and `just render human APH1A` pass cleanly. Action
  distribution remains 50 ACCEPT, 12 KEEP_AS_NON_CORE, 9
  MARK_AS_OVER_ANNOTATED, 2 MODIFY across 73 annotations.
- Completed APH1B second-pass audit: added `reference_review` metadata for
  APH1B-relevant APH-1 and isoform-specific gamma-secretase references. No
  annotation action changes were needed; `just validate human APH1B` and `just
  render human APH1B` pass cleanly. Action distribution remains 37 ACCEPT, 1
  KEEP_AS_NON_CORE, 4 MARK_AS_OVER_ANNOTATED, 1 MODIFY across 43 annotations.
- Completed PSENEN second-pass audit: added `reference_review` metadata for
  PEN-2 complex membership, presenilin endoproteolysis, gamma-secretase
  activity, and structural references. No annotation action changes were needed;
  `just validate human PSENEN` and `just render human PSENEN` pass cleanly.
  Action distribution remains 55 ACCEPT, 8 KEEP_AS_NON_CORE, 7
  MARK_AS_OVER_ANNOTATED, 1 MODIFY across 71 annotations.
- Completed APOE second-pass audit: added `reference_review` metadata for the
  key lipid-efflux, astrocyte lipoprotein-release, receptor-mediated
  lipoprotein uptake, amyloid-beta binding, and TREM2-ligand references. No
  annotation action changes were needed; `just validate human APOE` and `just
  render human APOE` pass cleanly. Action distribution remains 145 ACCEPT, 120
  KEEP_AS_NON_CORE, 28 MARK_AS_OVER_ANNOTATED across 293 annotations.
- Completed TREM2 second-pass audit: added `reference_review` metadata for the
  DAP12 receptor-signaling, apolipoprotein/amyloid/apoptotic-cell ligand,
  myelin-cholesterol response, and human microglia loss-of-function references.
  No annotation action changes were needed; `just validate human TREM2` and
  `just render human TREM2` pass cleanly. Action distribution remains 117
  ACCEPT, 151 KEEP_AS_NON_CORE, 5 MARK_AS_OVER_ANNOTATED across 273
  annotations.
- Completed ABCA7 second-pass audit: added `reference_review` metadata for
  phospholipid efflux, apolipoprotein binding, reconstituted phospholipid
  transport, lysophosphatidylcholine export, and APP/amyloid-processing
  references. No annotation action changes were needed; `just validate human
  ABCA7` and `just render human ABCA7` pass cleanly. Action distribution
  remains 55 ACCEPT, 20 KEEP_AS_NON_CORE, 4 MODIFY, 2 MARK_AS_OVER_ANNOTATED
  across 81 annotations.
- Completed BACE1 second-pass audit: added `reference_review` metadata for
  beta-secretase discovery, APP beta-site cleavage, late-Golgi/APP-access
  localization, and GGA/SNX6 trafficking-control references. No annotation
  action changes were needed; `just validate human BACE1` and `just render human
  BACE1` pass cleanly. Action distribution remains 94 ACCEPT, 24
  KEEP_AS_NON_CORE, 20 MARK_AS_OVER_ANNOTATED, 2 MODIFY across 140 annotations.
- Completed BIN1 second-pass audit: added `reference_review` metadata for
  BAR/N-BAR membrane curvature, membrane tubulation, DNM2 interaction,
  BIN1-BACE1 trafficking, and BIN1/tau/clusterin references. No annotation
  action changes were needed; `just validate human BIN1` and `just render human
  BIN1` pass cleanly. Action distribution remains 62 ACCEPT, 31
  KEEP_AS_NON_CORE, 18 MARK_AS_OVER_ANNOTATED, 1 MODIFY across 112 annotations.
- Completed CDK5 second-pass audit: added `reference_review` metadata for p35
  activation, p25 structural context, SH3GLB1/endophilin-B1 autophagy
  phosphorylation, NR2B regulation, and the p35-specific microtubule-binding
  caveat. No annotation action changes were needed; `just validate human CDK5`
  and `just render human CDK5` pass cleanly. Action distribution remains 76
  ACCEPT, 30 KEEP_AS_NON_CORE, 38 MARK_AS_OVER_ANNOTATED, 5 MODIFY across 149
  annotations.
- Completed CDK5R1 second-pass audit: added `reference_review` metadata for
  p35/CDK5 activation, p35-to-p25 conversion, CDK5/p25 structure, p35
  microtubule binding, p35 myristoylation/localization, and CDK5-mediated
  induced-autophagy context. No annotation action changes were needed; `just
  validate human CDK5R1` and `just render human CDK5R1` pass cleanly. Action
  distribution remains 61 ACCEPT, 16 KEEP_AS_NON_CORE, 19
  MARK_AS_OVER_ANNOTATED, 8 MODIFY across 104 annotations.
- Completed notes-only second-pass confirmations for PICALM, CR1, MS4A4A,
  MS4A6A, EPHA1, FERMT2, CASS4, MAPT, GSK3B, LRP1, and ABCA1. These reviews
  already had manual `reference_review` coverage, no UNDECIDED calls, and no
  REMOVE calls; no YAML action changes were needed. `just validate` passes
  cleanly for all eleven genes. Action distributions remain: PICALM 80 ACCEPT,
  22 KEEP_AS_NON_CORE, 10 MARK_AS_OVER_ANNOTATED, 1 MODIFY; CR1 42 ACCEPT, 17
  KEEP_AS_NON_CORE, 2 MODIFY, 3 MARK_AS_OVER_ANNOTATED; MS4A4A 7 ACCEPT, 2
  MARK_AS_OVER_ANNOTATED; MS4A6A 3 ACCEPT, 1 MODIFY, 2
  MARK_AS_OVER_ANNOTATED; EPHA1 30 ACCEPT, 10 KEEP_AS_NON_CORE, 2
  MARK_AS_OVER_ANNOTATED; FERMT2 52 ACCEPT, 30 KEEP_AS_NON_CORE, 3 MODIFY; CASS4
  13 ACCEPT, 1 MODIFY, 1 KEEP_AS_NON_CORE; MAPT 77 ACCEPT, 70 KEEP_AS_NON_CORE,
  50 MARK_AS_OVER_ANNOTATED, 1 MODIFY; GSK3B 172 ACCEPT, 126
  KEEP_AS_NON_CORE, 84 MARK_AS_OVER_ANNOTATED, 8 MODIFY; LRP1 77 ACCEPT, 29
  KEEP_AS_NON_CORE, 18 MARK_AS_OVER_ANNOTATED; ABCA1 94 ACCEPT, 34
  KEEP_AS_NON_CORE, 11 MARK_AS_OVER_ANNOTATED, 6 MODIFY.
- Created and validated `modules/alzheimer_disease_pathways.yaml`, a
  `ModuleReview` overview module grouping the reviewed gene set into APP
  processing/amyloid-beta handling, lipid/lipoprotein transport, microglial
  lipid-debris sensing, tau/cytoskeletal kinase biology, and
  endocytic/adhesion adaptor systems. `uv run linkml-validate -s
  src/ai_gene_review/schema/gene_review.yaml -C ModuleReview
  modules/alzheimer_disease_pathways.yaml` passes cleanly, and the module renders
  to `pages/modules/alzheimer_disease_pathways.html`.
