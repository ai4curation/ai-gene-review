---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD37
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q7Z713
self_evaluation_pairwise: 
faith_pct: 75.0
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

# Affinage mechanistic annotation for ANKRD37 (human)

## Current model (mechanistic narrative)

ANKRD37 is a hypoxia-responsive ankyrin-repeat protein that acts as a direct HIF-1 transcriptional target and contributes to the cellular response to low oxygen [PMID:19491311, PMID:32679233]. Its protein product carries ankyrin repeats and a nuclear localization signal, and nuclear translocation of ANKRD37 is required for its activity: in colon cancer cells, HIF-1α-driven ANKRD37 promotes hypoxia-induced autophagy and cell growth [PMID:32679233]. ANKRD37 binds Fem1b, facilitates Fem1b's cytoplasm-to-nucleus transport, and is itself targeted by Fem1b for ubiquitin-mediated degradation, placing it within a reciprocal regulatory partnership [PMID:21723927]. Beyond hypoxia, ANKRD37 restrains trophoblast migration and invasion through the NF-κB pathway, acting on p65 and IκBα phosphorylation [PMID:35218282], and its overexpression in mouse hippocampus reduces hippocampal volume via a causal chain originating from a methylation QTL [PMID:36195640].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-8953897 Cellular responses to stimuli, R-HSA-9612973 Autophagy
- **partners:** FEM1B
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | Medium | ANKRD37 is a direct transcriptional target of HIF-1 (Hypoxia-Inducible Factor-1). Experimental validation using an integrative genomics approach combining microarray data and promoter analysis for conserved HIF-1-binding sites confirmed ANKRD37 as a novel HIF-1 target gene. | PMID:19491311 | Nucleic Acids Research |
| 2011 | High | Ankrd37 protein contains ankyrin repeats and a putative nuclear localization signal (NLS), is present in the cytoplasm of elongating spermatids and later restricted to nuclei of spermatozoa during mouse spermatogenesis. Ankrd37 binds to Fem1b (feminization 1 homolog b) as shown by yeast two-hybrid screening and co-immunoprecipitation. Ankrd37 facilitates transport of Fem1b from cytoplasm to nucleus in co-transfected CHO cells. Fem1b targets Ankrd37 for ubiquitin-mediated degradation in a dose-dependent manner. | PMID:21723927 | Gene |
| 2020 | Medium | In colon cancer cells (RKO line), hypoxia-induced HIF-1α upregulates ANKRD37, and intranuclear ANKRD37 plays a required role in regulating hypoxia-induced autophagy and promoting cell growth. Translocation of ANKRD37 into the cell nucleus is necessary for these effects. | PMID:32679233 | Experimental Cell Research |
| 2022 | High | ANKRD37 overexpression in mouse hippocampus reduces hippocampal volume. A causal chain was established: rs1053218 SNP mutation causes cg26741686 hypermethylation, which leads to ANKRD37 overexpression, which reduces hippocampal volume. This was confirmed by CRISPR-based genome and epigenome editing of rs1053218 homologous alleles and cg26741686 methylation in mouse neural stem cell differentiation models, and by ANKRD37 overexpression in mouse hippocampus in vivo. | PMID:36195640 | Molecular Psychiatry |
| 2022 | Medium | ANKRD37 knockdown in trophoblast cell lines (HTR8/SVneo and JEG-3) enhances trophoblast migration and invasion and promotes extravillous explant outgrowth, while ANKRD37 overexpression has the opposite effects. RNA sequencing indicated NF-κB as a downstream pathway of ANKRD37, confirmed by changes in p-p65 and p-IκBα expression, suggesting ANKRD37 inhibits trophoblast migration/invasion via the NF-κB pathway. | PMID:35218282 | The Journal of Gene Medicine |
| 2017 | Low | ANKRD37 mRNA expression is regulated by iron status in intestinal (Caco-2) and liver (HepG2) cell lines; iron deficiency induces ANKRD37 mRNA, and iron supplementation (via ABS-derived iron or ferric ammonium citrate) reduces it. ANKRD37 functions as a marker gene for iron-deficiency anemia. | PMID:29110513 | Clinical and Applied Thrombosis/Hemostasis |

## Citations

- PMID:19491311
- PMID:21723927
- PMID:29110513
- PMID:32679233
- PMID:35218282
- PMID:36195640
