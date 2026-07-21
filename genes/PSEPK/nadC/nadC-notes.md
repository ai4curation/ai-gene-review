# nadC curation notes

## 2026-07-20

- Target identity: PP_0787 / UniProtKB Q88PR1, NadC-family quinolinate
  phosphoribosyltransferase [UniProtKB:Q88PR1, "Belongs to the NadC/ModD family."].
- Reaction: quinolinate plus PRPP yields NaMN, carbon dioxide, and diphosphate in
  the physiological biosynthetic direction [UniProtKB:Q88PR1,
  "Reaction=nicotinate beta-D-ribonucleotide + CO2 + diphosphate = quinolinate + 5-phospho-alpha-D-ribose 1-diphosphate + 2 H(+)"]
  [RHEA:12733, quinolinate phosphoribosyltransferase reaction].
- Family grounding: PTHR32179; PAINT node PTN000789406 carries GO:0004514 with
  characterized seed P30011 [GO_REF:0000033, PTHR32179 PAINT tree].
- Curation: GO:0004514 and NAD+ biosynthesis are core. GO:0034213 is retained as
  non-core because quinolinate is consumed, but this is not a separate
  degradation module in KT2440.
- OpenScientist recovered the NadC reaction and conserved QPRTase active-site
  context while explicitly noting that no KT2440 protein study was found. Its
  exact 61.2% pairwise identity and target residue mapping are not retained as
  curated evidence because no alignment artifact was saved; oligomeric state
  and essentiality are likewise ortholog context rather than Q88PR1
  measurements. The report's rejection of a "catabolic" role is interpreted
  narrowly: NadC is not part of
  the `nic*` nicotinate degradation pathway, but the seeded GO:0034213 term can
  still describe consumption of quinolinate and is therefore retained only as
  non-core [file:PSEPK/nadC/nadC-deep-research-openscientist.md,
  "All biochemical, kinetic, structural, and genetic evidence is from orthologs; annotation transfer is well justified by conservation but not experimentally confirmed for PP_0787."].
