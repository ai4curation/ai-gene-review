# sta-1 (Q9NAD6) curation notes

## 2026-10-04 review session

Sources read: UniProt Q9NAD6, `sta-1-deep-research-openscientist.md` (retrieval only;
claims checked against primary papers below), cached publications.

- PMID:16401427 (Wang & Levy 2006, Curr Biol) - abstract only in cache.
- PMID:16873887 (Wang & Levy 2006, FASEB J) - abstract only in cache.
- PMID:28874466 (Tanguy et al. 2017, mBio) - full text cached.
- PMID:42427644 (Batachari et al. 2026, bioRxiv preprint) - full text cached; not peer reviewed.
- PMID:14704431 (Li et al. 2004 WI5 interactome) - source of the protein binding IPI.

### Identity and domains
- STAT family; coiled-coil, DNA-binding, linker, SH2; lacks N-terminal oligomerization domain
  [PMID:16873887 "STA-1 lacks the conserved amino-terminal oligomerization domain found in vertebrate and other invertebrate STAT proteins"].
- Recognises a conserved STAT cis element [PMID:16873887 "recognizing a cis DNA element conserved through phylogeny"].
- Paralog STA-2 lacks coiled-coil and tyrosine motif [PMID:28874466 "STA-2 is similar but lacks the coiled-coil domain as well as the tyrosine phosphorylation motif"].
  STA-2 epidermal AMP papers cited by the deep research are about the paralog and not used here.

### No JAK in C. elegans
- [PMID:28874466 "There is no conserved homolog of the JAK kinases in C. elegans; however, the canonical tyrosine phosphorylation site on STA-1 is conserved."]
- [PMID:28874466 "despite the absence of both interferon and JAK, the C. elegans STAT homolog STA-1 orchestrates antiviral immunity"]
- So GO:0007259 (JAK-STAT) IBA from PTN000927860 is lineage-inappropriate -> REMOVE, as for sta-2
  (projects/IBA_REVIEW.md section 14; projects/TAXON_PATHWAY_VARIANCE.md case study 1).

### Repressor of antiviral program (intestine)
- [PMID:28874466 "These data suggest that STA-1 largely acts as a transcriptional repressor of an antiviral gene expression program."]
- ChIP-seq [PMID:28874466 "STA-1 was enriched close to transcription start sites (TSS) of about 20% of all genes, with an enriched binding peak located ~200 bp upstream of their TSS"].
- Some activation possible [PMID:28874466 "Thus, although STA-1 largely acts as a constitutive repressor of gene expression, it may have a more complex role at the promoters of some genes."].
- Phenotype [PMID:28874466 "sta-1 mutants were 100-fold less permissive to infection than wild-type animals"].
- SID-3 genetically upstream [PMID:28874466 "genes upregulated in sid-3 mutants, including those shared with sta-1, were enriched for STA-1 binding by ChIP-seq, suggesting that sid-3 acts upstream of sta-1"].
- Preprint: cell-intrinsic, nuclear, relocalises [PMID:42427644 "STA-1 protein disappears from nuclei of cells infected with the natural viral pathogen, Orsay virus, but remains nuclear in uninfected cells"];
  DRH-1 [PMID:42427644 "During viral infection, STA-1 forms cytoplasmic puncta that interact with the RNA viral sensor DRH-1"];
  residues [PMID:42427644 "STA-1 overexpression causes increased susceptibility to viral infection, in a manner dependent on conserved residues important for DNA binding, nuclear localization and phosphorylation"].

### Dauer repression (neurons)
- [PMID:16401427 "the nematode STAT ortholog STA-1 accumulated in the nuclei of five head neuron pairs, three of which are amphid neurons involved in dauer formation"]
- [PMID:16401427 "sta-1 mutants showed a synthetic dauer phenotype with selected TGF-beta mutations"]
- [PMID:16401427 "STA-1 functioned in the absence of DAF-7, DAF-4, and DAF-14, but it required DAF-1 and DAF-8"]
- [PMID:16401427 "These results highlight a role for activated STAT proteins in repression of dauer formation"]
- Hence MODIFY GO:0040024 rows -> GO:0061067 negative regulation of dauer larval development.

### Decisions summary
- NEW GO:0001227 (repressor activity, Pol II) and GO:0000122 from PMID:28874466: STA-1 is the
  promoter-bound repressor itself (participation test passes; MF, not a comparator argument).
  This resolves the FUNCTION_UNREVIEWED warning for STA-1 in
  modules/c_elegans_jak_independent_stat_signaling.yaml.
- GO:0006952 defense response IBA -> MODIFY to GO:0050687 (sign inversion vs. activating seeds).
- GO:0042127 proliferation IBA -> MARK_AS_OVER_ANNOTATED (no evidence; not JAK-presupposing).
- GO:0045944 IDA (PMID:16873887, abstract only) kept as non-core; not removed.
- protein binding (Y2H) -> REMOVE per policy.
- GO ids checked via QuickGO: GO:0001227, GO:0000122, GO:0050687, GO:0061067 (all current).
- For the PTHR11801 family review: removed GO:0007259 IBA derives from PAINT node PTN000927860
  (paint.tsv row GO:0007259 IBD, seeds vertebrate STATs + fly Stat92E). The nematode branch needs
  an IRD / member exception, as for sta-2.
