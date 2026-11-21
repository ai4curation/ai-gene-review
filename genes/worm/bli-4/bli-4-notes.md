# bli-4 notes

## 2026-11-21 curation notes

Deep research could not be generated in this checkout: `just
deep-research-falcon worm bli-4 --fallback perplexity-lite` failed because the
`falcon` and `perplexity-lite` providers were unavailable and `agentapi` was
not on the path. The review therefore uses the fetched WormBase gene
description, UniProt, PAINT/InterPro caches, and local cached publications.

`just paint-losses worm bli-4` reported no IRD or IKR loss on the BLI-4/P51559
lineage.

## Core cuticle role

- PMID:7774813 is abstract-only locally. It cloned `bli-4`, established that
  it encodes alternatively spliced Kex2/subtilisin-like proprotein convertases
  with shared N termini and divergent C termini, placed the embryonic lethal
  alleles in shared exons, and showed that the viable `e937` adult-blistering
  allele removes the exon unique to blisterase A.
- PMID:10903434 is abstract-only locally. Its abstract reports that
  Kex2/subtilisin-like proteinase activity is required for adult cuticle
  production, that lethal alleles cluster in shared exons including the
  peptidase domain, and that the `h384` allele changes the catalytic Ser-415.
- PMID:37721936 is full text locally and refines the cuticle mechanism. The
  paper generated an endogenous BLI-4::SfGFP fusion, found BLI-4 in sub-apical
  intracellular compartments and faintly in the extraembryonic space, produced
  null and isoform-specific alleles, and showed that BLI-4 promotes secretion
  of SQT-3 and DPY-17 cuticle collagens. The SQT-3 and DPY-17 consensus furin
  cleavage-site mutants phenocopy `bli-4` loss, strongly implicating BLI-4 in
  N-terminal collagen processing before efficient secretion, but direct
  biochemical cleavage of those two sites by BLI-4 remains untested.
- PMID:19716386 is abstract-only and centers on the BLI-5 Kunitz-domain
  protein rather than BLI-4. It is useful only as a parasite/cuticle-context
  citation here: the abstract describes BLI-5 as working in cuticle collagen
  biosynthesis through interaction with subtilisin-like processing enzymes such
  as BLI-4.

## Non-core ASEL role

- PMID:24013594 is full text locally. In the adult high-salt circuit, ASEL
  requires BLI-4 to process and release insulin-like neuropeptides that recruit
  AWCON to respond to high salt. The paper combined a `bli-4` hypomorph,
  ASEL-specific `bli-4` RNAi, `ins-6` genetics, and an `ins-6` cleavage-site
  mutant to support the model that BLI-4 matures INS-6 in ASEL. This is a
  genuine peptide-processing function but a tissue-specific side role relative
  to BLI-4's essential cuticle-collagen processing.
- The full text explicitly contrasts BLI-4 in the ASEL salt circuit with
  EGL-3-dependent INS-6 processing for neuromuscular-junction development.
  The PMID:23665919 EMBO J abstract also identifies EGL-3, not BLI-4, as the
  prohormone convertase in FSN-1-mediated synapse development. Because that
  article is abstract-only here, the BLI-4 rows on
  `GO:0045887 positive regulation of synaptic assembly at neuromuscular
  junction` are left undecided rather than removed.

## Localization

- UniProt models BLI-4 as a signal-peptide, type-I membrane proprotein
  convertase with a lumenal peptidase domain, a single transmembrane helix, and
  a short cytoplasmic tail. The PTHR42884 PAINT cache places serine-type
  endopeptidase activity and generic protein processing on the deep
  proprotein-convertase node and places Golgi/TGN location on an opisthokont
  node. The direct BLI-4::SfGFP reporter in PMID:37721936 resolves endogenous
  BLI-4 to sub-apical intracellular compartments and the extraembryonic space,
  so the exact BLI-4 cleavage compartment remains below current GO granularity.
- The WormBase 2004 `GO:0005634 nucleus` IDA row, citing PMID:7774813, is not
  consistent with the BLI-4 topology or the endogenous 2023 reporter. The 1995
  full text is not cached, so the review leaves the row undecided rather than
  asserting a structured upstream defect.
