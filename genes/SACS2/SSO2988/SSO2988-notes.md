# SSO2988 (Q97UL6) — Saccharolobus solfataricus P2 phosphomevalonate kinase

## Identity check

- Stub `id: Q97UL6` (PMK_SACS2), ordered locus SSO2988 (no gene name in UniProt), 323 aa,
  NCBITaxon:273057. RefSeq NP_344303 / WP_009992639. PANTHER PTHR31814:SF2 (PHOSPHOMEVALONATE
  KINASE), the GHMP-type (ERG8-like) PMK family; NCBIfam NF040957 (Arch_PMK); InterPro
  IPR035102 (Phosphomevalonate kinase).
- Folder uses the ordered locus name, as UniProt gives no gene symbol.
- No provider deep research (no keys in this campaign); this file records the manual search.

## Literature search (2026-11-18)

- NCBI `(Sulfolobus OR Saccharolobus OR Sulfolobales) AND (mevalonate)` -> 10 hits; relevant:
  PMID:23378249 (Nishimura et al. 2013, primary characterisation), PMID:28003359 and
  PMID:26303832 (DMD of S. solfataricus; not this gene), PMID:10600463 and PMID:9171410 (HMGR).
- Europe PMC/NCBI on archaeal pathways: PMID:24327557 (Dellas et al. 2013, eLife, full text) also
  assayed S. solfataricus PMK; PMID:30224495 (A. pernix modified pathway); PMID:40842514
  (Sarnik et al. 2025, screened SsPmvk for cell-free use).
- Identity of the protein assayed by Dellas et al.: their Table 3 lists S. solfataricus PMK as
  gi 15899698; NCBI esummary resolves this to NP_344303, "(phospho) mevalonate kinase
  [Sulfolobus solfataricus P2]", 323 aa, whose sequence is identical to Q97UL6.

## What the papers show

- Recombinant PMK, MVK and DMD of S. solfataricus are all active, and cell-free extracts convert
  only the classical-pathway intermediates [PMID:23378249 "Biochemical characterization using
  recombinant proteins showed that the orthologues of the enzymes catalyzing the late steps of the
  classical pathway, i.e. MVA kinase, PMK and DMD, are all active."; PMID:23378249 "in vitro
  conversion of the intermediates in the classical and modified pathways by cell-free extract from
  S. solfataricus indicated that only the classical pathway likely works in the organism."].
  UniProt records Km 77 uM for (R,S)-5-phosphomevalonate and Vmax 5.1 umol/min/mg at 37 C from
  this paper. Abstract only in the cache.
- Independent kinetic characterisation of the same protein [PMID:24327557 "In our experiments, S.
  solfataricus PMK and MDD activities were detected in steady-state kinetic experiments and GC-MS
  assays, respectively"]; Table 3 gives Km(MVAP) 23.1 uM and kcat 1.98 s-1 for gi 15899698.
- SsPmvk is essentially inactive at 22 C, as expected for a hyperthermophile enzyme
  [PMID:40842514 "Given that SsPmvk was essentially inactive at 22 °C"].

## Does it perform the classical reaction?

Yes. S. solfataricus is one of the few archaea with a complete classical pathway (MVK, PMK, DMD)
as well as an IPK homolog, and both biochemistry on the recombinant protein (two labs) and the
cell-free extract experiment point to the classical route operating in vivo. This member has not
diverged from the PMK function of PTHR31814; it is a genuine archaeal GHMP PMK rather than a
paralog with another activity.

## IBA rows (PTHR31814, node PTN001274235)

- PTN001274235 carries GO:0004631 and GO:0019287 (seeds AT1G31910, SGD ERG8); taxon field empty.
  `just paint-losses SACS2 SSO2988` reports no IRD/IKR on the lineage. The family's plant
  peroxisome IBD (PTN000781523, taxon Eukaryota) does not reach this archaeal member, and no
  peroxisome row is in its GOA set.
- SSO2988 is inside the clade that inherited PMK activity, and its own biochemistry confirms
  the function: both IBAs are sound.
- Family-level note: PTHR31814:SF2 holds fungal ERG8, plant PMK, this archaeal PMK and the
  Streptomyces CL190 PMK (Q9KWG3); the family review currently describes it as fungal only.

## Decisions

- PMK activity (IBA, IEA): ACCEPT, core.
- IPP biosynthesis, mevalonate pathway (IBA, IEA): ACCEPT, core.
- ATP binding (IEA, GHMP N-domain IPR006204): ACCEPT (ATP is the phosphoryl donor in both
  published assays).
- No NEW rows. There is no localization data for this protein; it lacks signal peptides or TM
  segments, but no CC row is added.
