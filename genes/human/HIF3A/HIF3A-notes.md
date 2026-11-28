# HIF3A manual review notes

`just deep-research-perplexity-lite human HIF3A` could not run in this
environment because the Perplexity provider was unavailable (`Available:
claude_code` only; `agentapi` was not on `PATH`). I therefore used the cached
UniProt, GOA, Reactome and publication files rather than creating a fake
provider deep-research file.

HIF3A encodes a bHLH-PAS HIF alpha subunit with multiple functional isoforms.
The original human kidney report showed HIF-3alpha expression and found that
HIF-3alpha suppresses HIF-mediated hypoxia-inducible reporter expression
[PMID:11573933, "HIF-3alpha suppresses hypoxia-inducible HIF-mediated gene
expression"]. The human HIF-3alpha4 paper extended that inhibitory model by
showing a dominant-negative splice variant that reduces HIF-1 HRE binding and
HIF-1 transcriptional output [PMID:16126907, "HIF-3alpha4 suppresses the
transcriptional activity of HIF-1"].

The long HIF-3alpha2 isoform also has a direct activating role. Tolonen et al.
showed HIF-3alpha2 binding at HRE-containing EPO promoter-proximal chromatin by
ChIP and activation of luciferase reporters from that region with HIF-beta
[PMID:31768607, "Chromatin immunoprecipitation analyses showed that HIF-3alpha2
binding associated with canonical hypoxia response elements in the promoter
regions of EPO."].

The HPA-derived nucleoplasm/cytosol annotations were retained as non-core
locations, and the Reactome cytosol and nucleoplasm rows were treated as
oxygen-dependent HIF3A shuttling, hydroxylation, VHL binding, ubiquitination,
and degradation rather than as the chromatin-bound core transcription-factor
activity. UniProt's mitochondrion and nuclear-speck locations are similarity
calls from mouse Hif3a; without a human HIF3A assay or a sub-mitochondrial
assay, both were kept as possible non-core conserved pools.
