# coq7 (O74826, SPBC337.15c) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (HAMAP MF_03194) and the cached
literature; PMID:24911838 was read in full, PMID:18808426 from the abstract.

## Literature

- DMQ10 accumulates in the deletion [PMID:18808426 "We first confirmed that coq7 is
  necessary for the penultimate step in ubiquinone biosynthesis, from the observation that
  the deletion mutant accumulated the ubiquinone precursor demethoxyubiquinone-10 instead
  of ubiquinone-10."]
- Mitochondrial [PMID:18808426 "Finally, Coq7 was found to localize in mitochondria,
  consistent with the possibility that ubiquinone biosynthesis occurs in mitochondria in
  yeasts."]
- Complementation [PMID:24911838 "An HPLC peak that we previously identified as
  demethoxyubiquinone (DMQ10) [22] was detected in the Δcoq7 strain; this peak was fully
  converted to CoQ10 by expression of S. pombe coq7 and partly converted by expression of
  HsCOQ7 containing a mitochondrial targeting signal (Figure 7A)."]
- No purified-enzyme assay for S. pombe Coq7.

## Audit decisions (2026-11)

- Location rows previously quoted the DMQ sentence; replaced with the localisation
  sentences of the cited papers. The PomBase inner-membrane EXP rows are accepted: the
  papers resolve only mitochondria, but the claim agrees with yeast Cat5/Coq7 IDA.
- Core function GO:0160224 (module annoton; human COQ7 core). The S. cerevisiae CAT5
  review uses GO:0008682 as core and keeps GO:0160224 as non-core; here both are
  accepted. Flagged as a sibling difference for the coordinator.
