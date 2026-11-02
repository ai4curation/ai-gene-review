---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATAD3C
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T2N8
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 4
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATAD3C (human)

## Current model (mechanistic narrative)

ATAD3C is an integral mitochondrial inner membrane protein that exposes its carboxy-terminus to the intermembrane space and functions as a dominant-negative regulator of the ATAD3A oligomeric complex, thereby modulating mitochondrial oxidative phosphorylation [PMID:38092275]. ATAD3C monomers incorporate into ATAD3A complexes and reduce their size, and its overexpression in fibroblasts lowers oxygen consumption, increases cellular ROS, and shifts respiratory chain organization toward dimeric Complex III at the expense of supercomplex assembly [PMID:38092275]. The locus is also a site of pathogenic genomic rearrangement: non-allelic homologous recombination and de novo duplications generate stable chimeric ATAD3A/ATAD3C fusion proteins that disrupt ATAD3 complex composition, reduce Complex I and its activity in patient tissue, and perturb mitochondrial DNA organization and cellular cholesterol homeostasis through dominant-negative mechanisms [PMID:32004445, PMID:33575671, PMID:28549128]. Beyond these complex-level and fusion-driven effects, no enzymatic activity or independent molecular function for ATAD3C itself has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** ATAD3A
- **complexes:** ATAD3A complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2023 | Medium | ATAD3C is an integral membrane protein that exposes its carboxy-terminus to the mitochondrial intermembrane space. Overexpression of ATAD3C (but not ATAD3A) in fibroblasts decreased cell proliferation and oxygen consumption rate and increased cellular ROS, due to incorporation of ATAD3C monomers into the ATAD3A complex in the mitochondrial membrane, reducing its size. ATAD3C expression also led to increased accumulation of respiratory chain dimeric Complex III in the inner membrane at the expense of its assembly into respiratory supercomplexes, demonstrating a dominant-negative role for ATAD3C in regulating ATAD3A function and mitochondrial OXPHOS. | PMID:38092275 | Free radical biology & medicine |
| 2020 | Medium | Heterozygous 67 kb duplications at the ATAD3 locus, mediated by non-allelic homologous recombination between ATAD3A exon 11 and ATAD3C exon 7, produce a chimeric ATAD3A/ATAD3C fusion gene. The fusion protein product is expressed and stable in patient fibroblasts, lacks key functional residues, and causes perturbed cholesterol and mitochondrial DNA organization similar to severe ATAD3A deficiency, consistent with a dominant-negative mechanism. | PMID:32004445 | American journal of human genetics |
| 2020 | Medium | De novo duplications in the ATAD3 locus produce chimeric ATAD3A/ATAD3C fusion proteins that alter ATAD3 complex composition and cause a striking reduction in mitochondrial Complex I and its activity in heart tissue, acting through a dominant-negative mechanism. | PMID:33575671 | Med (New York, N.Y.) |
| 2017 | Medium | Biallelic deletions generating chimeric ATAD3B/ATAD3A fusion genes (with genomic rearrangements affecting ATAD3C/ATAD3B on one allele) cause mitochondrial DNA abnormalities in patient fibroblasts, associated with altered cholesterol metabolism markers, establishing that the ATAD3 gene cluster including ATAD3C participates in the integration of mitochondrial DNA organization and cellular cholesterol homeostasis. | PMID:28549128 | Brain : a journal of neurology |

## Citations

- PMID:28549128
- PMID:32004445
- PMID:33575671
- PMID:38092275
