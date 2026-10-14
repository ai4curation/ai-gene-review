---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WWX0
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB5 (human)

## Current model (mechanistic narrative)

ASB5 is an ankyrin-repeat and SOCS-box protein expressed in vascular and muscle lineages that functions within cardiovascular and muscle gene-regulatory programs. It is a direct transcriptional target of serum-response factor (SRF), with its cardiac expression dependent on SRF, placing it downstream in the SRF-driven cardiovascular network [PMID:15699019]. In zebrafish, the paralogs asb5a and asb5b act redundantly: simultaneous loss of both — but not either alone — causes pericardial enlargement, atrial dilation, and impaired contractile function with disrupted expression of cardiac-contraction hub genes [PMID:38003559], and disrupts left-right cardiac asymmetry through the Nodal-spaw-lefty pathway, with rescue requiring co-injection of both paralog mRNAs [PMID:40141403]. In mammals, ASB5 marks muscle satellite cells but is dispensable for skeletal muscle growth, satellite cell behavior, and regeneration; its germline knockout reduces muscle Tnfa expression [PMID:41549311]. Beyond its role as an SRF target and its zebrafish cardiac functions, no biochemical substrate or E3-ligase-adaptor mechanism for ASB5 has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1266738 Developmental Biology, R-HSA-74160 Gene expression (Transcription)
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | Low | ASB5 protein localizes in vivo to endothelial cells, smooth muscle cells of collateral arteries, and satellite cells, and is significantly upregulated at both mRNA and protein levels in growing collateral arteries following femoral artery occlusion, implicating it in the initiation of arteriogenesis. | PMID:12593841 | Biochemical and biophysical research communications |
| 2005 | Medium | ASB5 was identified as a direct transcriptional target of serum-response factor (SRF) via chromatin immunoprecipitation; its expression in cardiac cells is dependent on SRF, placing it downstream of SRF in the cardiovascular gene regulatory network. | PMID:15699019 | The Journal of biological chemistry |
| 2023 | Medium | In zebrafish, simultaneous knockout of both asb5a and asb5b (but not either alone) causes severe pericardial cavity enlargement, atrial dilation, and impaired cardiac contractile function; RNA-seq identified 11 cardiac-contraction-related hub genes with disrupted expression, with three regulatory modules potentially acting through calcium ion channels, demonstrating functional redundancy between the two paralogs. | PMID:38003559 | International journal of molecular sciences |
| 2025 | Medium | In zebrafish, combined deficiency of asb5a and asb5b disrupts left-right asymmetric heart development through the Nodal-spaw-lefty signaling pathway; lefty1 (midline barrier) is downregulated and spaw/lefty2 expression in the left lateral plate mesoderm is disordered. Rescue requires simultaneous injection of both asb5a-mRNA and asb5b-mRNA, confirming functional redundancy and a joint role in establishing cardiac L-R asymmetry. | PMID:40141403 | International journal of molecular sciences |
| 2026 | Medium | Germline CRISPR/Cas9 knockout of Asb5 in mice causes no defects in postnatal skeletal muscle growth, satellite cell proliferation, differentiation, or self-renewal, and does not impair muscle regeneration after acute injury; however, Asb5 KO reduces Tnfa (TNF-alpha) expression in skeletal muscle. ASB5 is confirmed as a specific marker of muscle satellite cells. | PMID:41549311 | Skeletal muscle |

## Citations

- PMID:12593841
- PMID:15699019
- PMID:38003559
- PMID:40141403
- PMID:41549311
