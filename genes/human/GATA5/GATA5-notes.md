# GATA5 manual synthesis

Deep research with the configured Falcon provider and Perplexity-lite fallback failed in this checkout because the providers were unavailable to `deep-research-client`. This manual note summarizes the local cached sources used for the GATA5 review.

## PAINT and family context

GATA5 is Q9BWX5, `PTHR10071:SF289`. The PANTHER release 19.0 tree places human GATA5 at leaf `PTN002467693`. This leaf descends from the root GATA node `PTN001600628`, which carries IBD assertions for nucleus, RNA polymerase II-specific DNA-binding transcription factor activity, Pol II cis-regulatory region sequence-specific DNA binding, and positive and negative regulation of Pol II transcription. It also descends from `PTN000800998`, the Eumetazoa node with cell-fate commitment, and from `PTN002560190`, the GATA5-subfamily node with cardiac muscle tissue development. `just paint-losses human GATA5` reported no IRD or IKR on this lineage.

The single PAINT loss in the local slice, `PTN002467701` NOT cardiac muscle tissue development, sits on a sauropsid GATA5 branch under `PTN002560190` and outside the human GATA5 lineage. Human GATA5 therefore inherits the GATA5-subfamily cardiac-development IBA.

The other subfamily-specific PAINT rows on reviewed human paralogs are separated cleanly: GATA6 inherits epithelial cell differentiation from `PTN002560167`, GATA3 inherits immune/T cell/embryonic-organ terms from `PTN002560228`, and GATA2 inherits positive regulation of angiogenesis plus positive regulation of pri-miRNA transcription by RNA polymerase II from `PTN002560234`.

## Cached literature

### PMID:14986113

Ren et al. tested human GATA5 in COS-7 and 293T cells and found that GATA5 increased endogenous MUC2, MUC3, MUC4 and PGA transcripts and activated MUC2, MUC4 and PGA promoter reporters. Deleting the GATA5 zinc-finger domain, or the zinc-finger plus adjacent basic domain, strongly reduced reporter activation. This supports DNA-binding Pol II transcription-factor activity and positive regulation of Pol II transcription for human GATA5.

### PMID:9566909

Gao et al. tested Xenopus GATA-4/5/6 on the Xenopus IFABP promoter and found that the factors activated a defined proximal IFABP promoter element. The same study mapped chick GATA4/5/6 expression along the villus axis and reported that human HT-29 cells induce hGATA5 transcript early after sodium butyrate-induced differentiation, before intestinal alkaline phosphatase rises. This supports a conserved intestinal epithelial differentiation role, but the human part is expression timing, not a human GATA5 promoter perturbation.

### PMID:22641149 and PMID:24638895

Padang et al. is abstract-only locally. It reports rare nonsynonymous GATA5 variants in bicuspid aortic valve patients and identifies several variants in conserved activation-domain residues. The cached abstract does not describe a direct functional assay, so it is supportive genetic context rather than a mechanistic aortic-valve experiment.

Shi et al. is also abstract-only locally, but its abstract reports two heterozygous familial BAV mutations absent from control chromosomes and luciferase assays in which both GATA5 mutants had significantly reduced transcriptional activity. This supports a human loss-of-function valve-development context.

### PMID:28473536

Yin et al. assayed human transcription factor DNA-binding specificities by HT-SELEX and methyl-SELEX at scale. This supports sequence-specific double-stranded DNA binding by assayed human GATA5, but not endogenous chromatin occupancy or a specific process.

### PMID:32296183

Luck et al. generated the HuRI high-throughput binary protein-interaction map using repeated yeast two-hybrid screens and validation. The seven GATA5 IPI rows from this paper are retained as positive contact evidence but removed from GO because they assert only bare `GO:0005515` protein binding.

### Reactome:R-HSA-996755

The Reactome event models nucleoplasmic ZFPM/FOG binding to GATA proteins and states that all six GATA family members can interact with FOG-1 and FOG-2. This is useful nucleoplasmic cofactor context for GATA5, but it is a family model and not a GATA5-specific endogenous localization or coregulator-binding assay.
