# serC review notes (E. coli K-12, P23721)

Exemplar for step 3 of the DXP-dependent de novo PLP module and a seed of the
PTHR43247 SerC/PSAT PAINT node PTN000475655.

## Provenance

- No deep-research provider was available (no provider API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  UniProt record, the PTHR43247 PAINT file and cached publications.
- Literature checked (all abstract-only except PMID:19402753): PMID:2121717,
  PMID:8706854, PMID:3518706, PMID:4570768, PMID:9037153, PMID:15690043,
  PMID:19402753, PMID:15911532, PMID:18304323.

## Function

- Dual pathway role. [PMID:2121717 "Chromosomal insertions in serC caused a
  requirement for pyridoxine, serine, and aromatic compounds, which directly
  verified that SerC functions in the pyridoxine biosynthetic pathway."]
- Phosphorylated substrate in the B6 branch. [PMID:8706854 "Both enzymes used
  4-O-phosphoryl-L-threonine rather than 4-hydroxy-L-threonine as a substrate"]
- Serine auxotrophy. [PMID:4570768 "The auxotrophy was caused by a mutation in
  the structural gene for phosphohydroxy-pyruvate transaminase (serC)"]
- Kinetics (UniProt, from PMID:8706854): Km 17 uM phosphoserine, 15 uM
  3-phosphonooxypyruvate, 110 uM 4-phosphonooxy-L-threonine.

## Curation decisions

- Core MF GO:0004648 (serine pathway). GO has no MF for the
  phosphohydroxythreonine reaction (RHEA:16573), so GO:0004648 is not used for
  it; the second core function uses `proposed_molecular_function`
  "phosphohydroxythreonine aminotransferase activity", the same proposal as the
  P. putida SerC review.
- GO:0042823 IMP refined to GO:0036001 (added as NEW, IMP PMID:2121717).
- GO:0006563 IGI (spinach PSA complements serC) refined to GO:0006564.
- Cytoplasm (IBA and IEA) refined to cytosol (two IDA rows); cytosol non-core.
- Three bare GO:0005515 IPI rows (DnaK, SelB) removed per protein-binding policy.
- PLP binding and homodimerization non-core.
