---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATG16L2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8NAA4
self_evaluation_pairwise: win
faith_pct: 100.0
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

# Affinage mechanistic annotation for ATG16L2 (human)

## Current model (mechanistic narrative)

ATG16L2 is an ATG16L1 paralog that participates in autophagy regulation and innate immune inflammasome control but, unlike ATG16L1, is dispensable for canonical autophagosome formation [PMID:22082872, PMID:35426127]. It binds ATG5 and self-oligomerizes into an ~800-kDa ATG12–ATG5–ATG16L2 complex analogous to the ATG12–5–16L1 complex, yet remains largely cytosolic and is not recruited to phagophores; chimeric analysis localizes this functional divergence from ATG16L1 to the middle coiled-coil region [PMID:22082872]. Rather than acting directly in autophagosome biogenesis, ATG16L2 positively modulates autophagy flux by promoting assembly of the canonical ATG5-12-16L1 complex, and its loss in macrophages attenuates LPS-induced autophagy, compromises mitochondrial integrity, and drives elevated NLRP3 inflammasome activation, sensitizing mice to DSS-induced colitis in an NLRP3-dependent manner [PMID:35426127]. In parallel, ATG16L2 binds NAIPs and enhances their association with NLRC4 to facilitate NLRC4 inflammasome activation, with its loss reducing ASC oligomerization and caspase-1/gasdermin D cleavage and impairing clearance of Salmonella typhimurium [PMID:39175123]. ATG16L2 expression is transcriptionally controlled by TRAF6/c-Jun signaling, and its knockdown induces autophagy and apoptosis in melanoma cells [PMID:37484971].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-9612973 Autophagy, R-HSA-168256 Immune System
- **partners:** ATG5, NAIP, NLRC4
- **complexes:** ATG12-ATG5-ATG16L2 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | ATG16L2 interacts with ATG5 and self-oligomerizes to form an ~800-kDa complex analogous to the ATG12–5-16L1 complex. Despite forming this complex, ATG16L2 is not recruited to phagophores and remains mostly cytosolic, and it cannot compensate for ATG16L1 in autophagosome formation. Knockdown of ATG16L2 did not affect autophagosome formation. Chimeric analysis mapped the functional difference between ATG16L1 and ATG16L2 entirely to their middle regions containing a coiled-coil domain (specifically residues 229–242 of ATG16L1). | PMID:22082872 | Autophagy |
| 2019 | Medium | ATG16L2 knockout mice reveal that ATG16L1 and ATG16L2 contribute distinctly to autophagy and cellular ontogeny in myeloid, lymphoid, and epithelial lineages. A novel genetic interaction between ATG16L2 and epithelial ATG16L1 was identified. | PMID:31451676 | Journal of immunology |
| 2022 | Medium | ATG16L2 deficiency attenuates LPS-induced autophagy flux in macrophages by impairing ATG5-12-16L1 complex assembly, indicating ATG16L2 positively regulates the canonical autophagy complex. ATG16L2-deficient macrophages show elevated NLRP3 inflammasome activation and defects in mitochondrial integrity and respiration. ATG16L2 knockout mice are more susceptible to DSS-induced intestinal damage, which is ameliorated by NLRP3 inhibition. | PMID:35426127 | European journal of immunology |
| 2023 | Medium | TRAF6 regulates ATG16L2 expression through the transcription factor c-Jun; knockdown of TRAF6 reduces ATG16L2 mRNA levels, and ATG16L2 knockdown itself induces increased autophagy and apoptosis in melanoma cells. | PMID:37484971 | MedComm |
| 2024 | Medium | ATG16L2 interacts with NAIPs (neuronal apoptosis inhibitory proteins) via co-immunoprecipitation and enhances the association between NAIPs and NLRC4, thereby facilitating NLRC4 inflammasome activation. ATG16L2-deficient macrophages show reduced NLRC4 inflammasome activation (decreased ASC oligomerization, attenuated Pro-caspase-1, Pro-IL-1β, and gasdermin D cleavage). ATG16L2 knockout mice show impaired pathogen clearance and survival after Salmonella typhimurium infection. | PMID:39175123 | European journal of immunology |

## Citations

- PMID:22082872
- PMID:31451676
- PMID:35426127
- PMID:37484971
- PMID:39175123
