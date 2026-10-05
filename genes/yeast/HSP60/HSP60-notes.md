# HSP60 (YLR259C / P19882) curation notes

## 2026-10-01 current GOA refresh

- `just fetch-gene yeast HSP60 --force` refreshed HSP60 from 40 to 42
  current GOA rows, adding current `GO:0005524` InterPro ATP-binding and
  `GO:0006457` ARBA/InterPro protein-folding rows. The old
  `GO_REF:0000120` ATP-binding row and the old `GO_REF:0000002`
  protein-folding row disappeared from current GOA and are therefore retained
  as retired exact source rows.
- Five other exact rows are no longer current and are kept with `retired:
  true`: `GO:0000166 nucleotide binding` from UniProt keyword,
  `GO:0051082 unfolded protein binding` from ARBA, two generic
  high-throughput `GO:0005515 protein binding` rows from PMID:16554755 and
  PMID:19536198, and the SGD `GO:0051082` IMP row from PMID:1359644. The direct
  Hsp60 heat-stress refolding evidence in PMID:1359644 is still biologically
  correct, but the exact GO row has been withdrawn because `GO:0051082` is
  obsolete and the better MF is `GO:0140662 ATP-dependent protein folding
  chaperone`.

## IBA and PAINT review

- The current PTHR45633 PAINT snapshot assigns the core HSP60 process
  `GO:0006457 protein folding` at `PANTHER:PTN000143677` and the core
  location/MF rows `GO:0005759 mitochondrial matrix` and `GO:0051087
  protein-folding chaperone binding` at `PANTHER:PTN000143509`. All three are
  accepted as conserved, target-appropriate transfers.
- `PTN000143509` is a broad eukaryotic node that includes Hsp60 and the
  divergent yeast chaperonin-related protein Tcm62: `SGD:S000004249` is HSP60
  and `SGD:S000000248` is TCM62. Its `GO:0005743 mitochondrial inner membrane`
  transfer is compatible with Hsp60's import-associated context, but it stays
  non-core because Hsp60's resident active compartment is the matrix. The same
  node's broad `GO:0007005 mitochondrion organization` row is retained as non-core
  because Hsp60 directly assists mitochondrial matrix protein folding and complex
  assembly, while organelle-organization phenotypes are downstream.
- `PANTHER:PTN000143510` supports the two secondary process IBAs,
  `GO:0034514 mitochondrial unfolded protein response` and `GO:0045041
  protein import into mitochondrial intermembrane space`. Both stay
  non-core: folding newly imported matrix proteins is the principal activity,
  while Hsp60-dependent import/sorting and stress-response phenotypes are
  downstream contexts.

## 2023-2026 literature search

- Exact PubMed and web searches for newer `Saccharomyces` HSP60 / YLR259C /
  MIF4 papers did not identify a newer study that changes the GO review.
  Recent hits were mostly organism-general HSP60 papers or yeast engineering
  studies that mention Hsp60 as a stress marker.
- PMID:37585488 includes systematic position-2 mutagenesis of a prototypal yeast
  mitochondrial protein in a 2023 NatC/MTS study. The abstract does not name the
  assayed substrate, and the result does not require a new Hsp60 GO assertion
  beyond mitochondrial matrix localization.

## 2026-10-05 PR #3762 reviewer follow-up

- Demoted the broad `GO:0007005 mitochondrion organization` IBA row to non-core
  in the review and IBA current-GOA sidecar.
- Replaced title-backed PMID:7902576 ATPase support with the cached abstract's
  actual yeast cpn60 ATPase sentence and recorded the later PMID:9256426 Hsp10
  inhibition result as a finding-level dispute.
