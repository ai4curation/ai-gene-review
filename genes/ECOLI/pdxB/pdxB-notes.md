# pdxB review notes (E. coli K-12, P05459)

Reviewed as the reference exemplar for step 2 of the DXP-dependent de novo PLP
module; P05459 is the sole seed of PAINT node PTN000107798 (PTHR42938:SF9).

## Provenance

- No deep-research provider was available (no provider API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  UniProt record, the PTHR42938 PAINT file and cached publications.
- Literature checked: PMID:20831184 (full text), PMID:7751290, PMID:3029017,
  PMID:374678, PMID:15911532 (abstract-only), PMID:18304323 (PdxB not named in
  parsed text).

## Function

- Reaction. [PMID:20831184 "PdxB catalyzes the second step in the biosynthesis
  of pyridoxal phosphate by oxidizing 4-phospho-d-erythronate (4PE) to
  2-oxo-3-hydroxy-4-phosphobutanoate (OHPB) with concomitant reduction of
  NAD(+) to NADH."]
- Nicotino-enzyme reoxidized by alpha-keto acids. [PMID:20831184 "a variety of
  physiologically available α-keto acids serve as oxidants of PdxB to sustain
  multiple turnovers"]
- Kinetics. [PMID:20831184 "a k(cat) of 1.4 s⁻¹, a K(m) of 2.9 μM"]
- Dimer. [PMID:20831184 "The protein migrated as an apparent dimer by gel
  filtration chromatography"]
- Genetics. [PMID:3029017 "Complementation experiments confirmed that usg-2 is
  indeed pdxB"]

## Curation decisions

- GO:0033711 core MF; GO:0036001 core process; GO:0008615 accepted (GO's term
  for the UniPathway PNP branch, no PNP-specific GO term).
- GO:0016491 and GO:0016616 refined to GO:0033711; GO:0046983 refined to
  GO:0042803 (IDA); cytoplasm refined to cytosol.
- Cytosol rows (IBA, 2 IDA, ARBA IEA) KEEP_AS_NON_CORE, matching the P. putida
  PdxB cytosol verdict fixed by the TreeGrafter rereview of 2026-09-24.
- Open question for GO: the in vivo net reaction couples 4PE oxidation to
  2-oxo-acid reduction via bound NAD(H); GO:0033711 describes the NAD+
  half-reaction only. Recorded as a suggested question, not a new term.
