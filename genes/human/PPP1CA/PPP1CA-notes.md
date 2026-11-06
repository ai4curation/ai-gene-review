# PPP1CA notes

## Literature search (no deep-research provider available)

Sources checked: the UniProt record P62136 (CC FUNCTION, SUBUNIT, SUBCELLULAR LOCATION), and every publication behind the GOA rows, cached by `just fetch-gene-pmids human PPP1CA` (82 papers). Full text was available for the SHOC2-MRAS-PP1C structure papers, the PNUTS pause-release (mouse) and termination papers, the NBS1 telomere paper, the MYC/PNUTS paper, the iron-PP1 paper, RIG-I/MDA5, Nox4/GADD34, E-cadherin BioID, Sds22/Repo-Man and the circadian paper. Several others were abstract-only (noted in each row's summary). Context only: the integrated stress response and telomere end-joining pathway-choice modules (proposed in ai4curation/ai-gene-review#5904).

## Key findings

- Catalytic subunit with no intrinsic selectivity: [PMID:35768504 "although PP1C in isolation lacks intrinsic substrate selectivity"]
- SMP complex: [PMID:35830882 "The MRAS-SHOC2-PP1C holophosphatase dephosphorylates RAF at serine 259"]
- PNUTS-PP1 and pause release: [PMID:39603240 "PNUTS-PP1 promotes pause release by dephosphorylating multiple substrates, including the 7SK small nuclear ribonucleoprotein particle (snRNP) subunit MEPCE"]
- PNUTS-PP1 and termination: [PMID:31677974 "We report that PNUTS-PP1 phosphatase is a negative regulator of RNA polymerase II (Pol II) elongation rate."]
- PTW/PP1 complex: [PMID:20516061 "a stable multimeric complex composed of regulatory subunits PNUTS, Tox4, and Wdr82 and a PP1 catalytic subunit (denoted as the PTW/PP1 phosphatase complex)"]
- eIF2alpha phosphatase: [PMID:26095357 "Here, we report detailed structural and functional analyses of the GADD34:PP1 holoenzyme and its recruitment of eIF2α."]
- NBS1 at telomeres: [PMID:28216226 "The phosphatase PP1-α de-phosphorylates mNBS1S433 to promote interaction between NBS1 and TRF2"]
- Location: [PMID:17965019 "PP1alpha is primarily nuclear and largely excluded from nucleoli"]
- Metal: [PMID:30403291 "The phosphatase requires divalent metal cations for catalytic activity and contains iron naturally."]

## Curation decisions

- All 225 bare GO:0005515 rows: REMOVE, per the protein-binding policy. The interactions are mostly with regulatory subunits; their content is captured by the PP1 complex and PTW/PP1 complex CC rows.
- phosphatase activity / phosphoprotein phosphatase activity: MODIFY to GO:0004722.
- regulation of translational initiation in response to stress: MODIFY to GO:0036496 (eIF2alpha dephosphorylation), the term that names the PP1-catalysed step.
- Glycogen, synaptic and circadian rows (mostly rodent transfers): KEEP_AS_NON_CORE as holoenzyme- or tissue-specific roles.
- Photoperiod entrainment, response to lead, exosome, cadherin binding/cell-cell adhesion, PP1 binding, RNP/complex binding: MARK_AS_OVER_ANNOTATED.
- Cited TAS PMID:10640627 is about PP2A/PP2B rather than PP1. The activity row is accepted on other evidence.
