# clec-67 (F56D6.2; UniProtKB Q8ITX4) - manual literature research

Deep-research API providers were not available for this session; this file records a manual
literature survey (PubMed query `clec-67 OR F56D6.2 elegans`, 6 hits, all cached in
`publications/`) plus the cached UniProt record.

## Identity and domain architecture

- Unreviewed TrEMBL entry Q8ITX4, 467 aa, WormBase F56D6.2 / WBGene00018971, chromosome IV.
  [UniProt:Q8ITX4 "C-type lectin domain-containing protein"]
- Predicted signal peptide 1..17 (SignalP), no transmembrane segment annotated, so a secreted
  protein is predicted. [UniProt:Q8ITX4 "SIGNAL          1..17"]
- One C-type lectin-like domain (PROSITE PS50041, residues 27..144), plus Pfam PF23673 (DUF7154);
  PANTHER PTHR23062 ("HYPOTHETICAL PROTEIN C.ELEGANS"), a nematode-expanded family.
- UniProt CAUTION: "Lacks conserved residue(s) required for the propagation of feature
  annotation" (PROSITE-ProRule PRU00040). Our own inspection
  (`clec-67-bioinformatics/RESULTS.md`) finds 3 rather than 4 CTLD cysteines and none of the
  EPN / QPD / WND carbohydrate-recognition motifs.

## Literature

1. **Kerry et al. 2006, PLoS One (PMID:17183709)** - the founding paper for clec-67 as an immune
   marker. clec-67 is consistently induced by *Salmonella enterica*, is expressed in the
   intestine (Pclec-67::gfp), has a GATA site in its promoter, and its expression falls when the
   intestinal GATA factor ELT-2 is knocked down by RNAi
   [PMID:17183709 "when elt-2 expression is ablated by RNAi, clec-67 is downregulated compared to vector control, indicating that ELT-2 regulates the expression of this effector of C. elegans immunity to S. enterica"].
   No loss-of-function analysis of clec-67 itself is reported; it is used as a reporter.
2. **White & Herman 2018, Front Cell Infect Microbiol (PMID:30177956)** - clec-67 is a hub gene in
   the transcriptional network induced by *Stenotrophomonas maltophilia*; the clec-67(ok2770)
   deletion mutant is hyper-susceptible to the virulent JCMS strain but not to the avirulent K279a
   strain [PMID:30177956 "Mutations in cpr-4, mpk-2, lys-6, clec-67, and C48B4.1 caused hyper-susceptibility to JCMS but did not have a statistically significant survival phenotype on K279a"].
   This is the only loss-of-function evidence for the gene; the mechanism is not addressed.
3. **Kimura et al. 2012, Radiat Res (PMID:22967128; abstract only)** - ionizing radiation induces
   intestinal innate-immune genes including clec-67.
4. **Liu et al. 2013, Appl Environ Microbiol (PMID:24056462; abstract only)** - a red-seaweed
   extract induces F56D6.2 among other immune genes.
5. **Balamurugan 2026, Dev Comp Immunol (PMID:42263922; abstract only)** - *S. Typhi* metabolites
   up-regulate tol-1, clec-67 and skn-1.
6. **Zheng et al. 2026, J Adv Res (PMID:42142804; abstract only)** - clec-67 mentioned among
   immune genes in a cadmium/gut-microbiota study.
7. **Shen et al. 2005, PLoS Genet (PMID:16184190)** - genome-wide UPR microarrays. clec-67 is not
   named in the main text; WormBase's HEP annotation to PERK-mediated UPR presumably derives from
   the supplementary table of pek-1-dependent i-UPR genes
   [PMID:16184190 "approximately 23% (47 out of 202) of i-UPR genes require pek-1 for maximal induction (see Figure 3A; Table S2)."].
   The supplementary tables are not in the cache.

## Synthesis

clec-67 encodes a secreted, intestinally expressed CTLD protein whose transcription is a robust
marker of the intestinal response to bacterial pathogens (and other stresses), driven at least
in part by ELT-2. A deletion mutant is more susceptible to virulent *S. maltophilia*. No
biochemical activity has been demonstrated; the CTLD is non-canonical, so carbohydrate binding is
an untested hypothesis. There is no evidence for chaperone activity or for direct participation
in the UPR beyond being a transcriptional target.
