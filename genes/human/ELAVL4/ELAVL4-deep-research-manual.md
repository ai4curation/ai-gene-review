# Manual literature synthesis for human ELAVL4 (P26378)

## Provider status

The configured automated research command was attempted on 2026-07-18. Falcon failed with HTTP 402 Payment Required, and the Perplexity-lite fallback failed with HTTP 401 insufficient quota. This manual file is based on the reviewed UniProt record, all current GOA rows, the PTHR10352 PAINT record, cached PubMed/PMC primary sources, and targeted inspection of open full text.

## Functional synthesis

ELAVL4/HuD is a predominantly neuronal, three-RRM post-transcriptional regulator. Its best-established molecular activity is binding extended U-rich and AU-rich elements, especially in mRNA 3-prime UTRs. Structure and kinetics show that RRM1 and RRM2 recognize the AU-rich sequence while the three RRMs cooperate to form a stable complex [PMID:11175903, "These structures reveal a consensus RNA recognition sequence that suggests a preference for pyrimidine-rich sequences and a requirement for a central uracil residue"; PMID:10848602, "Thus, the three RRMs appear to cooperate not only to increase the affinity of the interaction but also to stabilize the formed complex."].

On target 3-prime UTRs, HuD commonly delays deadenylation and RNA decay. GAP43 is the clearest mechanistic example: HuD overexpression and recombinant HuD increase transcript half-life in a binding-element- and poly(A)-tail-dependent manner [PMID:12034726, "We conclude that HuD stabilizes the GAP-43 mRNA through a mechanism that is dependent on the length of the poly(A) tail and involves changes in its affinity for the mRNA."]. ACHE, NOVA1, APP, and BACE1 provide independent target examples. In human neuroblastoma cells, HuD also increases APP translation, showing that target stabilization can be coupled to greater polysome engagement [PMID:24857657, "In sum, HuD enhanced both the stability and translation of APP mRNA."].

HuD also has a distinct nuclear activity. Neuronal Hu proteins bind pyrimidine-rich CALCA intronic sequences and oppose TIA1/TIAL1 to select neuron-specific alternative processing [PMID:17035636, "We report here a novel function of these proteins as RNA processing regulators in the nucleus."]. This supports the specific process term regulation of alternative mRNA splicing, via spliceosome rather than only the broad RNA processing parent.

The direction of translation regulation depends on target context. In mouse pancreatic beta cells, HuD binds a conserved Ins2 5-prime-UTR element and represses translation; glucose triggers release of the mRNA [PMID:22387028, "Following treatment with glucose, HuD rapidly dissociated from Ins2 mRNA and enabled insulin biosynthesis."]. This animal evidence supports ISS transfer of mRNA 5-prime-UTR binding and negative regulation of translation to human ELAVL4, while direct human neuroblastoma experiments support positive regulation of translation.

HuD participates in neuronal mRNP transport. It binds SMN independently of RNA, and the SMN-HuD interaction helps recruit HuD and its target transcripts into neuronal RNA granules [PMID:21088113, "the interaction between HuD and SMN is required for proper recruitment of HuD and its mRNA targets in neuronal RNA granules"]. This provides mechanistic support for the PAINT protein-RNA adaptor activity assignment and for axonal/growth-cone localization. The generic ribonucleoprotein complex term remains biologically correct but does not specify a single constitutive complex.

## Biological boundary

Mouse and zebrafish loss-of-function studies support roles in neuronal differentiation, axon branching, dendrite formation, and motor function. These phenotypes are consistent with stabilization and transport of GAP43 and other neuronal transcripts, but they are not direct human experimental evidence. Likewise, the paraneoplastic Hu antigen identity is clinically important but does not itself define a separate molecular function.

CARM1 methylation of HuD modulates the balance between RNA binding and SMN interaction. Methylation-resistant HuD binds more CDKN1A/p21 RNA and promotes cell-cycle exit, whereas methylation favors SMN association [PMID:16508003, "Methylation-resistant HuD bound more p21cip1/waf1 mRNA than did the wild type"; PMID:21088113, "methylation of HuD by CARM1 reduces its interaction with the p21(cip1/waf1) mRNA"]. The isoform-specific impact of the hinge deletion present in isoforms 2-5 remains unresolved.

## Curation conclusion

The core annotation model contains three linked activities:

1. AU-rich 3-prime-UTR binding that protects selected mRNAs from deadenylation and decay and often enhances translation in neuronal cytoplasm and projections.
2. Pyrimidine-rich intronic RNA binding that regulates neuron-specific alternative pre-mRNA processing in the nucleus.
3. Protein-RNA adaptor activity that couples HuD-bound transcripts to neuronal mRNP machinery, including SMN-dependent granule localization.

The beta-cell 5-prime-UTR/translation-repression mechanism is a strong, conserved secondary function and is retained as an ISS-based new-term recommendation rather than generalized to all HuD targets.
