---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALDH16A1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8IZ83
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ALDH16A1 (human)

## Current model (mechanistic narrative)

ALDH16A1 is a catalytically inactive member of the aldehyde dehydrogenase superfamily that operates as a pseudoenzyme scaffold, exerting its biological effects through protein-protein interactions rather than enzymatic catalysis [PMID:30529746, PMID:40897711]. Although the bacterial ortholog ALDH16 is a bona fide NAD+-dependent enzyme, human ALDH16A1 lacks the essential catalytic cysteine and shows no measurable aldehyde oxidation activity while retaining the conserved ALDH dimer fold [PMID:30529746]. Functionally, ALDH16A1 binds directly to thioredoxin (TXN), occluding its active site to inhibit its oxidoreductase activity and facilitating TXN translocation to the lysosome for degradation; this axis lies downstream of SMARCA4, which opens chromatin at the ALDH16A1 locus to drive its expression and thereby sensitizes non-small-cell lung cancer cells to ferroptosis [PMID:40897711]. ALDH16A1 also physically interacts with the SPG21 protein maspardin/ACP33 and colocalizes with it in cells [PMID:19184135], and in mouse it localizes to renal proximal and distal tubule cells and zone-3 hepatocytes, where its loss dysregulates urate transporter expression and plasma lipid profiles, implicating it in uric acid homeostasis [PMID:28254523].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005764 lysosome
- **pathway (Reactome):** R-HSA-5357801 Programmed Cell Death
- **partners:** TXN, SPG21, SMARCA4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | Medium | ALDH16A1 physically interacts with the SPG21 protein maspardin (ACP33); this interaction was identified by immunoprecipitation of maspardin followed by mass spectrometry identification of coprecipitating proteins, confirmed by overexpressed-protein co-immunoprecipitation and fusion-protein pull-down, and the two proteins colocalize in cells. | PMID:19184135 | Neurogenetics |
| 2013 | Low | Human ALDH16A1 is predicted to lack aldehyde dehydrogenase catalytic activity because the essential catalytic cysteine (Cys-302 in bacterial/frog orthologs) is absent from mammalian and fish sequences. Molecular modeling further predicts that ALDH16A1 can interact with HPRT1 (hypoxanthine-guanine phosphoribosyltransferase) and that the gout-associated missense variant ALDH16A1*2 impairs this predicted interaction. | PMID:23348497 | Chemico-biological interactions |
| 2017 | Medium | In Aldh16a1 knockout mice, ALDH16A1 protein is localized to proximal and distal convoluted tubule cells of the kidney cortex and to zone-3 hepatocytes. Loss of ALDH16A1 dysregulates expression of urate transporters (up-regulation of Abcc4 and Slc16a9; down-regulation of Slc17a3) and alters plasma lipid profiles, implicating ALDH16A1 in renal uric acid homeostasis. | PMID:28254523 | Chemico-biological interactions |
| 2018 | High | Crystal structures of bacterial (Loktanella sp.) ALDH16 confirmed it is a bona fide enzyme with NAD+-binding, aldehyde oxidation, and esterase activities. In contrast, recombinant human ALDH16A1 lacks measurable aldehyde oxidation activity, consistent with absence of the catalytic Cys, establishing it as a pseudoenzyme. ALDH16 forms a unique dimer whose architecture mimics the classic ALDH superfamily dimer-of-dimer tetramer; small-angle X-ray scattering showed human ALDH16A1 shares the same dimer and overall fold. | PMID:30529746 | Journal of molecular biology |
| 2019 | Low | Recombinant Xenopus tropicalis ALDH16B1 (the frog homolog of human ALDH16A1, predicted to be catalytically active due to retention of the catalytic Cys) was expressed in Sf9 cells, purified, and crystallized, yielding diffraction data to 2.5 Å; structure determination was in progress at time of publication. | PMID:30894314 | Chemico-biological interactions |
| 2025 | High | ALDH16A1 binds directly to thioredoxin (TXN) and facilitates its translocation to the lysosome for degradation; simultaneously, ALDH16A1 directly inhibits TXN's oxidoreductase function by occluding its active site. SMARCA4 promotes chromatin accessibility at the ALDH16A1 locus to drive its expression, and the resulting ALDH16A1-mediated suppression of TXN sensitizes NSCLC cells to ferroptosis. | PMID:40897711 | Nature communications |

## Citations

- PMID:19184135
- PMID:23348497
- PMID:28254523
- PMID:30529746
- PMID:30894314
- PMID:40897711
