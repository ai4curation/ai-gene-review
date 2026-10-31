# HSF1 (human, Q00613) review notes

Deep research: not run. In this environment falcon times out and perplexity-lite is not installed. This review uses the
UniProt record and cached GOA-cited publications (abstracts and full text where available).

## Key points
- Master transcriptional activator of the heat shock response [file:human/HSF1/HSF1-uniprot.txt "plays a central role in the transcriptional activation of the heat shock response (HSR)"].
- The latent monomer is repressed by HSP90 [PMID:9727490 "Hsp90, by itself and/or associated with multichaperone complexes, is a major repressor of HSF1"] and by HSP70/DNAJB1 [PMID:9499401].
- Stress-induced trimerization gives HSE binding [PMID:7935471 "hHSF1 homotrimerizes and acquires heat shock element DNA-binding ability"].
- Activation domains contact TBP/TFIIB [PMID:11005381].
- Nuclear stress bodies [PMID:10359787].
- Non-canonical roles kept as non-core: IL1B/FOS repression [PMID:8926278; PMID:9341107], mitosis [PMID:18794143] and NHEJ inhibition [PMID:26359349].
- Chaperone-binding MF terms (HSP90/heat shock protein binding) are kept as non-core regulatory inputs. HSF1 is the client.
- The MAPK cascade, protein-containing complex assembly, heterodimerization and folding chaperone complex rows are marked over-annotated: HSF1 is the substrate or client there, not the executor.
- 51 protein binding IPI rows are removed as uninformative.
- Generic DNA binding (IDA x17 + IEA) is modified to GO:0000978.

## Module note
HSF1 is the stress-sensing transcriptional activator node of a heat shock response module. Its MF is GO:0001228 with GO:0000978. Chaperone-binding terms are inputs onto HSF1.
