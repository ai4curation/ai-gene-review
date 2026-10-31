---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALPK2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q86TB3
self_evaluation_pairwise: win
faith_pct: 75.0
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

# Affinage mechanistic annotation for ALPK2 (human)

## Current model (mechanistic narrative)

ALPK2 is an atypical alpha-protein kinase with context-dependent roles in cardiac biology and tumor cell growth. During cardiogenesis it acts as a negative regulator of WNT/β-catenin signaling: loss of ALPK2 in hESCs and zebrafish stabilizes β-catenin and elevates WNT activity, and the resulting cardiac defects are rescued by pharmacological WNT inhibition [PMID:29888752]. This essential cardiogenic function is not conserved in mouse, where two independent global Alpk2 knockouts show normal cardiac development and unaltered WNT signaling [PMID:32383995]. In the adult mammalian heart, ALPK2 instead operates in cardiomyocytes to regulate diastolic function by phosphorylating tropomyosin 1, with cardiomyocyte-specific deletion worsening diastolic dysfunction in aging and HFpEF and overexpression reducing cardiac stiffness [PMID:39556326]. In cancer contexts, ALPK2 supports proliferation, migration, and survival; it physically interacts with DEPDC1A, and DEPDC1A re-expression rescues the anti-proliferative, pro-apoptotic effects of ALPK2 knockdown in bladder cancer cells, placing DEPDC1A downstream of ALPK2 [PMID:34210956].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** DEPDC1A, TPM1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2018 | High | ALPK2 acts as a negative regulator of WNT/β-catenin signaling during cardiogenesis; loss of ALPK2 (by siRNA knockdown or CRISPR/Cas9 mutagenesis) leads to stabilization of β-catenin and increased WNT signaling, and cardiac defects can be rescued dose-dependently by direct WNT inhibition with XAV939. | PMID:29888752 | iScience |
| 2020 | High | In mouse, global Alpk2 knockout (two independent CRISPR/Cas9 lines) does not produce cardiac morphological or functional defects up to one year of age, and WNT signaling is not altered in neonatal Alpk2-KO hearts, indicating that ALPK2 is dispensable for cardiac development and function in mammals. | PMID:32383995 | American Journal of Physiology. Heart and Circulatory Physiology |
| 2021 | Medium | ALPK2 directly interacts with DEPDC1A (identified as a downstream target); knockdown of ALPK2 suppresses bladder cancer cell proliferation, migration, and promotes apoptosis, and overexpression of DEPDC1A rescues these inhibitory effects, placing DEPDC1A downstream of ALPK2. | PMID:34210956 | Cell Death & Disease |
| 2020 | Low | ALPK2 knockdown in renal cell carcinoma cells inhibits proliferation, colony formation, and migration while promoting apoptosis; downstream regulation involves Akt, CDK6, Cyclin D1, and PIK3CA signaling pathways. | PMID:32330508 | Experimental Cell Research |
| 2020 | Low | ALPK2 knockdown in ovarian cancer cells inhibits proliferation, induces cell cycle arrest, promotes apoptosis, and reduces migration; associated with regulation of EMT-related proteins (N-cadherin, Vimentin, Snail), anti-apoptotic proteins (Bcl-2, Bcl-w, Survivin, XIAP), and Akt/PI3K/Cyclin D1/CDK6 pathway components. | PMID:32595416 | Cancer Cell International |
| 2024 | Medium | Cardiomyocyte-specific Alpk2 deficiency (tamoxifen-inducible KO mice) exacerbates cardiac diastolic dysfunction in aging and HFpEF models without affecting systolic function; Alpk2 overexpression increases phosphorylation of tropomyosin 1 and mitigates cardiac stiffness in HFpEF, identifying tropomyosin 1 as a substrate of ALPK2 relevant to diastolic regulation. | PMID:39556326 | FASEB Journal |

## Citations

- PMID:29888752
- PMID:32330508
- PMID:32383995
- PMID:32595416
- PMID:34210956
- PMID:39556326
