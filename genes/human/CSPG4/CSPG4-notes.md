# CSPG4 (NG2 / MCSP) notes

Deep research providers unavailable in this environment; research from UniProt Q6UVK1 and the 8 cached
publications.

## Topology / localization
- Single-pass type I membrane proteoglycan: signal 1-29, extracellular 30-2224 (laminin G-like domains,
  CS attachment), TM 2225-2245, cytoplasmic 2246-2322 with a C-terminal PDZ-binding motif.
- UniProt: "SUBCELLULAR LOCATION: Cell membrane; Single-pass type I membrane protein; Extracellular side"
  plus apical cell membrane, lamellipodium membrane and cell surface.
- Conclusion: plasma membrane with a very large exposed ectodomain (the basis for anti-MCSP antibodies
  and CAR-T). Golgi-lumen and lysosomal-lumen rows are Reactome glycosaminoglycan biosynthesis/
  degradation reactions acting on the CS chains, not functional locations; ECM-proteomics rows reflect
  the glycanated/shed ectodomain.

## Functions
- Coreceptor/signalling platform: ectodomain binds collagen V/VI, tenascin, laminin, FGF2, PDGF-AA,
  plasminogen, MMP16, galectin-3, and integrins (ITGA4 via the CS chain).
- Signalling: [PMID:10587647 "MCSP stimulation also results in a pronounced activation and recruitment of
  the Rho-family GTPase Cdc42"], requiring ACK1 and p130Cas tyrosine phosphorylation for spreading.
- Cytoplasmic tail binds PDZ proteins (MPDZ first PDZ domain, GRIP1/2) — confirmed en masse by PDZ
  fragmentomics [PMID:36115835].

## Curation decisions
- 21 generic protein-binding rows from PDZ fragmentomics modified to GO:0030165 PDZ domain binding.
- IBA signal transduction modified to intracellular signal transduction (the human-supported level).
- Reactome Golgi-lumen / lysosomal-lumen / extracellular-region rows kept as non-core with explanation.
