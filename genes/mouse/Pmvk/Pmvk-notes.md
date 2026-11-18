# Pmvk (mouse) review notes

UniProt Q9D1G2 (PMVK_MOUSE), MGI:1915853, 192 aa. PANTHER PTHR13101:SF1 (PHOSPHOMEVALONATE
KINASE), the animal-type P-loop/NMP-kinase-fold PMK, not orthologous to the GHMP-type ERG8 of fungi
and plants. No deep-research provider file (no provider keys here); these are my own notes.

## Literature search (2026-11-18)

- Europe PMC `(TITLE:"phosphomevalonate kinase" OR TITLE:"Pmvk" OR TITLE:"PMVK")`: 48 hits. Mouse
  primary data: PMID:36808719 (Pmvk knockout and liver conditional knockout), PMID:42361171 and
  PMID:39325640 (hepatocellular carcinoma models), PMID:11792727 (enzyme activity in Pex5-/- mouse
  liver). Human biochemistry: PMID:8663599 (cloning, PTS1), PMID:16519518, PMID:17902708;
  localization: PMID:10191291 (peroxisomal, Krisans lab), PMID:14729858 (cytosolic, Hogenboom).
- Mouse peroxisome proteomics (Europe PMC `(TITLE:peroxisom*) AND (TITLE:proteom*) AND (mouse OR
  mice)`): PMID:38247867 (2024 mouse liver peroxisome SWATH-MS) names PMVK among proteins in the
  bona fide peroxisome cluster. PMID:17474143 (2007 mouse liver and kidney peroxisomes) is cached
  abstract-only and does not mention PMVK in the abstract.
- `"phosphomevalonate kinase" AND peroxisom* AND (mouse OR mice) AND (proteom* OR "protein
  correlation profiling")`: 46 hits, none adding mouse localization data beyond PMID:38247867.

## Mouse biology

- Activity in mouse liver: MGI curated PMK activity from the Pex5-/- liver enzyme survey
  [PMID:11792727 "We found that all enzymes measured, including putative peroxisomal enzymes, are at
  least as active in the peroxisome-deficient Zellweger mice as in control mice"] (abstract only).
- Essentiality: [PMID:36808719 "we constructed PMVK knockout mice and found that WT and PMVK+/− mice
  reproduced normally, but that PMVK homozygous knockout was embryonic lethal"]. Liver-specific loss
  reduces DEN/CCl4 tumours, and AAV8 re-expression raises serum cholesterol and triglyceride
  [PMID:36808719 "Adeno‐associated virus 8 (AAV8) restoration of PMVK expression promoted tumor growth
  and increased serum levels of TC and TG in CKO mice"].
- Mechanism and residues by orthology: human PMK is reversible [PMID:16519518 "PMK catalyzes a
  reversible reaction"], belongs to the NMP-kinase fold [PMID:17902708 "Animal PMK proteins belong to
  the nucleoside monophosphate (NMP) kinase family"], and uses the N-terminal K17-R18-K19-x-x-K22-D23
  Walker-A-like loop, conserved in mouse at the same positions.
- Isoforms: UniProt isoform 2 (Q9D1G2-2) lacks residues 1-21 and isoform 3 (Q9D1G2-3) lacks 1-75,
  so isoform 2 lacks most of the ATP-binding loop; no study of their activity was found.

## Localization

- Mouse PMVK ends in -AKL, a PTS1-type tripeptide; human PMVK ends in -SRL, also PTS1-type
  [PMID:8663599 "The human PMKase amino acid sequence contains a consensus peroxisomal targeting
  sequence (PTS-1), Ser-Arg-Leu, at the C terminus of the protein"].
- Human data conflict: [PMID:10191291 "we demonstrate that phosphomevalonate kinase is a peroxisomal
  protein which requires the C-terminal peroxisomal targeting signal, Ser-Arg-Leu, for localization to
  the organelle"] versus [PMID:14729858 "No indication of a peroxisomal localization was obtained."]
  (fractionation, digitonin, IF and immuno-EM of endogenous and overexpressed human PMVK).
- Mouse data: [PMID:38247867 "Notably, several proteins like ABHEB, ACNT1, LACB2, and PMVK, which have
  been suggested for a peroxisomal localization [3], can be found in the cluster of the bona fide
  peroxisomal proteins, supporting their localization to the organelle"]. The gradient peroxisome
  fractions were >90% pure by enzyme markers in that study.
- Decision: peroxisome (ISO) kept as non-core on the mouse proteomics plus the PTS1; the NOT
  peroxisome row (UniProt ISS from human) removed, because mouse data contradict it; cytosol
  accepted as the core location by orthology to human PMVK (no mouse fractionation study exists, and
  the soluble enzyme with a PTS1 could plausibly be dual-located). I stayed at the root organelle term: the PTS1 and the soluble fold point to the
  matrix, but the human localization data disagree, so the lines are not concordant.
- The GO-CAM cytosol row cites PMID:11725955, a rat MPD (Mvd) localization paper, with WITH
  RGD:1310812 (rat Pmvk); RGD has no rat Pmvk annotation from that paper (QuickGO, 2026-11-18).
  Recorded as a PROBABLE wrong-reference CHECK.

## Non-canonical claims (not annotated)

The Wuhan group reports protein-kinase activity of PMVK on beta-catenin Ser184 [PMID:36808719 "PMVK
functions as a protein kinase to directly phosphorylate β-catenin Ser184 to increase its protein
nuclear localization"] and on GAD1 (PMID:39325640); another group reports SP1 Thr355 phosphorylation
(PMID:42361171). These would be a second, protein-serine/threonine kinase activity for an NMP-kinase
fold enzyme. Single-lab cancer-cell work; recorded as a question, no NEW row.

## GO-CAM pathway-edge rows

Same pattern as Mvk (see genes/mouse/Mvk/Mvk-notes.md): cholesterol IMP (PMID:18669642,
PMID:35671633), GGPP IMP (PMID:35671633) and zymosterol IDA/IMP (PMID:36378328, PMID:33109681) come
from evidence on process-to-process edges of MGI GO-CAM models and concern other genes. The cohort
source defect is recorded once, on the Mvk review.
