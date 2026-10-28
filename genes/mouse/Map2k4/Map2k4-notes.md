# Map2k4 (mouse) review notes

- Fetched with `just fetch-gene mouse Map2k4`; UniProt P47809 confirmed (Swiss-Prot, MGI:1346869). 47 GOA rows.
- Deep-research API unavailable; literature synthesis in `Map2k4-deep-research-manual.md`.
- Read full text: PMID:10521398, PMID:10523642, PMID:24705900, PMID:20550965. Others abstract only.
- Prior reviews used for consistency: `genes/rat/Map2k4`, `genes/human/MAP2K4`.

## Key decisions

- Core MF: JUN kinase kinase activity (GO:0008545) in the JNK cascade; secondary MAP kinase kinase activity
  (GO:0004708) toward p38 in the p38MAPK cascade [PMID:7839144 "MKK4 did activate JNK"].
- NMJ development IMP (PMID:10521398): REMOVE, wrong gene (Erbb2 allele MGI:1929071; full text has no MKK4).
- ERBB signaling IDA (PMID:8702681): UNDECIDED, abstract describes ERK-pathway MEK; full text unavailable.
- negative regulation of motor neuron apoptotic process (PMID:25100604): MODIFY to positive regulation
  [PMID:25100604 "completely resistant to axotomy-induced death"]; source defect recorded.
- UniProt DISRUPTION PHENOTYPE says cardiac deletion "prevents pathological cardiac hypertrophy" but
  PMID:19265040 reports exacerbated hypertrophy; recorded as a UniProt source defect on the cardiac growth row.
- Bare protein binding rows (MEKK1, JIP3/JSAP1): REMOVE per protein-binding policy.
