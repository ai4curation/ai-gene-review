---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL16
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q0P5N6
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

# Affinage mechanistic annotation for ARL16 (human)

## Current model (mechanistic narrative)

ARL16 is an ARF-family GTPase that operates as a GTP-dependent regulatory switch in two distinct cellular contexts [PMID:21233210, PMID:35196065]. In innate immunity, GTP-loaded ARL16 binds the C-terminal domain of RIG-I and suppresses RIG-I association with viral RNA, thereby negatively regulating type I interferon signaling; GDP-restricted mutants (T37N, Δ45-54) fail to bind RIG-I or inhibit its signaling, establishing that nucleotide-dependent activation is required for both the interaction and its inhibitory function [PMID:21233210]. In ciliated cells, ARL16 is required for a Golgi-to-cilia trafficking pathway that specifically exports IFT140 and INPP5E to cilia: its loss reduces ciliogenesis, depletes ARL13B, ARL3, INPP5E, and IFT140 from cilia, and causes INPP5E and IFT140 to accumulate at the Golgi [PMID:35196065]. In this pathway ARL16 acts downstream of or in parallel with the ARF GAPs ELMOD1 and ELMOD3, since an activating ARL16 mutant rescues the ciliary defects of ELMOD1 or ELMOD3 deletion [PMID:34818063]. The biochemical mechanism linking these two roles and the direct effectors of ARL16 in cilia have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003924 GTPase activity
- **localization:** GO:0005794 Golgi apparatus, GO:0005929 cilium
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-5653656 Vesicle-mediated transport, R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** DDX58, ELMOD1, ELMOD3
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | ARL16 inhibits RIG-I innate immune signaling by binding the C-terminal domain (CTD) of RIG-I in a GTP-dependent manner, thereby suppressing the association between RIG-I and RNA. Mutants restricted to the GDP-bound form (T37N and Δ45-54) neither bind RIG-I nor inhibit its signaling, establishing that GTP loading is required for the interaction and inhibitory function. | PMID:21233210 | The Journal of biological chemistry |
| 2022 | High | ARL16 is required for ciliogenesis and for trafficking of IFT140 (an IFT-A core component) and INPP5E from the Golgi to cilia. Deletion of ARL16 in mouse embryonic fibroblasts (MEFs) decreases ciliogenesis yet increases ciliary length, causes loss of ARL13B, ARL3, INPP5E, and IFT140 from cilia, and leads to accumulation of INPP5E and IFT140 at the Golgi, indicating a specific defect in Golgi-to-cilia export of these cargoes. | PMID:35196065 | Molecular biology of the cell |
| 2021 | Medium | ARL16 acts downstream of or in parallel with ELMOD1 and ELMOD3 (ARF GAPs) in a Golgi-to-cilia trafficking pathway: expression of an activating mutant of ARL16 rescues the ciliogenesis and ciliary protein-traffic defects caused by deletion of either ELMOD1 or ELMOD3, placing ARL16 in the same pathway as these GAPs. | PMID:34818063 | Molecular biology of the cell |
| 2021 | Low | Phylogenetic analysis across 114 eukaryotic species provides evidence that ARL16 was present in the last eukaryotic common ancestor, indicating its ancient and wide distribution in eukaryotes as a member of the ARF GTPase family. | PMID:34247240 | Genome biology and evolution |

## Citations

- PMID:21233210
- PMID:34247240
- PMID:34818063
- PMID:35196065
