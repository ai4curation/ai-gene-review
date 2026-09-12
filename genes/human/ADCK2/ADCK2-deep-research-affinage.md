---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADCK2
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q7Z695
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADCK2 (human)

## Current model (mechanistic narrative)

ADCK2 is a mitochondrial aarF domain-containing kinase required for Coenzyme Q (CoQ) biosynthesis and its downstream support of fatty acid oxidation and skeletal muscle development [PMID:31480808, PMID:39354863]. Human haploinsufficiency and heterozygous knockout mice show decreased CoQ levels, impaired fatty acid oxidation, mitochondrial myopathy with skeletal muscle lipid droplets, and liver dysfunction, with the muscle phenotype originating in embryonic development; CoQ supplementation partially rescues these defects, establishing CoQ biosynthesis as the core function from which the metabolic and developmental phenotypes derive [PMID:31480808, PMID:39354863]. In cancer cells, ADCK2 depletion compromises mitochondrial integrity—triggering cytochrome C release, depolarization, ATP loss, and DNA damage—and inactivates Akt-mTOR signaling to suppress NSCLC growth in vivo, while ADCK2 also restrains cell migration through MYL6 in melanoma cells [PMID:35205819, PMID:36439873]. No structural model, direct kinase substrate, or biochemical mechanism linking ADCK2 to the CoQ pathway has been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** *(none)*
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | ADCK2 haploinsufficiency in humans and heterozygous Adck2 knockout mice causes impaired fatty acid oxidation, mitochondrial myopathy with lipid droplets in skeletal muscle, liver dysfunction, and significant decrease in Coenzyme Q (CoQ) biosynthesis; CoQ supplementation partially rescued the phenotype, establishing ADCK2's role in CoQ biosynthesis and organismal fatty acid metabolism. | PMID:31480808 | Journal of clinical medicine |
| 2022 | Medium | ADCK2 knockdown in melanoma cells enhances cell migration and promotes a dedifferentiated phenotype; this effect operates via MYL6, as knockdown of MYL6 in ADCK2-overexpressing cells abrogated the ADCK2 overexpression-mediated suppression of migration. | PMID:35205819 | Cancers |
| 2022 | Medium | ADCK2 depletion in NSCLC cells disrupts mitochondrial function (cytochrome C release, mitochondrial depolarization, DNA damage, ATP reduction) and inactivates Akt-mTOR signaling; ADCK2 knockout suppressed NSCLC xenograft growth in vivo. | PMID:36439873 | International journal of biological sciences |
| 2012 | Low | Depletion of ADCK2 by siRNA significantly decreases TNFα-induced nuclear accumulation of HIF-1α in osteosarcoma and prostate cancer cell lines, acting through a non-conventional RELB-dependent NFκB signaling pathway and regulation of superoxide activity. | PMID:22355351 | PloS one |
| 2024 | High | Adck2 heterozygous mice exhibit skeletal muscle defects from embryonic development (1102 deregulated genes, 7% smaller embryos, delayed development, decreased myogenic cell differentiation); prenatal and progressive postnatal CoQ10 supplementation mitigated embryonic defects and conferred protective effects on mitochondrial function and skeletal muscle structure. | PMID:39354863 | Journal of cachexia, sarcopenia and muscle |

## Citations

- PMID:22355351
- PMID:31480808
- PMID:35205819
- PMID:36439873
- PMID:39354863
