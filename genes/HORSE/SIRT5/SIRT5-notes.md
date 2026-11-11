# SIRT5: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/Q9NXA8/entry

Primary source: [PMID:22076378 Sirt5 is a NAD-dependent protein lysine demalonylase and desuccinylase.](https://pubmed.ncbi.nlm.nih.gov/22076378/).

> We found that Sirt5
> is an efficient protein lysine desuccinylase and demalonylase in vitro. The
> preference for succinyl and malonyl groups was explained by the presence of an
> arginine residue (Arg(105)) and tyrosine residue (Tyr(102)) in the acyl pocket
> of Sirt5.

The horse sequence comparison is in [SIRT5-bioinformatics/RESULTS.md](SIRT5-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## Horse-specific research access

A horse-specific Falcon/Edison investigation was requested because PMID:36361948 studies equine chondrocytes and reports SIRT5-expression changes. Edison rejected task creation with HTTP429; the configured Perplexity fallback returned HTTP401 insufficient quota. No horse provider report was generated. Expression-level evidence does not resolve the divergent F6S899 protein model or validate catalytic activity.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined the single GOA row (GO:0070403 NAD+ binding, IEA, InterPro IPR003000), the description and
core functions. ProtNLM2 files were not opened.

### Identity of F6S899: a defective gene model of horse SIRT5

New analysis: `SIRT5-bioinformatics/compare_gene_models_rereview.py` -> `RESULTS-rereview.md` /
`results-rereview.json` (live UniProt, Ensembl REST and QuickGO; the original `RESULTS.md` is untouched).

- Horse gene ENSECAG00000026898 has several protein-coding transcripts. F6S899 = ENSECAT00000028843 (282 aa).
  Full-length alternatives: A0A9L0T9B1 = ENSECAT00000146678 (310 aa, 88.1% identical to human Q9NXA8 over its whole
  length) and A0A9L0T6A9 = ENSECAT00000079525 (318 aa, the Ensembl canonical transcript, alternative C-terminal exon).
- F6S899 matches human SIRT5 window by window through human residue ~200 (identical to the other horse models), then
  collapses (10/30 and 7/40 identical in human windows 201-250 and 251-300).
- Cause: the F6S899 transcript omits the internal exon 13742662-13742785 (124 nt, 124 mod 3 = 1) present in both
  full-length transcripts, so everything downstream is translated in the wrong frame. Its last two "exons" are
  separated by a 3-nt gap (13757851-13757853), another sign of a computational model rather than a real splice form.
- Consequence for mapped human features: retained His158 (catalytic base), NAD loop 58-77, Tyr102/Arg105 acyl pocket,
  QNID 140-143, Cys166/Cys169; lost Cys207/Cys212 (zinc; W/W), GTS 249-251, NTE 275-277, Cys293. The full-length horse
  models keep all of these (A0A9L0T9B1 has NME for NTE, as many mammals).
- UniProt CAUTION on F6S899 ("Lacks conserved residue(s) required for the propagation of feature annotation",
  PROSITE PRU00236) and the failure of HAMAP MF_03160 to match F6S899 (it matches A0A9L0T9B1) are consistent with this.

### Evolutionary grounding

- PANTHER: F6S899 and A0A9L0T9B1 are both PTHR11085:SF10 (SIRT5 subfamily). The family review
  `interpro/panther/PTHR11085/PTHR11085-review.yaml` lists F6S899 and human Q9NXA8 as SF10 representatives; no
  disagreement about subfamily placement. (The family review says "no catalytic-residue loss is inferred from a short or
  incomplete input sequence"; this re-review identifies the cause of the incompleteness as a gene-model defect.)
- PAINT: node PTN000119399 (IBD seeds MGI:1915596 Sirt5 and UniProtKB:Q9NXA8) carries GO:0036054, GO:0036055,
  GO:0061697, GO:0005739, GO:0005829; PTN000872307 carries GO:0005759. QuickGO shows these IBAs on A0A9L0T9B1, not on
  F6S899. That is PAINT's one-representative-per-gene propagation, not a functional judgment against the gene; but it
  means the curated record for this gene's functions is A0A9L0T9B1.

### Decisions

- GO:0070403 NAD+ binding: UNDECIDED -> KEEP_AS_NON_CORE. True of the horse SIRT5 gene product (NAD+ is the
  co-substrate), domain-signature based; not the core activity. Whether the truncated F6S899 translation binds NAD is
  not established, stated in the reason.
- core_functions: added desuccinylase (core), demalonylase and deglutarylase activities in mitochondrial matrix, scoped
  to the gene and grounded in the SF10/PTN000119399 placement plus the mammalian primary literature
  [PMID:22076378 "is an efficient protein lysine desuccinylase and demalonylase in vitro"]
  [PMID:24703693 "We then showed that SIRT5 catalyzes lysine deglutarylation both in vitro and in vivo."].
  No NEW existing_annotations rows were added to F6S899 itself, because its own translation lacks the second zinc
  pair; the right anchor for those terms is a full-length product (A0A9L0T9B1 already carries them by IBA).
- Description rewritten as a project-independent summary that also records the gene-model defect.

### Relative to review next

Benchmark accession is an alternative/defective gene model; no reviewed (Swiss-Prot) horse SIRT5 exists, and no repo
review exists for the full-length horse product. Relative: A0A9L0T9B1 (same gene, full-length 310-aa product that
carries the PAINT IBAs) -> folder `genes/HORSE/SIRT5__A0A9L0T9B1`. Human SIRT5 (Q9NXA8) already has a review
(`genes/human/SIRT5/SIRT5-ai-review.yaml`, all 68 rows actioned, core functions present).

Modules: no module in `modules/` includes SIRT5 (grep for SIRT5/Q9NXA8 found none; desuccinylase hits are bacterial
succinylarginine/lysine-biosynthesis modules, unrelated).
