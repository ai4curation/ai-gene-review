# Tp53 (rat, P10361) curation notes

## Re-review 2026-10-10

### What GOA changed
- GOA refresh seeded 135 new rows (now 351 total). Most are qualifier or donor splits of
  existing ISO terms: MGI now uses `acts_upstream_of_or_within` for mouse Trp53 (MGI:98834)
  phenotype-based annotations, and human TP53 rows are split by isoform (P04637-2, -4, -7 etc.).
  About 60 carried terms the review had not seen, mostly mouse phenotype terms
  (development, lymphocyte, cardiac, metabolic).
- New IBA rows for chromatin and nucleus with `is_active_in`, an IEA protein tetramerization
  row with `involved_in`, and two `acts_upstream_of` IMP rows for PMID:30514107.
- One row is retired: GO:0005515 IPI PMID:15872011 (nucleophosmin).

### Pending rows (135): 29 ACCEPT, 77 KEEP_AS_NON_CORE, 24 MARK_AS_OVER_ANNOTATED, 1 MODIFY, 4 UNDECIDED
- Mouse developmental phenotypes (in utero/embryo development, somitogenesis, gastrulation,
  CNS/cerebellum/heart development, septum morphogenesis, organismal growth, lymphocyte
  lineage/thymic differentiation) were marked over-annotated. The donor studies are
  compound mutants (Gcn5, Jmjd5, Rps6, Mdm2/Mdm4, PACT, ASPP2) in which p53 *activation*
  causes the defect [PMID:26334721 "Genetic studies have shown that aberrant activation of p53 signaling leads to embryonic lethality."]
  [PMID:17000767 "a p53-dependent checkpoint is activated during gastrulation in response to ribosome insufficiency"].
- Mitochondrial matrix rows (ISO/ISS) kept as non-core:
  [PMID:22726440 "In response to oxidative stress and ischemia, p53 protein accumulates in the mitochondrial matrix and triggers PTP opening, mPT and necrosis by physical interaction with the critical PTP regulator CypD."]
- Endoplasmic reticulum rows over-annotated (p53 is a substrate of the ER ligase synoviolin)
  [PMID:17170702 "Synoviolin sequestrated and metabolized p53 in the cytoplasm"].
- Necroptotic process (GO:0070266) MODIFY to programmed necrotic cell death (GO:0097300): the
  p53 mechanism is cyclophilin D/permeability-transition necrosis, not death-receptor necroptosis.
- Protein import into nucleus, protein stabilization, chromosome organization, histone
  deacetylase regulator activity, gene expression, regulation of tissue remodeling marked
  over-annotated (p53 is cargo/upstream trigger, or the term is generic)
  [PMID:15657445 "Chromatin binding of p53 at the histone-acetylated SBE/p53RE region promotes the interaction of corepressor SnoN and HDAC complexes"].
- UNDECIDED (4):
  - GO:0035861 site of double-strand break (mouse IDA PMID:24550317): the cached paper only
    mentions 53BP1 ["tumor protein P53 binding protein foci formation"]; possible Trp53bp1 confusion at MGI.
  - GO:1903799 negative regulation of miRNA processing (PMID:21522133): the paper shows
    p53-dependent miR-29 transcription, not processing.
  - GO:0045861 negative regulation of proteolysis (PMID:23277542): the paper studies
    "p53-independent c-Myc-induced apoptosis".
  - NOT GO:0001701 in utero embryonic development (PMID:9425892, a correspondence with no
    abstract) conflicts with the positive row from other compound mutants.

### Changed actions on existing rows (7)
- GO:0005515 protein binding (IPI PMID:11278372, TAFII31): MARK_AS_OVER_ANNOTATED -> MODIFY to
  GO:0001223 transcription coactivator binding [PMID:11278372 "The coactivator protein TAF(II)31 binds to p53 at the amino-terminal region"].
- GO:0005515 (IPI PMID:8389468, WT1): MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0061629
  [PMID:8389468 "WT1 encodes a transcription factor which binds to the EGR1 consensus sequence"].
- GO:0005515 (IPI PMID:12464630, nucleostemin): MARK_AS_OVER_ANNOTATED -> REMOVE (generic,
  no more specific MF supported; interaction not disputed).
- GO:0005515 (IPI PMID:15872011, nucleophosmin, retired): MARK_AS_OVER_ANNOTATED -> REMOVE.
- GO:0005759 mitochondrial matrix (IEA SL-0170): MODIFY (-> outer membrane) -> KEEP_AS_NON_CORE;
  the earlier "not in the matrix" premise is contradicted by PMID:22726440 and PMID:24101517.
- GO:0031000 response to caffeine (IEP PMID:16544096): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED;
  caffeine was used as an ATM inhibitor ["caffeine (ATM kinase inhibitor) inhibited Ser-15 phosphorylation"].
- GO:0010038 response to metal ion (IEP PMID:17466256): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED;
  the platinum drug acts via DNA damage ["attack on DNA, leading to fast activation of p53 and caspase-3"].

### Other edits
- Added `supported_by` (verbatim UniProt CC, deep-research or cited-paper quotes) to 185
  existing rows that had none; added the cited PMIDs and UniProtKB:P10361 to references.
- Description: removed curation commentary ("captured here", "GOA set"); added the
  transcription-independent necrosis role.
- core_functions unchanged (TF activity, DNA-damage response, p53-mediated intrinsic
  apoptosis, G1 checkpoint).

### Open questions
- See suggested_questions for the three donor-side checks behind the UNDECIDED rows.
- Whether the many cell-type-specific apoptosis/proliferation ISO terms from mouse should
  transfer to rat at all remains a judgment call; they were kept as non-core.
