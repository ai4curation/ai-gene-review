# ADCY1 notes

## 2026-11-25 GO-CAM 59dc728000000351

ADCY1 is the sole enabled-by gene in `gocams/59dc728000000351` that did not
already have a merged review on `main` or an open PR when this workstream was
started. The model uses Q08828 as a plasma-membrane adenylyl cyclase downstream
of the FSH receptor. The ADCY1 review keeps the generic adenylyl cyclase
activity, plasma-membrane location and cAMP biosynthesis rows, but it does not
find direct evidence that human ADCY1 is the physiological transmembrane
cyclase downstream of FSHR in an FSH target cell.

Final GO-CAM consistency note to carry after the ADCY1 PR merges: the gene
review supports the MF and CC used by the ADCY1 node, but the model remains
isoform-generic and under-supported for an FSHR-specific FSH branch. Leave
`gocams/59dc728000000351/*` untouched in this gene PR.

## Evidence notes

- Human ADCY1 is an adenylyl cyclase. UniProt records the catalytic reaction
  `ATP = 3',5'-cyclic AMP + diphosphate`, and the type 1 PANTHER node
  `PTN002899368` carries IBD annotations to adenylate cyclase activity and cAMP
  biosynthetic process.
- The fetal-brain cloning paper supports the human type 1 identity and
  calcium/calmodulin response through a bovine/human chimeric enzyme whose
  activity and calcium/calmodulin sensitivity were indistinguishable from
  bovine type I adenylyl cyclase [PMID:8314585, "The activity of the chimeric
  gene product and its sensitivity to calmodulin and calcium were
  indistinguishable from those of the bovine type I adenylyl cyclase."].
- The human adrenal expression paper directly supports plasma membrane
  localization in adrenal tissue [PMID:11549699, "adenylyl cyclase 1 was
  detected in cells at the membrane level"].
- Mouse donor rows support a peripheral neural/circadian context for the human
  ortholog: Adcy1 loss impaired mossy fiber LTP [PMID:9547227, "These data
  indicate that coupling of Ca2+ to activation of AC1 is crucial for mossy
  fiber LTP"], AC1/AC8 supplied redundant hippocampal cAMP for late LTP and
  long-term memory [PMID:10482244, "AC1 or AC8 can produce the necessary cAMP
  signal."], AC1 localized to mouse synaptosomal PSD and extrasynaptic
  fractions [PMID:17335981, "synaptosome fractions from the adult brain
  demonstrated robust expression of AC1 in the postsynaptic density and
  extrasynaptic regions"], and Adcy1 loss reduced the retinal contrast
  sensitivity rhythm [PMID:24048828, "Adcy1(-/-) mice show strikingly similar
  reductions in the contrast sensitivity rhythm to that in mice lacking D4Rs."].
- The mouse anterior-cingulate inflammatory pain paper was not accepted as a
  neuroinflammatory-response role. Its abstract supports that AC1 and AC8 are
  needed for behavioral allodynia, but that is a downstream pain phenotype of
  calcium-stimulated cAMP signaling rather than direct evidence that ADCY1
  executes neuroinflammation [PMID:12441059, "AC1 and AC8 in the ACC selectively
  contribute to behavioral allodynia."].

## Workflow notes

- `just deep-research-falcon human ADCY1 --fallback perplexity-lite` could not
  run in this checkout because the Falcon stack was unavailable, the fallback
  provider was also unavailable and the local `agentapi` executable was absent.
  The review therefore used the GOA seed, UniProt, PANTHER PAINT cache,
  Reactome cache, the GO-CAM review files and fetched PMID caches directly.
- The first `just fetch-gene human ADCY1` call ran against a stale editable
  install in the shared runtime and fetched zero QuickGO rows. Re-running with
  `PYTHONPATH=src` used this checkout's current fetcher, retrieved 59 Q08828
  rows and seeded all 59 existing annotations.
- `just paint-losses human ADCY1` found no IKR/IRD PAINT losses for the ADCY1
  PANTHER family.
