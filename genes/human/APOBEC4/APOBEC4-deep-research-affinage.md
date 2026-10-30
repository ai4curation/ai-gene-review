---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APOBEC4
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8WW27
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

# Affinage mechanistic annotation for APOBEC4 (human)

## Current model (mechanistic narrative)

APOBEC4 is an AID/APOBEC family member that, despite retaining the conserved zinc-coordinating deaminase domain motifs, has no demonstrated cytidine deaminase function in mammalian systems and instead acts as a transcriptional enhancer [PMID:21568845, PMID:27249646]. Ectopically expressed human APOBEC4 localizes predominantly to the cytoplasm, binds single-stranded DNA only weakly, and shows no detectable in vitro deamination activity; rather than restricting HIV-1, it enhances HIV-1 replication dose-dependently through the viral LTR and broadly stimulates transcription from diverse viral and mammalian promoters [PMID:27249646]. Consistent with the absence of catalytic activity, heterologous expression in yeast and bacteria is non-mutagenic [PMID:21568845]. A distinct activity is observed for the chicken ortholog, which inhibits Newcastle Disease Virus replication in avian cells [PMID:31991164], and human APOBEC4 has additionally been placed in the ribosome biogenesis pathway as a nucleolar factor [PMID:38976757]. Beyond these observations, the molecular mechanism by which APOBEC4 modulates transcription or supports ribosome biogenesis has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription)
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | Low | APOBEC4 was identified as a new subfamily of the AID/APOBEC family. Computational analysis showed that the zinc-coordinating motifs involved in catalysis and the secondary structure of the APOBEC4 deaminase domain are evolutionarily conserved across mammals, chicken, and frog, suggesting APOBEC4 proteins are active polynucleotide (deoxy)cytidine deaminases. APOBEC4 forms a distinct phylogenetic clade most closely related to APOBEC1. | PMID:16082223 | Cell cycle (Georgetown, Tex.) |
| 2011 | Medium | Expression of human APOBEC4 in yeast and bacteria was non-mutagenic, indicating that APOBEC4 does not function as an active DNA cytidine deaminase in these heterologous systems. The lack of mutagenic effect could not be explained by protein insolubility or peculiarities of cellular distribution. | PMID:21568845 | Biochemistry. Biokhimiia |
| 2016 | Medium | Ectopic expression of APOBEC4 in HeLa cells resulted in predominantly cytoplasmic localization. APOBEC4 did not show detectable cytidine deamination activity in vitro and only weakly interacted with single-stranded DNA. Instead of inhibiting HIV-1, APOBEC4 enhanced HIV-1 replication in a dose-dependent manner by acting on the viral LTR. APOBEC4 enhanced transcription from a broad spectrum of both viral and mammalian promoters. | PMID:27249646 | PloS one |
| 2020 | Medium | Chicken APOBEC4 (chA4) contains conserved zinc-coordinating catalytic motif residues (His97, Glu99, Pro130, Cys131, Cys138). Ectopic overexpression of chA4 in chicken cells inhibited Newcastle Disease Virus (NDV) replication and reduced viral RNA levels, demonstrating antiviral activity in an avian system. | PMID:31991164 | Developmental and comparative immunology |
| 2024 | Low | APOBEC4 was identified and validated as a novel ribosome biogenesis factor in human MCF10A cells. siRNA depletion of APOBEC4 impaired nucleolar function, placing APOBEC4 in the ribosome biogenesis pathway. | PMID:38976757 | PLoS biology |

## Citations

- PMID:16082223
- PMID:21568845
- PMID:27249646
- PMID:31991164
- PMID:38976757
