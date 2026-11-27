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
- **AI review follow-up.** The `GO:0003700` rows refine to `GO:0000981`, not `GO:0000978`, because the
  existing term asserts transcription-factor activity rather than only DNA binding. The `GO:0035497`
  cAMP response element binding row from PMID:19861239 is kept as a direct, target-specific activity
  [PMID:19861239, "Using chromatin immunoprecipitation assays we showed comparable in vivo cJun and
  CREB1 binding to the G-CRE region"] rather than generalized to AP-1 Pol II cis-regulatory binding.
- **Miscited GOA rows.** PMID:11804590 is the ARAP1 Arf/Rho GAP paper and does not support JUN
  `GO:0005096` [PMID:11804590, "We have identified ARAP1 and ARAP2"]. PMID:14645924 attributes HPV-16
  P542 regulation to AP-4 and hSkn-1a, so the JUN rows that cite it now carry `source_defects` for
  UniProt checking rather than using that PMID to justify an AP-1-specific refinement.
- **Target-specific miRNA transcription.** The `GO:1902895` miR-92a transcription rows fit AP-1/Pol II
  transcriptional regulation but are target-specific lymphoma-cell outputs of the ERK1/2-AP1 axis
  [PMID:24375836, "Downregulation of miR-92a by AZD6244 is mediated by the ERK1/2-AP1 signalling
  pathway"], so they are retained as non-core rather than marked over-annotated.
- **Chromatin support.** The TFClass `GO:0000785` row is also supported by a direct JUN
  chromatin-associated TAP/MS workflow [PMID:25609649, "NF-kappaB1, JUN, FOS with treatment of 25 ng/ml
  TNF-alpha for 8 h to promote chromatin association"], so it no longer quotes the generic UniProt AP-1
  function text.
