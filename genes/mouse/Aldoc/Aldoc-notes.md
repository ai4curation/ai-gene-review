# Aldoc notes

## Workflow

- `just fetch-gene mouse Aldoc` seeded `Aldoc-ai-review.yaml` with 24 GOA rows
  and reused the existing PANTHER `PTHR11627` family cache.
- `just fetch-gene-pmids mouse Aldoc` found the four GOA PMIDs and confirmed they
  were already cached: PMID:4337889, PMID:24958256, PMID:14651853 and
  PMID:16294306.
- `just paint-losses mouse Aldoc` found no IRD or IKR loss on the mouse Aldoc
  lineage.
- `just deep-research-falcon mouse Aldoc --fallback perplexity-lite` failed
  because neither the Falcon nor Perplexity provider was available in this
  environment. I proceeded by manually reviewing the seeded YAML, the mouse
  UniProt record, cached publication abstracts/full text, QuickGO donor traces
  and the `PTHR11627` family review.

## Evidence Trace

- The conserved class I aldolase activity is sound. Human ALDOC has the first
  brain-aldolase structure and the mouse UniProt record preserves the catalytic
  `E188` proton acceptor and the `K230` Schiff-base lysine. The family review
  scopes `GO:0004332`, `GO:0006096`, `GO:0030388` and animal `GO:0005829` onto
  the Aldoc clade.
- The 1972 mouse IDA row for `GO:0004332` is title-only in the cache, but MGI's
  direct-assay assertion is biologically expected and is corroborated by rat
  Aldoc, human ALDOC and PAINT evidence.
- QuickGO traces the mouse cytoskeletal-protein binding rows to human ALDOC
  PMID:9244396, a direct aldolase/actin-cytoskeleton binding paper, so those rows
  are kept as real but non-core.
- QuickGO/MGI trace the rat donor rows to PMID:19003905 for `axon`, PMID:9570792
  for `postsynaptic cytosol`, and PMID:2188264 for both `identical protein
  binding` and `protein-containing complex binding`. PMID:2188264 supports rat
  Aldoc activity and tetramerization; the abstracts for PMID:19003905 and
  PMID:9570792 establish Aldoc-positive Purkinje-cell compartments but do not
  expose the direct subcellular localization evidence, so those two mouse ISO
  rows remain `UNDECIDED`.
- The `GO:0030855` epithelial-cell differentiation row is an automated transfer
  from a human Caco-2 differentiation proteomics paper. A protein-abundance
  change in that system is not evidence that ALDOC/Aldoc executes the
  differentiation process.
- PMID:24958256 supports calorie-restriction induction of liver Aldoc transcript,
  not direct Aldoc catalytic flux through gluconeogenesis. The MGI row uses IDA
  for this expression-only evidence, so the review records a
  `WRONG_EVIDENCE_CODE` source defect on the GO:0006094 annotation.

## GO-CAM Context

The reviewed 61e0e55600001225 and 62d0afa500000298 mouse gluconeogenesis
GO-CAMs both place Aldoc at the cytosolic aldolase step, condensing
glyceraldehyde 3-phosphate plus dihydroxyacetone phosphate to fructose
1,6-bisphosphate upstream of Fbp1. The molecular function and cytosolic
location are correct for Aldoc, and the causal chain is chemically coherent, but
the `part_of gluconeogenesis` assertion remains weak: the model's mouse
liver/kidney route is expected to use Aldob, whereas Aldoc is the brain/zebrin II
isoform and the model evidence is only a caloric-restriction transcript
increase. The unreviewed 62d0afa500000132 GO-CAM carries the same Aldoc step and
should be checked during the consistency-notes pass. The final GO-CAM
consistency-notes PR should therefore replace "No ALDOC/Aldoc gene review
exists" with a note that the mouse Aldoc review keeps `GO:0004332` and
`GO:0005829` but marks `GO:0006094` as `MARK_AS_OVER_ANNOTATED`.
