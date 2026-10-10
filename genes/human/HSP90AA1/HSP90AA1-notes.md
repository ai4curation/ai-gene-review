# HSP90AA1 (human, P07900) review notes

Deep research: not run. In this environment falcon times out and perplexity-lite is not installed. This review uses the UniProt record and cached GOA-cited publications.

## Approach
522 GOA rows (about 120 distinct terms) were reviewed term by term, so every row for a term gets the same action.
- The core is ATP-dependent chaperone activity [file:human/HSP90AA1/HSP90AA1-uniprot.txt "Undergoes a functional cycle that is linked to its ATPase activity which is essential for its chaperone activity."].
- ATPase regulation by co-chaperones [PMID:29127155 "Tsc1 is a new co-chaperone for Hsp90 that inhibits its ATPase activity"; PMID:27353360].
- Kinase client maturation [PMID:27339980 "Hsp90 traps and stabilizes an unfolded kinase"].
- TPR co-chaperone binding through the C-terminus [PMID:9660753].
- Client/co-chaperone-specific roles kept as non-core: eNOS [PMID:9580552; PMID:11988487], telomerase, Tom70 mitochondrial import [PMID:12526792; PMID:15644312], TBK1/IRF3 antiviral signalling [PMID:20628368; PMID:25609812] and CMA [PMID:25719862].
- About 25 Ensembl/ARBA rodent physiology transfers (responses to cocaine, salt, estrogen and so on) and the minor-nucleotide binding terms are marked over-annotated.
- 195 protein binding IPI rows are removed as uninformative.
- The minor locations (exosome, sperm, melanosome, growth cones and so on) are kept as non-core.
