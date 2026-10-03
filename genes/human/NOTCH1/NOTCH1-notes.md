# NOTCH1 review notes

## 2026-07-14 — cerebellum-module quality audit

- Audited the existing complete human NOTCH1 review rather than reseeding it. All 378
  GOA-derived annotations have explicit review actions and none remains `PENDING`.
  The project-independent description and three core-function units were retained.
- Added structured propagation metadata to the removed axon-guidance IBA annotation.
  Inspection of the recorded PANTHER node and GOA support traced the inference to
  SLIT-family donors rather than a conserved NOTCH-family function, supporting the
  existing removal decision.
- NOTCH1 is intentionally not an annoton in the cerebellum-development module. The
  original DNER study proposed a DNER–NOTCH1 mechanism, but a later full-text direct
  replication found no DNER binding or activation of NOTCH1
  [PMID:27622512 "DNER is not a Notch ligand and its true function remains unknown."].
  This module-specific evidence correction does not alter NOTCH1's well-supported
  canonical receptor activities elsewhere in the gene review.

## Evidence re-review, 2026-09-20: context and family transfer

The SLIT-seeded PTN002911625 trace does not establish a NOTCH1-specific axon-guidance mechanism, but it also does not refute one. The axon-guidance IBA is now UNDECIDED: direct Drosophila evidence identifies a noncanonical Notch/Disabled/Trio pathway for axon growth and guidance independent of canonical cell-fate signaling [PMID:18062953, “Molecular separation of two signaling pathways for the receptor, Notch.”]. A neutral focused OpenScientist report has been submitted by the coordinating reviewer to distinguish directional guidance, neurite growth and cell-fate effects in human NOTCH1; no duplicate was launched. Enzyme-inhibitor activity is retained as non-core because Notch ankyrin repeats compete with HIF for FIH hydroxylation [PMID:17573339, “Asparaginyl hydroxylation of the Notch ankyrin repeat domain by factor inhibiting hypoxia-inducible factor.”], with follow-up FIH sequestration/cross-talk evidence [PMID:18299578]. Broad transcription/coactivator and cell-periphery terms remain core where they directly capture canonical NOTCH1 function. DLL3 was removed from the list of canonical activating trans ligands. All 378 rows were screened, preserving pleiotropic developmental processes as non-core where appropriate.


## Focused axon-guidance report adjudication, 2026-09-20

The completed OpenScientist report is incorporated with a material identifier correction. The report calls the fly/mouse WITH/FROM genes Notch orthologs, but [FlyBase FBgn0264089](https://flybase.org/reports/FBgn0264089) is sli, and MGI:1315202/1315203/1315205 are [Slit3](https://www.informatics.jax.org/marker/MGI:1315202), [Slit1](https://www.informatics.jax.org/marker/MGI:1315203) and [Slit2](https://www.informatics.jax.org/marker/MGI:1315205). A fresh QuickGO exact-term query confirms those identifiers. Independent primary Notch evidence remains biologically relevant: PMID:21246649 establishes the Trio GEF1/Rac contribution, and PMID:29343637 separates cleavage/tyrosine-dependent axon patterning from cell-fate signaling. PMID:10465425 measures neurite outgrowth/morphology, while PMID:27040987 examines mammalian noncanonical synaptic-protein expression. Neither these different outputs nor absent STRING edges prove loss of guidance. The report did not align the fly determinants or reconstruct the PAINT tree; human conservation remains UNDECIDED. The report is complete and no duplicate query was launched.
