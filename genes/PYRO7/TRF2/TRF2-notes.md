# TRF2 (G4N2B2, MGG_04853) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review. ProtNLM2 predictions were not consulted.

### Deep research
`just deep-research-falcon PYRO7 TRF2 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" (HTTP 403) and the perplexity-lite fallback also
failed. No deep-research file exists; the review uses the primary paper and the UniProt record directly.

### Literature
- PMID:27902426 (Jacob et al. 2017, Microbiology) is the only paper on TRF2. Cached text is abstract-only
  (PMC5817273 has no PDF link for the cache). The abstract states that the PKS19 cluster "comprises two
  transcription factors MoC19TRF1 and MoC19TRF2, which were both found individually to act as negative
  regulators repressing gene expression of MoPKS19" [PMID:27902426].
- Full text read on PMC (not cached; not quoted in the review): Table 1 places MGG_04853 among ORFs flanking
  MoPKS19; deletion (ΔMoC19TRF2) increased MoPKS19 transcript by qRT-PCR under both high- and low-pyriculol
  conditions (Fig. 6b, Fig. S1); overexpression (MoEF1::C19TRF2) left MoPKS19 transcript "constant, at the
  most slightly decreased". Pyriculol/pyriculariol levels were NOT measured by HPLC in the TRF mutants, and
  DNA binding, localization and direct target binding were not tested. The UniProt FUNCTION line
  ("negatively regulates the expression of the gene cluster and the subsequent pyriculol and pyriculariol
  production") extrapolates beyond what was measured for metabolite output.
- Naming quirk: UniProt's RecName for TRF2 is "Pyriculol/pyriculariol biosynthesis cluster transcription
  factor 1", while the gene name is TRF2 (MoC19TRF2). The paper's TRF2 is MGG_04853 = this entry.
- Kim et al. 2009 (PMID:19997500, MoHOX1-8 deletion set) could not be mapped to MGG_04853 from the text I
  could read; no MoHOX phenotype is attributed to TRF2 here.

### Evolutionary placement (TRF2-bioinformatics/RESULTS.md)
- PANTHER PTHR24324:SF5; homeodomain 73-132 with WFQNRR (120-125) and canonical I47/Q50/N51/R53, so
  sequence-specific DNA binding is well grounded in sequence. C-terminal PF24818 (PH_TRF2_HOY1).
- 1:1 ortholog of N. crassa KAL-1 (Q7S7W0): shared HOGENOM CLU_023524_1_0_1, 67%/93% identity, only
  PF24818 protein in each proteome. OrthoDB 6159439at2759 is a broad eukaryote-level group (PHO2, HHEX also
  in it), so it is not discriminating.
- GOA has no IBA rows for TRF2 (P. oryzae is not a PANTHER reference proteome); the TreeGrafter rows
  (GO_REF:0000118) come from PTN004691474, i.e. the same PAINT annotations that give KAL-1 its IBAs.

### Decisions
- Activity: GO:0000981 and GO:0000978 accepted (homeodomain + subfamily). DNA binding / GO:0000977 refined
  to GO:0000978.
- Process: experimental evidence is for negative regulation of a cluster gene's transcription, so
  GO:0006355 / GO:0006357 are refined to GO:0000122 negative regulation of transcription by RNA polymerase II.
  Directness not shown; repressor MF (GO:0001227) not asserted because no binding and overexpression has
  little effect.
- No NEW secondary-metabolism term: pyriculol output was not measured in the TRF2 mutants. Left as a
  suggested experiment.
- cell differentiation (TreeGrafter): no TRF2 developmental phenotype has been reported (the virulence
  statement in the abstract concerns the pyriculol-null PKS19/OXR1 mutants, not clearly the TRF mutants).
  Marked over-annotated for this gene.
