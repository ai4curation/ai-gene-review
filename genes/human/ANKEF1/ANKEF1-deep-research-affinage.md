---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKEF1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9NU02
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 3
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKEF1 (human)

## Current model (mechanistic narrative)

ANKEF1 (ANKRD5) is an axonemal protein required for sperm motility that maintains the structural integrity of flagellar doublet microtubules [PMID:41460250]. It is a component of the sperm axoneme that physically associates with the nexin-dynein regulatory complex (N-DRC) through calcium-independent interactions with its DRC5/TCTE1 and DRC4/GAS8 subunits [PMID:41460250]. Loss of ANKEF1 in mice causes male infertility and impaired sperm motility; cryo-electron tomography of knockout sperm shows a structurally intact 9+2 axoneme but with pronounced morphological variability and increased structural heterogeneity of doublet microtubules, while ATP, reactive oxygen species, and mitochondrial membrane potential are unaffected — placing ANKEF1 in N-DRC mechanical buffering between adjacent doublets rather than in energy metabolism [PMID:41460250]. In zebrafish, the ortholog Ankef1a localizes in a regionalized pattern along the proximal-distal axis of sensory hair-cell kinocilia, consistent with a broader role at motile/sensory ciliary axonemes [PMID:37367482]. Beyond these findings, no additional mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005929 cilium, GO:0005856 cytoskeleton
- **pathway (Reactome):** *(none)*
- **partners:** TCTE1, GAS8
- **complexes:** nexin-dynein regulatory complex (N-DRC)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2025 | High | ANKEF1 (ANKRD5) is a component of the sperm axoneme that physically interacts with DRC5/TCTE1 and DRC4/GAS8, two key components of the nexin-dynein regulatory complex (N-DRC), and these interactions occur independently of calcium regulation. Loss of ANKEF1 in mice causes impaired sperm motility and male infertility. Cryo-electron tomography of Ankef1-/- sperm revealed a structurally intact '9+2' axoneme with intact doublet microtubules (DMTs) but with pronounced morphological variability and increased structural heterogeneity of DMTs, suggesting ANKEF1 attenuates N-DRC mechanical buffering between adjacent DMTs under high mechanical stress during flagellar beating. ANKEF1 deficiency did not alter ATP levels, reactive oxygen species levels, or mitochondrial membrane potential. | PMID:41460250 | eLife |
| 2024 | Medium | ANKEF1 (ANKRD5) interacts with DRC5/TCTE1 and DRC4/GAS8 of the nexin-dynein regulatory complex (N-DRC) in the sperm axoneme, with interactions independent of calcium. Ankrd5-/- male mice are infertile with impaired sperm motility; cryo-electron tomography shows intact '9+2' structure but increased DMT morphological variability and structural heterogeneity without changes in ATP, ROS, or mitochondrial membrane potential. | PMID:bio_10.1101_2024.12.03.626701 | bioRxiv |
| 2023 | Medium | The zebrafish ortholog Ankef1a localizes to the kinocilia of hair cells in sensory organs, exhibiting a distinct regionalized localization pattern along the proximal-distal axis of the kinocilium and within the cell body, as demonstrated by transgenic fluorescently tagged protein expression. | PMID:37367482 | Journal of developmental biology |

## Citations

- PMID:37367482
- PMID:41460250
- PMID:bio_10.1101_2024.12.03.626701
