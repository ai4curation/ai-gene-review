# CASP8 notes

## 2026-09-30

- Seeded and completed the human CASP8 review from GOA, UniProt, cached PubMed
  records, Reactome, GO-CAM models, and PAINT transfer context.
- Kept the CASP8 core centered on three direct mechanisms: FADD/death-effector
  domain recruitment to death-inducing signaling complexes, Asp-directed
  cysteine endopeptidase activity that matures downstream procaspases and
  gasdermin substrates, and RIPK1 cleavage that restrains RIPK1/RIPK3-dependent
  necroptosis.
- Tightened top-level `GO:0006915 apoptotic process` assertions toward
  death-domain receptor extrinsic apoptotic signaling, while leaving the
  abstract-only PMID:22891283 Fas vesicle row `UNDECIDED`.
- Moved CASP8 away from effector-only `GO:0097194 execution phase of apoptosis`
  wording. CASP8 is an initiator that activates CASP3/CASP7 and other
  substrates by proteolytic maturation; CASP3 and CASP7 carry the direct
  executioner role.
- Removed all 94 generic `GO:0005515 protein binding` rows. The FADD/CFLAR/FAS
  edges were either already represented by specific death-effector-domain or
  DISC annotations, and the BioPlex, binary-interactome, viral-inhibitor, and
  other screen edges did not identify a CASP8-specific molecular activity.
- Removed the impossible Ensembl electronic `GO:0030690 Noc1p-Noc2p complex`
  mapping to human CASP8, together with stimulus-response and assay-readout rows
  that did not establish direct CASP8 work.
- Kept pyroptosis, dectin-1 inflammasome, TLR3/TLR4 ripoptosome, N4BP1 innate
  immune, and host-pathogen perturbation rows as non-core where they captured
  real CASP8-containing complexes or substrate-cleavage branches.
- Deferred rows whose visible cached evidence was abstract-only, review-derived,
  or centered on a different caspase or readout, including the
  HSP70/GATA1 localization rows, the COP/CARD-only protein paper, the
  CAAP/C9orf82 paper, the p23 paper, and specific immune differentiation terms
  sourced only to PMID:18309324.
