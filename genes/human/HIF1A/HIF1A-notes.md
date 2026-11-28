# HIF1A manual review notes

`just deep-research-perplexity-lite human HIF1A` could not run in this
environment because the Perplexity provider was unavailable (`Available:
claude_code` only; `agentapi` was not on `PATH`). I therefore used the cached
UniProt, GOA, Reactome and publication files rather than creating a fake
provider deep-research file.

HIF1A encodes HIF-1alpha, the oxygen-regulated bHLH-PAS alpha subunit of the
HIF-1 transcription factor. The cloning paper identified HIF1A and ARNT/HIF-1beta
as bHLH-PAS proteins that dimerize in the hypoxia-inducible HIF-1 complex
[PMID:7539918, "HIF-1 beta is a series of ARNT gene products, which can thus
heterodimerize with either HIF-1 alpha or AHR"]. Earlier EPO-enhancer work showed
that HIF-1 binding sites are required for hypoxic induction of Pol II reporter
transcription [PMID:8756616, "A HIF-1 binding site was demonstrated in the 47-bp
hypoxia response element"].

The core HIF1A function is nuclear HIF-1 transcriptional activation at
hypoxia-response elements, with p300/CBP coactivator recruitment. Kallio et al.
showed that activation includes HIF-1alpha nuclear import and CBP/p300
recruitment [PMID:9822602, "hypoxia-dependent nuclear import and activation
(derepression) of the transactivation domain"], and Reactome records HIF-alpha
translocation, ARNT heterodimerization, and CBP/p300 recruitment as nuclear
target-promoter events.

HIF1A protein abundance is also the substrate side of a conserved oxygen-sensing
turnover pathway. In oxygenated cells, prolyl hydroxylation enables pVHL
recognition and VCB/VHL-CUL2 ubiquitin-ligase recruitment
[PMID:12050673, "Capture of HIF-1 alpha by pVHL is regulated by hydroxylation of
specific prolyl residues"]. I treated those VHL, DCNL1 and CUL2/neddylation rows
as important non-core turnover regulation rather than as independent core
activities executed by HIF1A.

The very broad `GO:0005515` protein-binding rows mostly record useful HIF1A
regulatory contacts, including p300/CBP, FIH-1, RORalpha, HDAC4/5, PLK3, p53,
VHL and many ubiquitin-system regulators. They were removed only at the bare
protein-binding term under the project policy; where a specific GO molecular
function existed, I retained the interaction as coactivator binding, histone
deacetylase binding, nuclear receptor binding, protein kinase binding or
ubiquitin protein ligase binding.
