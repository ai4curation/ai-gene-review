# FASLG manual curation notes

## 2026-09-30

- Reviewed all 126 seeded human FASLG GOA rows manually against UniProt, GOA,
  cached primary papers, the FASL/FAS GO-CAM, Reactome event summaries, and the
  PTHR11471 TNF-family/PTHR11471:SF33 FASLG PANTHER placement.
- Treated trimeric membrane FasL binding to FAS/CD95 as the core molecular
  activity. `GO:0005125 cytokine activity` is the GO-CAM molecular function for
  the FASLG activity node in `GO:0008625 extrinsic apoptotic signaling pathway
  via death domain receptors`, while generic `GO:0005102 signaling receptor
  binding`, `GO:0005164 tumor necrosis factor receptor binding`, and
  DISC-context `GO:0005515 protein binding` rows were narrowed to `GO:0005123
  death receptor binding`.
- Kept the ADAM10/SPPL2A-generated FasL intracellular domain as non-core
  biology. PMID:17557115 supports nuclear localization and transcriptional
  inhibition by the ICD, but this is distinct from the extracellular FAS ligand
  role.
- Removed the bulk of the imported `protein binding` rows. The recurrent SH3
  and FCH/PCH-family hits are plausible FasL-tail trafficking interactions, but
  they remain uninformative as generic binding rows; the HuRI, BioPlex,
  alternative-splicing, proximity-ligation, and U2OS cell-map rows are
  high-throughput interactome context rather than curated FASLG functions.
- Kept explicit Reactome FASL:FAS receptor events as extracellular FASLG
  localization support and removed transcriptional Reactome events for
  `FASLG` gene expression, plus generic downstream cFLIP/CASP8 events that no
  longer describe FASLG protein acting in the extracellular ligand complex.
- Split specialized outputs from the core pathway: exosome-associated FasL,
  T-cell apoptosis, endothelial-cell apoptosis, NF-kappaB activation, and
  RIPK-dependent necroptotic signaling are valid contextual FASLG outcomes,
  whereas endothelial angiogenesis, ER calcium release, phosphatidylserine
  exposure, LPS/growth-factor/IFN-gamma responses, neuronal apoptosis, and EGFR
  signaling sit too far downstream or come from over-specific transfers.
- Removed the PMID:12201652 plasma-membrane IDA row. The term is true for human
  membrane FasL, but that paper assays FasL-like soluble activity in catfish
  and tilapia nonspecific cytotoxic cells, so it is not direct human FASLG
  localization evidence.

## 2026-10-25 (Ligands in Signaling Pathways — Tranche 4A)

- Added a `NEW` annotation for `GO:0036337` (`Fas signaling pathway`, `is_a GO:0008625`
  *extrinsic apoptotic signaling pathway via death domain receptors*) with
  `original_reference_id: PMID:7826947` and `supported_by` citing `PMID:7826947`
  [PMID:7826947, "induces apoptosis by binding to its receptor, Fas"] and
  `PMID:9228058` [PMID:9228058, "a molecular model of the FasL homotrimer bound to three Fas molecules"].
- In human GOA and the production GO-CAM `663d668500001551` (*FASL-FAS interaction leading to apoptosis (human)*),
  `FAS` (`P25445`), `FADD` (`Q13158`), and `CASP8` (`Q14790`) are annotated to
  `GO:0036337`, whereas `FASLG` (`P48023`) is annotated only to the parent term
  `GO:0008625`. Including `GO:0036337` alongside `GO:0008625` aligns the ligand
  with its receptor and DISC partners and with the `PTHR11471:SF33` subfamily
  scope in `interpro/panther/PTHR11471/PTHR11471-review.yaml` and
  `modules/death_receptor_apoptotic_signaling.yaml`.
- Added `GO:0005125` (*cytokine activity*) alongside `GO:0005123` (*death receptor binding*)
  in `core_functions`, with both `GO:0036337` and `GO:0008625` in `directly_involved_in`.
