---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASTE1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q2TB18
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for ASTE1 (human)

## Current model (mechanistic narrative)

ASTE1 is a structure-specific DNA endonuclease that operates as a downstream effector of the 53BP1-RIF1-shieldin pathway to enforce DNA double-strand break repair by non-homologous end-joining [PMID:34354233]. Purified ASTE1 specifically cleaves single-stranded DNA and 3' overhang DNA, and it is recruited to DNA damage sites in a shieldin-dependent manner, where it trims resected ssDNA ends to attenuate end resection [PMID:34354233]. Loss of ASTE1 impairs NHEJ, causes hyper-resection, disrupts immunoglobulin class switch recombination, and restores homologous recombination in BRCA1-deficient cells, conferring PARP inhibitor resistance [PMID:34354233]. ASTE1 also carries a coding microsatellite in its last exon that is a target of frameshift mutation in microsatellite-instability-high cancers; the resulting truncated proteins are degraded by the ubiquitin-proteasome system [PMID:23674496], and the frameshift neopeptides are presented on HLA-A0201 to elicit cytotoxic T lymphocyte responses against MSI+ tumor cells [PMID:15563124]. Beyond these findings, no further mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140097 catalytic activity, acting on DNA
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-73894 DNA Repair
- **partners:** SHLD2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | ASTE1 functions as a structure-specific DNA endonuclease that specifically cleaves single-stranded DNA and 3' overhang DNA. It acts as a downstream effector of the shieldin complex (53BP1-RIF1-shieldin pathway), localizing to DNA damage sites in a shieldin-dependent manner. Loss of ASTE1 impairs non-homologous end-joining (NHEJ), leads to hyper-resection, causes defective immunoglobulin class switch recombination, and restores homologous recombination in BRCA1-deficient cells, causing PARP inhibitor resistance. | PMID:34354233 | Nature cell biology |
| 2013 | Medium | ASTE1 (HT001) harbors coding microsatellite repeats in its last exon; frameshift mutations at this locus generate NMD-irrelevant mRNAs that are translated but the resulting truncated mutant proteins are degraded via the ubiquitin-proteasome pathway rather than accumulating in MSI-H cancer cells. | PMID:23674496 | Clinical cancer research |
| 2004 | Medium | Frameshift mutations in the HT001 (ASTE1) coding microsatellite generate immunogenic neopeptides (frameshift peptides, FSPs) that are presented on HLA-A0201 and can stimulate cytotoxic T lymphocyte (CTL) responses capable of lysing MSI+ colon carcinoma cells expressing the relevant HLA allele and mutation. | PMID:15563124 | Cancer immunity |
| 2013 | Low | The human ASTE1 gene genomically overlaps with the ATP2C1 gene (encoding SPCA1 calcium pump), a configuration unique to humans and not present in mice. This overlap was proposed (but not experimentally confirmed in this paper) to affect alternative splicing and protein expression of ATP2C1/SPCA1. | PMID:23344038 | International journal of molecular sciences |

## Citations

- PMID:15563124
- PMID:23344038
- PMID:23674496
- PMID:34354233
