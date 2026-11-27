# JUN notes

- **Deep research.** `just deep-research human JUN --provider perplexity` failed because the configured
  deep-research client reported that `perplexity` was unavailable. Continue the review from UniProt, GOA,
  the PTHR11462 PAINT table, Reactome caches, and cached primary literature.
- **Core AP-1 function.** PTHR11462 PAINT places the core AP-1 transcription factor activities at the
  eukaryotic PTN000894784 node, including `GO:0000978`, `GO:0000981`, `GO:0005667`, and `GO:0045944`.
  The human UniProt record agrees that c-Jun is a nuclear AP-1 transcription factor that recognizes
  `5'-TGA[GC]TCA-3'`, forms AP-1 heterodimers with FOS-family partners, and binds AP-1 cis-regulatory
  DNA. Keep these as core or refine broader DNA-binding, transcription-regulator-complex, and
  transcription-regulation rows to the specific AP-1/Pol II terms.
- **Protein-binding policy.** The large `GO:0005515` block is mostly interaction-database support. Rows
  whose partners are FOS, ATF, BATF, CEBPG, CREB3, CREB5, ETS1, NFATC1/NFATC2, NFE2L2, or SMAD2 were
  refined to `GO:0061629`; MAPK8/MAPK10 rows were refined to `GO:0051019`. Viral, xeno, chaperone,
  cytoskeletal, transport, and large-screen-only interactors were removed as unrefinable bare protein
  binding.
- **Ubiquitin regulation is non-core.** Human DET1 promotes c-Jun ubiquitination through a CUL4A ligase
  [PMID:14739464, "promotes ubiquitination and degradation of the proto-oncogenic transcription factor
  c-Jun"], and PRR7 inhibits c-Jun ubiquitination by FBW7 [PMID:27458189, "PRR7 inhibits the
  ubiquitination of c-Jun by E3 ligase"]. These support ubiquitin-ligase binding rows, but not as core
  AP-1 function.
