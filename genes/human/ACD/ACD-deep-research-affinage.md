---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACD
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q96AP0
self_evaluation_pairwise: win
faith_pct: 85.71428571428571
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACD (human)

## Current model (mechanistic narrative)

ACD (TPP1) is a shelterin-complex scaffold protein that protects chromosome ends and licenses telomere elongation, and its loss couples telomere dysfunction to p53-dependent apoptosis during development and stem-cell maintenance [PMID:15181449, PMID:19660449]. It physically bridges TIN2 and POT1, with the POT1 interaction occurring through the POT1 C-terminus; disrupting this bridge prevents POT1 from localizing to telomeres and deregulates telomere length [PMID:15181449]. A distinct surface, the TEL patch, is required to recruit telomerase to telomeres: a single-amino-acid deletion (ΔK170) leaves telomeric localization intact but abolishes telomerase recruitment, causing telomere shortening and bone marrow failure in an affected family [PMID:25205116]. Loss of functional ACD in vivo produces chromosomal fusions both with and without internal telomeric sequence, indicating telomere-protective and broader genome-stability roles [PMID:18185984]. ACD-mediated telomere dysfunction acts upstream of p53: caudal truncation, limb hypoplasia, and vertebral anomalies in acd-mutant mice are rescued on a p53-null background, whereas hematopoietic stem cells are acutely depleted upon Acd inactivation in a p53-target-driven, cell-type-specific manner not rescued by p53 loss [PMID:19660449, PMID:24316971]. Cells maintain a single functional copy of ACD by post-transcriptionally restoring TPP1 protein to normal levels despite reduced mRNA [PMID:33446513]. In human disease, separation-of-function and loss-of-function ACD variants cause bone marrow failure and aplastic anemia [PMID:25205116], and TPP1-destabilizing missense variants reduce DKC1 expression and shorten telomeres in idiopathic pulmonary fibrosis [PMID:41822348].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-5357801 Programmed Cell Death
- **partners:** POT1, TIN2
- **complexes:** shelterin

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | PTOP (ACD/TPP1) physically interacts with both POT1 (via the C-terminus of POT1) and TIN2, forming a bridge that recruits POT1 to telomeres. RNAi-mediated knockdown of PTOP or disruption of the PTOP-POT1 interaction hindered POT1 localization to telomeres and extended telomere length. | PMID:15181449 | Nature cell biology |
| 2004 | High | A splice donor mutation in the mouse Acd gene (encoding the TPP1 ortholog) causes the adrenocortical dysplasia phenotype. Wild-type Acd transgene expression rescues the phenotype, establishing Acd as required for urogenital ridge differentiation, axial skeleton specification, and limb patterning. Reduced Wnt3a and Dll1 expression in the tail bud correlates with caudal regression severity. | PMID:15537664 | Human molecular genetics |
| 2008 | High | Cells from homozygous acd mice (lacking functional Tpp1/Acd) harbor chromosomal fusions at telomere sequences as well as fusions lacking internal telomere sequences, demonstrating that Tpp1/Acd plays a vital role in telomere protection in vivo and likely has additional genome-stability functions beyond simple telomere capping. | PMID:18185984 | Chromosome research |
| 2009 | High | Caudal truncation in acd mutant mice is caused by p53-dependent apoptosis, not altered proliferation. Genetic rescue by p53 null background rescues limb hypoplasia and vertebral anomalies in acd mutants, placing Acd/TPP1-mediated telomere dysfunction upstream of p53-dependent apoptosis in developmental patterning. | PMID:19660449 | Developmental biology |
| 2013 | High | Mouse hematopoietic stem cells (HSCs) are acutely sensitive to Acd/TPP1 inactivation. Complete Acd inactivation causes p53 target gene expression, cell cycle arrest, and rapid HSC depletion leading to hematopoietic failure. Unlike in epidermal stem cells, p53 deficiency did not rescue TPP1-deficient HSCs, indicating cell-type-specific shelterin functions. | PMID:24316971 | The Journal of clinical investigation |
| 2014 | High | A 1-amino-acid deletion in the TEL patch of TPP1 (ΔK170, encoded by ACD) fails to recruit telomerase to telomeres when introduced into 293T cells, causing telomere shortening and segregating with aplastic anemia and bone marrow failure in a human family. TPP1 ΔK170 localizes normally to telomeres but is specifically defective in telomerase recruitment. | PMID:25205116 | Blood |
| 2011 | Medium | TAp63 deficiency does not rescue acd skeletal phenotypes; instead, double acd/TAp63-heterozygous embryos show more severe limb and vertebral anomalies than acd alone, indicating TAp63 isoforms do not mediate p53-like apoptosis in response to Acd-mediated telomere dysfunction and may have a stabilizing role. | PMID:22038471 | Mammalian genome |
| 2015 | Medium | A somatic ACD missense mutation (p.G223V) identified in childhood acute lymphoblastic leukemia confers protection against apoptosis and leads to increased telomere length in leukemia cells expressing this variant, implying a gain-of-function effect on telomere maintenance. | PMID:26345285 | BMC cancer |
| 2018 | Medium | Silencing ACD/TPP1 by siRNA in glioblastoma cells enhances radiation sensitivity, decreases telomerase activity, reduces cyclin D1 and BIRC1 expression, and upregulates caspase-3, placing ACD upstream of telomerase activity and anti-apoptotic pathways in radioresistance. | PMID:30080989 | Translational research |
| 2021 | Medium | Heterozygous loss-of-function ACD variants (frameshift or chromosomal deletion) reduce nascent ACD RNA and mRNA but result in normal steady-state TPP1 protein levels in lymphoblastoid cell lines, indicating cells compensate for loss of one ACD allele by a post-transcriptional mechanism to maintain TPP1 protein levels and normal telomere length. | PMID:33446513 | Cold Spring Harbor molecular case studies |
| 2026 | Medium | Two novel ACD missense mutations (p.S295N and p.H358Q) identified in Chinese IPF patients compromise TPP1 protein stability and reduce TPP1 expression, which in turn decreases DKC1 expression and results in telomere shortening, linking ACD/TPP1 function to the DKC1-telomerase axis. | PMID:41822348 | Frontiers in cell and developmental biology |
| 2014 | Low | Four of five distinct ACD germline mutations identified in familial melanoma cluster in the POT1-binding domain of TPP1 (including a nonsense mutation p.Q320X), statistically enriched compared to population controls, demonstrating that disruption of the ACD–POT1 interaction interface is a recurrent mechanism in melanoma susceptibility. | PMID:25505254 | Journal of the National Cancer Institute |

## Citations

- PMID:15181449
- PMID:15537664
- PMID:18185984
- PMID:19660449
- PMID:22038471
- PMID:24316971
- PMID:25205116
- PMID:25505254
- PMID:26345285
- PMID:30080989
- PMID:33446513
- PMID:41822348
