---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASNSD1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NWL6
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 7
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASNSD1 (human)

## Current model (mechanistic narrative)

The ASNSD1 locus is bicistronic, producing both a microprotein, ASDURF, from an upstream ORF in its 5' UTR and the downstream ASNSD1 protein from the main CDS [PMID:31738558, PMID:40058972]. ASDURF is the 12th subunit of the PAQosome, assembling via β-prefoldin structural homology with the five subunits of the prefoldin-like module to form a heterohexameric chaperone complex [PMID:31738558], and through this complex it promotes medulloblastoma cell survival in a manner associated with MYC-family oncogenes [PMID:38176414, PMID:37205492]. The downstream ASNSD1 protein supports skeletal muscle maintenance, as its inactivation in mice produces a progressive degenerative myopathy with sarcopenia and replacement of muscle by adipose tissue [PMID:32638637]. ASNSD1 (NS3TP1) also acts in hepatic stellate cells, where it engages TGFβ1/Smad3 and NF-κB signaling — Smad3 and p65 bind ASNSD1, p65 activates the ASNSD1 promoter, and ASNSD1 enhances TGFβ1 receptor I promoter activity — to promote stellate cell activation and hepatic fibrosis [PMID:37274069]. Despite the annotated asparagine synthetase domain implied by its name, no catalytic enzymatic activity for the ASNSD1 protein has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0044183 protein folding chaperone
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-392499 Metabolism of proteins
- **partners:** PFDN4, PFDN5, URI1, UXT, SMAD3, RELA
- **complexes:** PAQosome

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | ASDURF, encoded by an upstream open reading frame (uORF) in the 5' UTR of ASNSD1 mRNA, is the 12th subunit of the PAQosome chaperone complex. It displays structural homology to β-prefoldins and assembles with the five known subunits of the prefoldin-like module of the PAQosome to form a heterohexameric prefoldin-like complex. | PMID:31738558 | Journal of proteome research |
| 2024 | High | The ASNSD1-uORF microprotein (ASDURF) promotes medulloblastoma cell survival through engagement with the prefoldin-like chaperone complex, and its expression is associated with MYC-family oncogenes. | PMID:38176414, PMID:37205492 | Molecular cell |
| 2020 | Medium | Inactivation of ASNSD1 in mice causes a progressive degenerative myopathy with sarcopenia, myosteatosis, and extensive replacement of muscle by adipose tissue, establishing a functional role for ASNSD1 in skeletal muscle maintenance. | PMID:32638637 | Veterinary pathology |
| 2023 | Medium | NS3TP1/ASNSD1 promotes activation, proliferation, and differentiation of hepatic stellate cells (HSCs) and enhances hepatic fibrosis via the TGFβ1/Smad3 and NF-κB signaling pathways. Both Smad3 and p65 were shown to bind NS3TP1 by co-immunoprecipitation, and p65 increased NS3TP1 promoter activity while NS3TP1 increased TGFβ1 receptor I promoter activity. | PMID:37274069 | World journal of gastroenterology |
| 2023 | Low | Aspartate upregulates NS3TP1/ASNSD1 expression in vivo and in vitro, and NS3TP1 exerts an inhibitory effect on liver fibrosis by suppressing the NF-κB/NLRP3 signaling pathway. | PMID:36983568 | Journal of personalized medicine |
| 2023 | Low | ASDURF (the ASNSD1-uORF product) promotes hepatic fibrosis through TGFβ1/Smad3 and NF-κB signaling pathways and regulates the expression of the downstream ASNSD1 protein. Other PAQosome subunits (PFDN4, PFDN5, URI1, UXT) regulate cell proliferation through the PI3K/AKT pathway. | PMID:38016755 | Journal of gastroenterology and hepatology |
| 2025 | Low | The ASNSD1 mRNA gives rise to a bicistronic transcript in which both the upstream sORF (encoding ASDURF) and the downstream CDS (encoding ASNSD1 protein) are translated; the translation regulation of this unusual genetic arrangement was discussed in the context of functional genomics findings. | PMID:40058972 | Biochemistry. Biokhimiia |

## Citations

- PMID:31738558
- PMID:32638637
- PMID:36983568
- PMID:37205492
- PMID:37274069
- PMID:38016755
- PMID:38176414
- PMID:40058972
