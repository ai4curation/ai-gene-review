# Syt4 (rat, P50232) review notes

## Session 2026-10-28

- `just fetch-gene rat Syt4` resolved P50232 (Swiss-Prot, RGD:68397, GeneID 64440); 128 GOA rows.
- No deep-research API keys; manual synthesis in `Syt4-deep-research-manual.md`.
- Full text read for PMID:18508778, 20688915, 10397765, 16618809, 15197251, 20303854,
  20735850, 21551071, 29166604, 30021165, 19448629 and 19136969 (both mouse). Abstract-only:
  PMID:10217258, 10646502, 15311271, 18046461, 22939844, 26750488, 7791877, 7892240, 9830048,
  7993622, 9162066, 15390175, 21576241, 12135783, 18468511, 23999003.

### Key judgements

- Core biology: rat Syt4 is a Ca2+-insensitive synaptotagmin. It binds t-SNAREs and syntaxins
  Ca2+-independently, inhibits SNARE-catalysed fusion and acts as a negative regulator of
  Ca2+-triggered dense-core vesicle exocytosis [PMID:18508778, PMID:20688915, PMID:21551071]. It is
  also an ISG-membrane protein needed for ISG homotypic fusion and granule maturation
  [PMID:16618809], and a DCV-membrane link to KIF1A for axonal DCV transport [PMID:29166604].
- Removed `calcium ion sensor activity` (IBA) and `calcium-dependent activation of synaptic vesicle
  fusion` (IBA). The rat protein shows functional divergence from the family node (PMID:15311271,
  PMID:20688915).
- Removed the ISO of `calcium-dependent phospholipid binding` because rat biochemistry contradicts
  it. `calcium ion binding` (ISO) marked over-annotated: older oligomerisation data suggested C2B
  Ca2+ effects, but crystallography says C2B cannot form full Ca2+ sites.
- PS binding: the two Chapman-lab papers disagree (Ca2+-independent binding in co-flotation in
  2008; none in co-sedimentation in 2010). The positive row is kept as non-core and the NOT row is
  accepted (no Ca2+-dependent binding, the functional point).
- `NOT syntaxin binding` (PMID:7791877, BHF-UCL): the abstract reports only that Ca2+-dependent
  syntaxin binding is absent for Syt IV C2A. Several later papers show Ca2+-independent syntaxin
  binding. Marked UNDECIDED, with a CHECK source defect.
- `microvesicle` (GO:1990742, an extracellular vesicle): this comes from the mouse
  ARUK-UCL IDA on PMID:19136969. In that paper "microvesicles" are intracellular synaptic-like
  microvesicles in nerve terminals, so the term is wrong. Removed and recorded as a source defect.
- `positive regulation of dendrite extension` ISO from human UniProt IDA PMID:23999003. That paper
  is about melanocyte dendrites (abstract focuses on SYT14L), and GO dendrite extension refers to
  neuronal dendrites. Marked over-annotated, with a SUSPECTED CHECK defect.
- The 30021165 protein-binding row has With/From TANC2 (F1LTE0). The paper shows Syt4 co-purifying
  with KIF1A, not TANC2, so this is a probable WRONG_WITH_FROM.
- The axon IMP row (PMID:29166604) is a location backed by imaging: kept, with a
  WRONG_EVIDENCE_CODE CHECK.
- NEW: kinesin binding (GO:0019894) to KIF1A (PMID:29166604, PMID:30021165).
