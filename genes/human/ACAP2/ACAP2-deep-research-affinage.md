---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACAP2
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q15057
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACAP2 (human)

## Current model (mechanistic narrative)

ACAP2 (centaurin-β2) is an ARF6 GTPase-activating protein that operates as a downstream effector of GTP-bound Rab35 to locally inactivate Arf6 and thereby couple membrane trafficking to actin-dependent cellular remodeling [PMID:22344257, PMID:22045739]. Rab35 accumulates at Arf6-positive endosomes and the phagocytic cup and recruits ACAP2 in a GTP-Rab35-dependent manner, and ACAP2's Arf6-GAP activity at these sites drives NGF-induced neurite outgrowth and FcγR-mediated phagosome formation [PMID:22344257, PMID:22045739]. This Rab35–ACAP2–Arf6 axis is also deployed as a negative regulator of oligodendrocyte differentiation and myelination, where ACAP2 opposes the Arf6-GEF cytohesin-2 [PMID:24600047]. The direct Rab35–ACAP2 interaction is highly specific, requiring Thr-76/Thr-81 in the Rab35 switch II region and Asn-610/Asn-691 within the minimal Rab35-binding domain of ACAP2, and binding-deficient mutants of either protein fail to support neurite outgrowth [PMID:25694427]. Independent of its GAP function, ACAP2 (the human homolog of C. elegans CNT-1) carries a phosphoinositide-binding-dependent pro-apoptotic activity, as its knockdown blocks 5-fluorouracil-induced apoptosis [PMID:25853217]. ACAP2 protein levels are set by ubiquitin-mediated proteasomal degradation through the E3 ligase RNF126 [PMID:40251363].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity, GO:0008289 lipid binding
- **localization:** GO:0005768 endosome, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-1266738 Developmental Biology, R-HSA-168256 Immune System, R-HSA-5357801 Programmed Cell Death
- **partners:** RAB35, ARF6, RNF126, K1L
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2012 | High | ACAP2 (centaurin-β2) functions as a Rab35 effector and as an Arf6-GAP during neurite outgrowth. Rab35 accumulates at Arf6-positive endosomes in response to NGF stimulation and recruits ACAP2 to the same compartment; the Arf6-GAP activity of ACAP2 at these endosomes is indispensable for NGF-induced neurite outgrowth in PC12 cells. | PMID:22344257 | Journal of cell science |
| 2011 | High | During FcγR-mediated phagocytosis in macrophages, Rab35 recruits ACAP2 (an ARF6-GAP) to the phagocytic cup in a GTP-Rab35-dependent manner; ACAP2 recruitment downstream of Rab35 controls actin-dependent phagosome formation, and co-overexpression of ACAP2 with GTP-locked Rab35 synergistically inhibits phagocytosis. | PMID:22045739 | Journal of cell science |
| 2014 | High | ACAP2, acting as an Arf6-GAP downstream of Rab35, negatively regulates oligodendrocyte morphological differentiation and myelination; ACAP2 knockdown promotes differentiation and myelination, while Arf6 (which ACAP2 inactivates) is required for differentiation. Cytohesin-2 (a GEF for Arf6) opposes ACAP2/Rab35 in this pathway. | PMID:24600047 | Molecular biology of the cell |
| 2015 | High | Thr-76 and Thr-81 in the switch II region of Rab35 are required for binding ACAP2, and are dispensable for binding other Rab35-binding proteins. Asn-610 and Asn-691 in ACAP2's minimal Rab35-binding domain are key residues for specific Rab35 recognition. Neither Rab35(T76S/T81A) nor ACAP2(N610A/N691A) binding-deficient mutants support neurite outgrowth, confirming the functional significance of the direct Rab35–ACAP2 interaction. | PMID:25694427 | The Journal of biological chemistry |
| 2015 | Medium | ACAP2, the human homolog of C. elegans CNT-1, has a pro-apoptotic function and shares an identical phosphoinositide-binding pattern with tCNT-1. Knockdown of ACAP2 blocks apoptosis in cancer cells in response to 5-fluorouracil treatment. | PMID:25853217 | Cell cycle (Georgetown, Tex.) |
| 2006 | Medium | Vaccinia virus K1L protein binds ACAP2 (an ARF6-GAP); however, ANK mutations that abolish VV replication in human or rabbit cells do not affect K1L's ability to bind ACAP2, indicating that ACAP2 binding is separable from the host-range function of K1L. | PMID:16806385 | Virology |
| 2025 | Medium | RNF126 (a ubiquitin E3 ligase) physically interacts with ACAP2 and promotes its ubiquitination and proteasomal degradation, thereby reprogramming lipid metabolism and promoting ovarian cancer progression. ACAP2 protein stability is negatively regulated by RNF126. | PMID:40251363 | Biochemical genetics |

## Citations

- PMID:16806385
- PMID:22045739
- PMID:22344257
- PMID:24600047
- PMID:25694427
- PMID:25853217
- PMID:40251363
