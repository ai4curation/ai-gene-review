# bcoE-bcoF (Q92NF5) curation notes

## 2026-11-04 — review for the bacterial L-carnitine catabolism module

- Scaffolded with `just fetch-gene RHIME bcoE-bcoF` while generalizing
  `modules/bacterial_l_carnitine_catabolism.yaml` beyond P. putida KT2440.
- No provider deep research was generated for this gene in this session (no
  provider run was available); no `-deep-research-*.md` file exists. The review
  rests on the curated UniProt entry, GOA, and the cached publications.
- Literature checked: PMID:19406895 (Wargo and Hogan 2009, P. aeruginosa
  carnitine locus; abstract only), PMID:24240508 (Bastard et al. 2014, BKACE
  screen; abstract only), PMID:19919675 (Chen et al. 2010, Cbc/CaiX; full text),
  PMID:30670548 (Bazire et al. 2019, S. meliloti carnitine metabolism; abstract
  only, PMC6416908 full text could not be retrieved), PMID:4302217 (Aurich et al.
  1968, P. aeruginosa carnitine dehydrogenase; no abstract cached).
- Where the cached paper is abstract-only, experimental detail (kinetics,
  disruption phenotypes, EC assignment) is quoted from the UniProt statements
  that carry ECO:0000269 evidence for that paper.
- GO has no exact terms for EC 2.3.1.317 (CdhC/BcoG) or EC 3.1.2.33
  (CdhB/BcoE-BcoF C-terminal region); these are recorded as proposed_new_terms
  and annotated at the parents GO:0016747 and GO:0016289.


## 2026-11-07 full-primary re-review

Full PMID30670548 was read from an official independent PMC HTML capture; the protected abstract cache is unchanged. Sequence comparison against CP004140.1 establishes496/496 BcoEF and300/300 BcoG identity to Rm2011, while the primary links the cloned 3D0a2 coding sequences to Rm2011. Native1021 GBB-growth failure must not be replaced by the positive3D0a2/Rm2011 phenotypes. Full assays used recombinant intact proteins, not independently isolated fusion domains.

BcoEF hydrolyzes carnitinyl-CoA as well as betainyl-CoA and oxidizes carnitine. Its former no-substrate-route claim and stale question are corrected. BcoG mutant attribution is unsupported by the primary mutant list; its historical IMP proposal is explicitly retired with exact archive, while actual catalytic participation remains in the metabolic-row refinement and core. No new annotations were added.

Default Falcon attempts for both genes failed403; no provider file was fabricated. PAINT-loss commands completed, but neither exact accession is present in the cached tree, so losses are unassessed rather than absent. All payloads and protected source bytes are preserved. See rhime-consultation proof and gene source-analysis for details.

The existing carnitine-metabolic parent is refined to both biosynthesis and catabolism: the same enzyme releases carnitine from carnitinyl-CoA and performs downstream degradative reactions. The added replacement term is not a new row; direct chemistry establishes participation. The module may keep the upstream reaction outside its boundary.

## 2026-11-07 PR6182 round1 follow-up

The redundant historical GO:0042413 NEW proposal is retired in place, preserving source payload/action/order and the supported metabolic-process refinement. GO:0070403 changes from KEEP_AS_NON_CORE to ACCEPT because NAD+ binding is integral to measured NAD-dependent carnitine oxidation. Full PMID30670548 Results/Table1 and the existing exact sequence bridge were rechecked. The carnitine-biosynthesis refinement refers to carnitinyl-CoA hydrolysis producing a transient intermediate of GBB utilization, not mammalian BBOX chemistry.

See the round1/core-consultation audit for immutable payload/source preservation and validation. Previously generated research and primary-source records were reused without modification.
