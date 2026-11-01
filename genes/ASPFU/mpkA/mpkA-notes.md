# mpkA re-review notes

## 2026-11-01 PTHR24055 fungal CWI MAPK review

- `mpkA` encodes the terminal MAP kinase of the Aspergillus fumigatus
  cell-wall-integrity module. PMID:19715768 places Bck1, Mkk2, and MpkA in the
  same MAPK module by showing that deletion of any tier causes severe
  cell-wall-drug sensitivity and abnormal morphology, and that Bck1 and Mkk2
  activate MpkA during vegetative growth and cell-wall stress.
- PMID:17981060 is the first direct A. fumigatus MpkA study. It showed that
  the Af293 genome encodes four MAPKs, identified MpkA as similar to fungal
  cell-wall-integrity MAPKs, and found that `mpkA` deletion causes severe
  sensitivity to cell-wall-active compounds, drastic morphological changes, and
  increased oxidative-stress resistance without attenuating virulence in the
  murine infection model they tested.
- The root `PANTHER:PTN000622075` IBDs transfer generic MAPK Ser/Thr kinase
  chemistry, broad cytoplasm/nucleus activity, and generic intracellular signal
  transduction. They are not wrong-paralog calls for MpkA, but
  `GO:0035556 intracellular signal transduction` is less informative than the
  direct imported `GO:0000196 cell integrity MAPK cascade`.
- The `GO:0004707 MAP kinase activity` IBA from `PANTHER:PTN001171896` is safe:
  the term is the exact enzyme class rather than a pathway claim, and direct
  2021 fumiquinazoline work showed that MpkA is the kinase responsible for
  FmqC phosphorylation during conidiogenesis.
- Several EnsemblFungi rows come from S. pombe `pmk1`/`spm1`. `GO:0000196`
  is reasonable for the conserved fungal CWI MAPK, and broad cytoplasm/nucleus
  rows are plausible active compartments to retain as non-core. By contrast,
  the negative regulation of mitotic cytokinesis, negative regulation of
  glucose-mediated signaling, and positive regulation of calcium ion import
  rows are PomBase-specific Pmk1 outputs, not established A. fumigatus MpkA
  functions.
- PMID:22220813, an abstract-only CWI sensor/Rho GTPase paper, supports the A.
  fumigatus CWI pathway background but the cached abstract does not mention
  `mpkA` or show how CGD's heat and alkaline-pH IMP rows were assigned. I kept
  those rows as non-core stress phenotypes rather than second-guessing the
  full-text curation.
- A 2024 search found PMID:38167253 as the newest direct MpkA paper. It adds
  full-text evidence that MpkA is required for gliotoxin production and
  self-protection, physically interacts with GliT and GtmA, and is required for
  their protein levels and vacuolar localization during gliotoxin production.
  Those findings extend the secondary-metabolism outputs of the CWI MAPK but
  do not change the core MAPK/cell-wall annotation decisions.
- `just deep-research-falcon ASPFU mpkA` failed in this environment because
  `agentapi` was not found in `PATH` and the Falcon provider was unavailable.
  I therefore used this notes file and `mpkA-deep-research-manual.md` rather
  than creating a provider-named deep-research file.
