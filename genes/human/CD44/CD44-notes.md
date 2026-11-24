# CD44 notes

## Setup

- `just fetch-gene human CD44` seeded 88 GOA rows from UniProtKB:P16070.
- `just fetch-gene-pmids human CD44` cached all 33 PMID references in the seeded
  review.
- Deep research failed because neither `falcon` nor the configured
  `perplexity-lite` fallback was available in this environment. No
  `CD44-deep-research-*.md` file was created.

## Evidence coverage

- The key MIF-receptor source, PMID:17045821, is abstract-only but its abstract
  states the core result: CD44 is not the MIF-binding subunit, but full-length
  CD44 is required with CD74 for MIF-induced ERK1/2 phosphorylation, Src-dependent
  signalling, and protection from apoptosis.
- Newer full-text caches cover direct CD74-CD44 association in breast cancer cells
  (PMID:29190904), galectin-9/CD44 signalling in NK cells (PMID:37006235),
  CD44-dependent foot-and-mouth-disease-virus macropinocytosis (PMID:40544280),
  the podoplanin-CD44 cell-migration complex (PMID:20962267), and the moesin/CD44
  glioblastoma migration study (PMID:23855374).
- Older hyaluronan-binding, collagen-binding, T-cell-activation and adhesion rows
  are mostly abstract-only; the abstracts verify the paper identities but often do
  not expose enough assay detail to infer functions beyond the seeded term.
- The review should stay aligned with `modules/mif_signaling.yaml`: CD74 is the
  MIF-binding unit; CD44 is the signal-transducing unit in the
  CD74-CD44 macrophage migration inhibitory factor receptor complex
  (`GO:0035692`), and contributes to the complex's cytokine receptor activity.

## Curation policy

- Treat `GO:0005540` hyaluronic acid binding as a core molecular function.
  CD44's N-terminal Link domain is the canonical hyaluronan-binding receptor
  module, and multiple human rows plus InterPro and PAINT converge on that call.
- Treat `GO:0004896` cytokine receptor activity with `contributes_to` and
  `GO:0035692` macrophage migration inhibitory factor receptor complex as real but
  non-core. CD44 is required for the MIF-CD74 receptor to signal to ERK, but it
  does not bind MIF by itself.
- Keep plasma membrane and cell-surface locations as core. Extracellular-region
  rows capture shed CD44 ectodomain / proteoglycan detections rather than the
  intact receptor's main site of action, so they belong outside the core.
- Remove bare `GO:0005515` rows when the interaction is either uninformative or
  already captured by a better CD44 process/complex row. The CD74 interaction is
  the one exception that maps cleanly to a more informative GO assertion:
  `GO:0035692` macrophage migration inhibitory factor receptor complex.
- Be conservative with very broad developmental and apoptotic ARBA rows. CD44 can
  regulate proliferation, migration, survival and inflammation in many cell
  systems, but single cancer-cell or pathogen assays should not be promoted to
  organism-level developmental functions.

## Source defects

- The PMID:40544280 FMDV row is attached to human CD44 in GOA/UniProt as
  experimental evidence for `GO:0005886`, but the paper cloned CD44 from hamster
  BHK-21 and porcine PK-15 cells and used hamster CD44 siRNAs. The review keeps
  the true plasma-membrane claim by relying on human evidence and records a
  UniProt source defect for the ortholog transfer as experimental.
- GO-CAM `gomodel:68b0f0d000000625/68b0f0d000001051` places CD44 in
  `GO:0051132` NK T cell activation even though the model title and PMID:37006235
  concern NK-cell activation. The review proposes `GO:0030101` natural killer
  cell activation and records a GO-CAM source defect asking for that repointing.
