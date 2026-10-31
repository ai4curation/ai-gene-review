# cep-290 (ccep-290, Y47G6A.17; UniProt A2A266) notes

Deep research: `just deep-research-falcon` timed out after 600 s, and the perplexity-lite fallback is not available in this environment. No deep-research file was produced. The review is based on cached full-text publications and PubMed.

Accession: `gene_exact:cep-290` finds nothing in UniProt. The current symbol in UniProt and WormBase is **ccep-290** (WormBase Y47G6A.17, WBGene00021643), and the only entry is TrEMBL A2A266 (1736 aa). The folder is named `cep-290` to match the module text.

## Key findings
- TZ protein, expressed only in ciliated neurons. It is needed for ciliary gate function and TZ ultrastructure [PMID:26982032 "Strikingly, however, cep-290 mutant cilia reveal no structures characteristic of the TZ, displaying a lack of Y-link axoneme-to-membrane attachments"].
- It is a core component of the central cylinder [PMID:26124290 "Based on protein localization and mutant phenotypes, CCEP-290 is an essential component of the central cylinder (this study)"].
- It acts downstream of MKS-5 and upstream of the MKS module [PMID:26982032 "Together, the data point to CEP-290 functioning downstream of MKS-5 and upstream of MKS module components."]. It is also needed at the TZ for TMEM-138 and CDKL-1.
- **Conflict:** Schouteden et al. report that CCEP-290 targets the TZ independently of MKS-5 [PMID:26124290 "CCEP-290 recruitment was unaffected in mutants of MKS-5, MKSR-2, and NPHP-4"]. Li et al. 2016 report that it depends on MKS-5. This is recorded as a DISPUTED finding.
- **PANTHER misassignment:** UniProt places A2A266 in PTHR43941 (SMC2). Because of that, five condensin/chromatin IBAs are wrong, and all five are REMOVEd. The CEP290 family is PTHR18879.
- **Wrong PMID:** the central cylinder IDA cites PMID:25961505, a CLK-1 mitochondrial paper with no cilium content (full text checked). The intended paper is PMID:26124290. This is recorded as reference_review WRONG_IDENTIFIER with a replacement.
- NEW GO:1905349 (ciliary transition zone assembly). CEP290-family orthologs carry this term by IBA (e.g. rat Cep290, checked in QuickGO). The worm protein misses it only because of the PANTHER misassignment.
