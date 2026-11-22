---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/GYG1
affinage_run_date: 2026-06-10T01:55:21
uniprot_accession: P46976
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for GYG1 (human)

## Current model (mechanistic narrative)

GYG1 encodes glycogenin-1, the auto-glucosylating priming enzyme required for glycogen synthesis, whose loss disrupts glycogen homeostasis across multiple tissues [PMID:29143313, PMID:29264399]. Disease-associated variants—including a substrate-binding-domain missense mutation (p.Gly135Arg), additional missense (p.Asp102His), frameshift, splice-acceptor, and deep intronic variants—abolish or reduce glycogenin-1 expression and eliminate autoglucosylation activity, as established directly by in vitro autoglucosylation assays and patient-muscle protein analysis [PMID:29143313, PMID:31791869, PMID:29264399]. Splice-disrupting alleles act through exon 2 skipping and cryptic exon activation, producing aberrant transcripts that can occur in trans as compound heterozygous lesions [PMID:42023422]. Enzymatic failure leads to accumulation of polyglucosan storage material in skeletal muscle fibers and cardiomyocytes [PMID:31791869, PMID:42165248]. In GYG1 cardiomyopathy (GSD15), this storage material sequesters glycogen-metabolism enzymes (glycogen synthase, UDP-glucose pyrophosphorylase 2, glycogenin-1, glycogen phosphorylase, debranching enzyme) along with p62 and desmin, accompanied by downregulation of mitochondrial proteins indicating impaired energy metabolism, without increased autophagy [PMID:42165248]. Beyond its role in storage disease, glycogenin-1-dependent glycogen supports inflammatory activation of myeloid cells: in vivo Gyg1 knockdown lowers myeloid glycogen, attenuates IL-6 and TNF-α production and neutrophilia, and improves survival in LPS-induced sepsis [PMID:41333476].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016740 transferase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2017 | Medium | A novel GYG1 missense mutation (c.403G>A; p.Gly135Arg) located in the substrate binding domain abolishes the enzymatic autoglucosylation function of glycogenin-1, as demonstrated by an in vitro autoglucosylation assay. The mutation also caused reduced expression of glycogenin-1 protein. | PMID:29143313 | Acta neurologica Scandinavica |
| 2019 | Medium | Loss-of-function variants in GYG1 (including splice acceptor, frameshift, and missense variants) result in either total absence or reduced expression of glycogenin-1 protein, and residual mutant protein (p.Asp102His) is non-functional, leading to glycogen and polyglucosan storage in skeletal muscle fibers. | PMID:31791869 | Neuromuscular disorders : NMD |
| 2017 | Medium | GYG1 mutations causing loss or reduction of glycogenin-1 expression result in impaired glucosylation activity, as shown by protein analysis of patient muscle biopsies revealing either absence of glycogenin-1 or reduced expression with impaired glucosylation. | PMID:29264399 | Neurology. Genetics |
| 2026 | Medium | In GSD15 (GYG1 cardiomyopathy), storage material in cardiomyocytes is enriched in proteins involved in glycogen metabolism (glycogen synthase, UDP-glucose pyrophosphorylase 2, glycogenin-1, glycogen phosphorylase, glycogen debranching enzyme), as well as sequestosome 1 (p62) and desmin, without evidence of increased autophagocytosis. Whole-tissue proteomics revealed upregulation of cardiomyopathy biomarkers and downregulation of mitochondrial proteins, indicating impaired energy metabolism. | PMID:42165248 | The Journal of clinical endocrinology and metabolism |
| 2025 | Medium | In vivo knockdown of Gyg1 via LNP-mediated siRNA delivery in an LPS-induced sepsis mouse model significantly reduced glycogen content in myeloid cells, attenuated IL-6 and TNF-α production, alleviated LPS-induced neutrophilia, and modestly decreased CD40 expression in monocytes and dendritic cells, improving survival. | PMID:41333476 | Frontiers in immunology |
| 2026 | Medium | RNA sequencing of patient muscle confirmed that the GYG1 splice-site variant c.143+3G>C causes exon 2 skipping, and the deep intronic variant c.7+992T>G activates a cryptic exon insertion, both leading to aberrant GYG1 transcripts. Long-read genome sequencing established that these two variants are in trans (compound heterozygous). | PMID:42023422 | Clinical genetics |

## Citations

- PMID:29143313
- PMID:29264399
- PMID:31791869
- PMID:41333476
- PMID:42023422
- PMID:42165248
