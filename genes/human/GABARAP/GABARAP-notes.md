# GABARAP notes (human, O95166)

Deep research: not run (falcon times out after 600 s in this environment and perplexity-lite is not
installed). Review based on cached publications and the UniProt record.

## Key findings
- Form II (PE-conjugated) on autophagosomes [PMID:15169837 "Generation of the form II correlates with autophagosome association of GABARAP and GATE16."].
- GABARAP subfamily governs autophagosome-lysosome fusion via PLEKHM1 and drives PINK1/Parkin mitophagy [PMID:27864321 "We find that the GABARAP subfamily promotes PLEKHM1 recruitment and governs autophagosome-lysosome fusion"].
- FLCN-FNIP sequestration -> TFEB/TFE3, lysosome biogenesis [PMID:34597140 "GABARAP directly binds to a previously unidentified LC3-interacting motif (LIR) in the FLCN/FNIP tumor suppressor complex and mediates sequestration to GABARAP-conjugated membrane compartments."]; also in STING-induced TFEB activation [PMID:39423796].
- ER-phagy receptor UBAC2 [PMID:39284914].
- GABA(A) receptor gamma2 and tubulin binding [PMID:9892355].
- CUL3-KBTBD6/7 scaffold for TIAM1 degradation [PMID:25684205].

## Decisions
- 101 protein binding IPI rows: REMOVE (uninformative).
- Core: PE binding (autophagosome maturation/assembly/mitophagy); protein sequestering activity (lysosome biogenesis); GABA receptor binding (neuronal trafficking).
- Death-domain receptor apoptosis (DDX47 co-overexpression) and chemical synaptic transmission: MARK_AS_OVER_ANNOTATED.
- Mouse-derived locations (smooth ER, sperm midpiece, axoneme, Golgi, plasma membrane, lysosome) kept as non-core.

## 2026-11-21 ORGANELLES peroxisome/lysosome batch 1

- Lysosome (GO:0005764) IEA row: Ensembl projection (GO_REF:0000107) of the MGI IDA on mouse
  Gabarap (Q9DCD6) from PMID:11146101 (abstract-only; abstract reports punctate structures only, no
  lysosome). Donor unreadable, so alone UNDECIDED; rescued for the root by readable human evidence in
  PMID:34597140 (full text cached): CASM conjugates ATG8s to LAMP1-positive single-membrane
  lysosomes, and GABARAP sequesters FLCN-FNIP there (confirmed on TMEM192 immuno-isolated lysosomes)
  to activate TFEB. Kept KEEP_AS_NON_CORE as a regulated functional pool, distinct from autophagic
  delivery of GABARAP for degradation (which alone would not be a location). LAMP1 images show LC3B
  and GABARAPL1 rather than GABARAP; recruitment is stimulus-dependent, so no GO:0098574 row.
  Autophagosome rows out of scope.
