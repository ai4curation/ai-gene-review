---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGAP36
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q6ZRI8
self_evaluation_pairwise: tie
faith_pct: 71.42857142857143
n_discoveries: 9
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGAP36 (human)

## Current model (mechanistic narrative)

ARHGAP36 is an atypical RhoGAP-family protein that functions as a positive, Smoothened-independent regulator of Hedgehog (Gli) signaling, blocking Gli repressor formation and driving accumulation of full-length Gli proteins in the primary cilium in a manner requiring the ciliogenesis factors KIF3A and IFT88, alongside a functional and biochemical interaction with SUFU [PMID:25024229]. Its central mechanism is bimodal inhibition of the PKA catalytic subunit (PKAC): a pseudosubstrate motif directly blocks PKAC catalytic activity while ARHGAP36 also targets PKAC for ubiquitin-mediated lysosomal degradation, and this PKA inhibition alone is sufficient to derepress Hedgehog signaling [PMID:27713425]. ARHGAP36 is stabilized at the centrosome/mother centriole by Patched1, and upon Shh activation it is displaced, permitting centrosomal PKA to phosphorylate Inversin and promote Smoothened ciliary translocation [PMID:30598432]. Its Gli-activating output depends on specific residues of the GAP homology domain, is restrained by an N-terminal autoinhibitory motif relieved by the C-terminal domain, and is antagonized by the binding partner PREPL [PMID:33999959]. Expression is controlled developmentally and pathologically: the Isl1-Lhx3 complex induces ARHGAP36 downstream of Shh in motor neuron specification with AKT stabilizing the protein [PMID:31305241], and FOXC1 directly activates its expression to potentiate Hedgehog signaling and confer Smoothened-inhibitor resistance. Misexpression of ARHGAP36 underlies disease and trait phenotypes including heterotopic ossification via enhancer hijacking [PMID:37041138] and orange coat color in cats through PKAC depletion in melanocytes. Beyond Hedgehog, ARHGAP36 promotes entotic cell-in-cell formation by mutually exclusive binding of β-catenin (stabilizing P-cadherin) and PKAc (activating RhoA-regulated actomyosin contraction) [PMID:41644816].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0098772 molecular function regulator activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005815 microtubule organizing center, GO:0005929 cilium, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-5357801 Programmed Cell Death
- **partners:** PRKACA, SUFU, PTCH1, PREPL, CTNNB1, INVS
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | High | ARHGAP36 acts as a positive regulator of the Hedgehog pathway in a Smoothened-independent manner by inhibiting Gli repressor formation and promoting activation of full-length Gli proteins. It induces accumulation of Gli proteins in the primary cilium, and this activity requires KIF3A and IFT88 (ciliogenesis factors). ARHGAP36 also functionally and biochemically interacts with Suppressor of Fused (SUFU). | PMID:25024229 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | High | ARHGAP36 inhibits PKA (PKAC) via two distinct mechanisms: (1) a pseudosubstrate motif that directly blocks PKAC catalytic activity, analogous to the protein kinase inhibitor (PKI) proteins; and (2) targeting PKAC for ubiquitin-mediated lysosomal degradation. PKA inhibition by ARHGAP36 is sufficient to derepress the Hedgehog signaling pathway. | PMID:27713425 | Nature communications |
| 2018 | High | Patched1 interacts with and stabilizes ARHGAP36 at the centrosome/mother centriole. Upon Shh pathway activation, ARHGAP36 is removed from the mother centriole, leading to centrosomal PKA accumulation. This centrosomal PKA then phosphorylates Inversin, promoting Inversin interaction with Smoothened and its ciliary translocation. Knockdown of Inversin disrupts Smoothened ciliary translocation and Shh pathway activation. | PMID:30598432 | Proceedings of the National Academy of Sciences of the United States of America |
| 2019 | High | ARHGAP36 expression is directly induced by the motor neuron-specific transcription factor complex Isl1-Lhx3, placing ARHGAP36 downstream of Shh in lateral motor column (LMC) neuron specification. AKT kinase stabilizes ARHGAP36 protein levels, thereby stimulating Shh pathway activity and LMC neuron generation in the developing spinal cord. | PMID:31305241 | eLife |
| 2021 | Medium | Structure-activity mapping of ARHGAP36 revealed: (1) specific residues within the GAP homology domain are essential for Gli activation; (2) the C-terminal domain counteracts an N-terminal autoinhibitory motif present in certain ARHGAP36 isoforms; (3) these domains modulate ARHGAP36 recruitment to the plasma membrane or primary cilium; (4) prolyl oligopeptidase-like protein (PREPL) is a novel binding partner of active ARHGAP36 and acts as an ARHGAP36 antagonist. | PMID:33999959 | PloS one |
| 2023 | Medium | ARHGAP36 overexpression (caused by enhancer hijacking via chromosomal structural variant) inhibits TGFβ signaling and activates Hedgehog signaling and extracellular matrix-related genes/proteins in fibroblasts, leading to ectopic bone formation (heterotopic ossification). | PMID:37041138 | Nature communications |
| 2024 | Medium | Ectopic melanocyte-specific expression of Arhgap36 (caused by a 5 kb deletion acting as a regulatory element) leads to reduced PKA catalytic subunit (PKAC) protein levels in melanocytes, thereby dampening the MC1R–cAMP–PKA pathway and suppressing melanogenic gene expression, shifting pigment synthesis from eumelanin to pheomelanin (orange coat color in cats). This provides in vivo evidence that Arhgap36 inhibits PKA by reducing PKAC levels. | — | bioRxiv (preprint) |
| 2025 | Medium | FOXC1 (forkhead transcription factor) directly binds a locus in closed chromatin to induce ARHGAP36 expression, as shown by ChIP-sequencing and CRISPR interference. FOXC1-driven ARHGAP36 expression increases Hedgehog pathway activity by inhibiting PKA (a core Hh inhibitor) and impairing SUFU function, making the pathway resistant to Smoothened inhibitors. | — | bioRxiv (preprint) |
| 2026 | Medium | ARHGAP36 promotes entotic cell-in-cell formation by simultaneously (1) binding β-catenin via its N-terminal arginine-rich domain to stabilize P-cadherin expression (adherens junction) and (2) interacting with PKAc to activate RhoA-regulated actomyosin contraction. The interactions with β-catenin and PKAc are mutually exclusive, creating a bifurcate activation mechanism. | PMID:41644816 | Cell death and differentiation |

## Citations

- PMID:25024229
- PMID:27713425
- PMID:30598432
- PMID:31305241
- PMID:33999959
- PMID:37041138
- PMID:41644816
