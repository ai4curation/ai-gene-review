# XPC notes

## Deep research status

- `just deep-research-falcon human XPC --fallback perplexity-lite` was attempted on
  2026-11-27. Falcon failed because the provider was unavailable in this environment,
  and the Perplexity-lite fallback failed for the same reason before producing an
  artifact. The review below is therefore a manual synthesis from the seeded GOA rows,
  XPC's UniProt record, the cached primary literature, Reactome GG-NER events, and the
  PANTHER PTHR12135 family metadata.

## Functional synthesis

- Human XPC is the DNA-damage-recognition subunit of the XPC-RAD23-CETN2 complex. The
  family fetch places Q01831 in the XPC/Rad4 PANTHER family PTHR12135 and the
  reviewed-protein slice has only one human member, XPC; the other reviewed members are
  fungal, fly, mouse, and Arabidopsis Rad4/Xpc orthologs.
- The core activity is global-genome nucleotide-excision repair. XPC-HR23B was purified
  as the XP-C complementation factor in early repair assays
  [PMID:8168482, "repair complex by in vitro complementation of the XP-C defect"], and
  later work identified XPC-HR23B as the earliest damage detector upstream of XPA
  [PMID:9734359, "XPC-HR23B as the earliest damage detector to initiate NER"].
- The molecular function is not generic DNA binding. XPC-RAD23B recognizes unpaired bases
  and distorted duplex structures; the purified complex prefers UV-damaged over
  undamaged DNA and also binds single-/double-strand junctions
  [PMID:10873465, "400-fold preference for binding of XPC-hHR23B to UV damaged over
  non-damaged DNA"; PMID:12509299, "specific secondary structures of DNA, involving a
  single- and double-strand junction, were strongly preferred by the complex"].
- XPC forms a trimeric XPC complex with RAD23B and CETN2. Araki et al. found that nearly
  all XPC complexes contain CETN2 and that CETN2 stabilizes XPC with HR23B
  [PMID:11279143, "nearly all XPC complexes contain CEN2"].
- XPC also has a reproducible but secondary transcriptional coactivator branch. The
  XPC-RAD23-CETN2 complex coactivates pluripotency transcription with Oct4/Sox2 in
  embryonic stem cells [PMID:21962512, "required for the synergistic activation of Nanog
  by Oct4 and Sox2 in vitro"], recruits KAT2A/ATAC through E2F1 at human class II
  promoters [PMID:29973595, "XPC interacts with E2F1"], and licenses KAT2A-dependent
  H2A.Z.1 acetylation at transactivated promoters [PMID:31527837,
  "XPC-RAD23-CEN2 interacts both with H2A.Z and KAT2A"].
- XPC localizes dynamically between the nucleus, chromatin, and cytoplasm. The
  high-confidence repair site is nuclear/chromatin; diffuse plasma membrane, perinuclear,
  neuronal-cell-body, and nuclear-pore annotations inherited from broad electronic
  mappings are not supported by the curated localization and NER literature
  [PMID:18682493, "XPC constantly associates with and dissociates from chromatin"].
- Bare `GO:0005515` protein-binding rows from affinity-purification screens and pairwise
  interaction experiments were all removed under the project protein-binding policy while
  preserving every source row and its WITH/FROM interactor.
