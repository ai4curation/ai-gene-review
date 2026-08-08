---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTMAP
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q5BKX5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 3
citation_count: 3
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTMAP (human)

## Current model (mechanistic narrative)

ACTMAP (C19orf54) is a dedicated cysteine protease that executes a noncanonical actin maturation step by excising the acetylated N-terminal methionine from cytoplasmic actin, a processing event required for the assembly of functional actin filaments [PMID:36173861]. Genetic ablation in mice yields viable animals whose cytoskeleton is built from immature, unprocessed actin across all tissues, establishing ACTMAP as the essential and specific protease for this step [PMID:36173861]. In skeletal muscle, loss of ACTMAP shortens sarcomeric actin filaments, decreases contractile function, and produces centralized nuclei characteristic of myopathy, demonstrating that ACTMAP-mediated N-terminal maturation is required for normal sarcomere architecture and muscle physiology [PMID:36173861]. Its catalytic mechanism rests on a cysteine nucleophile: covalent tryptoline butynamide stereoprobes that engage this cysteine inhibit ACTMAP and drive accumulation of unprocessed actin in human cancer cells, confirming both the protease classification and the essentiality of the active-site cysteine [PMID:42159598, PMID:41757055].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-397014 Muscle contraction
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | High | ACTMAP (C19orf54) was identified as the dedicated protease responsible for the noncanonical post-translational excision of the acetylated N-terminal methionine from cytoplasmic actin, a step required for actin maturation. Ablation of ACTMAP in mice produced viable animals whose cytoskeleton was composed of immature (unprocessed) actin molecules across all tissues, demonstrating its essential and specific role in actin maturation. | PMID:36173861 | Science |
| 2022 | High | Loss of ACTMAP in skeletal muscle resulted in shorter sarcomeric actin filaments, decreased muscle function, and progressive accumulation of centralized nuclei (a hallmark of myopathies), establishing that proper actin N-terminal maturation by ACTMAP is required for normal sarcomere architecture and muscle physiology. | PMID:36173861 | Science |
| 2026 | High | ACTMAP is a cysteine protease; its catalytic nucleophile (a cysteine residue) was directly engaged by (1S,3R)-tryptoline butynamide stereoprobes, which covalently inhibited ACTMAP and caused accumulation of N-terminally unprocessed actin in human cancer cells, confirming the catalytic mechanism and the essentiality of this cysteine for activity. | PMID:42159598, PMID:41757055 | Journal of the American Chemical Society |

## Citations

- PMID:36173861
- PMID:41757055
- PMID:42159598
