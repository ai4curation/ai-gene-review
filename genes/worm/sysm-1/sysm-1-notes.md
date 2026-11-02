# sysm-1 (T24B8.5, Q22714) notes

Deep research: `just deep-research-falcon worm sysm-1 --fallback perplexity-lite` failed on 2026-10-08
(falcon timed out at 600 s; perplexity provider not available). No deep-research file was written.
The review is based on cached publications and PubMed searches.

## Key findings
- The gene was named systemic stress signaling mediator in 2022 [PMID:35121747 "we propose to name the T24B8.5 gene systemic stress signaling mediator (sysm-1)"].
- Secreted intestinal ShKT peptide required for IR-induced germ cell apoptosis [PMID:35121747 "These results indicate that (i) SYSM-1 is required, (ii) intestinal SYSM-1 is sufficient, and (iii) constitutive germline expression of SYSM-1 is sufficient for DNA damage-induced germ cell apoptosis"].
- Secretion depends on the signal sequence [PMID:35121747 "These results establish that SYSM-1 that is generated in the intestine is secreted into the germline through recognition of the signal sequence"].
- It acts independently of CEP-1 output [PMID:42173292 "Notably, the induction of the two proapoptotic BH3 domain-only genes, egl-1 and ced-13 remains intact in sysm-1 mutants, suggesting that SYSM-1 conveys stress signals across tissues, independent of CEP-1 transcriptional activity"].
- It is the standard PMK-1 reporter [PMID:20369020 "the promoter of a PMK-1-regulated gene, T24B8.5, encoding a ShK-like toxin peptide, fused to green fluorescent protein (GFP) and provides an in vivo sensor of PMK-1 pathway activity"].
- No antibacterial activity or infection phenotype has been reported. Single-gene RNAi of PMK-1 targets had no effect [PMID:17096597 "However, none of the genes inactivated individually by RNAi reproducibly resulted in an enhanced susceptibility to pathogens (unpublished data)."].

## Curation decisions
- The antibacterial innate immune response IEP is marked over-annotated; the innate immune response HEP and IBA rows are kept as non-core.
- NEW: GO:1902231 positive regulation of intrinsic apoptotic signaling pathway in response to DNA damage (IMP, PMID:35121747).
- For the PMK-1 immunity module: SYSM-1 is a sound pathway output (reporter), but its only demonstrated function is
  inter-tissue signaling for germline DNA-damage apoptosis, not antibacterial defense.
