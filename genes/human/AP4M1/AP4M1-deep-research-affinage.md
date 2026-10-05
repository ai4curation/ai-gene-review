---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP4M1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: O00189
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP4M1 (human)

## Current model (mechanistic narrative)

AP4M1 encodes the mu (medium) subunit of a non-clathrin membrane coat adaptor complex, identified by homology to the medium chains of clathrin coat adaptors [PMID:9013859]. In neurons it functions in intracellular trafficking required for dendritic compartmentalization: loss-of-function mutation produces aberrant localization of the GluRdelta2 glutamate receptor, abnormal dendritic spine morphology, and neuroaxonal degeneration [PMID:19559397]. Biallelic loss-of-function variants abolish AP-4 complex function in patient-derived fibroblasts and cause the SPG50 form of hereditary spastic paraplegia [PMID:34087981]. AAV-mediated delivery of AP4M1 restores AP-4 function in patient fibroblasts and achieves functional rescue in Ap4m1-knockout mice, establishing that AP4M1 is an essential, dose-limiting subunit of the complex [PMID:36951961]. Beyond its role as an AP-4 subunit and its neuronal trafficking function, the molecular cargo-recognition mechanism of AP4M1 has not been further characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** *(none)*
- **complexes:** AP-4 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | Medium | AP4M1 (mu-ARP2) was identified as a novel mu-adaptin-related protein homologous to the medium chains of clathrin coat adaptor complexes, sharing 60% identity with mu-ARP1 and 27-31% identity with mu1/mu2-adaptins, suggesting it is a subunit of an uncharacterized non-clathrin protein coat involved in cellular membrane traffic. | PMID:9013859 | FEBS letters |
| 2009 | Medium | Loss-of-function mutation in AP4M1 (splice site mutation c.1137+1G>T in intron 14) causes neuroaxonal degeneration with aberrant GluRdelta2 glutamate receptor localization and abnormal dendritic spine morphology, establishing AP4M1's role in intracellular trafficking of glutamate receptors in neurons. | PMID:19559397 | American journal of human genetics |
| 2014 | Low | AP4M1 protein is normally distributed in the dendrites of hippocampal neurons; following oxygen-glucose deprivation, AP4M1 is downregulated at both mRNA and protein levels and redistributes from dendrites to axons, indicating a role in dendritic compartmentalization that is disrupted by ischemic injury. | PMID:24486887 | Neuroscience letters |
| 2021 | Low | Biallelic loss-of-function variants in AP4M1 (the mu subunit of adaptor protein complex 4) lead to loss of AP-4 complex function, as confirmed by functional studies in patient-derived fibroblasts from SPG50 patients. | PMID:34087981 | Stem cell research |
| 2023 | High | Transduction of SPG50 patient-derived fibroblasts with AAV2/AP4M1 rescues the AP-4 deficiency phenotype in vitro, and intrathecal delivery of AAV9/AP4M1 in Ap4m1-KO mice achieves dose- and age-dependent functional rescue, establishing that AP4M1 restoration is sufficient to correct AP-4 complex dysfunction. | PMID:36951961 | The Journal of clinical investigation |
| 2020 | Low | Functional studies in patient-derived fibroblasts with a loss-of-function AP4M1 splice variant (c.59-1G>C) confirmed loss of adaptor protein complex 4 function, supporting AP4M1 as an essential subunit of the AP-4 complex. | PMID:33553621 | Neurology. Genetics |

## Citations

- PMID:19559397
- PMID:24486887
- PMID:33553621
- PMID:34087981
- PMID:36951961
- PMID:9013859
