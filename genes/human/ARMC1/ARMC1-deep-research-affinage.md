---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NVT9
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

# Affinage mechanistic annotation for ARMC1 (human)

## Current model (mechanistic narrative)

ARMC1 is a dual-localized armadillo repeat-containing scaffold protein that partitions between the cytosol and the outer mitochondrial membrane to govern mitochondrial distribution and motility [PMID:31644573, PMID:40203102]. It associates with the outer membrane through its carboxy-terminus and behaves as a peripheral component of the MICOS/MIB complex; its loss fragments mitochondria and reduces their motility without disrupting cristae architecture, respiration, or protein content [PMID:31644573]. Mechanistically, ARMC1 partitions between two distinct mitochondrial complexes: it is recruited by the trafficking adaptor MIRO into a MIRO–ARMC1–MTFR complex in which ARMC1 mediates assembly and stability of the fission regulator MTFR and antagonizes retrograde mitochondrial movement, while a separate interaction with DNAJC11 facilitates ARMC1 release from mitochondria [PMID:40203102]. This DNAJC11-balanced mito-cytoplasmic shuttling sets steady-state mitochondrial positioning, such that ARMC1 deletion causes perinuclear mitochondrial clustering not rescued by disrupting MIRO–MTFR assembly alone, and disruption of the ARMC1–DNAJC11 interaction produces excess mitochondrial ARMC1 with distinct defects [PMID:40203102]. Consistent with a role in mitochondrial dynamics, ARMC1 overexpression shifts the fission/fusion balance toward fusion (lowering DRP1, raising OPA1 and MFN2), reduces ROS, and elevates antioxidant proteins in a kidney-cell injury model [PMID:41153008]. The C. elegans ortholog ARCP-1 acts as a dendritic scaffold that binds the phosphodiesterase PDE-1 and positions it with CO2 sensors in sensory neurons, shaping behavioral plasticity [PMID:31757604].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005739 mitochondrion, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** MIRO, MTFR, DNAJC11, PDE-1
- **complexes:** MICOS/MIB, MIRO-ARMC1-MTFR

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | Medium | ARMC1 localizes to both the cytosol and mitochondria, where it associates with the outer mitochondrial membrane through its carboxy-terminus, and interacts with components of the MICOS/MIB (mitochondrial intermembrane space bridging) complex. Mitochondria lacking ArmC1 appear fragmented and show reduced motility, but do not show defects in cristae structure, respiration, or protein content, indicating ArmC1 is a peripheral MICOS/MIB component with a role in mitochondrial distribution. | PMID:31644573 | PloS one |
| 2025 | High | ARMC1 partitions between two distinct mitochondrial protein complexes: (1) a MIRO-ARMC1-MTFR complex, where MIRO recruits ARMC1 which mediates assembly and stability of mitochondrial fission regulator MTFR, and this complex specifically antagonizes retrograde mitochondrial movement; and (2) a complex with DNAJC11, which facilitates ARMC1 release from mitochondria. ARMC1 deletion causes perinuclear mitochondrial clustering that cannot be rescued by disrupting MIRO-MTFR assembly alone, while disrupting the ARMC1-DNAJC11 interaction leads to excessive mitochondrially localized ARMC1 and distinct mitochondrial defects. Thus, ARMC1 mito-cytoplasmic shuttling balanced by DNAJC11 tunes steady-state mitochondrial distributions. | PMID:40203102 | Science advances |
| 2025 | Medium | MSC-conditioned media upregulates ARMC1 protein in TGF-β1-treated kidney cells and in adenine-induced nephropathy mouse renal tissue. ARMC1 overexpression reduces DRP1 (a fission regulator) and enhances OPA1 and MFN2 (fusion regulators), lowers ROS, and boosts mitochondrial bioactivity, suggesting ARMC1 inhibits mitochondrial fission and reduces oxidative stress. ARMC1 overexpression also decreases fibrosis markers and raises antioxidant proteins (NRF2, SOD1, SOD2, CAT). | PMID:41153008 | Stem cell research & therapy |
| 2019 | Medium | In C. elegans, the ARCP-1 protein (ortholog of ARMC1) is a polymorphic dendritic scaffold protein expressed in sensory neurons that binds the Ca2+-dependent phosphodiesterase PDE-1 and co-localizes PDE-1 with molecular sensors for CO2 at dendritic ends. Reducing ARCP-1 or PDE-1 activity promotes CO2 escape by altering neuropeptide expression in BAG CO2 sensors. Variation in ARCP-1 alters behavioral plasticity in multiple paradigms. | PMID:31757604 | Neuron |

## Citations

- PMID:31644573
- PMID:31757604
- PMID:40203102
- PMID:41153008
