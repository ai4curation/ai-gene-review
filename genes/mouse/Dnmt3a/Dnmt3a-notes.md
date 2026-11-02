# Dnmt3a (mouse, O88508) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is a new review. It does not use any ProtNLM2 output. The gene was reviewed in its own right, because
its experimental findings will be the reference for transfer to human DNMT3A (Q9Y6K1).

### Setup and deep research

- I ran `just fetch-gene mouse Dnmt3a`, which seeded 120 GOA rows, and `just fetch-gene-pmids mouse Dnmt3a`
  (23 publications).
- `just deep-research-falcon mouse Dnmt3a --fallback perplexity-lite` FAILED. Falcon gave
  "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient quota). No
  deep-research file exists. The review is based on the cached primary literature and the UniProt record.
- I cached six more mouse primary papers, with PMIDs checked by PubMed title search:
  PMID:20651149 (Wu 2010, neurogenesis), PMID:22138693 (Challen 2011, HSC), PMID:17616512 (Kato 2007,
  germline DMR and repeat methylation), PMID:12897133 (Chen 2003, ES-cell rescue), PMID:31485078 (Weinberg
  2019, H3K36me2), PMID:29056337 (Stroud 2017, neuronal mCA).

### Evolutionary grounding

- Mouse O88508 and human Q9Y6K1 are both in PANTHER PTHR23068:SF10 (DNA (CYTOSINE-5)-METHYLTRANSFERASE
  3A), according to the UniProt DR lines of each record. Dnmt3b and the noncatalytic Dnmt3L are paralogs placed outside SF10.
  The PTHR23068 family review records that Dnmt3L has diverged from catalysis. Dnmt3L-specific functions (stimulator) and
  Dnmt3b-specific ones (minor-satellite methylation) were not transferred.
- IBA rows: the GO:0003886 node (PTN000552637) lists mouse Dnmt3a itself as a donor, which is expected. The
  nucleus (PTN001497036), cytoplasm and negative regulation of transcription (PTN002747444) nodes are
  sound. Only the specificity of the transcription term was refined, to GO:0044027.

### What is experimentally established in mouse (direct evidence)

- DNA C5-methyltransferase activity: unmethylated and hemimethylated substrates are methylated with similar
  efficiency; CpA is methylated about 2x slower than CpG [PMID:11399089 "a high methylation activity was
  also found at CpA sites, which are modified only twofold slower than CpG sites"].
- De novo methylation in ES cells and embryos, with Dnmt3b [PMID:10555141 "Inactivation of both genes by
  gene targeting blocks de novo methylation in ES cells and early embryos"]. Re-expression rescues
  methylation [PMID:12897133].
- Germline imprints: germline cKO removes maternal imprints and most paternal imprints [PMID:15215868
  "both Dnmt3a and Dnmt3L are required for methylation of most imprinted loci in germ cells"]. In
  prospermatogonia Dnmt3a targets H19 and Dlk1/Gtl2 DMRs, SineB1, IAP and Line1, but satellites need only
  Dnmt3b [PMID:17616512 "Only Dnmt3b was required for the methylation of the satellite repeats"]. The Zdbf2
  DMR depends on Dnmt3a [PMID:20385583]. That paper carries a 2014 expression of concern.
- PWWP domain: reads H3K36me3 [PMID:20547484] and H3K36me2 [PMID:31485078]. It targets the enzyme to
  pericentric heterochromatin and is needed for major-satellite methylation in ES cells [PMID:15456878].
- Native Dnmt3a/Dnmt3b complex with mutual stimulation; Oct4/Nanog promoter methylation [PMID:17938196].
- Somatic stem cells: HSC differentiation [PMID:22138693] and postnatal neurogenesis via non-promoter
  methylation [PMID:20651149]. Neuronal mCA [PMID:29056337].
- Regulation: inhibition by MeCP2 binding to the ADD domain, with murine proteins [PMID:30102379];
  sumoylation disrupts HDAC1/2 binding [PMID:14752048]; cysteine auto-methylation side reaction
  [PMID:21481189]; nucleo-cytoplasmic control in germ cells [PMID:15739230].

### Inferred only (not experimentally shown in mouse here)

- Heterotetramer stoichiometry and self-association (UniProt "By similarity" from human structures).
- Nuclear matrix (UNDECIDED), and unmethylated CpG binding as an MF (kept non-core).
- Rat-sourced "response to X" IEAs (xenobiotic, lead, ethanol, cocaine, estradiol, vitamin A, nutrient
  levels, ionizing radiation, hypoxia, hepatocyte apoptosis). All were marked over-annotated because they
  are expression readouts, which matches the human review's handling.

### Key decisions

- All 13 bare protein-binding rows were removed under the protein-binding policy, except HDAC1/HDAC2, which
  were changed to GO:0042826 histone deacetylase binding.
- The DNMT3A2+DNMT3L overexpression transgenic post-embryonic development row (PMID:30834655) was removed as
  a gain-of-function lethality. The CpG-island methylation finding from the same paper is kept.
- The BPA exposure row (PMID:21980460) was removed as an expression readout. The amino-acid stimulus row
  (PMID:20548288) is UNDECIDED because the abstract does not mention Dnmt3a.
- piRNA-directed TE methylation is non-core. SPOCD1 co-purifies with DNMT3A [PMID:32674113], but DNMT3C
  is the principal enzyme for young TEs.
- NEW: GO:0140003 histone H3K36me3 reader activity (mouse PWWP, PMID:20547484).
