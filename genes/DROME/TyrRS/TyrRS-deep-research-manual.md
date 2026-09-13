# TyrRS: manual functional synthesis

This synthesis was prepared from primary literature, the fly aaRS catalogue and downloaded gene/sequence records during the provider request. It is not a provider-generated report.

## Identity and core mechanism

FlyBase identifies a single 525-residue TyrRS-PA protein, Q9VV60 / FBpp0075168 / NP_648895. The aaRS catalogue identifies CG4561 as cytoplasmic TyrRS and distinguishes it from mitochondrial TyrRS-m (CG16912). The protein has the class-I synthetase and tRNA-recognition architecture. Its supported core activity is ATP-dependent charging of tRNA(Tyr) with tyrosine, through an aminoacyl-adenylate intermediate. [Lu et al., PMID:26761199](https://pubmed.ncbi.nlm.nih.gov/26761199/), DOI [10.1080/19336934.2015.1101196](https://doi.org/10.1080/19336934.2015.1101196).

The native fly gene and human neuropathy-related variants have been examined in a Drosophila disease model. Biochemical and genetic complementation showed that activity loss is not common to all disease variants; the pathology therefore cannot be reduced to defective aminoacylation. The cached abstract supports this distinction but does not justify new construct-specific claims. The existing curated catalytic annotation is retained. [Storkebaum et al., PMID:19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/), DOI [10.1073/pnas.0905339106](https://doi.org/10.1073/pnas.0905339106).

## Noncanonical predictions

ProtNLM predicts starvation response and resveratrol binding with rat Q4KM49 as donor. A primary mammalian study directly demonstrates resveratrol bound in the human TyrRS active site, stress-associated nuclear relocation, and TyrRS–PARP1 signaling. Its full text describes HeLa-cell serum-starvation responses and mouse experiments. This makes the donor-side biological interpretation substantial; it is not merely annotation repetition. [Sajish and Schimmel, PMID:25533949](https://pubmed.ncbi.nlm.nih.gov/25533949/), DOI [10.1038/nature14028](https://doi.org/10.1038/nature14028).

However, the exact native fly protein has no inspected ligand-bound structure, binding assay or demonstrated starvation-induced nuclear signaling mechanism. Conservation of tRNA charging does not automatically establish an additional ligand interaction or transcriptional stress pathway. The resveratrol prediction remains uncertain. The broad starvation-response prediction is supported by direct fly secretion evidence, described below; the particular mammalian nuclear mechanism remains unresolved. Resveratrol effects in a fly model expressing human mutant TyrRS would also require careful separation from evidence about native fly TyrRS.

## Ontology scope

The saved QuickGO response confirms that GO:1905594 is obsolete because resveratrol binding is not an evolved molecular function. This is a suitability judgment for GO, not experimental refutation of resveratrol binding. The released identifier and label are preserved for evaluation.

QuickGO also confirms that GO:0006437 is obsolete because the tyrosine-specific process duplicates the ligase molecular function. The native GOA rows retain their original IDs; replacement recommendations use GO:0006418 for the translation-related aminoacylation process, with GO:0004831 separately capturing substrate-specific activity.

## Remaining questions

The informative next evidence would measure ligand recognition and starvation-linked localization/signaling of native Q9VV60, with separation from its housekeeping aminoacylation function. No such measurement is inferred from existing electronic labels or the human disease-model literature.

## Native fly extracellular role

The completed Falcon report identified PMID:26658841. Direct reading of its publisher full text supports regulated TyrRS secretion, Mmp2-dependent processing and EMAP-mediated haemocyte recruitment. Figure 3 additionally establishes secretion following serum deprivation in fly S2 cells; this supplies direct fly support for a broad starvation-response annotation. Resveratrol recognition remains unresolved. Details and retained primary text are linked from the evidence notes.
