---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMIGO3
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q86WK7
self_evaluation_pairwise: win
faith_pct: 80.0
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

# Affinage mechanistic annotation for AMIGO3 (human)

## Current model (mechanistic narrative)

AMIGO3 is a type I transmembrane protein composed of six leucine-rich repeats flanked by cysteine-rich LRR-N and LRR-C caps and a single immunoglobulin domain, and it acts as a cell adhesion molecule capable of homophilic and heterophilic binding with other AMIGO family members [PMID:12629050]. It dimerizes through an LRR-LRR interface, a contact required for proper cell-surface expression and stable folding [PMID:21983541]. Functionally, AMIGO3 serves as a co-receptor within the NgR1/p75-TROY inhibitory signaling complex, where it substitutes for LINGO-1, binds NgR1 and p75/TROY, and transduces CNS myelin-derived inhibitory signals through RhoA/ROCK activation to suppress axon growth [PMID:23613963, PMID:34650403]. Loss of AMIGO3 disinhibits axon regeneration: shRNA knockdown in primary DRG and retinal neurons promotes neurite outgrowth under myelin-inhibitory conditions [PMID:23613963], and in vivo knockdown in dorsal root ganglion neurons restores NT3-stimulated dorsal column axon regeneration, compound action potential conduction, and sensory-locomotor function [PMID:30013050]. AMIGO3 is also upregulated after status convulsion and contributes to myelin sheath damage, with its downregulation relieving myelin ultrastructural impairment via ROCK/RhoA suppression [PMID:34650403].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity, GO:0060089 molecular transducer activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** RTN4R, NGFR, TROY, AMIGO1, AMIGO2
- **complexes:** NgR1/p75-TROY inhibitory receptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | Medium | AMIGO3 is a type I transmembrane protein with six leucine-rich repeats (LRRs) flanked by cysteine-rich LRR N- and C-terminal domains and one immunoglobulin domain; AMIGO family members engage in homophilic and heterophilic binding with each other, functioning as cell adhesion molecules. | PMID:12629050 | The Journal of cell biology |
| 2011 | Medium | AMIGO-3 (along with AMIGO-1 and AMIGO-2) forms dimers through LRR-LRR interfaces, as inferred from the crystal structure of AMIGO-1 and small-angle X-ray scattering (SAXS) data on AMIGO-3; dimerization is necessary for proper cell-surface expression and likely stable folding in the ER. | PMID:21983541 | Journal of molecular biology |
| 2013 | High | AMIGO3 acts as a co-receptor in the NgR1/p75-TROY inhibitory signaling complex, substituting for LINGO-1; AMIGO3 interacts physically with NgR1 and p75/TROY (demonstrated in non-neuronal cells and brain lysates), mediates RhoA activation in response to CNS myelin, and its knockdown in primary DRG and retinal cultures promotes neurite growth under myelin-inhibitory conditions. | PMID:23613963 | PloS one |
| 2018 | High | In vivo shRNA-mediated knockdown of AMIGO3 in dorsal root ganglion neurons (>75% mRNA reduction) disinhibits NT3-stimulated regeneration of spinal cord dorsal column axons, restores compound action potential conduction across the lesion, and improves sensory and locomotor function, confirming AMIGO3's role in mediating axon growth inhibition through the RhoA pathway in vivo. | PMID:30013050 | Scientific reports |
| 2021 | Medium | AMIGO3 expression is upregulated after status convulsion in immature mice and contributes to myelin sheath damage; downregulation of AMIGO3 alleviates myelin structural impairment (assessed by TEM and myelin basic protein levels) and inhibits the ROCK/RhoA signaling pathway, indicating AMIGO3 signals through ROCK/RhoA to regulate myelination and axon growth after seizure. | PMID:34650403 | Frontiers in molecular neuroscience |

## Citations

- PMID:12629050
- PMID:21983541
- PMID:23613963
- PMID:30013050
- PMID:34650403
