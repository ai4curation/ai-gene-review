---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASPDH
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: A6ND91
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 2
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASPDH (human)

## Current model (mechanistic narrative)

ASPDH (aspartate dehydrogenase domain-containing protein) is a direct NAADP-binding protein that also functions as a metabolic suppressor of tumor progression in liver cancer. Biochemical purification from liver tissue together with isothermal titration calorimetry established that ASPDH binds NAADP with 1:1 stoichiometry and a Kd of ~455 nM, while the previously implicated NAADP receptors JPT2 and LSM12 showed no binding under the same conditions [PMID:35841763]. In liver cancer cells, ASPDH overexpression suppresses proliferation, migration, and invasion by lowering lactate secretion and dampening NF-κB/PD-L1 signaling; exogenous lactate restores nuclear p65 and PD-L1 and rescues the malignant phenotype, placing ASPDH upstream of lactate-driven NF-κB activity, with tumor suppression confirmed in xenografts [PMID:42127630]. Beyond NAADP binding and this lactate–NF-κB axis, the catalytic and structural mechanism of ASPDH has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | Medium | ASPDH (aspartate dehydrogenase domain-containing protein) was identified as a novel NAADP-binding protein. Biochemical purification from pig livers identified ASPDH, and isothermal titration calorimetry (ITC) with recombinant mouse ASPDH established a 1:1 binding stoichiometry with a Kd of 455 nM for NAADP. Previously identified NAADP-receptors JPT2 and LSM12 showed no binding in ITC experiments under the same conditions. | PMID:35841763 | Biochemical and biophysical research communications |
| 2026 | Medium | ASPDH overexpression in liver cancer cells suppressed proliferation, migration, and invasion by downregulating lactate secretion and suppressing the NF-κB/PD-L1 signaling pathway. Sodium lactate rescue experiments showed that exogenous lactate partially restored cell proliferation, migration, and invasion suppressed by ASPDH overexpression, and increased nuclear p65 and PD-L1 expression, placing ASPDH upstream of lactate-mediated NF-κB pathway activity. In vivo xenograft models confirmed suppressed tumor growth, decreased nuclear p65 and PD-L1, and reduced lactate secretion upon ASPDH overexpression. | PMID:42127630 | Clinics (Sao Paulo, Brazil) |

## Citations

- PMID:35841763
- PMID:42127630
